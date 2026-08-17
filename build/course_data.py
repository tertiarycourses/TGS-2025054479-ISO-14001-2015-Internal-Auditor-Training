"""
SINGLE SOURCE OF TRUTH — ISO 14001:2015 Internal Auditor Training (TGS-2025054479).

Every artifact (PPT deck, Lesson Plan, Learner Guide + LG.md, the activities/ pack
and the assessment) is generated from this module plus data_domain1..3.py, so the
titles, K/A mapping, schedule, activity numbering and assessment can never drift.

Authoritative sources for the structure below:
  * LMS-TMS course record (courseId 7f2fbc87-eee3-43c8-8987-cf48c2d52fdd)
      - TSC ACC-IAD-3005-1.1, trainingHours 14, assessmentHours 2
      - the 3 topics and their subtopics, verbatim
  * www.tertiarycourses.com.sg course page (learning outcomes, prerequisites)
  * The approved assessment papers on Drive:
      - WA (SAQ) 60 min, 4 questions -> K1 K2 K3 K4
      - Case Study 60 min, 3 questions -> A1 A2 A3
"""

# ------------------------------------------------------------------ metadata
TITLE        = "ISO 14001:2015 Internal Auditor Training"
SHORT_TITLE  = "ISO 14001-2015 Internal Auditor Training"
COURSE_CODE  = "TGS-2025054479"
VERSION      = "v6"
VERSION_DATE = "17 August 2026"

ORG     = "Tertiary Infotech Academy Pte Ltd"
UEN     = "UEN: 201200696W"
TRAINER = "Dr. Alfred Ang"
DAYS    = 2

TRAINING_HOURS   = 14      # classroom facilitation
ASSESSMENT_HOURS = 2       # WA (SAQ) 1 hr + Case Study 1 hr
TOTAL_HOURS      = TRAINING_HOURS + ASSESSMENT_HOURS

# ------------------------------------------------------------------ Skills Framework
TSC_TITLE = "Internal Audit Engagement Planning"
TSC_CODE  = "ACC-IAD-3005-1.1"
TSC_LEVEL = "Level 1"

# Knowledge statements — assessed by the Written Assessment (SAQ)
TSC_KNOWLEDGE = [
    ("K1", "International Professional Practices Framework (IPPF) comprising definitions of "
           "Internal Auditing, Code of Ethics, core principles and International Standards for "
           "the Professional Practice of Internal Auditing"),
    ("K2", "Organisation's significant risks, objectives, resources, operations, businesses "
           "and structure"),
    ("K3", "Internal audit methodologies and procedures of the organisation"),
    ("K4", "Risk identification and assessment techniques"),
]

# Ability statements — assessed by the Case Study
TSC_ABILITIES = [
    ("A1", "Identify relevant frameworks, guidelines and standards to be applied in the engagement"),
    ("A2", "Identify stages of the engagement and various stakeholders involved"),
    ("A3", "Support conduct of preliminary survey and risk assessment"),
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Identify ISO 14001:2015 standards for internal auditing based on the International "
    "Professional Practices Framework (IPPF) and organisational risks",
    "LO2: Identify phases of engagement with stakeholders by applying ISO 14001:2015 internal "
    "audit methodologies and procedures",
    "LO3: Support preliminary risk assessments using risk identification and assessment techniques",
]

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written   = "Written Assessment — Short Answer Questions (WA/SAQ): 4 questions, 60 minutes.",
    casestudy = "Case Study (CS): 3 scenario-based questions, 60 minutes.",
    note      = "Both instruments are OPEN BOOK and completed individually. "
                "All answers must be correct to be assessed Competent (C).",
    grading   = "Competent (C) / Not Yet Competent (NYC)",
)

# ------------------------------------------------------------------ prerequisites
PREREQUISITES = [
    ("Knowledge & skills", "Able to operate basic computer functions. Minimum 3 GCE 'O' Level "
                           "passes including English, or Workplace Literacy (WPL) Level 5."),
    ("Experience",         "Minimum 1 year of working experience. Target age group 21–65."),
    ("Attitude",           "Positive learning attitude and an enthusiastic learner."),
]

TARGET_ROLES = [
    "Internal Auditor / EMS Auditor",
    "Compliance Officer",
    "Quality Assurance Manager",
    "Risk Specialist",
    "EHS Manager",
    "Sustainability Manager",
    "Operations Manager",
    "Management Representative",
]

# ------------------------------------------------------------------ topics (= learning units)
# Topic titles and subtopics are VERBATIM from the approved LMS course record.
TOPICS = [
    dict(
        num=1, code="01",
        title="ISO 14001:2015 Internal Auditor Framework",
        lu="LU1: Introduction to ISO 14001:2015",
        lo="LO1",
        ka="K1 · K2 · A1",
        subtopics=[
            "Overview of International Professional Practices Framework (IPPF)",
            "Introduction of ISO 14001:2015 and Environmental Management System (EMS)",
            "Apply ISO 14001:2015 to Organization – Risks, Objectives, Resources, Operations",
        ],
        subtitle="IPPF · the EMS and Annex SL · Clauses 4–10 · aspects, impacts and "
                 "compliance obligations · risk-based thinking",
    ),
    dict(
        num=2, code="02",
        title="Auditing ISO 14001:2015",
        lu="LU2: Auditing Methodologies",
        lo="LO2",
        ka="K3 · A2",
        subtopics=[
            "Internal audit methodologies and procedures for ISO 14001:2015",
            "Phases of auditing and engagement with stakeholders",
        ],
        subtitle="ISO 19011:2018 principles · audit programme vs audit · the six-stage "
                 "lifecycle · checklists, evidence, interviewing · stakeholders",
    ),
    dict(
        num=3, code="03",
        title="Risk Assessment",
        lu="LU3: Risk Assessment Techniques",
        lo="LO3",
        ka="K4 · A3",
        subtopics=[
            "Conducting Risk assessment",
            "Writing effective corrective action requests",
            "Preparing audit reports",
        ],
        subtitle="Aspect/impact significance · risk matrices and FMEA · nonconformity "
                 "grading · root cause analysis · CARs · the audit report",
    ),
]

# ------------------------------------------------------------------ recommended follow-on
RECOMMENDED = [
    "WSQ - ISO 9001:2015 Internal Auditor Training",
    "WSQ - ISO 45001:2018 Internal Auditor Training",
    "WSQ - Sustainability Reporting and ESG Essentials",
    "WSQ - Carbon Footprint Accounting and Management",
]

# Funding validity as published on the course page (tertiarycourses.com.sg)
FUNDING_VALIDITY = "11 Apr 2025 to 10 Apr 2027"

LMS_URL = "https://lms-tms.tertiaryinfotech.com"
