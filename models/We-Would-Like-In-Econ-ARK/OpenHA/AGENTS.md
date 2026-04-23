# Ballpark entry: Auclert, Rognlie, Souchier, and Straub (2021)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing content lives in [`index.md`](index.md).

## Paper

- **Citation:** Auclert, Adrien; Rognlie, Matthew; Souchier, Martin; and Straub, Ludwig (2021), "Exchange Rates and Monetary Policy with Heterogeneous Agents: Sizing up the Real Income Channel," NBER Working Paper 28872.
- **DOI:** [10.3386/w28872](https://doi.org/10.3386/w28872) · also on [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3856853).
- **Core model:** Small-open-economy New Keynesian model with a heterogeneous-agent, incomplete-markets household block. Households hold a single real asset $a$ subject to a borrowing limit and face uninsurable idiosyncratic productivity $e_{it}$ following a first-order Markov chain. The household's only decision-perch control is aggregate real consumption $c_t$ (the CES home/foreign split is mechanical given relative prices; hours $N_t$ are union-set); savings follow from the budget identity $a_{t+1} = m_t - c_t$.
- **Why in-ballpark:** The paper's central decomposition, $d\mathbf{C} = -\tfrac{\alpha}{1-\alpha}\mathbf{M}\,d\mathbf{Q} + \mathbf{M}\,d\mathbf{Y}$, rests on the matrix $\mathbf{M}$ of intertemporal MPCs — exactly the sequence-space Jacobian object HARK's incomplete-markets household block already exposes. OpenHA is therefore the cleanest open-economy mapping for HARK.

## If a user asks to work on this item

1. **Read first:** [`bellman-excerpt.md`](bellman-excerpt.md) — SolvingMicroDSOPs-style three-stage decomposition (`shocks-only` → `cons-noshocks` → `disc`) with explicit perch table, InvEuler / endogenous-grid channel, and between-period connector $a_{t+1} = \psi_t$. This is the authoritative modular-DDSL statement; the `OpenHA_summary.ipynb` "Domestic (Brazil) households" section is its prose counterpart and matches it on effective controls, cash-on-hand definition, and borrowing-limit handling.
2. **Then:** [`OpenHA_summary.ipynb`](OpenHA_summary.ipynb) → "The model" for the broader closure (foreign demand, production, financial sector, unions, monetary policy, and the three channels).
3. **Paper source for AI ingestion:** neither `OpenHA.mmd` (Pandoc-converted paper) nor `OpenHA.pdf` is yet committed in this directory. Use the paper at <https://web.stanford.edu/~aauclert/ha_oe.pdf> (DOI `10.3386/w28872`) as the authoritative source, and treat completing the asset layer as one of the "Common next tasks" below.

## Formalization status

- Explicit recursive formulation: **present** in `OpenHA_summary.ipynb` → "Domestic (Brazil) households" (effective control $c$; cash-on-hand $m_t$; productivity $e_{it}$ as a Rouwenhorst-discretized AR(1) Markov chain; borrowing limit $\underline{a}$).
- [`bellman-excerpt.md`](bellman-excerpt.md): **committed** (product of the Matsya iteration loop, SolvingMicroDSOPs-polished).
- [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml): **committed** (household consumption-savings stage; YAML hand-constructed from Matsya's perch decomposition because Matsya's direct YAML generator timed out — see `verification.md`).
- [`verification.md`](verification.md): **committed**.
- [`matsya-session.txt`](matsya-session.txt): **committed** — session `topics2026-siying99-ballpark`.

## Known model features requiring attention in a formalization pass

- **Aggregate block not yet formalized.** `dolo-plus-draft.yaml` covers only the household consumption-savings stage. The aggregate closure — home-goods market clearing, wage Phillips curve, real UIP, Taylor-type monetary rule, CES expenditure shares as general-equilibrium price blocks — is stated verbally in `OpenHA_summary.ipynb` but has no modular-DDSL or YAML counterpart. Adding an aggregate scaffold is prerequisite for any end-to-end HANK replication.
- **Terminal-period stage not declared.** `dolo-plus-draft.yaml` is written for an infinite-horizon stationary problem but does not mark it as such; a formalizer consuming this YAML should either add a terminal-period stage or an explicit `horizon: infinite-stationary` preamble. Recorded as an intentional omission.
- **Calibration placeholders.** The values in `dolo-plus-draft.yaml` (`w: 1.0`, `N: 1.0`, `r: 0.04`, `a_bar: 0.0`, `rho_e: 0.95`, `sigma_eps: 0.1`) are generic fillers, not the paper's calibration. Replace with either the paper's values or symbolic pointers into the aggregate block.
- **Productivity process added by formalizer, not stated in ballpark prior to this pass.** The original ballpark notebook did not specify the stochastic structure of $e_{it}$. As documented in `verification.md`, this was **edited in** from the paper, which states a first-order Markov chain with $\mathbb{E}\,e_{it}=1$, calibrated as an AR(1) in log income and discretized (Rouwenhorst). A formalizer should treat `OpenHA_summary.ipynb` as the ballpark's current statement of this process.
- **Matsya YAML-generation timeout.** Matsya's direct YAML generator repeatedly timed out on the server during this pass; `dolo-plus-draft.yaml` was therefore constructed by hand from Matsya's perch-decomposition output. Re-running the YAML generator after upstream fixes is a latent task.

## Common next tasks (grounded)

1. **Add a terminal-period stage or horizon preamble to `dolo-plus-draft.yaml`.** Either append a terminal-period specification or prepend an explicit `horizon: infinite-stationary` note — referenced directly in the "Known features" list above.
2. **Replace generic calibration placeholders in `dolo-plus-draft.yaml`** (`w: 1.0`, `N: 1.0`, `r: 0.04`, `rho_e: 0.95`, `sigma_eps: 0.1`, etc.) with the paper's calibrated values or symbolic pointers to the aggregate block. The paper's calibration table (Brazil vs. US) is the source.
3. **Draft an aggregate/GE scaffold** (new file, e.g. `aggregate-scaffold.md`) stating the home-goods market clearing, wage Phillips curve, real UIP, and monetary rule in modular-DDSL form, so the household YAML can be wired into a closed model. Do not attempt this inside `dolo-plus-draft.yaml`; keep stages modular.
4. **Complete the asset layer.** Place `OpenHA.pdf` in this directory (if license permits; otherwise retain a DOI-only pointer) and add a Pandoc-converted `OpenHA.mmd` alongside it, per the `CONTRIBUTING.md` asset-layer requirements.
5. **Re-run Matsya `evaluate` on `bellman-excerpt.md`** in session `topics2026-siying99-ballpark` once the above items land, to confirm no further missing elements (productivity process, union-set hours, effective-control reduction are now all explicit). Record the outcome in `verification.md`.
6. **Retry Matsya YAML generation** (which previously timed out) against the polished `bellman-excerpt.md` and diff the output against the hand-constructed `dolo-plus-draft.yaml`.

## Workflow reminders

- **Matsya session:** continue `topics2026-siying99-ballpark` for any further Matsya calls on this item. Do **not** open a new session — session string is committed in [`matsya-session.txt`](matsya-session.txt).
- **Paper verification:** Matsya output must be checked against the paper PDF (or `.mmd` once committed), not only against the ballpark notebooks. `verification.md` explicitly references the paper at <https://web.stanford.edu/~aauclert/ha_oe.pdf>.
- **When flagging workarounds in YAML:** use inline `# workaround:` or `# unresolved:` comments rather than silently fudging non-canonical syntax. The current `dolo-plus-draft.yaml` has no such comments — add them next to any placeholder calibration or structural shortcut introduced in follow-up work.
