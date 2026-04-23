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
3. **Paper source for AI ingestion:** **TBD** — prefer `AlganRagot2009.mmd` once committed per Primer checklist; until then use the summary notebook + PDF.

## Formalization status

- Explicit recursive formulation: present in `ToramanSY_AlganRagot2009_Summary.ipynb` (ballpark summary; not yet split into the full four-notebook `index.md` layout).
- `docs/bellman-excerpt.md`: committed (Matsya-assisted iteration; human-edited for CONTRIBUTING structure).
- `docs/dolo-plus-draft.yaml`: committed (draft; utility block does not yet match CES form in summary excerpt).
- `docs/verification.md`: committed (accept / edit / reject vs. summary + paper).
- `docs/matsya-session.txt`: committed (`topics2026-armonetarypolicyhabc`).

## Known model features requiring attention in a formalization pass

- **Utility:** Summary excerpt uses a CES consumption–money composite with leisure; YAML uses a separable placeholder — see `docs/verification.md` and `# unresolved:` in `docs/dolo-plus-draft.yaml`.
- **Law of motion for `q'`:** Draft uses `q' = R a + (1+r_m) m` — verify against Algan–Ragot (2009) text (or `.mmd`).
- **Borrowing constraint:** `a_min` is a labeled placeholder; replace with paper-specific rule.
- **Markov `Pi`:** Named but not calibrated in YAML — replace with paper-consistent discretization.

## Common next tasks (grounded)

1. Align `dolo-plus-draft.yaml` utility with the CES–leisure specification in `docs/arg2009-bellman-excerpt.md`, or document a deliberate simpler kernel under `# workaround:`.
2. Replace placeholder `(R, r_m, Pi, a_min)` with values or explicit formulas from the paper.
3. When the exposition layer is refactored to the canonical four-notebook + `index.md` layout, add `self.bib`, `.mmd` if license permits, and wire `index.md` frontmatter (`tier`, `has_formalization_layer`, etc.).

## Workflow reminders

- **Matsya session:** use `topics2026-armonetarypolicyhabc` (see `docs/matsya-session.txt`) for new Matsya calls on this item.
- **Paper verification:** compare Matsya and YAML choices to the published paper (or Pandoc `.mmd`), not only the summary notebook — see `docs/verification.md`.
- **YAML:** use `# unresolved:` or `# workaround:` for anything that does not map cleanly to canonical dolo-plus syntax—do not silently fudge.
