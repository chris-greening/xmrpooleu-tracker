import pandas as pd

BLOCKS_FPATH = "blocks.csv"

def process_dataframe(df):
    df["Time Found"] = pd.to_datetime(df["Time Found"], format="%m/%d/%Y, %I:%M:%S %p")
    return df

if __name__ == "__main__":
    df = pd.read_csv(BLOCKS_FPATH)
    df = process_dataframe(df)
