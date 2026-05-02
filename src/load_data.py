import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load gene expression dataset from file.

    Parameters:
        file_path (str): Path to dataset file

    Returns:
        pd.DataFrame: Raw dataframe
    """
    df = pd.read_csv(file_path, sep="\t")

    # set first column as gene IDs (index)
    df = df.set_index(df.columns[0])

    return df