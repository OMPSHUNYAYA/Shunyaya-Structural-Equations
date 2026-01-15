# Case 2 — Structural Corridor Behavior (Plots)

This folder contains the finalized reference visualization for  
**Case 2 — Allow / Safe Corridor**.

Case 2 explores **corridor-based structural admissibility** across different  
function families (reciprocal and square-root), testing how permission (`a`)  
and resistance (`s`) evolve relative to fixed thresholds.

Only the **allow–safe corridor** scenario is included as a visual reference.  
Other outcomes (**ABSTAIN**, **DENY**) are intentionally excluded from plotted  
upload to avoid redundancy and visual noise.

All scenarios are fully reproducible using the provided plotting script.

---

## Included Plot (Reference Only)

### recip_allow_safe_corridor

This scenario is selected because it demonstrates the **canonical safe corridor  
behavior** most clearly.

---

### 1. Permission (`a`) vs `k`

Shows permission remaining consistently above the admissibility threshold `a_min`.

**Interpretation:**  
The system remains structurally admissible across the entire corridor.  
No instability or boundary violation occurs.

---

### 2. Resistance (`s`) vs `k`

Shows resistance remaining near zero and well below `s_max`.

**Interpretation:**  
No structural stress accumulates.  
The corridor is numerically and structurally safe.

---

### 3. Text Summary

Displays the first rows of the trace in tabular form.

**Interpretation:**  
All rows are marked **ALLOW**, with extremely small approximation error.  
This confirms safe structural behavior without relying on visual inference alone.

---

## Notes on Other Case 2 Scenarios (Not Plotted)

The following scenarios were executed, verified, and frozen, but are not  
included as uploaded plots:

### Reciprocal family

- **ABSTAIN — Instability Corridor**  
  Permission collapses and resistance spikes near singular regions.

- **DENY — Boundary Corridor**  
  Permission crosses below `a_min` and/or resistance exceeds `s_max`.

---

### Square-root family

- **ABSTAIN — Instability Corridor**  
  Structural undefined regions correctly trigger abstention.

- **ALLOW — Safe Corridor**  
  Stable, flat permission and zero resistance across the domain.

- **DENY — Boundary Corridor**  
  Clean threshold crossing produces deterministic denial.

These outcomes are summarized numerically via text diagnostics and are not  
suitable for upload as standalone plots.

---

## Reproducibility

All Case 2 plots (including **ABSTAIN** and **DENY** cases) can be regenerated using:

`python scripts/plot_sse_case2.py --case2_root "." --a_min 0.7 --s_max 0.8 --r_safe 0.15`

The script automatically:

- detects scenario folders
- creates `plots/` directories as needed
- generates either plots or text summaries depending on trace length

---

## Status

✔ All Case 2 scenarios verified  
✔ Threshold logic validated  
✔ Representative plot selected  
✔ Redundant plots excluded  
✔ Visualization frozen for release
