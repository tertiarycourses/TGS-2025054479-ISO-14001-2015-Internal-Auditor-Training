"""Topic 3 activities — Risk Assessment, CARs and the Audit Report (LO3 · K4 A3).

Same dict contract as data_domain1.py.

Regulatory figures used in this activity are the VERIFIED ones only (NEA trade effluent
limits to watercourse; EPM Boundary Noise Limits; carbon tax S$45/tCO2e for 2026-2027).
Figures flagged as uncertain during research are deliberately NOT taught as fact.
"""

DOMAIN3 = [
    dict(
        num=3,
        title="EcoTech Electronics — Risk Assessment, CARs and the Audit Report",
        minutes=75,
        topic="03",
        ka="K4 · A3",
        desc=("EcoTech failed an NEA inspection for exceeding its copper discharge limit, three "
              "hazardous waste containers are unlabelled, the spill bund is cracked, and the EHS "
              "Manager post has been vacant for three months. Assess the risks, write the CARs, "
              "and draft the report."),
        flow=[
            "Build the aspect/impact register for the five problem areas",
            "Score each risk on the 5×5 matrix and set the significance threshold",
            "Run 5 Whys on the copper exceedance to reach the true root cause",
            "Write 3 CARs — requirement + evidence + nonconformity, graded",
            "Draft the audit report sections and the conclusion on effectiveness",
        ],
        build="A prioritised environmental risk assessment, three fully-written Corrective Action "
              "Requests with root cause analysis, and the skeleton of the audit report to "
              "EcoTech's management.",
        services="Activity 3 brief · 5×5 risk matrix · CAR form · Audit report template",

        scenario=(
            "**EcoTech Electronics Pte Ltd** is a contract electronics manufacturer assembling "
            "printed circuit boards (PCBs) and electronic components for international clients. "
            "It operates a 10,000 m² facility in **Tuas, Singapore**, with 200 employees.\n\n"
            "EcoTech's operations generate several environmental concerns:\n\n"
            "* **hazardous waste** — solder dross, flux residues and waste solvents;\n"
            "* **wastewater containing heavy metals** (lead, tin, copper) from the PCB washing "
            "process;\n"
            "* **air emissions** from soldering operations.\n\n"
            "EcoTech recently **failed a regulatory inspection by the National Environment Agency "
            "(NEA)**, receiving a warning for exceeding the permitted trade effluent discharge "
            "limit for **copper concentration**. In addition, a routine check by the facilities "
            "team found that **three hazardous waste storage containers in the soldering area were "
            "unlabelled**, and the **spill containment bund was cracked and leaking**.\n\n"
            "The company's risk register was last updated **eight months ago** and does not reflect "
            "recent changes:\n\n"
            "1. introduction of a **lead-free soldering process** using higher temperatures and "
            "different flux chemicals;\n"
            "2. a **30% increase in production volume** from a new client contract;\n"
            "3. the **departure of the EHS Manager three months ago** — the position remains vacant.\n\n"
            "You have been tasked with conducting a preliminary risk assessment of EcoTech's "
            "environmental management practices and preparing an audit report with corrective "
            "action recommendations."
        ),
        facts=[
            "Contract electronics manufacturer, 10,000 m² in Tuas, 200 employees.",
            "Hazardous waste: solder dross, flux residues, waste solvents (toxic industrial waste).",
            "Wastewater with lead, tin and copper from PCB washing.",
            "Air emissions from soldering.",
            "NEA WARNING — trade effluent copper concentration exceeded the permitted limit.",
            "3 hazardous waste containers in the soldering area found UNLABELLED.",
            "Spill containment bund CRACKED and LEAKING.",
            "Risk register 8 months old — predates all three changes below.",
            "Change 1: lead-free soldering — higher temperature, different flux chemistry.",
            "Change 2: production volume +30% on a new client contract.",
            "Change 3: EHS Manager left 3 months ago; post still vacant.",
        ],
        steps=[
            ("Separate the aspects from the impacts",
             "Build a register with columns Activity | Aspect | Impact | Condition (Normal / "
             "Abnormal / Emergency). Discipline: the ASPECT is the interaction you control "
             "('discharge of trade effluent containing copper'); the IMPACT is the change to the "
             "environment ('contamination of the watercourse, toxicity to aquatic life'). Writing "
             "'copper' or 'pollution' as an aspect is the classic error."),
            ("Cover all three operating conditions",
             "Normal: routine PCB washing discharge, soldering emissions, waste generation. "
             "Abnormal: higher-temperature lead-free soldering, the +30% volume surge, cleaning and "
             "changeover. Emergency: bund failure releasing solvent to the drain, a fire in the "
             "solvent store. The cracked bund is an EMERGENCY-condition aspect with a control that "
             "has already failed — that combination is what makes it urgent."),
            ("Score each risk on the 5×5 matrix",
             "Severity 1 (Insignificant) to 5 (Catastrophic); Likelihood 1 (Rare) to 5 (Almost "
             "certain). Score = S × L. Bands: 1–4 Low, 5–9 Medium, 10–14 High (SIGNIFICANT), "
             "15–25 Extreme (SIGNIFICANT, act now). Then apply the OVERRIDE rules — an aspect is "
             "automatically significant if it is subject to a legal limit or licence condition, has "
             "attracted a regulatory notice in the last 3 years, has generated a substantiated "
             "complaint, or involves a controlled hazardous substance or toxic industrial waste."),
            ("Identify at least five significant risks and rank them",
             "The copper exceedance is automatically significant (legal limit AND a regulatory "
             "warning). The cracked bund is automatically significant (emergency aspect, controlled "
             "substances, failed control). The unlabelled hazardous waste containers are "
             "automatically significant (toxic industrial waste). Then the stale risk register "
             "after three material changes, and the vacant EHS Manager role — the competence and "
             "resource gap that explains the other four."),
            ("Run 5 Whys on the copper exceedance",
             "Do not stop at 'the operator did not check'. Push until you reach a SYSTEM cause: "
             "the exceedance -> pre-treatment not removing copper -> loading rose after the +30% "
             "volume increase -> the pre-treatment capacity was never re-assessed -> no "
             "management-of-change step requires an environmental re-assessment when volume rises "
             "-> and there is no EHS Manager to own that step. Root cause: the change-management "
             "process does not trigger re-evaluation of aspects and controls."),
            ("Distinguish correction from corrective action",
             "Correction fixes the symptom: re-label the three containers, repair the bund, "
             "re-dose the effluent. Corrective action eliminates the cause: amend the "
             "management-of-change procedure to require an environmental impact re-assessment for "
             "any volume or process change, fill the EHS Manager role, and re-run the aspects "
             "evaluation. Clause 10.2 requires the latter — a CAR that only lists corrections is "
             "an incomplete CAR."),
            ("Write each CAR in the three-part structure",
             "REQUIREMENT (the exact clause or legal obligation breached) + EVIDENCE (what you saw, "
             "specific and traceable — location, date, document number, quantity) + NONCONFORMITY "
             "(the plain statement of the gap). Then grade it Major or Minor and state why. Add "
             "root cause, correction, corrective action, owner and due date."),
            ("Grade the findings and justify the grade",
             "Major: a legal breach, a total absence of a required process, or a systemic breakdown. "
             "The copper exceedance with an NEA warning is Major. The stale risk register after "
             "three changes is Major (6.1.2 explicitly requires change to be considered). The "
             "unlabelled containers, if isolated, are Minor — but combined with the cracked bund "
             "they evidence a systemic failure of operational control under 8.1."),
            ("Draft the audit report",
             "Sections: (1) audit objective, scope, criteria and dates; (2) audit team and auditees; "
             "(3) the sampling basis and its limitations; (4) findings — each graded, with the "
             "clause and the evidence; (5) positive observations; (6) opportunities for improvement, "
             "shown separately from nonconformities; (7) the CONCLUSION on whether the EMS conforms "
             "and is effectively implemented and maintained; (8) agreed corrective action owners and "
             "due dates; (9) distribution and follow-up arrangements."),
        ],
        questions=[
            ("Conduct a preliminary risk assessment: identify at least five significant "
             "environmental risks, assess each using a likelihood and consequence framework, and "
             "prioritise them for audit attention.",
             "Look for correct aspect/impact separation, all three operating conditions covered, "
             "explicit S×L scores, and — most importantly — the override rules applied so that the "
             "legally-breached copper discharge is significant regardless of arithmetic."),
            ("For the three most critical risks, write effective Corrective Action Requests "
             "including the nonconformity description, the relevant ISO 14001:2015 clause, the root "
             "cause analysis, and specific corrective and preventive actions.",
             "Each CAR must have all three parts. Reject 'the operator was careless' as a root "
             "cause — it must reach a system or process gap. Correction and corrective action must "
             "be clearly distinguished."),
            ("Outline the key sections and content of the audit report to EcoTech's management.",
             "Must include the conclusion on effectiveness, the sampling limitation, and OFIs kept "
             "separate from nonconformities."),
        ],
        answers=(
            "**Five significant risks (ranked).**\n\n"
            "1. **Trade effluent copper exceedance** — Aspect: discharge of trade effluent "
            "containing copper from PCB washing. Impact: watercourse contamination, toxicity to "
            "aquatic life. S=4, L=4 → 16 Extreme. Automatically significant: legal limit breached "
            "AND an NEA warning issued. Clauses 6.1.3, 8.1, 9.1.2.\n"
            "2. **Cracked, leaking spill containment bund** — Aspect: potential release of solvents "
            "and metal-bearing liquids (emergency condition). Impact: soil and groundwater "
            "contamination. S=5, L=3 → 15 Extreme. The designed control has already failed. "
            "Clauses 8.1, 8.2.\n"
            "3. **Three unlabelled hazardous waste containers** — Aspect: storage of toxic "
            "industrial waste without identification. Impact: mis-handling, incompatible mixing, "
            "improper disposal, contamination. S=4, L=4 → 16 Extreme. Automatically significant "
            "(toxic industrial waste). Clauses 8.1, 7.2, 7.3.\n"
            "4. **Risk/aspects register 8 months stale across three material changes** — the "
            "lead-free process changes the flux chemistry and emission profile; +30% volume changes "
            "every loading rate. S=4, L=5 → 20 Extreme. Clause 6.1.2 explicitly requires change to "
            "be considered.\n"
            "5. **EHS Manager post vacant for three months** — no owner for aspects, legal register, "
            "monitoring or compliance evaluation. S=3, L=5 → 15 Extreme. Clauses 5.3, 7.1, 7.2. "
            "This is the resource gap underlying risks 1–4.\n\n"
            "**CAR 1 — Major.** *Requirement:* ISO 14001:2015 clause 6.1.3 requires the "
            "organisation to determine its compliance obligations and take them into account in the "
            "EMS, and clause 8.1 requires operational controls established against operating "
            "criteria; EcoTech's trade effluent discharge is subject to a permitted copper "
            "concentration limit. *Evidence:* NEA inspection warning dated [date] recording copper "
            "concentration above the permitted limit at the site discharge point; pre-treatment "
            "plant records show no capacity re-assessment following the 30% production increase. "
            "*Nonconformity:* the organisation has not maintained operational control sufficient to "
            "fulfil its compliance obligation for trade effluent copper. *Root cause (5 Whys):* the "
            "management-of-change process contains no step requiring environmental re-assessment "
            "when production volume or process chemistry changes. *Correction:* re-dose and re-test "
            "the effluent; notify NEA of actions taken. *Corrective action:* amend the "
            "management-of-change procedure to mandate an environmental impact and capacity "
            "re-assessment for any volume or process change; re-assess pre-treatment capacity at "
            "the new loading; add continuous monitoring where practicable. *Grade:* MAJOR — a "
            "breach of a legal compliance obligation confirmed by a regulator.\n\n"
            "**CAR 2 — Major.** *Requirement:* clause 6.1.2 requires environmental aspects to be "
            "determined considering change, including new or modified activities, and reasonably "
            "foreseeable emergency situations. *Evidence:* the environmental aspects and risk "
            "register is dated [8 months prior] and contains no entry for the lead-free soldering "
            "process introduced [date], the 30% volume increase, or the revised flux chemistry. "
            "*Nonconformity:* environmental aspects have not been re-determined following material "
            "changes to activities and processes. *Root cause:* same change-management gap, "
            "compounded by the vacant EHS Manager role leaving the register unowned. *Correction:* "
            "re-run the aspects identification for all three changes. *Corrective action:* assign "
            "ownership of the register; require aspects review as a gate in the change process; "
            "set a periodic review frequency. *Grade:* MAJOR — a systemic failure of a core "
            "planning process.\n\n"
            "**CAR 3 — Minor (escalating to Major if systemic).** *Requirement:* clause 8.1 "
            "requires operational controls consistent with operating criteria; hazardous waste "
            "storage must permit correct identification and handling. *Evidence:* on [date], three "
            "waste containers in the soldering area were observed without labels identifying "
            "contents or hazards; the adjacent spill containment bund was cracked with visible "
            "leakage. *Nonconformity:* operational controls for hazardous waste storage and spill "
            "containment are not implemented as required. *Root cause:* no scheduled inspection of "
            "the waste storage area and no bund integrity testing regime; competence and awareness "
            "gaps following the EHS Manager's departure. *Correction:* label the three containers; "
            "repair the bund; contain and clean the leak. *Corrective action:* introduce a "
            "documented weekly waste-area inspection with a checklist; add bund integrity testing "
            "to the maintenance schedule; re-train soldering staff on waste labelling. *Grade:* "
            "MINOR individually; raise to MAJOR because it occurs together with CAR 1 and CAR 2, "
            "evidencing a systemic operational-control breakdown.\n\n"
            "**Report sections.** Objective, scope, criteria and dates · audit team and auditees · "
            "sampling basis and its limitations · findings graded with clause and evidence · "
            "positive observations · opportunities for improvement (kept separate from "
            "nonconformities) · the conclusion on conformity and effective implementation · agreed "
            "corrective action owners and due dates · distribution and follow-up."
        ),
        debrief=(
            "Push hard on three things. First, **the override rule**: a group that scored the copper "
            "exceedance as 'medium' and left it out of the significant list has missed the point — "
            "a breached legal limit is significant regardless of the arithmetic. Second, **root "
            "cause depth**: any group whose 5 Whys ends at 'the operator did not check' has stopped "
            "at a person; make them push to the process. Third, **the vacant EHS Manager is the "
            "connective tissue** — it explains the stale register, the missed capacity assessment "
            "and the uninspected storage area. The best answers name it as a root cause of the "
            "others rather than as a fifth unrelated risk."
        ),
        pitfalls=[
            "You wrote 'copper' or 'pollution' in the aspect column. The aspect is the "
            "INTERACTION ('discharge of trade effluent containing copper').",
            "You scored the copper exceedance as medium and left it off the significant list. "
            "A breached legal limit is significant regardless of the arithmetic.",
            "Your 5 Whys stopped at 'the operator did not check'. Push to the missing process "
            "step — that is what corrective action can fix.",
            "Your CAR lists only corrections (re-label, repair). Clause 10.2 also requires "
            "action to eliminate the CAUSE.",
            "You graded everything Major. Grade against your defined criteria and justify each "
            "one; over-grading destroys credibility as fast as under-grading.",
            "You omitted the sampling statement from the report. It is the most commonly "
            "missed element and it protects you.",
        ],
        test="Your register separates aspect from impact correctly on every line, covers normal / "
             "abnormal / emergency conditions, applies the override rule so the copper exceedance "
             "is significant, your 5 Whys reaches a process cause (not a person), and each of your "
             "three CARs contains requirement + evidence + nonconformity with a stated grade.",
    ),
]
