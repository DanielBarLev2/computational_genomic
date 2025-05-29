from __future__ import annotations
import pandas as pd
from config import *


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build a per-patient feature matrix from raw mutation rows.

    silent_frac captures the regulatory mutational load, which has shown
    predictive value in cancer subtype classification.
    del_ratio reflects enrichment of deletions, known to be over-represented
    in cancer-relevant features. Both are dense and compact signal boosters.

    :return: Returned columns:
               total_mutations  - scalar count
               type_<class> - counts for every Variant_Classification
               gene_<symbol> - counts for every Gene_name
               silent_frac - silent_mutations / total_mutations
               del_ratio - deletions / total_mutations

               # All features are numeric; missing values are filled with 0
    """
    total_mutations = df.groupby('case_id').size().rename('total_mutations')

    type_counts = pd.crosstab(index=df['case_id'], columns=df['Variant_Classification']).add_prefix('type_')

    gene_counts = pd.crosstab(index=df['case_id'], columns=df['Gene_name']).add_prefix('gene_')

    # silent frac captures the regulatory mutational
    silent_mask = df["Variant_Classification"].isin(SILENT_CLASSES)
    silent_counts = (df[silent_mask].groupby("case_id").size().reindex(total_mutations.index, fill_value=0))
    silent_frac = (silent_counts / total_mutations).rename("silent_frac")

    # Detect deletions by allele length: ref > alt ⇒ bases deleted in tumour.
    alt2 = df["Tumor_Seq_Allele2"].fillna("").str.upper()
    ref = df["Reference_Allele"].fillna("").str.upper()
    del_mask = (alt2 == "-") | (ref.str.len() > alt2.str.len())

    del_counts = (df[del_mask].groupby("case_id").size().reindex(total_mutations.index, fill_value=0))
    del_ratio = (del_counts / total_mutations).rename("del_ratio")

    features = pd.concat([total_mutations, type_counts, gene_counts, silent_frac, del_ratio], axis=1)

    return features
