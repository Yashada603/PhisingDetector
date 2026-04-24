import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    data = pd.read_csv("dataset.csv")

    # ✅ REMOVE URL COLUMN (VERY IMPORTANT)
    if "url" in data.columns:
        data = data.drop("url", axis=1)

    # Features and label
    X = data.drop("label", axis=1)
    y = data["label"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model