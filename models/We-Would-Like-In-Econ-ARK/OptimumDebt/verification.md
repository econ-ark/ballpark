# Verification: Matsya Output vs. the Published Paper

This document verifies the formalization-layer artifacts in this item
(`bellman-excerpt.md`, `dolo-plus-draft.yaml`) against the published
paper, **Aiyagari & McGrattan (1998), "The Optimum Quantity of Debt,"
*Journal of Monetary Economics* 42**. Page/section references below are
to the paper itself, not to `OptimumDebt_summary.ipynb`.

## Accepted

- **Perch structure (Model A).** Arrival $(\tilde{a}, e)$ → decision
  $(\tilde{m}, e)$ with consumption control → continuation $\tilde{a}'$
  faithfully represents the paper's Sec. II timing: productivity is
  realized at the beginning of the period, the budget (paper eq. 1)
  builds cash-on-hand, and end-of-period assets are determined
  residually after consumption.
- **EGM inversion recipe.** The paper itself solves Model B by
  penalty-function / finite-element on the residual of the FOC (paper
  Sec. III, eq. 5–6) rather than by EGM; so "acceptance" here means
  accepting that EGM is a *valid alternative* solution method for the
  Model A stage. The Inverse Euler, the envelope condition, and the
  Markov forward expectation used in `bellman-excerpt.md` §§4–5 are
  consistent with the paper's Euler equation after the $(1+g)$ factor
  is restored (see "Edited" below).
- **Stage-external treatment of prices and fiscal instruments.** The
  household block in paper Sec. II takes $(r, \tilde w, \tau)$ as
  given — general-equilibrium closure (firm FOCs, government budget,
  market clearing; paper Sec. II after eq. 1) lives *outside* the
  stage. `bellman-excerpt.md` §9 and the YAML's `parameters:` block
  reflect this partial-equilibrium convention.
- **Penalty formulation rejected from the formal DP.** The cubic
  penalty terms in the paper's Sec. III objective, eq. (5), are
  correctly identified as a solver-level device for enforcing
  $\tilde{a} \ge 0$ and $l \in [0,1]$ numerically. The formal DP in
  `bellman-excerpt.md` §10 uses the hard constraints; the penalty
  version is quarantined in `OptimumDebt_summary.ipynb` Section III.

## Edited

- **$(1+g)$ growth factor in the decision-to-continuation transition.**
  The paper's budget (Sec. II, eq. 1) is
  $\tilde{c}_t + (1+g)\,\tilde{a}_{t+1} \le (1+r)\tilde{a}_t + \tilde w\, e_t - \tau$.
  Matsya's first YAML draft wrote
  `a_prime = m_tilde - c_tilde`, silently dropping the $(1+g)$ factor,
  and `bellman-excerpt-improved.md` (now consolidated into
  `bellman-excerpt.md`) had carried the same drop into §§3–5. The
  adopted resolution restores the factor throughout:
  - `dolo-plus-draft.yaml` dcsn_to_cntn_transition:
    `a_prime = (m_tilde - c_tilde) / (1 + g)`;
  - EGM reverse transition:
    `m_tilde[>] = (1 + g) * a_prime + c_tilde[>]`;
  - InvEuler:
    `c_tilde[>] = (beta_tilde * dV[>] / (1 + g))^(-1/nu)`
    (the $1/(1+g)$ factor comes from $\partial \tilde a'/\partial \tilde c = -1/(1+g)$ in the FOC);
  - `bellman-excerpt.md` §§3–5 and §10.6 updated in parallel.

  The alternative — absorbing $(1+g)$ into an effective discount factor
  and rescaling the poststate — is defensible but would require a
  `# workaround:` comment in the YAML. Keeping the paper's notation
  verbatim was judged to be cleaner.

- **Finite Markov chain $\Pi$ for $e$.** The paper does *not* pin down
  the transition matrix in the recursive statement (Sec. II); it is
  calibrated from an AR(1) Tauchen discretization in Sec. IV (paper
  p. 458). `dolo-plus-draft.yaml` declares `N_e: 7` without committing
  to a specific $\Pi$; this is an explicit modeling choice of the
  formalizer (matching the paper's calibration size), not a feature of
  the paper's Sec. II DP.

- **$\tilde{\beta} < 1$ restriction.** Required for the contraction
  mapping but not stated in the paper's recursive-form introduction
  (it is implicit in the paper's calibrated $\nu = 1.5$, $g = 0.0186$,
  $\beta \approx 0.96$). Added explicitly in `bellman-excerpt.md` §1
  as a derived restriction on primitives.

## Rejected

- **Penalty-function objective (paper Sec. III, eq. 5).** The cubic
  penalty terms $\zeta \cdot \min(\tilde{a}, 0)^3$ and
  $\zeta \cdot \min(1-l, 0)^3$ are a numerical device for the finite-
  element residual method; they are not part of the formal DP and are
  deliberately excluded from `bellman-excerpt.md` and the YAML. The
  formal DP uses the hard inequality constraints stated in
  `OptimumDebt_summary.ipynb` §II.A/§II.B.

- **Residual equation $R(x, i; \alpha)$ (paper Sec. III, eq. 6).**
  This is a solver-level object (the approximation error of a
  parametric policy $\alpha^h$); it is correctly kept out of the
  formal DP.

- **Nothing in Model B as "same stage template" was rejected.**
  Treating Model B's perch structure as identical to Model A's — only
  the control dimension at the decision perch and the labor-income
  term in the budget change — is faithful to the paper's Sec. III.A
  presentation.
