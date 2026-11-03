"""
Prompt Module for Experiment 4: Personalized Recommendation System
Builds structured prompts for local Ollama phi3.
"""

SYSTEM_PROMPT = (
    "You are an expert personalized learning and career advisor. "
    "Provide highly relevant, tailored recommendations strictly aligned with the user's skill level and goals. "
    "Format each recommendation on a SINGLE line using pipe separators strictly as:\n"
    "Resource Name | Suitability Score | One-sentence justification\n"
    "Suitability Score must be an integer between 1 and 100."
)

def build_prompt(profile: dict, analysis: dict) -> str:
    """Q4 - construct the prompt from the collected user information."""
    return (
        f"User Profile:\n"
        f"Name         : {profile['name']}\n"
        f"Age          : {profile['age']}\n"
        f"Background   : {profile['background']}\n"
        f"Interests    : {profile['interests']}\n"
        f"Skill Level  : {profile['skill_level']}\n"
        f"Target Goal  : {profile['goal']}\n"
        f"Preference   : {profile['category']}\n\n"
        f"Primary Focus: {analysis['primary_interest']}\n"
        f"Constraints  : {analysis['constraints']}\n\n"
        f"Instruction:\n"
        f"Recommend exactly {profile['count']} suitable learning resources or tools.\n"
        f"For each item, output on a new line strictly in this format:\n"
        f"Resource Name | Score | Clear reason explaining how it fits their goal\n\n"
        f"Example:\n"
        f"CS50 Introduction to Computer Science | 95 | Provides a strong fundamental programming foundation for beginners."
    )
