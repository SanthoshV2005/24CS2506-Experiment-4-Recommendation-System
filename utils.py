"""
Experiment 4: Personalized Recommendation System
Utility functions for Ollama phi3 communication, data cleaning, and persistence.
"""

import os
import re
import json
import ollama

OLLAMA_MODEL = "phi3"
DASH = "-" * 80
DOUBLE_DASH = "=" * 80
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
REC_FILE = os.path.join(OUTPUT_DIR, "recommendations.txt")
PROFILE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "profile_state.json")
RESULT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recommendations_state.json")

class ModelError(Exception):
    pass

def clean_markdown(text: str) -> str:
    """Strip unnecessary markdown formatting."""
    if not text:
        return ""
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    text = re.sub(r"_(.*?)_", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)
    text = text.replace("`", "")
    return text.strip()

def clean_item(line: str) -> str:
    """Clean a recommendation line by stripping leading numbering and quotes."""
    line = clean_markdown(line).strip()
    line = re.sub(r"^(?:\d+[\.\)]|[-*•])\s*", "", line)
    return line.strip(' "\'')

def ask(system: str, prompt: str, temperature: float = 0.7) -> str:
    """Send prompt to local Ollama phi3 model."""
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty.")
    try:
        messages = []
        if system and system.strip():
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=messages,
            options={"temperature": temperature}
        )
        content = response["message"]["content"]
        return clean_markdown(content)
    except ollama.ResponseError as e:
        raise ModelError(f"Ollama Response Error: {e.error}") from e
    except Exception as e:
        raise ModelError(f"Failed to communicate with Ollama ({OLLAMA_MODEL}): {e}") from e

def load_profile() -> dict:
    """Load current user profile."""
    if os.path.exists(PROFILE_FILE):
        try:
            with open(PROFILE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "name": "David Miller",
        "age": 22,
        "background": "Computer Science & Engineering",
        "interests": "Artificial Intelligence, Python, Cloud Computing",
        "skill_level": "Beginner",
        "category": "Online Courses & Projects",
        "goal": "Build End-to-End AI Applications",
        "count": 5
    }

def save_profile(profile: dict):
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)

def load_result() -> dict:
    if os.path.exists(RESULT_FILE):
        try:
            with open(RESULT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"items": [], "profile_name": ""}

def save_result(result: dict):
    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

def save_recommendations_file(profile: dict, items: list, verbose: bool = True) -> str:
    """Write ranked recommendations and profile to outputs/recommendations.txt."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    lines = [
        "PERSONALIZED RECOMMENDATION SYSTEM - OUTPUT REPORT",
        "=" * 75,
        f"User Name        : {profile.get('name', 'N/A')}",
        f"Age              : {profile.get('age', 'N/A')}",
        f"Background       : {profile.get('background', 'N/A')}",
        f"Interests        : {profile.get('interests', 'N/A')}",
        f"Skill Level      : {profile.get('skill_level', 'N/A')}",
        f"Target Goal      : {profile.get('goal', 'N/A')}",
        f"Category         : {profile.get('category', 'N/A')}",
        "=" * 75,
        "",
        "RANKED RECOMMENDATIONS",
        "-" * 75,
        f"{'Rank':<5} | {'Suitability':<11} | {'Recommendation & Reason'}",
        "-" * 75,
    ]
    for idx, itm in enumerate(items, 1):
        lines.append(f"{idx:<5} | {itm.get('score', 0)}%{'':<7} | {itm.get('name', '')}")
        lines.append(f"{'':<5} | {'':<11} | Reason: {itm.get('reason', '')}")
        lines.append("-" * 75)

    with open(REC_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    if verbose:
        print("\n" + DASH)
        print(f"[SUCCESS] Recommendations saved to: {os.path.abspath(REC_FILE)}")
        print(f"File size on disk: {os.path.getsize(REC_FILE)} bytes")
        print(DASH)

    return REC_FILE
