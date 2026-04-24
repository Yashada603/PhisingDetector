import pickle
from feature_extractor import extract_features
from utils import interpret_result

def load_model():
    with open("phishing_model.pkl", "rb") as f:
        return pickle.load(f)

def main():
    print("=== Phishing Detection Tool ===")

    try:
        model = load_model()
    except:
        print("Model not found! Train model first.")
        return

    url = input("Enter URL: ")

    features = extract_features(url)
    prediction = model.predict([features])[0]

    result = interpret_result(prediction)

    # 🔍 Output
    print("\n🔍 Analyzing URL...")
    print("Result:", result)
    print("-" * 40)

    # 📁 Save history
    with open("history.txt", "a") as f:
        f.write(f"{url} -> {result}\n")

if __name__ == "__main__":
    main()