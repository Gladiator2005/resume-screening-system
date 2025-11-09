"""
Main application file for Resume Screening System
Author: Gladiator2005
Date: 2025-11-09
Usage: python main.py
"""

import pandas as pd
from screening_engine import ResumeScreener

def main():
    """Main application entry point"""
    
    print("="*80)
    print("RESUME SCREENING SYSTEM")
    print("Author: Gladiator2005")
    print("Date: 2025-11-09")
    print("="*80)
    
    # Initialize screener
    screener = ResumeScreener()
    
    # Add sample roles
    print("\n[INFO] Creating sample roles...")
    
    screener.add_role_from_text(
        "Python Backend Developer",
        """We are looking for a Python developer with experience in Flask, APIs,
        and working with databases like PostgreSQL. Familiarity with Docker is a plus."
    )
    
    screener.add_role_from_text(
        "Systems Architect",
        """Seeking a Systems Architect with experience in system architecture design,
        database management, cloud computing, and technical documentation."""
    )
    
    screener.add_role_from_text(
        "Frontend Developer",
        """Looking for a Frontend Developer with React, TypeScript, and modern CSS.
        Experience with REST APIs and Git is required."""
    )
    
    # List roles
    print("\n" + "="*80)
    print("AVAILABLE ROLES:")
    print("="*80)
    roles_df = screener.db.list_roles()
    print(roles_df[['id', 'name', 'skills_text']].to_string(index=False))
    
    print("\n" + "="*80)
    print("System ready! Use the ResumeScreener class to screen resumes.")
    print("Example: screener.screen_resumes(role_id=1, pdf_paths=['resume.pdf'])")
    print("Database: resume_screening_multi_role.db")
    print("="*80)


if __name__ == "__main__":
    main()