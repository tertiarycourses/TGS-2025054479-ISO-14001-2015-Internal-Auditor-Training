#!/usr/bin/env python3
"""Build the WSQ Learner Guide for TGS-2025054479 as BOTH:
  * courseware/LG-<title>.docx  (WSQ cover, version control, TOC field, Arial 11, footer)
  * LG-<title>.md              (repo-root Markdown mirror, generated from the same source)

The step-by-step detail for every activity lives HERE (never on a slide), together with
the scenario, the questions, the model answers and the trainer debrief.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT

import course_data as C
import prodoc as P
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3

ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))
ASSETS = os.path.join(REPO, "courseware", "assets")
LOGO = os.path.join(ASSETS, "tertiary-infotech-logo.png")

VERSIONS = [
    ("1.0", "19 Apr 2025", "First version", "Tertiary Infotech Academy"),
    ("2.0", "8 May 2025", "Second version", "Tertiary Infotech Academy"),
    ("3.0", "—", "New format", "Tertiary Infotech Academy"),
    ("4.0", "17 Oct 2025", "Update company name", "Tertiary Infotech Academy"),
    ("5.0", C.VERSION_DATE,
     "Full content rebuild against ISO 14001:2015 and ISO 19011:2018. Adds the clause-by-"
     "clause reference, the Singapore compliance-obligation context, and three complete "
     "case-study activities (GreenPack, AquaPure, EcoTech) with full step-by-step "
     "guidance, questions, model answers and self-check criteria.",
     "Tertiary Infotech Academy"),
]

MD = []          # markdown mirror accumulates here


# ---------------------------------------------------------------- helpers
def h1(doc, t):
    MD.append(f"\n## {t}\n")
    x = doc.add_heading(t, level=1)
    for r in x.runs:
        r.font.name = "Arial"


def h2(doc, t):
    MD.append(f"\n### {t}\n")
    x = doc.add_heading(t, level=2)
    for r in x.runs:
        r.font.name = "Arial"


def h3(doc, t):
    MD.append(f"\n#### {t}\n")
    x = doc.add_heading(t, level=3)
    for r in x.runs:
        r.font.name = "Arial"


def para(doc, text, size=11, md=True):
    if md:
        MD.append(text + "\n")
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    P.md_runs(p, text, size=size)
    return p


def bullet(doc, text, size=11, md=True, prefix="- "):
    if md:
        MD.append(prefix + text)
    p = doc.add_paragraph(style="List Bullet")
    P.md_runs(p, text, size=size)
    return p


def numbered(doc, text, size=11, md=True, n=None):
    if md:
        MD.append(f"{n}. {text}" if n else text)
    p = doc.add_paragraph(style="List Number")
    P.md_runs(p, text, size=size)
    return p


def callout(doc, label, text, fill="F5F8FC", size=10.5):
    MD.append(f"\n> **{label}** {text}\n")
    t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"
    c = t.rows[0].cells[0]
    P.shade_cell(c, fill)
    c.text = ""
    p = c.paragraphs[0]
    r = p.add_run(label + "  ")
    r.bold = True; r.font.size = Pt(size); r.font.name = "Arial"
    r.font.color.rgb = P.BRAND
    P.md_runs(p, text, size=size)
    doc.add_paragraph()


def simple_table(doc, headers, rows, widths=None, size=9.5):
    MD.append("")
    MD.append("| " + " | ".join(headers) + " |")
    MD.append("|" + "|".join(["---"] * len(headers)) + "|")
    for r in rows:
        MD.append("| " + " | ".join(str(x).replace("\n", " ") for x in r) + " |")
    MD.append("")
    t = doc.add_table(rows=0, cols=len(headers))
    t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hr = t.add_row().cells
    for i, htext in enumerate(headers):
        hr[i].text = ""
        rr = hr[i].paragraphs[0].add_run(htext)
        rr.bold = True; rr.font.size = Pt(size); rr.font.name = "Arial"
        rr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        P.shade_cell(hr[i], "1F6FEB")
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]
            P.md_runs(p, str(val), size=size)
            for rr in p.runs:
                if i == 0:
                    rr.bold = True
    if widths:
        for row in t.rows:
            for i, c in enumerate(row.cells):
                c.width = Cm(widths[i])
    doc.add_paragraph()


def image(doc, name, width=6.2, caption=None):
    path = os.path.join(ASSETS, name)
    if not os.path.exists(path):
        return
    MD.append(f"\n![{caption or name}](courseware/assets/{name})\n")
    p = doc.add_paragraph(); p.alignment = 1
    p.add_run().add_picture(path, width=Inches(width))
    if caption:
        cp = doc.add_paragraph(); cp.alignment = 1
        r = cp.add_run(caption)
        r.italic = True; r.font.size = Pt(9); r.font.name = "Arial"
        r.font.color.rgb = P.GREY
        MD.append(f"*{caption}*\n")


# ---------------------------------------------------------------- build
def main():
    doc = Document()
    sec = doc.sections[0]
    sec.left_margin = sec.right_margin = Cm(2.2)
    sec.top_margin = sec.bottom_margin = Cm(2.0)
    P.style_base(doc)

    P.add_cover_page(doc, "Learner Guide", C.TITLE, "5.0", C.COURSE_CODE, org_logo=LOGO)
    P.add_version_control(doc, VERSIONS)
    P.add_toc(doc)

    MD.append(f"# Learner Guide — {C.TITLE}")
    MD.append(f"\n**TGS Ref No:** {C.COURSE_CODE}  ·  **Version:** 5.0  ·  "
              f"**{C.VERSION_DATE}**")
    MD.append(f"\n{C.ORG} ({C.UEN})\n")

    # ---------------- 1 About this course ----------------
    h1(doc, "1. About This Course")
    para(doc, f"This {C.TOTAL_HOURS}-hour course prepares you to plan, conduct, report and "
              f"follow up an **internal audit of an Environmental Management System (EMS)** "
              f"based on **ISO 14001:2015**, using the **International Professional Practices "
              f"Framework (IPPF)** and the auditing guidance of **ISO 19011:2018**.")
    para(doc, f"It runs over **{C.DAYS} days** — {C.TRAINING_HOURS} hours of facilitation "
              f"plus {C.ASSESSMENT_HOURS} hours of assessment — and is aligned to the "
              f"Skills Framework TSC **{C.TSC_TITLE} ({C.TSC_CODE}, {C.TSC_LEVEL})**.")

    h2(doc, "1.1 Learning Outcomes")
    for lo in C.LEARNING_OUTCOMES:
        bullet(doc, f"**{lo.split(':')[0]}:**{lo.split(':', 1)[1]}")

    h2(doc, "1.2 What Is Assessed")
    simple_table(doc, ["Code", "Statement", "Assessed by"],
                 [[c, d, "Written Assessment (SAQ)"] for c, d in C.TSC_KNOWLEDGE] +
                 [[c, d, "Case Study (CS)"] for c, d in C.TSC_ABILITIES],
                 widths=[1.6, 11.5, 4.0])

    h2(doc, "1.3 How to Use This Guide")
    para(doc, "Work through Topics 1–3 alongside the slides. Every activity in Section 5 "
              "gives you the full scenario, the step-by-step method, the questions to "
              "answer, and a self-check. **Both assessments are open book** — this guide is "
              "your primary reference, so annotate it freely during the course.")

    callout(doc, "IMPORTANT —",
            "ISO 14001:2015 was withdrawn on 15 April 2026 and replaced by ISO 14001:2026, "
            "with a 36-month transition for existing certificates. This course teaches the "
            "**2015 edition** because that is the edition most auditees are currently "
            "certified to, and it is the edition named in this course's approved scope. The "
            "10-clause high level structure is retained in the 2026 edition.",
            fill="FFF7E6")

    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # ---------------- 2 Topic 1 ----------------
    T = C.TOPICS[0]
    h1(doc, f"2. Topic 1 — {T['title']}")
    para(doc, f"**{T['lu']}**  ·  **{T['lo']}**  ·  Knowledge/Ability: **{T['ka']}**")

    h2(doc, "2.1 The International Professional Practices Framework (IPPF)  [K1]")
    para(doc, "The IPPF is the professional framework that governs how internal auditors "
              "behave and work. Four components are **mandatory**:")
    simple_table(doc, ["Component", "What it says", "What it means for you"],
                 [["Definition of Internal Auditing",
                   "An independent, objective assurance and consulting activity designed to "
                   "add value and improve an organisation's operations.",
                   "You are not an inspector and not a policeman — you add value by "
                   "improving risk management, control and governance."],
                  ["Code of Ethics",
                   "Integrity · Objectivity · Confidentiality · Competency.",
                   "You must not audit your own work, must not disclose what you learn, and "
                   "must decline (or get support for) work beyond your competence."],
                  ["Core Principles",
                   "Demonstrates integrity, competence and due professional care; is "
                   "objective and free from undue influence; aligns with strategy; is "
                   "insightful, proactive and future-focused.",
                   "Your audit plan should follow organisational risk, not organisational "
                   "convenience."],
                  ["International Standards",
                   "Attribute standards (who we are) and performance standards (what we do).",
                   "Engagements must be planned, evidenced, documented and reported."]],
                 widths=[3.8, 6.2, 6.5])

    h3(doc, "The Code of Ethics in practice")
    for t, d in [("Integrity", "Perform work with honesty, diligence and responsibility. "
                               "Do not knowingly be party to any illegal activity."),
                 ("Objectivity", "Maintain an unbiased mental attitude and avoid conflicts "
                                 "of interest. Do NOT audit an area for which you have "
                                 "operational responsibility."),
                 ("Confidentiality", "Respect the value and ownership of information "
                                     "received; do not use it for personal gain."),
                 ("Competency", "Apply the knowledge, skills and experience required. If a "
                                "process is beyond you technically, bring in a specialist.")]:
        bullet(doc, f"**{t}** — {d}")

    callout(doc, "AUDIT TIP —",
            "Record your independence in the audit plan BEFORE fieldwork starts. A single "
            "line — 'the auditor has no operational responsibility for the areas audited' — "
            "protects the whole engagement.")

    h2(doc, "2.2 ISO 14001:2015 and the EMS  [K1]")
    para(doc, "ISO 14001:2015 specifies the requirements for an environmental management "
              "system that an organisation can use to enhance its environmental "
              "performance. The standard's **three intended outcomes** are:")
    for i, (t, d) in enumerate([
            ("Enhancement of environmental performance",
             "the EMS must actually improve performance, not merely document what already "
             "happens"),
            ("Fulfilment of compliance obligations",
             "legal requirements the organisation has to comply with, and other "
             "requirements it has to or chooses to comply with"),
            ("Achievement of environmental objectives",
             "objectives consistent with the environmental policy and the significant "
             "environmental aspects")], 1):
        numbered(doc, f"**{t}** — {d}.", n=i)

    para(doc, "Two rules that catch new auditors out:")
    bullet(doc, "**There is no clause-exclusion mechanism.** Unlike ISO 9001, claims of "
                "conformity are not acceptable unless ALL requirements are incorporated and "
                "fulfilled.")
    bullet(doc, "**The standard sets no environmental performance levels.** It requires the "
                "organisation to set its own criteria and indicators (clause 9.1.1).")

    image(doc, "pdca_clauses.png", 6.0,
          "PDCA mapped to the clauses. Context (4.1/4.2) encircles the cycle.")

    h3(doc, "Verbal forms — what is actually auditable")
    simple_table(doc, ["Form", "Meaning", "Can you raise a nonconformity?"],
                 [["shall", "A requirement", "**Yes**"],
                  ["should", "A recommendation", "No"],
                  ["may", "A permission", "No"],
                  ["can", "A possibility or capability", "No"]],
                 widths=[2.5, 7.0, 7.0])
    callout(doc, "REMEMBER —",
            "ISO 19011:2018 is written entirely in 'should'. It is **guidance**. You audit "
            "against **ISO 14001 clause 9.2**, never 'against ISO 19011'.")

    h2(doc, "2.3 The Clauses You Audit — Clauses 4 to 10  [K1, K2]")
    image(doc, "clause_structure.png", 6.2,
          "The Annex SL high level structure. Clauses 4–10 carry every requirement.")

    for title, rows in [
        ("Clause 4 — Context of the organisation",
         [["4.1 Understanding the organisation and its context",
           "Determine external and internal issues, **including environmental conditions "
           "capable of affecting the organisation**. No documented information required."],
          ["4.2 Needs and expectations of interested parties",
           "Determine the parties, their relevant needs, and **which of those needs become "
           "compliance obligations**."],
          ["4.3 Determining the scope of the EMS",
           "Boundaries and applicability. **Maintained as documented information and "
           "available to interested parties.**"],
          ["4.4 Environmental management system",
           "Establish, implement, maintain and continually improve the EMS including the "
           "processes needed and their interactions."]]),
        ("Clause 5 — Leadership",
         [["5.1 Leadership and commitment",
           "Top management shall **demonstrate** leadership: accountability for EMS "
           "effectiveness, integration into business processes, ensuring resources. "
           "Non-delegable."],
          ["5.2 Environmental policy",
           "Commitments to protection of the environment (including prevention of "
           "pollution), to fulfil compliance obligations, and to continual improvement. "
           "Maintained, communicated, available."],
          ["5.3 Roles, responsibilities and authorities",
           "Assigned **and communicated**. The 2004 'management representative' role is no "
           "longer mandatory."]]),
        ("Clause 6 — Planning",
         [["6.1.1 General",
           "Determine **risks and opportunities** related to aspects, compliance obligations "
           "and 4.1/4.2 issues. Determine potential emergency situations."],
          ["6.1.2 Environmental aspects",
           "Determine aspects you **control and influence**, considering a **life cycle "
           "perspective**, **change**, **abnormal conditions** and **reasonably foreseeable "
           "emergencies**. Determine significance **by established criteria**."],
          ["6.1.3 Compliance obligations",
           "Determine and **have access to** them; determine **how they apply**; take them "
           "into account in the EMS."],
          ["6.1.4 Planning action",
           "Plan action on significant aspects, compliance obligations and risks and "
           "opportunities; integrate into EMS processes; **evaluate effectiveness**."],
          ["6.2.1 / 6.2.2 Environmental objectives",
           "Measurable if practicable, monitored, communicated, updated. Plan: **what · "
           "resources · who · when · how evaluated (with indicators)**."]]),
        ("Clause 7 — Support",
         [["7.1 Resources", "Determine and provide what the EMS needs."],
          ["7.2 Competence",
           "For work affecting environmental performance **and the ability to fulfil "
           "compliance obligations** — includes contractors. **Retain** evidence."],
          ["7.3 Awareness",
           "Policy · the significant aspects related to **their** work · their contribution "
           "to EMS effectiveness · implications of not conforming. Test by interview."],
          ["7.4 Communication",
           "What · when · with whom · how. Internal communication must let staff "
           "**contribute to continual improvement**."],
          ["7.5 Documented information",
           "Creating and updating (identification, format, review and approval) and control "
           "(availability, protection, distribution, storage, change, retention)."]]),
        ("Clause 8 — Operation",
         [["8.1 Operational planning and control",
           "Establish **operating criteria** and control to them. Control planned change; "
           "review unintended change. **Outsourced processes controlled or influenced.** "
           "Life cycle: design, procurement, external providers, end-of-life information."],
          ["8.2 Emergency preparedness and response",
           "Prepare · respond · mitigate · **periodically test** · review and revise "
           "(especially after an incident or test) · inform and train."]]),
        ("Clause 9 — Performance evaluation",
         [["9.1.1 Monitoring, measurement, analysis and evaluation",
           "What · methods ensuring valid results · **criteria and indicators** · when. "
           "Equipment **calibrated or verified**."],
          ["9.1.2 Evaluation of compliance",
           "Determine **frequency**; evaluate and **act if needed**; **maintain knowledge "
           "and understanding of compliance status**."],
          ["9.2.1 / 9.2.2 Internal audit",
           "At planned intervals, against ISO 14001 **and the organisation's own "
           "requirements**, and for **effective implementation**. Programme considers "
           "**environmental importance, changes and previous results**; auditors selected "
           "for **objectivity and impartiality**."],
          ["9.3 Management review",
           "Seven required inputs; six required outputs — including **implications for the "
           "strategic direction** of the organisation."]]),
        ("Clause 10 — Improvement",
         [["10.1 General",
           "Determine improvement opportunities from 9.1, 9.2 and 9.3."],
          ["10.2 Nonconformity and corrective action",
           "React and correct (**including mitigating environmental impacts**) · evaluate "
           "the need to **eliminate the cause** · check whether similar NCs exist elsewhere "
           "· implement · **review effectiveness** · change the EMS if needed."],
          ["10.3 Continual improvement",
           "Continually improve suitability, adequacy and effectiveness **to enhance "
           "environmental performance**."]])]:
        h3(doc, title)
        simple_table(doc, ["Sub-clause", "What the standard requires"], rows,
                     widths=[5.5, 11.0])

    h3(doc, "Documented information — maintain vs retain")
    para(doc, "The standard uses **maintain** for a document (how to do it) and **retain** "
              "for a record (evidence it was done). There are 15 mandatory items.")
    simple_table(doc, ["MAINTAIN (7 documents)", "RETAIN (8 records)"],
                 [["4.3 scope", "6.2.1 environmental objectives"],
                  ["5.2 environmental policy", "7.2 evidence of competence"],
                  ["6.1.1 risks and opportunities", "7.4.1 evidence of communications"],
                  ["6.1.2 aspects, criteria, significant aspects",
                   "9.1.1 monitoring and measurement results"],
                  ["6.1.3 compliance obligations", "9.1.2 compliance evaluation results"],
                  ["8.1 operational control", "9.2.2 audit programme and audit results"],
                  ["8.2 emergency preparedness", "9.3 management review results"],
                  ["—", "10.2 nature of NCs, actions taken, and corrective action results"]],
                 widths=[8.2, 8.3])
    callout(doc, "DO NOT RAISE THESE —",
            "There is **no required documented procedure** anywhere in ISO 14001:2015, "
            "**no environmental manual**, and **no preventive action procedure** (preventive "
            "action was deleted in the 2015 revision — clause 6.1 replaces it). Raising a "
            "nonconformity for any of these is a common and avoidable auditor error.",
            fill="FEF2F2")

    h2(doc, "2.4 Aspects, Impacts and Compliance Obligations  [K2]")
    image(doc, "aspect_impact.png", 6.2,
          "The aspect is the cause you control; the impact is the effect on the environment.")
    para(doc, "The **aspect** is the element of your activity that interacts with the "
              "environment. The **impact** is the resulting change to the environment — "
              "which may be **adverse or beneficial**.")
    simple_table(doc, ["Activity", "Aspect (cause)", "Impact (effect)", "Condition"],
                 [["PCB washing", "Discharge of trade effluent containing copper",
                   "Watercourse contamination; aquatic toxicity", "Normal"],
                  ["Solvent lamination", "Emission of VOCs",
                   "Air pollution; photochemical smog", "Normal"],
                  ["Boiler operation", "Emission of SO₂, NOₓ, particulates",
                   "Air pollution; acid deposition", "Normal"],
                  ["Chiller operation", "HFC refrigerant leakage",
                   "GHG emissions (high GWP); climate change", "Abnormal"],
                  ["Boiler cold start", "Elevated smoke and CO emissions",
                   "Air pollution — often the worst hourly rate", "Start-up"],
                  ["Chemical drum storage", "Potential release from bund failure",
                   "Soil and groundwater contamination", "**Emergency**"],
                  ["Waste segregation", "Recovery of recyclable material",
                   "Conserves resources — **beneficial**", "Normal"]],
                 widths=[3.2, 5.0, 5.4, 2.8])
    callout(doc, "RED FLAG —",
            "A register with **no beneficial aspects** and **no emergency aspects** has "
            "usually been copied rather than built. Ask how it was produced.")

    h3(doc, "Four methods for identifying aspects")
    for i, (t, d) in enumerate([
            ("Process mapping",
             "Flowchart each process step and interrogate every step for an environmental "
             "interaction."),
            ("Input–output analysis",
             "List what goes IN (materials, water, energy, chemicals, packaging) and what "
             "comes OUT (product, emissions, effluent, solid waste, noise, heat, odour). "
             "The **mass balance** is the auditor's best question: *'you purchased 500 L of "
             "solvent and disposed of 120 L — where did the other 380 L go?'* The answer is "
             "usually a fugitive emission that is not in the register."),
            ("Site walkthrough",
             "Walk the drains, stacks, vents, bunds, skips and storage areas. This catches "
             "the informal and undocumented."),
            ("Life cycle stages",
             "Raw materials → design → production → transport → use → end of life. Catches "
             "indirect aspects outside the fence.")], 1):
        numbered(doc, f"**{t}** — {d}", n=i)

    h3(doc, "Compliance obligations in the Singapore context")
    para(doc, "**Legal requirements** are what the organisation has to comply with. **Other "
              "requirements** are what it has to or chooses to comply with — and a voluntary "
              "commitment becomes auditable the moment the organisation adopts it "
              "(clause 4.2(c)).")
    simple_table(doc, ["Regime", "Regulator", "Evidence to ask for"],
                 [["Air emissions (EPMA)", "NEA",
                   "Source emission test reports from an accredited laboratory; stack/CEMS "
                   "records; **calibration certificates**"],
                  ["Trade effluent to public **sewer**", "PUB",
                   "**Written Approval** and its conditions; sampling results; pre-treatment "
                   "plant O&M logs; sanitary drainage plan"],
                  ["Trade effluent to **watercourse**", "NEA",
                   "Discharge limits (pH 6–9, TSS 50 mg/L, COD 100 mg/L to watercourse); "
                   "accredited laboratory analyses"],
                  ["Toxic industrial waste", "NEA",
                   "Collector's licence **covering that specific waste**; electronic "
                   "consignment notes (WRMS); transport approvals"],
                  ["General waste", "NEA",
                   "Contractor's **General Waste Collector licence** (1-year validity); "
                   "disposal tickets and weighbridge slips"],
                  ["Boundary noise", "NEA",
                   "Monitoring with a **Type 1** sound level meter; calibration "
                   "certificates; complaint register"],
                  ["Carbon tax", "NEA",
                   "Registration; Monitoring Plan; **verified** Emissions Report; activity "
                   "data and instrument calibration"],
                  ["Hazardous substances", "NEA",
                   "Hazardous Substances Licence and per-consignment permits; transaction "
                   "records; Safety Data Sheets"],
                  ["Energy Conservation Act", "NEA",
                   "Registration if ≥ 54 TJ/yr in 2 of 3 preceding years; appointed Energy "
                   "Manager; annual energy efficiency improvement plan"]],
                 widths=[3.6, 2.0, 10.8])
    callout(doc, "VERIFIED AS AT AUGUST 2026 —",
            "Carbon tax is **S$45/tCO₂e for 2026–2027**; a facility is **taxable at ≥ 25,000 "
            "tCO₂e** and **reportable at ≥ 2,000 tCO₂e**. Limits, thresholds and rates "
            "change. Audit the **method** by which the legal register is kept current "
            "(clause 6.1.3) and compliance is evaluated (clause 9.1.2) — do not treat any "
            "figure as permanent, and always date the figures in a legal register.",
            fill="FFF7E6")

    h2(doc, "2.5 Risks and Opportunities — and Objectives  [K2]")
    para(doc, "**Risks and opportunities (6.1.1) are not the same as environmental aspects "
              "(6.1.2).** Aspects are your physical interaction with the environment. Risks "
              "and opportunities are threats and opportunities to the **EMS achieving its "
              "intended outcomes** — and aspects are only one of their three inputs, "
              "alongside compliance obligations and the 4.1/4.2 issues.")
    callout(doc, "COMMON FAILURE —",
            "Relabelling the aspect register as the 'risk register' does **not** satisfy "
            "clause 6.1.1.", fill="FEF2F2")
    para(doc, "**Clause 6.2.2** requires five things for every objective. Use this as a "
              "checklist:")
    simple_table(doc, ["Requirement", "The question", "A weak answer"],
                 [["What will be done", "What are the actual actions?",
                   "'Improve energy efficiency' — that is the objective, not the plan"],
                  ["What resources", "Is the budget approved and released?",
                   "No capex and no headcount — a paper objective"],
                  ["Who is responsible", "Which **named role** owns it?",
                   "'The EHS department'"],
                  ["When completed", "Target date and milestones?", "'Ongoing'"],
                  ["How evaluated", "Which indicator, measured how and how often?",
                   "No indicator, or one with no calibrated measurement"]],
                 widths=[3.6, 6.4, 6.4])

    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # ---------------- 3 Topic 2 ----------------
    T = C.TOPICS[1]
    h1(doc, f"3. Topic 2 — {T['title']}")
    para(doc, f"**{T['lu']}**  ·  **{T['lo']}**  ·  Knowledge/Ability: **{T['ka']}**")

    h2(doc, "3.1 The Seven Audit Principles (ISO 19011:2018 Clause 4)  [K3]")
    simple_table(doc, ["Principle", "What it means"],
                 [["Integrity", "The foundation of professionalism — work honestly, "
                                "diligently and responsibly."],
                  ["Fair presentation", "Report truthfully and accurately — including "
                                        "unresolved disagreements between the team and the "
                                        "auditee."],
                  ["Due professional care", "Diligence and judgement appropriate to the "
                                            "importance of the task and the confidence "
                                            "placed in you."],
                  ["Confidentiality", "Security of information — do not use it for personal "
                                      "gain or to the auditee's detriment."],
                  ["Independence", "The basis for impartiality and objectivity — auditors "
                                   "do not audit their own work."],
                  ["Evidence-based approach", "The rational method for reaching reliable and "
                                              "**reproducible** conclusions."],
                  ["Risk-based approach", "Consider risks and opportunities — new in the "
                                          "2018 edition."]],
                 widths=[4.2, 12.3])

    h2(doc, "3.2 The Audit Programme vs the Individual Audit  [K3]")
    image(doc, "audit_lifecycle.png", 6.4,
          "Clause 5 manages the programme (the year). Clause 6 conducts one audit.")
    para(doc, "This distinction matters because most weaknesses you will find are "
              "**programme** weaknesses, and fixing one improves every future audit.")
    simple_table(doc, ["Programme-level finding (ISO 14001 cl. 9.2.2)",
                       "Audit-level finding (this one audit)"],
                 [["The audit procedure has not been updated after major change",
                   "The checklist does not cover the audit criteria"],
                  ["Equal audit time regardless of environmental risk",
                   "Evidence not verified before a finding was raised"],
                  ["Previous nonconformities closed without verification",
                   "A nonconformity statement missing its evidence"],
                  ["Auditors not competent or not impartial",
                   "No opening or closing meeting held"],
                  ["Results not reported to relevant management",
                   "The report omits the sampling limitation"]],
                 widths=[8.2, 8.3])

    h2(doc, "3.3 The Six-Stage Audit Lifecycle  [K3, A2]")
    for n, (stage, ref, items) in enumerate([
        ("Initiating the audit", "§6.2",
         ["Establish contact with the auditee and confirm your authority to audit.",
          "Confirm the audit is **feasible** — availability of information, cooperation, "
          "time and resources, and (critically) **access to every location in scope**."]),
        ("Preparing audit activities", "§6.3",
         ["**Review documented information**: the EMS documentation, previous audit reports "
          "and open corrective actions, the aspects register, the legal register, licences "
          "and monitoring data. Determine adequacy before you go on site.",
          "**Prepare the audit plan**: objectives, criteria, scope, locations, dates and "
          "times, methods, roles, and the opening and closing meeting times.",
          "**Assign work** to the audit team.",
          "**Prepare work documents** — the checklist and evidence-recording forms.",
          "**Decide the sampling approach** and be ready to justify it."]),
        ("Conducting audit activities", "§6.4",
         ["Hold the **opening meeting**.",
          "**Collect and verify** information — interview, observe, read documents, check "
          "records. Only verified information becomes audit evidence.",
          "**Generate audit findings** by evaluating evidence against the audit criteria.",
          "**Prepare audit conclusions** with the team.",
          "Hold the **closing meeting**."]),
        ("Preparing and distributing the report", "§6.5",
         ["Write the report so a reader who was not there understands what was found, where, "
          "and against which requirement.",
          "Distribute it to the recipients defined in the audit plan and to relevant "
          "management (ISO 14001 cl. 9.2.2)."]),
        ("Completing the audit", "§6.6",
         ["Complete all planned activities, retain or dispose of documents as agreed, and "
          "formally close the audit."]),
        ("Conducting audit follow-up", "§6.7",
         ["Verify that corrective actions were implemented **and effective** — required by "
          "ISO 14001 cl. 10.2(d).",
          "This is the stage most often skipped, and skipping it is what turns 'closed' "
          "findings into repeat findings."])], 1):
        h3(doc, f"Stage {n} — {stage}  ({ref})")
        for it in items:
            bullet(doc, it)

    h2(doc, "3.4 Building the Audit Checklist  [K3]")
    para(doc, "A good checklist is **organisation-specific** and **risk-weighted**, and "
              "every line has three columns.")
    simple_table(doc, ["Clause / requirement", "The question I will ask",
                       "The evidence I expect to see"],
                 [["6.1.2 aspects · change",
                   "How were aspects re-assessed after the new line was commissioned?",
                   "Dated register entry for the new process; the change record"],
                  ["6.1.3 compliance obligations",
                   "Which discharge limits apply to you, and how did you determine that?",
                   "Licence / Written Approval; legal register with applicability noted"],
                  ["7.2 competence",
                   "How did you determine the competence needed for this role?",
                   "Competence matrix; training records; evidence of effectiveness"],
                  ["8.1 operational control",
                   "What are the operating criteria for this process?",
                   "Work instruction with limits; monitoring records against them"],
                  ["9.1.1 monitoring",
                   "How do you know that monitoring result is valid?",
                   "**Calibration certificate in date**; accredited laboratory report"],
                  ["9.1.2 evaluation of compliance",
                   "How often do you evaluate compliance, and what did the last one find?",
                   "Compliance evaluation record and the actions arising"],
                  ["10.2 corrective action",
                   "How did you verify last year's corrective action worked?",
                   "Effectiveness review record — not merely a 'closed' status"]],
                 widths=[3.6, 6.4, 6.4])
    callout(doc, "AVOID —",
            "A generic clause-by-clause tick-list. It is the single most common weakness in "
            "internal audit practice: it produces the same findings every year and misses "
            "everything that actually changed.", fill="FEF2F2")

    h2(doc, "3.5 Audit Evidence and Sampling  [K3]")
    image(doc, "evidence_sources.png", 5.6,
          "Objective evidence comes from four sources — verify across at least two.")
    para(doc, "Evidence must be **sufficient** (enough of it) and **appropriate** (relevant "
              "and reliable), and **traceable** to its source.")
    bullet(doc, "**Interview** — what people say. The weakest form on its own; always verify.")
    bullet(doc, "**Observation** — what you see happening. Strong, but a snapshot in time.")
    bullet(doc, "**Documents** — what is supposed to happen (procedures, permits, licences).")
    bullet(doc, "**Records** — evidence that it did happen (results, certificates, logs).")
    para(doc, "**Sampling.** You cannot audit everything. Judgement-based sampling selects "
              "by risk (the newest process, the biggest aspect, the area with previous "
              "findings, the shift nobody watches); statistical sampling allows a confidence "
              "level to be stated. Record **what you sampled and why** — and put the "
              "sampling statement in the report.")
    callout(doc, "THE TEST —",
            "If you cannot explain why you looked at those three drums and not the other "
            "forty, your finding is vulnerable at the closing meeting.")

    h2(doc, "3.6 Questioning Technique  [A2]")
    image(doc, "question_funnel.png", 6.2,
          "The funnel: open → probing → closed → verify. Roughly 70% open/probing.")
    simple_table(doc, ["Type", "Use it to", "Example"],
                 [["Open", "Open a topic and let them talk",
                   "*'Walk me through what happens to the waste solvent.'*"],
                  ["Probing", "Push past the rehearsed answer",
                   "*'What happens if the reading is out of range?'*  *'How do you know?'*"],
                  ["Clarifying", "Remove ambiguity before you write anything down",
                   "*'When you say the bund is checked — by whom, and is it recorded?'*"],
                  ["Closed", "Confirm one specific fact, at the END",
                   "*'Is this the current revision?'*"],
                  ["Verify ('show me')", "Convert the answer into objective evidence",
                   "*'Show me the calibration certificate.'*"],
                  ["**Leading — never**", "Contaminates the evidence",
                   "*'You do calibrate that, don't you?'*"]],
                 widths=[3.0, 5.5, 8.0])

    h3(doc, "5W1H — so you miss no dimension")
    simple_table(doc, ["", "The question", "Applied to an EMS process"],
                 [["What", "What is done? What is the requirement?",
                   "What environmental aspects arise from this activity?"],
                  ["Why", "Why this way? Why this control?",
                   "Why was this aspect rated not significant?"],
                  ["Who", "Who does it? Who is competent or authorised?",
                   "Who is authorised to sign the waste consignment note?"],
                  ["Where", "Where is it done? Where is it recorded?",
                   "Where is the spill kit, and where is the nearest drain?"],
                  ["When", "When and how often? When last?",
                   "When was the emergency response last tested?"],
                  ["How", "How is it controlled, measured, verified?",
                   "How do you verify the disposal contractor is licensed?"]],
                 widths=[2.0, 6.5, 8.0])
    para(doc, "Two extensions worth using: **'how much / how many'** quantifies, and "
              "**'what if'** tests the abnormal and emergency conditions that clauses 6.1.2 "
              "and 8.2 require.")

    h3(doc, "PLOD — capturing traceable evidence as you find it")
    para(doc, "PLOD is a note-taking discipline (not an ISO term). Every observation in your "
              "working papers should carry as many of these as apply:")
    simple_table(doc, ["", "Capture", "Example"],
                 [["**P** — Person", "The **role**, never the individual's name",
                   "'the Warehouse Supervisor'"],
                  ["**L** — Location", "Building, area, line, tank",
                   "'Chemical Store B, external yard'"],
                  ["**O** — Object", "The physical thing with its identifier",
                   "'three 200 L drums, IDs WD-104/105/106'"],
                  ["**D** — Document", "Document identity **and revision or date**",
                   "'EMS-P-08 Rev 4, cl. 5.3'"]],
                 widths=[3.0, 6.5, 7.0])
    callout(doc, "THE TEST OF A GOOD NOTE —",
            "If your note carries none of P, L, O or D, you have an impression, not "
            "evidence. A finding must be **re-findable** six months later by someone else.")

    h3(doc, "What NOT to do in an interview")
    for it in ["**Leading questions** — they supply the answer and destroy the evidence.",
               "**Compound questions** — you will only get the last one answered.",
               "**Interrogating** — rapid-fire closed questions with no pauses.",
               "**Talking more than the auditee** — target under 30% of the airtime.",
               "**Filling the silence** — after a question, wait. The pause does the work.",
               "**Consulting mid-audit** — you become the author of what you must audit next "
               "year, and you lose independence.",
               "**Auditing the person** — 'why didn't *you* fill this in?' Reframe: 'what "
               "makes it hard to complete this log at shift change?'",
               "**Naming individuals in findings** — findings address the system.",
               "**Interviewing only managers** — the manager describes the procedure; the "
               "operator reveals the practice.",
               "**Accepting 'we always do it that way'** — that is an assertion. Show me."]:
        bullet(doc, it)

    h2(doc, "3.7 Opening and Closing Meetings  [A2]")
    h3(doc, "Opening meeting agenda")
    for i, it in enumerate(
            ["Introductions and roles — audit team, auditee representatives, guides.",
             "Confirm the audit plan: objectives, scope, criteria, timetable, closing "
             "meeting time.",
             "Confirm communication channels and how issues will be escalated.",
             "Explain the audit method and the **sampling basis**, and that sampling means "
             "the audit carries an element of uncertainty.",
             "Explain how findings will be **graded and reported**.",
             "Confirm safety, escort and facility arrangements.",
             "Invite questions and confirm agreement before fieldwork begins."], 1):
        numbered(doc, it, n=i)
    h3(doc, "Closing meeting agenda")
    for i, it in enumerate(
            ["Thank the auditee; restate the audit objective and scope.",
             "**Restate the sampling caveat** — absence of a finding is not proof of "
             "conformity.",
             "Present the findings, each with its evidence and grade, so they are understood "
             "and acknowledged.",
             "Present the audit conclusion on conformity **and** effective implementation.",
             "Agree the corrective action process, owners, timeframes and how effectiveness "
             "will be verified.",
             "**Record any diverging opinions** — unresolved disagreements are reported, "
             "never suppressed.",
             "Confirm report distribution, timing and the follow-up arrangement."], 1):
        numbered(doc, it, n=i)

    h2(doc, "3.8 Engaging the Stakeholders  [A2]")
    simple_table(doc, ["Group", "What you need from them", "How to engage"],
                 [["Operations staff", "What ACTUALLY happens",
                   "Interview at their normal workplace, put them at ease, open questions, "
                   "never blame"],
                  ["Process owners / managers", "The intended procedure and ownership of "
                                                "actions",
                   "Structured interview; then contrast what they say with what you observed"],
                  ["Top management", "Leadership (5.1), resources (7.1), programme decisions",
                   "Opening and closing meetings; direct interview for clause 5"],
                  ["Client representatives", "Site access and permission",
                   "**Not the auditee** — arrange in advance, observe their site rules, "
                   "protect confidentiality both ways"],
                  ["Regulators (NEA, PUB)", "The compliance position",
                   "**Indirectly** — licences, submitted returns, correspondence, notices. "
                   "An internal auditor does not interview the regulator"],
                  ["Contractors on site", "Competence and control of outsourced work",
                   "They work 'under the control of' the organisation — clauses 7.2 and 8.1 "
                   "apply to them"]],
                 widths=[3.4, 5.6, 7.5])

    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # ---------------- 4 Topic 3 ----------------
    T = C.TOPICS[2]
    h1(doc, f"4. Topic 3 — {T['title']}")
    para(doc, f"**{T['lu']}**  ·  **{T['lo']}**  ·  Knowledge/Ability: **{T['ka']}**")

    h2(doc, "4.1 Conducting the Risk Assessment  [K4]")
    para(doc, "ISO 14001 **prescribes no method** for determining significance. Clause 6.1.2 "
              "requires only that significant aspects are determined **by established "
              "criteria**, and that the criteria are documented. So the audit question is "
              "never *'is your method right?'* — it is *'is your method documented, "
              "criteria-based, consistently applied and reproducible?'*")
    image(doc, "risk_matrix.png", 5.4,
          "A 5×5 matrix: score = severity × likelihood. Significant at ≥ 10.")

    h3(doc, "Method 1 — Severity × Likelihood (5×5)")
    simple_table(doc, ["Score", "Band", "Action"],
                 [["1–4", "Low", "Not significant — maintain existing controls, review "
                                 "annually"],
                  ["5–9", "Medium", "Not significant — existing operational control, monitor"],
                  ["10–14", "High", "**SIGNIFICANT** — documented operational control (8.1) "
                                    "+ monitoring (9.1)"],
                  ["15–25", "Extreme", "**SIGNIFICANT — priority** — objective/programme "
                                       "required (6.2), escalate to management review"]],
                 widths=[2.5, 3.0, 11.0])

    h3(doc, "The override rules — what makes an aspect significant regardless of score")
    for it in ["It is subject to a **legal limit, licence or permit condition**.",
               "It has attracted a **regulatory notice, warning, fine or prosecution** in "
               "the last three years.",
               "It has generated a **substantiated external complaint**.",
               "It involves a **listed hazardous substance or toxic industrial waste**."]:
        bullet(doc, it)
    callout(doc, "WHY THIS MATTERS —",
            "Without override rules a licensed discharge can score 'medium' and drop off the "
            "significant list. That is the classic finding where the aspects register has "
            "become disconnected from the legal register.", fill="FEF2F2")

    h3(doc, "Method 2 — Multi-criteria scoring")
    para(doc, "Score = **Severity × Frequency × Legal exposure × Stakeholder concern**, each "
              "1–5. This builds compliance obligations (6.1.3) and interested parties (4.2) "
              "into the evaluation explicitly, which suits larger organisations. A weighted "
              "sum avoids the 'score explosion' of pure multiplication; the weights "
              "themselves then become documented criteria you must be able to justify.")

    h3(doc, "Method 3 — FMEA for environmental risk")
    simple_table(doc, ["Dimension", "What it rates", "The insight"],
                 [["Severity (S)", "How bad the environmental consequence is, 1–10",
                   "Usually cannot be reduced — a solvent stays toxic"],
                  ["Occurrence (O)", "How likely the failure mode is, 1–10",
                   "Reduced by maintenance, design and competence"],
                  ["Detection (D)", "Ability to detect **before** impact — inverted scale, "
                                    "1 = almost certain detection",
                   "The **cheapest and fastest** way to reduce risk"],
                  ["RPN = S × O × D", "1–1000; act at ≥ 100; any **S ≥ 9** acts regardless",
                   "Links straight to clause 9.1 monitoring"]],
                 widths=[3.2, 6.4, 6.9])
    para(doc, "**Worked example.** A cracked bund on a solvent tank: S = 9 (major off-site "
              "contamination), O = 4 (concrete degradation over years), D = 7 (monthly "
              "visual check only) → **RPN 252 — critical**. Install a leak-detection sensor "
              "and D falls to 2 → **RPN 72**. Same hazard, same likelihood — but now you "
              "find out before it reaches the soil.")

    h3(doc, "Auditing the significance method — questions that find weakness")
    simple_table(doc, ["Ask this", "A weak answer looks like"],
                 [["Show me the documented criteria for significance.",
                   "Criteria exist only in a spreadsheet formula or in someone's head"],
                  ["Who approved these criteria, and when?",
                   "No approval, no date, no version control"],
                  ["Would two assessors score this aspect the same? (Test it live.)",
                   "No calibration, no worked guidance, no examples"],
                  ["This aspect has a legal limit but scored 6. Explain.",
                   "No override rule for compliance obligations"],
                  ["Show me how each significant aspect flows to a control and to monitoring.",
                   "The register is standalone shelf-ware that nothing references"],
                  ["Why did significant aspects drop from 30 to 6 last year?",
                   "The threshold was quietly moved to reduce workload"]],
                 widths=[8.0, 8.5])

    h2(doc, "4.2 Writing Effective Nonconformity Statements  [A3]")
    image(doc, "nc_anatomy.png", 6.4,
          "Requirement + Evidence + Gap. Miss one and you have written an opinion.")
    image(doc, "nc_grading.png", 6.2,
          "Major, minor and OFI. The grading criteria come from your own audit procedure.")
    callout(doc, "WHERE GRADING CRITERIA COME FROM —",
            "ISO 19011 says only that findings *'can be graded'*. The major/minor criteria "
            "come from ISO/IEC 17021-1 and from **your organisation's own audit "
            "procedure**. Define them there and apply them consistently.")

    h3(doc, "Bad and good — rewrite every weak statement")
    simple_table(doc, ["Weak", "Why it fails", "Strong"],
                 [["'Housekeeping in the chemical store is poor.'",
                   "Opinion; no requirement, no evidence",
                   "'ISO 14001:2015 cl. 8.1 requires operational controls... On 14 Aug 2026 "
                   "three 200 L drums (WD-104/105/106) in Chemical Store B bore no contents "
                   "or hazard labels... therefore operational control for hazardous waste "
                   "storage is not implemented as required.'"],
                  ["'The operator did not follow the procedure.'",
                   "Blames a person; names no requirement",
                   "State the requirement, the observed evidence, and the systemic gap — not "
                   "the individual"],
                  ["'You should install a new bund.'",
                   "That is consulting, not a finding",
                   "State the nonconformity; let the auditee design the corrective action"],
                  ["'Training records were not very good.'",
                   "Vague; not traceable; not re-findable",
                   "Name the clause (7.2), the specific records examined, and what was "
                   "missing from them"]],
                 widths=[4.5, 4.0, 8.0])

    h2(doc, "4.3 Root Cause Analysis and Corrective Action  [A3]")
    image(doc, "five_whys.png", 6.0,
          "5 Whys: stop at a process gap, never at a person.")
    image(doc, "correction_vs_ca.png", 6.2,
          "Clause 10.2 requires BOTH correction and action to eliminate the cause.")
    para(doc, "**Correction** fixes the symptom (clean the spill, re-label the drum). "
              "**Corrective action** eliminates the cause so it does not recur or occur "
              "elsewhere (change the procedure, add the step, fix the schedule). Clause 10.2 "
              "requires both — a CAR that lists only corrections is incomplete.")

    h3(doc, "The anatomy of a corrective action request")
    for i, it in enumerate([
            "**The nonconformity statement** — requirement + evidence + gap, with the clause.",
            "**The grade and its justification** — major, minor or OFI, against your "
            "defined criteria.",
            "**Root cause** — reached by 5 Whys or fishbone; must be a **process or system** "
            "cause.",
            "**Correction** — what fixes the immediate problem and mitigates the "
            "environmental impact (10.2a).",
            "**Corrective action** — what eliminates the cause, plus whether **similar "
            "nonconformities exist elsewhere** (10.2b).",
            "**Owner and due date** — a named role and a real date.",
            "**Effectiveness verification** — how and when you will confirm it worked "
            "(10.2d), retained as documented information."], 1):
        numbered(doc, it, n=i)

    simple_table(doc, ["Weak corrective action", "Strong corrective action"],
                 [["'Operator re-trained.'",
                   "'Amended management-of-change procedure PR-12 to require an "
                   "environmental re-assessment before any volume or process change — "
                   "effective 1 Sep 2026, owner: EHS Manager.'"],
                  ["'Reminded staff at the toolbox talk.'",
                   "'Added bund integrity testing to the planned maintenance schedule at "
                   "12-month frequency, owner: Facilities Manager.'"],
                  ["'Increased management awareness.'",
                   "'Installed continuous pH monitoring with an interlocked shut-off on the "
                   "discharge line.'"],
                  ["'Will monitor more closely.'",
                   "Named owner, stated frequency, defined acceptance criterion, and a date "
                   "for the effectiveness review"]],
                 widths=[6.5, 10.0])
    callout(doc, "THE TEST —",
            "Would this corrective action survive the person leaving tomorrow? If not, you "
            "have a correction dressed up as a corrective action. Re-training is sometimes "
            "right — but only when the root cause genuinely is a competence gap, and then "
            "clause 7.2 requires you to evaluate the effectiveness of that training.")

    h2(doc, "4.4 Preparing the Audit Report  [A3]")
    for i, it in enumerate([
            "**Audit objectives, scope and criteria** — including anything excluded.",
            "**Audit team, auditees and dates.**",
            "**The audit findings**, each with its evidence, its clause and its grade.",
            "**The audit conclusion** — on conformity **and** on effective implementation "
            "and maintenance (ISO 14001 cl. 9.2.1 requires both).",
            "**The sampling statement** — that the audit was a sampling exercise and "
            "therefore carries uncertainty. This is the **most commonly omitted element** of "
            "real internal audit reports, and it protects both you and the organisation.",
            "**Opportunities for improvement**, kept clearly separate from nonconformities.",
            "**Agreed actions, owners and due dates**, and the follow-up arrangement.",
            "**Distribution list** — results must be reported to relevant management."], 1):
        numbered(doc, it, n=i)

    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # ---------------- 5 Activities ----------------
    h1(doc, "5. Hands-On Activities")
    para(doc, "Each activity is a case study run in small groups and debriefed by the "
              "trainer. Work through the steps in order; the questions at the end of each "
              "activity are deliberately similar in shape to the final assessment.")

    for a in ACTIVITIES:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        h2(doc, f"Activity {a['num']} — {a['title']}")
        para(doc, f"**Topic {int(a['topic'])}**  ·  **{a['minutes']} minutes**  ·  "
                  f"Assesses **{a['ka']}**")

        h3(doc, "Scenario")
        for block in a["scenario"].split("\n\n"):
            b = block.strip()
            if not b:
                continue
            if b.startswith("* "):
                for lineitem in b.split("\n"):
                    if lineitem.strip().startswith("* "):
                        bullet(doc, lineitem.strip()[2:])
            else:
                para(doc, b)

        h3(doc, "The evidence you have been given")
        for f in a["facts"]:
            bullet(doc, f)

        h3(doc, "Step-by-step method")
        for i, (title, detail) in enumerate(a["steps"], 1):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(f"Step {i}: {title}")
            r.bold = True; r.font.size = Pt(11); r.font.name = "Arial"
            r.font.color.rgb = P.BRAND
            MD.append(f"\n**Step {i}: {title}**\n")
            para(doc, detail, size=10.5)

        h3(doc, "Questions to answer")
        for i, (q, guide) in enumerate(a["questions"], 1):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(f"Q{i}. {q}")
            r.bold = True; r.font.size = Pt(11); r.font.name = "Arial"
            MD.append(f"\n**Q{i}. {q}**\n")
            para(doc, f"*What a good answer contains:* {guide}", size=10)

        h3(doc, "Self-check")
        callout(doc, "YOU ARE DONE WHEN —", a["test"], fill="E8F7EE")
        h3(doc, "If you are stuck — what usually goes wrong")
        for pf in a.get("pitfalls", []):
            bullet(doc, pf)

        h3(doc, "Model answer")
        for block in a["answers"].split("\n\n"):
            if block.strip():
                para(doc, block.strip(), size=10.5)

        h3(doc, "Trainer debrief")
        para(doc, a["debrief"], size=10.5)

    # ---------------- 6 Assessment ----------------
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h1(doc, "6. Preparing for the Assessment")
    para(doc, "The assessment has two instruments, both **open book** and completed "
              "individually on Day 2.")
    simple_table(doc, ["Instrument", "Format", "Duration", "Covers"],
                 [["Written Assessment — Short Answer Questions (WA/SAQ)",
                   "4 short-answer questions", "60 minutes", "K1, K2, K3, K4"],
                  ["Case Study (CS)", "3 scenario-based questions", "60 minutes",
                   "A1, A2, A3"]],
                 widths=[6.0, 4.5, 2.6, 3.4])
    para(doc, f"You must answer all questions correctly to be assessed **Competent (C)**. "
              f"Otherwise the outcome is **Not Yet Competent (NYC)** and re-assessment is "
              f"offered in line with the Assessment Plan. An appeal process is available.")

    h2(doc, "6.1 How to Prepare")
    for it in ["Re-read Section 2.3 (the clauses) and Section 4 (risk, CARs, reporting) — "
               "these carry the most assessable content.",
               "Redo Activity 1's clause mapping from memory: for each symptom, name the "
               "clause and say why.",
               "Practise writing three nonconformity statements in the "
               "requirement + evidence + gap structure.",
               "Be ready to distinguish: aspect vs impact; risk vs aspect; correction vs "
               "corrective action; 6.1.3 vs 9.1.2; programme vs individual audit.",
               "Bring this guide, the slides and your activity notes — the assessment is "
               "open book."]:
        bullet(doc, it)

    h2(doc, "6.2 Glossary")
    simple_table(doc, ["Term", "Definition (ISO 14001:2015 Clause 3)"],
                 [["Environmental aspect",
                   "Element of an organisation's activities or products or services that "
                   "interacts or can interact with the environment"],
                  ["Environmental impact",
                   "Change to the environment, whether adverse or beneficial, wholly or "
                   "partially resulting from an organisation's environmental aspects"],
                  ["Environmental condition",
                   "State or characteristic of the environment as determined at a certain "
                   "point in time"],
                  ["Interested party",
                   "Person or organisation that can affect, be affected by, or perceive "
                   "itself to be affected by a decision or activity"],
                  ["Compliance obligations",
                   "Legal requirements that an organisation has to comply with and other "
                   "requirements that an organisation has to or chooses to comply with"],
                  ["Life cycle",
                   "Consecutive and interlinked stages of a product (or service) system, "
                   "from raw material acquisition or generation from natural resources to "
                   "final disposal"],
                  ["Risk", "Effect of uncertainty"],
                  ["Risks and opportunities",
                   "Potential adverse effects (threats) and potential beneficial effects "
                   "(opportunities)"],
                  ["Nonconformity", "Non-fulfilment of a requirement"],
                  ["Corrective action",
                   "Action to eliminate the cause of a nonconformity and to prevent "
                   "recurrence"],
                  ["Continual improvement", "Recurring activity to enhance performance"],
                  ["Documented information",
                   "Information required to be controlled and maintained by an organisation "
                   "and the medium on which it is contained"],
                  ["Audit",
                   "Systematic, independent and documented process for obtaining audit "
                   "evidence and evaluating it objectively to determine the extent to which "
                   "the audit criteria are fulfilled"],
                  ["Environmental performance",
                   "Performance related to the management of environmental aspects"],
                  ["Prevention of pollution",
                   "Use of processes, practices, techniques, materials, products, services "
                   "or energy to avoid, reduce or control the creation, emission or "
                   "discharge of any type of pollutant or waste, in order to reduce adverse "
                   "environmental impacts"]],
                 widths=[4.5, 12.0])

    P.add_page_numbers(doc)
    P.enable_update_fields(doc)

    out = os.path.join(REPO, "courseware", f"LG-{C.SHORT_TITLE}.docx")
    doc.save(out)
    print("Saved", out)

    md_out = os.path.join(REPO, f"LG-{C.SHORT_TITLE}.md")
    with open(md_out, "w") as f:
        f.write("\n".join(MD) + "\n")
    print("Saved", md_out)


if __name__ == "__main__":
    main()
