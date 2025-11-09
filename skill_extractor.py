import spacy
from spacy.matcher import PhraseMatcher

class SkillExtractor:
    def __init__(self, skill_list):
        self.nlp = spacy.load('en_core_web_sm')
        self.matcher = PhraseMatcher(self.nlp.vocab)
        self.skills = skill_list
        self.add_skills_to_matcher()

    def add_skills_to_matcher(self):
        patterns = [self.nlp(text) for text in self.skills]
        self.matcher.add('SKILLS', patterns)

    def extract_technical_skills_line(self, text_line):
        doc = self.nlp(text_line)
        matches = self.matcher(doc)
        extracted_skills = []

        for match_id, start, end in matches:
            skill = doc[start:end].text
            extracted_skills.append(skill)

        return extracted_skills

    def extract_skills(self, text):
        lines = text.split('\n')
        all_skills = []
        for line in lines:
            skills = self.extract_technical_skills_line(line)
            all_skills.extend(skills)
        return all_skills

if __name__ == '__main__':
    skills = ['Python', 'Java', 'C++', 'Machine Learning', 'Data Analysis']
    extractor = SkillExtractor(skills)
    sample_text = "Experienced in Python and Java development. Interested in Machine Learning projects."
    extracted_skills = extractor.extract_skills(sample_text)
    print(extracted_skills)