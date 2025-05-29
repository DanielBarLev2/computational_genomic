from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
PLOT_DIR = PROJECT_ROOT / "plots"
TRAIN_FILE = DATA_DIR / "muts" / "train_muts_data.csv"
TEST_FILE = DATA_DIR / "muts" / "test_muts_data.csv"
GENE_LIST = DATA_DIR / "100_genes.csv"

SILENT_CLASSES = {"Silent",
                  "Synonymous",
                  "Intron",
                  "3'UTR",
                  "5'UTR",
                  "IGR",
                  "Flank",
                  "FlankNC"}

# All others -> Non-silent
GROUP_MAP = [
    "Missense_Mutation",
    "In_Frame_Del",
    "Nonsense_Mutation",
    "Frame_Shift_Del",
    "Frame_Shift_Ins",
    "In_Frame_Ins",
    "Translation_Start_Site",
    "Nonstop_Mutation",
    "Splice_Region",
    "3'UTR",
    "5'UTR",
    "Intron",
    "Splice_Site",
    "Silent",
    "3'Flank",
    "5'Flank"
]

