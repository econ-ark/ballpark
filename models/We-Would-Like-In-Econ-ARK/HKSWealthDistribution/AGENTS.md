# Ballpark entry: Hubmer, Krusell, and Smith (2018)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing content lives in the four exposition notebooks (and in an `index.md` still to be produced).

## Paper

- **Citation:** Hubmer, J., Krusell, P., and Smith, A. A. Jr. (2018 working paper; 2021 published), "Sources of U.S. Wealth Inequality: Past, Present, and Future," *NBER Macroeconomics Annual* 35.
- **DOI:** [10.1086/712332](https://doi.org/10.1086/712332)
- **Core model:** Infinite-horizon Bewley–Huggett–Aiyagari household with CRRA utility, stochastic Gaussian-AR(1) discount factor, persistent + transitory earnings, wealth-dependent mean and idiosyncratic-volatility return schedules (reduced form of a 4-asset-class portfolio), progressive income tax + flat capital-gains tax + lump-sum transfer. Single control: end-of-period assets.
- **Why in-ballpark:** First quantitative HA theory that jointly accounts for the U.S. wealth distribution *and* its 1967–2012 dynamics via portfolio heterogeneity and declining tax progressivity; its wealth-dependent return schedules are a natural extension target for HARK's Markov-chain exogenous-state machinery.

## If a user asks to work on this item

1. **Read first:** `bellman-excerpt.md` — the canonical modular-DDSL statement (symbol table, timing, two-stage perch decomposition, dolo-plus-spec open issues). For full-form math and Table-8 portfolio-schedule data, see `source/HKS_bellman_excerpt.md`.
2. **Paper source for AI ingestion:** `source/hubmerkrusellsmith_wealth2018/hubmerkrusellsmith_wealth2018.tex` (Pandoc-converted from `hubmerkrusellsmith_wealth2018.pdf`; prefer over the PDF).

## Formalization status

- Explicit recursive formulation: present in `HKSWealthDistribution_summary.ipynb` and `bellman-excerpt.md`.
- `bellman-excerpt.md`: committed (root-level canonical version synthesized from `source/HKS_bellman_excerpt.md` + `source/HKS_bellman_stages.md`).
- `dolo-plus-draft.yaml`: committed at root as a conservative composition manifest aligned with the dolo-plus spec `05-periods-models.md` (period-level keys `name`, `stages`, optional `connectors`; canonical `# workaround:` / `# unresolved:` flags). Two-stage drafts remain at `source/hks_consumption.yaml` and `source/hks_shock_resolution.yaml` as provenance.
- `verification.md`: committed (root-level; expansion of `source/verification_paragraph.md`).
- `matsya-session.txt`: committed.

## Known model features requiring attention in a formalization pass

Each is a **dolo-plus-spec representation gap**, not a paper gap — see `verification.md` for the distinction.

- **Stochastic $\beta_t$ as a Markov state.** Canonical dolo-plus treats $\beta$ as a scalar parameter; here it is a Gaussian-AR(1) state multiplying the continuation value. The draft YAMLs encode it as state `b`. Design choice with no canonical precedent.
- **Function-valued aggregates $\tau(\cdot), r^X(\cdot), \sigma^X(\cdot), \psi(\cdot)$.** The paper uses 11-bracket tax schedules, 13-bin wealth-percentile portfolio tables (Bach 2015), and a piecewise-Pareto labour-efficiency map. Dolo-plus has no canonical lookup-table idiom; parametric approximations or explicit tabulation are needed.
- **EGM feasibility under wealth-dependent returns.** $r^X(a), \sigma^X(a)$ break the standard Euler-inversion envelope. First-pass YAML should omit `InvEuler`/`MarginalBellman` blocks pending analysis.
- **Aggregate-price treatment.** Partial equilibrium is the YAML's scope; general equilibrium and transition experiments (time-varying $\sigma^P_t, \sigma^T_t, \kappa_t, \bar r_{c,t}, \tau_t, \tilde\tau_t$) are out of scope.
- **Inter-stage and inter-period value-function wiring.** Mechanically clear (see `bellman-excerpt.md` §4), but needs a canonical YAML idiom for two-stage composition; currently marked `# TODO` in `source/` drafts, to be retagged `# unresolved:` during YAML consolidation.

## Common next tasks (grounded)

1. Period-level `wiring:` → `connectors:` alignment is **done** in `dolo-plus-draft.yaml` (per dolo-plus spec `05-periods-models.md`). Remaining follow-up tasks at the formalization layer: (i) resolve the rename convention between stage boundary variables — either rename the `hks_consumption` poststates to bare names `(a, p, b)` so the intra-period connector becomes identity and is omitted per spec, or keep the `_cntn` suffix and carry an explicit `rename:` map in the period file's `connectors:` block; (ii) if future work continues, write the nest-level twister file that wires `hks_shock_resolution.continuation` → next-period `hks_consumption.arrival`. Separately, retag any remaining `# PLACEHOLDER` / `# TODO` markers in the two `source/` stage files with canonical `# workaround:` / `# unresolved:` flags keyed to `bellman-excerpt.md` §7.
2. Add the portfolio-heterogeneity + zero-earnings-state + stochastic-$\beta$ paragraph to `HKSWealthDistribution_summary.ipynb` → "The Model" (these are currently only in `bellman-excerpt.md`).
3. Add Bach et al. (2015) as the empirical anchor in `HKSWealthDistribution_prior-literature.ipynb`; trim the prior-literature list to the 3–6 range.
4. Add the 3-sentence in-ballpark pitch to `HKSWealthDistribution_intro.ipynb`; remove the self-addressed Note cell.
5. Produce an `index.md` with CONTRIBUTING's required JSON-LD frontmatter.

## Workflow reminders

- **Matsya session:** use `topics2026-improve-hks-wealth-distribution-rubyzheng` for every call on this item (content of `matsya-session.txt`); do not open a new session.
- **Paper verification:** Matsya output must be checked against `hubmerkrusellsmith_wealth2018.pdf` (or `.tex`), not only against the ballpark summary notebook.
- **When flagging workarounds in YAML:** use inline `# workaround:` or `# unresolved:` comments rather than silently fudging non-canonical syntax.
