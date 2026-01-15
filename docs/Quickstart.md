# ⭐ Shunyaya Structural Equations (SSE)

## Quickstart

**Deterministic • Structural Admissibility • Equation Governance • Trust Denial & Allowance • Reproducible Proofs**

---

## WHAT YOU NEED

Shunyaya Structural Equations (SSE) are intentionally **minimal**, **deterministic**, and **implementation-neutral**.

### Requirements

- Python 3.9+
- Standard library only (no external dependencies)

Everything is:

- deterministic
- offline
- reproducible
- identical across machines

No randomness.  
No training.  
No probabilistic heuristics.  
No adaptive tuning.

---

## MINIMAL PROJECT LAYOUT

A minimal SSE proof-series release contains:

```
Shunyaya-Structural-Equations/

case1/
  scripts/
    sse_case1_mgh17_solver_replay.py
    plot_sse_case1.py
  data/
    mgh17_data.csv
  allow_converged/
    trace_classical.csv
    trace_sse.csv
    plots_reference/
      permission_a_vs_iter.png
      cond_vs_iter_log.png
      resistance_s_vs_iter.png
      sse_vs_iter.png
      step_norm_vs_iter_log.png
  deny_numeric/
    trace_classical.csv
    trace_sse.csv
  abstain_singular/
    trace_classical.csv
    trace_sse.csv

case2/
  scripts/
    sse_case2_calculus_linearization.py
    plot_sse_case2.py
  recip_allow_safe_corridor/
    trace_classical.csv
    trace_sse.csv
    plots_reference/
      a_vs_k.png
      s_vs_k.png
      summary.png
  recip_deny_boundary_corridor/
    trace_classical.csv
    trace_sse.csv
  recip_abstain_instability_corridor/
    trace_classical.csv
    trace_sse.csv
  sqrt_allow_safe_corridor/
    trace_classical.csv
    trace_sse.csv
  sqrt_deny_boundary_corridor/
    trace_classical.csv
    trace_sse.csv
  sqrt_abstain_instability_corridor/
    trace_classical.csv
    trace_sse.csv

docs/
  Quickstart.md
  FAQ.md
  SSE_ver1.3.pdf
  PROOF-SSE_ver1.3.pdf

README.md
LICENSE

```

---

## Notes

- Case 1 uses a **single canonical real dataset**
- Case 2 uses **declared mathematical regimes** (no dataset required)
- Each output folder represents a **structural regime**, not a rerun
- No build step. No compilation. No external libraries

---

## WHY SSE MATTERS (PRACTITIONER VIEW)

Many numerical failures are not *wrong math* — they are  
**right math in the wrong place**.

SSE adds one capability classical mathematics does not provide:

A deterministic way for mathematics to say:  
“I can compute this — but I cannot responsibly claim trust here.”

---

## ONE-MINUTE MENTAL MODEL

Classical mathematics asks:

“What is the result?”

Calculus asks:

“How does the result change?”

SSE asks:

“Should this result be trusted here at all?”

SSE does not modify equations.  
SSE governs whether mathematically correct results may responsibly claim trust.

---

## CORE STRUCTURAL IDEA (IN ONE LINE)

An equation may be correct everywhere —  
**but trusted only where structure permits.**

---

## GLOSSARY (FROZEN DEFINITIONS)

SSE attaches a structural triple to any computed value:

`E(x) = (y(x), a(x), s(x))`

where:

- `y` = classical value (unchanged)
- `a` = structural permission (admissibility)
- `s` = accumulated structural resistance (memory)

Collapse invariant:

`phi(E(x)) = y(x)`

or equivalently:

`phi((y, a, s)) = y`

Classical outputs are never altered.

---

## DENY vs ABSTAIN (CRITICAL DISTINCTION)

ABSTAIN:

- the expression or step is undefined in the current regime
- examples: NaN domain, singular normal matrix, undefined derivative
- meaning: “No admissible evaluation exists here.”

DENY:

- the expression is defined, but structurally inadmissible
- meaning: “A value exists, but trust is revoked.”

---

## SSE GOVERNANCE OUTCOMES

Each evaluation results in exactly one outcome:

- `ALLOW`
- `CONVERGED_ALLOW`
- `DENY`
- `ABSTAIN`

These outcomes are categorical, deterministic, and axiom-driven.

---

## SSE GOVERNANCE GATES

Gate 1 — Structural Undefinedness

If the equation or solver step is mathematically undefined  
(e.g., singular normal matrix, undefined derivative):

Outcome: `ABSTAIN`

Gate 2 — Structural Denial

If structural permission collapses  
or accumulated resistance exceeds safe bounds:

Outcome: `DENY`

Denial occurs before numeric catastrophe.

Gate 3 — Responsible Allowance

If structure remains admissible and stable:

Outcome: `ALLOW`

If convergence is structurally detected:

Outcome: `CONVERGED_ALLOW`

---

## GOVERNANCE PARAMETERS DISCLOSURE (NO HIDDEN TUNING)

SSE governance is controlled only by declared thresholds such as:

- `a_min` minimum admissible permission
- `s_max` maximum admissible resistance
- `cond_max` maximum acceptable conditioning posture
- `step_norm_max` maximum acceptable step magnitude
- `conv_step_tol` step tolerance for convergence
- `conv_imp_tol` improvement tolerance for convergence

No other hidden parameters influence outcomes.

---

## SSE OUTPUTS (WHAT YOU GET)

For each proof case, SSE produces:

- Classical trace (CSV)
- SSE trace (CSV)

Each iteration records:

- status
- structural permission `a`
- structural resistance `s`
- conditioning posture
- step magnitude
- improvement posture

Only trust status differs.  
Classical computation remains identical.

---

## QUICK RUN — CASE 1 (MGH17)

Structural Undefinedness (Abstain)

`python scripts\sse_case1_mgh17_solver_replay.py --in_csv data\mgh17_data.csv --start 1 --out_dir case1_abstain_singular`

Numeric Catastrophe Prevention (Deny)

`python scripts\sse_case1_mgh17_solver_replay.py --in_csv data\mgh17_data.csv --start 1 --damping 1e-3 --out_dir case1_deny_numeric`

Safe Convergence Allowance

`python scripts\sse_case1_mgh17_solver_replay.py --in_csv data\mgh17_data.csv --start 2 --out_dir case1_allow_converged --warmup_allow 12 --neg_imp_tol -1e9 --step_norm_max 1e9 --cond_max 1e30 --a_min 0.0 --s_max 1e9 --conv_step_tol 1e-4 --conv_imp_tol 1e-4`

---

## QUICK RUN — CASE 2 (CALCULUS)

Calculus linearization governance example:

`python scripts\sse_case2_calculus_linearization.py --fn sqrt --root .`

This generates:

- safe allowance far from instability
- deterministic denial near the boundary
- structural abstention at undefined regimes

No dataset is required.

---

## ONE-LINE SUMMARY

Shunyaya Structural Equations introduce deterministic, equation-level governance — allowing mathematics to abstain, deny, or responsibly allow trust, **without altering a single classical result**.
