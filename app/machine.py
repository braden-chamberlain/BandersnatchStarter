from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load
from datetime import datetime


class Machine:

    def __init__(self, df: DataFrame = None, model=None):
        self.name = "Random Forest Classifier"
        if df is not None:
            target = df["Rarity"]
            features = df.drop(columns=["Rarity"])
            self.model = RandomForestClassifier()
            self.model.fit(features, target)
        elif model is not None:
            self.model = model

    def __call__(self, pred_basis: DataFrame):
        prediction = self.model.predict(pred_basis)[0]
        confidence = max(self.model.predict_proba(pred_basis)[0])
        return prediction, confidence

    def save(self, filepath):
        dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        model = load(filepath)
        return Machine(model=model)

    def info(self, pred_basis: DataFrame):
        prediction = self.__call__(pred_basis)
        confidence = max(self.model.predict_proba(pred_basis)[0])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Timestamp: {timestamp}, Prediction: {prediction}, Confidence: {confidence}"

