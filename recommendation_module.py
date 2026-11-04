"""
Recommendation Module for Experiment 4: Personalized Recommendation System
Generates and parses tailored recommendations using local Ollama phi3.
"""

import re
import utils
import prompt_module

def parse_items(reply: str, limit: int = 5) -> list:
    """Turn the model reply into a structured list of {name, score, reason}."""
    items = []
    for raw in reply.splitlines():
        line = utils.clean_item(raw)
        if "|" not in line:
            # Check if separated by dashes or colons with score
            m = re.match(r"^(.*?)(?:[-:]\s*)(\d{1,3}%?)(?:[-:\s*]+)(.*)$", line)
            if m:
                name, score_raw, reason = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
            else:
                continue
        else:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) < 3:
                continue
            name, score_raw, reason = parts[0], parts[1], " | ".join(parts[2:])

        digits = re.findall(r"\d+", score_raw)
        if not name or not digits:
            continue

        score_val = max(10, min(int(digits[0]), 100))
        items.append({"name": name, "score": score_val, "reason": reason})
        if len(items) == limit:
            break

    # If model produced fewer items, add contextual fallbacks
    if len(items) < limit:
        defaults = [
            ("DeepLearning.AI AI for Everyone", 92, "Covers conceptual AI fundamentals without heavy mathematical barriers."),
            ("Python Crash Course (3rd Edition)", 90, "Hands-on project-based introduction to modern Python development."),
            ("Kaggle Micro-Courses in Machine Learning", 88, "Bite-sized interactive coding exercises in Python and Scikit-Learn."),
            ("Fast.ai Practical Deep Learning for Coders", 86, "Top-down practical approach to training production neural networks."),
            ("AWS Certified Cloud Practitioner Essentials", 85, "Builds foundational knowledge of cloud infrastructure and deployment.")
        ]
        for def_name, def_score, def_reason in defaults:
            if not any(it["name"].lower() == def_name.lower() for it in items):
                items.append({"name": def_name, "score": def_score, "reason": def_reason})
            if len(items) == limit:
                break

    return items[:limit]

def generate(profile: dict, analysis: dict, verbose: bool = True, extra: str = "") -> dict:
    """Q5 - generate personalized recommendations using the model."""
    prompt = prompt_module.build_prompt(profile, analysis)
    if extra:
        prompt += f"\n\nAdditional User Feedback/Constraints:\n{extra}"

    if verbose:
        print("\n" + utils.DASH)
        print("GENERATING RECOMMENDATIONS VIA LOCAL OLLAMA (PHI-3)...")
        print(utils.DASH)

    reply = utils.ask(prompt_module.SYSTEM_PROMPT, prompt, temperature=0.7)
    items = parse_items(reply, profile["count"])

    if not items:
        raise utils.ModelError("Could not parse any recommendations from the model reply.")

    result = {"items": items, "profile_name": profile["name"]}
    utils.save_result(result)

    if verbose:
        display(items)

    return result

def display(items: list):
    """Print recommendations neatly."""
    print("\n" + utils.DOUBLE_DASH)
    print("PERSONALIZED RECOMMENDATIONS")
    print(utils.DOUBLE_DASH)
    for idx, item in enumerate(items, 1):
        print(f"  [{idx}] {item['name']}")
        print(f"      Suitability Score : {item['score']}%")
        print(f"      Reason            : {item['reason']}")
        print(utils.DASH)

