"""
Semantic matching using sentence transformers
Author: Gladiator2005
Date: 2025-11-09
"""

from sentence_transformers import SentenceTransformer, util
from config import SENTENCE_TRANSFORMER_MODEL, DEFAULT_SEMANTIC_THRESHOLD

class SemanticMatcher:
    def __init__(self):
        self.model = SentenceTransformer(SENTENCE_TRANSFORMER_MODEL)
    
    def compute_skill_matches(self, job_skills, resumes_texts, threshold=DEFAULT_SEMANTIC_THRESHOLD):
        if not job_skills or not resumes_texts:
            return [[] for _ in resumes_texts]
        
        skill_emb = self.model.encode(job_skills, convert_to_tensor=True)
        resume_emb = self.model.encode(resumes_texts, convert_to_tensor=True)
        sim_matrix = util.pytorch_cos_sim(skill_emb, resume_emb).cpu().numpy()
        
        matched = []
        for j in range(sim_matrix.shape[1]):
            matched_skills = []
            for i, skill in enumerate(job_skills):
                if sim_matrix[i, j] >= threshold:
                    matched_skills.append(skill)
            matched.append(sorted(set(matched_skills)))
        
        return matched
    
    def compute_similarity_scores(self, role_text, resumes_texts):
        if not resumes_texts:
            return []
        
        role_emb = self.model.encode([role_text], convert_to_tensor=True)
        resume_emb = self.model.encode(resumes_texts, convert_to_tensor=True)
        
        return util.pytorch_cos_sim(role_emb, resume_emb).cpu().numpy().flatten()