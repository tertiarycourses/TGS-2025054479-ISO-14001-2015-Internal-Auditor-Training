# WSQ — ISO 14001:2015 Internal Auditor Training

**Course code:** `TGS-2025054479` · **Version:** v6 · 17 August 2026
**Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)
**Course page:** https://www.tertiarycourses.com.sg/wsq-iso-14001-2015-internal-auditor-training.html

A 2-day (16-hour) WSQ course that prepares learners to plan, conduct, report and follow up an
internal audit of an Environmental Management System based on **ISO 14001:2015**, using the
**International Professional Practices Framework (IPPF)** and the auditing guidance of
**ISO 19011:2018**.

| | |
|---|---|
| **Duration** | 16 hours over 2 days — 14 h facilitation + 2 h assessment |
| **Skills Framework TSC** | Internal Audit Engagement Planning · `ACC-IAD-3005-1.1` · Level 1 |
| **Mode** | Classroom / instructor-led |
| **Assessment** | Written Assessment (SAQ) 4 questions · 60 min · Case Study 3 questions · 60 min — both open book |
| **Grading** | Competent (C) / Not Yet Competent (NYC) |
| **Funding validity** | 11 Apr 2025 to 10 Apr 2027 |

---

## Learning outcomes

- **LO1** — Identify ISO 14001:2015 standards for internal auditing based on the International
  Professional Practices Framework (IPPF) and organisational risks.
- **LO2** — Identify phases of engagement with stakeholders by applying ISO 14001:2015 internal
  audit methodologies and procedures.
- **LO3** — Support preliminary risk assessments using risk identification and assessment techniques.

## Course outline

| Topic | Title | Covers | K/A |
|---|---|---|---|
| 1 | ISO 14001:2015 Internal Auditor Framework | IPPF · the EMS and Annex SL · Clauses 4–10 · aspects, impacts and compliance obligations · risk-based thinking | K1 · K2 · A1 |
| 2 | Auditing ISO 14001:2015 | ISO 19011:2018 principles · audit programme vs audit · the six-stage lifecycle · checklists, evidence, interviewing · stakeholders | K3 · A2 |
| 3 | Risk Assessment | Aspect/impact significance · risk matrices and FMEA · nonconformity grading · root cause analysis · CARs · the audit report | K4 · A3 |

## Hands-on activities

Three scenario-based case studies, one per topic. Each brief carries the scenario, the evidence
given, a step-by-step method, the questions and a self-check; the trainer pack adds model answers
and debrief notes.

| # | Activity | Topic | Duration | Assesses |
|---|---|---|---|---|
| 1 | Auditing GreenPack — Framework, Context and Scope | 1 | 45 min | K1 · K2 · A1 |
| 2 | AquaPure — Planning the Engagement and the Audit Checklist | 2 | 60 min | K3 · A2 |
| 3 | EcoTech Electronics — Risk Assessment, CARs and the Audit Report | 3 | 75 min | K4 · A3 |

---

## Repository layout

```
courseware/
  ISO 14001-2015 Internal Auditor Training-v6.pptx   trainer slide deck (106 slides)
  ISO 14001-2015 Internal Auditor Training-v6.pdf    learner slides
  LP-…docx / .pdf                                    Lesson Plan
  LG-…docx / .pdf                                    Learner Guide
  assets/                                            generated diagrams (matplotlib)
activities/                                          one folder per activity
  activity-1-…/                                      md · docx · pdf + trainer pack
  activity-2-…/
  activity-3-…/
build/                                               the single-source generators
  course_data.py                                     SINGLE SOURCE OF TRUTH (metadata, outcomes, topics)
  data_domain1..3.py                                 the three activities
  slide_lib.py                                       slide component library
  make_charts.py                                     diagram generator
  build_slides.py / build_lesson_plan.py / build_learner_guide.py / build_activities.py
LG-….md                                              Markdown mirror of the Learner Guide
reference/                                           source material and research notes
```

### Single-source build

Every artifact is generated from `build/course_data.py` plus `build/data_domainN.py`, so the deck,
Lesson Plan, Learner Guide, Markdown mirror and activity briefs can never drift apart. The two
schedule slides in the deck are generated *from the Lesson Plan's own schedule*, and the Lesson Plan
asserts at build time that the day totals equal 14 h facilitation + 2 h assessment.

```bash
python3 build/make_charts.py          # regenerate the diagrams
python3 build/build_slides.py         # deck  -> courseware/…-v6.pptx
python3 build/build_lesson_plan.py    # LP    -> courseware/LP-….docx
python3 build/build_learner_guide.py  # LG    -> courseware/LG-….docx + LG-….md
python3 build/build_activities.py     # activity briefs (md + docx + pdf)
```

Rendering to PDF and injecting page-numbered tables of contents:

```bash
soffice --headless --convert-to pdf --outdir courseware "courseware/<file>"
python3 .claude/skills/courseware-build/build/inject_toc.py "<docx>" "<pdf>" 2
```

---

## Standards and sources

Content is written against the standards themselves and cross-checked with the published syllabi of
SGS, BSI, TÜV SÜD, Bureau Veritas, LRQA and Ensure Safe:

- **ISO 14001:2015** — Environmental management systems — Requirements with guidance for use
- **ISO 19011:2018** — Guidelines for auditing management systems
- Singapore compliance context — EPMA, EPHA, Sewerage & Drainage Act, Resource Sustainability Act,
  Carbon Pricing Act, Energy Conservation Act, and the NEA/PUB licensing regimes

> **Transition note.** ISO 14001:2015 was withdrawn on 15 April 2026 and replaced by ISO 14001:2026,
> with a 36-month transition for existing certificates. This course teaches the **2015 edition**,
> which is the edition named in its approved scope and the one most auditees are still certified to.
> Regulatory figures in the courseware are dated **"verified as at August 2026"** — the course
> deliberately teaches the *method* of maintaining a legal register rather than treating any figure
> as permanent.

## Note on the assessment

The assessment papers and answer keys are **confidential** and are deliberately **not** published to
this repository. They are distributed through Google Drive and the LMS to authorised trainers and
assessors only.

---

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg
