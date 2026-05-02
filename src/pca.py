from sklearn.decomposition import PCA


def run_pca(X_scaled, n_components):
    """
    Fit PCA and transform data.

    Returns:
        X_pca, pca_model
    """
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)

    return X_pca, pca