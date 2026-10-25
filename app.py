
import streamlit as st

from skill_matcher import analyze_skills
from roadmap_generator import generate_roadmap

st.set_page_config(
    page_title="SkillTwin AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 SkillTwin AI")
st.subheader("Your Personal AI Career Readiness Assistant")

st.write(
    "Understand your current skills, discover career gaps, "
    "and get a personalized learning roadmap."
)

st.divider()

career = st.selectbox(
    "Choose your target career",
    [
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Python Developer",
        "AI Engineer"
    ]
)

skills = st.text_area(
    "Enter your current skills",
    placeholder="Example: Python, SQL, Pandas, NumPy"
)

job_description = st.text_area(
    "Paste the job description",
    placeholder=(
        "Example: Python, SQL, Pandas, Machine Learning, "
        "Deep Learning, Docker"
    )
)

if st.button("Analyze My Career", type="primary"):

    if not skills.strip() or not job_description.strip():
        st.warning(
            "Please enter both your skills and a job description."
        )

    else:
        result = analyze_skills(skills, job_description)

        st.session_state["career_result"] = result
        st.session_state["career_goal"] = career

if "career_result" in st.session_state:

    result = st.session_state["career_result"]
    career = st.session_state["career_goal"]

    st.divider()
    st.header(f"Career Analysis: {career}")

    st.metric(
        "Recognized Skill Match",
        f"{result['match_percentage']}%"
    )

    st.progress(result["match_percentage"] / 100)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matching Skills")

        if result["matching_skills"]:
            for skill in result["matching_skills"]:
                st.write(f"• {skill.title()}")
        else:
            st.write("No matching skills found.")

    with col2:
        st.subheader("📚 Skills to Learn")

        if result["missing_skills"]:
            for skill in result["missing_skills"]:
                st.write(f"• {skill.title()}")
        else:
            st.write("No recognized missing skills!")

    st.caption(
        "The score measures overlap among recognized skills. "
        "It does not measure overall job readiness."
    )

    st.divider()
    st.header("🗺️ Your Personalized Learning Roadmap")

    roadmap = generate_roadmap(result["missing_skills"])

    if roadmap:

        total_weeks = 0

        for index, item in enumerate(roadmap, start=1):

            with st.expander(
                f"Step {index}: {item['topic']}",
                expanded=(index == 1)
            ):
                st.write(f"**Skill:** {item['skill']}")
                st.write(f"**Estimated duration:** {item['duration']}")
                st.write(f"**Practice project:** {item['project']}")

                st.markdown(
                    f"[Open learning resource]({item['resource']})"
                )

        st.info(
            "Follow the recommendations in order, practice each "
            "skill, and build the suggested projects."
        )

    else:
        st.success(
            "You have no recognized missing skills for this job "
            "description. Try another job description to explore "
            "additional learning opportunities."
        )

st.divider()

st.caption("SkillTwin AI | Student AI/ML Portfolio Project")