"""Topic 2 activities — Auditing ISO 14001:2015 (LO2 · K3 A2).

Same dict contract as data_domain1.py.
"""

DOMAIN2 = [
    dict(
        num=2,
        title="AquaPure — Planning the Engagement and the Audit Checklist",
        minutes=60,
        topic="02",
        ka="K3 · A2",
        desc=("AquaPure's workload has tripled on a new government contract, its audit procedure is "
              "five years old, and two 'closed' nonconformities have no verification evidence. "
              "Plan the engagement stage by stage, build the checklist, and decide how you will "
              "handle each stakeholder group."),
        flow=[
            "Walk the ISO 19011 §6.2–6.7 lifecycle and list actions for AquaPure at each stage",
            "Draft the audit plan: objective, criteria, scope, sampling and timetable",
            "Write 8 checklist lines with the clause, the question and the evidence sought",
            "Build the stakeholder engagement matrix for the four groups",
            "Rehearse the opening meeting and one interview using the questioning funnel",
        ],
        build="An Audit Plan + an 8-line risk-based Audit Checklist + a Stakeholder Engagement "
              "Matrix for the AquaPure wastewater audit, plus a rehearsed opening-meeting script.",
        services="Activity 2 brief · ISO 19011:2018 lifecycle map · Checklist and plan templates",

        scenario=(
            "**AquaPure Water Treatment Services Ltd** provides industrial water-treatment solutions "
            "to factories and commercial buildings across Southeast Asia. It runs a **central "
            "treatment plant** and deploys **mobile treatment units to client sites**.\n\n"
            "AquaPure recently won a large government contract to treat wastewater from a new "
            "industrial park, which has **tripled its operational workload**. The EMS Manager has "
            "scheduled an internal audit of the wastewater treatment operations.\n\n"
            "During your preliminary review you discover:\n\n"
            "* the internal audit procedure was written **five years ago** and has not been updated "
            "for the expanded operations or the government contract requirements;\n"
            "* the previous audit report (12 months ago) raised **two minor nonconformities** — "
            "(1) incomplete training records for mobile unit operators, and (2) inconsistent "
            "calibration of pH monitoring equipment. Both were marked **'closed'**, but **no "
            "verification evidence was found**;\n"
            "* four stakeholder groups feature in the audit process: **Operations staff, Client "
            "representatives, Regulatory authorities (e.g. NEA), and Senior management**;\n"
            "* the audit schedule allocates **equal time to all departments**, regardless of risk "
            "level or operational significance;\n"
            "* the Operations Manager is concerned that **mobile unit operators at client sites are "
            "not consistently following the effluent discharge monitoring procedures**."
        ),
        facts=[
            "Central plant + mobile units deployed to third-party client sites.",
            "New government contract tripled the operational workload.",
            "Internal audit procedure is 5 years old — predates the expansion.",
            "2 minor NCs from 12 months ago marked 'closed' with NO verification evidence.",
            "Stakeholders: Operations staff, Client reps, Regulators (NEA), Senior management.",
            "Audit schedule gives equal time to every department irrespective of risk.",
            "Operations Manager suspects mobile operators deviate from discharge monitoring procedures.",
        ],
        steps=[
            ("Separate the audit PROGRAMME from THIS audit",
             "ISO 19011 Clause 5 governs the programme (frequency, methods, responsibilities, "
             "resources, monitoring and improvement); Clause 6 governs the individual audit. "
             "AquaPure's failures are mostly programme-level: a 5-year-old procedure, equal time "
             "regardless of risk, and unverified closures. Record them as programme findings against "
             "ISO 14001 clause 9.2.2, which requires the programme to take into account the "
             "environmental importance of the processes and the results of previous audits."),
            ("Stage 1 — Initiating the audit (§6.2)",
             "Establish contact with the auditee, confirm the audit's feasibility, and confirm your "
             "authority to audit. For AquaPure, feasibility is a genuine question: mobile units "
             "operate on CLIENT premises, so site access must be negotiated in advance. If you cannot "
             "get access, say so now — not in the report."),
            ("Stage 2 — Preparing audit activities (§6.3)",
             "Review documented information (the audit procedure, the previous report, the CAR "
             "records, discharge licences and monitoring data). Prepare the audit plan. Assign work. "
             "Prepare work documents — the checklist. Critically, decide your SAMPLING approach: how "
             "many mobile units, which clients, which months of monitoring data, and why."),
            ("Write the audit plan",
             "Objective: determine conformity of the wastewater treatment operations with "
             "ISO 14001:2015, AquaPure's own procedures and its discharge obligations, and whether "
             "the EMS is effectively implemented — with specific attention to mobile operations and "
             "to the effectiveness of previous corrective actions. Criteria, scope, dates, auditors, "
             "locations (central plant + a sample of client sites), and the timetable including "
             "opening and closing meetings."),
            ("Build the risk-based checklist",
             "Eight lines minimum, each with three columns: the CLAUSE, the QUESTION you will ask, "
             "and the EVIDENCE you expect to see. Weight it toward the risk: mobile operations, "
             "calibration, training/competence, discharge monitoring, and the two previous NCs. "
             "A generic clause-by-clause tick-list is the wrong answer — the checklist must be "
             "specific to AquaPure."),
            ("Attack the unverified closures",
             "The two 'closed' NCs with no verification evidence are the strongest audit trail in "
             "the scenario. ISO 14001 clause 10.2(d) requires the organisation to review the "
             "EFFECTIVENESS of corrective action taken, and to retain documented information on the "
             "results. Closure without verification is a nonconformity against 10.2 in its own "
             "right — and both original NCs must be re-tested to see whether they recurred."),
            ("Build the stakeholder engagement matrix",
             "For each of the four groups record: what you need from them, when in the audit you "
             "engage them, how you engage (interview, opening/closing meeting, document request, "
             "observation), and the risk of engaging them badly. Note that Client representatives "
             "are NOT the auditee — you have no authority over them and need permission and "
             "confidentiality care; and Regulators are usually engaged INDIRECTLY through records "
             "of correspondence, not interviewed."),
            ("Stage 3 — Conducting the audit (§6.4) and the opening meeting",
             "Run the opening meeting agenda: introductions and roles, confirm the plan and "
             "timetable, confirm criteria and scope, confirm communication channels and the guide, "
             "explain the sampling basis and its uncertainty, explain how findings will be graded "
             "and reported, confirm safety/escort arrangements, and confirm the closing meeting "
             "time. Then rehearse ONE interview with a mobile unit operator using the funnel: "
             "open -> probing -> closed -> show me."),
        ],
        questions=[
            ("Identify and explain the key stages of the ISO 14001:2015 internal audit engagement "
             "for AquaPure. For each stage, describe the specific actions you would take.",
             "All six ISO 19011 stages must appear (initiating, preparing, conducting, reporting, "
             "completing, follow-up) and — critically — each action must be AquaPure-specific: "
             "client-site access, mobile-unit sampling, re-testing the two closed NCs."),
            ("How should you engage each of the four stakeholder groups to ensure a comprehensive "
             "and effective audit?",
             "Look for differentiation. Operations staff = the main evidence source, interviewed on "
             "site, non-threatening technique. Client reps = access and permission, confidentiality, "
             "not the auditee. Regulators = usually via records of correspondence and licences, not "
             "interviewed. Senior management = opening/closing meetings, resources, and the "
             "programme-level failures."),
            ("What programme-level (as opposed to audit-level) findings does this scenario reveal?",
             "The 5-year-old procedure, equal time regardless of risk, and closure without "
             "verification. All three sit against ISO 14001 clause 9.2.2 and ISO 19011 Clause 5."),
        ],
        answers=(
            "**Stages.** *Initiating (§6.2)* — contact the EMS Manager, confirm authority, and "
            "resolve access to client sites where mobile units operate; without that access the "
            "audit is not feasible as scoped. *Preparing (§6.3)* — review the 5-year-old procedure, "
            "the previous report, both CARs, the discharge licence and 12 months of monitoring data; "
            "write the plan; build a risk-weighted checklist; define the sample (e.g. 3 of 12 mobile "
            "units across 2 client sites, plus 6 months of pH and discharge records). *Conducting "
            "(§6.4)* — opening meeting; collect evidence by interview, observation, documents and "
            "records; verify what operators say by watching them work and by tracing records; "
            "generate findings; closing meeting. *Reporting (§6.5)* — a report stating criteria, "
            "scope, sample, findings graded major/minor/OFI, and conclusions on effectiveness. "
            "*Completing (§6.6)* — distribute, retain records, close the audit. *Follow-up (§6.7)* — "
            "verify the corrective actions, this time with evidence.\n\n"
            "**Stakeholders.** *Operations staff* — the primary evidence source; interview on site "
            "using open questions, never blame; they will tell you what actually happens if they are "
            "not threatened. *Client representatives* — gatekeepers for site access, not auditees; "
            "obtain permission in advance, observe their site rules, and keep AquaPure's and the "
            "client's information confidential. *Regulatory authorities (NEA)* — normally engaged "
            "indirectly: review licences, permits, submitted monitoring returns and any "
            "correspondence or warnings; an internal auditor does not interview the regulator. "
            "*Senior management* — opening and closing meetings, and the audience for the "
            "programme-level findings; they own the resources and the decision to move to risk-based "
            "scheduling.\n\n"
            "**Programme findings.** The audit procedure has not been maintained (9.2.2 requires the "
            "programme to consider changes affecting the organisation — the workload tripled). Equal "
            "time regardless of risk contradicts 9.2.2's requirement to consider the environmental "
            "importance of the processes concerned. And closure of both prior NCs without "
            "verification evidence breaches 10.2(d) and 10.2's retention requirement."
        ),
        debrief=(
            "Three teaching points. First, **most of AquaPure's problems are programme problems, not "
            "audit problems** — this is the distinction no commercial competitor teaches, and it is "
            "the difference between an auditor who fixes one audit and one who fixes the system. "
            "Second, **'closed' is not a finding of effectiveness**: clause 10.2(d) requires a review "
            "of effectiveness, and no evidence means no closure. Third, contrast the groups' "
            "checklists — the ones that wrote generic clause questions will visibly have less to ask "
            "than those who wrote AquaPure-specific ones."
        ),
        pitfalls=[
            "Your checklist is a generic clause-by-clause tick-list. Rebuild it from "
            "AquaPure's own risks: mobile units, calibration, training, discharge monitoring.",
            "You missed the third checklist column. Every line needs the EVIDENCE you expect "
            "to see, not just the question.",
            "You classified the 5-year-old procedure as an audit finding. It is a PROGRAMME "
            "finding against ISO 14001 cl. 9.2.2.",
            "You accepted 'closed' on the two previous NCs. Clause 10.2(d) requires a review "
            "of EFFECTIVENESS — no evidence means no closure.",
            "You planned to interview the regulator. Internal auditors engage NEA indirectly, "
            "through licences, returns and correspondence.",
            "You forgot client-site access. If you cannot reach the mobile units, the audit is "
            "not feasible as scoped — raise it at initiation, not in the report.",
        ],
        test="Your checklist has at least 8 lines, every line names a clause AND the specific "
             "evidence you will ask to see, at least 4 lines target mobile operations / calibration / "
             "training / the previous NCs, and your matrix treats client representatives differently "
             "from the auditee.",
    ),
]
