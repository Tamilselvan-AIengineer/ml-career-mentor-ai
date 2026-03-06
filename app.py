import streamlit as st
from rag_engine import CareerRAG
from skill_analyzer import analyze_skills
from translator import translate_to_english
from continual_learning import update_profile
from transformers import pipeline

st.title("🎓 AI Career Mentor")

st.write("Multilingual AI powered career guidance")

rag = CareerRAG()

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

name = st.text_input("Student Name")

query = st.text_input("Ask Career Question")

skills = st.text_input("Your Skills (comma separated)")


if st.button("Get Career Advice"):

    english_query = translate_to_english(query)

    context = rag.retrieve(english_query)

    prompt = f"""
    Student Question: {english_query}

    Context:
    {context}

    Provide career guidance and roadmap.
    """

    result = generator(prompt, max_length=200)

    st.subheader("Career Guidance")

    st.write(result[0]["generated_text"])

    skill_list = [s.strip().lower() for s in skills.split(",")]

    missing = analyze_skills(skill_list)

    st.subheader("Skill Gap Analysis")

    if missing:

        st.write("You need to learn:")

        for s in missing:
            st.write("-", s)

    else:
        st.write("Your skills match industry requirements")

    update_profile(name, skill_list)

    st.success("Profile updated for continual learning")
