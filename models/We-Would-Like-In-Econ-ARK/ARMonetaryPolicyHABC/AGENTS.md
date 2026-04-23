# Ballpark entry: Algan–Ragot (2009)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing exposition lives in the notebooks and (when present) `index.md`.

## Paper

- **Citation:** Algan, Yann, and Xavier Ragot (2009), *Monetary Policy and Heterogeneous Agent Models* (exact venue/pages — **TBD**: copy from `ToramanSY_AlganRagot2009_Summary.ipynb` intro cell when polishing).
- **DOI:** **TBD** — add from the summary notebook or `self.bib` when available.
- **Core model:** Heterogeneous households with incomplete markets, money and risky savings, idiosyncratic productivity following a finite-state Markov chain; monetary policy interacts with distribution and savings margins.
- **Why in-ballpark:** Structural heterogeneous-agent monetary economics with explicit household problem and quantitative policy experiments — natural fit for Econ-ARK’s HA / monetary threads.

## If a user asks to work on this item

1. **Read first:** `docs/bellman-excerpt.md` — canonical modular Bellman / stages / perches for the household block.
2. **Draft computational scaffold:** `docs/dolo-plus-draft.yaml` — interior two-stage draft; read inline `# unresolved:` / `# workaround:` before changing equations.
3. **AI iteration log:** `docs/opus-review.md` (Opus 4.7 review), `docs/matsya-evaluate-turn.txt` (Matsya Evaluate turn on the decomposition), and `docs/verification.md` (accept / edit / reject vs. paper and vs. dolo-plus spec).
4. **Paper source for AI ingestion:** **TBD** — prefer `AlganRagot2009.mmd` once committed per Primer checklist; until then use the summary notebook + PDF.

## Formalization status

- Explicit recursive formulation: present in `ToramanSY_AlganRagot2009_Summary.ipynb` (ballpark summary; not yet split into the full four-notebook `index.md` layout).
- `docs/bellman-excerpt.md`: committed (human-authored + Matsya-Evaluate-synchronized; three free controls with `a'` pinned by budget identity).
- `docs/dolo-plus-draft.yaml`: committed (draft; utility block does not yet match CES form in summary excerpt; `P_e` declared plain per Matsya Evaluate Q3; three free controls per Matsya Flag C).
- `docs/verification.md`: committed (partitioned into paper gaps vs. dolo-plus spec gaps).
- `docs/matsya-evaluate-turn.txt`: committed (verbatim Matsya Evaluate response on the two-stage decomposition; 4 CANONICAL, 1 PROVISIONAL-now-resolved, 1 UNRESOLVED-now-resolved).
- `docs/lessons-learned.md`: committed (consolidated reusable patterns, mirrored from the Benhabib worked example).
- `docs/matsya-session.txt`: committed (`topics2026-armonetarypolicyhabc`).

## Known model features requiring attention in a formalization pass

- **Scope (household block only).** The YAML and `docs/bellman-excerpt.md` encode the household block. The aggregate side from `docs/arg2009-bellman-excerpt.md` — production `Y = K^alpha L^(1-alpha)`, resource constraint, asset-market clearing, money growth `Omega_t`, inflation-tax `tau^{tot}` — is intentionally deferred to a later general-equilibrium pass. Do not rediscover this; scope new work accordingly.
- **Notation: Markov `P_e` vs inflation `Pi_inf`.** The household-side Markov kernel was renamed from `Pi` to `P_e` (see commit history and `docs/bellman-excerpt.md` symbol table) to avoid collision with the inflation series `Pi_inf` that appears on the aggregate side. Keep `P_e` in future edits to the household YAML; reintroduce `Pi_inf` explicitly when the monetary block is added.
- **Utility.** Summary excerpt uses a CES consumption–money composite with leisure parameterized by `(sigma, eta, omega, psi)` (rows now in `docs/bellman-excerpt.md` symbol table); YAML still uses a separable placeholder parameterized by `(rho, rho_m, phi_m, phi_l, gamma)` — flagged as `# workaround:` in `docs/dolo-plus-draft.yaml`.
- **Law of motion for `q'`.** Draft uses `q' = R a + (1+r_m) m` in the shock stage — verify against Algan–Ragot (2009) text (or `.mmd`).
- **Borrowing constraint `a_min`.** Labeled placeholder in YAML; replace with paper-specific rule once the paper is in-repo.
- **Transfer `mu`.** Domain is `R` (not `R+`) because the inflation-tax redistribution can make the net transfer negative for some households. Sign rule for an individual household is still TBD against the paper.
- **`P_e` calibration.** `P_e` is declared in both stages' `parameters:` blocks as plain `@in R+`; row-stochastic semantics are carried by `@dist MarkovChain(P_e)` on the exogenous block (canonical per Matsya Evaluate turn Q3). Numerical entries are `# unresolved:` until drawn from the paper.
- **Three free controls; `a'` pinned.** Per Matsya Evaluate Flag C, the household's free controls are `(c, m_d, l)`. The illiquid-asset poststate `a'` is pinned by the budget identity inside `dcsn_to_cntn_transition`. Preserve this encoding when aligning the utility kernel with the paper's CES-with-leisure form.

## Common next tasks (grounded)

1. Align `docs/dolo-plus-draft.yaml` utility with the CES–leisure specification in `docs/arg2009-bellman-excerpt.md`, or document a deliberate simpler kernel under `# workaround:`.
2. Replace placeholder `(R, r_m, P_e, a_min)` with values or explicit formulas from the paper.
3. Refactor exposition layer to the canonical four-notebook + `index.md` layout (`<citekey>_intro.ipynb`, `_prior-literature.ipynb`, `_summary.ipynb`, `_subsequent-literature.ipynb`); add `references.bib`, `self.bib`, `.mmd` if license permits, wire `index.md` frontmatter (`tier`, `has_formalization_layer`, etc.). Tracked as accepted-but-deferred item #1 in `docs/accept-edit-reject.md`.
4. Rewrite `docs/verification.md` to cite specific equations from the paper PDF/`.mmd` once it is in-repo. Tracked as accepted-but-deferred item #2 in `docs/accept-edit-reject.md`.
5. Add a conditional EGM-channel discussion to `docs/bellman-excerpt.md` once the utility is aligned with the paper (rejected-for-now in `docs/accept-edit-reject.md` item #10; revisit after task 1 above lands).

## Workflow reminders

- **Matsya session:** use `topics2026-armonetarypolicyhabc` (see `docs/matsya-session.txt`) for new Matsya calls on this item. Never open a new session mid-project.
- **Matsya prompt style:** one focused question per turn, `--no-think`, compact prompt (<3 KB). Request verdicts as CANONICAL / PROVISIONAL / UNRESOLVED with one-line justification. See `docs/matsya-evaluate-turn.txt` for the pattern that succeeded.
- **Paper verification:** compare Matsya and YAML choices to the published paper (or Pandoc `.mmd`), not only the summary notebook — see `docs/verification.md`. Paper gaps and dolo-plus spec gaps are partitioned explicitly there; close them via different routes.
- **YAML:** use `# unresolved:` or `# workaround:` for anything that does not map cleanly to canonical dolo-plus syntax—do not silently fudge.
- **Reusable patterns:** `docs/lessons-learned.md` records the iteration patterns from this pass; consult before starting a fresh round of changes.
