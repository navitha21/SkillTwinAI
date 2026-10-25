
# Personalized learning recommendations for SkillTwin AI

ROADMAP = {
    "python": {
        "topic": "Python Programming",
        "duration": "1-2 weeks",
        "resource": "https://docs.python.org/3/tutorial/",
        "project": "Build a command-line expense tracker."
    },
    "sql": {
        "topic": "SQL and Databases",
        "duration": "1 week",
        "resource": "https://sqlbolt.com/",
        "project": "Build a student database and write SQL queries."
    },
    "pandas": {
        "topic": "Data Analysis with Pandas",
        "duration": "1 week",
        "resource": "https://pandas.pydata.org/docs/getting_started/",
        "project": "Analyze a real-world CSV dataset."
    },
    "numpy": {
        "topic": "Numerical Computing with NumPy",
        "duration": "4-5 days",
        "resource": "https://numpy.org/learn/",
        "project": "Implement basic statistical calculations."
    },
    "machine learning": {
        "topic": "Machine Learning Fundamentals",
        "duration": "2-3 weeks",
        "resource": "https://scikit-learn.org/stable/getting_started.html",
        "project": "Build a student performance prediction model."
    },
    "deep learning": {
        "topic": "Deep Learning",
        "duration": "3-4 weeks",
        "resource": "https://www.tensorflow.org/tutorials",
        "project": "Build an image classification model."
    },
    "scikit-learn": {
        "topic": "Scikit-learn",
        "duration": "1-2 weeks",
        "resource": "https://scikit-learn.org/stable/tutorial/index.html",
        "project": "Compare classification models on a dataset."
    },
    "tensorflow": {
        "topic": "TensorFlow",
        "duration": "2 weeks",
        "resource": "https://www.tensorflow.org/tutorials",
        "project": "Train a handwritten digit classifier."
    },
    "pytorch": {
        "topic": "PyTorch",
        "duration": "2 weeks",
        "resource": "https://pytorch.org/tutorials/",
        "project": "Build a neural network for image classification."
    },
    "nlp": {
        "topic": "Natural Language Processing",
        "duration": "2 weeks",
        "resource": "https://huggingface.co/learn/nlp-course",
        "project": "Build a review sentiment classifier."
    },
    "natural language processing": {
        "topic": "Natural Language Processing",
        "duration": "2 weeks",
        "resource": "https://huggingface.co/learn/nlp-course",
        "project": "Build a review sentiment classifier."
    },
    "data analysis": {
        "topic": "Data Analysis",
        "duration": "1 week",
        "resource": "https://www.kaggle.com/learn/data-cleaning",
        "project": "Analyze and visualize a public dataset."
    },
    "data visualization": {
        "topic": "Data Visualization",
        "duration": "1 week",
        "resource": "https://plotly.com/python/",
        "project": "Create an interactive analytics dashboard."
    },
    "statistics": {
        "topic": "Statistics for Data Science",
        "duration": "2 weeks",
        "resource": "https://www.khanacademy.org/math/statistics-probability",
        "project": "Explore distributions and correlations in a dataset."
    },
    "git": {
        "topic": "Git and Version Control",
        "duration": "3-5 days",
        "resource": "https://git-scm.com/doc",
        "project": "Publish a Python project with meaningful commits."
    },
    "docker": {
        "topic": "Docker Fundamentals",
        "duration": "1 week",
        "resource": "https://docs.docker.com/get-started/",
        "project": "Package a Python application in a container."
    },
    "fastapi": {
        "topic": "Building APIs with FastAPI",
        "duration": "1 week",
        "resource": "https://fastapi.tiangolo.com/tutorial/",
        "project": "Create an API that predicts a model's output."
    },
    "streamlit": {
        "topic": "Streamlit Application Development",
        "duration": "3-5 days",
        "resource": "https://docs.streamlit.io/get-started",
        "project": "Build an interactive data dashboard."
    },
    "aws": {
        "topic": "Cloud Computing with AWS",
        "duration": "1-2 weeks",
        "resource": "https://aws.amazon.com/getting-started/",
        "project": "Deploy a small application using an appropriate AWS service."
    },
    "power bi": {
        "topic": "Power BI",
        "duration": "1 week",
        "resource": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi",
        "project": "Create a business analytics dashboard."
    },
    "excel": {
        "topic": "Excel for Data Analysis",
        "duration": "1 week",
        "resource": "https://support.microsoft.com/en-us/excel",
        "project": "Build a spreadsheet-based data analysis report."
    }
}

def generate_roadmap(missing_skills):
    """Generate learning recommendations for missing skills."""

    recommendations = []

    for skill in missing_skills:
        details = ROADMAP.get(skill.lower())

        if details:
            recommendations.append({
                "skill": skill.title(),
                **details
            })

        else:
            recommendations.append({
                "skill": skill.title(),
                "topic": f"Learn {skill.title()}",
                "duration": "To be determined",
                "resource": "https://www.google.com/search?q="
                            + skill.replace(" ", "+")
                            + "+official+tutorial",
                "project": f"Build a small project using {skill.title()}."
            })

    return recommendations