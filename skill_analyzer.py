def analyze_skills(student_skills):

    required_skills = [
        "python",
        "machine learning",
        "deep learning",
        "data structures",
        "sql",
        "statistics",
        "git",
        "docker"
    ]

    missing = []

    for skill in required_skills:

        if skill not in student_skills:
            missing.append(skill)

    return missing
