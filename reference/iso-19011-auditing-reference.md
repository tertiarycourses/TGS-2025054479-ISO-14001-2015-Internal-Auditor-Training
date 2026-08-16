# ISO 19011:2018 and the Practical Craft of Internal EMS Auditing
### Reference notes for ISO 14001:2015 Internal Auditor training courseware

> **Source note.** Clause and Annex A material below is taken from the text of **ISO 19011:2018, *Guidelines for auditing management systems*** (2nd edition, July 2018). ISO 19011 is a **guidance** standard — it uses "should", not "shall". Nothing in it is auditable in its own right. ISO 14001:2015 **clause 9.2** is what actually *requires* internal audits; ISO 19011 tells you *how* to do them well. Grading rules (major/minor) come from **ISO/IEC 17021-1:2015** and certification-body practice, not from ISO 19011 itself — ISO 19011 only says findings "can be graded".

---

## 0. Vocabulary you must teach first

These definitions (ISO 19011:2018 Clause 3, drawn from ISO 9000:2015) are the load-bearing terms. Learners who confuse *criteria / evidence / finding / conclusion* will write bad nonconformities all week.

| Term | Definition (ISO 19011:2018 Cl. 3) |
|---|---|
| **Audit** (3.1) | "Systematic, independent and documented process for obtaining objective evidence and evaluating it objectively to determine the extent to which the audit criteria are fulfilled." Internal audits = **first-party**. Second-party = by an interested party (e.g. a customer auditing you). Third-party = independent certification body or regulator. |
| **Audit programme** (3.4) | "Arrangements for a set of one or more audits planned for a specific time frame and directed towards a specific purpose." (The *year's* plan — not one audit.) |
| **Audit scope** (3.5) | "Extent and boundaries of an audit" — physical **and virtual** locations, functions, organizational units, activities, processes, and the **time period** covered. |
| **Audit plan** (3.6) | "Description of the activities and arrangements for an audit." (One specific audit.) |
| **Audit criteria** (3.7) | "Set of requirements used as a reference against which objective evidence is compared." May include policies, procedures, work instructions, legal requirements, contractual obligations. *Note 1:* if the criteria are legal requirements, the words **compliance / non-compliance** are used instead. |
| **Objective evidence** (3.8) | "Data supporting the existence or verity of something." Obtainable "through observation, measurement, test or by other means"; generally consists of "records, statements of fact, or other information which are relevant to the audit criteria and **verifiable**." |
| **Audit evidence** (3.9) | "Records, statements of fact or other information, which are relevant to the audit criteria and **verifiable**." |
| **Audit findings** (3.10) | "Results of the evaluation of the collected audit evidence against audit criteria." Indicate conformity or nonconformity; can also lead to identification of risks, OFIs, or recording good practices. |
| **Audit conclusion** (3.11) | "Outcome of an audit, after consideration of the audit objectives and all audit findings." |
| **Audit client** (3.12) | "Organization or person requesting an audit." For internal audits this can be the auditee itself or the person managing the programme. |
| **Auditee** (3.13) | "Organization as a whole or parts thereof being audited." |
| **Technical expert** (3.16) | Provides specific knowledge/expertise to the team — **does not act as an auditor**. |
| **Observer** (3.17) | Accompanies the team but **does not act as an auditor**. |
| **Nonconformity** (3.21) | "Non-fulfilment of a requirement." |
| **Conformity** (3.20) | "Fulfilment of a requirement." |
| **Competence** (3.22) | "Ability to apply knowledge and skills to achieve intended results." |
| **Combined audit** (3.2) | Two or more management systems audited together at one auditee (e.g. 14001 + 45001). |
| **Joint audit** (3.3) | One auditee audited by two or more *auditing organizations*. |

**Teaching point — the audit equation:**
`Criteria (what should be) + Evidence (what is) → Finding (the gap or the match) → Conclusion (the overall verdict)`

---

## 1. The seven audit principles (ISO 19011:2018, Clause 4)

ISO 19011 states these principles "should help to make the audit an effective and reliable tool... Adherence to these principles is a prerequisite for providing audit conclusions that are relevant and sufficient, and for **enabling auditors, working independently from one another, to reach similar conclusions in similar circumstances**." That last phrase is the whole point — the principles exist to make audits *reproducible*.

### a) Integrity — "the foundation of professionalism"
Auditors and the person managing the audit programme should perform their work ethically, with honesty and responsibility, and should **only undertake audit activities if competent to do so**. They must work impartially — fair and unbiased in all dealings. They should stay sensitive to any influences that may be exerted on their judgement while carrying out an audit (pressure from a manager to downgrade a finding is the classic EMS example).

### b) Fair presentation — "the obligation to report truthfully and accurately"
Audit findings, conclusions and reports should reflect the audit activities truthfully and accurately. **Significant obstacles encountered and unresolved diverging opinions between the audit team and the auditee must be reported** — you do not quietly drop a finding because the auditee disagreed. All communication should be "truthful, accurate, objective, timely, clear and complete."

### c) Due professional care — "the application of diligence and judgement in auditing"
Auditors should exercise care in proportion to the importance of the task they perform and the confidence placed in them by the audit client and other interested parties. The standard singles out one factor as most important: **"having the ability to make reasoned judgements in all audit situations."** In an EMS this means knowing when a missing waste manifest is trivial paperwork and when it is a regulatory exposure.

### d) Confidentiality — "security of information"
Auditors should exercise discretion in the use and protection of information acquired during their duties. Audit information **must not be used inappropriately for personal gain** by the auditor or the audit client, or in a manner detrimental to the auditee's legitimate interests. Includes proper handling of sensitive or proprietary information — e.g. process formulations, emissions data before regulatory submission, incident details.

### e) Independence — "the basis for the impartiality of the audit and objectivity of the audit conclusions"
Auditors should be independent of the activity being audited wherever practicable, and should **in all cases** act free from bias and conflict of interest. For internal audits, auditors should be independent from the function being audited if practicable. Objectivity must be maintained throughout so findings rest **only** on audit evidence.
> **Critical for internal auditor training:** ISO 19011 explicitly concedes that "for small organizations, it may not be possible for internal auditors to be fully independent of the activity being audited, but **every effort should be made to remove bias and encourage objectivity**." The practical rule taught in class: **you may not audit your own work.** Cross-departmental pairing (the warehouse auditor audits the lab, the lab auditor audits the warehouse) is the standard workaround.

### f) Evidence-based approach — "the rational method for reaching reliable and reproducible audit conclusions in a systematic audit process"
Audit evidence should be **verifiable**. It should generally be based on **samples** of the available information, since an audit runs for a finite time with finite resources. "An appropriate use of sampling should be applied, since this is closely related to the confidence that can be placed in the audit conclusions." This principle is the source of the mandatory sampling caveat in every audit report and closing meeting.

### g) Risk-based approach — "an audit approach that considers risks and opportunities"
**New in the 2018 edition** (the 2011 edition had six principles). The risk-based approach "should substantively influence the **planning, conducting and reporting** of audits in order to ensure that audits are focused on matters that are significant for the audit client, and for achieving the audit programme objectives." In EMS terms: spend your audit days on the significant environmental aspects, the permitted discharges and the emergency scenarios — not on evenly dividing time across all clauses.

---

## 2. Clause 5 — Managing an audit programme

Clause 5 runs on a **Plan-Do-Check-Act** cycle (ISO 19011 Figure 1): 5.2–5.4 Plan → 5.5 Do → 5.6 Check → 5.7 Act.

### 5.1 General
An audit programme may cover one or more management system standards, audited separately or in combination. **Its extent should be based on** the size and nature of the auditee, and the nature, functionality, complexity, type of risks and opportunities, and **level of maturity** of the management system(s).

To understand the auditee's context, the programme should take into account the auditee's:
- organizational objectives;
- relevant external and internal issues;
- needs and expectations of relevant interested parties;
- information security and confidentiality requirements.

Two rules with teeth:
- The individual(s) managing the programme "should ensure the integrity of the audit is maintained and that **there is not undue influence exerted over the audit**."
- **"Audit priority should be given to allocating resources and methods to matters in a management system with higher inherent risk and lower level of performance."**

**The audit programme must include/identify (5.1 a–i):**
| | Item |
|---|---|
| a | objectives for the audit programme |
| b | risks and opportunities associated with the programme, and actions to address them |
| c | scope (extent, boundaries, locations) of each audit |
| d | schedule — number / duration / frequency of audits |
| e | audit types (internal or external) |
| f | audit criteria |
| g | audit methods to be employed |
| h | criteria for selecting audit team members |
| i | relevant documented information |

### 5.2 Establishing audit programme objectives
The **audit client** ensures objectives are established, and that they are consistent with the client's strategic direction and support the management system policy and objectives.

*Objectives can be based on:* (a) needs/expectations of interested parties; (b) characteristics and requirements of processes, products, services, projects and changes to them; (c) management system requirements; (d) need to evaluate external providers; (e) the auditee's performance level and system maturity (KPIs, occurrence of nonconformities/incidents/complaints); (f) identified risks and opportunities; (g) results of previous audits.

*Examples of programme objectives given in the standard:*
- identify opportunities for improvement of the management system and its performance;
- evaluate the capability of the auditee to determine its context;
- evaluate the capability to determine risks and opportunities and implement effective actions;
- **conform to all relevant requirements, e.g. statutory and regulatory requirements, compliance commitments**, certification requirements *(directly relevant to ISO 14001 clause 6.1.3 / 9.1.2)*;
- obtain and maintain confidence in an external provider's capability;
- determine the continuing **suitability, adequacy and effectiveness** of the management system;
- evaluate compatibility/alignment of system objectives with the organization's strategic direction.

### 5.3 Determining and evaluating audit programme risks and opportunities
The person managing the programme "should identify and present to the audit client the risks and opportunities considered when developing the audit programme and resource requirements."

**Risks (a–h):**
| | Risk area | Example given |
|---|---|---|
| a | Planning | failure to set relevant audit objectives; wrong extent, number, duration, locations, schedule |
| b | Resources | insufficient time, equipment and/or training |
| c | Selection of the audit team | insufficient overall competence |
| d | Communication | ineffective external/internal communication processes/channels |
| e | Implementation | ineffective coordination of audits; not considering information security and confidentiality |
| f | Control of documented information | failure to determine needed documented information; failure to adequately protect audit records |
| g | Monitoring, reviewing and improving the programme | ineffective monitoring of programme outcomes |
| h | Availability and cooperation of auditee, and availability of evidence to be sampled | — |

**Opportunities for improving the programme:**
- allowing multiple audits to be conducted in a single visit;
- minimizing time and distances travelling to site;
- matching the competence level of the team to what the audit objectives need;
- aligning audit dates with the availability of the auditee's key staff.

### 5.4 Establishing the audit programme

**5.4.1 Roles and responsibilities of the individual(s) managing the programme (a–h):**
- **a)** establish the extent of the programme according to objectives and known constraints;
- **b)** determine external/internal issues and risks/opportunities affecting the programme, and implement actions to address them;
- **c)** ensure selection of audit teams and overall competence by assigning roles, responsibilities and authorities, with leadership support;
- **d)** establish all relevant processes, including: coordination and scheduling of audits; establishing audit objectives, scopes and criteria, determining methods and selecting the team; **evaluating auditors**; external/internal communication; **resolution of disputes and handling of complaints**; audit follow-up; reporting to the audit client and interested parties;
- **e)** determine and ensure provision of all necessary resources;
- **f)** ensure appropriate documented information is prepared and maintained, including programme records;
- **g)** monitor, review and improve the programme;
- **h)** communicate the programme to the audit client and relevant interested parties.

The individual managing the programme **should request its approval by the audit client**.

**5.4.2 Competence of the individual(s) managing the programme** — knowledge of: (a) audit principles, methods and processes; (b) management system standards and other reference/guidance documents; (c) information on the auditee and its context; (d) applicable statutory/regulatory and other requirements. Knowledge of risk management, project and process management, and ICT may also be considered. They "should engage in appropriate continual development activities."

**5.4.3 Establishing extent of the audit programme** — factors (a–m) include: objective/scope/duration and number of audits; the standards or criteria applied; number, importance, complexity, similarity and **locations** of activities; factors influencing system effectiveness; applicable criteria including statutory/regulatory and other commitments; results of previous internal/external audits and management reviews; results of a previous programme review; **language, cultural and social issues**; concerns of interested parties (complaints, non-compliance, supply chain issues); significant changes to context/operations and related risks; availability of ICT to support remote auditing; **the occurrence of internal and external events, such as nonconformities of product or service, information security leaks, health and safety incidents, criminal acts or environmental incidents**; business risks and opportunities.

**5.4.4 Determining audit programme resources** — (a) financial and time resources; (b) audit methods; (c) availability of auditors and technical experts with appropriate competence; (d) extent of the programme and its risks/opportunities; (e) travel time and cost, accommodation; (f) impact of different time zones; (g) availability of ICT; (h) availability of tools, technology and equipment; (i) availability of necessary documented information; (j) **facility requirements including security clearances and equipment — background checks, PPE, clean-room attire**.

### 5.5 Implementing the audit programme
**5.5.1 General** — the manager should: (a) communicate relevant parts of the programme, including risks and opportunities, to interested parties and inform them of progress; (b) define objectives, scope and criteria for each individual audit; (c) select audit methods; (d) coordinate and schedule audits; (e) ensure teams have necessary competence; (f) provide resources; (g) ensure audits are conducted per the programme, managing operational risks and unexpected events; (h) ensure documented information is managed and maintained; (i) define and implement operational controls for monitoring; (j) review the programme to identify improvement opportunities.

**5.5.2 Defining objectives, scope and criteria for an individual audit**

*Audit objectives may include (a–f):*
- **a)** determination of the extent of conformity of the management system (or parts) with audit criteria;
- **b)** evaluation of the capability of the system to help the organization meet statutory/regulatory and other requirements it is committed to;
- **c)** evaluation of the **effectiveness** of the system in meeting its intended results;
- **d)** identification of opportunities for potential improvement;
- **e)** evaluation of the **suitability and adequacy** of the system relative to context and strategic direction;
- **f)** evaluation of the capability to establish and achieve objectives and effectively address risks and opportunities in a changing context.

*Audit scope* includes locations, functions, activities and processes to be audited, plus the **time period covered**.

*Audit criteria* "are used as a reference against which conformity is determined" and may include: applicable policies, processes, procedures, performance criteria including objectives, statutory and regulatory requirements, management system requirements, information on context and risks/opportunities as determined by the auditee, sector codes of conduct or other planned arrangements.

**5.5.3–5.5.7** cover: selecting audit methods; selecting audit team members (competence needed to achieve objectives, impartiality, ability to work together); assigning responsibility for an individual audit to the **audit team leader**; managing audit programme results; and managing and maintaining audit programme records (records on each audit, programme review results, personnel records covering auditor competence and performance evaluation).

### 5.6 Monitoring the audit programme
The manager should ensure evaluation of:
- **a)** whether schedules are being met and programme objectives achieved;
- **b)** the performance of audit team members including the team leader and technical experts;
- **c)** the ability of the audit teams to implement the audit plan;
- **d)** feedback from audit clients, auditees, auditors, technical experts and other relevant parties;
- **e)** sufficiency and adequacy of documented information in the whole audit process.

*Factors indicating a need to modify the programme:* changes to audit findings; demonstrated level of the auditee's system effectiveness and maturity; effectiveness of the programme; audit or programme scope; the auditee's management system; standards and other commitments; external providers; **identified conflicts of interest**; the audit client's requirements.

### 5.7 Reviewing and improving the audit programme
The manager and the audit client review the programme to assess whether objectives were achieved; **"lessons learned from the audit programme review should be used as inputs for the improvement of the programme."**

The manager should ensure: review of overall implementation; identification of areas and opportunities for improvement; application of changes if necessary; **review of the continual professional development of auditors (per 7.6)**; reporting of results and the review to the audit client and interested parties.

*The review should consider (a–h):* results and trends from monitoring; conformity with programme processes and documented information; evolving needs and expectations of interested parties; audit programme records; alternative or new auditing methods; alternative or new methods to evaluate auditors; effectiveness of actions to address risks/opportunities and internal/external issues; confidentiality and information security issues.

---

## 3. Clause 6 — Conducting an audit (the 6.1–6.7 lifecycle)

The full sequence — this is the backbone of the course:

```
6.2 Initiating          → establish contact with auditee; determine feasibility
6.3 Preparing           → review documented information; plan the audit;
                          assign work; prepare work documents/checklists
6.4 Conducting          → guides & observers; OPENING MEETING; communicating;
                          information access; reviewing documented information;
                          collecting & verifying information; generating findings;
                          determining conclusions; CLOSING MEETING
6.5 Reporting           → prepare audit report; distribute audit report
6.6 Completing          → all planned activities done; retain/dispose records
6.7 Follow-up           → corrections, corrective actions, OFIs; verify effectiveness
```

### 6.1 General
Guidance on preparing and conducting a specific audit within a programme. "The extent to which the provisions of this clause are applicable depends on the objectives and scope of the specific audit." (i.e. scale it — a 2-hour internal audit of one department does not need the full ceremony.)

### 6.2 Initiating the audit

**6.2.1 General** — "The responsibility for conducting the audit should remain with the assigned **audit team leader** until the audit is completed."

**6.2.2 Establishing contact with the auditee (a–k):**
- **a)** confirm communication channels with the auditee's representatives;
- **b)** confirm the **authority** to conduct the audit;
- **c)** provide information on audit objectives, scope, criteria, methods and team composition, including technical experts;
- **d)** request access to relevant information for planning, **including information on the risks and opportunities the organization has identified and how they are addressed**;
- **e)** determine applicable statutory and regulatory requirements and other requirements relevant to the auditee's activities, processes, products and services;
- **f)** confirm agreement on the extent of disclosure and treatment of confidential information;
- **g)** make arrangements for the audit including the schedule;
- **h)** determine location-specific arrangements for access, **health and safety**, security, confidentiality;
- **i)** agree on attendance of observers and the need for guides or interpreters;
- **j)** determine areas of interest, concern or risks to the auditee in relation to the audit;
- **k)** resolve issues regarding composition of the audit team with the auditee or audit client.

**6.2.3 Determining feasibility of the audit** — to give "reasonable confidence that the audit objectives can be achieved", considering availability of: (a) sufficient and appropriate information for planning and conducting; (b) adequate cooperation from the auditee; (c) adequate time and resources. **"Where the audit is not feasible, an alternative should be proposed to the audit client, in agreement with the auditee."**

### 6.3 Preparing audit activities

**6.3.1 Performing review of documented information** — review the auditee's relevant documented information in order to:
- gather information to understand the auditee's operations and to prepare audit activities and applicable work documents;
- **"establish an overview of the extent of the documented information to determine possible conformity to the audit criteria and detect possible areas of concern, such as deficiencies, omissions or conflicts."**

It "should include, but not be limited to: management system documents and records, as well as **previous audit reports**." Take into account the auditee's size, nature, complexity, related risks and opportunities, and the audit scope/criteria/objectives.

> **EMS practice point:** the desktop review for an ISO 14001 audit typically pulls the environmental policy, the aspects/impacts register, the register of compliance obligations, environmental objectives and programmes, the legal register, permits/licences, monitoring data, previous audit reports and NC logs, and management review minutes.

**6.3.2 Audit planning**

*6.3.2.1 Risk-based approach to planning.* The team leader "should adopt a risk-based approach to planning". Planning should consider **the risks of the audit activities on the auditee's processes**. In planning, consider: (a) the composition of the team and its overall competence; (b) **the appropriate sampling techniques**; (c) opportunities to improve effectiveness and efficiency of the audit; (d) risks to achieving the audit objectives created by ineffective planning; (e) **risks to the auditee created by performing the audit** — e.g. "the presence of the audit team members adversely influencing the auditee's arrangements for health and safety, environment and quality, and its products, services, personnel or infrastructure (e.g. contamination in clean room facilities)."

*6.3.2.2 Audit planning details.* The audit plan should address or reference:
| | Item |
|---|---|
| a | the audit objectives |
| b | the audit scope, including identification of the organization and its functions, and processes to be audited |
| c | the audit criteria and any reference documented information |
| d | the locations (**physical and virtual**), dates, expected time and duration of audit activities, including meetings with management |
| e | the need for the team to familiarize themselves with facilities and processes (site tour, ICT review) |
| f | the audit methods to be used, **including the extent to which audit sampling is needed to obtain sufficient audit evidence** |
| g | roles and responsibilities of audit team members, guides, observers, interpreters |
| h | allocation of appropriate resources based on risks and opportunities of the activities audited |

*Also take into account, as appropriate:* identification of the auditee's representative(s); the working and reporting **language**; the audit report topics; logistics and communications arrangements; specific actions to address risks to achieving objectives; **confidentiality and information security**; any follow-up actions from a previous audit or other sources (lessons learned, project reviews); any follow-up activities to the planned audit; coordination with other audit activities in a joint audit.

"Audit plans should be presented to the auditee. Any issues with the audit plans should be resolved between the audit team leader, the auditee and, if necessary, the individual(s) managing the audit programme." Planning "should be sufficiently flexible to permit changes which can become necessary as the audit activities progress."

**6.3.3 Assigning work to the audit team** — the team leader, **in consultation with the team**, assigns responsibility for auditing specific processes, activities, functions or locations, and as appropriate the authority for decision-making. Assignments should take into account **impartiality, objectivity and competence** of auditors, effective use of resources, and the different roles of auditors, **auditors-in-training** and technical experts. "Changes to the work assignments can be made as the audit progresses."

**6.3.4 Preparing documented information for the audit (work documents / checklists)**
Team members collect and review information relevant to their assignments and prepare documented information, which "can include but is not limited to":
- **a)** physical or digital **checklists**;
- **b)** audit **sampling details**;
- **c)** **audio visual information**.

> **The checklist warning, verbatim from the standard:** *"The use of these media should not restrict the extent of audit activities, which can change as a result of information collected during the audit."* Teach this hard — the checklist is a memory aid, not a script, and never a cage.

Documented information prepared for and resulting from the audit should be retained at least until audit completion. Confidential or proprietary information created during the audit "should be suitably safeguarded at all times by the audit team members."

**A.13 Preparing audit work documents** — for each work document ask:
- a) Which **audit record** will be created by using this work document?
- b) Which **audit activity** is linked to this particular work document?
- c) Who will be the **user** of this work document?
- d) What **information is needed** to prepare this work document?

For combined audits (e.g. 14001 + 45001), avoid duplication by **clustering similar requirements from different criteria** and **coordinating the content of related checklists and questionnaires**.

### 6.4 Conducting audit activities

**6.4.1 General** — activities are normally conducted in a defined sequence, but "this sequence may be varied to suit the circumstances of specific audits."

**6.4.2 Roles and responsibilities of guides and observers**

*Both:* may accompany the team with approvals from the team leader, audit client and/or auditee. **"They should not influence or interfere with the conduct of the audit."** If that cannot be assured, "the audit team leader should have the right to deny observers from being present during certain audit activities."

*Observers:* arrangements for access, H&S, environmental, security and confidentiality are managed between the audit client and the auditee. An observer does **not** act as an auditor (Cl. 3.17).

*Guides* are **appointed by the auditee**, assist the team, and act on the request of the team leader or their assigned auditor. Responsibilities (a–e):
- **a)** assisting auditors in identifying individuals to participate in interviews and confirming timings and locations;
- **b)** arranging access to specific locations;
- **c)** ensuring rules on location-specific access, **health and safety, environmental**, security, confidentiality are known and respected by team members and observers, and any risks addressed;
- **d)** witnessing the audit on behalf of the auditee, when appropriate;
- **e)** providing clarification or assisting in collecting information, when needed.

> **Classroom caution:** a guide who answers the questions *for* the interviewee has crossed the line into interference. The auditor should politely redirect: *"Thank you — I'd like to hear how Mr Lim does it at his workstation."*

**6.4.3 Conducting the opening meeting** → see the full agenda in **§9** below.

**6.4.4 Communicating during the audit**
- The team "should confer periodically to exchange information, assess audit progress and reassign work between the audit team members, as needed."
- The team leader should **periodically communicate the progress, any significant findings and any concerns** to the auditee and audit client. **"Evidence collected during the audit that suggests an immediate and significant risk should be reported without delay to the auditee and, as appropriate, to the audit client."** *(In EMS: an active uncontained spill, an unpermitted discharge, a breached bund — you stop and report it; you do not save it for the closing meeting.)*
- Any concern about an issue **outside the audit scope** should be noted and reported to the team leader for possible communication to the client and auditee.
- Where evidence indicates the **audit objectives are unattainable**, the team leader reports the reasons to the audit client and auditee to determine action — which "may include changes to audit planning, the audit objectives or audit scope, or **termination of the audit**."
- Formal arrangements may be needed with external interested parties (e.g. regulators), "especially where statutory and regulatory requirements require mandatory reporting of nonconformities."

**6.4.5 Audit information availability and access** — methods depend on objectives, scope, criteria, duration and location; "the location is where the information needed for the specific audit activity is available to the audit team. This may include physical and virtual locations." An audit can use a mixture of methods, and methods may need to change during the audit.

**Table A.1 — Audit methods** (by auditor location × human interaction):

| | **On-site** | **Remote** |
|---|---|---|
| **Human interaction** | Conducting interviews; completing checklists and questionnaires with auditee participation; conducting document review with auditee participation; sampling | Via interactive communication means: conducting interviews; observing work performed with remote guide; completing checklists and questionnaires; conducting document review with auditee participation |
| **No human interaction** | Conducting document review (records, data analysis); observing work performed; conducting on-site visit; completing checklists; sampling (e.g. products) | Conducting document review (records, data analysis); observing work performed via surveillance means (considering social and statutory/regulatory requirements); analysing data |

**6.4.6 Reviewing documented information while conducting the audit** — review to (i) determine conformity of the system, as far as documented, with audit criteria; and (ii) gather information to support audit activities. May be combined with other activities and continue throughout the audit. **If adequate documented information cannot be provided within the audit plan timeframe, the team leader informs both the programme manager and the auditee, and a decision is made whether to continue or suspend the audit.**

**6.4.7 Collecting and verifying information**
Information relevant to objectives, scope and criteria — "including information relating to **interfaces between functions, activities and processes**" — should be collected by appropriate sampling and verified as far as practicable.

> **The evidence gate, verbatim:** *"Only information that can be subject to some degree of verification should be accepted as audit evidence. Where the degree of verification is low the auditor should use their professional judgement to determine the degree of reliance that can be placed on it as evidence. Audit evidence leading to audit findings should be recorded."*

If the team becomes aware of new or changed circumstances, or risks or opportunities, these should be addressed accordingly.

**The four sources / methods of collecting information** (6.4.7, expanded by A.14) → see **§5** below.

**6.4.8 Generating audit findings**
- "Audit evidence should be evaluated against the audit criteria in order to determine audit findings. Audit findings can indicate **conformity or nonconformity**."
- When specified by the audit plan, findings should include **conformity and good practices** with supporting evidence, **opportunities for improvement**, and any recommendations.
- **"Nonconformities and their supporting audit evidence should be recorded."**
- **Grading:** "Nonconformities can be graded depending on the context of the organization and its risks. This grading can be quantitative (e.g. 1 to 5) and qualitative (e.g. minor, major)."
- **"They should be reviewed with the auditee in order to obtain acknowledgement that the audit evidence is accurate and that the nonconformities are understood. Every attempt should be made to resolve any diverging opinions concerning the audit evidence or findings. Unresolved issues should be recorded in the audit report."**
- The team "should meet as needed to review the audit findings at appropriate stages during the audit."
- *Note 2:* conformity/nonconformity against statutory or regulatory requirements "is sometimes referred to as **compliance or non-compliance**."

**A.18.1 Determining audit findings** — consider: (a) follow-up of previous audit records and conclusions; (b) requirements of the audit client; (c) **accuracy, sufficiency and appropriateness of objective evidence to support audit findings**; (d) extent to which planned audit activities are realized and planned results achieved; (e) findings exceeding normal practice, or opportunities for improvement; (f) **sample size**; (g) categorization (if any) of the findings.

**A.18.2 Recording conformities** — record: (a) description of or reference to the audit criteria against which conformity is shown; (b) audit evidence to support conformity and effectiveness; (c) declaration of conformity, if applicable.

**A.18.3 Recording nonconformities** — record: **(a) description of or reference to audit criteria; (b) audit evidence; (c) declaration of nonconformity;** (d) related audit findings, if applicable. *(This is the source of the 3-part NC statement — see §7.)*

**A.18.4 Findings related to multiple criteria** — on a combined audit, where a finding is linked to one criterion, consider the possible impact on corresponding or similar criteria of the other management systems. The auditor may raise **(a) separate findings for each criterion, or (b) a single finding combining references to multiple criteria** — depending on arrangements with the audit client.

**6.4.9 Determining audit conclusions**

*6.4.9.1 Preparation for the closing meeting* — the team should confer **prior to** the closing meeting to:
- **a)** review the audit findings and any other appropriate information collected, against the audit objectives;
- **b)** agree on the audit conclusions, **"taking into account the uncertainty inherent in the audit process"**;
- **c)** prepare recommendations, if specified by the audit plan;
- **d)** discuss audit follow-up, as applicable.

*6.4.9.2 Content of audit conclusions* — should address:
- **a)** the extent of conformity with the audit criteria and **robustness of the management system**, including its effectiveness in meeting intended outcomes, the identification of risks, and effectiveness of actions taken to address risks;
- **b)** the effective **implementation, maintenance and improvement** of the management system;
- **c)** achievement of audit objectives, coverage of audit scope and fulfilment of audit criteria;
- **d)** **similar findings made in different areas** that were audited, or from a joint or previous audit, **for the purpose of identifying trends**.

**6.4.10 Conducting the closing meeting** → see the full agenda in **§9** below.

### 6.5 Preparing and distributing the audit report
**6.5.1 Preparing** and **6.5.2 Distributing** → see the full contents list in **§10** below.

Distribution rules: issued within an agreed period of time; if delayed, reasons communicated to the auditee and the programme manager; **dated, reviewed and accepted** in accordance with the audit programme; then distributed to relevant interested parties defined in the programme or plan; **"appropriate measures to ensure confidentiality should be considered."**

### 6.6 Completing the audit
- "The audit is completed when **all planned audit activities have been carried out**, or as otherwise agreed with the audit client (e.g. there might be an unexpected situation that prevents the audit being completed according to the audit plan)."
- Documented information "should be retained or disposed of by agreement between the participating parties and in accordance with audit programme and applicable requirements."
- **Confidentiality:** "Unless required by law, the audit team and the individual(s) managing the audit programme should not disclose any information obtained during the audit, or the audit report, to any other party **without the explicit approval of the audit client** and, where appropriate, the approval of the auditee."
- "Lessons learned from the audit can identify risks and opportunities for the audit programme and the auditee."

> **Teaching point:** completion of the *audit* is **not** the same as closure of the *findings*. The audit is complete at 6.6; the nonconformities may stay open for weeks under 6.7.

### 6.7 Conducting audit follow-up
- "The outcome of the audit can, depending on the audit objectives, indicate the need for **corrections**, or for **corrective actions**, or **opportunities for improvement**."
- "Such actions are usually **decided and undertaken by the auditee** within an agreed timeframe." *(The auditor does not fix it — that would breach independence.)*
- "As appropriate, the auditee should keep the individual(s) managing the audit programme and/or the audit team informed of the status of these actions."
- **"The completion and effectiveness of these actions should be verified. This verification may be part of a subsequent audit."**
- "Outcomes should be reported to the individual managing the audit programme and reported to the audit client **for management review**." *(This is the hand-off into ISO 14001 clause 9.3.)*

---

## 4. Clause 7 — Competence and evaluation of auditors

### 7.1 General
"Confidence in the audit process and the ability to achieve its objectives depends on the competence of those individuals who are involved in performing audits." Competence should be evaluated regularly through a process considering **personal behaviour** and **the ability to apply knowledge and skills** gained through education, work experience, auditor training and audit experience.

> **Key exam point:** *"It is not necessary for each auditor in the audit team to have the same competence. However, the **overall competence of the audit team** needs to be sufficient to achieve the audit objectives."* This is what lets a competent generalist auditor pair with a technical expert on, say, wastewater treatment.

**The four-step evaluation process:** (a) determine the required competence to fulfil the needs of the audit programme; (b) establish the evaluation criteria; (c) select the appropriate evaluation method; (d) conduct the evaluation.

Outcomes feed: selection of audit team members; determining the need for improved competence (e.g. additional training); ongoing performance evaluation of auditors.

### 7.2.1 Determining auditor competence — what to consider
(a) size, nature, complexity, products, services and processes of auditees; (b) the methods for auditing; (c) the management system disciplines to be audited; (d) the complexity and processes of the system; (e) the **types and levels of risks and opportunities** addressed by the system; (f) the objectives and extent of the audit programme; (g) the uncertainty in achieving audit objectives; (h) other requirements imposed by the audit client or interested parties.

### 7.2.2 Personal behaviour (a–m) — the thirteen desired professional behaviours
| | Behaviour | ISO's own gloss |
|---|---|---|
| a | **Ethical** | fair, truthful, sincere, honest and discreet |
| b | **Open-minded** | willing to consider alternative ideas or points of view |
| c | **Diplomatic** | tactful in dealing with individuals |
| d | **Observant** | actively observing physical surroundings and activities |
| e | **Perceptive** | aware of and able to understand situations |
| f | **Versatile** | able to readily adapt to different situations |
| g | **Tenacious** | persistent and focused on achieving objectives |
| h | **Decisive** | able to reach timely conclusions based on logical reasoning and analysis |
| i | **Self-reliant** | able to act and function independently while interacting effectively with others |
| j | **Able to act with fortitude** | able to act responsibly and ethically, **even though these actions may not always be popular and may sometimes result in disagreement or confrontation** |
| k | **Open to improvement** | willing to learn from situations |
| l | **Culturally sensitive** | observant and respectful to the culture of the auditee |
| m | **Collaborative** | effectively interacting with others, including team members and auditee personnel |

*(Mnemonic that works in class: the two most-tested are **(d) observant** — the EMS auditor's core sense — and **(j) fortitude** — the willingness to raise the finding your boss won't like.)*

### 7.2.3 Knowledge and skills

**7.2.3.1 General** — auditors should possess (a) the knowledge and skills necessary to achieve the intended results of the audits they perform; (b) **generic competence** plus a level of **discipline- and sector-specific** knowledge and skills. Team leaders need additional knowledge and skills to lead.

**7.2.3.2 Generic knowledge and skills — four areas:**

**a) Audit principles, processes and methods.** An auditor should be able to:
- understand the types of risks and opportunities associated with auditing and the principles of the risk-based approach;
- plan and organize the work effectively;
- perform the audit within the agreed time schedule;
- **prioritize and focus on matters of significance**;
- communicate effectively, orally and in writing (personally or through interpreters);
- **collect information through effective interviewing, listening, observing and reviewing documented information**, including records and data;
- **understand the appropriateness and consequences of using sampling techniques**;
- understand and consider technical experts' opinions;
- **audit a process from start to finish, including the interrelations with other processes and different functions**;
- verify the relevance and accuracy of collected information;
- **confirm the sufficiency and appropriateness of audit evidence to support audit findings and conclusions**;
- assess those factors that may affect the reliability of the findings and conclusions;
- document audit activities and findings, and prepare reports;
- maintain the confidentiality and security of information.

**b) Management system standards and other references** — the standards/guidance used to establish criteria or methods; their application by the auditee and other organizations; relationships and interactions between management system processes; the importance and priority of multiple standards; application of standards to different audit situations.

**c) The organization and its context** — needs and expectations of relevant interested parties; type of organization, governance, size, structure, functions and relationships; general business and management concepts, processes and terminology (planning, budgeting, management of individuals); cultural and social aspects of the auditee.

**d) Applicable statutory and regulatory requirements and other requirements** — the requirements and their governing agencies; basic legal terminology; contracting and liability.
> **Critical caveat, verbatim:** *"Awareness of statutory and regulatory requirements does not imply legal expertise and a management system audit **should not be treated as a legal compliance audit**."* For ISO 14001 this is the line between auditing clause 9.1.2 (does the *process* for evaluating compliance work?) and acting as a regulator (are you *actually* compliant with every permit condition?).

**7.2.3.3 Discipline and sector-specific competence**
"Audit teams should have the **collective** discipline and sector-specific competence appropriate for auditing the particular types of management systems and sectors." It includes:
- **a)** management system requirements and principles, and their application;
- **b)** fundamentals of the discipline(s) and sector(s) related to the management system standards as applied by the auditee;
- **c)** application of discipline- and sector-specific methods, techniques, processes and practices "to enable the audit team to assess conformity within the defined audit scope and generate appropriate audit findings and conclusions";
- **d)** principles, methods and techniques relevant to the discipline and sector, "such that the auditor can determine and evaluate the **risks and opportunities** associated with the audit objectives."

> **What this means concretely for an ISO 14001 (environmental) internal auditor.** ISO 19011:2018 dropped the 2011 edition's discipline-specific annex, so the environmental content must be derived from ISO 14001:2015 itself. The environmental discipline competence an EMS internal auditor needs:
> - **Environmental aspects and impacts** — how aspects are identified across activities, products and services; normal / abnormal / emergency conditions; the **life cycle perspective** (see A.11 below); significance determination methodology and its consistency (14001 cl. 6.1.2).
> - **Compliance obligations** — how legal and other requirements are identified, accessed, kept current and applied; permits, licences, consents and their conditions; the process for **evaluation of compliance** (14001 cl. 6.1.3 and 9.1.2). *In the Singapore context: the Environmental Protection and Management Act (EPMA) and its regulations, the Environmental Public Health Act, NEA licensing and toxic industrial waste (TIW) collector licensing, trade effluent discharge to public sewers under PUB's Sewerage and Drainage Act, the Energy Conservation Act for registered corporations, and the Resource Sustainability Act reporting duties.*
> - **Environmental terminology and measurement** — emissions, effluent, trade effluent, discharge consents, waste classification and hazardous/toxic industrial waste, scheduled waste manifests/tracking, chemical storage and secondary containment (bunding), noise, odour, contaminated land, energy and water consumption, GHG accounting basics.
> - **Operational control and emergency preparedness** — controls proportionate to significance; the hierarchy of controls; spill response, containment and drills (14001 cl. 8.1, 8.2).
> - **Monitoring and measurement** — what is monitored, methods, calibration of monitoring equipment, and the evaluation of environmental performance and KPIs (14001 cl. 9.1.1).
> - **Technology and practice** — pollution control equipment (scrubbers, oil-water separators, wastewater treatment), waste segregation and licensed disposal chains, and the environmental risks typical of the auditee's sector.

**A.11 Life cycle** (Annex A, of direct EMS relevance): "Auditors should **not** consider this as a requirement to adopt a life cycle *approach*. A life cycle **perspective** involves consideration of the control and influence the organization has over the stages of its product and service life cycle." Stages listed: **acquisition of raw materials, design, production, transportation/delivery, use, end of life treatment and final disposal.** The auditor should use professional judgement as to how the organization has applied a life cycle perspective in terms of its strategy and: (a) life of the product or service; (b) organization's influence on the supply chain; (c) length of the supply chain; (d) technological complexity of the product.

**A.7 Auditing compliance within a management system** — the team should consider whether the auditee has effective processes for: (a) identifying its statutory/regulatory and other requirements it is committed to; (b) managing its activities, products and services to achieve compliance; (c) **evaluating its compliance status**. Also consider whether the auditee (1) has an effective process for identifying **changes** in compliance requirements and considering them as part of management of change; (2) has **competent individuals** to manage its compliance processes.

**7.2.3.4 Generic competence of the audit team leader** — able to: (a) plan the audit and assign tasks per individual competence; (b) **discuss strategic issues with top management** to determine whether they considered these when evaluating risks and opportunities; (c) develop and maintain a collaborative working relationship among team members; (d) manage the audit process — effective use of resources, managing uncertainty of achieving objectives, **protecting the health and safety of the audit team**, directing team members, **providing direction and guidance to auditors-in-training**, preventing and resolving conflicts and problems including within the team; (e) represent the team in communications with the programme manager, audit client and auditee; (f) lead the team to reach the audit conclusions; (g) prepare and complete the audit report.

**7.2.3.5 Multiple disciplines** — team members should understand "the interactions and synergy between the different management systems"; team leaders should understand the requirements of each standard being audited **and recognize the limits of their competence in each discipline**.

### 7.2.4 Achieving auditor competence
A combination of: (a) successfully completing training programmes covering generic auditor knowledge and skills; (b) experience in a relevant technical, managerial or professional position involving judgement, decision making, problem solving and communication; (c) education/training and experience in a specific discipline and sector; (d) **audit experience acquired under the supervision of an auditor competent in the same discipline**.

**7.2.5 Audit team leader competence** — additional audit experience "gained by working under the direction and guidance of a **different** audit team leader."

### 7.3 Establishing auditor evaluation criteria
Criteria should be both **qualitative** (demonstrated behaviour, knowledge, or performance of skills, in training or the workplace) and **quantitative** (years of work experience and education, number of audits conducted, hours of audit training).

### 7.4 Selecting the evaluation method — Table 2
**"The evaluation should be conducted using two or more of the methods"**; methods "may differ in their reliability"; a combination "should be used to ensure an outcome that is objective, consistent, fair and reliable."

| Method | Objective | Examples |
|---|---|---|
| **Review of records** | Verify the background of the auditor | Analysis of records of education, training, employment, professional credentials and auditing experience |
| **Feedback** | Provide information about how the auditor's performance is perceived | Surveys, questionnaires, personal references, testimonials, complaints, performance evaluation, peer review |
| **Interview** | Evaluate desired professional behaviour and communication skills, verify information, test knowledge, acquire additional information | Personal interviews |
| **Observation** | Evaluate desired professional behaviour and the ability to apply knowledge and skills | Role playing, **witnessed audits**, on-the-job performance |
| **Testing** | Evaluate desired behaviour, knowledge and skills and their application | Oral and written exams, psychometric testing |
| **Post-audit review** | Provide information on auditor performance during audit activities; identify strengths and opportunities for improvement | Review of the audit report, interviews with the team leader and team, and if appropriate feedback from the auditee |

### 7.5 Conducting the evaluation
Information collected is compared against the criteria in 7.2.3. **"When an auditor under evaluation... does not fulfil the criteria, then additional training, work or audit experience should be undertaken and a subsequent re-evaluation should be performed."**

### 7.6 Maintaining and improving auditor competence
- Auditors maintain competence "through **regular participation in management system audits** and **continual professional development**" — achieved through additional work experience, training, private study, coaching, attendance at meetings, seminars and conferences.
- The programme manager "should establish suitable mechanisms for the **continual evaluation of the performance** of the auditors and audit team leaders."
- CPD activities should take account of: (a) changes in the needs of the individual and the organization; (b) **developments in the practice of auditing including the use of technology**; (c) relevant standards, guidance/supporting documents and other requirements; (d) changes in sector or disciplines.

---

## 5. Audit evidence

### 5.1 Definition and the test of "objective"
- **Audit evidence** (3.9): "records, statements of fact or other information, which are relevant to the audit criteria and **verifiable**."
- **Objective evidence** (3.8): "data supporting the existence or verity of something" — obtained "through observation, measurement, test or by other means."

**What makes evidence "objective":**
1. **Verifiable** — someone else could go back and find the same thing.
2. **Relevant to the audit criteria** — it speaks to a specific requirement.
3. **Factual, not inferred** — what was seen/read/said, not what the auditor concluded about a person.
4. **Specific and traceable** — identified by document number, revision, date, equipment tag, batch/manifest number, location, or role.

| **Is objective evidence** | **Is NOT objective evidence** |
|---|---|
| "Waste manifest No. WM-2024-0871 dated 12 Mar 2024" | "The waste paperwork looked messy" |
| "Calibration certificate for pH meter TAG-PH-03, last calibrated 14 Jan 2023, sticker states next due 14 Jan 2024" | "The meter is probably out of calibration" |
| "Drum storage area B: three 200 L drums of waste solvent stood outside the bunded area" | "Chemical storage is generally poor" |
| "Operator at Line 2 stated he had not been shown the spill response procedure" | "Staff don't seem to care about the environment" |
| "Aspects register EMS-REG-02 Rev 3 dated 2021 does not include the new solvent recovery still commissioned Aug 2023" | "The aspects register is out of date" *(no evidence of how you know)* |

### 5.2 The four sources of evidence
From 6.4.7 ("interviews; observations; review of documented information") and expanded in **A.14 Selecting sources of information**:

| # | Source | What it gives you | Cautions |
|---|---|---|---|
| **1** | **Interview** — "interviews with employees and other individuals" | What people actually do; awareness and understanding; how the process really runs vs. how it is written | Weakest form alone; must be corroborated. A statement is evidence *of what was said*, not proof of the fact. Never attribute by name in a finding. |
| **2** | **Observation** — "observations of activities and the surrounding work environment and conditions" | Reality on the ground: bunding, labelling, segregation, PPE, housekeeping, actual practice at the point of work | Only a snapshot in time; record location, date, time. Do **not** touch or operate equipment (A.15). |
| **3** | **Documents** — "policies, objectives, plans, procedures, standards, instructions, **licences and permits**, specifications, drawings, contracts and orders" | The criteria and the planned arrangements — what *should* happen | Check revision status and control. A document proves intent, not implementation. |
| **4** | **Records** — "inspection records, minutes of meetings, audit reports, **records of monitoring programme and the results of measurements**" | Proof that the planned arrangement actually happened | The primary evidence of implementation. Look for completeness, authorisation, and dates. |

*A.14 also lists:* (e) **data summaries, analyses and performance indicators**; (f) information on the auditee's sampling plans and procedures for control of sampling and measurement processes; (g) reports from other sources — customer feedback, external surveys and measurements, external provider ratings; (h) **databases and websites**; (i) **simulation and modelling**.

> **Teaching device — triangulation.** Strongest findings rest on **two or more** sources: the procedure says X (document), the operator says Y (interview), the record shows Z (record), and you saw W (observation). Where they diverge, you have found something.

### 5.3 Sufficient and appropriate evidence
ISO 19011 requires the auditor to "**confirm the sufficiency and appropriateness of audit evidence** to support audit findings and conclusions" (7.2.3.2 a) and to consider "accuracy, sufficiency and appropriateness of objective evidence" (A.18.1 c).

- **Sufficient** = *quantity*. Enough of it. One record out of 200 is a data point; five out of five sampled failing the same way is a pattern.
- **Appropriate** = *quality / relevance / reliability*. It actually addresses the requirement, and comes from a reliable source.

**Reliability hierarchy taught in practice** (strongest → weakest): the auditor's own observation and measurement → original records and permits held by the organization → externally-generated documents (regulator correspondence, licensed disposal contractor's receipts, third-party lab reports) → internally generated documents → verbal statements → hearsay ("the previous manager used to...").

**A.5 Verifying information** — the four C's. Consider whether information is:
- **a) complete** — all expected content is contained in the documented information;
- **b) correct** — the content conforms to other reliable sources such as standards and regulations;
- **c) consistent** — consistent in itself and with related documents;
- **d) current** — the content is up to date.

Also: "If information is provided in a manner other than expected (e.g. by different individuals, alternate media), **the integrity of the evidence should be assessed**." And take specific care over data-protection regulations for information outside the audit scope but contained in the same document.

### 5.4 Sampling (A.6)
**A.6.1 General.** "Audit sampling takes place when it is not practical or cost effective to examine all available information... the process of selecting **less than 100 %** of the items within the total available data set (population) to obtain and evaluate evidence about some characteristic of that population, in order to form a conclusion concerning the population."

**The sampling risk, verbatim:** *"The risk associated with sampling is that the samples may not be representative of the population from which they are selected. Thus, the auditor's conclusion may be biased and be different from that which would be reached if the whole population was examined."*

**The six steps of audit sampling:**
1. establishing the objectives of sampling;
2. selecting the extent and composition of the population to be sampled;
3. selecting a sampling method;
4. determining the sample size to be taken;
5. conducting the sampling activity;
6. compiling, evaluating, reporting and documenting results.

"When sampling, consideration should be given to the **quality of the available data**, as sampling insufficient and inaccurate data will not provide a useful result." Reporting on the sample "could take into account the sample size, selection method and estimates made based on the sample and the confidence level."

**A.6.2 Judgement-based sampling** — "relies on the competence and experience of the audit team." Consider:
- **a)** previous audit experience within the audit scope;
- **b)** complexity of requirements (including statutory and regulatory) to achieve the audit objectives;
- **c)** complexity and interaction of the organization's processes and management system elements;
- **d)** degree of change in technology, human factor or management system;
- **e)** previously identified significant risks and opportunities for improvement;
- **f)** output from monitoring of management systems.

> **Drawback, verbatim:** *"there can be no statistical estimate of the effect of uncertainty in the findings of the audit and the conclusions reached."*
> **This is what internal EMS auditors use in practice** — you deliberately weight the sample toward significant aspects, recent changes, previous NC areas and high-risk operations. That is the risk-based principle in action.

**A.6.3 Statistical sampling** — "uses a sample selection process based on probability theory."
- **Attribute-based** sampling: only two possible outcomes per sample (correct/incorrect, pass/fail) — e.g. "evaluating conformity of completed forms to the requirements set out in a procedure."
- **Variable-based** sampling: outcomes occur in a continuous range — e.g. "examining the occurrence of food safety incidents or the number of security breaches." *(EMS analogue: effluent pH values, monthly waste tonnages, kWh consumption.)*

*Elements affecting the sampling plan:* (a) the context, size, nature and complexity of the organization; (b) the number of competent auditors; (c) the frequency of audits; (d) the time of individual audit; (e) any externally required confidence level; (f) the occurrence of undesirable and/or unexpected events.

**Sampling risk / confidence level, verbatim:** *"a sampling risk of 5 % corresponds to an acceptable confidence level of 95 %. A sampling risk of 5 % means the auditor is willing to accept the risk that 5 out of 100 (or 1 in 20) of the samples examined will not reflect the actual values that would be seen if the entire population was examined."*

When statistical sampling is used, document: the population intended to be sampled, the sampling criteria used for evaluation (what is an acceptable sample), the statistical parameters and methods used, the number of samples evaluated, and the results obtained.

### 5.5 Traceability and the audit trail
ISO 19011 requires auditors to "**audit a process from start to finish, including the interrelations with other processes and different functions**" (7.2.3.2 a) — this is the audit trail.

**The two directions:**
- **Forward tracing (input → output)**, "tracking": start at the cause and follow through. *EMS example:* start at the aspects register entry "waste solvent generation" → follow to the significance rating → to the operational control (SOP) → to the training records of the operators → to the storage arrangements on the floor → to the manifest → to the licensed disposal contractor's receipt → to the monthly waste KPI → to management review.
- **Backward tracing (output → input)**, "tracing back": start at a record and work back to the requirement. *EMS example:* pick a disposal receipt from last quarter → back to its manifest → back to the waste stream that generated it → back to whether that stream appears in the aspects register and the licence conditions.

**Practical rules for a defensible trail:**
- Record the **unique identifier** of every item you sample at the moment you see it — document number *and revision*, record number, date, equipment tag, drum/container label, area, name of the role (not the person).
- Record what you sampled **and what you did not** — the population and the sample size — so the report's sampling caveat is honest.
- A finding must be **re-findable**: another auditor should be able to take your note and put their hand on the same evidence.
- Pick up the trail where the process crosses a **boundary** between departments — that is where EMS systems most often fail (e.g. production generates a new waste stream but never tells the EHS team, so the aspects register and the licence are never updated).

---

## 6. Questioning technique

ISO 19011 **A.17 Conducting interviews** gives the frame; the technique below is standard auditor-training practice built on it.

### 6.1 What the standard says (A.17)
Interviews "are an important means of collecting information and should be carried out in a manner adapted to the situation and the individual interviewed." The auditor should consider:
- **a)** interviews should be held with individuals from **appropriate levels and functions** performing activities/tasks within the audit scope;
- **b)** interviews "should normally be conducted **during normal working hours** and, where practical, **at the normal workplace** of the individual";
- **c)** "attempts should be made to **put the individual being interviewed at ease** prior to and during the interview";
- **d)** "the **reason for the interview and any note taking should be explained**";
- **e)** "interviews may be initiated by **asking individuals to describe their work**";
- **f)** "the **type of question used should be carefully selected** (e.g. open, closed, leading questions, appreciative inquiry)";
- **g)** awareness of limited non-verbal communication in virtual settings — "instead focus should be on the type of questions to use in finding objective evidence";
- **h)** "the results from the interview should be **summarized and reviewed with the interviewed individual**";
- **i)** "the interviewed individuals should be **thanked** for their participation and cooperation."

### 6.2 Question types

| Type | Form | Use it to | Example (EMS) | Risk |
|---|---|---|---|---|
| **Open** | Who / what / where / when / why / how; "Tell me about…", "Describe…", "Walk me through…" | Open a topic, get the person talking, discover what you didn't know to ask | *"Walk me through what happens to the waste solvent from the moment it comes off the line."* | Can wander; costs time |
| **Closed** | Answerable yes/no or with one fact | **Confirm** a specific fact, pin down a detail, close a line of enquiry | *"Is that drum logged in the waste register?"* | Yields no new information; a string of them feels like an interrogation |
| **Probing** | Follow-up that digs into the previous answer: "What happens then?", "How do you know?", "What if…?", "Who decides?" | Push past the rehearsed answer to the real practice; test depth of understanding | *"You said you'd call the EHS manager — how would you reach him at 2 a.m. on a Sunday?"* | None if done neutrally; becomes badgering if repeated aggressively |
| **Clarifying** | "When you say 'regularly', how often is that?" | Remove ambiguity before you write anything down | *"You said the bund is 'checked' — checked by whom, and is it recorded?"* | — |
| **Leading** ⚠️ | Contains the answer: "You do calibrate that meter, don't you?" | **AVOID** — contaminates the evidence | *(bad)* *"So you segregate the hazardous waste, right?"* | Answer is worthless as evidence; breaches fair presentation |
| **Multiple / compound** ⚠️ | Two or three questions at once | **AVOID** — you'll only get the last one answered | *(bad)* *"Do you have a procedure and were you trained and when was it revised?"* | Confuses the interviewee and the record |
| **Appreciative inquiry** | "What works well here?", "What are you most proud of in how you handle this?" | Named in A.17(f); opens defensive interviewees and surfaces good practice worth recording | *"What's the one improvement to waste handling you'd make if it were up to you?"* | — |

### 6.3 The funnel technique
Structure every line of enquiry as a funnel — wide at the top, narrow at the bottom:

```
     OPEN        "Tell me about how you handle waste solvent here."
       │          → let them talk, don't interrupt, note the threads
       ▼
    PROBING      "You mentioned a transfer log — how does that get filled in?"
       │          → follow the threads that touch the audit criteria
       ▼
   CLARIFYING    "When you say the drums are 'checked daily' — by whom?"
       │
       ▼
     CLOSED      "Is that check recorded on the same log?"
       │
       ▼
    VERIFY       "Could you show me the log for last week?"   ← evidence
```
**Rule of thumb:** roughly 70 % open/probing, 30 % closed. A funnel that starts closed ("Do you have a procedure?") gets a "yes" and teaches you nothing.

**Inverted funnel** (narrow → wide) is used deliberately with a nervous or junior interviewee: start with two or three easy closed factual questions to build confidence, then widen out.

### 6.4 5W1H
The systematic question set that guarantees no dimension of a process is missed. Apply it to every process you audit:

| | Question | EMS application |
|---|---|---|
| **What** | What is done? What could go wrong? What is the requirement? | *What environmental aspects arise from this activity?* |
| **Why** | Why is it done this way? Why this control? | *Why was this aspect rated significant / not significant?* |
| **Who** | Who does it? Who is competent/authorised? Who approves? | *Who is authorised to sign the waste manifest?* |
| **Where** | Where is it done? Where is it recorded/stored? | *Where is the spill kit, and where is the nearest drain?* |
| **When** | When is it done? How often? When was it last done/reviewed? | *When was the emergency drill last performed?* |
| **How** | How is it done? How is it controlled, measured, verified? How do you know it works? | *How do you verify the disposal contractor is licensed?* |

**Two extensions worth teaching:** **"How much / how many"** (quantifies — tonnage, ppm, frequency, cost) and **"What if"** (tests abnormal and emergency conditions — required by ISO 14001 cl. 6.1.2 and 8.2: *"What if the pump fails at 3 a.m.?"*).

### 6.5 "Show me / prove it"
The single most important move in the whole craft: **convert every verbal claim into verifiable evidence.**

- **"Show me."** *"You've explained the process — please show me where that's recorded."* / *"Show me the last three manifests."* / *"Can you show me on the shop floor how you'd do that?"*
- **"How do you know?"** Turns an assertion into a source. *"How do you know the disposal contractor's licence is still valid?"*
- **"Prove it to me."** Used lightly and with a smile, never as a challenge — the framing is *"help me record the evidence"*, not *"I don't believe you."*
- **Demonstration.** For competence and emergency preparedness, ask the person to *show* rather than *tell*: *"If that drum split right now, talk me through and show me what you'd do first."*

> The rule: **an interview answer alone is rarely enough to close a line of enquiry.** Either you saw it, or there is a record of it, or you have not verified it.

### 6.6 PLOD — Person, Location, Object, Document
A memory aid for **capturing the traceable identity of evidence at the moment you find it**, so a finding can be re-found and re-verified later.

| Letter | Capture | EMS example |
|---|---|---|
| **P — Person** | The **role/function** interviewed (never the individual's name in the finding) | "the Warehouse Supervisor" |
| **L — Location** | Where — building, area, line, tank, virtual location | "Chemical Store B, external yard" |
| **O — Object** | The physical thing — equipment tag, drum, container, meter, sign, bund | "three 200 L drums labelled 'waste thinner', drum IDs WD-104/105/106" |
| **D — Document** | Document or record identity **and revision/date** | "Waste Management Procedure EMS-P-08 Rev 4, cl. 5.3; Waste Transfer Log WTL-03 for week ending 08 Mar 2024" |

Used as a note-taking discipline: every observation you write in your working papers should carry as many of P, L, O, D as apply. If your note has none of them, you have an impression, not evidence.

### 6.7 What NOT to do

**In questioning:**
- ❌ **Leading questions** — "You do check that daily, don't you?" Supplies the answer, destroys the evidence.
- ❌ **Compound questions** — three questions in one breath.
- ❌ **Interrogating** — rapid-fire closed questions, no pauses, no eye contact.
- ❌ **Talking more than the auditee** — the auditor should be listening, not lecturing. Target: auditor talks < 30 % of the time.
- ❌ **Filling the silence** — after a question, wait. The pause does the work.
- ❌ **Trick or "gotcha" questions** — asking something you know they can't answer to manufacture a finding.
- ❌ **Consulting mid-audit** — "What you should do is buy a new bund." Advising breaches independence and makes you the author of what you will audit next year. Note the gap; let the auditee design the fix.
- ❌ **Auditing the person, not the process** — "Why didn't *you* fill this in?" Reframe: *"What makes it hard to complete this log at shift change?"*
- ❌ **Arguing or debating** — the auditor collects evidence; disagreements about *conclusions* go to the closing meeting, and if unresolved, into the report.
- ❌ **Jargon and clause-quoting at the shop floor** — "Does this satisfy 8.1?" means nothing to a forklift driver. Ask about the work.
- ❌ **Naming individuals in findings** — findings address the system; naming invites blame and kills cooperation for the next audit.
- ❌ **Asking questions outside the audit scope** — note the concern, pass it to the team leader (6.4.4).
- ❌ **Accepting "we always do it that way"** — that is an assertion. Show me.
- ❌ **Interviewing only managers** — the manager describes the procedure; the operator reveals the practice. Interview "individuals from appropriate levels and functions" (A.17 a).

**On site (A.15) — hard rules:**
- ❌ **"Do not touch or manipulate any equipment, unless explicitly permitted, even when competent or licensed."**
- ❌ Do not photograph, screenshot or copy documents without asking permission **in advance**.
- ❌ "When taking notes, **avoid collecting personal information** unless required by the audit objectives or criteria."
- ✅ Avoid unnecessary disturbance of operational processes; use PPE properly; know the emergency procedures (exits, assembly points).

---

## 7. Nonconformity statements

### 7.1 The three-part structure
Straight from **A.18.3 Recording nonconformities**: "(a) description of or reference to **audit criteria**; (b) **audit evidence**; (c) **declaration of nonconformity**."

| Part | What it is | The question it answers | Common name |
|---|---|---|---|
| **1. Requirement** | The specific criterion — standard clause, procedure + revision + section, permit condition, or legal requirement | *What SHOULD be?* | "The Requirement" |
| **2. Evidence** | The specific, verifiable objective evidence found — PLOD detail | *What WAS found?* | "The Evidence" |
| **3. Statement of nonconformity** | The declared gap between the two | *WHY is it a nonconformity?* | "The Declaration" |

**Template:**
> **Requirement:** *[Standard/procedure/permit] clause [X] requires that "[quote or accurately paraphrase the requirement]".*
> **Evidence:** *[Specific evidence with PLOD detail — what, where, which document/record, which revision, which date, how many of how many sampled].*
> **Nonconformity:** *[The requirement] was not met, in that [the concise statement of the gap].*

**The tests every NC statement must pass:**
1. **Factual** — the content cannot be disputed.
2. **Specific and traceable** — someone else can find the same evidence.
3. **Against a stated requirement** — no requirement, no nonconformity (it's an OFI at best).
4. **Self-standing** — readable and understandable in six months by someone who wasn't there.
5. **Free of solutions** — states the gap, not the fix. The auditee owns the corrective action.
6. **Free of blame** — describes the system failure, not the person.
7. **Free of opinion words** — no "inadequate", "poor", "insufficient", "weak" without objective definition.

### 7.2 Grading: major, minor, OFI

> ISO 19011 (6.4.8) only says nonconformities "**can** be graded... quantitative (e.g. 1 to 5) and qualitative (e.g. minor, major)". The criteria below are the widely-used ISO/IEC 17021-1 / certification-body convention. **Each organization must define its own grading rules in its internal audit procedure and apply them consistently.**

| Grade | Criteria | ISO 14001 examples |
|---|---|---|
| **MAJOR** | Any one of: <br>• **Total absence** of a required process, control or documented information <br>• A **systemic breakdown** — the failure is widespread or repeated, not isolated <br>• A failure that **affects the capability of the EMS to achieve its intended outcomes** <br>• A **significant doubt** that effective control is in place <br>• An **actual or imminent significant environmental impact**, or a **breach of a compliance obligation / legal non-compliance** <br>• **Several minors against the same requirement**, together demonstrating a systemic failure <br>• A **repeat** of a previously-raised minor whose corrective action failed | No process at all for identifying compliance obligations (cl. 6.1.3); discharge exceeding permit limits with no action taken; no emergency preparedness arrangements for a site handling bulk chemicals (cl. 8.2); management review not conducted for two years (cl. 9.3) |
| **MINOR** | • A **single, isolated lapse** in an otherwise implemented and effective process <br>• Does **not** affect the capability of the EMS to achieve intended outcomes <br>• A **system weakness** that could grow into a major if left unaddressed <br>• Typically an administrative or record-keeping failure with no environmental consequence | One of twelve sampled waste manifests missing the receiving signature; one operator of eight sampled not yet retrained after a procedure revision; a single monitoring reading recorded a day late |
| **OFI** (Opportunity for Improvement) | • **No requirement is breached** — the system conforms <br>• A suggestion to make a conforming process more effective, efficient or robust <br>• **Not binding** — the auditee may decline it, and declining it is not a finding <br>• Must **never** be used to soften a real nonconformity | The aspects register meets cl. 6.1.2 but could be strengthened by adding a quantitative scoring scale; spill kits are provided and adequate but are not colour-coded by area; environmental KPIs are reported monthly but not trended graphically for management review |

**Two grading traps to teach explicitly:**
1. **The "minor because they're nice people" trap.** Grading is driven by the evidence and the risk, not by the auditee's reaction. (Principle: fair presentation; behaviour: fortitude.)
2. **The OFI dumping-ground trap.** Auditors who dislike confrontation record real nonconformities as OFIs. Since OFIs are non-binding, the failure is never corrected and reappears in the certification audit as a major. **If a requirement is not met, it is a nonconformity — full stop.**

Also note **ISO 19011 Note 2 to 6.4.8**: where the criteria are statutory or regulatory, the correct words are **compliance / non-compliance**, not conformity/nonconformity.

### 7.3 Worked examples — well-written vs badly-written (ISO 14001 contexts)

---

**Example 1 — Waste manifests (ISO 14001 cl. 8.1 / compliance obligations)**

❌ **BADLY WRITTEN**
> *"Waste management is poor. The manifests are not being controlled properly and staff need more training."*

*What's wrong:* No requirement cited. No evidence — nothing traceable. "Poor" and "properly" are opinions. Contains a proposed solution ("need more training") — that's the auditee's job and it pre-empts root cause analysis. Not re-findable.

✅ **WELL WRITTEN**
> **Requirement:** Waste Management Procedure EMS-P-08 Rev 4, section 5.3 requires that each toxic industrial waste consignment be recorded on a waste manifest signed by both the despatching Store Supervisor and the licensed collector's driver, and that the completed manifest be filed within 3 working days of collection.
> **Evidence:** Of twelve manifests sampled from the TIW manifest file for the period 01 Jan – 31 Mar 2024, four (Nos. WM-2024-0812, 0834, 0851 and 0866) carried no collector's driver signature. Manifest WM-2024-0871, for a collection on 12 Mar 2024, had not been filed at the time of the audit on 09 Apr 2024.
> **Nonconformity:** The requirement of EMS-P-08 Rev 4 section 5.3 was not met, in that waste manifests were not consistently signed by the collector and were not filed within the specified 3 working days.
>
> *Grade: **Minor** — the manifest process exists and is largely followed; the failures are record-keeping lapses in 4 of 12 sampled with no evidence of waste going to an unlicensed route.*
> *(Grade would escalate to **Major** if the manifests were absent entirely, or if evidence showed waste had gone to an unlicensed disposer — a breach of a compliance obligation.)*

---

**Example 2 — Environmental aspects register (ISO 14001 cl. 6.1.2)**

❌ **BADLY WRITTEN**
> *"The aspects register is out of date and doesn't seem to cover everything. Mr Tan in Production wasn't aware of it either."*

*What's wrong:* Names an individual. "Doesn't seem to" is speculation. No clause reference. No specifics — which aspects, which register, which revision. "Out of date" against what requirement?

✅ **WELL WRITTEN**
> **Requirement:** ISO 14001:2015 clause 6.1.2 requires the organization to determine the environmental aspects of its activities, products and services that it can control and those it can influence, and their associated environmental impacts, considering a life cycle perspective, taking into account **change, including planned or new developments**. EMS Procedure EMS-P-03 Rev 2 section 4.1 further requires the Environmental Aspects Register to be reviewed and updated within 30 days of the introduction of any new process or equipment.
> **Evidence:** The Environmental Aspects and Impacts Register (EMS-REG-02 Rev 3, dated 15 Feb 2021) does not include the solvent recovery still installed in Building C, which the Production Manager confirmed was commissioned in August 2023 and which was observed operating during the audit on 09 Apr 2024. Neither the associated VOC emissions nor the still-bottoms waste stream appear in the register. No record of a register review following the commissioning was available.
> **Nonconformity:** ISO 14001:2015 cl. 6.1.2 and EMS-P-03 Rev 2 section 4.1 were not met, in that the environmental aspects arising from a new process introduced approximately 8 months prior to the audit have not been determined and added to the aspects register.
>
> *Grade: **Major** — a significant new emission source and waste stream sit entirely outside the aspects determination process. Because significance ratings drive operational controls, monitoring and compliance obligations, the omission undermines the EMS's capability to achieve its intended outcomes and may carry a permitting exposure.*

---

**Example 3 — Chemical storage / operational control (ISO 14001 cl. 8.1)**

❌ **BADLY WRITTEN**
> *"Some drums were seen outside the bund in the yard. This is unacceptable and could cause pollution. The site should install a larger bunded area."*

*What's wrong:* No requirement cited. "Some" — how many? Where exactly? Which drums? "Unacceptable" is opinion; "could cause pollution" is speculation. **Prescribes the solution** ("should install a larger bunded area") — the auditor has become a consultant and has foreclosed root cause analysis (maybe the real cause is a delivery scheduling failure, not bund capacity).

✅ **WELL WRITTEN**
> **Requirement:** Chemical Storage and Handling Procedure EMS-P-11 Rev 2, section 6.2 requires that all containers of liquid chemicals and liquid wastes be stored within secondary containment (bunding) with a capacity of at least 110 % of the largest container stored.
> **Evidence:** During the site tour on 09 Apr 2024 at approximately 11:15, three 200 L drums labelled "Waste Thinner" (drum IDs WD-104, WD-105, WD-106) were observed standing on unsealed ground in the external yard adjacent to Chemical Store B, outside any secondary containment, approximately 4 m from an open surface-water drain. The Store Supervisor stated that the drums had been placed there "two or three days ago" because the bunded area was full.
> **Nonconformity:** EMS-P-11 Rev 2 section 6.2 was not met, in that liquid waste containers were stored outside secondary containment.
>
> *Grade: **Major** — liquid waste is stored uncontained adjacent to an open surface-water drain, presenting an immediate risk of an uncontrolled release to the environment and a potential breach of discharge compliance obligations.*
> *Note under 6.4.4, this evidence "suggests an immediate and significant risk" and should be reported to the auditee without delay rather than held to the closing meeting.*

---

**Example 4 — Competence and awareness (ISO 14001 cl. 7.2 / 7.3)**

❌ **BADLY WRITTEN**
> *"Training records are inadequate. Staff are not competent."*

*What's wrong:* Both sentences are conclusions with no evidence and no requirement. "Inadequate" and "not competent" are judgements about people. Nothing traceable. And it over-reaches — a records gap is not proof of incompetence.

✅ **WELL WRITTEN**
> **Requirement:** ISO 14001:2015 clause 7.2 requires the organization to determine the necessary competence of persons doing work under its control that affects its environmental performance and its ability to fulfil compliance obligations, to ensure these persons are competent on the basis of appropriate education, training or experience, and to **retain appropriate documented information as evidence of competence**.
> **Evidence:** The EMS Training Matrix EMS-F-22 identifies "Spill Response — Chemical Store" as a required competence for all Chemical Store operators. Of the five Chemical Store operators listed on the current shift roster, training records were available for three. No records of spill response training were available for the two operators engaged through Wanjia Manpower Services on 04 Jan 2024. When asked to describe the first action on discovering a solvent spill, one of these two operators stated he "would go and find the supervisor" and was unable to locate the spill kit, which was observed to be stored in Chemical Store B.
> **Nonconformity:** ISO 14001:2015 cl. 7.2 was not met, in that documented information evidencing the required spill response competence was not retained for two of five Chemical Store operators, and the demonstrated response was not in accordance with the Spill Response Procedure EMS-P-14 Rev 1 section 3.
>
> *Grade: **Major** — the competence gap affects the site's emergency response capability for a significant aspect. (Had records simply been missing for one operator who nevertheless demonstrated correct response, **Minor** would be appropriate.)*

---

**Example 5 — Evaluation of compliance (ISO 14001 cl. 9.1.2)**

❌ **BADLY WRITTEN**
> *"Legal compliance evaluation is overdue. This has been raised before and nothing has been done about it. Management doesn't take this seriously."*

*What's wrong:* No requirement cited, no evidence of *what* is overdue or by how long. "Nothing has been done" is unsupported. **"Management doesn't take this seriously"** is an accusation about attitude, not a statement about the system — it is unverifiable, inflammatory, and will guarantee the finding is fought rather than fixed.

✅ **WELL WRITTEN**
> **Requirement:** ISO 14001:2015 clause 9.1.2 requires the organization to establish, implement and maintain the processes needed to evaluate fulfilment of its compliance obligations, to determine the frequency of the evaluation, and to **retain documented information as evidence of the compliance evaluation result(s)**. Compliance Evaluation Procedure EMS-P-06 Rev 1 section 4 specifies a **six-monthly** evaluation against the Register of Compliance Obligations.
> **Evidence:** The most recent completed Compliance Evaluation Record (EMS-F-09) on file is dated 30 June 2023. No evaluation record was available for the period July – December 2023 or for the period ending March 2024. The Register of Compliance Obligations EMS-REG-01 Rev 5 lists 23 obligations; the EHS Manager confirmed no evaluation had been carried out since June 2023. Internal audit report IA-2023-04 dated 12 Oct 2023 raised the same issue (finding NC-2023-11), which was closed on 20 Nov 2023 on the basis of a diary reminder being set.
> **Nonconformity:** ISO 14001:2015 cl. 9.1.2 and EMS-P-06 Rev 1 section 4 were not met, in that the compliance evaluation has not been performed at the specified six-monthly frequency, with no evaluation carried out in the nine months preceding the audit, and the corrective action taken against the previous nonconformity NC-2023-11 has not been effective.
>
> *Grade: **Major** — the organization has no current knowledge of its compliance status against 23 obligations, and this is a **repeat** finding whose corrective action failed, evidencing a systemic breakdown rather than an isolated lapse.*

---

**Example 6 — Monitoring equipment (ISO 14001 cl. 9.1.1) — a *minor*, and a matching *OFI***

❌ **BADLY WRITTEN**
> *"Calibration of monitoring equipment needs improvement — one meter was found overdue and this is a major nonconformity as it affects all the data."*

*What's wrong:* Vague requirement ("needs improvement"). The **grading is asserted and over-stated** — a single overdue instrument in an otherwise-working calibration system is an isolated lapse, and "affects all the data" is unsupported speculation about consequence. Grade first from evidence, not from alarm.

✅ **WELL WRITTEN (Minor NC)**
> **Requirement:** ISO 14001:2015 clause 9.1.1 requires that the organization ensure that **calibrated or verified monitoring and measurement equipment is used and maintained** as appropriate. Monitoring & Measurement Procedure EMS-P-09 Rev 3 section 5.1 requires all equipment on the Calibration Schedule EMS-F-17 to be calibrated annually and to carry a current calibration status label.
> **Evidence:** The Calibration Schedule EMS-F-17 lists six items of environmental monitoring equipment. Five held current calibration certificates. The portable pH meter (asset tag TAG-PH-03), used for the weekly trade effluent checks required by the trade effluent discharge licence, carried a label stating "Calibration due: 14 Jan 2024" and no calibration certificate later than 14 Jan 2023 was available. The Effluent Monitoring Log EMS-F-19 shows the meter was used for weekly readings on 12 occasions between 14 Jan 2024 and the audit date.
> **Nonconformity:** ISO 14001:2015 cl. 9.1.1 and EMS-P-09 Rev 3 section 5.1 were not met, in that one of six items of monitoring equipment was used beyond its specified calibration due date.
>
> *Grade: **Minor** — an isolated lapse in an otherwise-implemented calibration system (5 of 6 conforming). Note that the auditee's corrective action should include evaluating the validity of the 12 affected readings.*

✅ **WELL WRITTEN (OFI — same area, no requirement breached)**
> **Opportunity for Improvement:** The Calibration Schedule EMS-F-17 is maintained as a standalone spreadsheet and calibration due dates are tracked manually by the EHS Executive. The organization may wish to consider adding automated advance-notice reminders (e.g. 30 days before due date) or incorporating environmental monitoring equipment into the existing plant maintenance system, to reduce the likelihood of instruments passing their due date unnoticed.
> *No requirement of ISO 14001:2015 or of EMS-P-09 is breached by the current arrangement. This suggestion is not binding on the auditee.*

---

### 7.4 Words to avoid in NC statements

| Avoid | Why | Use instead |
|---|---|---|
| "inadequate", "poor", "insufficient", "weak", "unacceptable" | Opinion, not fact; disputable | State the specific gap against the requirement |
| "always", "never", "all", "none" | Almost never supportable from a sample | "In 4 of 12 records sampled…" |
| "should", "must", "needs to", "we recommend…" (as the fix) | Auditor prescribing the corrective action | State only the gap; the auditee determines the action |
| "Mr Tan failed to…" | Blames a person | "The Store Supervisor role…" or better, describe the system failure |
| "appears to", "seems", "possibly", "may be" | Speculation, not evidence | Only state what was observed, read or heard |
| "It is felt that…" | Unattributable opinion | Delete |
| "Management doesn't care / isn't committed" | Unverifiable accusation about attitude | Point to the specific missing output of the required process |
| "Same as last year" (with no detail) | Not self-standing | Restate the requirement and the new evidence, and cross-reference the prior NC number |

---

## 8. Root cause analysis

### 8.1 Correction vs corrective action vs root cause
This distinction is the most commonly failed exam item, and the most commonly botched thing in real corrective action forms.

| Term | Definition (ISO 9000:2015 / ISO 14001:2015 cl. 10.2) | Answers | Example 3 EMS case |
|---|---|---|---|
| **Correction** | Action to **eliminate a detected nonconformity**. Deals with the symptom / the immediate situation. Does **not** prevent recurrence. | *"Fix what's in front of me now."* | Move the three drums into the bunded area; check for and clean up any spillage; block the drain. |
| **Root cause** | The **fundamental reason** the nonconformity occurred — the point at which, if you remove it, the problem cannot recur. | *"Why did this happen at all?"* | Chemical store capacity was never recalculated after production volumes rose; there is no trigger in the management-of-change process to reassess storage capacity. |
| **Corrective action** | Action to **eliminate the cause(s) of a nonconformity and prevent recurrence**. Addresses the root cause. | *"Stop it happening again — anywhere."* | Add a storage-capacity review step to the management-of-change procedure; establish a maximum-drum-count control with a visual marker and a trigger for scheduling early collection; brief all store staff. |
| *(For contrast)* **Preventive action** | In ISO 14001:2015 this is absorbed into **clause 6.1 risk and opportunity planning** — the whole "actions to address risks and opportunities" clause is the preventive action mechanism. | *"Stop it happening in the first place."* | Identifying storage capacity as a risk during aspects/risk planning, before any drum ever sits outside. |

**ISO 14001:2015 clause 10.2 requires the organization, when a nonconformity occurs, to:**
1. **react** to it and, as applicable, take action to control and correct it, and **deal with the consequences** (including mitigating adverse environmental impacts) — *this is the correction*;
2. **evaluate the need for action to eliminate the root cause(s)**, so that it does not recur or occur elsewhere, by reviewing the nonconformity, **determining its causes**, and determining whether similar nonconformities exist or could potentially occur;
3. **implement** any action needed;
4. **review the effectiveness** of any corrective action taken;
5. **make changes to the EMS**, if necessary.

Documented information must be retained as evidence of **the nature of the nonconformities and any subsequent actions taken**, and **the results of any corrective action**.

> **The auditor's follow-up test (6.7):** don't just check that *an action was done*. Check that (i) a **correction** was made, (ii) a **root cause** was actually identified — not restated as "human error" or "staff carelessness", (iii) the **corrective action addresses that root cause**, and (iv) its **effectiveness has been verified with evidence**.
>
> **"Human error" / "operator carelessness" / "need more training" are almost never root causes** — they are places where the analysis stopped too early. Ask: *why was the error possible? why was it not detected? why did the system allow it?*

### 8.2 The 5 Whys
Linear technique for a single causal chain. Start with the nonconformity statement and ask "why?" until you reach a cause that is **within the organization's control** and whose removal would prevent recurrence. Five is a guideline, not a rule — sometimes it is three, sometimes seven.

**Rules for doing it properly:**
- Start from the **NC statement**, not from a guess.
- Each "why" must be **supported by evidence**, not assumption.
- Stop when the cause is **actionable and systemic**, not when you reach a person to blame.
- If the answer is a person's failing, ask why **again** — the next level is the system failure.
- A chain that ends in "we need to train them" has usually stopped one or two Whys short.
- Test the chain **backwards** with "therefore": if the logic doesn't hold in reverse, the chain is broken.

### 8.3 Fishbone / Ishikawa (cause-and-effect) diagram
For problems with **multiple contributing factors across different domains**, where a single linear chain would be misleading. Place the nonconformity in the "head", draw major "bones" as cause categories, brainstorm causes on each bone, then test the most likely candidates with evidence (often driving each one down with 5 Whys).

**The 6M categories** (classic manufacturing set), with the **EMS-adapted set** alongside:

| 6M | EMS-adapted category | Typical EMS causes to probe |
|---|---|---|
| **Man / People** | People & competence | Competence not determined; training not delivered or not effective; awareness of aspects lacking (cl. 7.2, 7.3); roles/responsibilities undefined (cl. 5.3); shift handover |
| **Method** | Procedures & process | Procedure absent, unclear, out of date, or not reflecting actual practice; no management-of-change trigger; operational criteria not defined (cl. 8.1) |
| **Machine** | Equipment & infrastructure | Containment capacity; pollution control equipment maintenance; monitoring equipment calibration; no interlock or alarm |
| **Material** | Materials & inputs | Substitution of a chemical without review; supplier change; incoming material spec change; container type |
| **Measurement** | Monitoring & measurement | What is monitored not defined; wrong frequency; no trigger threshold; data not analysed or not escalated (cl. 9.1) |
| **Mother Nature / Milieu** | Environment & conditions | Weather (rain into an unbunded area); temperature; lighting; congestion/space; time pressure at shift end |
| *(often added)* | **Management & communication** | Resources not provided (cl. 7.1); communication between production and EHS (cl. 7.4); management review not acting on inputs (cl. 9.3) |

### 8.4 Worked ISO 14001 example

**The nonconformity (from Example 3 above):**
> EMS-P-11 Rev 2 section 6.2 was not met, in that three 200 L drums of liquid waste thinner (WD-104/105/106) were stored on unsealed ground in the external yard, outside secondary containment, approximately 4 m from an open surface-water drain, on 09 Apr 2024.

**Step 1 — Correction (immediate):**
- Drums relocated into bunded Chemical Store B on 09 Apr 2024; ground inspected for staining; no release identified; drain interceptor checked and confirmed clear. *(This is the 14001 cl. 10.2 a) "react and correct, deal with the consequences" step. It is **not** the corrective action.)*

**Step 2 — 5 Whys:**

| | Question | Answer | Evidence supporting it |
|---|---|---|---|
| **Why 1** | Why were the drums outside the bund? | The bunded area in Chemical Store B was full. | Store Supervisor statement; store observed at capacity — 18 of 18 drum positions occupied. |
| **Why 2** | Why was the bunded area full? | Waste thinner was being generated faster than it was being collected, and collections are booked only when the store is already full. | Waste Transfer Log WTL-03: generation averaged 11 drums/month over Jan–Mar 2024 vs. 6 drums/month in 2023; collections remained monthly. |
| **Why 3** | Why did generation outpace collection? | Production volume on the coating line rose ~80 % after the new contract started in January 2024, but the waste collection schedule was never revised. | Production records; unchanged collection frequency in EMS-P-08 schedule since 2022. |
| **Why 4** | Why was the collection schedule not revised when volumes rose? | The change in production volume was not assessed for its environmental consequences — no one reviewed waste generation, storage capacity or the aspects register when the new contract was taken on. | No management-of-change record for the January 2024 contract; aspects register EMS-REG-02 unchanged since 2021. |
| **Why 5** | Why was the change not assessed? | **The organization's management-of-change process (EMS-P-05) is triggered only by changes to *equipment or chemicals*; it contains no trigger for changes in *production volume or throughput*, so volume-driven environmental consequences are never reviewed.** | EMS-P-05 Rev 1 section 3 trigger list reviewed; contains no volume/throughput trigger. |

**Root cause identified:** The management-of-change process does not trigger an environmental review for changes in production volume or throughput, so increases in waste generation are not assessed against storage capacity, collection frequency, aspects or compliance obligations.

**Step 3 — Cross-check with a fishbone** (confirms it is not a single-thread problem):
- **Method:** MOC procedure has no throughput trigger *(← root cause)*; EMS-P-08 collection frequency is fixed rather than demand-driven.
- **Measurement:** No monitoring of drum-storage occupancy; no threshold or alarm at, say, 80 % capacity; waste generation KPI reported monthly in arrears, too late to act.
- **People:** Store Supervisor had no defined escalation route when the store filled up; production planning has no EHS touchpoint.
- **Machine/Infrastructure:** Bund capacity sized for 2022 volumes.
- **Management:** Aspects register (and therefore the significance ratings driving controls) not maintained on change — *the same underlying weakness that produced Example 2's major NC*. **This linkage across two findings is exactly what ISO 19011 6.4.9.2 d) means by identifying trends.**

**Step 4 — Corrective actions (addressing the root cause, not the symptom):**
1. Revise EMS-P-05 (Management of Change) to add **production volume / throughput change** as a trigger for environmental review, with a mandatory check of waste generation rates, storage capacity, aspects register and compliance obligations. *(Owner: EHS Manager. Due: 31 May 2024.)*
2. Change waste collection from fixed-monthly to **threshold-triggered**: automatic collection booking when drum occupancy reaches 70 %. Install a visual capacity marker and add occupancy to the daily store check. *(Owner: Store Supervisor / EHS. Due: 30 Apr 2024.)*
3. Update the Environmental Aspects Register for current coating-line volumes and re-assess significance. *(Owner: EHS Manager. Due: 31 May 2024.)*
4. Brief store and production planning staff on the revised MOC trigger and the escalation route when storage nears capacity. *(Owner: EHS Manager. Due: 15 Jun 2024.)*

**Step 5 — Verification of effectiveness (the auditor's 6.7 follow-up, not to be done at day 1):**
- Confirm EMS-P-05 Rev 2 issued with the throughput trigger, and that at least one subsequent volume change has an MOC record showing the environmental review was performed.
- Sample three months of storage occupancy records and collection bookings after implementation — confirm occupancy never exceeded 70 % without a booking, and no drums stored outside containment.
- Re-inspect the external yard and Chemical Store B unannounced.
- Confirm the aspects register reflects current volumes.
- **Only then close the finding.** "Procedure revised" alone is implementation, not effectiveness.

> **Contrast — a weak corrective action** that a trained auditor must reject: *"Store Supervisor reminded to keep drums inside the bund. Toolbox talk held 10 Apr 2024. Closed."* This is a **correction plus a reminder**, not a corrective action. It addresses no cause, and the drums will be outside again within two months because the capacity problem is untouched.

---

## 9. Opening and closing meeting agendas

### 9.1 Opening meeting (ISO 19011:2018, 6.4.3)

**Purpose (a–c):** (a) confirm the agreement of all participants to the audit plan; (b) introduce the audit team and their roles; (c) ensure that all planned audit activities can be performed.

**Who:** held with the auditee's management and, where appropriate, those responsible for the functions or processes to be audited. **Chaired by the audit team leader.** An opportunity to ask questions should be provided. For formal audits, records of attendance should be retained.

> **Scale it:** *"In many instances, e.g. internal audits in a small organization, the opening meeting may simply consist of communicating that an audit is being conducted and explaining the nature of the audit."*

**Standard agenda:**

**A. Introductions**
1. Introduce the audit team and their roles.
2. Introduce other participants — **observers and guides, interpreters — and outline their roles**.
3. Introduce the audit methods used to manage risks to the organization arising from the presence of the audit team.

**B. Confirmations**
4. The audit **objectives, scope and criteria**.
5. The **audit plan** and other relevant arrangements — including the date and time for the **closing meeting**, any interim meetings between the team and auditee management, and any change(s) needed.
6. **Formal communication channels** between the audit team and the auditee.
7. The **language** to be used during the audit.
8. That the auditee will be **kept informed of audit progress** during the audit.
9. The **availability of resources and facilities** needed by the audit team.
10. Matters relating to **confidentiality and information security**.
11. Relevant **access, health and safety, security, emergency and other arrangements** for the audit team.
12. **Activities on site that can impact the conduct of the audit**.

**C. Presentation of information**
13. The **method of reporting audit findings**, including **criteria for grading**, if any.
14. **Conditions under which the audit may be terminated**.
15. **How to deal with possible findings** during the audit.
16. Any **system for feedback** from the auditee on the findings or conclusions, including **complaints or appeals**.

*Practical additions used in internal audit practice:* thank the auditee for their time and cooperation; confirm the sampling basis up front; confirm timings for breaks and the lunch period; confirm who will accompany the auditors to each area; check that the required staff are available and not on leave/shift.

### 9.2 Closing meeting (ISO 19011:2018, 6.4.10)

**Purpose:** "A closing meeting should be held to present the audit findings and conclusions."

**Who:** **chaired by the audit team leader**, attended by the auditee's management and, as applicable: those responsible for the functions or processes audited; the audit client; other members of the audit team; other relevant interested parties determined by the audit client and/or auditee.

> **Scale it:** *"For some audit situations, the meeting can be formal and minutes, including records of attendance, should be kept. In other instances, e.g. internal audits, the closing meeting can be less formal and consist solely of communicating the audit findings and audit conclusions."*

**Standard agenda:**

1. **Thank the auditee** for cooperation, time and access.
2. **Re-confirm the audit objectives, scope and criteria** — remind everyone what was and was not covered.
3. **State the sampling caveat** — verbatim from 6.4.10 a): "advising that the audit evidence collected was based on a **sample** of the information available and **is not necessarily fully representative** of the overall effectiveness of the auditee's processes."
4. **Present positive findings and good practices** — conformities and areas of strength observed.
5. **Present the audit findings** — each nonconformity read out with its requirement, evidence and grade, and its acknowledgement confirmed. Present opportunities for improvement, if specified by the audit objectives, **"emphasiz[ing] that recommendations are not binding."**
6. **Present the audit conclusions** — "in such a manner that they are understood and acknowledged by the auditee's management" (6.4.10 e).
7. **Explain the method of reporting** (6.4.10 b) — what the report will contain, and when it will be issued.
8. **Explain how the audit findings should be addressed**, based on the agreed process (6.4.10 c) — correction, root cause analysis, corrective action, and **the agreed time frame for an action plan** ("If defined in the management system or by agreement with the audit client, the participants should agree on the time frame for an action plan to address audit findings").
9. **Explain the possible consequences of not adequately addressing the findings** (6.4.10 d).
10. **Explain related post-audit activities** (6.4.10 f) — implementation and review of corrective actions, addressing audit complaints, the appeal process, and follow-up verification.
11. **Advise of any situations encountered during the audit that may decrease the confidence that can be placed in the audit conclusions** (e.g. records unavailable, key staff absent, area not accessible, process not running).
12. **Discuss and resolve any diverging opinions** regarding the findings or conclusions — **"If not resolved, this should be recorded."**
13. **Questions from the auditee**; confirm next steps and close.

> "The degree of detail should take into account the effectiveness of the management system in achieving the auditee's objectives, including consideration of its context and risks and opportunities," and the auditee's familiarity with the audit process.

> **No surprises rule.** Everything presented at the closing meeting should already have been raised with the relevant area during the audit (6.4.8: findings "should be reviewed with the auditee in order to obtain acknowledgement that the audit evidence is accurate"). A nonconformity first revealed at the closing meeting is an auditor failure, not an auditee failure.

---

## 10. Audit report contents (ISO 19011:2018, 6.5.1)

**The report "should provide a complete, accurate, concise and clear record of the audit."**

### Mandatory content — "should include or refer to" (a–k)

| | Item |
|---|---|
| **a** | **Audit objectives** |
| **b** | **Audit scope** — particularly identification of the organization (the auditee) and the functions or processes audited |
| **c** | **Identification of the audit client** |
| **d** | **Identification of the audit team and the auditee's participants** in the audit |
| **e** | **Dates and locations** where the audit activities were conducted |
| **f** | **Audit criteria** |
| **g** | **Audit findings and related evidence** |
| **h** | **Audit conclusions** |
| **i** | **A statement on the degree to which the audit criteria have been fulfilled** |
| **j** | **Any unresolved diverging opinions** between the audit team and the auditee |
| **k** | **A statement that audits by nature are a sampling exercise; as such there is a risk that the audit evidence examined is not representative** |

### Optional content — "can also include or refer to, as appropriate"
- the **audit plan** including time schedule;
- a **summary of the audit process**, including any **obstacles encountered that may decrease the reliability of the audit conclusions**;
- confirmation that the audit objectives have been achieved within the audit scope in accordance with the audit plan;
- **any areas within the audit scope not covered**, including any issues of availability of evidence, resources or confidentiality, with related justifications;
- a summary covering the audit conclusions and the main audit findings that support them;
- **good practices identified**;
- **agreed action plan follow-up**, if any;
- a **statement of the confidential nature** of the contents;
- any **implications for the audit programme or subsequent audits**.

### Distribution (6.5.2)
- Issued **within an agreed period of time**; if delayed, the reasons communicated to the auditee and the programme manager.
- **Dated, reviewed and accepted**, as appropriate, in accordance with the audit programme.
- Distributed to the relevant interested parties defined in the audit programme or audit plan.
- **"When distributing the audit report, appropriate measures to ensure confidentiality should be considered."**

> **Practical internal-audit report structure** built on the above: 1) Cover/identification block (a–f); 2) Executive summary for management; 3) Conclusion and statement on degree of fulfilment of criteria (h, i); 4) Summary table of findings by grade; 5) Individual NC/OFI forms (g) — each carrying requirement, evidence, declaration, grade, and space for the auditee's correction, root cause, corrective action, target date and verification; 6) Good practices; 7) Areas not covered and obstacles; 8) Unresolved diverging opinions (j); 9) **Sampling caveat (k)**; 10) Distribution list and confidentiality statement. Item **(k) is the one internal auditors most often omit** — and it is mandatory guidance.

---

## 11. Common auditor mistakes and pitfalls

### A. Planning and preparation
1. **Not planning** — turning up with a generic checklist and no desktop review (6.3.1). You cannot spot deficiencies, omissions or conflicts in the documentation if you haven't read it.
2. **Scope creep** — auditing beyond the agreed scope because something interesting turned up. Correct action: note it, report it to the team leader (6.4.4), do not chase it.
3. **Ignoring previous audit results** — A.18.1 a) requires "follow-up of previous audit records and conclusions". Repeat findings are the single strongest signal in an internal audit.
4. **Even-spreading the time** — giving equal time to every clause instead of weighting by risk. Breaches the **risk-based approach** principle; ISO 19011 5.1 says priority goes "to matters... with higher inherent risk and lower level of performance."
5. **Not verifying auditor independence** — letting someone audit their own department or their own process (Principle e).
6. **Not confirming feasibility** (6.2.3) — auditing a line that isn't running, or on a day the key staff are on leave.

### B. Conducting the audit
7. **Auditing the standard clause-by-clause instead of the process** — marching down the clause list produces a fragmented picture. **A.3 Professional judgement** warns auditors to "avoid concentrating on the specific requirements of each clause of the standard at the expense of achieving the intended [outcome]", and 7.2.3.2 requires the ability to "audit a process from start to finish, including the interrelations with other processes."
8. **Being a slave to the checklist** — 6.3.4 verbatim: "The use of these media **should not restrict the extent of audit activities**." Ticking boxes without following the interesting thread is the commonest rookie failure.
9. **Auditing documents instead of practice** — confirming that a procedure exists and stopping. A document proves intent; only records and observation prove implementation.
10. **Interviewing only managers** — the manager tells you the procedure; the operator shows you the practice. A.17 a) requires "individuals from appropriate levels and functions performing activities".
11. **Accepting verbal assurance** — closing a line of enquiry on "yes we do that" without "show me". Breaches the evidence-based approach: "only information that can be subject to some degree of verification should be accepted as audit evidence" (6.4.7).
12. **Talking too much / lecturing** — the auditor should be listening. Every minute you spend explaining is a minute you're not collecting evidence.
13. **Leading questions** — supplying the answer, then recording it as evidence.
14. **Consulting / giving solutions** — "You should buy software for this." Breaches independence, makes you the author of next year's audit subject, and short-circuits the auditee's root cause analysis. Note the gap; the auditee owns the fix.
15. **Auditing the person, not the system** — asking "why didn't *you*…" produces defensiveness and hides the systemic cause.
16. **Arrogance / condescension toward frontline staff** — destroys cooperation for every future audit and breaches "diplomatic" and "culturally sensitive" (7.2.2 c, l).
17. **Letting the guide answer for the interviewee** — 6.4.2: guides "should not influence or interfere with the conduct of the audit."
18. **Being led around by the auditee** — following a curated tour route and a pre-selected file of perfect records. Choose your own samples.
19. **Sample of one** — raising a systemic finding from a single instance without checking whether it is isolated (A.18.1 f: "sample size").
20. **Not recording evidence at the moment you find it** — memory is not evidence. Capture PLOD detail on the spot; a note written up that evening is already degraded.
21. **Touching or operating equipment** — A.15 b) verbatim: "do not touch or manipulate any equipment, unless explicitly permitted, **even when competent or licensed**."
22. **Photographing or copying without permission** — A.15 requires permission to be asked **in advance**, with confidentiality and security considered.
23. **Ignoring an immediate significant risk** to save it for the closing meeting — 6.4.4 requires it be reported **without delay**.
24. **Running out of time** and skipping the areas planned for the afternoon — those are usually the ones the auditee was least ready for.

### C. Findings and grading
25. **Findings with no requirement** — a finding that cites no criterion is an opinion. If no requirement is breached, it is at most an OFI.
26. **Findings with no evidence** — "records were not well maintained" is unverifiable and indefensible.
27. **Opinion words** — "poor", "inadequate", "insufficient", "weak" instead of the factual gap.
28. **Prescribing the corrective action inside the finding** — pre-empts root cause analysis and breaches independence.
29. **Naming individuals** — invites blame, guarantees resistance, and misidentifies a system failure as a personal one.
30. **Grading softly to avoid conflict** — downgrading a major to a minor, or a real NC to an OFI, because the auditee pushed back. Breaches **fair presentation** and **fortitude** (7.2.2 j). The OFI category is not a diplomatic parking space for findings you don't want to argue about.
31. **Grading harshly to look rigorous** — inflating an isolated administrative lapse to a major destroys the credibility of the grading scale and of the auditor.
32. **Inconsistent grading between auditors** — the whole point of Clause 4 is that independent auditors "reach similar conclusions in similar circumstances." Requires a written, shared grading rule.
33. **Surprises at the closing meeting** — findings must be reviewed with the auditee as they arise (6.4.8) to obtain acknowledgement that the evidence is accurate.
34. **Dropping a finding because the auditee disagreed** — 6.4.8 and 6.5.1 j) require unresolved diverging opinions to be **recorded in the report**, not deleted.
35. **Missing the trend** — reporting five findings individually without noting that all five point to the same weak process. 6.4.9.2 d) explicitly requires considering "similar findings made in different areas... for the purpose of identifying trends."

### D. Reporting
36. **Late reports** — the report loses its force; 6.5.2 requires issue within an agreed period, with reasons communicated if delayed.
37. **Omitting the sampling caveat** — mandatory guidance under 6.5.1 k) and the most commonly missing element of internal audit reports.
38. **Omitting positives and good practices** — a report of pure criticism is demoralising, is not a fair presentation of the audit, and loses management's attention.
39. **Narrative, story-format findings** — long, meandering findings that bury the requirement and the evidence. Keep them short, structured and factual.
40. **No statement on the degree to which criteria were fulfilled** — required by 6.5.1 i); many internal reports list findings and never state an overall verdict.
41. **Not recording areas within scope that were not covered** — leaves management with false assurance.

### E. Follow-up and programme level
42. **Closing findings on promises** — accepting "procedure will be revised" as closure. 6.7 requires that "the completion **and effectiveness** of these actions should be verified."
43. **Accepting correction as corrective action** — the drums were moved back, so the finding is closed. Nothing prevents recurrence.
44. **Accepting "human error" or "more training required" as a root cause** — the analysis stopped too early.
45. **No verification of effectiveness after a suitable interval** — effectiveness cannot be verified the day the action is implemented; you need evidence of the changed system operating over time.
46. **Not feeding audit results into management review** — 6.7 requires outcomes be "reported to the audit client for management review" (the hand-off to ISO 14001 cl. 9.3).
47. **Never reviewing the audit programme itself** (5.7) — running the same audit plan year after year, so the programme never learns from its own results.
48. **Never evaluating the auditors** (7.4, 7.6) — no witnessed audits, no feedback, no CPD, so bad habits are never corrected.
49. **Treating the internal audit as a certification-audit rehearsal only** — the purpose under ISO 14001 cl. 9.2 is to determine whether the EMS conforms **and is effectively implemented and maintained**, and to provide information to management. Effectiveness — environmental performance — is the part most often skipped.

---

## 12. Quick-reference summary for slide/handout use

**The seven principles:** Integrity · Fair presentation · Due professional care · Confidentiality · Independence · Evidence-based approach · Risk-based approach.
*(Mnemonic: **I** **F**ind **D**ue **C**are **I**s **E**ssential **R**eally.)*

**The audit lifecycle:** Initiate → Prepare → Conduct (Open / Collect / Find / Conclude / Close) → Report → Complete → Follow up.

**The three-part NC:** Requirement + Evidence + Statement of nonconformity.

**The four evidence sources:** Interview · Observation · Document · Record.

**The evidence test:** Sufficient (enough) + Appropriate (relevant and reliable) + Verifiable (re-findable).

**The four C's of verifying information (A.5):** Complete · Correct · Consistent · Current.

**The questioning funnel:** Open → Probing → Clarifying → Closed → **Show me**.

**PLOD:** Person (role) · Location · Object · Document (with revision/date).

**The correction chain:** Correction (fix it) → Root cause (why?) → Corrective action (stop it recurring) → Verify effectiveness.

**Never:** lead, consult, blame, guess, or accept "we always do it that way."

---

### Sources
- [ISO 19011:2018 — Guidelines for auditing management systems (full text)](https://www.synersia.org/wp-content/uploads/2021/02/ISO-19011-2018-Pedoman-Audit-Sistem-Manajemen-EN.pdf) — primary source for all Clause 3, 4, 5, 6, 7 and Annex A material quoted above
- [ISO 19011:2018 catalogue entry — iso.org](https://www.iso.org/standard/70017.html)
- [ISO 19011:2018 Clause 4 — Principles of auditing (Pretesh Biswas)](https://preteshbiswas.com/2023/11/28/iso-190012018-clause-4-principles-of-auditing/)
- [ISO 19011:2018 Clause 6 — Conducting an audit (Pretesh Biswas)](https://preteshbiswas.com/2023/12/03/iso-190112018-clause-6-conducting-an-audit/)
- [ISO 19011:2018 Clause 7 — Competence and evaluation of auditors (Pretesh Biswas)](https://preteshbiswas.com/2023/12/07/iso-190112018-clause-7-competence-and-evaluation-of-auditors/)
- [Writing an effective nonconformity — CQI/IRCA](https://www.quality.org/knowledge/writing-effective-nonconformity)
- [ISO 9001 Auditing Practices Group — Guidance on Reviewing a Nonconformity (ISO/TC 176)](https://committee.iso.org/files/live/sites/tc176sc2/files/documents/ISO%209001%20Auditing%20Practices%20Group%20docs/Auditing%20General/APG-ReviewNonconformity2015.pdf)
- [Common ISO 14001 nonconformances written by third-party auditors — simpleQuE](https://www.simpleque.com/commmon-iso-14001-nonconformances-written-by-third-party-auditors/)
- [ISO/IEC 17021-1:2015 Section 3 — Terms and Definitions (major/minor nonconformity)](https://www.iasonline.org/wp-content/uploads/2021/02/17021-1-2015-Section-3-1.pdf)
- [ISO 14001 Clause 10.2 — Nonconformity and corrective action (Auditor Training Online)](https://blog.auditortrainingonline.com/blog/iso-14001-clause-10-2)
- [ISO 14001:2015 Clause 10.2 — Nonconformity and corrective action (Pretesh Biswas)](https://preteshbiswas.com/2023/09/16/iso-140012015-clause-10-2-nonconformity-and-corrective-action/)
- [Root Cause Analysis: The 5 Whys and Fishbone Diagram — SGS](https://www.sgs.com/en-jo/news/2026/05/root-cause-analysis-the-5-whys-and-fishbone-diagram-for-health-and-safety-incident-management)
- [Improving Internal Audits Using the 5W1H Method — Internal Audit 360](https://internalaudit360.com/improving-internal-audits-using-the-5w1h-method/)
- [Mistakes Rookie Internal Auditors Make and How to Fix Them — Internal Audit 360](https://internalaudit360.com/mistakes-rookie-internal-auditors-make-and-how-to-fix-them/)
- [Common ISO Audit Failures: Seven Mistakes to Avoid — The Auditor](https://www.theauditoronline.com/common-iso-audit-failures/)
- [Plan for Effective Interviews — Internal Auditor Magazine (IIA)](https://internalauditor.theiia.org/en/articles/2023/june/plan-for-effective-interviews/)
- [The Questioning Funnel — Revolution Learning & Development](https://www.revolutionlearning.co.uk/article/the-questioning-funnel/)
