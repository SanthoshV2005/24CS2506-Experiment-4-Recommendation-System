"""
Intent Module for Experiment 4: Personalized Recommendation System
Routes queries into:
- GENERATE (or GENERATE_RECOMMENDATION)
- REFINE (or REFINE_RECOMMENDATION)
- SHOW_PROFILE
- EXPLAIN (or EXPLAIN_RECOMMENDATION)
- SAVE (or SAVE_RECOMMENDATION)
- EXIT
"""

import utils

INTENTS = [
    "GENERATE_RECOMMENDATION", "REFINE_RECOMMENDATION",
    "SHOW_PROFILE", "EXPLAIN_RECOMMENDATION",
    "SAVE_RECOMMENDATION", "EXIT"
]

SYSTEM = (
    "You are an AI intent classifier for a recommendation system. "
    "Classify the user input into EXACTLY ONE of the following categories:\n"
    "- GENERATE_RECOMMENDATION : user wants to generate new recommendations\n"
    "- REFINE_RECOMMENDATION   : user wants to refine, modify, or filter recommendations\n"
    "- SHOW_PROFILE            : user wants to see, display, or inspect their profile\n"
    "- EXPLAIN_RECOMMENDATION  : user asks why or wants an explanation of recommendations\n"
    "- SAVE_RECOMMENDATION     : user wants to save, export, or store recommendations\n"
    "- EXIT                    : user wants to quit, exit, or stop\n\n"
    "Respond ONLY with the exact label."
)

def detect_intent(query: str, verbose: bool = True) -> str:
    """Q9 - classify the request into exactly one of the allowed intents."""
    if not query or not query.strip():
        return "GENERATE_RECOMMENDATION"

    prompt = f"User Request: \"{query}\"\nLabel:"
    raw = utils.ask(SYSTEM, prompt, temperature=0.0)
    text = raw.upper().replace("-", "_").replace(" ", "_")

    intent = None
    for candidate in INTENTS:
        if candidate in text:
            intent = candidate
            break

    if not intent:
        if "REFINE" in text or "ADAPT" in text or "FILTER" in text:
            intent = "REFINE_RECOMMENDATION"
        elif "EXPLAIN" in text or "WHY" in text or "JUSTIF" in text:
            intent = "EXPLAIN_RECOMMENDATION"
        elif "PROFILE" in text or "USER" in text or "DETAILS" in text:
            intent = "SHOW_PROFILE"
        elif "SAVE" in text or "EXPORT" in text or "FILE" in text:
            intent = "SAVE_RECOMMENDATION"
        elif "EXIT" in text or "QUIT" in text or "BYE" in text:
            intent = "EXIT"
        else:
            intent = "GENERATE_RECOMMENDATION"

    if verbose:
        print("\n" + utils.DASH)
        print("INTENT CLASSIFICATION")
        print(utils.DASH)
        print(f"User Query      : \"{query}\"")
        print(f"Detected Intent : {intent}")
        print(utils.DASH)

    return intent

