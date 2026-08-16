#!/usr/bin/env python3
"""Build the ISO 14001:2015 Internal Auditor Training slide deck (TGS-2025054479).

2-day / 16-hour WSQ course -> house band is 100-150 slides.
Content sources: the approved LMS topic structure, ISO 14001:2015 and ISO 19011:2018,
and the verified Singapore regulatory research. Step-by-step procedure lives in the
Learner Guide, never on a slide.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from slide_lib import *          # noqa: F403
import slide_lib as L
from slide_lib import _ellipsis

ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3
L.set_footer(C.SHORT_TITLE, C.COURSE_CODE)

# ============================================================ COVER
cover(C, badge_top="ISO", badge_sub="14001:2015")

# ============================================================ ADMIN
mark("admin")
section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")

flow_h("Digital Attendance (Mandatory)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR with your phone camera",
    "Submit your attendance — AM, PM and Assessment",
    "Repeat on BOTH days of the course",
    "75% minimum attendance for assessment and funding",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=VIOLET,
   note="Digital attendance is mandatory for WSQ-funded courses and is the record SSG uses "
        "to determine your funding eligibility.")

trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
              "General Trainer template —\nto be completed by the trainer",
              [("Name", ""), ("Title / Designation", ""), ("Qualifications", ""),
               ("Areas of expertise", ""), ("Training & industry experience", ""),
               ("Contact", "")],
              initials="?", accent=GREY)

trainer_slide("YOUR TRAINER", C.TRAINER,
              "Principal Trainer\nTertiary Infotech Academy Pte Ltd",
              [("Role", "Principal Trainer, Tertiary Infotech Academy Pte Ltd"),
               ("Background", "PhD — 20+ years of industry and training experience in "
                              "management systems, quality and data analytics."),
               ("Delivers", "WSQ courses on ISO management system auditing, quality, "
                            "sustainability and data science."),
               ("Founder", "Founder and lead instructor at Tertiary Infotech / "
                           "Tertiary Courses.")],
              initials="AA", accent=BLUE)

content("Let's Know Each Other", [
    "Your name, organisation and role.",
    "Your experience with ISO 14001, EMS or internal auditing (if any) — and whether your "
    "organisation is certified.",
    "One environmental issue at your workplace you would like to be able to audit "
    "confidently by the end of Day 2.",
], kicker="ICE-BREAKER")

tile_grid("Ground Rules", [
    "Set your mobile phone to silent mode.",
    "Participate actively — no question is too small.",
    "Mutual respect: agree to disagree.",
    "One conversation at a time.",
    "Be punctual; return from breaks on time.",
    "75% attendance is required for funding.",
], kicker="HOUSEKEEPING", cols=2, size=14)

lms_slide(C.TITLE)

table_slide("Skills Framework Alignment",
            ["TSC element", "Detail"],
            [("TSC Title", C.TSC_TITLE),
             ("TSC Code", f"{C.TSC_CODE}  ·  Proficiency {C.TSC_LEVEL}")] +
            [(f"Knowledge {c}", d) for c, d in C.TSC_KNOWLEDGE] +
            [(f"Ability {c}", d) for c, d in C.TSC_ABILITIES],
            kicker="WSQ ALIGNMENT", widths=[0.20, 0.80], fsize=11,
            note="Every topic, activity and assessment item in this course maps to these "
                 "TSC knowledge and ability statements.")

tile_grid("Learning Outcomes",
          [(lo.split(": ")[0], lo.split(": ", 1)[1]) for lo in C.LEARNING_OUTCOMES],
          kicker="BY THE END OF THIS COURSE", cols=1, size=13)

two_panel("Course Outline — Three Topics Over Two Days",
          "DAY 1 — the standard and the framework",
          [("Topic 1 — ISO 14001:2015 Internal Auditor Framework", 0, True),
           ("Overview of the IPPF", 1),
           ("Introduction to ISO 14001:2015 and the EMS", 1),
           ("Applying ISO 14001:2015 to the organisation — risks, "
            "objectives, resources, operations", 1),
           ("Activity 1 — scoping a real engagement", 1),
           ("Topic 2 begins — audit methodologies", 0, True)],
          "DAY 2 — auditing and risk assessment",
          [("Topic 2 — Auditing ISO 14001:2015", 0, True),
           ("Phases of auditing and stakeholder engagement", 1),
           ("Activity 2 — audit plan, checklist and interviews", 1),
           ("Topic 3 — Risk Assessment", 0, True),
           ("Risk assessment · corrective action requests · audit reports", 1),
           ("Activity 3 — risk, CARs and the report", 1),
           ("Final assessment: WA (SAQ) then Case Study", 1)],
          kicker="THE JOURNEY", note="14 hours of facilitation + 2 hours of assessment = "
                                     "16 hours in total.")

# The two schedule slides are generated FROM THE LESSON PLAN's own schedule, so the
# deck and the LP can never disagree about the hours again.
from build_lesson_plan import DAY1 as _LP_D1, DAY2 as _LP_D2, _hours as _lp_hours, _ampm

def _sched_rows(day):
    """LP row -> compact deck row. Break rows are kept so the day reads correctly."""
    out = []
    for st, en, dur, topic, method, _res in day:
        first = topic.split("\n")[0].strip()
        if first in ("Tea Break", "Lunch Break"):
            out.append((f"{st}–{en}", first, "—"))
            continue
        # take the headline lines only; the bullet detail lives in the LP
        lines = [l.strip() for l in topic.split("\n") if l.strip()]
        head = [l for l in lines if not l.startswith("•")]
        label = " · ".join(head[:2]) if head else lines[0]
        out.append((f"{st}–{en}", _ellipsis(label, 78), _ellipsis(method, 26)))
    return out

_f1, _a1 = _lp_hours(_LP_D1)
_f2, _a2 = _lp_hours(_LP_D2)

table_slide("Lesson Plan — Day 1", ["Time", "Session", "Method"],
            _sched_rows(_LP_D1), kicker="SCHEDULE · DAY 1",
            widths=[0.17, 0.62, 0.21], fsize=10,
            note=f"{_f1 // 60} hours of facilitation ({_ampm(_LP_D1[0][0])} – "
                 f"{_ampm(_LP_D1[-1][1])}). Digital attendance is taken in the morning "
                 f"and again in the afternoon.")

table_slide("Lesson Plan — Day 2", ["Time", "Session", "Method"],
            _sched_rows(_LP_D2), kicker="SCHEDULE · DAY 2",
            widths=[0.17, 0.62, 0.21], fsize=10,
            note=f"{_f2 // 60} hours of facilitation + {_a2 // 60} hours of assessment "
                 f"({_ampm(_LP_D2[0][0])} – {_ampm(_LP_D2[-1][1])}). Course total: "
                 f"{(_f1 + _f2) // 60} h facilitation + {(_a1 + _a2) // 60} h assessment.")

mark("briefing")
tile_grid("Briefing for Assessment", [
    ("Phones away", "Place phones and all other materials under the table or on the floor."),
    ("No recording", "No photographs or recording of the assessment scripts."),
    ("Work alone", "No discussion with other learners during the assessment."),
    ("Black or blue pen", "No liquid paper and no correction tape."),
    ("Raise your hand", "The assessor will come to you if you have a question."),
    ("Time is called", "Scripts are collected when the time is up."),
], kicker="BEFORE THE ASSESSMENT", cols=2, size=14, accent=AMBER)

tile_grid("Final Assessment", [
    ("Written Assessment (SAQ)", "4 short-answer questions · 60 minutes · covers K1–K4."),
    ("Case Study (CS)", "3 scenario-based questions · 60 minutes · covers A1–A3."),
    ("Open book", "Slides, Learner Guide, activity briefs and your own notes."),
    ("Individual work", "Both instruments are completed individually."),
    ("Grading", f"{C.ASSESSMENT['grading']} — all answers must be correct to be Competent."),
    ("Appeals", "An appeal process is available if you disagree with the outcome."),
], kicker="FINAL ASSESSMENT", cols=2, size=14, accent=BLUE)

flow_h("Assessment Flow", [
    "TRAQOM — scan the QR code on the LMS",
    "Assessment digital attendance — scan the SSG QR",
    "Sit the WA (SAQ) 1 hr, then the Case Study 1 hr — open book",
    "Submit your answers on the LMS",
    "Sign the Assessment Summary Record",
], kicker="ON ASSESSMENT DAY")

tile_grid("Criteria for WSQ Funding", [
    ("Attendance", "Minimum 75% attendance based on the SSG digital attendance record."),
    ("Assessment", "Complete both instruments and be assessed as Competent (C)."),
    ("TRAQOM", "Complete the TRAQOM survey on the LMS."),
    ("SkillsFuture Credit", "Eligible individuals may use SkillsFuture Credit to offset "
                            "course fees. See www.skillsfuture.gov.sg."),
], kicker="ELIGIBILITY", cols=2, size=14)

# ============================================================ TOPIC 1
T = C.TOPICS[0]
mark("topic1")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])

big_statement("An internal audit is not an inspection.",
              "It is a systematic, independent and documented process for obtaining evidence "
              "and evaluating it objectively against agreed criteria.",
              "WHY WE ARE HERE", color=BLUE)

tile_grid("What an Internal EMS Auditor Actually Does", [
    ("Verifies conformity", "Tests the EMS against ISO 14001:2015 AND the organisation's own "
                            "requirements — clause 9.2.1 requires both."),
    ("Tests effectiveness", "Not just 'is there a procedure' but 'is it implemented, "
                            "maintained and working'."),
    ("Gathers objective evidence", "Records, documented information, observations and "
                                   "interview responses — never opinion."),
    ("Reports to management", "Findings go to the people who can act on them, and feed "
                              "clause 9.3 management review."),
    ("Supports improvement", "Findings drive corrective action under clause 10.2 and "
                             "continual improvement under 10.3."),
    ("Stays independent", "Auditors do not audit their own work — clause 9.2.2 requires "
                          "objectivity and impartiality."),
], kicker="THE ROLE", cols=2, size=13)

# ---- IPPF (K1) ----
section("K1 · KNOWLEDGE", "The International Professional Practices Framework", "1.1",
        "The professional framework that governs how internal auditors behave and work")

cards("The IPPF — Mandatory Guidance", [
    ("Definition of Internal Auditing",
     "An independent, objective assurance and consulting activity designed to add value "
     "and improve an organisation's operations, using a systematic, disciplined approach."),
    ("Code of Ethics",
     "Integrity · Objectivity · Confidentiality · Competency — the rules of conduct that "
     "govern auditor behaviour."),
    ("Core Principles",
     "The fundamental characteristics of effective internal auditing: integrity, competence, "
     "due professional care, objectivity, alignment with strategy, and insight."),
    ("International Standards",
     "The Standards for the Professional Practice of Internal Auditing — attribute standards "
     "(who we are) and performance standards (what we do)."),
], kicker="FOUR MANDATORY COMPONENTS", accent=BLUE,
   note="All four are MANDATORY. Conformance is required for anyone claiming to practise "
        "internal auditing under the IPPF — and each one is examinable in this course.")

tile_grid("The Code of Ethics — Four Principles in Practice", [
    ("Integrity", "Perform work with honesty, diligence and responsibility. Do not knowingly "
                  "be party to any illegal activity."),
    ("Objectivity", "Maintain an unbiased mental attitude. Do NOT audit an area where you "
                    "have operational responsibility."),
    ("Confidentiality", "Respect the value and ownership of information received; do not "
                        "disclose it without authority."),
    ("Competency", "Apply the knowledge, skills and experience needed. Decline — or get "
                   "support for — work you are not competent to do."),
], kicker="HOW ETHICS SHOWS UP IN AN AUDIT", cols=2, size=14, accent=VIOLET)

split_note("Independence and Objectivity — the Two Failure Modes",
           "✗  IMPAIRED — do not do this",
           [("Auditing the department you work in", 0, True),
            ("Auditing a procedure you personally wrote", 1),
            ("Auditing your own corrective actions from last year", 1),
            ("Accepting gifts or hospitality from the auditee", 1),
            ("Consulting mid-audit: 'what you should do is buy a new bund'", 1),
            ("Being pressured to downgrade a finding", 1)],
           "✓  INTACT — this is the standard",
           [("Auditing a department other than your own", 0, True),
            ("Declaring any prior involvement before the audit starts", 1),
            ("A second auditor verifies your own area", 1),
            ("Findings graded on evidence, not on how the auditee reacts", 1),
            ("You note the gap; the auditee designs the fix", 1),
            ("Impartiality recorded in the audit plan", 1)],
           kicker="ISO 14001 CL. 9.2.2 · IPPF OBJECTIVITY",
           note="Clause 9.2.2 requires the organisation to 'select auditors and conduct audits "
                "to ensure objectivity and the impartiality of the audit process'. In a small "
                "company, cross-departmental auditing is the usual solution.")

# ---- ISO 14001 & the EMS ----
section("K1 · KNOWLEDGE", "ISO 14001:2015 and the Environmental Management System", "1.2",
        "What the standard is, how it is structured, and what an EMS is for")

tile_grid("What is ISO 14001:2015?", [
    ("An EMS standard", "Specifies requirements for an environmental management system an "
                        "organisation can use to enhance its environmental performance."),
    ("Certifiable", "The requirements are auditable; organisations can be certified to it by "
                    "an accredited certification body."),
    ("No performance levels", "The standard does NOT state specific environmental performance "
                              "criteria — the organisation sets its own."),
    ("No exclusions", "Unlike ISO 9001, there is no clause-exclusion mechanism. All "
                      "requirements must be incorporated and fulfilled."),
], kicker="THE STANDARD IN ONE SLIDE", cols=2, size=14)

cards("The Three Intended Outcomes of an EMS", [
    ("Enhancement of environmental performance",
     "The EMS must actually improve how the organisation performs environmentally — not "
     "merely document what it already does."),
    ("Fulfilment of compliance obligations",
     "Legal requirements the organisation has to comply with, and other requirements it has "
     "to or chooses to comply with."),
    ("Achievement of environmental objectives",
     "Objectives set by the organisation, consistent with its environmental policy and its "
     "significant environmental aspects."),
], kicker="CLAUSE 1 · WHAT THE EMS IS FOR", accent=TEAL,
   note="Every audit finding you write should ultimately connect to one of these three "
        "outcomes. If it does not, ask yourself whether it is really a finding.")

img_full("PDCA — the Engine of the Standard", "pdca_clauses.png",
         kicker="THE STRUCTURE", accent=BLUE,
         caption="Plan (clauses 4–7) · Do (clause 8) · Check (clause 9) · Act (clause 10). "
                 "Context (4.1/4.2) encircles the whole cycle. Continual improvement is the "
                 "purpose, not a by-product.")

img_full("The 10 Clauses — Annex SL High Level Structure", "clause_structure.png",
         kicker="CLAUSES 4–10 · WHAT YOU AUDIT", accent=BLUE,
         caption="Clauses 1–3 are Scope, Normative references and Terms. Clauses 4–10 carry "
                 "every auditable requirement. The identical high level structure is what lets "
                 "ISO 14001 integrate with ISO 9001 and ISO 45001.")

table_slide("Verbal Forms — What Is Actually Auditable",
            ["Form", "Meaning", "Auditable?"],
            [("shall", "A requirement", "YES — non-fulfilment is a nonconformity"),
             ("should", "A recommendation", "No — cannot raise an NC against a 'should'"),
             ("may", "A permission", "No"),
             ("can", "A possibility or capability", "No")],
            kicker="READ THE STANDARD LIKE AN AUDITOR", widths=[0.14, 0.40, 0.46],
            accent=AMBER,
            note="ISO 19011 is written entirely in 'should' — it is GUIDANCE. You audit "
                 "against ISO 14001 clause 9.2, never 'against ISO 19011'.")

two_panel("What Changed: ISO 14001:2004 → 2015",
          "NEW OR STRENGTHENED",
          [("Context of the organisation (4.1, 4.2)", 0, True),
           ("Two-way: the organisation affects the environment AND environmental conditions "
            "affect the organisation", 1),
           ("Leadership (5.1) — top management must DEMONSTRATE leadership", 0, True),
           ("Risk-based thinking (6.1) — risks and opportunities", 0, True),
           ("Life cycle perspective (6.1.2, 8.1)", 0, True),
           ("Environmental performance emphasis (9.1.1, 10.3)", 0, True)],
          "REMOVED OR RENAMED",
          [("Preventive action — DELETED", 0, True),
           ("The whole of clause 6.1 IS the preventive mechanism. Never raise an NC for "
            "'no preventive action procedure'", 1),
           ("Management representative — no longer mandatory", 0, True),
           ("Duties remain but may be distributed (5.3)", 1),
           ("'Documents' + 'records' → 'documented information'", 0, True),
           ("'Objectives and targets' → 'environmental objectives'", 0, True)],
          kicker="THE 2015 REVISION", lcolor=TEAL, rcolor=AMBER,
          note="The single most common auditor error on a transitioned EMS: raising a finding "
               "for a missing preventive-action procedure or a missing environmental manual. "
               "Neither is required by ISO 14001:2015.")

# --- clause walkthrough ---
cards("Clause 4 — Context of the Organisation", [
    ("4.1 Issues",
     "Determine external and internal issues relevant to the EMS — INCLUDING environmental "
     "conditions capable of affecting the organisation. No documented information required."),
    ("4.2 Interested parties",
     "Determine the parties, their relevant needs, and CRUCIALLY which of those needs the "
     "organisation adopts as compliance obligations."),
    ("4.3 Scope",
     "Boundaries and applicability. MUST be maintained as documented information and be "
     "available to interested parties."),
    ("4.4 The EMS",
     "Establish, implement, maintain and continually improve the EMS including the processes "
     "needed and their interactions."),
], kicker="WHAT YOU AUDIT · CLAUSE 4", accent=BLUE,
   note="Audit tip: 4.1 and 4.2 require NO documented information. Do not demand a 'context "
        "document' — test by interview and by tracing whether context actually shaped the "
        "aspects, obligations and objectives.")

cards("Clause 5 — Leadership", [
    ("5.1 Leadership and commitment",
     "Top management shall DEMONSTRATE leadership: take accountability for EMS effectiveness, "
     "integrate EMS requirements into business processes, ensure resources. Non-delegable — "
     "interview top management directly."),
    ("5.2 Environmental policy",
     "Commitments to protection of the environment (including prevention of pollution), to "
     "fulfil compliance obligations, and to continual improvement. Maintained as documented "
     "information; communicated; available to interested parties."),
    ("5.3 Roles and responsibilities",
     "Assigned AND communicated. Specific assignment for EMS conformity and for reporting EMS "
     "performance to top management. The 'management representative' is no longer mandatory."),
], kicker="WHAT YOU AUDIT · CLAUSE 5", accent=VIOLET,
   note="The strongest leadership test is not the signed policy on the wall — it is whether "
        "top management can describe the organisation's significant environmental aspects "
        "without being prompted.")

img_points("Clause 6.1.2 — Environmental Aspects", "aspect_impact.png",
           [("Aspect = the CAUSE", "The element of your activity that interacts with the "
                                   "environment. You control it."),
            ("Impact = the EFFECT", "The change to the environment — adverse OR beneficial."),
            ("Control AND influence", "6.1.2 covers aspects you can control and those you can "
                                      "influence — not just inside the fence."),
            ("Criteria decide significance", "Determine significant aspects BY USING "
                                             "ESTABLISHED CRITERIA. The criteria are auditable.")],
           kicker="THE CORE CONCEPT OF THE STANDARD", accent=TEAL, img_w=6.6,
           note="The classic register errors: writing 'diesel generator' (that is equipment), "
                "or 'pollution' (that is an impact) in the aspect column.")

img_full("Determining Aspects — the Required Process", "aspect_process.png",
         kicker="CLAUSE 6.1.2 IN PRACTICE", accent=TEAL,
         caption="Clause 6.1.2 explicitly requires consideration of CHANGE (including new or "
                 "modified activities), of ABNORMAL conditions and of REASONABLY FORESEEABLE "
                 "EMERGENCY situations — and a life cycle perspective.")

table_slide("Aspects and Impacts — Worked Examples",
            ["Activity", "Environmental ASPECT (cause)", "Environmental IMPACT (effect)"],
            [("PCB washing", "Discharge of trade effluent containing copper",
              "Watercourse contamination; toxicity to aquatic life"),
             ("Solvent lamination", "Emission of VOCs from solvent-based adhesives",
              "Air pollution; photochemical smog"),
             ("Chiller operation", "Consumption of grid electricity; HFC refrigerant leakage",
              "Resource depletion; GHG emissions and climate change"),
             ("Chemical drum storage", "Potential release from bund failure (EMERGENCY)",
              "Soil and groundwater contamination"),
             ("Waste segregation", "Recovery of recyclable material",
              "Conserves resources — a BENEFICIAL impact")],
            kicker="GET THE COLUMNS RIGHT", widths=[0.18, 0.40, 0.42], fsize=11,
            accent=TEAL,
            note="A register with zero beneficial aspects and zero emergency aspects is a red "
                 "flag — it usually means the register was copied, not built.")

tile_grid("The Three Dimensions of a Complete Aspect Register", [
    ("Normal", "Routine, steady-state operation as designed."),
    ("Abnormal", "Predictable but non-routine: maintenance, cleaning, changeover, start-up "
                 "and shut-down — often the WORST emissions per hour."),
    ("Emergency", "Reasonably foreseeable: spill, fire, bund failure, power loss. Links "
                  "directly to clause 8.2."),
    ("Past · present · planned", "Legacy contamination, current operations, and planned "
                                 "changes — assessed BEFORE the change."),
    ("Direct (control)", "Own emissions, own effluent, own waste, own energy."),
    ("Indirect (influence)", "Supplier practices, contractor behaviour, product use, "
                             "end-of-life. Omitting these entirely is a common finding."),
], kicker="WHAT A GOOD REGISTER COVERS", cols=2, size=13, accent=TEAL)

cards("Clause 6.1.3 — Compliance Obligations", [
    ("Legal requirements",
     "What the organisation HAS TO comply with: EPMA and its regulations, EPHA, the "
     "Sewerage and Drainage Act, the Resource Sustainability Act, the Carbon Pricing Act, "
     "licences and permit conditions."),
    ("Other requirements",
     "What it HAS TO or CHOOSES TO comply with: customer contracts, corporate policies, "
     "industry codes, agreements with community groups."),
    ("The three duties",
     "(a) determine and HAVE ACCESS TO them; (b) determine HOW THEY APPLY; (c) TAKE THEM "
     "INTO ACCOUNT in the EMS. Maintained as documented information."),
], kicker="WHAT YOU AUDIT · CLAUSE 6.1.3", accent=AMBER,
   note="A bare register of law titles does not meet 6.1.3 — the organisation must have "
        "determined HOW each obligation applies to it. That interpretation is what you audit.")

table_slide("Singapore Compliance Obligations — What to Ask For",
            ["Regime", "Regulator", "Evidence an auditor asks to see"],
            [("Air emissions (EPMA)", "NEA",
              "Source emission test reports from an accredited lab; stack/CEMS records; "
              "calibration certificates"),
             ("Trade effluent to SEWER", "PUB",
              "Written Approval and its conditions; sampling results; pre-treatment O&M logs"),
             ("Trade effluent to WATERCOURSE", "NEA",
              "Discharge limits (e.g. pH 6–9, TSS 50 mg/L); accredited lab analyses"),
             ("Toxic industrial waste", "NEA",
              "Collector's licence covering THAT waste; e-consignment notes (WRMS); "
              "transport approvals"),
             ("Boundary noise", "NEA",
              "Monitoring by a Type 1 meter; calibration certificates; complaint register"),
             ("Carbon tax", "NEA",
              "Registration; Monitoring Plan; verified Emissions Report; calibration records"),
             ("Hazardous substances", "NEA",
              "Hazardous Substances Licence and permits; transaction records; SDS")],
            kicker="THE SINGAPORE CONTEXT", widths=[0.22, 0.13, 0.65], fsize=10,
            accent=AMBER,
            note="Verified as at August 2026. Limits, thresholds and rates change — audit the "
                 "METHOD of maintaining the legal register (6.1.3) and the evaluation of "
                 "compliance (9.1.2), not just this year's numbers.")

table_slide("Verified Singapore Figures — Use With a 'Verified As At' Date",
            ["Item", "Figure", "Source"],
            [("Carbon tax 2026–2027", "S$45 per tCO₂e", "NCCS / Carbon Pricing Act"),
             ("Carbon tax — taxable facility", "≥ 25,000 tCO₂e per year", "Carbon Pricing Act"),
             ("Carbon tax — reportable facility", "≥ 2,000 tCO₂e per year (report, no tax)",
              "Carbon Pricing Act"),
             ("Boundary noise — factory, day", "75 dB(A) over any 5-min period",
              "EPM (Boundary Noise) Regs"),
             ("Trade effluent to watercourse", "pH 6–9 · TSS 50 mg/L · COD 100 mg/L", "NEA"),
             ("Energy Conservation Act trigger", "≥ 54 TJ/yr in 2 of 3 preceding years",
              "ECA 2012")],
            kicker="FIGURES VERIFIED AUG 2026", widths=[0.34, 0.36, 0.30], fsize=11,
            accent=RED,
            note="Teach learners to date every figure in a legal register and to re-verify at a "
                 "defined frequency — that discipline is what clause 6.1.3 and 9.1.2 actually "
                 "require.")

tile_grid("Clause 4.1 — Context Works BOTH Ways", [
    ("The organisation affects the environment", "Emissions, effluent, waste, resource use — "
                                                 "the traditional view, and still clause 6.1.2."),
    ("The environment affects the organisation", "NEW in 2015: 'environmental conditions "
                                                 "capable of affecting the organisation'."),
    ("External issues", "Regulation, climate, resource scarcity and price, technology, "
                        "market and competitive pressure, community expectations."),
    ("Internal issues", "Activities, products and services, strategic direction, culture, "
                        "capabilities, and planned change."),
    ("Climate change is explicit", "The Feb 2024 amendment requires the organisation to "
                                   "determine whether climate change is a relevant issue."),
    ("No document required", "4.1 mandates no documented information — test whether context "
                             "actually shaped the aspects, obligations and objectives."),
], kicker="THE TWO-WAY TEST", cols=2, size=13, accent=BLUE)

process_map("How an Interested Party Need Becomes Auditable",
            [("Identify the party", "Neighbours, NEA, customers, landlord, employees"),
             ("Determine their need", "What they actually require or expect of you"),
             ("DECIDE — clause 4.2(c)", "Which needs the organisation ADOPTS"),
             ("It becomes an obligation", "Now a compliance obligation under 6.1.3"),
             ("Audit it", "Determined, applied, taken into account, and evaluated at 9.1.2")],
            kicker="CLAUSE 4.2(c) · THE GATEWAY", accent=VIOLET,
            synthesis="Not every expectation is a compliance obligation. A customer request "
                      "becomes one the moment it is written into a contract the organisation "
                      "signs — or the organisation otherwise chooses to comply. That decision "
                      "point is exactly what you audit.")

table_slide("Identifying Aspects — Four Methods That Actually Work",
            ["Method", "How it works", "What it catches"],
            [("Process mapping", "Flowchart each step, interrogate each for interaction",
              "Aspects inside repeatable production processes"),
             ("Input–output analysis",
              "Materials, water, energy, chemicals IN → product, emissions, effluent, waste OUT",
              "The MASS BALANCE gap — 'you bought 500 L of solvent and disposed of 120 L. "
              "Where did the rest go?'"),
             ("Site walkthrough", "Walk the drains, stacks, vents, bunds, skips, storage areas",
              "The informal and undocumented — the unbunded drum behind the workshop"),
             ("Life cycle stages", "Raw materials → design → production → transport → use → "
                                   "end of life",
              "Indirect aspects outside the fence that a register often misses")],
            kicker="TAKE THESE ON SITE", widths=[0.20, 0.40, 0.40], fsize=10.5, accent=TEAL,
            note="The mass-balance question is the single most productive aspect-audit "
                 "technique: unaccounted input is almost always an unregistered fugitive "
                 "emission.")

img_points("Risks and Opportunities are NOT Aspects", "risk_matrix.png",
           [("Aspect (6.1.2)", "Your interaction with the environment. Technical and physical."),
            ("Risk / opportunity (6.1.1)", "Threats and opportunities to the EMS achieving its "
                                           "intended outcomes. Strategic."),
            ("Aspects FEED risks", "Aspects are one input to 6.1.1 — along with compliance "
                                   "obligations and 4.1/4.2 issues."),
            ("The common failure", "Relabelling the aspect register as the 'risk register' "
                                   "does NOT meet clause 6.1.1.")],
           kicker="THE MOST MISUNDERSTOOD PART OF THE 2015 STANDARD", accent=VIOLET,
           img_w=6.2)

cards("Clause 6.2 — Environmental Objectives", [
    ("6.2.1 The objective",
     "Established at relevant functions and levels, taking account of significant aspects and "
     "associated compliance obligations. Consistent with policy, measurable if practicable, "
     "monitored, communicated, updated."),
    ("6.2.2 The plan — five parts",
     "WHAT will be done · WHAT RESOURCES · WHO is responsible · WHEN it completes · HOW "
     "results are evaluated, including indicators."),
    ("The audit test",
     "Trace each objective BACKWARDS to a significant aspect or obligation, and FORWARDS to "
     "9.1 monitoring evidence and 9.3 management review."),
], kicker="WHAT YOU AUDIT · CLAUSE 6.2", accent=GREEN,
   note="'Comply with all laws' and 'zero incidents' are not improvement objectives — they "
        "are baseline expectations. Challenge them.")

cards("Clause 7 — Support", [
    ("7.1 Resources · 7.2 Competence",
     "Determine and provide resources. Determine necessary competence for work affecting "
     "environmental performance and the ability to fulfil compliance obligations — including "
     "contractors. RETAIN evidence of competence."),
    ("7.3 Awareness",
     "Policy, the significant aspects related to THEIR work, their contribution to EMS "
     "effectiveness, and the implications of not conforming. No documented information "
     "required — test by interview."),
    ("7.4 Communication",
     "What, when, with whom and how. Internal communication must enable staff to CONTRIBUTE "
     "to continual improvement. External as required by compliance obligations."),
    ("7.5 Documented information",
     "Creating and updating (identification, format, review and approval); control "
     "(availability, protection, distribution, storage, change control, retention)."),
], kicker="WHAT YOU AUDIT · CLAUSE 7", accent=BLUE,
   note="Awareness ≠ competence. Ask an operator: 'which environmental aspects relate to YOUR "
        "job, and what happens if this goes wrong?' — that is a 7.3 test, and it is where "
        "paper systems fall over.")

cards("Clause 8 — Operation", [
    ("8.1 Operational planning and control",
     "Establish OPERATING CRITERIA and control processes in accordance with them. Control "
     "planned changes and review unintended changes. Ensure outsourced processes are "
     "controlled or influenced."),
    ("8.1 Life cycle perspective — four duties",
     "Environmental requirements in design and development · procurement requirements · "
     "communicate requirements to external providers including contractors · consider "
     "providing information on transport, use and end-of-life."),
    ("8.2 Emergency preparedness and response",
     "Prepare, respond, mitigate, PERIODICALLY TEST where practicable, review and revise "
     "(especially after an incident or a test), and provide information and training."),
], kicker="WHAT YOU AUDIT · CLAUSE 8", accent=AMBER,
   note="A full Life Cycle Assessment is NOT required. Ask instead: 'which life cycle stages "
        "did you consider, what did you conclude you can control or influence, and why?'")

cards("Clause 9 — Performance Evaluation", [
    ("9.1.1 Monitoring and measurement",
     "What to monitor, methods ensuring valid results, the CRITERIA and INDICATORS for "
     "evaluating performance, and when. Equipment must be CALIBRATED OR VERIFIED."),
    ("9.1.2 Evaluation of compliance",
     "Determine the FREQUENCY of evaluation, evaluate and act, and MAINTAIN KNOWLEDGE AND "
     "UNDERSTANDING of compliance status. Retain the results."),
    ("9.2 Internal audit",
     "At planned intervals, testing conformity to ISO 14001 AND the organisation's own "
     "requirements, and effective implementation. The programme must consider environmental "
     "importance, changes, and previous results."),
    ("9.3 Management review",
     "Seven required inputs and six required outputs — including implications for the "
     "STRATEGIC DIRECTION of the organisation."),
], kicker="WHAT YOU AUDIT · CLAUSE 9", accent=VIOLET,
   note="9.1.2 is NOT the same as 6.1.3, and NOT the same as 9.2. 6.1.3 asks 'which "
        "obligations apply?'; 9.1.2 asks 'are we actually complying?'; 9.2 audits the system.")

cards("Clause 10 — Improvement", [
    ("10.1 General",
     "Determine opportunities for improvement from 9.1, 9.2 and 9.3, and implement actions "
     "to achieve the intended outcomes of the EMS."),
    ("10.2 Nonconformity and corrective action",
     "React and correct · evaluate the need to eliminate the CAUSE · determine whether "
     "similar nonconformities exist or could occur · implement · REVIEW EFFECTIVENESS · "
     "change the EMS if necessary. Retain evidence of both the NC and the results."),
    ("10.3 Continual improvement",
     "Continually improve the suitability, adequacy and effectiveness of the EMS TO ENHANCE "
     "ENVIRONMENTAL PERFORMANCE."),
], kicker="WHAT YOU AUDIT · CLAUSE 10", accent=GREEN,
   note="10.2(d) — 'review the effectiveness of any corrective action taken' — is the clause "
        "that makes 'closed without verification' a nonconformity in its own right.")

table_slide("Documented Information — MAINTAIN vs RETAIN",
            ["", "MAINTAIN (a document — how to do it)", "RETAIN (a record — evidence it was done)"],
            [("Clause 4–6", "4.3 scope · 5.2 policy · 6.1.1 risks & opportunities · "
                            "6.1.2 aspects, criteria, significant aspects · 6.1.3 obligations",
              "6.2.1 environmental objectives"),
             ("Clause 7", "—", "7.2 competence · 7.4.1 communications"),
             ("Clause 8", "8.1 operational control · 8.2 emergency", "—"),
             ("Clause 9", "—", "9.1.1 monitoring results · 9.1.2 compliance evaluation · "
                               "9.2.2 audit programme and results · 9.3 management review"),
             ("Clause 10", "—", "10.2 nature of NCs, actions taken, and results of "
                                "corrective action")],
            kicker="15 MANDATORY ITEMS · 7 MAINTAIN + 8 RETAIN", widths=[0.13, 0.44, 0.43],
            fsize=10, accent=BLUE,
            note="There is NO required documented procedure anywhere in ISO 14001:2015, and NO "
                 "environmental manual. Never raise a nonconformity for their absence.")

big_statement("ISO 14001:2015 was withdrawn on 15 April 2026 and replaced by ISO 14001:2026.",
              "Certificates issued to the 2015 edition remain valid through a 36-month "
              "transition. The 10-clause high level structure is retained. This course teaches "
              "the 2015 edition because that is what most auditees are still certified to.",
              "TRANSITION AWARENESS", color=AMBER)

# ---- Activity 1 ----
mark("act1")
activity_slide(ACTIVITIES[0])
verify_slide(ACTIVITIES[0])

brk("Tea Break", "15 minutes")

# ============================================================ TOPIC 2
T = C.TOPICS[1]
mark("topic2")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])

big_statement("ISO 19011 tells you HOW to audit. ISO 14001 clause 9.2 says you MUST.",
              "ISO 19011:2018 is written entirely in 'should' — it is guidance, not "
              "requirements. You never raise a nonconformity 'against ISO 19011'.",
              "GET THIS RIGHT FIRST", color=TEAL)

tile_grid("The Seven Audit Principles — ISO 19011:2018 Clause 4", [
    ("Integrity", "The foundation of professionalism — perform work honestly, diligently and "
                  "responsibly."),
    ("Fair presentation", "The obligation to report truthfully and accurately — including "
                          "unresolved disagreements."),
    ("Due professional care", "Diligence and judgement appropriate to the importance of the "
                              "task and the confidence placed in the auditor."),
    ("Confidentiality", "Security of information — auditors must not use information for "
                        "personal gain or to the detriment of the auditee."),
    ("Independence", "The basis for impartiality and objectivity of the audit conclusions — "
                     "auditors do not audit their own work."),
    ("Evidence-based approach", "The rational method for reaching reliable and REPRODUCIBLE "
                                "conclusions in a systematic process."),
    ("Risk-based approach", "An audit approach that considers risks and opportunities — new "
                            "in the 2018 edition."),
], kicker="THE PROFESSIONAL FOUNDATION", cols=2, size=13, accent=TEAL)

img_full("Audit Programme vs Individual Audit", "audit_lifecycle.png",
         kicker="THE DISTINCTION MOST COURSES SKIP", accent=BLUE,
         caption="Clause 5 manages the PROGRAMME — the whole schedule of audits for the year. "
                 "Clause 6 conducts ONE audit. ISO 14001 clause 9.2.2 requires the programme to "
                 "consider environmental importance, changes, and previous audit results.")

two_panel("Programme Findings vs Audit Findings",
          "PROGRAMME-LEVEL (ISO 14001 cl. 9.2.2)",
          [("The audit procedure has not been updated after major change", 1),
           ("Equal audit time regardless of environmental risk", 1),
           ("Previous nonconformities closed without verification", 1),
           ("Auditors not competent or not impartial", 1),
           ("Results not reported to relevant management", 1),
           ("The programme itself is not monitored or improved", 1)],
          "AUDIT-LEVEL (this one audit)",
          [("A checklist that does not cover the audit criteria", 1),
           ("Evidence not verified before a finding is raised", 1),
           ("A nonconformity statement missing its evidence", 1),
           ("No opening or closing meeting held", 1),
           ("The report omits the sampling limitation", 1),
           ("Findings not agreed with the auditee before reporting", 1)],
          kicker="TWO DIFFERENT CONVERSATIONS", lcolor=VIOLET, rcolor=BLUE,
          note="Fixing a programme finding improves every future audit. Fixing an audit "
               "finding improves one. Know which one you are looking at.")

process_map("The Six-Stage Audit Lifecycle",
            [("Initiating", "Contact the auditee · confirm feasibility and authority"),
             ("Preparing", "Document review · audit plan · work assignment · checklist"),
             ("Conducting", "Opening meeting · collect and VERIFY · findings · closing"),
             ("Reporting", "Prepare and distribute the audit report"),
             ("Completing", "Distribute · retain records · close the audit"),
             ("Follow-up", "Verify the corrective actions were effective")],
            kicker="ISO 19011:2018 §6.2 – §6.7", accent=BLUE,
            synthesis="Every commercial provider researched teaches this same sequence. Stage 6 "
                      "is the one organisations most often skip — and skipping it is what turns "
                      "'closed' nonconformities into repeat findings.")

stack("Clause 5 — Managing the Audit Programme", [
    ("Establish programme objectives", "Driven by management priorities, the significant "
                                       "aspects, compliance obligations and previous results."),
    ("Determine programme risks and opportunities", "Resourcing, scheduling, auditor "
                                                    "competence, access, and ineffective "
                                                    "follow-up."),
    ("Establish the programme", "Frequency, methods, responsibilities, planning requirements "
                                "and reporting — ISO 14001 cl. 9.2.2."),
    ("Implement it", "Schedule audits, select and assign competent auditors, manage records."),
    ("Monitor it", "Are audits happening on schedule? Are findings being closed? Are auditors "
                   "performing?"),
    ("Review and improve it", "Feed the programme's own performance back into next year's "
                              "programme."),
], kicker="ISO 19011 CLAUSE 5 · THE YEAR, NOT THE DAY", accent=VIOLET,
   note="ISO 14001 cl. 9.2.2 requires the programme to take into account the environmental "
        "importance of the processes concerned, changes affecting the organisation, and the "
        "results of previous audits. All three are directly auditable.")

cards("Sampling — Why Every Audit Report Carries a Caveat", [
    ("You cannot audit everything",
     "An audit examines a SAMPLE of evidence within a finite time. That is not a weakness — "
     "it is the definition of auditing."),
    ("Judgement-based sampling",
     "Chosen by risk: the newest process, the biggest aspect, the area with previous findings, "
     "the shift nobody watches. Most internal audits use this."),
    ("Statistical sampling",
     "Random selection allowing a confidence level to be stated. Used where populations are "
     "large and homogeneous, e.g. thousands of waste tickets."),
    ("State the basis and its limit",
     "Record what you sampled and why — and put the sampling statement in the report. Absence "
     "of a finding is NOT proof of conformity."),
], kicker="ISO 19011 A.6", accent=BLUE,
   note="If you cannot explain WHY you looked at those three drums and not the other forty, "
        "your finding is vulnerable at the closing meeting.")

process_map("Following an Audit Trail",
            [("Start at a claim", "'All hazardous waste goes to a licensed collector'"),
             ("Ask for the record", "Show me last month's consignment notes"),
             ("Verify the counterparty", "Is the collector licensed for THAT waste stream?"),
             ("Reconcile the quantities", "Do the notes match the waste actually generated?"),
             ("Close or escalate", "Consistent → conformity. Gap → collect more evidence")],
            kicker="TRACEABILITY IN PRACTICE", accent=TEAL,
            synthesis="An audit trail is a chain: claim → record → verification → "
                      "reconciliation. Each link is a chance to find the gap, and the whole "
                      "chain is what makes a finding defensible six months later.")

stack("Stage 2 — Preparing: What Actually Happens", [
    ("Review documented information",
     "The EMS documentation, previous audit reports, the aspects register, the legal "
     "register, licences and monitoring data. Determine adequacy BEFORE you go on site."),
    ("Prepare the audit plan",
     "Objectives, criteria, scope, locations, dates and times, methods, roles, and the "
     "opening and closing meeting times. Agreed with the auditee."),
    ("Assign work to the audit team",
     "Who audits which process, which clause, which shift, which site."),
    ("Prepare work documents",
     "The checklist, sampling plans and forms for recording evidence. These are working "
     "papers — they are retained."),
    ("Decide the sampling approach",
     "How many, which ones, over what period — and be ready to justify it. Sampling is why "
     "every audit report carries the uncertainty caveat."),
], kicker="ISO 19011 §6.3", accent=BLUE,
   note="An audit that is under-prepared cannot be rescued on site. Most weak audits fail here.")

cards("The Audit Checklist — What Makes One Good", [
    ("Organisation-specific",
     "Built from THIS auditee's processes, aspects and obligations. A generic clause-by-clause "
     "tick-list is the single most common weakness."),
    ("Risk-weighted",
     "More lines against the significant aspects, the recent changes and the previous "
     "findings; fewer against low-risk administrative processes."),
    ("Three columns minimum",
     "The CLAUSE or requirement · the QUESTION you will ask · the EVIDENCE you expect to see. "
     "The third column is what most checklists omit."),
    ("A guide, not a script",
     "Follow the audit trail where it leads. A checklist that stops you investigating "
     "something you have just discovered is being used wrongly."),
], kicker="WORK DOCUMENTS · §6.3.4", accent=TEAL,
   note="Bureau Veritas and TÜV SÜD both single out checklist customisation as a core skill. "
        "Build it from the aspects register, not from the standard's contents page.")

table_slide("A Risk-Based Checklist Line — the Shape",
            ["Clause / requirement", "The question I will ask", "Evidence I expect to see"],
            [("6.1.2 aspects · change",
              "How were aspects re-assessed after the new line was commissioned?",
              "Dated register entry for the new process; the change record"),
             ("6.1.3 obligations",
              "Which discharge limits apply to you, and how did you determine that?",
              "Licence/Written Approval; legal register with applicability noted"),
             ("9.1.1 monitoring",
              "How do you know the monitoring result is valid?",
              "Calibration certificate in date; accredited lab report"),
             ("9.1.2 compliance",
              "How often do you evaluate compliance, and what did the last one find?",
              "Compliance evaluation record and the actions arising"),
             ("10.2 corrective action",
              "How did you verify last year's corrective action worked?",
              "Effectiveness review record — NOT just a 'closed' status")],
            kicker="COPY THIS STRUCTURE", widths=[0.22, 0.40, 0.38], fsize=10, accent=TEAL)

img_points("Audit Evidence — the Four Sources", "evidence_sources.png",
           [("Interview", "What people say. The weakest form on its own — always verify it."),
            ("Observation", "What you see happening. Strong, but a snapshot in time."),
            ("Documents", "Procedures, permits, licences, drawings — what is SUPPOSED to happen."),
            ("Records", "Monitoring results, certificates, logs — evidence it DID happen."),
            ("The test", "Sufficient, appropriate, verifiable and TRACEABLE to its source.")],
           kicker="OBJECTIVE EVIDENCE · ISO 19011", accent=BLUE, img_w=6.4,
           note="An interview answer alone rarely closes a line of enquiry. Either you saw it, "
                "or there is a record of it, or you have not verified it.")

img_full("Questioning Technique — the Funnel", "question_funnel.png",
         kicker="WHERE MOST NEW AUDITORS FAIL", accent=TEAL,
         caption="Roughly 70% open and probing, 30% closed. A funnel that STARTS closed ('do "
                 "you have a procedure?') gets a yes and teaches you nothing.")

table_slide("5W1H — Guaranteeing You Miss No Dimension",
            ["", "The question", "Applied to an EMS process"],
            [("What", "What is done? What is the requirement?",
              "What environmental aspects arise from this activity?"),
             ("Why", "Why is it done this way? Why this control?",
              "Why was this aspect rated not significant?"),
             ("Who", "Who does it? Who is competent or authorised?",
              "Who is authorised to sign the waste consignment note?"),
             ("Where", "Where is it done? Where is it recorded?",
              "Where is the spill kit, and where is the nearest drain?"),
             ("When", "When is it done? How often? When last?",
              "When was the emergency response last tested?"),
             ("How", "How is it controlled, measured, verified?",
              "How do you verify the disposal contractor is licensed?")],
            kicker="THE SYSTEMATIC QUESTION SET", widths=[0.10, 0.42, 0.48], fsize=10.5,
            accent=BLUE,
            note="Two extensions worth teaching: 'how much / how many' quantifies, and "
                 "'what if' tests the abnormal and emergency conditions clause 6.1.2 and 8.2 "
                 "require.")

split_note("Interviewing — What Works and What Destroys Evidence",
           "✗  NEVER DO THIS",
           [("Leading: 'you do calibrate that, don't you?'", 1),
            ("Compound: three questions in one breath", 1),
            ("Interrogating: rapid-fire closed questions", 1),
            ("Talking more than the auditee", 1),
            ("Consulting: 'what you should do is…'", 1),
            ("Naming individuals in a finding", 1),
            ("Interviewing only managers", 1),
            ("Accepting 'we always do it that way'", 1)],
           "✓  DO THIS INSTEAD",
           [("Open first: 'walk me through what happens…'", 1),
            ("One question, then WAIT — the pause does the work", 1),
            ("Explain why you are there and why you take notes", 1),
            ("Target: the auditor talks less than 30% of the time", 1),
            ("Note the gap; let the auditee design the fix", 1),
            ("Address the system, never the person", 1),
            ("Managers describe the procedure; operators reveal the practice", 1),
            ("'Show me' — convert every claim into evidence", 1)],
           kicker="ISO 19011 A.17 · CONDUCTING INTERVIEWS",
           note="Interviewing is the largest published gap in the commercial market — only two "
                "of seven major providers teach questioning technique at all. It is also where "
                "new internal auditors most often fail.")

tile_grid("PLOD — Capturing Traceable Evidence as You Find It", [
    ("P — Person", "The ROLE interviewed, never the individual's name: 'the Warehouse "
                   "Supervisor'."),
    ("L — Location", "Building, area, line, tank: 'Chemical Store B, external yard'."),
    ("O — Object", "The physical thing with its identifier: 'drums WD-104/105/106'."),
    ("D — Document", "Document identity AND revision or date: 'EMS-P-08 Rev 4, cl. 5.3'."),
], kicker="A NOTE-TAKING DISCIPLINE — NOT AN ISO TERM", cols=2, size=14, accent=VIOLET)

big_statement("If your note has none of P, L, O or D, you have an impression — not evidence.",
              "A finding must be re-findable. Another auditor, six months later, should be "
              "able to go to the same place, ask for the same document and reach the same "
              "conclusion.",
              "THE TEST OF A GOOD NOTE", color=VIOLET)

stack("The Opening Meeting — the Standard Agenda", [
    ("Introductions and roles", "Audit team, auditee representatives, guides and observers."),
    ("Confirm the audit plan", "Objectives, scope, criteria, timetable and the closing "
                               "meeting time."),
    ("Confirm communication channels", "Who the audit team reports to during the audit; how "
                                       "issues are escalated."),
    ("Explain the method and the SAMPLING basis", "And that sampling means the audit carries "
                                                  "an element of uncertainty."),
    ("Explain how findings will be graded and reported", "Major, minor, OFI — and what each "
                                                         "means here."),
    ("Confirm safety, escort and facility arrangements", "PPE, restricted areas, emergency "
                                                         "procedures."),
    ("Invite questions", "Confirm the auditee understands and agrees before fieldwork begins."),
], kicker="ISO 19011 §6.4.2", accent=BLUE)

stack("The Closing Meeting — the Standard Agenda", [
    ("Thank the auditee", "And restate the audit objective and scope."),
    ("Restate the sampling caveat", "Findings are based on sampled evidence — absence of a "
                                    "finding is not proof of conformity."),
    ("Present the findings", "Each with its evidence and its grade, so they are understood "
                             "and acknowledged."),
    ("Present the audit conclusion", "On conformity and on effective implementation and "
                                     "maintenance."),
    ("Agree the corrective action process", "Owners, timeframes and how effectiveness will "
                                            "be verified."),
    ("Record any diverging opinions", "Unresolved disagreements are REPORTED, not suppressed "
                                      "— that is fair presentation."),
    ("Confirm the report and follow-up", "Distribution, timing and the follow-up arrangement."),
], kicker="ISO 19011 §6.4.10", accent=TEAL)

tile_grid("Engaging the Stakeholders — They Are Not All the Same", [
    ("Operations staff", "Your primary evidence source. Interview at their normal workplace, "
                         "put them at ease, never blame."),
    ("Process owners / managers", "Describe the intended procedure and own the corrective "
                                  "actions. Contrast what they say with what operators do."),
    ("Top management", "Opening and closing meetings; leadership (5.1), resources (7.1) and "
                       "the programme-level findings."),
    ("Client representatives", "NOT the auditee. Gatekeepers for site access — get permission "
                               "in advance and protect confidentiality."),
    ("Regulators (NEA, PUB)", "Engaged INDIRECTLY — through licences, submitted returns and "
                              "correspondence. An internal auditor does not interview them."),
    ("Contractors on site", "Work 'under the control of' the organisation — clause 7.2 "
                            "competence and 8.1 outsourced control apply to them."),
], kicker="K3 · A2 · WHO YOU DEAL WITH", cols=2, size=13, accent=AMBER)

# ---- Activity 2 ----
mark("act2")
activity_slide(ACTIVITIES[1])
verify_slide(ACTIVITIES[1])

brk("Lunch Break", "45 minutes")

# ============================================================ TOPIC 3
T = C.TOPICS[2]
mark("topic3")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])

img_points("Evaluating Significance — the 5×5 Matrix", "risk_matrix.png",
           [("Score = Severity × Likelihood", "The most common method, and defensible if the "
                                              "criteria are documented."),
            ("Threshold ≥ 10 = significant", "High and Extreme bands. The threshold itself is "
                                             "what an auditor challenges."),
            ("ISO prescribes NO method", "6.1.2 requires only that significance is determined "
                                         "BY ESTABLISHED CRITERIA."),
            ("The real audit question", "Not 'is your method right?' but 'is it documented, "
                                        "criteria-based and consistently applied?'")],
           kicker="K4 · RISK ASSESSMENT TECHNIQUES", accent=AMBER, img_w=6.2)

cards("The Override Rules — What Makes an Aspect Automatically Significant", [
    ("A legal limit applies",
     "The aspect is subject to a regulatory limit, licence or permit condition — regardless "
     "of its arithmetic score."),
    ("A regulator has acted",
     "A notice, warning, fine or prosecution in the last three years."),
    ("A substantiated complaint",
     "An interested party has complained and the complaint was upheld."),
    ("Controlled substances or waste",
     "The aspect involves a listed hazardous substance or toxic industrial waste."),
], kicker="WHY SCORING ALONE IS NOT ENOUGH", accent=RED,
   note="Without override rules, a licensed discharge can score 'medium' and drop off the "
        "significant list — the classic finding where the aspects register has become "
        "disconnected from the legal register.")

table_slide("Three Significance Methods — Pick One and Document It",
            ["Method", "How it scores", "Best for"],
            [("Severity × Likelihood", "5×5, score 1–25; significant at ≥ 10",
              "SMEs and first registers — simple and defensible"),
             ("Multi-criteria weighted",
              "Severity × Frequency × Legal × Stakeholder, or a weighted sum",
              "Larger organisations — builds in obligations and interested parties"),
             ("FMEA (S × O × D)", "RPN 1–1000; act at ≥ 100; any S ≥ 9 acts regardless",
              "Abnormal and emergency aspects where DETECTION matters")],
            kicker="K4 · THE TOOLKIT", widths=[0.24, 0.46, 0.30], fsize=11, accent=AMBER,
            note="FMEA adds the dimension the others miss: can we DETECT the failure before it "
                 "becomes an impact? The cheapest risk reduction is almost always better "
                 "detection — which is exactly what clause 9.1 monitoring is for.")

tile_grid("Auditing the Significance Method — Questions That Find Weakness", [
    ("Show me the documented criteria.", "If the criteria live only in a spreadsheet formula "
                                         "or someone's head, that is a 6.1.2 finding."),
    ("Who approved them, and when?", "No approval, no date, no version control."),
    ("Would two assessors score this the same?", "Test it live — re-score one aspect with the "
                                                 "process owner."),
    ("This has a legal limit but scored 6. Explain.", "Tests whether override rules exist."),
    ("Show me how each significant aspect reaches a control.", "6.1.2 → 8.1 → 9.1. A register "
                                                               "nothing references is shelf-ware."),
    ("Why did significant aspects drop from 30 to 6?", "Tests whether the threshold was quietly "
                                                       "moved to reduce work."),
], kicker="TAKE THESE ON SITE", cols=2, size=13, accent=AMBER)

table_slide("FMEA for Environmental Risk — S × O × D",
            ["Dimension", "What it rates", "The audit insight"],
            [("Severity (S)", "How bad the environmental consequence is, 1–10",
              "You cannot usually reduce it — a solvent stays toxic"),
             ("Occurrence (O)", "How likely the failure mode is, 1–10",
              "Reduced by maintenance, design and competence"),
             ("Detection (D)", "Ability to detect BEFORE impact — INVERTED scale, 1 = certain",
              "The cheapest and fastest RPN reduction available"),
             ("RPN = S × O × D", "1–1000; act at ≥ 100; any S ≥ 9 acts regardless of RPN",
              "Links directly to clause 9.1 monitoring and measurement")],
            kicker="WHEN SEVERITY × LIKELIHOOD IS TOO COARSE", widths=[0.20, 0.44, 0.36],
            fsize=10.5, accent=VIOLET,
            note="Worked example: cracked bund, S=9 O=4 D=7 → RPN 252. Add a leak-detection "
                 "sensor and D falls to 2 → RPN 72. Same hazard, same likelihood, but now you "
                 "find out before it reaches the soil.")

table_slide("Environmental Objectives — the 6.2.2 Five-Part Test",
            ["Requirement", "The audit question", "Weak answer"],
            [("What will be done", "What are the actual actions and programme?",
              "'Improve energy efficiency' — that is the objective, not the plan"),
             ("What resources", "Is the budget approved and released?",
              "No capex, no headcount — a paper objective"),
             ("Who is responsible", "Which NAMED role owns it?",
              "'The EHS department'"),
             ("When completed", "Target date and milestones?", "'Ongoing'"),
             ("How evaluated", "Which indicator, measured how, how often, by whom?",
              "No indicator, or an indicator with no calibrated measurement")],
            kicker="CLAUSE 6.2.2 · A RELIABLE CHECKLIST", widths=[0.20, 0.42, 0.38],
            fsize=10.5, accent=GREEN,
            note="Trace every objective BACKWARDS to a significant aspect, obligation or risk, "
                 "and FORWARDS to 9.1 monitoring and 9.3 management review. An orphan objective "
                 "means the 6.1 → 6.2 link is broken.")

img_full("Writing a Nonconformity — the Three-Part Structure", "nc_anatomy.png",
         kicker="THE MOST IMPORTANT SKILL IN THIS COURSE", accent=RED,
         caption="Requirement + Evidence + the statement of the gap. Miss any one and you have "
                 "written an opinion, which the auditee is entitled to reject.")

img_full("Grading the Finding — Major, Minor or OFI", "nc_grading.png",
         kicker="AND WHERE THE CRITERIA COME FROM", accent=AMBER,
         caption="ISO 19011 says only that findings 'can be graded'. The major/minor criteria "
                 "come from ISO/IEC 17021-1 and from your own organisation's audit procedure — "
                 "so define them in the procedure and apply them consistently.")

split_note("Nonconformity Statements — Bad and Good",
           "✗  WEAK — will be rejected",
           [("'Housekeeping in the chemical store is poor.'", 1),
            ("→ opinion, no requirement, no evidence", 1),
            ("'The operator did not follow the procedure.'", 1),
            ("→ blames a person, names no requirement", 1),
            ("'You should install a new bund.'", 1),
            ("→ that is consulting, not a finding", 1),
            ("'Training records were not very good.'", 1),
            ("→ vague, not traceable, not re-findable", 1)],
           "✓  STRONG — evidence-based",
           [("'ISO 14001:2015 cl. 8.1 requires operational controls...", 1),
            ("...On 14 Aug 2026, three 200 L drums (WD-104/105/106) in Chemical Store B "
             "bore no contents or hazard labels...", 1),
            ("...therefore operational control for hazardous waste storage is not "
             "implemented as required.'", 1),
            ("Requirement + Evidence + Gap", 1),
            ("Traceable: another auditor can re-find it", 1),
            ("Addresses the SYSTEM, not the person", 1)],
           kicker="REWRITE EVERY WEAK ONE",
           note="Write findings so that a reader who was not there understands exactly what was "
                "seen, where, and which requirement it breaches.")

img_full("Root Cause Analysis — 5 Whys Worked Through", "five_whys.png",
         kicker="STOP AT A PROCESS, NOT AT A PERSON", accent=BLUE,
         caption="If your 5 Whys ends at 'the operator forgot', you have found a symptom. Push "
                 "until you reach a step that is missing from a process — that is what "
                 "corrective action can actually fix.")

img_full("Correction vs Corrective Action vs Improvement", "correction_vs_ca.png",
         kicker="CLAUSE 10.2 vs 10.3", accent=TEAL,
         caption="Clause 10.2 requires BOTH: react and correct, AND evaluate the need to "
                 "eliminate the cause so it does not recur. A CAR that only lists corrections "
                 "is an incomplete CAR.")

stack("Writing an Effective Corrective Action Request", [
    ("The nonconformity statement", "Requirement + evidence + gap, with the clause cited."),
    ("The grade and its justification", "Major, minor or OFI — and WHY, against your defined "
                                        "criteria."),
    ("Root cause", "Reached by 5 Whys or fishbone; must be a process or system cause."),
    ("Correction", "What fixes the immediate problem and contains the consequences — "
                   "including mitigating the environmental impact (10.2a)."),
    ("Corrective action", "What eliminates the cause so it does not recur OR OCCUR ELSEWHERE "
                          "— and whether similar NCs exist in other areas (10.2b)."),
    ("Owner and due date", "A named role and a real date."),
    ("Effectiveness verification", "How and when you will confirm it worked — required by "
                                   "10.2(d) and retained under 10.2."),
], kicker="THE CAR · A3", accent=RED,
   note="'Re-trained the operator' is the most over-used and least effective corrective "
        "action in industry. Ask: if that person leaves tomorrow, does the problem return?")

stack("The Audit Report — What Must Be In It", [
    ("Audit objectives, scope and criteria", "Including what was EXCLUDED."),
    ("Audit team, auditees and dates", "Who audited, who was audited, when."),
    ("The audit findings", "Each with its evidence, its clause and its grade."),
    ("The audit conclusion", "On conformity AND on effective implementation and maintenance "
                             "— clause 9.2.1 requires both."),
    ("The sampling statement", "That the audit was a sampling exercise and therefore carries "
                               "uncertainty — the single most commonly OMITTED element."),
    ("Opportunities for improvement", "Kept clearly SEPARATE from nonconformities."),
    ("Agreed actions, owners and dates", "And the follow-up arrangement."),
    ("Distribution list", "Reported to relevant management — ISO 14001 cl. 9.2.2."),
], kicker="ISO 19011 §6.5 · A3", accent=VIOLET,
   note="Report item (k) — the sampling caveat — protects both the auditor and the "
        "organisation. Absence of a finding is never proof of conformity.")

process_map("Stage 6 — Audit Follow-Up: the Stage Everyone Skips",
            [("Receive the action plan", "Root cause, correction, corrective action, dates"),
             ("Review its adequacy", "Does the action actually address the ROOT cause?"),
             ("Verify implementation", "Was it done? Evidence, not assertion"),
             ("Verify EFFECTIVENESS", "Has the problem stopped recurring? — cl. 10.2(d)"),
             ("Close and record", "Retain evidence of the NC, the action AND the result")],
            kicker="ISO 19011 §6.7 · ISO 14001 CL. 10.2", accent=GREEN,
            synthesis="'Closed' is a status, not a conclusion. Clause 10.2(d) requires a review "
                      "of the EFFECTIVENESS of corrective action, and 10.2 requires the result "
                      "to be retained. Closure without that evidence is itself a nonconformity.")

split_note("Corrective Actions — Weak and Strong",
           "✗  WEAK — the problem will return",
           [("'Operator re-trained.'", 1),
            ("→ if that person leaves, the gap returns", 1),
            ("'Reminded staff at the toolbox talk.'", 1),
            ("→ no change to any process", 1),
            ("'Increased management awareness.'", 1),
            ("→ unmeasurable, unverifiable", 1),
            ("'Will monitor more closely.'", 1),
            ("→ no owner, no frequency, no criterion", 1)],
           "✓  STRONG — the cause is removed",
           [("'Amended MOC procedure PR-12 to require an", 1),
            ("environmental re-assessment before any volume", 1),
            ("or process change — effective 1 Sep 2026.'", 1),
            ("'Added bund integrity testing to the PM schedule", 1),
            ("at 12-month frequency, owner: Facilities Manager.'", 1),
            ("'Installed continuous pH monitoring with an", 1),
            ("interlocked shut-off on the discharge line.'", 1),
            ("Process changed · owner named · date set · verifiable", 1)],
           kicker="THE TEST: WOULD THIS SURVIVE THE PERSON LEAVING?",
           note="Re-training is the most over-used corrective action in industry. It is "
                "sometimes right — but only when the root cause genuinely IS a competence gap, "
                "and then clause 7.2 requires you to evaluate the effectiveness of the training.")

tile_grid("Common Auditor Mistakes — Recognise Them In Yourself", [
    ("Auditing the person, not the process", "'Why didn't YOU fill this in?' kills cooperation "
                                             "and finds nothing."),
    ("Raising an NC against a 'should'", "Only 'shall' statements are requirements."),
    ("Demanding documents that are not required", "No procedure, no manual, no preventive "
                                                  "action procedure is required."),
    ("Consulting mid-audit", "You become the author of what you must audit next year."),
    ("Accepting an assertion as evidence", "'We always do that.' Show me."),
    ("Stopping the 5 Whys at human error", "Human error is a symptom. Find the process gap."),
], kicker="THE PITFALLS", cols=2, size=13, accent=RED)

# ---- Activity 3 ----
mark("act3")
activity_slide(ACTIVITIES[2])
verify_slide(ACTIVITIES[2])

# ============================================================ CLOSE
mark("close")
section("WRAP-UP", "Course Summary & Next Steps", "")

tile_grid("What You Achieved", [
    ("The framework (LO1)", "The IPPF, the Code of Ethics, ISO 14001:2015 clause by clause, "
                            "and how context, aspects and obligations drive the EMS."),
    ("The audit process (LO2)", "ISO 19011's seven principles, the programme/audit "
                                "distinction, the six-stage lifecycle, checklists, evidence "
                                "and interviewing."),
    ("Risk and reporting (LO3)", "Significance evaluation, risk matrices and FMEA, root cause "
                                 "analysis, corrective action requests and the audit report."),
    ("Three real engagements", "GreenPack scoping, AquaPure planning, EcoTech risk and CARs — "
                               "the same shape as the assessment."),
], kicker="LEARNING OUTCOMES DELIVERED", cols=1, size=13)

tile_grid("Your First Real Internal Audit — a Checklist", [
    ("Confirm your independence", "You cannot audit your own area. Declare any prior "
                                  "involvement."),
    ("Read before you walk", "The aspects register, the legal register, previous reports and "
                             "open corrective actions."),
    ("Build the checklist from THEIR risks", "Not from the standard's contents page."),
    ("Verify everything you are told", "Interview, then observe, then check the record."),
    ("Write findings that are re-findable", "Requirement + evidence + gap, with P, L, O, D."),
    ("Follow up — always", "10.2(d) requires you to review whether the action was effective."),
], kicker="WHAT TO DO ON MONDAY", cols=2, size=13, accent=TEAL)

tile_grid("Recommended Follow-On Courses",
          [(t.replace("WSQ - ", ""), "WSQ funded · Tertiary Infotech Academy")
           for t in C.RECOMMENDED],
          kicker="CONTINUE THE JOURNEY", cols=1, size=13)

cards("Support — We're Here to Help", [
    ("Email", "enquiry@tertiaryinfotech.com\nFor course, certificate and funding enquiries "
              "during and after the class."),
    ("Telephone", "+65 6100 0613\nOffice hours, Monday to Friday."),
    ("Website", "www.tertiarycourses.com.sg\nCourse schedules, funding information and the "
                "full WSQ catalogue."),
], kicker="AFTER THE COURSE", accent=TEAL,
   note="Your certificate is issued after you are assessed Competent, meet the 75% "
        "attendance requirement and complete the TRAQOM survey on the LMS.")

# ---- assessment admin block repeated at the END (house rule) ----
mark("assessment")
tile_grid("Assessment", [
    ("Written Assessment (SAQ)", "4 short-answer questions · 60 minutes · K1–K4."),
    ("Case Study (CS)", "3 scenario-based questions · 60 minutes · A1–A3."),
    ("Open book", "Slides, Learner Guide, activity briefs and your own notes."),
    ("Attendance first", "Take the Assessment digital attendance before you start."),
    ("Submit on the LMS", f"{C.LMS_URL}"),
    ("Sign the record", "Sign the Assessment Summary Record before you leave."),
], kicker="FINAL ASSESSMENT", cols=2, size=14, accent=BLUE)

flow_h("Assessment Flow", [
    "TRAQOM — scan the QR code on the LMS",
    "Assessment digital attendance — scan the SSG QR",
    "Sit the WA (SAQ) 1 hr, then the Case Study 1 hr — open book",
    "Submit your answers on the LMS",
    "Sign the Assessment Summary Record",
], kicker="ON ASSESSMENT DAY")

flow_h("Digital Attendance (Mandatory)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR with your phone camera",
    "Submit your attendance — AM, PM and Assessment",
    "Repeat on BOTH days of the course",
    "75% minimum attendance for assessment and funding",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=VIOLET,
   note="Digital attendance is mandatory for WSQ-funded courses and is the record SSG uses "
        "to determine your funding eligibility.")

big_statement("Thank You!",
              "You can now plan, conduct, report and follow up an internal audit of an "
              "ISO 14001:2015 environmental management system — and write findings that "
              "stand up.",
              "SEE YOU AT THE OPENING MEETING", color=TEAL)
mark("end")

# ============================================================ SAVE
OUT = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
MAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slide_map.json")
n = save(OUT, MAP)
print(f"Saved {OUT}  ({n} slides)")
