"""
================================================================================
24CS2506 – BUILDING APPLICATIONS WITH GPT-4
EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM
Student Name   : Santhosh V
Register Number: URK23CS1003
Academic Year  : 2026–2027 (Odd Semester)
Faculty-in-Charge: Dr. C. Priyadharsini
================================================================================
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import utils
import profile_module
import prompt_module
import recommendation_module
import ranking_module
import explanation_module
import feedback_module
import intent_module

def print_banner():
    """Print the application startup banner."""
    print(utils.DOUBLE_DASH)
    print("     PERSONALIZED RECOMMENDATION SYSTEM - LOCAL OLLAMA (PHI-3)")
    print("   Course : 24CS2506 - Building Applications with GPT-4")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)

def print_menu():
    """Display the 9 menu options."""
    print("\n" + utils.DASH)
    print("                    EXPERIMENT 4 - MAIN MENU")
    print(utils.DASH)
    print("  [1] Enter / Configure User Profile")
    print("  [2] Analyze Preferences & Synthesize Constraints")
    print("  [3] Generate Personalized Recommendations (Phi-3)")
    print("  [4] Display Ranked Recommendations Table")
    print("  [5] Generate In-Depth Recommendation Explanations")
    print("  [6] Provide User Feedback & Refine Recommendations")
    print("  [7] Save Recommendations Report to Disk")
    print("  [8] Run LLM Intent Detection Router")
    print("  [9] Exit Application")
    print(utils.DASH)

def run_demo():
    """Non-interactive automated demonstration executing live phi3 processing."""
    print_banner()
    print("\n[INFO] Starting Automated Demonstration Mode for Experiment 4...")
    print("[INFO] Executing live preference synthesis & Ollama phi3 inference...\n")
    time.sleep(1)

    # 1. Profile
    print("\n>>> OPTION 1: USER PROFILE")
    sample_profile = {
        "name": "Emily Watson",
        "age": 21,
        "background": "Data Science & Statistics",
        "interests": "Deep Learning, PyTorch, Computer Vision",
        "skill_level": "Intermediate",
        "category": "Hands-on Practical Projects",
        "goal": "Build Computer Vision Models for Autonomous Systems",
        "count": 5
    }
    profile_module.display_profile(sample_profile)
    utils.save_profile(sample_profile)
    time.sleep(1)

    # 2. Preference Analysis
    print("\n>>> OPTION 2: PREFERENCE ANALYSIS")
    analysis = profile_module.analyse_preferences(sample_profile, verbose=True)
    time.sleep(1)

    # 3. Prompt Construction & Recommendation Generation
    print("\n>>> OPTION 3: GENERATE PERSONALIZED RECOMMENDATIONS")
    res = recommendation_module.generate(sample_profile, analysis, verbose=True)
    items = res.get("items", [])
    time.sleep(1)

    # 4. Ranking
    print("\n>>> OPTION 4: RANK RECOMMENDATIONS BY SUITABILITY SCORE")
    ranked = ranking_module.rank(items, verbose=True)
    time.sleep(1)

    # 5. Explanations
    print("\n>>> OPTION 5: EXPLAIN RECOMMENDATIONS")
    exp = explanation_module.explain_recommendations(sample_profile, ranked, verbose=True)
    time.sleep(1)

    # 6. User Feedback & Refinement
    print("\n>>> OPTION 6: REFINE WITH USER FEEDBACK")
    feedback = "Focus specifically on open-source PyTorch projects implementing object detection with YOLO."
    refined = feedback_module.refine_with_feedback(feedback, sample_profile, verbose=True)
    time.sleep(1)

    # 7. Save Report
    print("\n>>> OPTION 7: SAVE RECOMMENDATIONS TO DISK")
    saved_path = utils.save_recommendations_file(sample_profile, refined, verbose=True)
    time.sleep(1)

    # 8. Intent Detection
    print("\n>>> OPTION 8: TEST LLM INTENT DETECTION")
    queries = [
        "Please suggest 5 learning resources for computer vision.",
        "Refine these recommendations to focus only on beginner friendly tutorials.",
        "Show my user profile and goals.",
        "Why do these courses fit my intermediate background?",
        "Save the current recommendation list to a text file."
    ]
    for q in queries:
        intent_module.detect_intent(q, verbose=True)
        time.sleep(0.5)

    print("\n" + utils.DOUBLE_DASH)
    print("   EXPERIMENT 4 DEMONSTRATION COMPLETED SUCCESSFULLY")
    print(utils.DOUBLE_DASH)

def interactive_loop():
    """Interactive loop for normal execution."""
    print_banner()
    profile = utils.load_profile()
    analysis = profile_module.analyse_preferences(profile, verbose=False)
    res = utils.load_result()
    current_items = res.get("items", [])

    while True:
        print_menu()
        choice = input("Select an option (1-9): ").strip()

        if choice == "1":
            profile = profile_module.collect_profile(interactive=True)
            analysis = profile_module.analyse_preferences(profile, verbose=False)

        elif choice == "2":
            profile = utils.load_profile()
            analysis = profile_module.analyse_preferences(profile, verbose=True)

        elif choice == "3":
            profile = utils.load_profile()
            analysis = profile_module.analyse_preferences(profile, verbose=False)
            try:
                res = recommendation_module.generate(profile, analysis, verbose=True)
                current_items = res.get("items", [])
            except Exception as e:
                print(f"[ERROR] Generation failed: {e}")

        elif choice == "4":
            if not current_items:
                res = utils.load_result()
                current_items = res.get("items", [])
            if not current_items:
                print("[WARNING] No recommendations available. Generating recommendations first...")
                res = recommendation_module.generate(profile, analysis, verbose=True)
                current_items = res.get("items", [])
            ranking_module.rank(current_items, verbose=True)

        elif choice == "5":
            if not current_items:
                print("[WARNING] No recommendations available. Generating first...")
                res = recommendation_module.generate(profile, analysis, verbose=True)
                current_items = res.get("items", [])
            explanation_module.explain_recommendations(profile, current_items, verbose=True)

        elif choice == "6":
            fb = input("\nEnter your feedback or refinement criteria: ").strip()
            if not fb:
                fb = "Focus on free, open-source resources with practical exercises."
            try:
                current_items = feedback_module.refine_with_feedback(fb, profile, verbose=True)
            except Exception as e:
                print(f"[ERROR] Refinement failed: {e}")

        elif choice == "7":
            if not current_items:
                res = utils.load_result()
                current_items = res.get("items", [])
            if not current_items:
                print("[WARNING] No recommendations to save. Generate first.")
            else:
                utils.save_recommendations_file(profile, current_items, verbose=True)

        elif choice == "8":
            q = input("\nEnter query for intent classification (or press Enter for default): ").strip()
            if not q:
                q = "Explain why these courses are recommended for my skill level."
            intent_module.detect_intent(q, verbose=True)

        elif choice == "9":
            print("\nExiting Personalized Recommendation System. Goodbye!")
            break

        else:
            print("[ERROR] Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo()
    else:
        interactive_loop()
