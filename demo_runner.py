"""
Demo Runner for Experiment 4: Personalized Recommendation System
Executed directly inside the Windows CMD window to display live output.
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

STATUS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "status.txt")

def set_status(val):
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        f.write(val)

def main():
    set_status("starting")
    os.system("cls")

    # STEP 1: Home Screen
    print(utils.DOUBLE_DASH)
    print("     PERSONALIZED RECOMMENDATION SYSTEM - LOCAL OLLAMA (PHI-3)")
    print("   Course : 24CS2506 - Building Applications with GPT-4")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
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
    print("\n[READY] Recommendation Engine initialized.")
    set_status("step_1_ready")
    time.sleep(3)

    # STEP 2 & 3: Profile Input & Collected Profile
    os.system("cls")
    print(utils.DOUBLE_DASH)
    print("   EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
    print("\n>>> OPTION 1: USER PROFILE CONFIGURATION")
    sample_profile = {
        "name": "Emily Watson",
        "age": 21,
        "background": "Data Science & Statistics",
        "interests": "Deep Learning, PyTorch, Computer Vision",
        "skill_level": "Intermediate",
        "category": "Practical Projects & Courses",
        "goal": "Build Computer Vision Models for Autonomous Systems",
        "count": 5
    }
    profile_module.display_profile(sample_profile)
    utils.save_profile(sample_profile)
    print("\n[SUCCESS] Profile validated and registered in active memory.")
    set_status("step_2_ready")
    time.sleep(3)

    # STEP 4: Preference Analysis
    os.system("cls")
    print(utils.DOUBLE_DASH)
    print("   EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
    print("\n>>> OPTION 2: PREFERENCE & CONSTRAINT SYNTHESIS")
    analysis = profile_module.analyse_preferences(sample_profile, verbose=True)
    set_status("step_4_ready")
    time.sleep(3)

    # STEP 5: Prompt Generation
    os.system("cls")
    print(utils.DOUBLE_DASH)
    print("   EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
    print("\n>>> PROMPT GENERATION ENGINE")
    p_text = prompt_module.build_prompt(sample_profile, analysis)
    print(utils.DASH)
    print(p_text)
    print(utils.DASH)
    set_status("step_5_ready")
    time.sleep(3)

    # STEP 6: Recommendation Generation
    os.system("cls")
    print(utils.DOUBLE_DASH)
    print("   EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
    print("\n>>> OPTION 3: GENERATE RECOMMENDATIONS (OLLAMA PHI-3)")
    res = recommendation_module.generate(sample_profile, analysis, verbose=True)
    items = res.get("items", [])
    set_status("step_6_ready")
    time.sleep(3)

    # STEP 7: Ranking Table
    os.system("cls")
    print(utils.DOUBLE_DASH)
    print("   EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
    print("\n>>> OPTION 4: RANK RECOMMENDATIONS BY SUITABILITY SCORE")
    ranked = ranking_module.rank(items, verbose=True)
    set_status("step_7_ready")
    time.sleep(3)

    # STEP 8: Explanations
    os.system("cls")
    print(utils.DOUBLE_DASH)
    print("   EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
    print("\n>>> OPTION 5: RECOMMENDATION EXPLANATION ROADMAP")
    exp = explanation_module.explain_recommendations(sample_profile, ranked, verbose=True)
    set_status("step_8_ready")
    time.sleep(3)

    # STEP 9 & 10: Feedback & Refinement
    os.system("cls")
    print(utils.DOUBLE_DASH)
    print("   EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
    print("\n>>> OPTION 6: DYNAMIC FEEDBACK REFINEMENT")
    feedback = "Focus strictly on open-source PyTorch projects implementing real-time YOLO object detection."
    refined = feedback_module.refine_with_feedback(feedback, sample_profile, verbose=True)
    set_status("step_10_ready")
    time.sleep(3)

    # STEP 11: Intent Detection
    os.system("cls")
    print(utils.DOUBLE_DASH)
    print("   EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
    print("\n>>> OPTION 8: TEST LLM INTENT DETECTION")
    queries = [
        "Please suggest 5 learning resources for computer vision.",
        "Refine these recommendations to focus only on beginner friendly tutorials.",
        "Show my user profile and goals.",
        "Why do these courses fit my intermediate background?",
        "Save the current recommendation list to a text file.",
        "Exit application now."
    ]
    for q in queries:
        intent_module.detect_intent(q, verbose=True)
        time.sleep(0.3)
    set_status("step_11_ready")
    time.sleep(3)

    # STEP 12: Save Recommendations
    os.system("cls")
    print(utils.DOUBLE_DASH)
    print("   EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM")
    print("   Student: Santhosh V (URK23CS1003) | Date: 14/10/2026")
    print(utils.DOUBLE_DASH)
    print("\n>>> OPTION 7: VERIFY AND SAVE RECOMMENDATIONS TO DISK")
    saved_path = utils.save_recommendations_file(sample_profile, refined, verbose=True)
    print(f"\n[CONFIRMED] File Path : {os.path.abspath(saved_path)}")
    print(f"File Size     : {os.path.getsize(saved_path)} bytes")
    print(utils.DASH)
    print("File Content Preview:")
    with open(saved_path, "r", encoding="utf-8") as f_in:
        print(f_in.read()[:350] + " ...")
    print(utils.DASH)
    print("\n" + utils.DOUBLE_DASH)
    print("   EXPERIMENT 4 LIVE DEMONSTRATION COMPLETED SUCCESSFULLY")
    print(utils.DOUBLE_DASH)
    set_status("step_12_ready")
    time.sleep(3)
    set_status("demo_completed")

if __name__ == "__main__":
    main()

