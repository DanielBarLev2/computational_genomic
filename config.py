from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
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
