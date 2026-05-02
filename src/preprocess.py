import pandas as pd
from sklearn.preprocessing import StandardScaler


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert all values to numeric and remove invalid rows.
    """
    df = df.apply(pd.to_numeric, errors="coerce")
    df = df.dropna(how="all")  # remove completely empty rows
    return df


def transpose_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transpose data so rows = samples, columns = genes.
    """
    return df.T


def scale_data(X: pd.DataFrame):
    """
    Standardize features using StandardScaler.

    Returns:
        X_scaled, scaler
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler