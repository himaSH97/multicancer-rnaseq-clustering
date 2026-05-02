import numpy as np


def extract_labels(column_names):
    """
    Extract cancer type labels from sample names.

    Parameters:
        column_names (list or array): df.columns

    Returns:
        np.array: cleaned labels
    """
    labels = []

    for name in column_names:
        name_lower = str(name).lower()

        if "breast" in name_lower or "brca" in name_lower:
            labels.append("Breast")

        elif "lung" in name_lower or "nsclc" in name_lower:
            labels.append("Lung")

        elif "crc" in name_lower:
            labels.append("CRC")

        elif "gbm" in name_lower:
            labels.append("GBM")

        elif "pancr" in name_lower or "panc" in name_lower:
            labels.append("Pancreatic")

        elif "liver" in name_lower or "chol" in name_lower:
            labels.append("Liver")

        elif "hd" in name_lower or "control" in name_lower:
            labels.append("Healthy")

        else:
            labels.append("Unknown")

    return np.array(labels)


def filter_unknown(X, labels):
    """
    Remove samples labeled as Unknown.

    Returns:
        X_filtered, labels_filtered
    """
    mask = labels != "Unknown"

    X_filtered = X[mask]
    labels_filtered = labels[mask]

    return X_filtered, labels_filtered