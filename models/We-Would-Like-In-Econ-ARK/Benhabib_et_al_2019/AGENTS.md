# Ballpark entry: Benhabib, Bisin, and Luo (2019)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing content lives in [`index.md`](index.md).

## Paper

- **Citation:** Benhabib, Bisin, and Luo (2019), "Wealth Distribution and Social Mobility in the US: A Quantitative Approach," *American Economic Review* 109(5), 1623–1647.
- **DOI:** [10.1257/aer.20151684](https://doi.org/10.1257/aer.20151684)
- **Core model:** Finite-lifetime consumption-savings with warm-glow bequest at $T$; no within-life shocks; heterogeneous $(r, w)$ drawn once per dynasty.
- **Why in-ballpark:** Canonical example of heterogeneous-returns driving the wealth tail — a headline result in modern HA macro.

## If a user asks to work on this item

1. **Read first:** [`bellman-excerpt.md`](bellman-excerpt.md) — the modular-DDSL Bellman statement with comprehensive symbol table, perch decomposition, stage operators, and EGM channel. This is the authoritative formalization input; a YAML-drafting agent should read this before touching the notebooks.
2. **For economic context beyond the formalization:** `Benhabib_et_al_2019_summary.ipynb` → "The Model".
3. **Paper source for AI ingestion:** `Benhabib_et_al_2019.mmd` (Pandoc-converted). Prefer this over `Benhabib_et_al_2019.pdf`.

## Formalization status

- Explicit recursive formulation: **present** in `_summary.ipynb`.
- `bellman-excerpt.md`: **committed and iterated with Matsya**. After the Improve step, reflects matsya's recommended patterns (identity forward mover idiom; terminal boundary wiring; calibration-override family; corrected terminal-FOC discussion).
- `dolo-plus-draft.yaml`: **committed (first Matsya draft)**. Canonical stage structure; two speculative blocks (`terminal:`, `calibration_family:`) preserved with `# SPECULATIVE` flags intact per matsya's advisory.
- `verification.md`: **committed**. Compares the YAML against the paper's §I; paper's description is sufficient; remaining gaps are dolo-plus spec gaps, not paper gaps.
- `matsya-session.txt`: **committed** (`topics2026-benhabib-demo`).

## Known model features requiring attention in a formalization pass

- **Perch-ready notation convention.** The recursive problem in `_summary.ipynb` → "The Model" → "Recursive Formulation" uses an explicit, perch-ready convention: $a_t$ = beginning-of-period wealth; $m_t \coloneqq (1+r)a_t + w_t$ = cash-on-hand at the decision perch; $a_{t+1} = m_t - c_t$ = savings identity. The paper's own compact statement ($a' = (1+r)a - c + w$ with $0 \le c \le a$) carried an `a`-double-role ambiguity; the notebook's current rewrite resolves it. **A formalizer should build on the notebook's convention, not re-derive from the paper.**
- **Terminal period under-specified.** Warm-glow $e(a_T) = A a_T^{1-\mu} / (1-\mu)$ is stated, but the budget at $T$ is left implicit (is there a $w_T$? does $e$ apply to savings or to post-return assets?). A complete formalization must resolve this explicitly.
- **Dynasty-level heterogeneity** is the paper's distinguishing feature: $(r, w)$ fixed within a life, stochastic across generations. A single-agent lifecycle YAML is not sufficient to reproduce the paper's tail-thickness result — you need a dynasty-level wrapper or a parameterized family indexed by $(r, w)$ draws.
- **Age profile $w_t$** should not flatten to a scalar `w` in the YAML. The period template needs age-varying wage overrides.
- **Stochastic return process.** $r^n$ is a **finite 5-state Markov chain** in the paper's baseline, with off-diagonal probabilities that decay geometrically away from the diagonal (except the last row, which uses constant off-diagonals); see paper §I and footnote 13. A simple AR(1) or lognormal shock does **not** capture the paper's specification — the YAML's `exogenous` block must accommodate the Markov-chain structure. See `_summary.ipynb` → "The Model" → "Stochastic Structure" for the full specification.
- **Wealth-dependent return (Section IIID extension).** The paper considers an optional extension in which the Markov state space of $r^n$ depends on the agent's initial wealth $a_1$. Improves fit; a complete formalization should note this as an alternative stage structure rather than silently baking in the independence assumption.

## Common next tasks (grounded)

1. **Produce the formalization layer** (`bellman-excerpt.md`, `dolo-plus-draft.yaml`, `verification.md`, `matsya-session.txt`) from the recursive formulation in `_summary.ipynb`, via the Matsya iteration loop described in the repo-root `CONTRIBUTING.md`.
2. **Add the terminal-period stage** to the YAML (warm-glow closure).
3. **Formalize the dynasty wrapper** — type-indexed family over $(r, w)$ draws.
4. **Convert figures to alt-text-annotated MyST directives** for accessibility and LLM legibility.

## Workflow reminders

- **Matsya session:** use the course convention `topics2026-<slug>` for new work on this item.
- **Paper verification:** Matsya output must be checked against the paper PDF (or `.mmd`), not only against the ballpark `_summary.ipynb` — the notebook is a summary with known simplifications.
- **When flagging workarounds in YAML:** use inline `# workaround:` or `# unresolved:` comments rather than silently fudging non-canonical syntax.
