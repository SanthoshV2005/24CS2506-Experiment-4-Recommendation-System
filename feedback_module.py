"""
Feedback Module for Experiment 4: Personalized Recommendation System
Incorporates user critiques and feedback to iteratively refine recommendations.
"""

import utils
import profile_module
import recommendation_module
import ranking_module

def refine_with_feedback(feedback_text: str, profile: dict = None, verbose: bool = True) -> list:
    """Regenerate recommendations incorporating user feedback constraints."""
    if not profile:
        profile = utils.load_profile()

    analysis = profile_module.analyse_preferences(profile, verbose=False)
    
    extra_constraint = (
        f"CRITICAL USER FEEDBACK / REFINEMENT REQUEST:\n"
        f"\"{feedback_text}\"\n"
        f"Adapt all recommendations strictly to honor this feedback."
    )

    if verbose:
        print("\n" + utils.DASH)
        print("REFINING RECOMMENDATIONS BASED ON USER FEEDBACK")
        print(utils.DASH)
        print(f"Feedback Received: \"{feedback_text}\"")

    res = recommendation_module.generate(profile, analysis, verbose=False, extra=extra_constraint)
    items = res.get("items", [])
    ranked_items = ranking_module.rank(items, verbose=verbose)
    
    return ranked_items
