import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def plot_pca(pca_path, cluster_path):
    """
    PCA scatter plot colored by cluster
    """
    pca = pd.read_csv(pca_path)
    clusters = pd.read_csv(cluster_path)

    plt.figure(figsize=(6, 5))
    plt.scatter(
        pca.iloc[:, 0],
        pca.iloc[:, 1],
        c=clusters["cluster"],
        alpha=0.7
    )

    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("PCA Plot (Clusters)")
    plt.colorbar(label="Cluster")

    plt.tight_layout()
    plt.savefig("results/plots/pca_plot.png")
    plt.close()


def plot_cluster_composition(path):
    """
    Cluster → cancer % (stacked bar)
    """
    df = pd.read_csv(path, index_col=0)

    plt.figure(figsize=(8, 5))
    df.plot(kind="bar", stacked=True)

    plt.title("Cluster Composition (%)")
    plt.ylabel("Percentage")
    plt.xlabel("Cluster")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.tight_layout()
    plt.savefig("results/plots/cluster_composition.png")
    plt.close()


def plot_category_distribution(path):
    """
    Cancer → cluster % (stacked bar)
    """
    df = pd.read_csv(path, index_col=0)

    plt.figure(figsize=(8, 5))
    df.plot(kind="bar", stacked=True)

    plt.title("Category Distribution Across Clusters (%)")
    plt.ylabel("Percentage")
    plt.xlabel("Cancer Type")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.tight_layout()
    plt.savefig("results/plots/category_distribution.png")
    plt.close()

def plot_pca_3d(pca_path, metadata_path):
    import pandas as pd
    import plotly.express as px

    pca = pd.read_csv(pca_path)
    meta = pd.read_csv(metadata_path)

    # ===== count categories =====
    counts = meta["label"].value_counts().to_dict()

    # ===== create label with count =====
    meta["label_with_count"] = meta["label"].apply(
        lambda x: f"{x} ({counts[x]})"
    )

    # ===== combine =====
    df = pd.DataFrame({
        "PC1": pca.iloc[:, 0],
        "PC2": pca.iloc[:, 1],
        "PC3": pca.iloc[:, 2],
        "Type": meta["label_with_count"]
    })

    # ===== plot =====
    fig = px.scatter_3d(
        df,
        x="PC1",
        y="PC2",
        z="PC3",
        color="Type",
        title="3D PCA (with Category Counts)"
    )

    fig.write_html("results/plots/pca_3d.html")

def save_table_as_png(csv_path, output_path, title):


    df = pd.read_csv(csv_path, index_col=0)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis("tight")
    ax.axis("off")

    table = ax.table(
        cellText=df.round(2).values,
        colLabels=df.columns,
        rowLabels=df.index,
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.5)

    plt.title(title)
    plt.tight_layout()

    plt.savefig(output_path, dpi=300)
    plt.close()