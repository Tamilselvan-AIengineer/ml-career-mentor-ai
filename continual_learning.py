import json

FILE = "student_profiles.json"


def load_profiles():

    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}


def update_profile(name, skills):

    profiles = load_profiles()

    profiles[name] = skills

    with open(FILE, "w") as f:
        json.dump(profiles, f)
