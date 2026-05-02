import pandas as pd


def cluster_composition(clusters, labels):
    """
    % of each cancer type inside each cluster

    Returns:
        DataFrame (clusters as rows)
    """
    df = pd.DataFrame({
        "Cluster": clusters,
        "Type": labels
    })

    counts = pd.crosstab(df["Cluster"], df["Type"])
    percentages = counts.div(counts.sum(axis=1), axis=0) * 100

    return percentages


def category_distribution(clusters, labels):
    """
    % of each cancer type distributed across clusters

    Returns:
        DataFrame (types as rows)
    """
    df = pd.DataFrame({
        "Cluster": clusters,
        "Type": labels
    })

    counts = pd.crosstab(df["Type"], df["Cluster"])
    percentages = counts.div(counts.sum(axis=1), axis=0) * 100

    return percentages


def dominant_cluster_info(cluster_percentages):
    """
    Add dominant cancer type and percentage per cluster
    """
    result = cluster_percentages.copy()

    # ensure only numeric columns are used
    numeric_cols = result.select_dtypes(include="number").columns

    result["Max_Type"] = result[numeric_cols].idxmax(axis=1)
    result["Max_%"] = result[numeric_cols].max(axis=1)

    return result