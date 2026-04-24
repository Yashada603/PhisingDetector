from model import train_model
import pickle
import os
from sklearn.metrics import accuracy_score
import pandas as pd

print("Starting training...")

# Train model
model = train_model()

# Load dataset again for evaluation
data = pd.read_csv("dataset.csv")
if "url" in data.columns:
    data = data.drop("url", axis=1)

X = data.drop("label", axis=1)
y = data["label"]

# Predictions
preds = model.predict(X)

# Accuracy
accuracy = accuracy_score(y, preds)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
model_path = os.path.join(os.getcwd(), "phishing_model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved at:", model_path)