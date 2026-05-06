# Verification: Matsya Outputs vs. Source Paper

Reference: Gornemann, Kuester, and Nakajima (2012), Section 2, equations (1)–(4), Tables 1–2.

## What we accepted

**Three-perch ADC decomposition.** Matsya's split into arrival \((e_\text{old}, s_\text{old}, a, X)\), decision \((e, s, m, X')\), and continuation \((e, s, a', X')\) is structurally sound. The paper's Bellman equations (1) and (3) separate cleanly into a pure optimization over \(c\) (the backward mover \(\mathbb{B}\)) and an expectation over next-period shocks (the integration mover \(\mathbb{I}\)). We accepted this decomposition without modification.

**Mover placement.** Matsya correctly placed all stochastic transitions — employment, skill, TFP, monetary shock — in the arrival mover \(\mathbb{I}\), leaving the decision mover \(\mathbb{B}\) as a deterministic \(\max_c\). This matches the paper: consumption and saving are chosen *after* the household knows its employment status and the aggregate state (Section 2.2, Figure 1).

**EGM structure.** The inverse Euler equation, endogenous grid recovery, and envelope condition in the YAML's `cntn_to_dcsn_mover` follow directly from the CRRA first-order condition in equation (1) and are standard.

**Calibration block.** All parameter values (\(\sigma, \beta, \lambda, b, \alpha, \gamma, \rho_Z, \sigma_Z, \rho_D, \sigma_D, \rho_\Pi, \bar{\Pi}\)), the skill grid, and the \(4 \times 4\) transition matrix were verified against Tables 1 and 2 of the paper. However, **Matsya returned the skill transition matrix as a zero placeholder** — it could not retrieve the values from piped input — so we filled in the actual matrix from Table 2 by hand.

## What we edited

**Resource formation notation.** Matsya's first decomposition used the generic expression \(m = R(X')a + y(e,s,X')\). The paper uses mutual-fund shares, not a risk-free return. We corrected this to \(m = (p_a(X') + d_a(X'))a + y(e,s,X')\), matching the budget constraints in equations (2) and (4). Matsya's YAML draft (produced in a later call) used the correct notation.

**Shadow marginal value.** The `dcsn_to_arvl_mover` ShadowBellman carries the factor \((p_a + d_a)\) through the expectation. Matsya produced this correctly in the YAML, but it was absent from the initial plain-text decomposition. We added it to the improved markdown (Section 5.4).

**Timing of \(f(\tilde{X}')\).** Matsya's initial decomposition was ambiguous about whether the job-finding rate is evaluated at the pre-transition or post-transition aggregate state. The paper is explicit: \(f\) is a function of \(\tilde{X}'\) (the pre-transition state of the next period), not \(X'\). The YAML records the employment transition as `P_e(e_old, X)`, which conflates the two. The improved markdown and the YAML comments clarify that the argument is \(\tilde{X}'\).

**Wage and tax in income function.** The YAML's `arvl_to_dcsn_transition` correctly uses `w(X_prime) * s * (1 - tau(X_prime))` for employed income. We verified this against equation (2): \(y(1,s,X) = w(X)s(1-\tau(X))\). The use of `X_prime` in the YAML (vs. \(X\) in the paper) reflects the stage decomposition's timing convention, where the decision-stage aggregate state has already been relabeled as \(X'\).

## What we rejected or flagged

**Piped-content retrieval.** Matsya's vector-store retrieval never ingested the piped excerpt. Across three attempts it returned only internal dolo-plus spec documents. This means Matsya's equations were reconstructed from conversation context and its training data, not directly from the paper. All equations were therefore cross-checked against the source before acceptance.

**Generic `H(X, Z', D')` law of motion.** The YAML uses a black-box `H` for the aggregate transition. The paper solves this via Krusell-Smith log-linear forecasting rules (Appendix B), but does not give a closed-form \(H\) in the main text. We accepted `H` as a placeholder and noted the approximation method.

**Grid settings.** Matsya proposed `n_a = 200`, `a_max = 500.0`, `n_X = 3` as computational settings. These are reasonable defaults but are not from the paper (which does not report grid sizes in the main text). We kept them as placeholders in the YAML `settings` block.
