from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

from src.feature_engineering import build_features
from utils.ploting import plot_mutation_distribution
import pandas as pd
from config import *
from src.model import SVMClassifier
from sklearn.model_selection import train_test_split

def main():
    train_df = pd.read_csv(TRAIN_FILE)
    test_df = pd.read_csv(TEST_FILE)

    # section a + b)
    train_features = build_features(train_df)
    test_features = build_features(test_df)

    # section c)
    plot_mutation_distribution(train_df, test_df)

    # section d)
    labels = train_df.groupby("case_id")["Label"].first()

    clf = SVMClassifier(use_pca=False, n_components=40)


    x_train, x_val, y_train, y_val = train_test_split(train_features,
                                                             labels,
                                                             test_size=0.2,
                                                             stratify=labels,
                                                             random_state=1)

    clf.fit(x_train, y_train)

    predictions = clf.evaluate(x_val, y_val)
    error = (predictions['true_label'] != predictions['predicted_label']).mean()
    print(f"Validation Error Rate: {error:.4f}")

if __name__ == "__main__":
    main()
