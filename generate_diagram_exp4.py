"""
Generate high-resolution architecture diagram for Experiment 4: Personalized Recommendation System.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_diagram(output_path):
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Background
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    # Title
    ax.text(50, 95, "EXPERIMENT 4: PERSONALIZED RECOMMENDATION SYSTEM", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#f8fafc', fontfamily='sans-serif')
    ax.text(50, 91, "System Architecture: Profile Analysis, Scoring, Ranking & Feedback", 
            ha='center', va='center', fontsize=11, color='#94a3b8', fontfamily='sans-serif')

    def draw_box(x, y, w, h, title, subtitle, color, border_color):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1.5,rounding_size=2",
                                     facecolor=color, edgecolor=border_color, linewidth=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2 + 2, title, ha='center', va='center', 
                fontsize=11, fontweight='bold', color='#ffffff', fontfamily='sans-serif')
        ax.text(x + w/2, y + h/2 - 3, subtitle, ha='center', va='center', 
                fontsize=8, color='#cbd5e1', fontfamily='sans-serif')

    # Level 1: Input & Profile
    draw_box(6, 75, 40, 11, "User Profile Module", "Name, Age, Background, Interests\nSkill Level, Category, Goals", "#1e293b", "#38bdf8")
    draw_box(54, 75, 40, 11, "LLM Intent Classifier", "GENERATE | REFINE | EXPLAIN\nSHOW_PROFILE | SAVE | EXIT", "#1e293b", "#c084fc")

    # Level 2: Analysis & Prompting
    draw_box(6, 56, 40, 11, "Preference Analysis Engine", "Extract Primary/Secondary axes\nSynthesize strict constraints", "#1e293b", "#818cf8")
    draw_box(54, 56, 40, 11, "Structured Prompt Module", "Inject constraints & format schema:\nName | Score | Justification", "#1e293b", "#fbbf24")

    # Level 3: LLM Inference
    draw_box(30, 38, 40, 11, "Local Ollama Engine (phi3)", "Personalized Generation & Scoring\n(Integer percentage 1-100%)", "#1e1b4b", "#6366f1")

    # Level 4: Downstream modules
    draw_box(4, 18, 28, 12, "Ranking Module", "Descending sort by score\nFormatted tabular view", "#1e293b", "#34d399")
    draw_box(36, 18, 28, 12, "Explanation Module", "Multi-paragraph narrative\nRoadmap justification", "#1e293b", "#f87171")
    draw_box(68, 18, 28, 12, "Feedback Module", "Critique incorporation &\niterative re-prompting", "#1e293b", "#fb923c")

    # Level 5: Persistence
    draw_box(32, 4, 36, 8, "Storage & Export Layer", "outputs/recommendations.txt", "#064e3b", "#10b981")

    # Connective Arrows
    arrow_props = dict(arrowstyle="->", color="#94a3b8", lw=1.8, shrinkA=5, shrinkB=5)
    
    ax.annotate("", xy=(26, 67), xytext=(26, 75), arrowprops=arrow_props)
    ax.annotate("", xy=(54, 61), xytext=(46, 61), arrowprops=arrow_props)
    ax.annotate("", xy=(50, 49), xytext=(65, 56), arrowprops=arrow_props)
    ax.annotate("", xy=(18, 30), xytext=(40, 38), arrowprops=arrow_props)
    ax.annotate("", xy=(50, 30), xytext=(50, 38), arrowprops=arrow_props)
    ax.annotate("", xy=(82, 30), xytext=(60, 38), arrowprops=arrow_props)
    ax.annotate("", xy=(50, 12), xytext=(18, 18), arrowprops=arrow_props)
    ax.annotate("", xy=(50, 12), xytext=(50, 18), arrowprops=arrow_props)
    ax.annotate("", xy=(50, 12), xytext=(82, 18), arrowprops=arrow_props)

    ax.text(50, 1, "Santhosh V (URK23CS1003) | 24CS2506 Building Applications with GPT-4 | Dr. C. Priyadharsini",
            ha='center', va='center', fontsize=9, color='#64748b', fontfamily='sans-serif')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Architecture diagram generated: {output_path}")

if __name__ == "__main__":
    generate_diagram(r"D:\OllamaLab\Exp4_RecommendationSystem\architecture_exp4.png")
