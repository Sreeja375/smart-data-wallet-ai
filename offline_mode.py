import json


def save_offline(data):
    with open("offline_data.json", "w") as f:
        json.dump(data, f)


def load_offline():
    try:
        with open("offline_data.json", "r") as f:
            return json.load(f)
    except:
        return []