"""
Configuration file for Resume Screening System
Author: Gladiator2005
Date: 2025-11-09
"""

# Database Configuration
DB_PATH = "resume_screening_multi_role.db"

# Spacy Model
SPACY_MODEL = "en_core_web_sm"

# Sentence Transformer Model
SENTENCE_TRANSFORMER_MODEL = "all-MiniLM-L6-v2"

# Semantic Matching Threshold
DEFAULT_SEMANTIC_THRESHOLD = 0.45

# Comprehensive Skills Database (100+ technical skills)
SKILLS_DB = [
    # Programming Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "ruby", "go", "rust",
    "php", "swift", "kotlin", "scala", "r", "matlab", "perl", "bash", "shell",
    
    # Web Technologies
    "html", "css", "react", "angular", "vue", "svelte", "jquery", "bootstrap",
    "tailwind", "sass", "less", "webpack", "vite", "nextjs", "nuxt",
    
    # Backend Frameworks
    "django", "flask", "fastapi", "spring", "spring boot", "express", "nestjs",
    "rails", "laravel", "asp.net", "node.js", "nodejs",
    
    # Databases
    "sql", "mysql", "postgresql", "postgres", "mongodb", "redis", "cassandra",
    "dynamodb", "elasticsearch", "oracle", "sql server", "sqlite", "mariadb",
    
    # Cloud & DevOps
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "jenkins",
    "gitlab", "github actions", "terraform", "ansible", "chef", "puppet",
    "ci/cd", "devops", "microservices",
    
    # Data Science & ML
    "machine learning", "deep learning", "tensorflow", "pytorch", "keras",
    "scikit-learn", "pandas", "numpy", "data analysis", "data science",
    "nlp", "computer vision", "neural networks", "ai", "artificial intelligence",
    
    # Big Data
    "spark", "hadoop", "kafka", "airflow", "databricks", "snowflake",
    "big data", "data engineering", "etl",
    
    # Mobile Development
    "android", "ios", "react native", "flutter", "xamarin", "mobile development",
    
    # Version Control & Tools
    "git", "github", "gitlab", "bitbucket", "svn", "mercurial",
    
    # Testing
    "pytest", "junit", "selenium", "cypress", "jest", "unit testing",
    "integration testing", "test automation", "tdd",
    
    # Other Skills
    "rest api", "graphql", "websockets", "oauth", "jwt", "linux", "unix",
    "agile", "scrum", "jira", "confluence", "system design", "architecture",
    "data structures", "algorithms", "oop", "functional programming"
]
