import streamlit as st
from rag_engine import CareerRAG
from skill_analyzer import analyze_skills
from continual_learning import update_profile
from translator import Translator
from transformers import pipeline

st.title("🎓 Multi-Lingual AI Career Mentor")

st.write("LLM + Context-Aware RAG + Continual Learning")

rag = CareerRAG()

translator = Translator()

llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

name = st.text_input("Student Name")

query = st.text_input("Ask your career question")

skills = st.text_input("Your Skills (comma separated)")


if st.button("Generate Career Advice"):

    english_query = translator.translate_to_english(query)

    context = rag.retrieve(english_query)

    prompt = f"""
    Student question: {english_query}

    Context:
    {context}

    Provide career guidance and roadmap.
    """

    result = llm(prompt, max_length=200)

    st.subheader("Career Guidance")

    st.write(result[0]["generated_text"])

    skill_list = [s.strip().lower() for s in skills.split(",")]

    missing = analyze_skills(skill_list)

    st.subheader("Skill Gap Analysis")

    if missing:

        st.write("Missing skills:")

        for m in missing:
            st.write("-", m)

    else:

        st.write("Your skills match industry expectations")

    update_profile(name, skill_list)

    st.success("Student profile updated (continual learning)")
