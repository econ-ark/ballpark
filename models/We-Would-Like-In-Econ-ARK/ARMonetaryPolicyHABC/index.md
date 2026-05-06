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
tier: formalized
has_formalization_layer: true
ballpark_contributor:
  name: TBD
updated_by:
  - date: "2026-04-28"
    note: "Promoted from Draft to Formalized: full four-notebook exposition layer (intro / prior-literature / summary / subsequent-literature) added on top of the paper-grounded formalization layer (PR #76), modelled on the Benhabib_et_al_2019 canonical example (PR #66). Toraman 2020 legacy single-notebook digest moved to docs/legacy-drafts/ and credited in _summary.ipynb."
---

# Algan and Ragot (2009) — Ballpark Entry

```{include} ARMonetaryPolicyHABC_intro.ipynb
```

```{include} ARMonetaryPolicyHABC_prior-literature.ipynb
```

```{include} ARMonetaryPolicyHABC_summary.ipynb
```

```{include} ARMonetaryPolicyHABC_subsequent-literature.ipynb
```

## What is in this item

**Exposition layer** (Primer-tier deliverables, rendered via the `{include}` directives above):

- [`ARMonetaryPolicyHABC_intro.ipynb`](ARMonetaryPolicyHABC_intro.ipynb) — citation, DOI, JEL codes, and the required 3-sentence pitch (*what the paper uniquely does / why Econ-ARK cares / what a REMARK would enable*).
- [`ARMonetaryPolicyHABC_prior-literature.ipynb`](ARMonetaryPolicyHABC_prior-literature.ipynb) — five canonical antecedents (Sidrauski 1967, Aiyagari 1994, Bewley 1983, İmrohoroğlu 1992, Erosa–Ventura 2002) and how Algan–Ragot synthesises them.
- [`ARMonetaryPolicyHABC_summary.ipynb`](ARMonetaryPolicyHABC_summary.ipynb) — paper digest: overview of the four channels of long-run inflation non-neutrality, the explicit recursive household problem, the firm/government/monetary blocks, the equilibrium definition, and the headline hump-shaped capital–inflation result.
- [`ARMonetaryPolicyHABC_subsequent-literature.ipynb`](ARMonetaryPolicyHABC_subsequent-literature.ipynb) — three threads of post-2009 literature: HANK (KMV 2018, McKay–Reis 2016), redistribution channel (Auclert 2019, Doepke–Schneider 2006), and money-demand / financial-frictions extensions (Ragot 2014, Challe et al. 2017).

**Formalization layer** (Formalized-tier deliverables, item-root):

- [`bellman-excerpt.md`](bellman-excerpt.md) — canonical modular-DDSL Bellman / stages / perches for the household block.
- [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml) — two-stage dolo-plus draft (household block only; aggregate side out of scope — see [`AGENTS.md`](AGENTS.md)). Inline `# unresolved:` flags on the CES-utility kernel and the Markov-chain calibration block, per `CONTRIBUTING.md` line 44.
- [`verification.md`](verification.md) — Accept / Edit / Reject judgments grounded paper-by-paper-equation against Algan & Ragot (2009), *Review of Economic Dynamics* 13(2), pp. 295–316.
- [`matsya-session.txt`](matsya-session.txt) — the `--session` string used for this item (`topics2026-armonetarypolicyhabc`).
- [`AGENTS.md`](AGENTS.md) — structured brief for coding agents.

**Bibliography** (cited by the four notebooks via `{cite}` directives, rendered through `myst.yml`):

- [`self.bib`](self.bib) — BibTeX entry for the paper itself.
- [`references.bib`](references.bib) — papers cited by Algan–Ragot 2009 and listed in the prior-literature notebook (Sidrauski, Tobin, Phelps, Friedman, Bewley, Aiyagari, İmrohoroğlu, Erosa–Ventura, Akyol, …).
- [`subsequent-literature.bib`](subsequent-literature.bib) — post-2009 HA-monetary literature cited in the subsequent-literature notebook (Kaplan–Moll–Violante 2018, Auclert 2019, McKay et al., Doepke–Schneider 2006, Ragot 2014, Challe et al. 2017, Bayer et al. 2019, Werning 2015, …).

**Iteration / review artifacts** under `docs/` (kept out of the item root because they are the AI loop's history, not the Formalized deliverables themselves):

- [`docs/opus-prompt.md`](docs/opus-prompt.md) + [`docs/opus-review.md`](docs/opus-review.md) + [`docs/accept-edit-reject.md`](docs/accept-edit-reject.md) — Class 12 review artifacts.
- [`docs/matsya-evaluate-turn.txt`](docs/matsya-evaluate-turn.txt) — verbatim Matsya Evaluate turn on the two-stage decomposition.
- [`docs/lessons-learned.md`](docs/lessons-learned.md), [`docs/tier-assessment.md`](docs/tier-assessment.md) — synthesis docs.
- [`docs/legacy-drafts/`](docs/legacy-drafts/) — pre-iteration drafts retained for history: the two earlier Bellman drafts (superseded by `bellman-excerpt.md` at the item root) and `ToramanSY_AlganRagot2009_Summary.ipynb` (Toraman 2020 single-notebook digest, superseded by the four-notebook exposition layer above; the model statement in `_summary.ipynb` is adapted from this digest with explicit credit).

## Known outstanding items

Listed in [`bellman-excerpt.md`](bellman-excerpt.md) → "Open issues" and in [`docs/accept-edit-reject.md`](docs/accept-edit-reject.md):

1. **CES-with-leisure utility kernel.** The YAML currently uses a separable CRRA + log-money + convex-labour-disutility workaround under an inline `# unresolved:` flag, with the paper's actual CES-aggregator-times-leisure-power form (eq. 15) transcribed verbatim in `docs/legacy-drafts/arg2009-bellman-excerpt.md`. Closing this requires locating a canonical dolo-plus example with a CES inner aggregator (a focused Matsya turn would do it), not rereading the paper.
2. **Markov-chain matrix literal.** The 3×3 productivity-process transition matrix is documented in the YAML as a comment block (paper §3.3.2 entries) but left as `P_e: '@in R+'` because the `@in StochasticMatrix` idiom has no precedent in the canonical dolo-plus corpus. Closing this is a small spec question for the dolo-plus maintainers.

Neither is blocking; both are inline-flagged per `CONTRIBUTING.md` line 44.
