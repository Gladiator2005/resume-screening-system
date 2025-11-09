# config.py

# Database Configuration
DATABASE_PATH = 'path/to/your/database.db'

# PDF Extraction Settings
PDF_EXTRACTOR_SETTINGS = {
    'max_pages': 5,
    'extract_tables': True,
    'language': 'eng',
}

# Semantic Matching Settings
SEMANTIC_MATCHING_SETTINGS = {
    'model': 'sentence-transformers/all-MiniLM-L6-v2',
    'threshold': 0.75,
}

# Comprehensive Skills Database
SKILLS_DATABASE = [
    # Add 100+ technical skills here
    'Python', 'Java', 'JavaScript', 'C#', 'C++', 'Ruby', 'Go', 
    'SQL', 'HTML', 'CSS', 'React', 'Angular', 'Node.js',
    'Django', 'Flask', 'Kubernetes', 'Docker', 'Machine Learning',
    'Deep Learning', 'Data Analysis', 'AWS', 'Azure', 'GCP',
    # Add additional skills as required...
]

# Model Configurations
SPACY_MODEL = 'en_core_web_sm'
SENTENCE_TRANSFORMERS_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'