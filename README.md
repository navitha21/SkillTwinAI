# 🚀 SkillTwin AI

### Your Personal AI Career Readiness Assistant

SkillTwin AI is a Python-based career skill analysis application that compares a user's current skills with the skills mentioned in a job description. It identifies skill gaps and generates a personalized learning roadmap with learning resources and project ideas.

## ✨ Features

* **Skill Matching:** Compare current skills with job requirements.
* **Skill Gap Analysis:** Identify recognized skills that may need further development.
* **Match Score:** Calculate the percentage of recognized job skills that match the user's listed skills.
* **Personalized Learning Roadmap:** Recommend learning resources, estimated durations, and practice projects.
* **Interactive Dashboard:** Use a simple web interface built with Streamlit.

## 🛠️ Technologies Used

* Python
* Streamlit
* Regular expressions
* Git and GitHub

## 📁 Project Structure

```text
SkillTwinAI/
├── app.py
├── skill_matcher.py
├── roadmap_generator.py
├── requirements.txt
├── README.md
└── .gitignore
```

The `.venv/` virtual environment is created locally and should not be committed to the repository.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SkillTwinAI
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 🧪 How to Use

1. Select your target career.
2. Enter your current skills.
3. Paste a job description.
4. Click **Analyze My Career**.
5. Review matching skills and missing skills.
6. Explore the recommended learning roadmap.

## 📊 How the Match Score Works

The current version uses a predefined list of recognizable skills.

The match score is calculated as:

**Match Score = (Matching Recognized Skills / Total Recognized Job Skills) × 100**

The score measures skill overlap only. It does not measure overall job readiness or guarantee employment.

## 🔮 Future Improvements

* Resume PDF upload and text extraction.
* Semantic skill matching using NLP embeddings.
* Role-specific skill recommendations.
* Unit tests and automated quality checks.
* Improved dashboard visualizations.
* Online deployment.

## 👩‍💻 Project Purpose

SkillTwin AI is a learning and portfolio project designed to demonstrate Python programming, text processing, rule-based skill matching, and interactive application development.

## 📄 License

This project can be published under the MIT License if you choose to add an MIT `LICENSE` file.
