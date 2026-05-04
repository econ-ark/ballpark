---
title: "Algan and Ragot (2009) — Ballpark Entry"
schema_type: ScholarlyArticle
about:
  doi: TBD
  authors: [Algan, Ragot]
  year: 2009
  journal: TBD
keywords: [heterogeneous-agents, monetary-policy, borrowing-constraints, money-in-utility, inflation-tax]
econ_ark_topic:
  - HA-macro
  - monetary
jel: [E21, E52, D31]
difficulty: stretch
tier: draft
has_formalization_layer: true
ballpark_contributor:
  name: TBD
updated_by: []
---

# Algan and Ragot (2009) — Ballpark Entry

> **Stub `index.md`.** This file exists so the item has the required Draft-tier frontmatter and a single entry-point page. The canonical four-notebook exposition layout (`<citekey>_intro.ipynb`, `_prior-literature.ipynb`, `_summary.ipynb`, `_subsequent-literature.ipynb`) per [`CONTRIBUTING.md`](https://github.com/econ-ark/ballpark/blob/master/CONTRIBUTING.md) is **not yet in place**; it is tracked as deferred item #1 in [`docs/accept-edit-reject.md`](docs/accept-edit-reject.md).

## What is in this item today

Item-root files (the layout `CONTRIBUTING.md` §"Formalized" expects, so that the automated Formalized check finds them):

- [`ToramanSY_AlganRagot2009_Summary.ipynb`](ToramanSY_AlganRagot2009_Summary.ipynb) — legacy single-notebook ballpark summary (will be split at the Primer-promotion step).
- [`bellman-excerpt.md`](bellman-excerpt.md) — canonical modular-DDSL Bellman / stages / perches for the household block.
- [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml) — two-stage dolo-plus draft (household block only; aggregate side out of scope — see [`AGENTS.md`](AGENTS.md)).
- [`verification.md`](verification.md) — accept / edit / reject against the summary + AI iteration (paper-grounded rewrite is deferred).
- [`matsya-session.txt`](matsya-session.txt) — the `--session` string used for this item (`topics2026-armonetarypolicyhabc`).
- [`AGENTS.md`](AGENTS.md) — structured brief for coding agents.

Iteration / review artifacts under `docs/` (kept out of the item root because they are the AI loop's history, not the Formalized deliverables themselves):

- [`docs/opus-prompt.md`](docs/opus-prompt.md) + [`docs/opus-review.md`](docs/opus-review.md) + [`docs/accept-edit-reject.md`](docs/accept-edit-reject.md) — Class 12 review artifacts.
- [`docs/matsya-evaluate-turn.txt`](docs/matsya-evaluate-turn.txt) — verbatim Matsya Evaluate turn on the two-stage decomposition.
- [`docs/lessons-learned.md`](docs/lessons-learned.md), [`docs/tier-assessment.md`](docs/tier-assessment.md) — synthesis docs.
- [`docs/legacy-drafts/`](docs/legacy-drafts/) — pre-iteration Bellman drafts retained for history (superseded by `bellman-excerpt.md` at the item root).

## Next promotion steps (toward Primer → Formalized)

- Add the four exposition notebooks, `references.bib`, `self.bib`, `subsequent-literature.bib`, and the paper `.pdf` / `.mmd`.
- Rewrite `verification.md` against the published paper (cite equations by number).
- Align the YAML utility with the CES-with-leisure specification preserved in [`docs/legacy-drafts/arg2009-bellman-excerpt.md`](docs/legacy-drafts/arg2009-bellman-excerpt.md) (verbatim from the summary notebook), or keep the separable kernel and justify the simplification under the `# unresolved:` block already present in [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml).
- See [`docs/accept-edit-reject.md`](docs/accept-edit-reject.md) for the full list of deferred items from the Opus 4.7 review and the [class-wide review of PR #72](https://github.com/econ-ark/ballpark/pull/72).
