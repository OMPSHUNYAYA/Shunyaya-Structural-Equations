# Case 1 — Structural SSE Behavior (Allow / Converged)

This folder contains the finalized and complete visualization set for  
**Case 1 — Allow / Converged**, the only scenario in Case 1 that produces a  
meaningful multi-iteration trajectory.

All plots in this folder describe the **same converged run** and together form  
a complete structural diagnostic of convergence behavior.

Single-iteration outcomes (**ABSTAIN**, **DENY**) are intentionally excluded  
to avoid misleading time-series visuals.

---

## Included Plots — Complete Convergence Diagnostics

### 1. SSE vs Iteration

Shows rapid structural collapse after the initial iteration, with SSE stabilizing  
near zero.

**Interpretation:**  
The system reaches a structurally admissible configuration almost immediately,  
confirming stable convergence.

---

### 2. Permission (`a`) vs Iteration

Tracks the permission signal relative to the admissibility threshold `a_min`.

**Interpretation:**  
Permission fluctuates early, then decisively crosses `a_min` only after  
structural stabilization — indicating **earned admissibility**, not premature  
acceptance.

---

### 3. Resistance (`s`) vs Iteration

Tracks resistance growth relative to `s_max`.

**Interpretation:**  
Resistance increases and saturates as the system approaches convergence,  
reflecting **structural stiffening rather than instability**.

---

### 4. Condition Number vs Iteration (Log Scale)

Shows numerical conditioning across iterations.

**Interpretation:**  
Conditioning improves and stabilizes without singular or explosive behavior,  
confirming numerical well-posedness throughout convergence.

---

### 5. Step Norm vs Iteration (Log Scale)

Tracks the magnitude of iterative updates.

**Interpretation:**  
Step norms decay exponentially, a clear signature of **true convergence**  
rather than oscillation or truncation.

---

## Notes on Excluded Case 1 Scenarios

### ABSTAIN_SINGULAR
Single-iteration termination due to structural singularity.

### DENY_NUMERIC
Single-iteration termination due to numeric inadmissibility.

These outcomes are documented via CSV summaries and diagnostics but are not  
suitable for time-series plotting.

---

## Status

✔ All five plots verified  
✔ Thresholds (`a_min`, `s_max`) respected  
✔ Convergence behavior internally consistent  
✔ Visualization frozen for release
