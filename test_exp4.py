"""
Automated Test Suite for Experiment 4: Personalized Recommendation System
Tests:
1. Profile validation and boundary constraints
2. Preference and constraint analysis
3. Prompt construction
4. Recommendation generation and parsing
5. Ranking module descending order
6. Explanation generation
7. User feedback refinement
8. Intent classification across all 6 categories
9. File persistence to outputs/recommendations.txt
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import utils
import profile_module
import prompt_module
import recommendation_module
import ranking_module
import explanation_module
import feedback_module
import intent_module

class TestExp4RecommendationSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n" + "="*70)
        print("RUNNING AUTOMATED TESTS FOR EXPERIMENT 4: RECOMMENDATION SYSTEM")
        print("="*70)

    def test_01_profile_validation(self):
        """Test profile collection and bounds clamping."""
        prof = profile_module.collect_profile(interactive=False, prefill={
            "name": "David Miller",
            "age": 22,
            "background": "Computer Science",
            "interests": "AI, Cloud, Python",
            "skill_level": "Beginner",
            "category": "Courses",
            "goal": "Build AI",
            "count": 25 # Out of bounds
        })
        self.assertEqual(prof["name"], "David Miller")
        self.assertEqual(prof["count"], 10, "Count should be clamped to maximum 10")

    def test_02_preference_analysis(self):
        """Test preference extraction."""
        prof = {
            "name": "David", "age": 22, "background": "CS",
            "interests": "Deep Learning, PyTorch, Robotics",
            "skill_level": "Intermediate", "category": "Projects",
            "goal": "Build Vision Systems", "count": 3
        }
        analysis = profile_module.analyse_preferences(prof, verbose=False)
        self.assertEqual(analysis["primary_interest"], "Deep Learning")
        self.assertEqual(analysis["secondary_interest"], "PyTorch")
        self.assertIn("intermediate", analysis["constraints"].lower())

    def test_03_recommendation_generation(self):
        """Test recommendation generation and item parsing."""
        prof = {
            "name": "David", "age": 22, "background": "CS",
            "interests": "Python, Machine Learning",
            "skill_level": "Beginner", "category": "Online Courses",
            "goal": "Learn ML", "count": 3
        }
        analysis = profile_module.analyse_preferences(prof, verbose=False)
        res = recommendation_module.generate(prof, analysis, verbose=False)
        items = res.get("items", [])
        self.assertGreaterEqual(len(items), 3, "Should generate at least 3 items")
        for item in items:
            self.assertTrue(len(item["name"]) > 0)
            self.assertTrue(1 <= item["score"] <= 100)
            self.assertTrue(len(item["reason"]) > 0)

    def test_04_ranking_order(self):
        """Test that ranking sorts items in descending order of score."""
        sample_items = [
            {"name": "Course B", "score": 75, "reason": "Reason B"},
            {"name": "Course A", "score": 95, "reason": "Reason A"},
            {"name": "Course C", "score": 85, "reason": "Reason C"}
        ]
        ranked = ranking_module.rank(sample_items, verbose=False)
        scores = [it["score"] for it in ranked]
        self.assertEqual(scores, [95, 85, 75], "Ranked scores must be strictly descending")

    def test_05_explanation_generation(self):
        """Test explanation generation."""
        prof = utils.load_profile()
        sample_items = [
            {"name": "Fast.ai Practical Deep Learning", "score": 95, "reason": "Hands-on approach to neural networks."}
        ]
        exp = explanation_module.explain_recommendations(prof, sample_items, verbose=False)
        self.assertTrue(len(exp) > 50, "Explanation should be substantive")

    def test_06_feedback_refinement(self):
        """Test that user feedback generates adapted recommendations."""
        prof = utils.load_profile()
        feedback = "Focus strictly on free GitHub open source projects for beginners."
        refined = feedback_module.refine_with_feedback(feedback, prof, verbose=False)
        self.assertTrue(len(refined) > 0, "Refined recommendations should not be empty")

    def test_07_intent_classification(self):
        """Test intent classification across the 6 allowed intents."""
        test_cases = {
            "Please generate new recommendations for me": "GENERATE_RECOMMENDATION",
            "Refine these recommendations to focus on open source projects": "REFINE_RECOMMENDATION",
            "Show my user profile and preferences": "SHOW_PROFILE",
            "Explain why these recommendations were selected for me": "EXPLAIN_RECOMMENDATION",
            "Save the recommendations to disk": "SAVE_RECOMMENDATION",
            "I want to exit the application": "EXIT"
        }
        for q, expected in test_cases.items():
            intent = intent_module.detect_intent(q, verbose=False)
            self.assertEqual(intent, expected, f"Query '{q}' mapped to '{intent}' instead of '{expected}'")

    def test_08_file_persistence(self):
        """Test saving recommendations to file."""
        prof = utils.load_profile()
        sample_items = [
            {"name": "Test Course 1", "score": 90, "reason": "Test Reason 1"},
            {"name": "Test Course 2", "score": 85, "reason": "Test Reason 2"}
        ]
        path = utils.save_recommendations_file(prof, sample_items, verbose=False)
        self.assertTrue(os.path.exists(path))
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("PERSONALIZED RECOMMENDATION SYSTEM", content)
        self.assertIn("Test Course 1", content)

if __name__ == "__main__":
    unittest.main()
