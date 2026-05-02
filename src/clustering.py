from sklearn.cluster import KMeans


def run_kmeans(X_pca, n_clusters, random_state=42):
    """
    Fit KMeans clustering.

    Returns:
        clusters, kmeans_model
    """
    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=random_state
    )

    clusters = kmeans.fit_predict(X_pca)

    return clusters, kmeans