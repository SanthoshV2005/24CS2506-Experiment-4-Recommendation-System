"""
Generate the concise individual Word laboratory record (.docx) for Experiment 4: Personalized Recommendation System.
Follows the official university reference format (Experiment_4_Personalized_Recommendation_System_FINAL_4.docx).
Student: Santhosh V (URK23CS1003) | Date: 14/10/2026 | Faculty: Dr. C. Priyadharsini
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

DOCX_OUTPUT = r"D:\OllamaLab\Records\Experiment_4_Personalized_Recommendation_System.docx"
EXP_DIR = r"D:\OllamaLab\Exp4_RecommendationSystem"
SCREENSHOT_DIR = os.path.join(EXP_DIR, "screenshots")
ARCH_DIAGRAM = os.path.join(EXP_DIR, "architecture_exp4.png")

def set_cell_background(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_styled_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = 'Calibri'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0, 51, 102) # Navy Blue
    return p

def add_code_block(doc, title, code_text):
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(2)
    p_title.paragraph_format.keep_with_next = True
    r_t = p_title.add_run(title)
    r_t.bold = True
    r_t.font.name = 'Calibri'
    r_t.font.size = Pt(10)
    r_t.font.color.rgb = RGBColor(40, 40, 40)

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:left w:val="single" w:sz="12" w:space="0" w:color="003366"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/></w:tcBorders>')
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = Pt(11)
    run = p.add_run(code_text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 41, 59)

def add_screenshot(doc, img_path, caption):
    if not os.path.exists(img_path):
        return
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(6)
    p_img.paragraph_format.space_after = Pt(2)
    p_img.paragraph_format.keep_with_next = True
    run = p_img.add_run()
    run.add_picture(img_path, width=Inches(6.2))

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(1)
    p_cap.paragraph_format.space_after = Pt(6)
    run_cap = p_cap.add_run(caption)
    run_cap.italic = True
    run_cap.font.name = 'Calibri'
    run_cap.font.size = Pt(9.5)
    run_cap.font.color.rgb = RGBColor(70, 70, 70)

def build_word_record():
    doc = Document()

    # Set 0.75-inch page margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # 1. Top Header Table (Reference Format)
    tbl_hdr = doc.add_table(rows=2, cols=3)
    tbl_hdr.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_data = [
        [("Ex. No.: 4", True), ("Personalized Recommendation System", True), ("REG NO: URK23CS1003", True)],
        [("DATE: 14/10/2026", True), ("Student: Santhosh V", False), ("Odd Semester 2026-27", False)]
    ]
    for r_idx, row in enumerate(hdr_data):
        for c_idx, (text, is_bold) in enumerate(row):
            cell = tbl_hdr.cell(r_idx, c_idx)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(text)
            run.bold = is_bold
            run.font.name = 'Calibri'
            run.font.size = Pt(10)
            set_cell_background(cell, "F1F5F9" if r_idx == 0 else "FFFFFF")
            set_cell_margins(cell, 60, 60, 80, 80)
            tcPr = cell._tc.get_or_add_tcPr()
            tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="6" w:space="0" w:color="003366"/><w:left w:val="single" w:sz="6" w:space="0" w:color="003366"/><w:bottom w:val="single" w:sz="6" w:space="0" w:color="003366"/><w:right w:val="single" w:sz="6" w:space="0" w:color="003366"/></w:tcBorders>')
            tcPr.append(tcBorders)

    # 2. Aim
    add_styled_heading(doc, "Aim:")
    p_aim = doc.add_paragraph()
    p_aim.paragraph_format.space_before = Pt(2)
    p_aim.paragraph_format.space_after = Pt(4)
    p_aim.paragraph_format.line_spacing = Pt(13)
    p_aim.add_run(
        "To develop a personalized recommendation system using local Ollama (phi3) that analyzes user preferences "
        "and generates, ranks, and explains suitable recommendations based on the user's profile, interests, skill level, and goals."
    )

    # 3. Problem Statement
    add_styled_heading(doc, "Problem Statement:")
    p_prob = doc.add_paragraph()
    p_prob.paragraph_format.space_before = Pt(2)
    p_prob.paragraph_format.space_after = Pt(4)
    p_prob.paragraph_format.line_spacing = Pt(13)
    p_prob.add_run(
        "Design and develop an intelligent personalized recommendation system using local Ollama (phi3). The application should collect "
        "user information and preferences, analyze the user's requirements, generate personalized recommendations, rank them according to "
        "suitability, provide explanations for the recommendations, refine the results based on user feedback, and classify operational user intents."
    )

    # 4. Software Requirements
    add_styled_heading(doc, "Software Requirements:")
    tbl_soft = doc.add_table(rows=5, cols=2)
    tbl_soft.alignment = WD_TABLE_ALIGNMENT.CENTER
    soft_data = [
        ("Software", "Version"),
        ("Python", "3.12.6"),
        ("Ollama", "0.40.13"),
        ("Model (phi3)", "phi3:latest"),
        ("Operating System", "Windows 10 / 11")
    ]
    for r_idx, (s, v) in enumerate(soft_data):
        row = tbl_soft.rows[r_idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.5), Inches(3.9)
        p0, p1 = c0.paragraphs[0], c1.paragraphs[0]
        p0.add_run(s).bold = (r_idx == 0)
        p1.add_run(v).bold = (r_idx == 0)
        bg = "003366" if r_idx == 0 else ("F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
        set_cell_background(c0, bg)
        set_cell_background(c1, bg)
        if r_idx == 0:
            p0.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            p1.runs[0].font.color.rgb = RGBColor(255, 255, 255)
        set_cell_margins(c0, 50, 50, 100, 100)
        set_cell_margins(c1, 50, 50, 100, 100)
        for c in (c0, c1):
            tcPr = c._tc.get_or_add_tcPr()
            tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/></w:tcBorders>')
            tcPr.append(tcBorders)

    # 5. Input Parameters
    add_styled_heading(doc, "Input Parameters:")
    tbl_param = doc.add_table(rows=9, cols=2)
    tbl_param.alignment = WD_TABLE_ALIGNMENT.CENTER
    param_data = [
        ("Parameters", "Description"),
        ("Name", "Name of the user seeking personalized recommendations (e.g., Emily Watson)."),
        ("Age", "Age of the user (e.g., 22)."),
        ("Background", "Academic or professional background (e.g., Computer Science Student)."),
        ("Interests", "Comma-separated topics of interest (e.g., Machine Learning, Cloud Computing)."),
        ("Skill Level", "User proficiency level (Beginner, Intermediate, or Advanced)."),
        ("Category", "Preferred resource category (Courses, Projects, Books, or Certifications)."),
        ("Goal", "Target career or academic learning objective (e.g., Become a Machine Learning Engineer)."),
        ("Count", "Target number of recommendations to generate (1 to 10; default: 5).")
    ]
    for r_idx, (p_name, desc) in enumerate(param_data):
        row = tbl_param.rows[r_idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(4.2)
        p0, p1 = c0.paragraphs[0], c1.paragraphs[0]
        p0.add_run(p_name).bold = (r_idx == 0)
        p1.add_run(desc).bold = (r_idx == 0)
        bg = "003366" if r_idx == 0 else ("F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
        set_cell_background(c0, bg)
        set_cell_background(c1, bg)
        if r_idx == 0:
            p0.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            p1.runs[0].font.color.rgb = RGBColor(255, 255, 255)
        set_cell_margins(c0, 50, 50, 100, 100)
        set_cell_margins(c1, 50, 50, 100, 100)
        for c in (c0, c1):
            tcPr = c._tc.get_or_add_tcPr()
            tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/></w:tcBorders>')
            tcPr.append(tcBorders)

    # 6. System Architecture
    add_styled_heading(doc, "System Architecture:")
    p_arch = doc.add_paragraph()
    p_arch.paragraph_format.space_before = Pt(2)
    p_arch.paragraph_format.space_after = Pt(6)
    p_arch.add_run(
        "The system architecture follows a modular pipeline comprising Profile Ingestion, Preference Synthesis, Structured "
        "Prompt Compilation, Local LLM Inference via Ollama (phi3), Suitability Sorting & Ranking, In-Depth Rationale Explanation, "
        "Dynamic User Feedback Adaptation, and Zero-Shot Intent Routing."
    )
    if os.path.exists(ARCH_DIAGRAM):
        add_screenshot(doc, ARCH_DIAGRAM, "Figure: System Architecture of the Personalized Recommendation System")

    # 7. Module Design
    add_styled_heading(doc, "Module Design:")
    mod_data = [
        ("Module", "Responsibility"),
        ("Profile Module", "Collects and validates user profile attributes, saving profile state to profile_state.json."),
        ("Preference Module", "Extracts primary and secondary interests and synthesizes academic complexity constraints."),
        ("Prompt Module", "Constructs structured system and user prompts enforcing the exact pipe-delimited recommendation format."),
        ("Recommendation Module", "Dispatches prompts to local Ollama (phi3) and parses output into structured item records."),
        ("Ranking Module", "Sorts recommendations in strict descending order of suitability score (0–100%) in an ASCII table."),
        ("Explanation Module", "Generates detailed personalized rationales explaining why each recommendation accelerates user goals."),
        ("Feedback Module", "Accepts qualitative user critiques to iteratively refine and regenerate adapted recommendations."),
        ("Intent Module", "Classifies user queries into discrete operational intents using zero-shot LLM classification.")
    ]
    tbl_mod = doc.add_table(rows=len(mod_data), cols=2)
    tbl_mod.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, (m_name, m_resp) in enumerate(mod_data):
        row = tbl_mod.rows[r_idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(4.2)
        p0, p1 = c0.paragraphs[0], c1.paragraphs[0]
        p0.add_run(m_name).bold = (r_idx == 0)
        p1.add_run(m_resp).bold = (r_idx == 0)
        bg = "003366" if r_idx == 0 else ("F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
        set_cell_background(c0, bg)
        set_cell_background(c1, bg)
        if r_idx == 0:
            p0.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            p1.runs[0].font.color.rgb = RGBColor(255, 255, 255)
        set_cell_margins(c0, 50, 50, 100, 100)
        set_cell_margins(c1, 50, 50, 100, 100)
        for c in (c0, c1):
            tcPr = c._tc.get_or_add_tcPr()
            tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/></w:tcBorders>')
            tcPr.append(tcBorders)

    # 8. Implementation
    add_styled_heading(doc, "Implementation:")

    # Snippet 1: Preference Analysis
    code_pref = '''def analyse_preferences(profile: dict, verbose: bool = True) -> dict:
    """Q3 - derive primary/secondary interests and constraints."""
    raw_interests = profile.get("interests", "")
    tokens = [t.strip() for t in raw_interests.split(",") if t.strip()]
    primary = tokens[0] if tokens else "General Computer Science"
    secondary = tokens[1] if len(tokens) > 1 else (tokens[0] if tokens else "Practical Applications")
    
    level = profile.get("skill_level", "Intermediate")
    goal = profile.get("goal", "Professional Growth")
    constraints = f"Must match {level} level learner focusing on: {goal}."

    return {
        "primary_interest": primary,
        "secondary_interest": secondary,
        "skill_level": level,
        "goal": goal,
        "preference": profile.get("category", "Courses"),
        "constraints": constraints
    }'''
    add_code_block(doc, "Preference and Constraint Analysis (profile_module.py)", code_pref)

    # Snippet 2: Prompt Construction
    code_prompt = '''def build_recommendation_prompt(profile: dict, analysis: dict) -> str:
    """Q4 - construct structured prompt for Ollama phi3."""
    return (
        f"User Profile:\\n"
        f"Name: {profile.get('name')}\\n"
        f"Background: {profile.get('background')}\\n"
        f"Interests: {profile.get('interests')}\\n"
        f"Skill Level: {analysis.get('skill_level')}\\n"
        f"Goal: {analysis.get('goal')}\\n"
        f"Preferred Category: {analysis.get('preference')}\\n\\n"
        f"Constraints: {analysis.get('constraints')}\\n\\n"
        f"Task: Recommend exactly {profile.get('count', 5)} items in this format:\\n"
        f"Name | Suitability Score (10-100) | Brief Reason"
    )'''
    add_code_block(doc, "Structured Prompt Construction (prompt_module.py)", code_prompt)

    # Snippet 3: Recommendation Generation and Parsing
    code_rec = '''def generate(profile: dict, analysis: dict, verbose: bool = True, extra_feedback: str = "") -> dict:
    """Q5 - generate personalized recommendations using local Ollama model."""
    user_prompt = prompt_module.build_recommendation_prompt(profile, analysis)
    if extra_feedback:
        user_prompt += f"\\n\\nUser Feedback Adjustment: {extra_feedback}"

    raw_output = utils.ask(prompt_module.SYSTEM_PROMPT, user_prompt, temperature=0.7)
    items = parse_items(raw_output, limit=profile.get("count", 5))
    result = {"profile": profile, "analysis": analysis, "items": items}
    utils.save_recommendations(result)
    return result'''
    add_code_block(doc, "Recommendation Generation and Parsing (recommendation_module.py)", code_rec)

    # Snippet 4: Ranking Engine
    code_rank = '''def rank(items: list, verbose: bool = True) -> list:
    """Q6 - rank recommendations by suitability score in descending order."""
    ranked = sorted(items, key=lambda x: x.get("score", 0), reverse=True)
    if verbose:
        print("RECOMMENDATION RANKING TABLE")
        print(utils.DASH)
        for i, item in enumerate(ranked, 1):
            print(f"Rank {i}: {item.get('name')} | Score: {item.get('score')}%")
    return ranked'''
    add_code_block(doc, "Suitability Ranking Engine (ranking_module.py)", code_rank)

    # Snippet 5: Intent Detection
    code_intent = '''def detect_intent(query: str, verbose: bool = True) -> str:
    """Q9 - classify user intent using zero-shot model inference."""
    raw = utils.ask(SYSTEM, f"User Input: {query}\\nClassify into INTENTS:\\nIntent:", temperature=0.0)
    for intent in ALLOWED_INTENTS:
        if intent.lower() in raw.lower():
            return intent
    return "GENERATE_RECOMMENDATION"'''
    add_code_block(doc, "Zero-Shot Intent Classification Router (intent_module.py)", code_intent)

    # 9. Links
    p_links_hdr = doc.add_paragraph()
    p_links_hdr.paragraph_format.space_before = Pt(8)
    p_links_hdr.paragraph_format.space_after = Pt(2)
    p_links_hdr.add_run("Links:").bold = True

    p_gh = doc.add_paragraph()
    p_gh.paragraph_format.space_before = Pt(1)
    p_gh.paragraph_format.space_after = Pt(1)
    p_gh.add_run("GitHub Link: ").bold = True
    p_gh.add_run("https://github.com/SanthoshV2005/24CS2506-Experiment-4-Recommendation-System")

    p_li = doc.add_paragraph()
    p_li.paragraph_format.space_before = Pt(1)
    p_li.paragraph_format.space_after = Pt(8)
    p_li.add_run("LinkedIn Post Link: ").bold = True

    # 10. Output Screenshots
    add_styled_heading(doc, "Output Screenshots:")
    
    screenshots = [
        ("01_main_menu.png", "Figure 1: Home Screen of the Personalized Recommendation System"),
        ("02_user_profile.png", "Figure 2: User Profile Input (Emily Watson)"),
        ("03_preference_analysis.png", "Figure 3: Preference and Constraint Analysis"),
        ("04_prompt_generation.png", "Figure 4: Structured Prompt Generation"),
        ("05_generated_recommendations.png", "Figure 5: Generated Recommendations with Suitability Scores"),
        ("06_ranking_table.png", "Figure 6: Recommendation Ranking Table in Descending Order"),
        ("07_explanations.png", "Figure 7: In-Depth Recommendation Explanations"),
        ("08_feedback_refinement.png", "Figure 8: User Feedback and Recommendation Refinement"),
        ("09_intent_detection.png", "Figure 9: Intent Detection Router"),
        ("10_saved_recommendations.png", "Figure 10: Recommendation Saved Successfully to Disk")
    ]

    for fname, caption in screenshots:
        fpath = os.path.join(SCREENSHOT_DIR, fname)
        add_screenshot(doc, fpath, caption)

    # 11. Result
    add_styled_heading(doc, "Result:")
    p_res = doc.add_paragraph()
    p_res.paragraph_format.space_before = Pt(2)
    p_res.paragraph_format.space_after = Pt(6)
    p_res.paragraph_format.line_spacing = Pt(13)
    p_res.add_run(
        "The AI-powered Personalized Recommendation System using Python and local Ollama (phi3) was successfully designed, "
        "implemented, evaluated, and demonstrated. The application effectively collected user profiles (Emily Watson), synthesized "
        "thematic preferences and constraints, generated personalized recommendations with suitability scores, ranked them in descending "
        "order, provided detailed personalized justifications, interactively refined outputs based on feedback, classified operational intents, "
        "and persisted reports to outputs/recommendations.txt."
    )

    doc.save(DOCX_OUTPUT)
    print(f"[SUCCESS] Experiment 4 concise Word record created at: {DOCX_OUTPUT}")

if __name__ == "__main__":
    build_word_record()
