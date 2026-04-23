# Tier assessment for this PR

> Evaluated against [`CONTRIBUTING.md`](https://github.com/econ-ark/ballpark/blob/master/CONTRIBUTING.md) after **(a)** the Opus 4.7 accepted changes in `docs/opus-review.md` / `docs/accept-edit-reject.md` and **(b)** the Matsya Evaluate-turn fixes in `docs/matsya-evaluate-turn.txt` are applied.

## Claimed tier after this PR: **Draft** (with partial Formalized-layer artifacts)

This item cannot yet be claimed at **Primer** or **Formalized**, because each tier presupposes the tier below it and several Draft / Primer prerequisites are still deferred.

### Draft checklist

| Requirement | Status | Where |
|-------------|--------|-------|
| Item directory exists under `models/We-Would-Like-In-Econ-ARK/<citekey>/` | Satisfied | `models/We-Would-Like-In-Econ-ARK/ARMonetaryPolicyHABC/` |
| `index.md` with required frontmatter including `tier:` | **Satisfied in this PR** (stub) | [`index.md`](../index.md) |
| `<citekey>_intro.ipynb` with citation, DOI link, original ballpark author + date, 3-sentence pitch | **Not satisfied** — legacy `ToramanSY_AlganRagot2009_Summary.ipynb` conflates intro and summary | Deferred item #1 in [`accept-edit-reject.md`](accept-edit-reject.md) |
| `<citekey>_summary.ipynb` with non-technical motivation + findings overview | **Partially satisfied** via `ToramanSY_AlganRagot2009_Summary.ipynb` | Rename and split at Primer promotion |
| `references.bib` (may be empty at Draft) | **Not satisfied** | Deferred item #1 |
| Paper `.pdf` OR DOI pointer with license note in `_intro.ipynb` | **Not satisfied** | Deferred item #1 |

### Primer checklist (additional over Draft)

| Requirement | Status |
|-------------|--------|
| `<citekey>_prior-literature.ipynb` with 3–6 `{cite:t}` citations | Not satisfied |
| `<citekey>_summary.ipynb` extended with explicit "The Model" section | Partially — the explicit recursive formulation exists in `docs/bellman-excerpt.md`; it is not yet re-surfaced inside the summary notebook as a named "The Model" subsection |
| `<citekey>_subsequent-literature.ipynb` + `subsequent-literature.bib` | Not satisfied |
| `self.bib` | Not satisfied |
| `.mmd` (Pandoc-converted) | Not satisfied |
| `myst.yml` configured; `myst build` clean | Not satisfied |

### Formalized checklist (additional over Primer)

| Requirement | Status |
|-------------|--------|
| `bellman-excerpt.md` with comprehensive symbol table, timing, periods/stages/perches decomposition, stage operator | **Satisfied** after this PR (symbol-table closure + identity-mover labels + `P_e` rename + three-free-controls / budget-pinned `a'` per Matsya Flag C) — `docs/bellman-excerpt.md` |
| `dolo-plus-draft.yaml` (interior period acceptable); unresolved features flagged with `# workaround:` / `# unresolved:` | **Satisfied** after this PR — `docs/dolo-plus-draft.yaml`. Canonical patterns confirmed by `docs/matsya-evaluate-turn.txt` (4 CANONICAL verdicts); two non-canonical items from the draft (`@in StochasticMatrix`, four-control budget) were fixed in the Improve commits. |
| `verification.md` comparing Matsya output against the **published paper** | **Partially satisfied** after this PR — paper gaps and dolo-plus spec gaps are now partitioned explicitly in `docs/verification.md`. Spec-side gaps are closed; paper-side claims still grounded in the summary notebook, with paper-equation rewrite tracked as deferred item #2. |
| `matsya-session.txt` | **Satisfied** — `docs/matsya-session.txt` |
| `AGENTS.md` with the six required top-level sections | **Satisfied** after this PR — `AGENTS.md` |

## Conclusion

The **formalization-layer artifacts** (`bellman-excerpt.md`, `dolo-plus-draft.yaml`, `verification.md` in structure, `matsya-session.txt`, `AGENTS.md`) are in place and were substantially improved by the accepted changes from the Opus 4.7 review. However, the **exposition-layer prerequisites** for Draft and Primer are only partially satisfied (stub `index.md`; no four-notebook split; no bib files; no paper PDF/`.mmd`), so the honest tier label for the item right now is **Draft** — with a clearly advanced formalization-layer scaffold that will be re-evaluated for **Formalized** once the deferred items in `docs/accept-edit-reject.md` are merged.
