"""
Profile and Preference Analysis Module for Experiment 4.
Collects user profile and derives constraints and primary/secondary preferences.
"""

from utils import DASH, save_profile, load_profile

def collect_profile(interactive: bool = True, prefill: dict = None) -> dict:
    """Collect user profile attributes."""
    if not interactive and prefill:
        profile = {
            "name": prefill.get("name", "Emily Watson").strip(),
            "age": int(prefill.get("age", 22)),
            "background": prefill.get("background", "Computer Science Student").strip(),
            "interests": prefill.get("interests", "Machine Learning, Cloud Computing").strip(),
            "skill_level": prefill.get("skill_level", "Intermediate").strip(),
            "category": prefill.get("category", "Courses").strip(),
            "goal": prefill.get("goal", "Become a Machine Learning Engineer").strip(),
            "count": max(1, min(10, int(prefill.get("count", 5))))
        }
        save_profile(profile)
        display_profile(profile)
        return profile

    print("\n" + DASH)
    print("ENTER USER PROFILE DETAILS")
    print(DASH)

    while True:
        name = input("Enter Full Name: ").strip()
        if name:
            break
        print("[ERROR] Name cannot be empty.")

    age_in = input("Enter Age [Default: 22]: ").strip()
    age = int(age_in) if age_in.isdigit() else 22

    bg_in = input("Enter Educational / Professional Background [Default: Computer Science]: ").strip()
    background = bg_in if bg_in else "Computer Science"

    int_in = input("Enter Interests (comma separated) [Default: Machine Learning, Python, Web Development]: ").strip()
    interests = int_in if int_in else "Machine Learning, Python, Web Development"

    skill_in = input("Enter Skill Level (Beginner / Intermediate / Advanced) [Default: Beginner]: ").strip()
    skill_level = skill_in if skill_in else "Beginner"

    cat_in = input("Enter Preferred Category (e.g. Online Courses, Books, Projects, Certifications) [Default: Online Courses]: ").strip()
    category = cat_in if cat_in else "Online Courses"

    goal_in = input("Enter Primary Goal [Default: Build AI Applications]: ").strip()
    goal = goal_in if goal_in else "Build AI Applications"

    cnt_in = input("Enter Number of Recommendations (1 to 10) [Default: 5]: ").strip()
    count = int(cnt_in) if cnt_in.isdigit() and 1 <= int(cnt_in) <= 10 else 5

    profile = {
        "name": name,
        "age": age,
        "background": background,
        "interests": interests,
        "skill_level": skill_level,
        "category": category,
        "goal": goal,
        "count": count
    }
    save_profile(profile)
    display_profile(profile)
    return profile

def display_profile(profile: dict):
    """Neatly display current user profile."""
    print("\n" + DASH)
    print("USER PROFILE CONFIGURED")
    print(DASH)
    print(f"  Name           : {profile.get('name')}")
    print(f"  Age            : {profile.get('age')}")
    print(f"  Background     : {profile.get('background')}")
    print(f"  Interests      : {profile.get('interests')}")
    print(f"  Skill Level    : {profile.get('skill_level')}")
    print(f"  Category       : {profile.get('category')}")
    print(f"  Primary Goal   : {profile.get('goal')}")
    print(f"  Target Items   : {profile.get('count')}")
    print(DASH)

def analyse_preferences(profile: dict = None, verbose: bool = True) -> dict:
    """Q3 - identify major interests, skill level, goal, preferred type and constraints."""
    if not profile:
        profile = load_profile()

    interests = [i.strip() for i in profile["interests"].split(",") if i.strip()]
    analysis = {
        "primary_interest": interests[0] if interests else profile["interests"],
        "secondary_interest": interests[1] if len(interests) > 1 else "General Computer Science",
        "skill_level": profile["skill_level"],
        "goal": profile["goal"],
        "preference": profile["category"],
        "constraints": f"Content must strictly suit a {profile['skill_level'].lower()} learner aiming to {profile['goal'].lower()}.",
    }

    if verbose:
        print("\n" + DASH)
        print("PREFERENCE ANALYSIS")
        print(DASH)
        print(f"  Primary Interest   : {analysis['primary_interest']}")
        print(f"  Secondary Interest : {analysis['secondary_interest']}")
        print(f"  Skill Level        : {analysis['skill_level']}")
        print(f"  Goal               : {analysis['goal']}")
        print(f"  Preferred Type     : {analysis['preference']}")
        print(f"  Derived Constraint : {analysis['constraints']}")
        print(DASH)

    return analysis

