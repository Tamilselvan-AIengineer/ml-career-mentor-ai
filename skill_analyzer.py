"""
skill_analyzer.py — Analyze student skill gaps and recommend learning paths.
"""
from pathlib import Path
import json
import re


class SkillAnalyzer:
    """Matches student profiles against the skills knowledge base."""

    def __init__(self, skills_file: str = "data/skills.txt"):
        self.skills_file = Path(skills_file)
        self.skill_catalog: list[str] = self._load_skills()

    def _load_skills(self) -> list[str]:
        if not self.skills_file.exists():
            return ["Python", "Machine Learning", "SQL", "Statistics", "Deep Learning",
                    "TensorFlow", "PyTorch", "Data Visualization", "NLP", "Computer Vision"]
        text = self.skills_file.read_text()
        # Simple line/comma split
        skills = []
        for line in text.splitlines():
            for part in line.split(","):
                s = part.strip()
                if s:
                    skills.append(s)
        return skills

    def analyze_gaps(self, student_skills: dict[str, int]) -> dict:
        """
        Returns skill gaps (skills in catalog but weak in student profile).
        student_skills: {"Python": 72, "ML": 58, ...}
        """
        gaps = []
        strengths = []
        threshold = 70

        for skill in self.skill_catalog[:10]:   # top 10
            # Try fuzzy match
            matched_key = next(
                (k for k in student_skills if skill.lower()[:3] in k.lower()),
                None
            )
            score = student_skills.get(matched_key, 0) if matched_key else 0
            if score < threshold:
                gaps.append({"skill": skill, "current_score": score, "gap": threshold - score})
            else:
                strengths.append({"skill": skill, "score": score})

        gaps.sort(key=lambda x: x["gap"], reverse=True)
        return {"gaps": gaps[:5], "strengths": strengths[:5]}

    def recommend_courses(self, gaps: list[dict], courses_file: str = "data/courses.txt") -> list[str]:
        """Map skill gaps to relevant courses."""
        p = Path(courses_file)
        if not p.exists():
            return [f"Course on {g['skill']}" for g in gaps[:3]]

        content = p.read_text()
        lines = [l.strip() for l in content.splitlines() if l.strip()]
        recommendations = []
        for gap in gaps[:3]:
            keyword = gap["skill"].lower()
            match = next((l for l in lines if keyword in l.lower()), None)
            if match:
                recommendations.append(match)
            else:
                recommendations.append(f"Foundational {gap['skill']} course")
        return recommendations

    def career_fit(self, student_skills: dict[str, int], careers_file: str = "data/careers.txt") -> list[dict]:
        """Score career options based on student skill profile."""
        p = Path(careers_file)
        if not p.exists():
            return [{"career": "Data Scientist", "fit": 82}, {"career": "ML Engineer", "fit": 75}]

        content = p.read_text()
        careers = [l.strip() for l in content.splitlines() if l.strip()]
        avg_skill = sum(student_skills.values()) / max(len(student_skills), 1)

        results = []
        for career in careers[:6]:
            # Mock fit score — replace with real semantic matching
            fit = min(99, int(avg_skill + (hash(career) % 20) - 10))
            results.append({"career": career, "fit": max(30, fit)})

        results.sort(key=lambda x: x["fit"], reverse=True)
        return results
