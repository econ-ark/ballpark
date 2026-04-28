---
title: "Algan and Ragot (2009) — Ballpark Entry"
schema_type: ScholarlyArticle
about:
  doi: 10.1016/j.red.2009.05.001
  authors: [Algan, Ragot]
  year: 2009
  journal: "Review of Economic Dynamics"
  volume: 13
  issue: 2
  pages: "295-316"
  preprint: "hal-01170621v1"
  preprint_url: "https://sciencespo.hal.science/hal-01170621v1"
keywords: [heterogeneous-agents, monetary-policy, borrowing-constraints, money-in-utility, inflation-tax]
econ_ark_topic:
  - HA-macro
  - monetary
jel: [E2, E5]
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
- [`verification.md`](verification.md) — accept / edit / reject judgments grounded in the published paper (Algan & Ragot 2009, *Review of Economic Dynamics* 13(2), pp.295-316), with paper-equation cross-references.
- [`matsya-session.txt`](matsya-session.txt) — the `--session` string used for this item (`topics2026-armonetarypolicyhabc`).
- [`AGENTS.md`](AGENTS.md) — structured brief for coding agents.
- [`self.bib`](self.bib) — BibTeX entry for the paper itself.

Iteration / review artifacts under `docs/` (kept out of the item root because they are the AI loop's history, not the Formalized deliverables themselves):

- [`docs/opus-prompt.md`](docs/opus-prompt.md) + [`docs/opus-review.md`](docs/opus-review.md) + [`docs/accept-edit-reject.md`](docs/accept-edit-reject.md) — Class 12 review artifacts.
- [`docs/matsya-evaluate-turn.txt`](docs/matsya-evaluate-turn.txt) — verbatim Matsya Evaluate turn on the two-stage decomposition.
- [`docs/lessons-learned.md`](docs/lessons-learned.md), [`docs/tier-assessment.md`](docs/tier-assessment.md) — synthesis docs.
- [`docs/legacy-drafts/`](docs/legacy-drafts/) — pre-iteration Bellman drafts retained for history (superseded by `bellman-excerpt.md` at the item root).

## Next promotion steps (toward Primer → Formalized)

- Add the four exposition notebooks, `references.bib`, `subsequent-literature.bib`, and the paper `.pdf` / `.mmd` (or only `.mmd`, depending on licence verification).
- Re-encode the YAML utility kernel into the paper's CES-with-leisure form (eq. 15 of the paper, transcribed verbatim in [`docs/legacy-drafts/arg2009-bellman-excerpt.md`](docs/legacy-drafts/arg2009-bellman-excerpt.md)), or keep the separable workaround and justify it under the `# unresolved:` block already present in [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml).
- See [`docs/accept-edit-reject.md`](docs/accept-edit-reject.md) for the full list of deferred items from the Opus 4.7 review and the [class-wide review of PR #72](https://github.com/econ-ark/ballpark/pull/72).
