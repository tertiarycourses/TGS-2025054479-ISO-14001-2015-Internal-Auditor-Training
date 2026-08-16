"""Topic 1 activities — ISO 14001:2015 Internal Auditor Framework (LO1 · K1 K2 A1).

Each activity dict is consumed by:
  build_slides.py        -> the activity workflow slide (scenario + 5-chip strip)
  build_learner_guide.py -> the FULL step-by-step guide + worked answer
  activities/            -> the standalone activity brief (MD + PDF)

Contract:
  num, title, minutes, topic, ka   : identity and mapping
  desc                             : 2-3 line scenario shown on the slide
  flow                             : exactly 5 short chip labels (the workflow)
  build                            : the deliverable ("YOU'LL PRODUCE ...")
  services                         : tools / templates used
  scenario                         : the FULL case-study narrative (LG + brief)
  facts                            : bullet list of the given evidence/data
  steps                            : [(instruction, detail)] - the real procedure
  questions                        : [(q, guidance)] - what learners must answer
  answers                          : the trainer's worked/model answer
  debrief                          : what the trainer draws out in the discussion
  test                             : the acceptance criterion (self-check)
"""

DOMAIN1 = [
    dict(
        num=1,
        title="Auditing GreenPack — Framework, Context and Scope",
        minutes=45,
        topic="01",
        ka="K1 · K2 · A1",
        desc=("GreenPack Manufacturing has expanded capacity by 40% and added a solvent-based "
              "thermal lamination line. Energy use is up 25%, VOC emissions have risen and three "
              "odour complaints have been received — but the aspects register and policy are stale. "
              "You are the lead internal auditor: scope the engagement."),
        flow=[
            "Read the scenario and list the IPPF components that govern your conduct",
            "Map the symptoms to ISO 14001:2015 clauses (4.1–4.4, 5.2, 6.1.2, 8.1)",
            "Build a context table: issues, interested parties, compliance obligations",
            "Decide the audit scope, boundaries and the areas you will prioritise",
            "Write the engagement note justifying scope against risk",
        ],
        build="A completed Audit Engagement Scoping Note for GreenPack — clause map, "
              "context table, prioritised scope and the IPPF basis for your independence.",
        services="Activity 1 brief · ISO 14001:2015 clause map · Context & scope template",

        scenario=(
            "**GreenPack Manufacturing Pte Ltd** is a Singapore company producing biodegradable "
            "packaging materials from a single leased facility in Tuas. It achieved ISO 14001:2015 "
            "certification two years ago and employs 150 staff across three departments: "
            "Production, Warehousing & Logistics, and Administration.\n\n"
            "Eight months ago the company expanded production capacity by 40% and introduced a new "
            "**thermal lamination process using solvent-based adhesives**. Since the expansion:\n\n"
            "* electricity consumption has risen by 25%;\n"
            "* volatile organic compound (VOC) emissions from the lamination line have increased;\n"
            "* **three customer complaints** about chemical odours from the packaging have been received;\n"
            "* one **neighbouring tenant** has complained informally to the landlord about solvent smell.\n\n"
            "The Environmental Policy was last reviewed 18 months ago and makes no reference to the "
            "new process. The environmental aspects and impacts register has **not been updated since "
            "the expansion**. The company's strategic plan carries an objective to **reduce its carbon "
            "footprint by 30% within three years**. The internal audit function follows the "
            "**International Professional Practices Framework (IPPF)**.\n\n"
            "You are the lead internal auditor. The Managing Director has directed the internal audit "
            "team to conduct a comprehensive EMS audit and wants the scope agreed this week. You have "
            "been given the Environmental Policy, the (stale) aspects register, the organisation chart "
            "and the strategic plan."
        ),
        facts=[
            "Certified to ISO 14001:2015 for 2 years; single leased site in Tuas; 150 staff.",
            "Capacity +40%; new solvent-based thermal lamination line commissioned 8 months ago.",
            "Electricity consumption +25%; VOC emissions increased.",
            "3 customer odour complaints; 1 informal neighbour complaint via the landlord.",
            "Environmental Policy last reviewed 18 months ago — does not mention lamination.",
            "Aspects & impacts register not updated since the expansion.",
            "Strategic objective: reduce carbon footprint 30% in 3 years.",
            "Internal audit function operates under the IPPF.",
            "You report to the Audit Manager; you have never worked in Production.",
        ],
        steps=[
            ("Establish your professional basis under the IPPF",
             "List the four mandatory IPPF components and state, in one line each, how they govern "
             "THIS engagement: the Definition of Internal Auditing (independent, objective assurance "
             "adding value); the Code of Ethics (integrity, objectivity, confidentiality, competency); "
             "the Core Principles; and the International Standards. Note explicitly that you have "
             "never worked in Production — record that your independence is intact."),
            ("Convert each symptom into a clause hypothesis",
             "Take every fact in the scenario and ask 'which ISO 14001:2015 requirement would have "
             "prevented this?'. Stale policy -> 5.2. Stale aspects register after a process change -> "
             "6.1.2 (change is explicitly named). Odour and VOC -> 6.1.2, 8.1 operational control, "
             "6.1.3 compliance obligations. Neighbour and customer complaints -> 4.2 interested "
             "parties and 7.4 communication. Energy +25% against a carbon objective -> 6.2, 9.1.1."),
            ("Build the context table (clause 4.1 / 4.2)",
             "Three columns: EXTERNAL issues (NEA air-quality regulation, landlord lease terms, "
             "customer sustainability expectations, solvent price), INTERNAL issues (new process, "
             "capacity change, competence of new operators, ageing policy), and INTERESTED PARTIES "
             "with their relevant needs (NEA, landlord, neighbouring tenants, customers, employees). "
             "Then apply clause 4.2(c): mark which of those needs the organisation has ADOPTED as "
             "compliance obligations."),
            ("Test the declared EMS scope (clause 4.3)",
             "Ask whether the certified scope still covers what the company actually does. A 40% "
             "capacity increase and a brand-new process either fall inside the existing scope "
             "statement or reveal that the scope was never updated. Record which, and the evidence "
             "you would request to confirm it."),
            ("Prioritise the audit by risk, not by department",
             "Rank the areas: lamination line and its emissions (highest — new, uncontrolled, "
             "complaints, legal exposure); aspects/risk management process; policy and management "
             "review; energy and the carbon objective; warehousing; administration (lowest). "
             "State the reason for each rank in one line — this is what makes the plan defensible."),
            ("Write the engagement scoping note",
             "One page: audit objective, criteria (ISO 14001:2015 + GreenPack's own EMS procedures + "
             "applicable compliance obligations), scope and boundaries, areas prioritised with "
             "rationale, auditor independence statement, and the documents you will request before "
             "fieldwork."),
        ],
        questions=[
            ("Which IPPF components govern your conduct on this engagement, and what does each "
             "require of you here?",
             "Expect all four mandatory elements named, each tied to a concrete action in this case "
             "(e.g. Objectivity — you must not audit work you performed; Competency — you may need "
             "technical support on solvent chemistry)."),
            ("Which ISO 14001:2015 clauses are most relevant to GreenPack's situation, and why is "
             "each applicable?",
             "Look for 6.1.2 (change / stale register) and 5.2 (stale policy) as the two strongest, "
             "plus 4.1, 4.2, 4.3, 6.1.3, 6.2, 7.4, 8.1, 9.1.1 and 9.3, each justified by a specific "
             "fact from the scenario — not a generic clause list."),
            ("How should GreenPack's risks, objectives, resources and operational changes shape the "
             "scope and focus of your audit plan?",
             "The answer must move from risk to scope: the highest-risk, most-changed, most-complained "
             "-about area gets the most audit time. Equal time per department is the wrong answer."),
        ],
        answers=(
            "**IPPF.** The Definition frames the work as independent, objective assurance that adds "
            "value. The **Code of Ethics** binds the auditor to Integrity, Objectivity, "
            "Confidentiality and Competency — here, objectivity is satisfied because the auditor has "
            "never worked in Production, and competency may require a technical specialist on solvent "
            "emissions. The **Core Principles** and the **International Standards** require the "
            "engagement to be risk-based, adequately planned and reported to those charged with "
            "governance.\n\n"
            "**Clause map.** 4.1 — the new process and rising energy cost are internal issues; NEA "
            "air regulation and the landlord's lease are external. 4.2 — neighbours, customers, NEA "
            "and the landlord are interested parties whose expectations may become compliance "
            "obligations under 4.2(c). 4.3 — the EMS scope must still be valid after a 40% expansion. "
            "**5.2 — the policy has not been reviewed since a material process change and does not "
            "cover lamination: a likely nonconformity.** **6.1.2 — the standard explicitly requires "
            "aspects to be determined considering change, including new or modified activities; the "
            "register is 8 months out of date: a likely major.** 6.1.3 — VOC discharge triggers "
            "EPMA/air-impurities obligations that must be identified. 6.2 — the 30% carbon objective "
            "is contradicted by a 25% energy rise. 7.4 — three customer complaints and a neighbour "
            "complaint test the communication process. 8.1 — operational control and operating "
            "criteria for the new line. 9.1.1 — is VOC and energy performance being monitored at all? "
            "9.3 — did management review consider the change?\n\n"
            "**Scope.** Objective: determine whether the EMS conforms to ISO 14001:2015 and to "
            "GreenPack's own requirements, and is effectively implemented, with particular regard to "
            "the capacity expansion and the lamination process. Boundaries: the Tuas site, all three "
            "departments, EMS activity from the date of the expansion. Priority order: (1) lamination "
            "line — aspects, controls, emissions, legal; (2) the aspect-identification and "
            "change-management process itself; (3) policy, objectives and management review; "
            "(4) energy performance vs the carbon objective; (5) warehousing; (6) administration. "
            "Equal time per department would be indefensible: audit effort follows environmental "
            "risk and change."
        ),
        debrief=(
            "Draw out three points. First, **the stale aspects register is the systemic finding** — "
            "everything else (odour, VOC, complaints) is a symptom of a change-management process "
            "that does not trigger a re-evaluation of aspects. Second, **clause 6.1.2 names 'change' "
            "explicitly**, so this is not an auditor's opinion but a requirement breach. Third, "
            "**scope is a risk decision**: the group that allocated equal time to all three "
            "departments should defend that against the group that front-loaded the lamination line."
        ),
        pitfalls=[
            "You listed clauses but did not tie each one to a fact from the scenario — the "
            "clause map must be evidence-led, not a contents page.",
            "You allocated equal audit time to all three departments. Audit effort follows "
            "environmental risk and change; say so and defend it.",
            "You treated the odour complaints as the finding. They are a SYMPTOM — the stale "
            "aspects register is the systemic issue.",
            "You forgot the independence statement. The IPPF requires objectivity to be "
            "considered and recorded before the engagement starts.",
            "You wrote 'the policy is old' without naming clause 5.2 and what it requires.",
        ],
        test="Your scoping note names at least 8 relevant clauses each tied to a specific scenario "
             "fact, ranks the lamination line as the top priority with a stated reason, and contains "
             "an explicit auditor-independence statement.",
    ),
]
