import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    read csv return the data frame
    index=false to get rid of row number
    """
    try:
        df = pd.read_csv(path)
        print('Loading dataset of dimensions', df.shape)
        return df.to_string(index=False)
    except FileNotFoundError:
        print("FileNotFoundError: no such file or directory:", path)
