"""
Explanation Module for Experiment 4: Personalized Recommendation System
Generates detailed explanations describing why each resource suits the user's goals.
"""

import utils

SYSTEM = (
    "You are an academic and career mentor. Explain clearly and motivatingly "
    "why each recommended learning resource aligns with the student's background, skill level, and goals."
)

def explain_recommendations(profile: dict, items: list, verbose: bool = True) -> str:
    """Generate in-depth explanations for why the recommendations suit the user."""
    if not items:
        return "No recommendations available to explain."

    item_summary = "\n".join([f"- {it['name']} ({it['score']}%): {it['reason']}" for it in items])
    prompt = (
        f"User Profile:\n"
        f"Name: {profile.get('name')}\n"
        f"Skill Level: {profile.get('skill_level')}\n"
        f"Primary Goal: {profile.get('goal')}\n\n"
        f"Recommendations:\n{item_summary}\n\n"
        f"Instruction: Provide a cohesive, 2 to 3 paragraph explanation detailing how these resources "
        f"form an optimal learning roadmap for {profile.get('name')} to achieve their goal."
    )

    if verbose:
        print("\n" + utils.DASH)
        print("GENERATING EXPLANATIONS VIA OLLAMA (PHI-3)...")
        print(utils.DASH)

    explanation = utils.ask(SYSTEM, prompt, temperature=0.6)

    if verbose:
        print("\n" + utils.DOUBLE_DASH)
        print("RECOMMENDATION EXPLANATION ROADMAP")
        print(utils.DOUBLE_DASH)
        print(explanation)
        print(utils.DOUBLE_DASH)

    return explanation
