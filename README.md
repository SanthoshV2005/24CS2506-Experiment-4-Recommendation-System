# 24CS2506 – Experiment 4: Personalized Recommendation System

**Course:** 24CS2506 – Building Applications with GPT-4  
**Student Name:** Santhosh V  
**Register Number:** URK23CS1003  
**Faculty-in-Charge:** Dr. C. Priyadharsini  
**Date of Experiment:** 14/10/2026  
**Practical Exam Date:** 11/11/2026  

---

## 1. Aim
To develop a personalized recommendation system using local Ollama (`phi3`) that analyzes user preferences, generates tailored learning recommendations, ranks them by suitability, provides comprehensive explanations, and refines results based on user feedback.

---

## 2. Problem Statement
Design and develop an intelligent personalized recommendation system. The application should collect user information and preferences, analyze the user's requirements, generate personalized recommendations, rank them according to suitability scores (1-100), provide detailed explanations for the recommendations, and refine the results dynamically based on user critique.

---

## 3. Architecture Overview
```
+-------------------------------------------------------------+
|                        User Profile                         |
|   (Name, Age, Background, Interests, Skill Level, Goal)     |
+------------------------------+------------------------------+
                               |
                               v
+------------------------------+------------------------------+
|                    Preference Analysis                      |
|         (Derives Constraints, Primary/Secondary Focus)      |
+------------------------------+------------------------------+
                               |
                               v
+------------------------------+------------------------------+
|                     Prompt Construction                     |
|           (Structured formatting instructions & pipes)      |
+------------------------------+------------------------------+
                               |
                               v
+------------------------------+------------------------------+
|                      Local Ollama (phi3)                    |
|           (Generates Name | Score | Reason per item)        |
+------------------------------+------------------------------+
                               |
   +---------------------------+---------------------------+
   |                           |                           |
   v                           v                           v
+------------------+   +-------------------+   +--------------------+
|  Ranking Module  |   | Explanation Module|   |  Feedback Module   |
| (Sort Descending)|   | (Roadmap Narrative|   |  (Iterative Refine)|
+------------------+   +-------------------+   +--------------------+
                               |
                               v
+-------------------------------------------------------------+
|                      Persistence Layer                      |
|                (outputs/recommendations.txt)                |
+-------------------------------------------------------------+
```

---

## 4. Features & Menu Options
1. **User Profile Configuration:** Collects name, age, background, interests, skill level, category, and goals.
2. **Preference Analysis:** Extracts core constraints and primary/secondary learning axes.
3. **Recommendation Generation:** Generates structured resource recommendations with suitability scores and justifications.
4. **Ranking Table:** Visualizes ranked recommendations sorted by suitability percentage.
5. **Roadmap Explanation:** Synthesizes an in-depth justification of how the resources fit the user's profile.
6. **Feedback Refinement:** Allows user to provide critiques and dynamically regenerate adapted recommendations.
7. **Report Persistence:** Saves complete audit report to `outputs/recommendations.txt`.
8. **Intent Detection:** LLM routes user queries into `GENERATE_RECOMMENDATION`, `REFINE_RECOMMENDATION`, `SHOW_PROFILE`, `EXPLAIN_RECOMMENDATION`, `SAVE_RECOMMENDATION`, `EXIT`.
9. **Automated Demonstration:** Non-interactive end-to-end execution.

---

## 5. Execution Instructions
```cmd
cd D:\OllamaLab\Exp4_RecommendationSystem
pip install -r requirements.txt

:: Interactive Mode
run.bat

:: Automated Demo Mode
demo_exp4.bat
```
