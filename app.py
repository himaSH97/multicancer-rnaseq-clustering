import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("📊 Gene Expression Analysis Results\n")

    # ===== Load results =====
    cluster_summary = pd.read_csv("results/cluster_summary.csv", index_col=0)
    cluster_pct = pd.read_csv("results/cluster_percentages.csv", index_col=0)
    category_pct = pd.read_csv("results/category_distribution.csv", index_col=0)

    # ===== Display summaries =====
    print("🔹 Cluster Summary (Dominant Cancer per Cluster):")
    print(cluster_summary)
    print("\n")

    print("🔹 Cluster Composition (%):")
    print(cluster_pct)
    print("\n")

    print("🔹 Category Distribution (%):")
    print(category_pct)
    print("\n")

    # ===== Show plots =====
    try:
        pca_img = plt.imread("results/plots/pca_plot.png")
        comp_img = plt.imread("results/plots/cluster_composition.png")
        dist_img = plt.imread("results/plots/category_distribution.png")

        plt.figure(figsize=(12, 8))

        plt.subplot(2, 2, 1)
        plt.imshow(pca_img)
        plt.title("PCA Plot")
        plt.axis("off")

        plt.subplot(2, 2, 2)
        plt.imshow(comp_img)
        plt.title("Cluster Composition")
        plt.axis("off")

        plt.subplot(2, 2, 3)
        plt.imshow(dist_img)
        plt.title("Category Distribution")
        plt.axis("off")

        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("⚠️ Plots not found. Run train_pipeline.py first.")


if __name__ == "__main__":
    main()