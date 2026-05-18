from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_PATH = Path("data/assurance-maladie.csv")
REPORTS_PATH = Path("reports")
FIGURES_PATH = REPORTS_PATH / "figures"


def load_dataset():
    return pd.read_csv(DATA_PATH)


def save_chart(output_path):
    """
    Save the current matplotlib figure and close it.
    """
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def main():
    df = load_dataset()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    execution_folder = FIGURES_PATH / f"eda_charts_{timestamp}"
    execution_folder.mkdir(parents=True, exist_ok=True)

    sns.set_style("whitegrid")

    numerical_columns = ["age", "bmi", "children", "charges"]

    # =========================
    # HISTOGRAMS
    # =========================
    for column in numerical_columns:
        plt.figure(figsize=(8, 5))

        sns.histplot(df[column], kde=True)

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        save_chart(execution_folder / f"histogram_distribution_{column}.png")

    # =========================
    # BOXPLOTS
    # =========================
    for column in numerical_columns:
        plt.figure(figsize=(8, 5))

        sns.boxplot(x=df[column])

        plt.title(f"Boxplot of {column}")

        save_chart(execution_folder / f"boxplot_outliers_{column}.png")

    # =========================
    # SMOKER VS CHARGES
    # =========================
    plt.figure(figsize=(8, 5))

    sns.boxplot(x="smoker", y="charges", data=df)

    plt.title("Charges by Smoker Status")
    plt.xlabel("Smoker")
    plt.ylabel("Charges")

    save_chart(execution_folder / "boxplot_charges_by_smoker_status.png")

    # =========================
    # BMI VS CHARGES
    # =========================
    plt.figure(figsize=(8, 5))

    sns.scatterplot(x="bmi", y="charges", hue="smoker", data=df)

    plt.title("BMI vs Charges by Smoker Status")
    plt.xlabel("BMI")
    plt.ylabel("Charges")

    save_chart(execution_folder / "scatterplot_bmi_vs_charges_by_smoker.png")

    # =========================
    # CORRELATION HEATMAP
    # =========================
    correlation = df[["age", "bmi", "children", "charges"]].corr()

    plt.figure(figsize=(8, 6))

    sns.heatmap(correlation, annot=True, cmap="coolwarm")

    plt.title("Correlation Heatmap")

    save_chart(execution_folder / "heatmap_correlation_numeric_features.png")

    # =========================
    # ZIP GENERATED IMAGES
    # =========================
    zip_path = REPORTS_PATH / f"eda_charts_{timestamp}.zip"

    with ZipFile(zip_path, "w") as zip_file:
        for image_path in execution_folder.glob("*.png"):
            zip_file.write(image_path, arcname=image_path.name)

    print("\n✅ EDA charts generated successfully.")
    print(f"📁 Images folder: {execution_folder}")
    print(f"🗜️ ZIP file: {zip_path}")


if __name__ == "__main__":
    main()