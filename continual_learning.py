import json

FILE = "student_profiles.json"


def load_profiles():

    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}


def save_profiles(data):

    with open(FILE, "w") as f:
        json.dump(data, f)


def update_profile(name, skills):

    data = load_profiles()

    data[name] = skills

    save_profiles(data)
