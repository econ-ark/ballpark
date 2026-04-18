# Ballpark entry: Benhabib, Bisin, and Luo (2019)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing content lives in [`index.md`](index.md).

## Paper

- **Citation:** Benhabib, Bisin, and Luo (2019), "Wealth Distribution and Social Mobility in the US: A Quantitative Approach," *American Economic Review* 109(5), 1623–1647.
- **DOI:** [10.1257/aer.20151684](https://doi.org/10.1257/aer.20151684)
- **Core model:** Finite-lifetime consumption-savings with warm-glow bequest at $T$; no within-life shocks; heterogeneous $(r, w)$ drawn once per dynasty.
- **Why in-ballpark:** Canonical example of heterogeneous-returns driving the wealth tail — a headline result in modern HA macro.

## If a user asks to work on this item

1. **Read first:** `Benhabib_et_al_2019_summary.ipynb` → section "The Model" → Recursive Formulation. This is the authoritative recursive statement; do not re-derive from the PDF.
2. **Paper source for AI ingestion:** `Benhabib_et_al_2019.mmd` (Pandoc-converted). Prefer this over `Benhabib_et_al_2019.pdf`.
3. **Prior formalization attempt (external to this repo):** see [`workspace-course-topics/artifacts/matsya-workflow-example-benhabib-2019/`](https://github.com/llorracc/workspace-course-topics/tree/main/artifacts/matsya-workflow-example-benhabib-2019) for an instructor worked-example that produced a stage decomposition, SMD-polished excerpt, and an interior-period dolo-plus YAML draft. **Those artifacts have not been committed to this ballpark directory.**

## Formalization status

- Explicit recursive formulation: **present** in `_summary.ipynb`.
- `bellman-excerpt.md`: **not committed**. A candidate exists in the external workspace (see above).
- `dolo-plus-draft.yaml`: **not committed**. An interior-period draft exists in the external workspace.
- `verification.md`: **not committed**.
- `matsya-session.txt`: **not committed**. The external instructor demo used session `topics-instructor-benhabib2019-matsya-demo`.

## Known model features requiring attention in a formalization pass

- **Notebook uses `a` ambiguously** (raw assets vs. cash-on-hand). The instructor demo resolved this by introducing $m \coloneqq (1+r)a_{\prec} + w_t$ as the decision-perch state. Any YAML must distinguish prestate `a` from poststate `a` (e.g. `a_prev` / `a`) — the raw YAML from the demo conflates them.
- **Terminal period under-specified.** Warm-glow $e(a_T) = A a_T^{1-\mu}/(1-\mu)$ is stated, but the budget at $T$ is left implicit (is there a $w_T$? does $e$ apply to savings or to post-return assets?). A complete formalization should resolve this explicitly.
- **Dynasty-level heterogeneity** is the paper's distinguishing feature: $(r, w)$ fixed within a life, stochastic across generations. A single-agent lifecycle YAML is not sufficient to reproduce the paper's tail-thickness result — you need a dynasty-level wrapper or a parameterized family indexed by $(r, w)$ draws.
- **Age profile $w_t$** should not flatten to a scalar `w` in the YAML. The period template needs age-varying wage overrides.

## Common next tasks (grounded)

1. **Commit the formalization layer** (`bellman-excerpt.md`, `bellman-excerpt-SMD-polished.md`, `dolo-plus-draft.yaml`, `verification.md`) from the external instructor demo, cleaned up per CONTRIBUTING.md.
2. **Add the terminal-period stage** to the YAML (warm-glow closure).
3. **Formalize the dynasty wrapper** — type-indexed family over $(r, w)$ draws, analogous to HAFiscal's $(\beta_i, e)$ pattern.
4. **Convert figures to alt-text-annotated MyST directives** for accessibility and LLM legibility.

## Workflow reminders

- **Matsya session:** use the course convention `topics2026-<your-slug>` for new work on this item (not the instructor's demo session name, which is retained for provenance).
- **Paper verification:** Matsya output must be checked against the paper PDF (or `.mmd`), not only against the ballpark `_summary.ipynb` — the notebook is a summary with known simplifications.
- **When flagging workarounds in YAML:** use inline `# workaround:` or `# unresolved:` comments rather than silently fudging non-canonical syntax.
