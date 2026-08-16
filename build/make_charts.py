#!/usr/bin/env python3
"""Generate the diagram / chart assets for the ISO 14001:2015 Internal Auditor deck.

House rules (tertiary-ppt-design): matplotlib, Arial, white background, brand palette,
150 dpi, bbox_inches="tight". Never bake the slide title into the figure — head() draws
it. Captions belong in the figure only where they label a part of the diagram.
"""
import os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import (FancyBboxPatch, Rectangle, FancyArrowPatch,
                                Circle as _MplCircle, Ellipse, Polygon)
import numpy as np

plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 11

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "courseware", "assets"))
os.makedirs(OUT, exist_ok=True)

BLUE = "#1F6FEB"; TEAL = "#10B981"; VIOLET = "#7C3AED"; AMBER = "#F59E0B"
RED = "#DC2626"; INK = "#161B26"; GREY = "#5B6372"; LIGHT = "#F5F8FC"; LINE = "#D7E0EA"
GREEN = "#16845B"


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ", name)


def _box(ax, x, y, w, h, text, fc, ec=None, tc="white", fs=11, bold=True, r=0.02):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec or fc, lw=1.4, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=tc,
            fontsize=fs, fontweight="bold" if bold else "normal", zorder=3, linespacing=1.45)


def _arrow(ax, x1, y1, x2, y2, color=GREY, lw=1.8, style="-|>"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, color=color,
                                 lw=lw, mutation_scale=15, zorder=1,
                                 shrinkA=0, shrinkB=0))


def _blank(w=12, h=6.4):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.axis("off")
    ax._agg = w / h            # data-unit aspect: 1 x-unit = _agg y-units on screen
    return fig, ax


def Circle(xy, r, **kw):
    """Visually-round badge inside a 0-100 x 0-100 box on a non-square figure.

    A true Circle in these axes renders as an ellipse because the x and y data units
    map to different screen lengths. Callers keep the Circle(...) signature; the
    active axes' stored aspect squashes the width so the badge looks round.
    """
    ax = plt.gca()
    a = getattr(ax, "_agg", 1.0)
    return Ellipse(xy, width=2 * r / a, height=2 * r, **kw)


# ---------------------------------------------------------------- 1. PDCA / Annex SL
def pdca_clauses():
    fig, ax = _blank(12, 7.0)
    ring = [("PLAN", BLUE, "Clause 4  Context\nClause 5  Leadership\nClause 6  Planning\nClause 7  Support"),
            ("DO", TEAL, "Clause 8\nOperation"),
            ("CHECK", AMBER, "Clause 9\nPerformance\nevaluation"),
            ("ACT", VIOLET, "Clause 10\nImprovement")]
    cx, cy, R = 50, 50, 30
    angles = [135, 45, -45, -135]
    for (label, col, body), a in zip(ring, angles):
        rad = math.radians(a)
        x = cx + R * math.cos(rad); y = cy + R * math.sin(rad)
        ax.add_patch(Circle((x, y), 17, fc=col, ec="white", lw=3, zorder=2))
        ax.text(x, y + 7.5, label, ha="center", va="center", color="white",
                fontsize=15, fontweight="bold", zorder=3)
        ax.text(x, y - 3.5, body, ha="center", va="center", color="white",
                fontsize=9, zorder=3, linespacing=1.5)
    # centre
    ax.add_patch(Circle((cx, cy), 12.5, fc="white", ec=LINE, lw=2, zorder=4))
    ax.text(cx, cy + 2.6, "EMS", ha="center", va="center", color=INK,
            fontsize=14, fontweight="bold", zorder=5)
    ax.text(cx, cy - 3.2, "Continual\nimprovement", ha="center", va="center",
            color=GREY, fontsize=8.5, zorder=5, linespacing=1.4)
    # rotation arrows — clockwise PLAN -> DO -> CHECK -> ACT -> PLAN.
    # The axes are not equal-aspect, so the arc must be drawn in SCREEN space and
    # mapped back, otherwise the arrowheads point the wrong way and the arc misses
    # the badges. agg squashes x exactly as Circle() above does.
    agg = 12 / 7.0
    Rx, Ry = 24.5, 24.5            # arc radius in y-units
    for a0 in (118, 28, -62, -152):
        th = np.radians(np.linspace(a0, a0 - 56, 60))
        xs = cx + (Rx / agg) * np.cos(th) * 1.9
        ys = cy + Ry * np.sin(th) * 1.9
        ax.plot(xs, ys, color="#9AA4B2", lw=2.0, zorder=1, solid_capstyle="round")
        ax.add_patch(FancyArrowPatch((xs[-6], ys[-6]), (xs[-1], ys[-1]),
                                     arrowstyle="-|>", color="#9AA4B2", lw=2.0,
                                     mutation_scale=22, zorder=1,
                                     shrinkA=0, shrinkB=0))
    ax.text(50, 101, "Clause 4.1 / 4.2  Context of the organisation and interested parties",
            ha="center", va="center", color=GREY, fontsize=9.5, style="italic")
    save(fig, "pdca_clauses.png")


# ---------------------------------------------------------------- 2. Clause structure
def clause_structure():
    fig, ax = _blank(12, 6.3)
    rows = [
        ("4", "Context of the organisation", BLUE,
         "4.1 issues · 4.2 interested parties · 4.3 scope · 4.4 the EMS"),
        ("5", "Leadership", BLUE,
         "5.1 leadership & commitment · 5.2 environmental policy · 5.3 roles"),
        ("6", "Planning", BLUE,
         "6.1 risks & opportunities, aspects, compliance obligations · 6.2 objectives"),
        ("7", "Support", BLUE,
         "7.1 resources · 7.2 competence · 7.3 awareness · 7.4 communication · 7.5 documented info"),
        ("8", "Operation", TEAL,
         "8.1 operational planning & control (life cycle perspective) · 8.2 emergency preparedness"),
        ("9", "Performance evaluation", AMBER,
         "9.1 monitoring & evaluation of compliance · 9.2 internal audit · 9.3 management review"),
        ("10", "Improvement", VIOLET,
         "10.1 general · 10.2 nonconformity & corrective action · 10.3 continual improvement"),
    ]
    y = 92; h = 11.4; gap = 1.3
    for num, title, col, detail in rows:
        ax.add_patch(Rectangle((4, y - h), 92, h, fc=LIGHT, ec=LINE, lw=0.9, zorder=1))
        ax.add_patch(Rectangle((4, y - h), 1.5, h, fc=col, ec=col, zorder=2))
        ax.add_patch(Circle((10.5, y - h / 2), 3.4, fc=col, zorder=3))
        ax.text(10.5, y - h / 2, num, ha="center", va="center", color="white",
                fontsize=12.5, fontweight="bold", zorder=4)
        ax.text(16.5, y - h / 2 + 2.6, title, ha="left", va="center", color=INK,
                fontsize=12, fontweight="bold")
        ax.text(16.5, y - h / 2 - 2.9, detail, ha="left", va="center", color=GREY, fontsize=9)
        y -= (h + gap)
    save(fig, "clause_structure.png")


# ---------------------------------------------------------------- 3. Aspect vs impact
def aspect_impact():
    fig, ax = _blank(12, 5.6)
    ax.text(50, 95, "ACTIVITY, PRODUCT or SERVICE", ha="center", color=GREY,
            fontsize=10.5, fontweight="bold")
    _box(ax, 6, 66, 26, 18, "ENVIRONMENTAL\nASPECT", BLUE, fs=13)
    _box(ax, 37, 66, 26, 18, "ENVIRONMENTAL\nIMPACT", TEAL, fs=13)
    _box(ax, 68, 66, 26, 18, "CONTROL /\nOBJECTIVE", VIOLET, fs=13)
    ax.text(19, 61, "the CAUSE — what the\norganisation does that\ninteracts with the environment",
            ha="center", va="top", color=GREY, fontsize=9.5, linespacing=1.5)
    ax.text(50, 61, "the EFFECT — the change\nto the environment,\nadverse or beneficial",
            ha="center", va="top", color=GREY, fontsize=9.5, linespacing=1.5)
    ax.text(81, 61, "what the EMS does\nabout it — clause 8.1\noperational control",
            ha="center", va="top", color=GREY, fontsize=9.5, linespacing=1.5)
    _arrow(ax, 32.5, 75, 36.5, 75, BLUE, 2.2)
    _arrow(ax, 63.5, 75, 67.5, 75, TEAL, 2.2)
    ax.text(34.5, 79.5, "causes", ha="center", color=BLUE, fontsize=9, style="italic")
    ax.text(65.5, 79.5, "drives", ha="center", color=TEAL, fontsize=9, style="italic")

    ex = [("Discharge of trade effluent", "Water pollution; harm to aquatic life"),
          ("Use of diesel generator", "Depletion of fossil fuel; GHG emissions"),
          ("Solvent-based lamination", "VOC emissions; degraded air quality"),
          ("Storage of chemical drums", "Soil/groundwater contamination if spilled"),
          ("Segregating waste for recycling", "Conserves resources — a BENEFICIAL impact")]
    ax.add_patch(Rectangle((6, 4), 88, 46, fc=LIGHT, ec=LINE, lw=0.9))
    ax.text(10, 45, "ASPECT", ha="left", color=BLUE, fontsize=10, fontweight="bold")
    ax.text(52, 45, "IMPACT", ha="left", color=TEAL, fontsize=10, fontweight="bold")
    y = 38
    for a, i in ex:
        ax.text(10, y, a, ha="left", color=INK, fontsize=9.6)
        ax.text(48, y, "→", ha="center", color=GREY, fontsize=10)
        ax.text(52, y, i, ha="left", color=INK, fontsize=9.6)
        y -= 7.6
    save(fig, "aspect_impact.png")


# ---------------------------------------------------------------- 4. Audit lifecycle
def audit_lifecycle():
    fig, ax = _blank(12, 5.4)
    stages = [("6.2", "Initiating\nthe audit", BLUE),
              ("6.3", "Preparing\naudit activities", BLUE),
              ("6.4", "Conducting\naudit activities", TEAL),
              ("6.5", "Preparing &\ndistributing\nthe report", AMBER),
              ("6.6", "Completing\nthe audit", VIOLET),
              ("6.7", "Audit\nfollow-up", GREEN)]
    n = len(stages); w = 13.5; gap = ((100 - 8) - n * w) / (n - 1); x = 4
    for i, (num, label, col) in enumerate(stages):
        ax.add_patch(Rectangle((x, 40), w, 34, fc=LIGHT, ec=LINE, lw=1))
        ax.add_patch(Rectangle((x, 71), w, 3, fc=col, ec=col))
        ax.add_patch(Circle((x + w / 2, 63), 4.4, fc=col))
        ax.text(x + w / 2, 63, str(i + 1), ha="center", va="center",
                color="white", fontsize=15, fontweight="bold")
        ax.text(x + w / 2, 51, label, ha="center", va="center", color=INK,
                fontsize=9.6, fontweight="bold", linespacing=1.5)
        ax.text(x + w / 2, 43.5, f"ISO 19011 §{num}", ha="center", va="center",
                color=GREY, fontsize=8)
        if i < n - 1:
            ax.plot(x + w + gap / 2, 57, marker=">", ms=11, color=col,
                    markeredgecolor=col, zorder=4)
        x += w + gap
    ax.add_patch(Rectangle((4, 8), 92, 24, fc="#E8F0FE", ec=LINE, lw=0.9))
    ax.text(50, 27, "THE AUDIT PROGRAMME  (ISO 19011 Clause 5)", ha="center",
            color=BLUE, fontsize=11, fontweight="bold")
    ax.text(50, 17.5,
            "Objectives · roles & competence · risks and opportunities of the programme · "
            "resources\nEstablishing → implementing → monitoring → reviewing and improving "
            "the programme",
            ha="center", va="center", color=INK, fontsize=9.6, linespacing=1.7)
    for xx in (25, 50, 75):
        _arrow(ax, xx, 33, xx, 39, GREY, 1.4)
    save(fig, "audit_lifecycle.png")


# ---------------------------------------------------------------- 5. Risk matrix 5x5
def risk_matrix():
    fig, ax = plt.subplots(figsize=(9.2, 6.4))
    sev = ["1\nInsignificant", "2\nMinor", "3\nModerate", "4\nMajor", "5\nCatastrophic"]
    lik = ["5  Almost certain", "4  Likely", "3  Possible", "2  Unlikely", "1  Rare"]
    likv = [5, 4, 3, 2, 1]
    for r, lv in enumerate(likv):
        for c in range(5):
            score = lv * (c + 1)
            if score >= 15:   fc, tc = "#DC2626", "white"
            elif score >= 10: fc, tc = "#F59E0B", "white"
            elif score >= 5:  fc, tc = "#FCD34D", INK
            else:             fc, tc = "#86EFAC", INK
            ax.add_patch(Rectangle((c, 4 - r), 1, 1, fc=fc, ec="white", lw=2.2))
            ax.text(c + 0.5, 4 - r + 0.5, str(score), ha="center", va="center",
                    color=tc, fontsize=13, fontweight="bold")
    ax.set_xlim(-0.05, 5.05); ax.set_ylim(-0.05, 5.05)
    ax.set_xticks([i + 0.5 for i in range(5)]); ax.set_xticklabels(sev, fontsize=9)
    ax.set_yticks([i + 0.5 for i in range(5)]); ax.set_yticklabels(lik[::-1], fontsize=9)
    ax.set_xlabel("SEVERITY of environmental impact", fontsize=11, fontweight="bold",
                  color=INK, labelpad=10)
    ax.set_ylabel("LIKELIHOOD of occurrence", fontsize=11, fontweight="bold",
                  color=INK, labelpad=10)
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.tick_params(length=0)
    handles = [Rectangle((0, 0), 1, 1, fc=c) for c in ("#86EFAC", "#FCD34D", "#F59E0B", "#DC2626")]
    ax.legend(handles, ["1–4  Low — monitor", "5–9  Medium — controls",
                        "10–14  High — SIGNIFICANT", "15–25  Extreme — SIGNIFICANT, act now"],
              loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2,
              frameon=False, fontsize=9.5)
    fig.tight_layout()
    save(fig, "risk_matrix.png")


# ---------------------------------------------------------------- 6. NC statement anatomy
def nc_anatomy():
    fig, ax = _blank(12, 5.9)
    parts = [("1", "REQUIREMENT", BLUE,
              "State the exact requirement breached —\nthe clause of ISO 14001:2015, the\nprocedure, permit or legal obligation.",
              '"ISO 14001:2015 clause 7.5.2 requires\ndocumented information to be identified\nand approved for suitability."'),
             ("2", "EVIDENCE", TEAL,
              "The objective evidence you saw —\nspecific, traceable, verifiable.\nWho, what, where, which document.",
              '"The Waste Disposal Procedure WI-07 at\nthe Tuas store was unsigned, undated\nand showed no revision number."'),
             ("3", "NONCONFORMITY", RED,
              "The statement of the gap itself —\nwhat is not conforming. No opinions,\nno solutions, no blame.",
              '"Therefore documented information is\nnot controlled as required."')]
    x = 4; w = 29.5; gap = 2.75
    for num, title, col, desc, example in parts:
        ax.add_patch(Rectangle((x, 30), w, 60, fc=LIGHT, ec=LINE, lw=1))
        ax.add_patch(Rectangle((x, 87), w, 3, fc=col, ec=col))
        ax.add_patch(Circle((x + 5.4, 81), 3.6, fc=col))
        ax.text(x + 5.4, 81, num, ha="center", va="center", color="white",
                fontsize=13, fontweight="bold")
        ax.text(x + 11.5, 81, title, ha="left", va="center", color=col,
                fontsize=12, fontweight="bold")
        ax.text(x + 2.4, 71, desc, ha="left", va="top", color=INK,
                fontsize=9.5, linespacing=1.6)
        ax.add_patch(Rectangle((x + 2.2, 33), w - 4.4, 22, fc="white", ec=col, lw=1.1))
        ax.text(x + w / 2, 44, example, ha="center", va="center", color=INK,
                fontsize=8.6, style="italic", linespacing=1.6)
        if x < 60:
            ax.text(x + w + gap / 2, 60, "+", ha="center", va="center",
                    color=GREY, fontsize=17, fontweight="bold")
        x += w + gap
    ax.add_patch(Rectangle((4, 6), 92, 17, fc="#E8F7EE", ec=LINE, lw=0.9))
    ax.text(50, 18, "THE RULE", ha="center", color=GREEN, fontsize=10.5, fontweight="bold")
    ax.text(50, 11.5,
            "A nonconformity statement without all three parts is an opinion. "
            "Requirement + Evidence + Gap — every time.",
            ha="center", va="center", color=INK, fontsize=10.5)
    save(fig, "nc_anatomy.png")


# ---------------------------------------------------------------- 7. Five whys
def five_whys():
    fig, ax = _blank(11.5, 6.2)
    steps = [("PROBLEM", "Trade effluent exceeded the copper discharge limit", RED),
             ("WHY 1?", "The pH dosing pump was not maintaining set point", AMBER),
             ("WHY 2?", "The pH probe was reading 1.4 units high", AMBER),
             ("WHY 3?", "The probe had not been calibrated for 9 months", AMBER),
             ("WHY 4?", "It was not on the calibration schedule", BLUE),
             ("WHY 5?", "New equipment is not added to the schedule — no step in\nthe change-management procedure requires it", BLUE),
             ("ROOT CAUSE", "The management-of-change procedure omits calibration\nregistration — a SYSTEM gap, not an operator error", GREEN)]
    y = 92; h = 11.2; gap = 1.6
    for i, (label, text, col) in enumerate(steps):
        ax.add_patch(Rectangle((4, y - h), 92, h, fc=LIGHT if i else "#FEF2F2",
                               ec=LINE, lw=0.9))
        ax.add_patch(Rectangle((4, y - h), 1.6, h, fc=col, ec=col))
        ax.text(8.5, y - h / 2, label, ha="left", va="center", color=col,
                fontsize=10.5, fontweight="bold")
        ax.text(26, y - h / 2, text, ha="left", va="center", color=INK,
                fontsize=10, linespacing=1.45)
        if i < len(steps) - 1:
            _arrow(ax, 15, y - h, 15, y - h - gap, GREY, 1.5)
        y -= (h + gap)
    save(fig, "five_whys.png")


# ---------------------------------------------------------------- 8. Correction vs CA
def correction_vs_ca():
    fig, ax = _blank(12, 4.9)
    cols = [("CORRECTION", RED, "Fixes the SYMPTOM",
             ["Clean up the spill", "Re-label the drums", "Re-issue the missing record",
              "Immediate, necessary — but\nthe problem WILL come back"]),
            ("CORRECTIVE ACTION", TEAL, "Eliminates the CAUSE",
             ["Change the procedure", "Add the calibration to the schedule",
              "Re-train and verify competence", "Prevents RECURRENCE —\nthis is what clause 10.2 requires"]),
            ("CONTINUAL IMPROVEMENT", VIOLET, "Raises PERFORMANCE",
             ["Redesign to remove the hazard", "Substitute a less harmful input",
              "Improve the EMS itself", "Goes beyond conformity —\nclause 10.3"])]
    x = 4; w = 29.5; gap = 2.75
    for title, col, sub, items in cols:
        ax.add_patch(Rectangle((x, 8), w, 80, fc=LIGHT, ec=LINE, lw=1))
        ax.add_patch(Rectangle((x, 74), w, 14, fc=col, ec=col))
        ax.text(x + w / 2, 83.5, title, ha="center", va="center", color="white",
                fontsize=11.5, fontweight="bold")
        ax.text(x + w / 2, 77.5, sub, ha="center", va="center", color="white", fontsize=9.5)
        y = 66
        for it in items:
            ax.text(x + 2.6, y, "•  " + it, ha="left", va="top", color=INK,
                    fontsize=9.4, linespacing=1.55)
            y -= (13 if "\n" in it else 9.5)
        x += w + gap
    save(fig, "correction_vs_ca.png")


# ---------------------------------------------------------------- 9. Evidence sources
def evidence_sources():
    fig, ax = _blank(11.5, 5.6)
    ax.add_patch(Circle((50, 52), 15, fc=BLUE, zorder=3))
    ax.text(50, 56, "OBJECTIVE", ha="center", va="center", color="white",
            fontsize=12, fontweight="bold", zorder=4)
    ax.text(50, 48, "EVIDENCE", ha="center", va="center", color="white",
            fontsize=12, fontweight="bold", zorder=4)
    src = [(16, 84, "INTERVIEW", TEAL, "Ask the people who\ndo the work — then\nverify what they say"),
           (84, 84, "OBSERVATION", VIOLET, "Watch the process\nrunning; walk the\nsite and look"),
           (16, 20, "DOCUMENTS", AMBER, "Procedures, permits,\nlicences, registers,\ndrawings"),
           (84, 20, "RECORDS", GREEN, "Monitoring results,\ncalibration certs,\nwaste tickets, logs")]
    for x, y, label, col, desc in src:
        ax.add_patch(FancyBboxPatch((x - 15, y - 12), 30, 24,
                                    boxstyle="round,pad=0,rounding_size=1.5",
                                    fc=LIGHT, ec=col, lw=2, zorder=2))
        ax.text(x, y + 6.5, label, ha="center", va="center", color=col,
                fontsize=11.5, fontweight="bold", zorder=3)
        ax.text(x, y - 3.5, desc, ha="center", va="center", color=INK,
                fontsize=9, zorder=3, linespacing=1.5)
        dx, dy = 50 - x, 52 - y
        d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
        _arrow(ax, x + ux * 16, y + uy * 13, 50 - ux * 16, 52 - uy * 16, GREY, 1.6)
    ax.text(50, 4, "Sufficient · appropriate · verifiable · traceable to its source",
            ha="center", color=GREY, fontsize=10, style="italic")
    save(fig, "evidence_sources.png")


# ---------------------------------------------------------------- 10. NC grading
def nc_grading():
    fig, ax = _blank(12, 5.2)
    cards = [("MAJOR", RED,
              ["Total absence of a required process", "A systemic breakdown of the EMS",
               "A legal / permit breach", "Several minors against one clause",
               "Puts certification at risk"]),
             ("MINOR", AMBER,
              ["A single lapse against a requirement", "An isolated slip in an otherwise",
               "  working process", "Does not break the system",
               "Still needs correction + CA"]),
             ("OFI", TEAL,
              ["NOT a nonconformity", "The requirement IS met",
               "A suggestion to do better", "Never forced on the auditee",
               "Recorded separately"])]
    x = 4; w = 29.5; gap = 2.75
    for title, col, items in cards:
        ax.add_patch(Rectangle((x, 12), w, 76, fc=LIGHT, ec=LINE, lw=1))
        ax.add_patch(Rectangle((x, 76), w, 12, fc=col, ec=col))
        ax.text(x + w / 2, 82, title, ha="center", va="center", color="white",
                fontsize=13, fontweight="bold")
        y = 67
        for it in items:
            pre = "" if it.startswith("  ") else "•  "
            ax.text(x + 2.6, y, pre + it.strip(), ha="left", va="top",
                    color=INK, fontsize=9.6)
            y -= 10
        x += w + gap
    ax.text(50, 6, "Grade the finding against the REQUIREMENT and the EVIDENCE — never against "
                   "how the auditee reacts.",
            ha="center", color=GREY, fontsize=10, style="italic")
    save(fig, "nc_grading.png")


# ---------------------------------------------------------------- 11. Aspect register flow
def aspect_process():
    fig, ax = _blank(12, 4.6)
    steps = [("Map the\nprocess", BLUE, "inputs → activity →\noutputs"),
             ("Identify\naspects", BLUE, "normal · abnormal ·\nemergency"),
             ("Determine\nimpacts", TEAL, "the change to the\nenvironment"),
             ("Evaluate\nsignificance", AMBER, "severity × likelihood\nagainst criteria"),
             ("Register &\ncontrol", VIOLET, "significant aspects →\n6.1.4 actions, 8.1 controls")]
    n = len(steps); w = 16.5; gap = ((100 - 8) - n * w) / (n - 1); x = 4
    for i, (label, col, sub) in enumerate(steps):
        ax.add_patch(Rectangle((x, 30), w, 46, fc=LIGHT, ec=LINE, lw=1))
        ax.add_patch(Rectangle((x, 73), w, 3, fc=col, ec=col))
        ax.add_patch(Circle((x + w / 2, 64), 5, fc=col))
        ax.text(x + w / 2, 64, str(i + 1), ha="center", va="center", color="white",
                fontsize=15, fontweight="bold")
        ax.text(x + w / 2, 50, label, ha="center", va="center", color=INK,
                fontsize=10.5, fontweight="bold", linespacing=1.5)
        ax.text(x + w / 2, 37, sub, ha="center", va="center", color=GREY,
                fontsize=8.6, linespacing=1.5)
        if i < n - 1:
            ax.plot(x + w + gap / 2, 53, marker=">", ms=11, color=col,
                    markeredgecolor=col, zorder=4)
        x += w + gap
    ax.add_patch(Rectangle((4, 6), 92, 16, fc="#E8F0FE", ec=LINE, lw=0.9))
    ax.text(50, 14, "Clause 6.1.2 requires aspects to be determined for activities, products and "
                    "services the organisation can CONTROL and those it can INFLUENCE —\n"
                    "considering a life cycle perspective, and past, present and planned activities.",
            ha="center", va="center", color=INK, fontsize=9.5, linespacing=1.7)
    save(fig, "aspect_process.png")


# ---------------------------------------------------------------- 12. Questioning funnel
def question_funnel():
    """Funnel as staggered bands: the width narrows to show the funnel, but each band
    keeps a full-width text column so the examples never clip."""
    fig, ax = _blank(12, 6.1)
    tiers = [(2,  97, "OPEN", TEAL,
              "Get them talking. Cannot be answered yes/no.",
              '"Tell me how waste is handled here."   ·   "Walk me through what happens when a spill occurs."'),
             (8,  77, "PROBING", BLUE,
              "Follow the thread. Chase the detail behind the answer.",
              '"What happens if the reading is out of range?"   ·   "How do you know that?"'),
             (14, 57, "CLOSED", VIOLET,
              "Confirm one specific fact. Yes/no, and only at the end.",
              '"Is this the current revision?"   ·   "Was this drum labelled on Tuesday?"'),
             (20, 37, "SHOW ME", AMBER,
              "Convert the answer into objective evidence.",
              '"Show me the calibration certificate."   ·   "Prove the training was completed."')]
    for inset, y, label, col, why, ex in tiers:
        w = 100 - 2 * inset
        ax.add_patch(Rectangle((inset, y - 17), w, 17, fc=LIGHT, ec=LINE, lw=1))
        ax.add_patch(Rectangle((inset, y - 17), w, 17, fc="none", ec=col, lw=1.6))
        ax.add_patch(Rectangle((inset, y - 17), 1.6, 17, fc=col, ec=col))
        ax.text(inset + 4.5, y - 5.2, label, ha="left", va="center", color=col,
                fontsize=13, fontweight="bold")
        ax.text(inset + 21, y - 5.2, why, ha="left", va="center", color=GREY, fontsize=9.4)
        ax.text(inset + 4.5, y - 12.6, ex, ha="left", va="center", color=INK,
                fontsize=9.2, style="italic")
        if y > 40:
            ax.plot(50, y - 19.5, marker="v", ms=9, color="#9AA4B2")
    ax.add_patch(Rectangle((4, 0), 92, 15, fc="#FEF2F2", ec="#FCA5A5", lw=1))
    ax.text(50, 10.0, "NEVER LEAD THE WITNESS", ha="center", va="center",
            color=RED, fontsize=10, fontweight="bold")
    ax.text(50, 4.4, '"You do segregate the waste, don\'t you?"  —  you have just told the '
                     "auditee the answer, and the evidence is worthless.",
            ha="center", va="center", color=INK, fontsize=9.6, style="italic")
    save(fig, "question_funnel.png")


if __name__ == "__main__":
    print("Generating chart assets ->", OUT)
    pdca_clauses()
    clause_structure()
    aspect_impact()
    audit_lifecycle()
    risk_matrix()
    nc_anatomy()
    five_whys()
    correction_vs_ca()
    evidence_sources()
    nc_grading()
    aspect_process()
    question_funnel()
    print("Done.")
