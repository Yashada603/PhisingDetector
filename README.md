# PhisingDetector
Developed an ML-based Phishing Detection Tool using Python and scikit-learn. It extracts features from URLs and 
classifies them as safe or phishing using a trained model. Includes real-time prediction, accuracy evaluation, and history logging for security analysis.

# 🕵️ PhishingDetector - ML-Based URL Threat Detection Tool

## 📌 Description

I developed PhishingDetector as a Python-based machine learning tool to identify malicious or phishing URLs. 
This project focuses on extracting key features from URLs and using a trained model to classify them as safe or phishing. 
The goal is to understand real-world phishing detection techniques and apply basic machine learning in cybersecurity.

---

## 🚀 Features

I can analyze any URL for phishing detection 🌐
I can extract important features from URLs 🔍
I can classify websites as Safe or Phishing ⚠️
I can display real-time prediction results 📊
I can store scan history for future analysis 📁
CLI-based simple and easy-to-use interface

---

## 🛠️ Technologies Used

Python
Pandas (Data handling)
Scikit-learn (Machine Learning)
Random Forest Algorithm
Feature Engineering
Pickle (Model saving/loading)

---

## 📂 Project Structure

PhishingDetector/
│── main.py # Main program (user input & prediction)
│── train_model.py # Model training script
│── model.py # ML model logic
│── feature_extractor.py # URL feature extraction
│── utils.py # Result interpretation
│── dataset.csv # Training dataset
│── phishing_model.pkl # Trained model file
│── history.txt # Scan history

---

## ⚙️ Installation & Setup

Install Python from official website

Install required libraries:

```bash
pip install pandas scikit-learn
```

---

## ▶️ How to Run

First train the model:

```bash
python train_model.py
```

Then run the program:

```bash
python main.py
```

---

## 🖥️ Usage

I run the program
I enter a URL to analyze
The tool extracts features from the URL
The trained model predicts whether it is Safe or Phishing
The result is displayed instantly
The scan is saved in history.txt

---

## 📊 Output

Example:

```
=== Phishing Detection Tool ===
Enter URL: http://free-money-now.com

🔍 Analyzing URL...
Result: ⚠️ Phishing Website Detected!
----------------------------------------
```

---

## 🎯 Project Goal

To build a practical cybersecurity tool that demonstrates phishing detection using machine 
learning and feature-based analysis, helping understand how modern systems identify malicious URLs.

---
