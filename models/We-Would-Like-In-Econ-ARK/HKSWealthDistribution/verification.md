# Verification — HKS (2018) ballpark item

One-paragraph summary per CONTRIBUTING.md, expanded into three subsections so reviewers can see the paper-vs-representation split explicitly. This file supersedes `source/verification_paragraph.md` (kept in place as provenance), and accompanies the top-level composition manifest `dolo-plus-draft.yaml`.

## Accepted from Matsya (faithful to the paper)

The two-stage decomposition of each HKS period into (i) a consumption stage with a single decision over end-of-period assets $a$ and (ii) a shock-resolution stage that draws $(p', \beta', \nu', \eta')$ and forms $x'$ deterministically is accepted as faithful to the paper's timing — the arrival mover of the consumption stage is the identity (no within-stage shocks), and the shock-resolution stage has no decision, consistent with the paper's statement that the household observes $(x_t, p_t, \beta_t)$ at the decision node and uncertainty about next period's persistent states and transitory shocks is integrated in the continuation value. The individual-states-vs-aggregate-prices split (individual states $(x, p, \beta)$; individual control $a$; idiosyncratic shocks $(p', \beta', \nu', \eta')$; aggregate prices $(w, r)$; fiscal objects $(\tau(\cdot), \tilde\tau, T)$; return schedules $(r^X(\cdot), \sigma^X(\cdot))$) is accepted. The period operator $\mathbb{T}_t = \mathbb{B}^{\text{cons}} \circ \mathbb{B}^{\text{shock}}$ composes correctly to the original HKS recursion; this was verified by expanding the composition algebraically against paper §§4.2–4.3.

Calibration values added to `bellman-excerpt.md` and `source/HKS_bellman_stages.md` §7 (benchmark $\gamma, \alpha, \delta, \underline{a}, \chi, \lambda, \phi, \mu_\beta, \rho_\beta, \sigma_\beta$, and the Table-8 portfolio schedule across 13 wealth-percentile bins) were cross-checked directly against the paper Sections 6.1–6.5 and Appendix A / Appendix C.

## Unresolved in representation (dolo-plus-spec gaps)

Five items remain unresolved in the YAML drafts (`source/hks_consumption.yaml`, `source/hks_shock_resolution.yaml`; see `bellman-excerpt.md` §7 for the flag-by-flag catalogue). Each is a design decision forced by the current dolo-plus specification, not by HKS:

1. Stochastic-$\beta_t$-as-state treatment (non-standard; dolo-plus canonical idiom treats $\beta$ as scalar).
2. Function-valued $\tau(\cdot), r^X(\cdot), \sigma^X(\cdot), \psi(\cdot)$ (no canonical lookup-table idiom in dolo-plus spec).
3. Aggregate-price treatment (partial equilibrium is a YAML scope decision; full equilibrium / transition paths would need `exogenous` time series).
4. EGM feasibility under wealth-dependent returns (the envelope condition is not cleanly invertible; first-pass YAML will omit `InvEuler` / `MarginalBellman`).
5. Inter-stage and inter-period value-function wiring (mechanically clear in `bellman-excerpt.md` §4; needs a canonical two-stage composition idiom in dolo-plus).

These are flagged canonically in `dolo-plus-draft.yaml` with `# workaround:` (items 1, 3) or `# unresolved:` (items 2, 4, 5), and — after the retag task in `AGENTS.md` → "Common next tasks" — in the stage-level YAMLs themselves.

## Dolo-plus-spec gaps, not paper gaps

The top-level `dolo-plus-draft.yaml` declares the two stages, the inter-stage and inter-period value-function wiring, and the shared scalar calibration, but is explicitly **not executable**. Every remaining issue in that file, and in the two stage-level YAMLs under `source/`, is a *dolo-plus specification* gap, in the following precise sense:

- *The paper specifies the object.* Each of the five open issues in `bellman-excerpt.md` §7 points to a paper construction that is fully pinned down in HKS (2018) §§4.2–4.3 and §§6.1–6.5 and Appendices A and C. Where the paper defers — $\rho_P, \sigma^P_t, \sigma^T_t$ to Heathcote, Storesletten, and Violante (2010); $\kappa_t$ to Piketty and Saez (2003); $\tau_t(\cdot)$ to Piketty and Saez (2007); $\tilde\tau_t$ to U.S. Treasury (2016); portfolio schedules to Bach et al. (2015); aggregate excess returns to Jordà et al. (2017) and Kartashova (2014) — the deferral is to explicit external sources, not to under-specification.
- *The dolo-plus spec does not yet have a canonical idiom for that object.* The blockers are: stochastic $\beta_t$ as a Markov state multiplying the continuation value (flagged `# workaround:`); function-valued tabulated schedules $\tau(\cdot), r^X(\cdot), \sigma^X(\cdot), \psi(\cdot)$ (flagged `# unresolved:`); the partial-equilibrium-vs-exogenous-path treatment of aggregate prices (flagged `# workaround:`); EGM feasibility under wealth-dependent returns (flagged `# unresolved:`; the Euler inversion is not obviously well-posed); and an explicit two-stage composition and inter-period wiring idiom (flagged `# unresolved:`).
- *Hence a formalizer picks up this item without needing to contact the paper's authors, re-read the paper for under-specified prose, or make economic judgement calls.* All remaining choices are about which dolo-plus idioms to use for objects HKS already fixes. Each such choice is flagged, in `dolo-plus-draft.yaml` itself, with `# workaround:` (a non-standard representation we are willing to commit to) or `# unresolved:` (a representation question we do not yet have a good answer to), so downstream reviewers can distinguish the two.

The faithful economic content of the two-stage decomposition is the subject of the "Accepted from Matsya" subsection above; this subsection only certifies that the residual representation work is *representation work*, not paper interpretation.

## Session

Matsya interactions for this item used `--session topics2026-improve-hks-wealth-distribution-rubyzheng`; the full server-side thread is inspectable under that session name. See `matsya-session.txt`.
