from sklearn.svm import SVC
from sklearn.preprocessing import MaxAbsScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd


class SVMClassifier:
    """
    SVM pipeline with scaling, optional PCA, and fixed hyperparameters.
    Includes reproducibility via random_state.
    """

    def __init__(self, use_pca=True, n_components=40, random_state=0):
        self.use_pca = use_pca
        self.n_components = n_components
        self.random_state = random_state
        self.model = None

    def build_pipeline(self):
        """
        Construct a scikit-learn pipeline for SVM classification.

        The pipeline includes:
        - MaxAbsScaler: Scales each feature by its max absolute value.
        - (Optional) PCA: Dimensionality reduction with a fixed random_state.
        - SVC: Support Vector Classifier with C=1, gamma='scale', and balanced class weights.
        """
        steps = [("scale", MaxAbsScaler())]
        if self.use_pca:
            steps.append(("pca", PCA(n_components=self.n_components, random_state=self.random_state)))
        steps.append(("svc", SVC(C=1, gamma="scale", class_weight="balanced")))
        return Pipeline(steps)

    def fit(self, X: pd.DataFrame, y: pd.Series):
        """
        Fit the fixed-parameter SVM pipeline on training data.

        Args:
            X (pd.DataFrame): Feature matrix.
            y (pd.Series): Target labels.
        """
        self.model = self.build_pipeline()
        self.model.fit(X, y)

    def evaluate(self, X_val: pd.DataFrame, y_val: pd.Series):
        """Evaluate model performance on validation data."""
        y_pred = self.model.predict(X_val)
        acc = accuracy_score(y_val, y_pred)
        print("Hold-out accuracy:", acc)
        print(classification_report(y_val, y_pred))

        results_df = pd.DataFrame({
            "case_id": X_val.index,
            "true_label": y_val.values,
            "predicted_label": y_pred})
        return results_df

    def predict(self, X_test: pd.DataFrame) -> pd.Series:
        """Predict labels for unseen test data."""
        return pd.Series(self.model.predict(X_test), index=X_test.index)
