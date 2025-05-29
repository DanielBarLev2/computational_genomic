import pandas as pd
import matplotlib.pyplot as plt
from config import *


def plot_mutation_distribution(train_df: pd.DataFrame, test_df: pd.DataFrame) -> None:
    """
    Create and save a bar plot showing mutation counts by Variant_Classification
    in a specified order (TCGA-style). Combines train and test datasets.
    """
    out_file = PLOT_DIR / "mutation_types_ordered.png"
    PLOT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.concat([train_df, test_df], ignore_index=True)

    mask = df["Group"] = df["Variant_Classification"].isin(GROUP_MAP)
    df_filtered = df[mask]

    counts = (df_filtered["Variant_Classification"]
              .value_counts()
              .reindex(GROUP_MAP, fill_value=0)
              .rename_axis("VC")
              .reset_index(name="Count"))

    plt.figure(figsize=(12, 5))
    plt.bar(counts["VC"], counts["Count"])
    plt.xticks(rotation=60, ha="right")
    plt.ylabel("Mutation Count")
    plt.title("Mutation types in specified order (GROUP_MAP)")
    plt.tight_layout()
    plt.show()
    plt.savefig(out_file, dpi=150)
    print(f"Plot saved to: {out_file}")
