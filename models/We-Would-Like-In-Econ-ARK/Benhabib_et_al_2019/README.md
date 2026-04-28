# Benhabib, Bisin, and Luo (2019) — Reading Guide

A *Formalized*-tier ballpark entry for Benhabib, Bisin, and Luo (2019), "Wealth Distribution and Social Mobility in the US: A Quantitative Approach," *American Economic Review* 109(5), 1623–1647 ([DOI: 10.1257/aer.20151684](https://doi.org/10.1257/aer.20151684)).

For the rendered, human-facing version of this entry — citation, pitch, headline result, summary, prior/subsequent literature — see [`index.md`](index.md), which assembles four notebooks into one MyST page. The rest of this README is for someone landing on the GitHub directory listing who wants to know what the technical files are and how to read them.

## Reading the formalization layer

The YAML files in this directory are written in **dolo-plus**, a modular-DP YAML format used by the Bellman-DDSL ecosystem. They were produced by iteration with **[Matsya](https://github.com/econ-ark/matsya)** (a DDSL-aware evaluator) starting from the corresponding excerpt; see the repo-root [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) "The formalization iteration" section for the workflow.

Two parallel excerpt-plus-YAML pairs cover two layers of the model:

- **Within-life** (one household's finite-horizon Bellman): [`bellman-excerpt.md`](bellman-excerpt.md) is the modular-DDSL Bellman statement (symbol table, perch decomposition, transitions, movers, EGM channel); [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml) is the dolo-plus YAML, paper-calibrated from Tables 1, 4 plus the full Π_r matrix from online Appendix C.1.
- **Dynasty** (cross-generational composition): [`dynasty-excerpt.md`](dynasty-excerpt.md) describes the lifetime map g(·; τ, r), the joint Markov chain Π_τ ⊗ Π_r, and the paper's Pareto-tail Proposition; [`dolo-plus-dynasty.yaml`](dolo-plus-dynasty.yaml) is the corresponding YAML.

Inline `# unresolved:` and `# SPECULATIVE` comments in the YAMLs flag places where the dolo-plus spec has no canonical idiom yet — the structural intent is paper-faithful even where keyword names may need to be renamed once the spec stabilizes.

The construction audit trail lives in [`verification.md`](verification.md) (paragraph-level comparison against the published paper, including online Appendix A.1) and in `bellman-excerpt.md` Open Issues #1–#10 (chronological record of corrections, notably Issue #10 — where the published §I budget equation was found inconsistent with its own `c ≤ a` constraint, and the online-Appendix-A.1 model was adopted instead).

## Index of main files

**Exposition layer** (rendered MyST page; the public-facing entry):

- [`index.md`](index.md) — MyST page assembling the four notebooks below.
- [`Benhabib_et_al_2019_intro.ipynb`](Benhabib_et_al_2019_intro.ipynb) — citation, contributor info, paper pitch with headline quantitative result.
- [`Benhabib_et_al_2019_prior-literature.ipynb`](Benhabib_et_al_2019_prior-literature.ipynb) — foundational literature (Bewley / Huggett / Aiyagari / De Nardi / Benhabib-Bisin-Zhu).
- [`Benhabib_et_al_2019_summary.ipynb`](Benhabib_et_al_2019_summary.ipynb) — headline numbers, identification mechanism, "The Model" recursive formulation, counterfactuals, results, limitations.
- [`Benhabib_et_al_2019_subsequent-literature.ipynb`](Benhabib_et_al_2019_subsequent-literature.ipynb) — research directions since BBL 2019.

**Formalization layer** (technical artifacts):

- [`bellman-excerpt.md`](bellman-excerpt.md) — within-life modular-DDSL Bellman statement (input to Matsya iteration; Open Issues #1–#10 record post-Matsya corrections).
- [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml) — within-life dolo-plus YAML, paper-calibrated.
- [`dynasty-excerpt.md`](dynasty-excerpt.md) — dynasty-level cross-generational composition algebra.
- [`dolo-plus-dynasty.yaml`](dolo-plus-dynasty.yaml) — dynasty-level dolo-plus YAML.
- [`verification.md`](verification.md) — paper-fidelity audit (accepted / edited / refined post-paper-and-appendix-review).
- [`matsya-session.txt`](matsya-session.txt) — Matsya session pointer (`topics2026-benhabib-demo`, 6 turns).

**Asset layer** (paper source material):

- The paper PDF is **not** redistributed here for AER copyright reasons; access via the [DOI](https://doi.org/10.1257/aer.20151684). For AI-assisted reading, produce a local `Benhabib_et_al_2019.mmd` (Mathpix or pandoc conversion of the PDF) — this is gitignored at the repo root and not committed (see repo-root `CONTRIBUTING.md` Asset-layer table for the rationale).
- [`fig1.png`](fig1.png), [`fig2.png`](fig2.png) — paper Figure 1 (life-cycle earnings profiles) and Figure 2 (wealth distribution).
- [`references.bib`](references.bib), [`self.bib`](self.bib), [`subsequent-literature.bib`](subsequent-literature.bib) — bibliography (cited literature, the paper's own bib entry, and subsequent-literature citations respectively).

**Project files**:

- [`AGENTS.md`](AGENTS.md) — agent-facing brief: formalization status, known model features needing attention, common next tasks, workflow reminders.
- [`myst.yml`](myst.yml) — MyST site configuration.
