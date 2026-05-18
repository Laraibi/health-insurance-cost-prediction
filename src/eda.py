from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/assurance-maladie.csv")


def load_dataset():
    df = pd.read_csv(DATA_PATH)
    return df


def main():
    df = load_dataset()

    print("\n================ DATASET OVERVIEW ================\n")

    # Shape
    print("Dataset shape:")
    print(df.shape)

    # Columns
    print("\nColumns:")
    print(df.columns.tolist())

    # Data types
    print("\nData types:")
    print(df.dtypes)

    # Missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Duplicates
    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    # Statistical summary
    print("\nStatistical summary:")
    print(df.describe())

    # Categorical columns analysis
    categorical_columns = ["sex", "smoker", "region"]

    for column in categorical_columns:
        print(f"\nValue counts for '{column}':")
        print(df[column].value_counts())


if __name__ == "__main__":
    main()