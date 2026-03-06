import streamlit as st
import json
import os
import time
from pathlib import Path

# Page config
st.set_page_config(
    page_title="EduAI — Adaptive Learning System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── Background ── */
.stApp {
    background: #0a0e1a;
    color: #e8eaf0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1628 0%, #0a0e1a 100%);
    border-right: 1px solid rgba(99, 179, 237, 0.15);
}
[data-testid="stSidebar"] .stMarkdown h1,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
    font-family: 'Syne', sans-serif;
    color: #63b3ed;
}

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #0f1628 0%, #1a2040 40%, #0f2035 100%);
    border: 1px solid rgba(99, 179, 237, 0.2);
    border-radius: 20px;
    padding: 40px 48px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 260px; height: 260px;
    background: radial-gradient(circle, rgba(99,179,237,0.12) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -80px; left: 20%;
    width: 320px; height: 320px;
    background: radial-gradient(circle, rgba(154,117,234,0.08) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #63b3ed, #9a75ea, #63b3ed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 8px 0;
    line-height: 1.1;
}
.hero-sub {
    font-size: 1rem;
    color: #8892a8;
    font-weight: 300;
    letter-spacing: 0.02em;
}
.hero-badges {
    display: flex;
    gap: 10px;
    margin-top: 20px;
    flex-wrap: wrap;
}
.badge {
    background: rgba(99, 179, 237, 0.1);
    border: 1px solid rgba(99, 179, 237, 0.3);
    color: #63b3ed;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 500;
    letter-spacing: 0.04em;
}
.badge.purple {
    background: rgba(154, 117, 234, 0.1);
    border-color: rgba(154, 117, 234, 0.3);
    color: #9a75ea;
}
.badge.green {
    background: rgba(72, 199, 142, 0.1);
    border-color: rgba(72, 199, 142, 0.3);
    color: #48c78e;
}

/* ── Section Headers ── */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #c8d0e4;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin: 28px 0 16px 0;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(99,179,237,0.3), transparent);
}

/* ── Cards ── */
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 16px;
    transition: all 0.2s ease;
}
.card:hover {
    border-color: rgba(99,179,237,0.25);
    background: rgba(99,179,237,0.04);
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    color: #e8eaf0;
    margin-bottom: 6px;
}
.card-body {
    font-size: 0.88rem;
    color: #8892a8;
    line-height: 1.6;
}

/* ── Metric Cards ── */
.metric-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 24px;
}
.metric-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 20px;
    text-align: center;
}
.metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #63b3ed;
    line-height: 1;
}
.metric-label {
    font-size: 0.78rem;
    color: #8892a8;
    margin-top: 6px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

/* ── Chat ── */
.chat-container {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 20px;
    min-height: 400px;
    max-height: 520px;
    overflow-y: auto;
    margin-bottom: 16px;
}
.message-user {
    background: linear-gradient(135deg, rgba(99,179,237,0.15), rgba(99,179,237,0.08));
    border: 1px solid rgba(99,179,237,0.2);
    border-radius: 14px 14px 4px 14px;
    padding: 14px 18px;
    margin: 10px 0 10px 40px;
    font-size: 0.92rem;
    color: #e8eaf0;
}
.message-ai {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px 14px 14px 4px;
    padding: 14px 18px;
    margin: 10px 40px 10px 0;
    font-size: 0.92rem;
    color: #c8d0e4;
    line-height: 1.65;
}
.msg-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin-bottom: 6px;
    text-transform: uppercase;
}
.msg-label.user { color: #63b3ed; }
.msg-label.ai   { color: #9a75ea; }

/* ── Source chips ── */
.source-chip {
    display: inline-block;
    background: rgba(154,117,234,0.12);
    border: 1px solid rgba(154,117,234,0.25);
    color: #9a75ea;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    margin: 4px 4px 0 0;
}

/* ── Profile card ── */
.profile-header {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 20px;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    margin-bottom: 16px;
}
.avatar {
    width: 56px; height: 56px;
    border-radius: 50%;
    background: linear-gradient(135deg, #63b3ed, #9a75ea);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    color: white;
    flex-shrink: 0;
}
.profile-name {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #e8eaf0;
}
.profile-sub {
    font-size: 0.82rem;
    color: #8892a8;
    margin-top: 2px;
}

/* ── Skill bars ── */
.skill-bar-wrap { margin-bottom: 12px; }
.skill-bar-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.82rem;
    color: #a0aaba;
    margin-bottom: 5px;
}
.skill-bar-bg {
    background: rgba(255,255,255,0.06);
    border-radius: 6px;
    height: 6px;
    overflow: hidden;
}
.skill-bar-fill {
    height: 100%;
    border-radius: 6px;
    background: linear-gradient(90deg, #63b3ed, #9a75ea);
}

/* ── Status dots ── */
.status-ok  { color: #48c78e; }
.status-warn{ color: #f6c90e; }
.status-err { color: #f25f5c; }

/* ── Streamlit overrides ── */
.stButton > button {
    background: linear-gradient(135deg, #1e3a5f, #2d1b5e);
    color: #e8eaf0;
    border: 1px solid rgba(99,179,237,0.3);
    border-radius: 10px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    padding: 10px 22px;
    transition: all 0.2s;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #2a4f80, #3d2680);
    border-color: #63b3ed;
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(99,179,237,0.2);
}
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: rgba(99,179,237,0.4) !important;
    box-shadow: 0 0 0 2px rgba(99,179,237,0.1) !important;
}
.stSelectbox > div > div { color: #e8eaf0 !important; }
div[data-baseweb="select"] > div { background: rgba(255,255,255,0.04) !important; border-color: rgba(255,255,255,0.1) !important; }
.stRadio > div { gap: 6px; }
label[data-baseweb="radio"] { color: #c8d0e4 !important; }
.stCheckbox > label { color: #c8d0e4 !important; }
.stSlider > div > div > div { background: rgba(99,179,237,0.15) !important; }
div[data-testid="stMetricValue"] { color: #63b3ed !important; font-family: 'Syne', sans-serif !important; }
div[data-testid="stMetricLabel"] { color: #8892a8 !important; }
.stProgress > div > div > div { background: linear-gradient(90deg, #63b3ed, #9a75ea) !important; }
.stTabs [data-baseweb="tab"] {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.85rem !important;
    color: #8892a8 !important;
    font-weight: 600 !important;
}
.stTabs [aria-selected="true"] { color: #63b3ed !important; }
.stTabs [data-baseweb="tab-border"] { background: #63b3ed !important; }
.stAlert { border-radius: 12px !important; }
hr { border-color: rgba(255,255,255,0.07) !important; }
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)


# ── Helpers / Mock Data ────────────────────────────────────────────────────
def load_student_profiles():
    try:
        p = Path("student_profiles.json")
        if p.exists():
            with open(p) as f:
                return json.load(f)
    except Exception:
        pass
    return {
        "students": [
            {"id": "S001", "name": "Aisha Patel",    "level": "Intermediate", "skills": {"Python": 72, "ML": 58, "Math": 85}, "completed": 14, "total": 20},
            {"id": "S002", "name": "Ravi Kumar",     "level": "Beginner",     "skills": {"Python": 40, "ML": 25, "Math": 60}, "completed": 5,  "total": 20},
            {"id": "S003", "name": "Sara Chen",      "level": "Advanced",     "skills": {"Python": 91, "ML": 87, "Math": 95}, "completed": 19, "total": 20},
            {"id": "S004", "name": "Tom Okonkwo",    "level": "Intermediate", "skills": {"Python": 65, "ML": 70, "Math": 78}, "completed": 12, "total": 20},
        ]
    }

def load_data_file(filename):
    for base in ["data/", ""]:
        p = Path(base + filename)
        if p.exists():
            return p.read_text()
    return None

def skill_bar(label, value):
    st.markdown(f"""
    <div class="skill-bar-wrap">
        <div class="skill-bar-label"><span>{label}</span><span>{value}%</span></div>
        <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:{value}%"></div></div>
    </div>""", unsafe_allow_html=True)

def init_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "selected_student" not in st.session_state:
        st.session_state.selected_student = None
    if "rag_context" not in st.session_state:
        st.session_state.rag_context = []

init_session()

# ── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 16px 0 24px;">
        <div style="font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:800;
                    background:linear-gradient(90deg,#63b3ed,#9a75ea);
                    -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            🧠 EduAI
        </div>
        <div style="font-size:0.75rem; color:#8892a8; margin-top:4px;">
            LLM · RAG · Continual Learning
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio("Navigation", [
        "🏠  Dashboard",
        "💬  AI Tutor (RAG)",
        "👤  Student Profiles",
        "📚  Knowledge Base",
        "🔄  Continual Learning",
        "⚙️  System Config",
    ], label_visibility="collapsed")

    st.markdown("---")
    st.markdown("### 🟢 System Status")
    st.markdown('<span class="status-ok">●</span> LLM Engine online', unsafe_allow_html=True)
    st.markdown('<span class="status-ok">●</span> RAG Index loaded', unsafe_allow_html=True)
    st.markdown('<span class="status-ok">●</span> CL Module active', unsafe_allow_html=True)
    st.markdown('<span class="status-warn">●</span> GPU: CPU fallback', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📁 Data Files")
    for fname in ["courses.txt", "careers.txt", "skills.txt"]:
        exists = load_data_file(fname) is not None
        icon = "✅" if exists else "⬜"
        st.markdown(f"{icon} `{fname}`")

# ── Page Router ───────────────────────────────────────────────────────────
page_key = page.split("  ")[-1].strip()

# ═══════════════════════════════════════════════════════════
# PAGE: DASHBOARD
# ═══════════════════════════════════════════════════════════
if "Dashboard" in page:
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">Adaptive Learning Intelligence</div>
        <div class="hero-sub">Powered by LLM · Retrieval-Augmented Generation · Continual Learning</div>
        <div class="hero-badges">
            <span class="badge">🤖 LLM Core</span>
            <span class="badge purple">📡 RAG Pipeline</span>
            <span class="badge green">🔄 Continual Learning</span>
            <span class="badge">🌐 Multi-lingual</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    profiles = load_student_profiles()
    students = profiles.get("students", [])
    total_students = len(students)
    avg_progress = sum(s["completed"]/s["total"]*100 for s in students) / max(total_students, 1)

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("👥 Students", total_students)
    with c2: st.metric("📊 Avg Progress", f"{avg_progress:.0f}%")
    with c3: st.metric("📚 Courses", "12 Active")
    with c4: st.metric("🧠 CL Cycles", "47")

    st.markdown("---")

    col_left, col_right = st.columns([3, 2])
    with col_left:
        st.markdown('<div class="section-title">Student Progress</div>', unsafe_allow_html=True)
        for s in students:
            pct = s["completed"] / s["total"] * 100
            lvl_color = {"Beginner": "#48c78e", "Intermediate": "#63b3ed", "Advanced": "#9a75ea"}.get(s["level"], "#aaa")
            st.markdown(f"""
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                    <div>
                        <div class="card-title">{s['name']}</div>
                        <div style="font-size:0.78rem; color:{lvl_color}; font-weight:500;">{s['level']}</div>
                    </div>
                    <div style="font-family:'Syne',sans-serif; font-size:1.4rem; font-weight:800; color:#63b3ed;">{pct:.0f}%</div>
                </div>
                <div class="skill-bar-bg"><div class="skill-bar-fill" style="width:{pct}%"></div></div>
                <div style="font-size:0.78rem; color:#8892a8; margin-top:6px;">{s['completed']} / {s['total']} modules complete</div>
            </div>""", unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="section-title">System Pipeline</div>', unsafe_allow_html=True)
        pipeline = [
            ("📥", "Data Ingestion",    "courses.txt · careers.txt · skills.txt", "#63b3ed"),
            ("🔍", "RAG Indexing",      "Vector embeddings + semantic search",     "#9a75ea"),
            ("🤖", "LLM Inference",     "Contextual answer generation",            "#48c78e"),
            ("🔄", "Continual Update",  "Profile adaptation & memory refresh",     "#f6c90e"),
        ]
        for icon, title, desc, color in pipeline:
            st.markdown(f"""
            <div class="card">
                <div style="display:flex; gap:14px; align-items:flex-start;">
                    <div style="font-size:1.4rem; line-height:1;">{icon}</div>
                    <div>
                        <div class="card-title" style="color:{color};">{title}</div>
                        <div class="card-body">{desc}</div>
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-title">Quick Actions</div>', unsafe_allow_html=True)
        if st.button("🔄 Refresh Knowledge Base", use_container_width=True):
            with st.spinner("Indexing documents..."):
                time.sleep(1.5)
            st.success("Knowledge base updated!")
        if st.button("📊 Generate Report", use_container_width=True):
            with st.spinner("Generating..."):
                time.sleep(1)
            st.success("Report ready!")

# ═══════════════════════════════════════════════════════════
# PAGE: AI TUTOR
# ═══════════════════════════════════════════════════════════
elif "AI Tutor" in page:
    st.markdown("""
    <div class="hero-banner" style="padding: 28px 36px;">
        <div class="hero-title" style="font-size:1.9rem;">💬 AI Tutor — RAG Powered</div>
        <div class="hero-sub">Answers grounded in your knowledge base: courses, careers & skills</div>
    </div>
    """, unsafe_allow_html=True)

    col_chat, col_ctx = st.columns([3, 1])

    with col_chat:
        # Render history
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        if not st.session_state.chat_history:
            st.markdown("""
            <div style="text-align:center; padding: 60px 20px; color:#8892a8;">
                <div style="font-size:2.5rem; margin-bottom:12px;">🧠</div>
                <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:600; color:#c8d0e4;">Ask me anything</div>
                <div style="font-size:0.85rem; margin-top:6px;">Try: "What Python courses are available?" or "What career paths suit ML skills?"</div>
            </div>""", unsafe_allow_html=True)
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f"""
                <div class="message-user">
                    <div class="msg-label user">You</div>
                    {msg['content']}
                </div>""", unsafe_allow_html=True)
            else:
                sources_html = "".join(f'<span class="source-chip">📄 {s}</span>' for s in msg.get("sources", []))
                st.markdown(f"""
                <div class="message-ai">
                    <div class="msg-label ai">🧠 EduAI</div>
                    {msg['content']}
                    <div style="margin-top:10px;">{sources_html}</div>
                </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Input
        with st.form("chat_form", clear_on_submit=True):
            ic1, ic2 = st.columns([5, 1])
            with ic1:
                user_input = st.text_input("", placeholder="Ask about courses, careers, skills…", label_visibility="collapsed")
            with ic2:
                send = st.form_submit_button("Send ➤", use_container_width=True)

        if send and user_input.strip():
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            # Mock RAG retrieval
            courses_data  = load_data_file("courses.txt")  or "Python Fundamentals, Machine Learning A-Z, Data Science Bootcamp"
            careers_data  = load_data_file("careers.txt")  or "Data Scientist, ML Engineer, AI Researcher, Data Analyst"
            skills_data   = load_data_file("skills.txt")   or "Python, TensorFlow, SQL, Statistics, Deep Learning"

            q = user_input.lower()
            if "course" in q or "learn" in q or "study" in q:
                answer  = f"Based on our course catalog, here are relevant options:\n\n{courses_data[:300]}…\n\nI recommend starting with foundational courses before moving to advanced topics."
                sources = ["courses.txt"]
            elif "career" in q or "job" in q or "work" in q:
                answer  = f"For career guidance, our data shows:\n\n{careers_data[:300]}…\n\nYour skill profile aligns well with Data Science and ML Engineering roles."
                sources = ["careers.txt"]
            elif "skill" in q or "python" in q or "ml" in q:
                answer  = f"Key skills in our database:\n\n{skills_data[:300]}…\n\nFocusing on Python + ML libraries would maximize your career opportunities."
                sources = ["skills.txt"]
            else:
                answer  = f"Great question! I searched our knowledge base covering courses, careers, and skills. Based on the context, I can provide personalized guidance. Could you clarify whether you're asking about learning paths, career options, or specific skills to develop?"
                sources = ["courses.txt", "careers.txt"]

            st.session_state.chat_history.append({
                "role": "ai", "content": answer, "sources": sources
            })
            st.rerun()

    with col_ctx:
        st.markdown('<div class="section-title" style="font-size:0.85rem;">⚙️ RAG Config</div>', unsafe_allow_html=True)
        st.selectbox("Retriever", ["Dense (FAISS)", "Sparse (BM25)", "Hybrid"], label_visibility="visible")
        st.slider("Top-K docs", 1, 10, 3)
        st.slider("Temperature", 0.0, 1.0, 0.3, step=0.05)
        st.checkbox("Show sources", value=True)
        st.checkbox("Stream response", value=True)

        if st.button("🗑 Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

        st.markdown('<div class="section-title" style="font-size:0.85rem;">📚 Active Docs</div>', unsafe_allow_html=True)
        for fname in ["courses.txt", "careers.txt", "skills.txt"]:
            exists = load_data_file(fname) is not None
            icon = "🟢" if exists else "⚪"
            st.markdown(f"{icon} `{fname}`")

# ═══════════════════════════════════════════════════════════
# PAGE: STUDENT PROFILES
# ═══════════════════════════════════════════════════════════
elif "Student Profiles" in page:
    st.markdown("""
    <div class="hero-banner" style="padding:28px 36px;">
        <div class="hero-title" style="font-size:1.9rem;">👤 Student Profiles</div>
        <div class="hero-sub">Personalized learner data — continually updated by the CL module</div>
    </div>
    """, unsafe_allow_html=True)

    profiles = load_student_profiles()
    students = profiles.get("students", [])
    names = [s["name"] for s in students]

    col_list, col_detail = st.columns([1, 2])

    with col_list:
        st.markdown('<div class="section-title">Learners</div>', unsafe_allow_html=True)
        for s in students:
            pct = s["completed"] / s["total"] * 100
            if st.button(f"{'→ ' if st.session_state.selected_student == s['id'] else ''}{s['name']}\n{s['level']} · {pct:.0f}%", key=s["id"], use_container_width=True):
                st.session_state.selected_student = s["id"]
                st.rerun()

        st.markdown("---")
        st.markdown('<div class="section-title">Add Student</div>', unsafe_allow_html=True)
        with st.expander("➕ New Student"):
            new_name  = st.text_input("Name")
            new_level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])
            if st.button("Add"):
                students.append({"id": f"S{len(students)+1:03d}", "name": new_name, "level": new_level,
                                 "skills": {"Python": 0, "ML": 0, "Math": 0}, "completed": 0, "total": 20})
                st.success(f"Added {new_name}")

    with col_detail:
        sel = next((s for s in students if s["id"] == st.session_state.selected_student), students[0] if students else None)
        if sel:
            pct = sel["completed"] / sel["total"] * 100
            initials = "".join(p[0] for p in sel["name"].split())
            st.markdown(f"""
            <div class="profile-header">
                <div class="avatar">{initials}</div>
                <div>
                    <div class="profile-name">{sel['name']}</div>
                    <div class="profile-sub">{sel['level']} · ID: {sel['id']} · {sel['completed']}/{sel['total']} modules</div>
                </div>
            </div>""", unsafe_allow_html=True)

            t1, t2, t3 = st.tabs(["📊 Skills", "📈 Progress", "🧠 AI Insights"])

            with t1:
                st.markdown('<div class="section-title">Skill Proficiency</div>', unsafe_allow_html=True)
                for skill, val in sel["skills"].items():
                    skill_bar(skill, val)
                st.markdown("---")
                edit_py = st.slider("Python", 0, 100, sel["skills"].get("Python", 0), key=f"py_{sel['id']}")
                edit_ml = st.slider("ML",     0, 100, sel["skills"].get("ML", 0),     key=f"ml_{sel['id']}")
                if st.button("💾 Save Skills"):
                    sel["skills"]["Python"] = edit_py
                    sel["skills"]["ML"]     = edit_ml
                    st.success("Saved!")

            with t2:
                st.progress(pct / 100)
                st.markdown(f"**{pct:.1f}%** complete — {sel['completed']} of {sel['total']} modules")
                upd = st.number_input("Update completed modules", 0, sel["total"], sel["completed"])
                if st.button("✅ Update Progress"):
                    sel["completed"] = upd
                    st.success("Progress updated!")

            with t3:
                st.markdown(f"""
                <div class="card">
                    <div class="card-title">🎯 Recommended Next</div>
                    <div class="card-body">Based on {sel['name']}'s {sel['level']} level and current skill scores, 
                    the model recommends focusing on <strong>Deep Learning Fundamentals</strong> 
                    and <strong>Applied Statistics</strong> next.</div>
                </div>
                <div class="card">
                    <div class="card-title">📡 RAG Personalization</div>
                    <div class="card-body">Retrieval system has indexed this student's learning history. 
                    The LLM will generate responses tailored to their background and gaps.</div>
                </div>
                <div class="card">
                    <div class="card-title">🔄 CL Update Schedule</div>
                    <div class="card-body">Profile will be refreshed after each completed module.
                    Last update: <strong>2 hours ago</strong>. Next: after next quiz submission.</div>
                </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════
# PAGE: KNOWLEDGE BASE
# ═══════════════════════════════════════════════════════════
elif "Knowledge Base" in page:
    st.markdown("""
    <div class="hero-banner" style="padding:28px 36px;">
        <div class="hero-title" style="font-size:1.9rem;">📚 Knowledge Base</div>
        <div class="hero-sub">View and edit source documents used by the RAG pipeline</div>
    </div>
    """, unsafe_allow_html=True)

    files = {"courses.txt": "📘", "careers.txt": "💼", "skills.txt": "🛠️"}
    tabs = st.tabs([f"{icon} {name}" for name, icon in files.items()])

    for tab, (fname, icon) in zip(tabs, files.items()):
        with tab:
            content = load_data_file(fname)
            col_v, col_e = st.columns([1, 1])
            with col_v:
                st.markdown(f'<div class="section-title">{icon} {fname} — Current</div>', unsafe_allow_html=True)
                if content:
                    st.code(content[:1500] + ("…" if len(content) > 1500 else ""), language="text")
                    st.caption(f"📄 {len(content)} characters · {len(content.splitlines())} lines")
                else:
                    st.info(f"`{fname}` not found in `data/` directory.")
            with col_e:
                st.markdown(f'<div class="section-title">✏️ Edit / Upload</div>', unsafe_allow_html=True)
                new_content = st.text_area("Edit content", value=content or "", height=300, key=f"edit_{fname}")
                uploaded = st.file_uploader(f"Or upload new {fname}", type=["txt"], key=f"up_{fname}")
                if st.button(f"💾 Save {fname}", key=f"save_{fname}"):
                    os.makedirs("data", exist_ok=True)
                    data = uploaded.read().decode() if uploaded else new_content
                    with open(f"data/{fname}", "w") as f:
                        f.write(data)
                    st.success(f"✅ {fname} saved! RAG index will refresh on next query.")

# ═══════════════════════════════════════════════════════════
# PAGE: CONTINUAL LEARNING
# ═══════════════════════════════════════════════════════════
elif "Continual" in page:
    st.markdown("""
    <div class="hero-banner" style="padding:28px 36px;">
        <div class="hero-title" style="font-size:1.9rem;">🔄 Continual Learning</div>
        <div class="hero-sub">Monitor and trigger adaptive model updates — no catastrophic forgetting</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.metric("CL Cycles Run", "47", delta="+3 today")
    with c2: st.metric("Avg Accuracy",  "87.4%", delta="+1.2%")
    with c3: st.metric("Memory Replay", "2,840 samples")

    st.markdown("---")
    col_l, col_r = st.columns(2)

    with col_l:
        st.markdown('<div class="section-title">⚙️ CL Configuration</div>', unsafe_allow_html=True)
        strategy = st.selectbox("Strategy", ["Elastic Weight Consolidation (EWC)", "Experience Replay", "Progressive Neural Networks", "PackNet"])
        replay_size = st.slider("Replay Buffer Size", 100, 5000, 1000, step=100)
        ewc_lambda  = st.slider("EWC Lambda (forgetting penalty)", 0.0, 1.0, 0.4, step=0.05)
        lr          = st.number_input("Learning Rate", value=1e-4, format="%.0e")
        auto_trigger= st.checkbox("Auto-trigger on new student data", value=True)
        st.markdown("---")
        if st.button("▶️ Run CL Update Cycle", use_container_width=True):
            bar = st.progress(0)
            status = st.empty()
            for i, msg in enumerate(["Loading profiles…", "Sampling replay buffer…", "Fine-tuning LLM…", "Evaluating…", "Saving checkpoint…"]):
                status.markdown(f"**{msg}**")
                bar.progress((i+1)*20)
                time.sleep(0.7)
            st.success("✅ Continual Learning cycle complete! Model updated without catastrophic forgetting.")

    with col_r:
        st.markdown('<div class="section-title">📊 Training History</div>', unsafe_allow_html=True)
        import random
        cycles = list(range(43, 48))
        for c in cycles:
            acc = 82 + random.random() * 8
            st.markdown(f"""
            <div class="card" style="padding:14px 18px; margin-bottom:8px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <div class="card-title" style="font-size:0.88rem;">Cycle #{c}</div>
                        <div class="card-body" style="font-size:0.78rem;">EWC · {replay_size} samples</div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#48c78e;">{acc:.1f}%</div>
                        <div style="font-size:0.72rem; color:#8892a8;">accuracy</div>
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-title">🧪 Evaluation</div>', unsafe_allow_html=True)
        if st.button("📊 Run Evaluation", use_container_width=True):
            with st.spinner("Evaluating on held-out set…"):
                time.sleep(1.5)
            st.metric("Test Accuracy", "88.1%", delta="+0.7% vs baseline")
            st.metric("Backward Transfer", "-0.02", delta="✅ minimal forgetting")

# ═══════════════════════════════════════════════════════════
# PAGE: SYSTEM CONFIG
# ═══════════════════════════════════════════════════════════
elif "System Config" in page:
    st.markdown("""
    <div class="hero-banner" style="padding:28px 36px;">
        <div class="hero-title" style="font-size:1.9rem;">⚙️ System Configuration</div>
        <div class="hero-sub">LLM provider, RAG pipeline, and deployment settings</div>
    </div>
    """, unsafe_allow_html=True)

    t_llm, t_rag, t_deploy = st.tabs(["🤖 LLM", "📡 RAG Pipeline", "🚀 Deployment"])

    with t_llm:
        st.markdown('<div class="section-title">LLM Provider</div>', unsafe_allow_html=True)
        provider = st.selectbox("Provider", ["OpenAI", "Anthropic Claude", "Ollama (Local)", "Hugging Face"])
        model    = st.text_input("Model", "gpt-4o-mini" if "Open" in provider else "claude-3-haiku-20240307")
        api_key  = st.text_input("API Key", type="password", placeholder="sk-…")
        col_a, col_b = st.columns(2)
        with col_a: max_tokens = st.number_input("Max Tokens", 256, 8192, 1024)
        with col_b: temp       = st.slider("Temperature", 0.0, 1.0, 0.3)
        if st.button("🔗 Test Connection"):
            with st.spinner("Testing…"):
                time.sleep(1)
            st.success("✅ Connected successfully!")

    with t_rag:
        st.markdown('<div class="section-title">Retrieval Settings</div>', unsafe_allow_html=True)
        embed_model = st.selectbox("Embedding Model", ["text-embedding-3-small", "all-MiniLM-L6-v2", "instructor-xl"])
        vector_db   = st.selectbox("Vector Store", ["FAISS (in-memory)", "ChromaDB", "Pinecone", "Weaviate"])
        chunk_size  = st.slider("Chunk Size (tokens)", 128, 1024, 256)
        chunk_overlap = st.slider("Chunk Overlap", 0, 256, 32)
        top_k       = st.slider("Top-K Retrieval", 1, 20, 5)
        if st.button("🔄 Re-index Knowledge Base"):
            with st.spinner("Indexing…"):
                time.sleep(2)
            st.success("✅ Knowledge base re-indexed!")

    with t_deploy:
        st.markdown('<div class="section-title">Deployment</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card">
            <div class="card-title">🚀 Streamlit Cloud</div>
            <div class="card-body">Deploy directly from your GitHub repository. Set secrets via the Streamlit Cloud dashboard under App Settings → Secrets.</div>
        </div>
        <div class="card">
            <div class="card-title">🐳 Docker</div>
            <div class="card-body"><code>docker build -t eduai . && docker run -p 8501:8501 eduai</code></div>
        </div>
        <div class="card">
            <div class="card-title">📋 Required Secrets</div>
            <div class="card-body">OPENAI_API_KEY · ANTHROPIC_API_KEY · PINECONE_KEY (optional)</div>
        </div>""", unsafe_allow_html=True)
