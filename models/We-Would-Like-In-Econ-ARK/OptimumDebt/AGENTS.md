# Ballpark entry: Aiyagari & McGrattan (1998)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing content lives in [`index.md`](index.md).

## Paper

- **Citation:** S. Rao Aiyagari and Ellen R. McGrattan (1998), "The Optimum Quantity of Debt," *Journal of Monetary Economics* 42(3), 447–469.
- **DOI:** [10.1016/S0304-3932(98)00031-2](https://doi.org/10.1016/S0304-3932(98)00031-2)
- **Core model:** Aiyagari (1994)-style incomplete-markets heterogeneous-agent economy, augmented with balanced growth, government debt, and distortionary taxes. The household problem is a single consumption-savings stage with a persistent Markov productivity shock; two variants are studied (Model A: inelastic labor, lump-sum taxes; Model B: elastic labor, proportional taxes — the paper's benchmark). General equilibrium closes via firm FOCs, the government budget, and asset-market clearing $K + B = \int a\,dH$.
- **Why in-ballpark:** Canonical quantitative answer to the Bewley–Aiyagari normative question about optimal public debt. The punchline is a **null result**: moving U.S. debt to the calibrated optimum delivers a trivially small welfare gain, because the liquidity benefit of more safe-asset supply is roughly cancelled by tax-distortion and capital-crowding-out costs. This is the paper's cited contribution and an obvious REMARK / DemARK candidate.

## If a user asks to work on this item

1. **Read first:** [`bellman-excerpt.md`](bellman-excerpt.md) — the product of the Matsya iteration loop. §§1–9 are Model A (single consumption-savings stage with full perch decomposition, EGM recipe); §10 is Model B (added symbols, perches, transitions, movers, EGM-feasibility note). This supersedes `OptimumDebt_summary.ipynb` as the authoritative recursive statement once the formalization layer is present, per `CONTRIBUTING.md`.
2. **Formal YAML:** [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml) — one stage, Model A only. All unresolved features flagged inline.
3. **Supporting exposition:** [`OptimumDebt_summary.ipynb`](OptimumDebt_summary.ipynb) §II.A / §II.B for non-technical framing; §III for the solver-level penalty method (kept out of the formal DP).
4. **Paper source for AI ingestion:** *Not yet committed* — see next-tasks item 3 below. Pandoc the PDF into `OptimumDebt.mmd` and prefer that over the PDF for AI ingestion.

## Formalization status

- Explicit recursive formulation: **present** in `_summary.ipynb` §II.A (Model A) and §II.B (Model B).
- [`bellman-excerpt.md`](bellman-excerpt.md): **committed** (single evolving artifact per `CONTRIBUTING.md`; earlier "improved" variant consolidated into this file).
- [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml): **committed** (Model A interior stage only).
- [`verification.md`](verification.md): **committed** (verifies against the published paper, with section/equation cites).
- [`matsya-session.txt`](matsya-session.txt): **committed** — session name is `emma-ballpark-topics2026`.

## Known model features requiring attention in a formalization pass

- **$(1+g)$ growth factor in the dcsn→cntn transition.** The paper's budget (Sec. II, eq. 1) has $c + (1+g)\tilde{a}'$ on the LHS. The YAML restores this factor explicitly: `a_prime = (m_tilde - c_tilde)/(1+g)`, with matching $(1+g)$ adjustments in the EGM reverse transition and in the InvEuler FOC. Any agent refactoring the stage must preserve this or flag an equivalent workaround (absorbing $(1+g)$ into an effective discount factor). Do not silently drop the factor — this was the exact failure mode the current file corrects.
- **Markov transition matrix $\Pi$ for the productivity process $e$.** The paper's recursive statement (Sec. II) does *not* pin down $\Pi$; it is calibrated via Tauchen discretization of an AR(1) in Sec. IV (p. 458). `dolo-plus-draft.yaml` declares `N_e: 7` but leaves $\Pi$ symbolic — this is a formalizer choice, not a feature of the paper's DP.
- **Model B in the YAML is not yet encoded.** `bellman-excerpt.md` §10 gives the full perch decomposition for Model B and an EGM-feasibility note, but `dolo-plus-draft.yaml` covers only Model A. A Model-B YAML needs a second control `l`, a labor-income term in the budget, and the intratemporal FOC $\tilde{c}/l = \eta \bar w e / (1-\eta)$ to close conditional inversion.
- **$\tilde{\beta} < 1$ contraction restriction.** Not stated in the paper's Sec. II recursive form; implicit in the calibration ($\nu = 1.5$, $g = 0.0186$, $\beta \approx 0.96$). The YAML encodes $\tilde{\beta} = \beta(1+g)^{1-\nu}$ in the `calibration:` block; any reparameterization must preserve the inequality.
- **Penalty terms are solver-level, not formal DP.** The cubic $\zeta \cdot \min(\tilde{a}, 0)^3$ and $\zeta \cdot \min(1-l, 0)^3$ in paper Sec. III eq. (5) are the finite-element numerical device. Agents must not map them into the Bellman or the perch transitions; they belong (if at all) in a `replication/` subfolder when the item is promoted to REMARK.
- **General-equilibrium closure is out of scope.** The household stage treats $(r, \bar r, \tilde w, \bar w, \tau, \chi)$ as parameters. Firm FOCs, government budget, and market clearing ($K + B = \int \tilde{a}\, dH$) sit outside the stage. Do not add equilibrium equations into the stage YAML.

## Common next tasks (grounded)

1. **Encode Model B as a second stage in `dolo-plus-draft.yaml`** — parallel to the existing Model A stage, with controls $(\tilde{c}, l)$, the labor-income budget, the intratemporal FOC, and an EGM InvEuler using the composite marginal utility. See `bellman-excerpt.md` §§10.5–10.8 for the specification.
2. **Add the Tauchen discretization of the AR(1) productivity process** as a concrete $\Pi$ in the YAML's `calibration:` block (or as a separate `processes/` file), grounded in paper Sec. IV (p. 458). This removes the one remaining symbolic element.
3. **Commit `OptimumDebt.pdf` and `OptimumDebt.mmd`** (Pandoc-converted markdown) to the item folder. `self.bib` is present but the paper artifact is not; this is a Primer-checklist gap per `CONTRIBUTING.md`.
4. **Matsya-session rename (optional).** The committed session `emma-ballpark-topics2026` does not follow the course convention `topics2026-<citekey>` suggested in `CONTRIBUTING.md`. If course-staff review wants the convention enforced, rename to `topics2026-aiyagari1998` on next use; otherwise keep the existing session so the accumulated server-side context is preserved.
5. **Update the `index.md` frontmatter** for `tier: formalized` once items 1–3 above are merged. CI will then enforce the Formalized gate (file existence, AGENTS.md six-section structure, symbol-table heuristic, perch-name keyword check, YAML parse).

## Workflow reminders

- **Matsya session:** use `emma-ballpark-topics2026` for any new Matsya call on this item, so the server-side context from the original formalization iteration is preserved. Do not open a new session.
- **Paper verification:** Matsya and general-purpose-AI output must be checked against the paper itself (Sec. II for Model A, Sec. III for Model B, Sec. IV for calibration), not only against `OptimumDebt_summary.ipynb`. The summary is a derived notebook with known simplifications.
- **When flagging workarounds in YAML:** use inline `# workaround:` or `# unresolved:` comments rather than silently fudging non-canonical syntax. The $(1+g)$ drop was exactly the failure mode this convention is designed to prevent.
- **`bellman-excerpt.md` is the single evolving artifact.** Do not create `bellman-excerpt-*.md` variants (e.g. "improved", "draft", "polished"); edit the canonical file in place. This item's prior history contained a duplicate that has been consolidated.
