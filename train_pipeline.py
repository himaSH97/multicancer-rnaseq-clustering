import json
import os
import pandas as pd
import joblib

from src.load_data import load_data
from src.preprocess import clean_data, transpose_data, scale_data
from src.pca import run_pca
from src.clustering import run_kmeans
from src.labeling import extract_labels, filter_unknown
from src.analysis import (
    cluster_composition,
    category_distribution,
    dominant_cluster_info
)
from src.visualization import (
    plot_pca,
    plot_cluster_composition,
    plot_category_distribution
)
from src.visualization import plot_pca_3d, save_table_as_png


def main():
    # ===== load config =====
    with open("config/config.json", "r") as f:
        config = json.load(f)

    # ===== load data =====
    df = load_data(config["data_path"])

    # ===== clean data =====
    df = clean_data(df)

    # ===== feature selection (top variable genes) =====
    variances = df.var(axis=1)
    top_genes = variances.sort_values(ascending=False)\
                         .head(config["n_top_genes"]).index
    df_filtered = df.loc[top_genes]

    # ===== extract labels (before transpose) =====
    labels = extract_labels(df_filtered.columns)

    # ===== transpose (samples as rows) =====
    X = transpose_data(df_filtered)

    # ===== remove unknown samples BEFORE modeling =====
    X, labels = filter_unknown(X, labels)

    # ===== scaling =====
    X_scaled, scaler = scale_data(X)

    # ===== PCA =====
    X_pca, pca = run_pca(X_scaled, config["pca_components"])

    # ===== clustering =====
    clusters, kmeans = run_kmeans(
        X_pca,
        config["n_clusters"],
        config["random_state"]
    )

    # ===== analysis =====
    cluster_pct = cluster_composition(clusters, labels)
    category_pct = category_distribution(clusters, labels)
    cluster_summary = dominant_cluster_info(cluster_pct)

    # ===== create folders =====
    os.makedirs("models", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    # ===== save models =====
    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(pca, "models/pca.pkl")
    joblib.dump(kmeans, "models/kmeans.pkl")

    # ===== save results =====
    pd.DataFrame(X_pca).to_csv("results/pca.csv", index=False)
    pd.DataFrame({"cluster": clusters}).to_csv("results/clusters.csv", index=False)
    pd.DataFrame({
    "cluster": clusters,
    "label": labels
    }).to_csv("results/metadata.csv", index=False)

    cluster_pct.to_csv("results/cluster_percentages.csv")
    category_pct.to_csv("results/category_distribution.csv")
    cluster_summary.to_csv("results/cluster_summary.csv")

    os.makedirs("results/plots", exist_ok=True)

    plot_pca("results/pca.csv", "results/clusters.csv")
    plot_cluster_composition("results/cluster_percentages.csv")
    plot_category_distribution("results/category_distribution.csv")
    plot_pca_3d("results/pca.csv", "results/metadata.csv")

    save_table_as_png(
    "results/cluster_percentages.csv",
    "results/plots/cluster_composition_table.png",
    "Cluster Composition (%)"
    )
    save_table_as_png(
        "results/category_distribution.csv",
        "results/plots/category_distribution_table.png",
        "Category Distribution (%)"
    )

    print("✅ Training complete. Models and results saved.")


if __name__ == "__main__":
    main()