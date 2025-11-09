# Resume Screening System

**Author:** Gladiator2005  
**Date:** 2025-11-09  
**Version:** 1.0.0

## Overview

An intelligent resume screening system that uses NLP and machine learning to match candidate resumes with job requirements. Features multi-role support, PDF extraction with OCR fallback, semantic skill matching, and persistent SQLite storage.

## Features

- ✅ **PDF Text Extraction** - PyMuPDF → pdfplumber → OCR fallback
- ✅ **Smart Skill Extraction** - PhraseMatcher + regex + NLP
- ✅ **Semantic Matching** - Sentence transformers for context-aware matching
- ✅ **Multi-Role Support** - Store and screen for multiple job roles
- ✅ **SQLite Database** - Persistent storage with full audit trail
- ✅ **Ranked Results** - Sort by skills matched + similarity score
- ✅ **Google Colab Ready** - Works seamlessly in Colab notebooks

## Installation

### Local Installation

```bash
chmod +x install.sh
./install.sh
```

### Google Colab

```python
!bash install.sh
```

## Quick Start

```python
from screening_engine import ResumeScreener

# Initialize
screener = ResumeScreener()

# Add a role
screener.add_role_from_text(
    "Python Developer",
    "Looking for Python developer with Flask, PostgreSQL, Docker experience"
)

# Screen resumes
results = screener.screen_resumes(
    role_id=1,
    pdf_paths=["resume1.pdf", "resume2.pdf"]
)

# View results
import pandas as pd
print(pd.DataFrame(results))
```

## Project Structure

```
resume-screening/
├── config.py              # Configuration and constants
├── pdf_extractor.py       # PDF text extraction module
├── skill_extractor.py     # Skill extraction using NLP
├── semantic_matcher.py    # Semantic matching with transformers
├── database.py            # SQLite database operations
├── screening_engine.py    # Main screening engine
├── utils.py               # Utility functions
├── main.py                # Main application
├── install.sh             # Installation script
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## License

MIT License - Free to use and modify

## Author

**Gladiator2005**  
GitHub: https://github.com/Gladiator2005

---

**Happy Screening!** 🚀
