
import re

# Skills that our first version can recognize.
SKILLS = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "data analysis",
    "data visualization",
    "statistics",
    "tensorflow",
    "pytorch",
    "nlp",
    "natural language processing",
    "git",
    "docker",
    "fastapi",
    "streamlit",
    "aws",
    "power bi",
    "excel"
]

def extract_skills(text):
    """Find recognized skills in a piece of text."""
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        # Match complete words or phrases, not partial words.
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(set(found_skills))

def analyze_skills(current_skills, job_description):
    """Compare the user's skills with job requirements."""

    user_skills = extract_skills(current_skills)
    required_skills = extract_skills(job_description)

    matching_skills = [
        skill for skill in required_skills
        if skill in user_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in user_skills
    ]

    if required_skills:
        match_percentage = round(
            len(matching_skills) / len(required_skills) * 100
        )
    else:
        match_percentage = 0

    return {
        "user_skills": user_skills,
        "required_skills": required_skills,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage
    }