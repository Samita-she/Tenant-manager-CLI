import json
import os

TENANTS_FILE = "tenants.json"
PAYMENTS_FILE = "payments.json"

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
