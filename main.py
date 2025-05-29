from src.feature_engineering import build_features
from utils.ploting import plot_mutation_distribution
import pandas as pd
from config import *


def main():
    train_df = pd.read_csv(TRAIN_FILE)
    train_features = build_features(train_df)

    test_df = pd.read_csv(TEST_FILE)
    test_features = build_features(test_df)

    # section a + b)
    # features = build_features(train_df)

    # section c)
    plot_mutation_distribution(train_df, test_df)
if __name__ == "__main__":
    main()