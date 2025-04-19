import pandas as pd

def load_bottle_dataset(path="data/Copy of 501 Bottle Dataset - Sheet1.csv"):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        raise Exception(f"Error loading bottle dataset: {e}")
