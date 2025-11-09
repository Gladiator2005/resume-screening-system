"""
Skill extraction module using NLP and pattern matching
Author: Gladiator2005
Date: 2025-11-09
"""

import re
import spacy
from spacy.matcher import PhraseMatcher

try:
    from config import SKILLS_DB, SPACY_MODEL
except ImportError:
    # Minimal fallback if config not available
    SPACY_MODEL = "en_core_web_sm"
    SKILLS_DB = [
        "python", "java", "sql", "react", "docker", "kubernetes"
    ]


def _safe_load_spacy_model(model_name: str):
    """
    Try to load a spaCy model. If not installed, attempt to download it.
    If download fails (e.g. no network), fall back to blank('en') pipeline.
    """
    try:
        return spacy.load(model_name)
    except OSError:
        # Attempt auto-download
        try:
            from spacy.cli import download
            download(model_name)
            return spacy.load(model_name)
        except Exception:
            # Final fallback
            return spacy.blank("en")


class SkillExtractor:
    """Extract skills from text using multiple methods"""

    def __init__(self, skills_list=None, model_name: str = None):
        """
        Initialize NLP model and phrase matcher

        Args:
            skills_list: Optional override list of skills
            model_name: Optional override spaCy model name
        """
        self.skills = [s.strip().lower() for s in (skills_list or SKILLS_DB) if s.strip()]
        chosen_model = model_name or SPACY_MODEL
        self.nlp = _safe_load_spacy_model(chosen_model)

        # If we fell back to blank('en'), add basic components for tokenization
        if "tagger" not in self.nlp.pipe_names and self.nlp.meta.get("lang") == "en":
            # Optionally you can add simple components, but blank is fine for phrase matching
            pass

        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")
        patterns = [self.nlp.make_doc(skill) for skill in self.skills]
        self.matcher.add("SKILLS", patterns)

    def extract_technical_skills_line(self, text):
        """
        Extract skills from explicit 'Technical Skills:' lines in resumes.

        Args:
            text: Entire resume text

        Returns:
            List of skill strings (raw tokens from that line)
        """
        if not text:
            return []

        # Direct search
        m = re.search(r"technical skills\s*[:\-]\s*(.+)", text, flags=re.I)
        if not m:
            # Line-by-line fallback
            for line in text.splitlines():
                if re.match(r"^\s*technical skills\s*[:\-]?", line, flags=re.I):
                    remainder = re.sub(r"^\s*technical skills\s*[:\-]?\s*", "", line, flags=re.I)
                    if remainder:
                        m = re.match(r"(.+)", remainder)
                        break

        if not m:
            return []

        skills_text = m.group(1)
        parts = re.split(r"[,;•\n]+", skills_text)
        parts = [p.strip() for p in parts if p.strip()]
        return parts

    def extract_skills(self, text):
        """
        Extract skills using multiple strategies:
        1. PhraseMatcher (exact matches)
        2. Parsing 'Technical Skills:' line
        3. Regex for common database / tech variants
        4. Noun chunks fallback (only if nothing found)

        Args:
            text: Resume or job description text

        Returns:
            Sorted list of unique skill strings (lowercase)
        """
        if not text:
            return []

        doc = self.nlp(text)
        found = set()

        # Method 1: PhraseMatcher exact matches
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end].text.lower().strip()
            found.add(span)

        # Method 2: Regex for common database/technology variants
        db_patterns = ["postgresql", "postgres", "mysql", "mongodb", "oracle", "sql server"]
        for pat in db_patterns:
            if re.search(r"\b" + re.escape(pat) + r"\b", text, flags=re.I):
                found.add(pat.lower())

        # Method 3: Parse 'Technical Skills:' line
        tech_line = self.extract_technical_skills_line(text)
        for s in tech_line:
            # Normalize
            found.add(s.lower())

        # Method 4: Fallback - noun chunks containing known skill tokens
        if not found and hasattr(doc, "noun_chunks"):
            for chunk in doc.noun_chunks:
                chunk_text = chunk.text.lower().strip()
                if len(chunk_text) >= 3 and any(tok.lemma_.lower() in self.skills for tok in chunk):
                    found.add(chunk_text)

        return sorted(found)


if __name__ == "__main__":
    sample_text = """
    Technical Skills: Python, React, Docker, Kubernetes; PostgreSQL
    Experienced building REST APIs with Flask and deploying via Docker and Kubernetes.
    """
    extractor = SkillExtractor()
    print(extractor.extract_skills(sample_text))
