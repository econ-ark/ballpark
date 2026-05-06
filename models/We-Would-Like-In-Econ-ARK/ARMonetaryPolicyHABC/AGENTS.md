# Ballpark entry: Algan–Ragot (2009)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing exposition lives in the notebooks and (when present) `index.md`.

## Paper

- **Citation:** Algan, Yann, and Xavier Ragot (2009), "Monetary policy with heterogeneous agents and borrowing constraints," *Review of Economic Dynamics* 13(2), pp. 295–316. (Available online 2009; print volume 13(2).)
- **DOI:** [10.1016/j.red.2009.05.001](https://doi.org/10.1016/j.red.2009.05.001).
- **Author preprint:** HAL [hal-01170621v1](https://sciencespo.hal.science/hal-01170621v1) (open-access archive; the verification is grounded in this preprint).
- **BibTeX:** see [`self.bib`](self.bib) (citekey: `algan2009monetary`).
- **JEL:** E2 (general macroeconomics), E5 (monetary policy, central banking).
- **Core model (paper §3, "The general model").** Heterogeneous households with incomplete markets, money-in-utility (CES with leisure), riskless capital savings, no borrowing (`a' ≥ 0`), idiosyncratic labor productivity following a 3-state Markov chain `e ∈ {e_h, e_m, e_l}`, lump-sum monetary transfer `μ` (sign depends on redistribution scheme), Cobb-Douglas aggregate production `Y = K^α L^(1-α)`, distortionary income tax `χ`, monetary growth rule `Ω_t = Ω_{t-1}/Π_t + π Ω_{t-1}/Π_t`. Quarterly model period.
- **Why in-ballpark:** Structural heterogeneous-agent monetary economics with explicit household problem (paper eqs. 15-22) and quantitative policy experiments (paper §4). Natural fit for Econ-ARK's HA / monetary threads.

## If a user asks to work on this item

1. **Read first:** `bellman-excerpt.md` (item root) — canonical modular Bellman / stages / perches for the household block.
2. **Draft computational scaffold:** `dolo-plus-draft.yaml` (item root) — interior two-stage draft; read inline `# unresolved:` / `# workaround:` before changing equations.
3. **AI iteration log:** `docs/opus-review.md` (Opus 4.7 review), `docs/matsya-evaluate-turn.txt` (Matsya Evaluate turn on the decomposition), and `verification.md` at the item root (accept / edit / reject vs. paper and vs. dolo-plus spec).
4. **Exposition layer (Primer / Formalized tier rendering):** the four-notebook layout at the item root — `ARMonetaryPolicyHABC_intro.ipynb`, `_prior-literature.ipynb`, `_summary.ipynb`, `_subsequent-literature.ipynb` — wired into `index.md` via `{include}` directives and resolved against `self.bib` + `references.bib` + `subsequent-literature.bib` through `myst.yml`.
5. **Paper source for AI ingestion:** **TBD** — prefer `AlganRagot2009.mmd` (HAL preprint, open-access) once committed; the publisher PDF is *not* committed for the same AER-copyright reason that prompted [PR #75](https://github.com/econ-ark/ballpark/pull/75) to remove `Benhabib_et_al_2019.pdf` after PR #66 merged. Until the `.mmd` is committed, use the summary notebook plus the user-supplied off-repo PDF (RED is published by Elsevier; the HAL preprint is the author-accepted-manuscript version that is open-access).

## Formalization status

This item targets `tier: formalized` (frontmatter in `index.md`). The full canonical layout that the `CONTRIBUTING.md` automated Formalized check looks for now lives at the **item root** (per `CONTRIBUTING.md` §"Formalized" + the Benhabib worked example layout in [PR #66](https://github.com/econ-ark/ballpark/pull/66)):

**Formalization-layer files (paper-grounded; verified in PR #76):**

- `bellman-excerpt.md`: committed at item root (human-authored + Matsya-Evaluate-synchronized; three free controls with `a'` pinned by budget identity).
- `dolo-plus-draft.yaml`: committed at item root (draft; utility block does not yet match CES form in paper eq. 15; `P_e` declared plain per Matsya Evaluate Q3; three free controls per Matsya Flag C; inline `# unresolved:` flags on the two open items).
- `verification.md`: committed at item root (paper-grounded against Algan & Ragot 2009 *Review of Economic Dynamics* 13(2); partitioned into paper gaps vs. dolo-plus spec gaps).
- `matsya-session.txt`: committed at item root (`topics2026-armonetarypolicyhabc`).
- `AGENTS.md`: this file, at the item root.

**Exposition-layer files (Primer-tier deliverables; this PR):**

- `ARMonetaryPolicyHABC_intro.ipynb`: committed at item root — citation, DOI, JEL codes, the required 3-sentence pitch (*what the paper uniquely does / why Econ-ARK cares / what a REMARK would enable*).
- `ARMonetaryPolicyHABC_prior-literature.ipynb`: committed at item root — five canonical antecedents (within the 3–6 prior-papers Primer-tier bound).
- `ARMonetaryPolicyHABC_summary.ipynb`: committed at item root — paper digest adapted from the Toraman 2020 single-notebook digest (now under `docs/legacy-drafts/`) with explicit credit; model statement aligned with `bellman-excerpt.md`.
- `ARMonetaryPolicyHABC_subsequent-literature.ipynb`: committed at item root — three threads of post-2009 literature (HANK, redistribution channel, money-demand / financial-frictions extensions).

**Bibliography files:**

- `self.bib`: BibTeX entry for the paper itself (citekey `algan2009monetary`).
- `references.bib`: papers cited by Algan–Ragot 2009 and listed in `_prior-literature.ipynb`.
- `subsequent-literature.bib`: post-2009 HA-monetary literature cited in `_subsequent-literature.ipynb`.

**Site config:**

- `myst.yml`: project-level MyST config wiring `index.md` to the three bib files.
- `index.md`: stitches the four exposition notebooks together via `{include}` directives.

**Iteration history under `docs/` (deliberately not at the item root):**

- `docs/opus-prompt.md`, `docs/opus-review.md`, `docs/accept-edit-reject.md`: Class 12 Opus 4.7 review artifacts (verbatim).
- `docs/matsya-evaluate-turn.txt`: verbatim Matsya Evaluate response (4 CANONICAL, 1 PROVISIONAL-now-resolved, 1 UNRESOLVED-now-resolved).
- `docs/lessons-learned.md`: consolidated reusable patterns mirrored from the Benhabib worked example.
- `docs/tier-assessment.md`: tier walk-through against the `CONTRIBUTING.md` checklist.
- `docs/legacy-drafts/`: pre-iteration drafts retained for history — the two earlier Bellman drafts (`arg2009-bellman-excerpt.md`, `arg2009-improved-stage-description.md`) and the Toraman 2020 single-notebook digest (`ToramanSY_AlganRagot2009_Summary.ipynb`); see `docs/legacy-drafts/README.md`.

Per `CONTRIBUTING.md` line 52, there is exactly **one** Bellman excerpt at the item root; the two `arg2009-*` drafts under `docs/legacy-drafts/` are **not** parallel canonical files. Per the PR-#66 → PR-#75 lesson, there is also exactly **one** summary notebook at the item root (`ARMonetaryPolicyHABC_summary.ipynb`); the Toraman 2020 single-notebook digest under `docs/legacy-drafts/` is preserved for authorship credit but is **not** an alternative canonical exposition.

## Known model features requiring attention in a formalization pass

- **Scope (household block only).** The YAML and `bellman-excerpt.md` encode the household block. The aggregate side from `docs/legacy-drafts/arg2009-bellman-excerpt.md` — production `Y = K^alpha L^(1-alpha)`, resource constraint, asset-market clearing, money growth `Omega_t`, inflation-tax `tau^{tot}` — is intentionally deferred to a later general-equilibrium pass. Do not rediscover this; scope new work accordingly.
- **Notation: Markov `P_e` vs inflation `Pi_inf`.** The household-side Markov kernel was renamed from `Pi` to `P_e` (see commit history and `bellman-excerpt.md` symbol table) to avoid collision with the inflation series `Pi_inf` that appears on the aggregate side. Keep `P_e` in future edits to the household YAML; reintroduce `Pi_inf` explicitly when the monetary block is added.
- **Utility.** Summary excerpt uses a CES consumption–money composite with leisure parameterized by `(sigma, eta, omega, psi)` (rows now in `bellman-excerpt.md` symbol table; verbatim form preserved in `docs/legacy-drafts/arg2009-bellman-excerpt.md`); YAML still uses a separable placeholder parameterized by `(rho, rho_m, phi_m, phi_l, gamma)`. The `# unresolved:` block on the `cntn_to_dcsn_mover` `Bellman:` block in `dolo-plus-draft.yaml` now spells out the canonical CES-with-leisure form and the two ways to close the deferral (replace the kernel; or justify the workaround under a calibration regime where separability and CES coincide).
- **Law of motion for `q'`.** Draft uses `q' = R a + (1+r_m) m` in the shock stage — verify against Algan–Ragot (2009) text (or `.mmd`).
- **Borrowing constraint `a_min`.** Labeled placeholder in YAML; replace with paper-specific rule once the paper is in-repo.
- **Transfer `mu`.** Domain is `R` (not `R+`) because the inflation-tax redistribution can make the net transfer negative for some households. Sign rule for an individual household is still TBD against the paper.
- **`P_e` calibration.** `P_e` is declared in both stages' `parameters:` blocks as plain `@in R+`; row-stochastic semantics are carried by `@dist MarkovChain(P_e)` on the exogenous block (canonical per Matsya Evaluate turn Q3). Numerical entries are `# unresolved:` until drawn from the paper.
- **Three free controls; `a'` pinned.** Per Matsya Evaluate Flag C, the household's free controls are `(c, m_d, l)`. The illiquid-asset poststate `a'` is pinned by the budget identity inside `dcsn_to_cntn_transition`. Preserve this encoding when aligning the utility kernel with the paper's CES-with-leisure form.

## Common next tasks (grounded)

1. Align `dolo-plus-draft.yaml` utility with the CES–leisure specification in `docs/legacy-drafts/arg2009-bellman-excerpt.md` (verbatim from the summary), or keep the separable kernel and justify the simplification under the existing `# unresolved:` block on the `Bellman:` mover. (This is the largest remaining substantive gap between the YAML and the paper; closing it is a focused Matsya turn, not a paper-rereading task — see PR #76 / PR #66 precedent.)
2. Replace the `P_e: '@in R+'` placeholder with the literal 3×3 row-stochastic matrix entries already documented in the YAML's `parameters:` comment block (paper §3.3.2). Closing this is a small spec question for the dolo-plus maintainers about matrix-literal idioms in the parameter block.
3. Commit `AlganRagot2009.mmd` (Pandoc/MathPix conversion of the open-access HAL preprint). The publisher PDF is **not** to be committed — see the AER-copyright lesson in [PR #75](https://github.com/econ-ark/ballpark/pull/75) and the `# Copyright check` annotation in `AGENTS.md`'s "If a user asks to work on this item" §4 above.
4. Add the EGM-channel discussion to `bellman-excerpt.md` once the utility is aligned with the paper (rejected-for-now in `docs/accept-edit-reject.md` item #10; revisit after task 1 above lands).
5. (REMARK precursor.) Begin a working numerical implementation of the model under HARK's `IndShockConsumerType` extended with the money-in-utility kernel, targeting the paper's headline hump-shaped capital–inflation result. This is REMARK territory rather than ballpark territory and would close the promotion-from-Formalized step.

Tasks 1–3 are each at most a focused weekly assignment; tasks 4–5 are larger and live beyond Formalized.

## Workflow reminders

- **Matsya session:** use `topics2026-armonetarypolicyhabc` (see `matsya-session.txt`) for new Matsya calls on this item. Never open a new session mid-project.
- **Matsya prompt style:** one focused question per turn, `--no-think`, compact prompt (<3 KB). Request verdicts as CANONICAL / PROVISIONAL / UNRESOLVED with one-line justification. See `docs/matsya-evaluate-turn.txt` for the pattern that succeeded.
- **Paper verification:** compare Matsya and YAML choices to the published paper (or Pandoc `.mmd`), not only the summary notebook — see `verification.md` at the item root. Paper gaps and dolo-plus spec gaps are partitioned explicitly there; close them via different routes.
- **YAML:** use `# unresolved:` or `# workaround:` for anything that does not map cleanly to canonical dolo-plus syntax—do not silently fudge.
- **Reusable patterns:** `docs/lessons-learned.md` records the iteration patterns from this pass; consult before starting a fresh round of changes.
