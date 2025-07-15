import os
import json

def load_test_data(filename):
    path = os.path.join(os.path.dirname(__file__), '..', 'test_data', filename)
    path = os.path.abspath(path)

    if not os.path.isfile(path):
        raise FileNotFoundError(f"Test data file not found: {path}")

    with open(path, 'r') as file:
        return json.load(file)
