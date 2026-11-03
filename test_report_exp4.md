# EXPERIMENT 4: AUTOMATED TEST REPORT
**Course Code:** 24CS2506 – Building Applications with GPT-4  
**Experiment 4:** Personalized Recommendation System  
**Student Name:** Santhosh V  
**Register Number:** URK23CS1003  
**Execution Date:** 14/10/2026  
**Test Execution Environment:** Windows 10/11, Python 3.12.6, Local Ollama v0.40.13 (`phi3:latest`)

---

## 1. Executive Summary

| Metric | Result |
|---|---|
| Total Automated Unit Tests | 8 |
| Tests Passed | 8 |
| Tests Failed | 0 |
| Tests Errored | 0 |
| Pass Rate | **100%** |
| Total Execution Time | 730.291s |
| Status | **PASSED** |

---

## 2. Detailed Test Results

| Test ID | Test Function | Target Module / Requirement | Status | Execution Details |
|---|---|---|---|---|
| **TEST-01** | `test_01_profile_validation` | `profile_module.py` (Q1, Q2) | **PASS** | Validated profile field assignment, types, and clamp boundary checks (count clamped from 25 to max 10). |
| **TEST-02** | `test_02_preference_analysis` | `profile_module.py` (Q3) | **PASS** | Successfully extracted primary ("Deep Learning") and secondary ("PyTorch") interests and mapped constraints. |
| **TEST-03** | `test_03_recommendation_generation` | `recommendation_module.py` (Q5) | **PASS** | Verified end-to-end prompt building and Ollama `phi3` generation. Parsed items with valid scores (1-100) and rationale. |
| **TEST-04** | `test_04_ranking_order` | `ranking_module.py` (Q6) | **PASS** | Confirmed strict descending suitability score sort order (`[95, 85, 75]`). |
| **TEST-05** | `test_05_explanation_generation` | `explanation_module.py` (Q7) | **PASS** | Verified generated qualitative explanation of why recommended items fit the user profile (>50 characters). |
| **TEST-06** | `test_06_feedback_refinement` | `feedback_module.py` (Q8) | **PASS** | Tested iterative constraint adaptation based on user critiques; generated updated recommendation set. |
| **TEST-07** | `test_07_intent_classification` | `intent_module.py` (Q9) | **PASS** | Validated Ollama zero-shot intent routing across all 6 official intent classes (`GENERATE_RECOMMENDATION`, `REFINE_RECOMMENDATION`, `SHOW_PROFILE`, `EXPLAIN_RECOMMENDATION`, `SAVE_RECOMMENDATION`, `EXIT`). |
| **TEST-08** | `test_08_file_persistence` | `utils.py` (Q10) | **PASS** | Verified formatted tabular export to `outputs/recommendations.txt` with user profile headers. |

---

## 3. Verification Conclusion
All 8 test cases completed with zero failures. The recommendation engine satisfies all academic, modular, and functional requirements specified in `Experiment_4_Personalized_Recommendation_System_FINAL_4.docx`.
