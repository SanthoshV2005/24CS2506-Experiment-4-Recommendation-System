"""
Ranking Module for Experiment 4: Personalized Recommendation System
Ranks recommendations by suitability score and prints a clear tabular report.
"""

import utils

def rank(items: list, verbose: bool = True) -> list:
    """Q6 - rank the recommendations by suitability score descending."""
    if not items:
        return []

    ranked = sorted(items, key=lambda x: x.get("score", 0), reverse=True)

    if verbose:
        width = max([len(i["name"]) for i in ranked] + [20])
        print("\n" + utils.DOUBLE_DASH)
        print("                     RECOMMENDATION RANKING TABLE")
        print(utils.DOUBLE_DASH)
        print(f"{'Rank':<6} | {'Recommendation':<{width}} | {'Score':<7} | {'Reason'}")
        print("-" * (width + 60))
        for rank_no, item in enumerate(ranked, 1):
            reason_snippet = item["reason"][:45] + "..." if len(item["reason"]) > 48 else item["reason"]
            print(f"{rank_no:<6} | {item['name']:<{width}} | {item['score']}%{'':<3} | {reason_snippet}")
        print("-" * (width + 60))

    return ranked

