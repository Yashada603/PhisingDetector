import re

def extract_features(url):
    features = {}

    features['length'] = len(url)
    features['has_https'] = 1 if url.startswith("https") else 0
    features['has_ip'] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    features['has_at'] = 1 if "@" in url else 0
    features['has_dash'] = 1 if "-" in url else 0

    return list(features.values())