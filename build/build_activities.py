#!/usr/bin/env python3
"""Build the standalone activity pack for TGS-2025054479.

For each activity, from the SAME source the deck and the Learner Guide use:
  activities/activity-N-<slug>.md    the learner-facing brief (markdown)
  activities/activity-N-<slug>.docx  the same brief, WSQ-formatted
  activities/activity-N-<slug>.pdf   rendered PDF (the user asked for PDFs)
  activities/README.md               the index

The learner brief deliberately EXCLUDES the model answer and the trainer debrief —
those go in a separate trainer pack so the briefs can be handed out in class.
"""
import os, sys, re, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_BREAK

import course_data as C
import prodoc as P
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3

ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(REPO, "activities")
ASSETS = os.path.join(REPO, "courseware", "assets")
LOGO = os.path.join(ASSETS, "tertiary-infotech-logo.png")
os.makedirs(OUT, exist_ok=True)

SOFFICE = "soffice"


def slug(t):
    s = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return re.sub(r"-+", "-", s)[:48]


def h(doc, text, level):
    x = doc.add_heading(text, level=level)
    for r in x.runs:
        r.font.name = "Arial"
    return x


def para(doc, text, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    P.md_runs(p, text, size=size)
    return p


def bullet(doc, text, size=11):
    p = doc.add_paragraph(style="List Bullet")
    P.md_runs(p, text, size=size)
    return p


def callout(doc, label, text, fill="F5F8FC", size=10.5):
    t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"
    c = t.rows[0].cells[0]
    P.shade_cell(c, fill); c.text = ""
    p = c.paragraphs[0]
    r = p.add_run(label + "  ")
    r.bold = True; r.font.size = Pt(size); r.font.name = "Arial"
    r.font.color.rgb = P.BRAND
    P.md_runs(p, text, size=size)
    doc.add_paragraph()


def build_docx(a, trainer=False):
    doc = Document()
    sec = doc.sections[0]
    sec.left_margin = sec.right_margin = Cm(2.2)
    sec.top_margin = sec.bottom_margin = Cm(2.0)
    P.style_base(doc)

    kind = f"Activity {a['num']}" + (" — Trainer Pack" if trainer else "")
    P.add_cover_page(doc, kind, C.TITLE, "5.0", C.COURSE_CODE, org_logo=LOGO)

    h(doc, f"Activity {a['num']} — {a['title']}", 1)
    para(doc, f"**Topic {int(a['topic'])}**  ·  **{a['minutes']} minutes**  ·  "
              f"Assesses **{a['ka']}**  ·  Course {C.COURSE_CODE}")

    h(doc, "Learning purpose", 2)
    para(doc, a["desc"])

    h(doc, "Scenario", 2)
    for block in a["scenario"].split("\n\n"):
        b = block.strip()
        if not b:
            continue
        if b.startswith("* "):
            for li in b.split("\n"):
                if li.strip().startswith("* "):
                    bullet(doc, li.strip()[2:])
        else:
            para(doc, b)

    h(doc, "The evidence you have been given", 2)
    for f in a["facts"]:
        bullet(doc, f)

    h(doc, "What you will produce", 2)
    callout(doc, "DELIVERABLE —", a["build"], fill="E8F0FE")

    h(doc, "Step-by-step method", 2)
    for i, (title, detail) in enumerate(a["steps"], 1):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(f"Step {i}: {title}")
        r.bold = True; r.font.size = Pt(11); r.font.name = "Arial"
        r.font.color.rgb = P.BRAND
        para(doc, detail, size=10.5)

    h(doc, "Questions to answer", 2)
    for i, (q, guide) in enumerate(a["questions"], 1):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(f"Q{i}. {q}")
        r.bold = True; r.font.size = Pt(11); r.font.name = "Arial"
        if trainer:
            para(doc, f"*What a good answer contains:* {guide}", size=10)
        else:
            doc.add_paragraph()

    h(doc, "Self-check", 2)
    callout(doc, "YOU ARE DONE WHEN —", a["test"], fill="E8F7EE")

    h(doc, "If you are stuck — what usually goes wrong", 2)
    for pf in a.get("pitfalls", []):
        bullet(doc, pf, size=10.5)

    if trainer:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        h(doc, "Model answer (trainer only)", 1)
        for block in a["answers"].split("\n\n"):
            if block.strip():
                para(doc, block.strip(), size=10.5)
        h(doc, "Trainer debrief", 1)
        para(doc, a["debrief"], size=10.5)

    P.add_page_numbers(doc)
    P.enable_update_fields(doc)
    return doc


def build_md(a):
    L = []
    L.append(f"# Activity {a['num']} — {a['title']}")
    L.append("")
    L.append(f"**Course:** {C.TITLE} ({C.COURSE_CODE})  ")
    L.append(f"**Topic:** {int(a['topic'])}  ·  **Duration:** {a['minutes']} minutes  ·  "
             f"**Assesses:** {a['ka']}")
    L.append("")
    L.append("## Learning purpose")
    L.append("")
    L.append(a["desc"])
    L.append("")
    L.append("## Scenario")
    L.append("")
    L.append(a["scenario"])
    L.append("")
    L.append("## The evidence you have been given")
    L.append("")
    for f in a["facts"]:
        L.append(f"- {f}")
    L.append("")
    L.append("## What you will produce")
    L.append("")
    L.append(f"> **DELIVERABLE —** {a['build']}")
    L.append("")
    L.append("## Step-by-step method")
    L.append("")
    for i, (title, detail) in enumerate(a["steps"], 1):
        L.append(f"### Step {i}: {title}")
        L.append("")
        L.append(detail)
        L.append("")
    L.append("## Questions to answer")
    L.append("")
    for i, (q, _g) in enumerate(a["questions"], 1):
        L.append(f"**Q{i}.** {q}")
        L.append("")
    L.append("## Self-check")
    L.append("")
    L.append(f"> **YOU ARE DONE WHEN —** {a['test']}")
    L.append("")
    L.append("## If you are stuck — what usually goes wrong")
    L.append("")
    for pf in a.get("pitfalls", []):
        L.append(f"- {pf}")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"*© 2026 {C.ORG}. All rights reserved.*")
    return "\n".join(L) + "\n"


def main():
    made = []
    for a in ACTIVITIES:
        base = f"activity-{a['num']}-{slug(a['title'])}"
        # markdown (learner)
        with open(os.path.join(OUT, base + ".md"), "w") as f:
            f.write(build_md(a))
        # docx learner + trainer
        build_docx(a, trainer=False).save(os.path.join(OUT, base + ".docx"))
        build_docx(a, trainer=True).save(os.path.join(OUT, base + "-trainer.docx"))
        made.append((a, base))
        print("  built", base)

    # index
    idx = [f"# Activities — {C.TITLE}", "",
           f"**Course code:** {C.COURSE_CODE}  ·  **Version:** {C.VERSION}  ·  "
           f"{C.VERSION_DATE}", "",
           "Three scenario-based case-study activities, one per topic. Each brief is "
           "self-contained: scenario, given evidence, step-by-step method, questions and a "
           "self-check. Full model answers are in the Learner Guide and in the matching "
           "`-trainer` pack.", "",
           "| # | Activity | Topic | Duration | Assesses | Files |",
           "|---|---|---|---|---|---|"]
    for a, base in made:
        idx.append(f"| {a['num']} | {a['title']} | Topic {int(a['topic'])} | "
                   f"{a['minutes']} min | {a['ka']} | "
                   f"[md]({base}.md) · [docx]({base}.docx) · [pdf]({base}.pdf) |")
    idx += ["", "## How these are used", "",
            "- Learners receive the **learner brief** (`.pdf` / `.docx`) in class.",
            "- Trainers use the **`-trainer.docx`** pack, which adds the model answer, the "
            "answer guidance per question and the debrief notes.",
            "- The same content appears in Section 5 of the Learner Guide, generated from "
            "the same source module, so the two can never diverge.", "",
            f"*© 2026 {C.ORG}. All rights reserved.*"]
    with open(os.path.join(OUT, "README.md"), "w") as f:
        f.write("\n".join(idx) + "\n")
    print("  built README.md")

    # PDFs
    docxs = [os.path.join(OUT, f) for f in sorted(os.listdir(OUT)) if f.endswith(".docx")]
    if docxs:
        subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf",
                        "--outdir", OUT] + docxs,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  rendered {len(docxs)} PDFs")


if __name__ == "__main__":
    main()
