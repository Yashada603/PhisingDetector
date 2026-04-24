def interpret_result(prediction):
    if prediction == 1:
        return "⚠️ Phishing Website Detected!"
    else:
        return "✅ Safe Website"