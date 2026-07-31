# 🎓 EduAI – Adaptive Learning Intelligence

> **An AI-powered personalized learning platform built with Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Continual Learning to provide intelligent tutoring, career guidance, and adaptive learning experiences.**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=flat-square&logo=streamlit)
![LLM](https://img.shields.io/badge/LLM-Gemini-success?style=flat-square)
![RAG](https://img.shields.io/badge/RAG-Enabled-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-orange?style=flat-square)

---

# 📖 Overview

EduAI is an intelligent educational assistant that combines **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, and **Continual Learning** to create personalized learning experiences.

The platform adapts to each student's progress, retrieves relevant information from a knowledge base, and generates context-aware responses for academic learning and career guidance.

Unlike traditional chatbots, EduAI continuously improves student profiles based on learning behavior and provides personalized recommendations.

---

# ✨ Features

## 🏠 Dashboard

- Modern and responsive UI
- Student learning analytics
- Active course tracking
- Average learning progress
- Continual learning status
- AI system monitoring

---

## 🤖 AI Tutor (RAG)

- Context-aware question answering
- Semantic document retrieval
- Personalized explanations
- Career guidance
- Programming assistance
- Intelligent learning recommendations

---

## 👨‍🎓 Student Profiles

- Personalized student information
- Learning level tracking
- Skill management
- Progress monitoring
- Learning history
- Adaptive recommendations

---

## 📚 Knowledge Base

- Educational resources
- Programming notes
- Career documents
- Interview preparation materials
- Course content
- Skill documentation

---

## 🔄 Continual Learning

EduAI continuously updates the student profile based on:

- Previous conversations
- Learning progress
- Completed modules
- Skill improvements
- Knowledge gaps

This enables adaptive and personalized learning.

---

## ⚙️ System Configuration

Configure:

- LLM settings
- Embedding models
- Retrieval parameters
- Knowledge base
- API keys
- Continual learning options

---

# 🏗️ System Architecture

```
                    Student
                       │
                       ▼
             Streamlit Web Interface
                       │
                       ▼
               Student Interaction
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 Student Profile  Knowledge Base  Career Data
        │              │              │
        └──────────────┼──────────────┘
                       ▼
              Document Processing
                       │
                       ▼
           Text Chunking & Embeddings
                       │
                       ▼
             Vector Database (FAISS)
                       │
                       ▼
            Retrieval-Augmented Search
                       │
                       ▼
                 Gemini LLM API
                       │
                       ▼
          Personalized AI Response
                       │
                       ▼
           Continual Learning Engine
                       │
                       ▼
        Updated Student Learning Profile
```

---

# 🚀 Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | Google Gemini |
| Retrieval | LangChain |
| Vector Database | FAISS |
| Embeddings | Sentence Transformers |
| Data Storage | JSON |
| Machine Learning | Scikit-learn |
| Visualization | Plotly |

---

# 📂 Project Structure

```
EduAI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── courses.txt
│   ├── careers.txt
│   └── skills.txt
│
├── pages/
│   ├── Dashboard.py
│   ├── AI_Tutor.py
│   ├── Student_Profile.py
│   ├── Knowledge_Base.py
│   ├── Continual_Learning.py
│   └── System_Config.py
│
├── rag/
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
│
├── continual_learning/
│   └── learner.py
│
├── llm/
│   └── gemini.py
│
├── profiles/
│   └── students.json
│
└── assets/
    └── screenshots/
```

---

# 🔄 Workflow

```
Student Query
      │
      ▼
Profile Detection
      │
      ▼
Retrieve Relevant Documents
      │
      ▼
Semantic Search
      │
      ▼
Gemini LLM
      │
      ▼
Generate Personalized Response
      │
      ▼
Update Student Profile
      │
      ▼
Continual Learning
```

---

# 📊 Key Modules

### 📈 Dashboard

- Student statistics
- Progress analytics
- Active courses
- System status
- Learning insights

### 🤖 AI Tutor

- Question answering
- Coding assistance
- Career advice
- Personalized tutoring

### 📚 Knowledge Base

- Document indexing
- Semantic search
- Embedding generation
- Information retrieval

### 🔄 Continual Learning

- Student memory
- Adaptive learning
- Progress tracking
- Recommendation updates

---

# 📸 Screenshots

## Dashboard

Add screenshots here.

```
assets/screenshots/dashboard.png
assets/screenshots/student_progress.png
assets/screenshots/rag_pipeline.png
```

Example:

```markdown
![Dashboard](assets/screenshots/dashboard.png)
```

---

# 📈 Future Enhancements

- Resume Analyzer
- Interview Preparation AI
- Placement Prediction
- Job Recommendation System
- Voice Assistant
- PDF Upload Support
- Learning Roadmaps
- Multi-language Support
- PostgreSQL Integration
- Docker Deployment
- Authentication & Authorization

---

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/Tamilselvan-AIengineer/ml-career-mentor-ai.git
```

Navigate to the project directory

```bash
cd ml-career-mentor-ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🎯 Applications

- Personalized Learning
- AI Tutoring
- Career Guidance
- Skill Development
- Educational Analytics
- Intelligent Knowledge Retrieval

---

# 👨‍💻 Author

**Tamilselvan M**

AI & Machine Learning Enthusiast

SRM Institute of Science and Technology

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project helpful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🐛 Report issues
- 💡 Suggest new features

---

## 💡 Project Vision

EduAI demonstrates how **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, and **Continual Learning** can be combined to build an intelligent educational ecosystem that delivers personalized learning, adaptive tutoring, and career guidance for students.
