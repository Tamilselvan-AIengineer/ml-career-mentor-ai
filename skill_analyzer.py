def analyze_skills(student_skills):

    required_skills = [
        "python",
        "data structures",
        "machine learning",
        "deep learning",
        "statistics",
        "sql",
        "git",
        "docker"
    ]

    missing = []

    for skill in required_skills:

        if skill not in student_skills:
            missing.append(skill)

    return missing
