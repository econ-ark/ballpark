# Auclert, Rognlie, Souchier, and Straub (2024) — Reading Guide

> 📖 **Rendered version of this entry:** [econ-ark.github.io/ballpark/openha/](https://econ-ark.github.io/ballpark/openha/) — full MyST rendering with citations, math, and the four exposition notebooks assembled into one page. Recommended for human readers.

A *Formalized*-tier ballpark entry for Auclert, Rognlie, Souchier, and Straub (2024), "Exchange Rates and Monetary Policy with Heterogeneous Agents: Sizing up the Real Income Channel," NBER Working Paper 28872 ([DOI: 10.3386/w28872](https://doi.org/10.3386/w28872)).

The rendered version above is built from [`OpenHA.md`](OpenHA.md), which assembles the four exposition notebooks into a single MyST page. The rest of this README is for someone landing on the GitHub directory listing who wants to know what the technical files are and how to read them.

## Scope of the formalization layer

[`dolo-plus-draft.yaml`](dolo-plus-draft.yaml) encodes the **household block only** — the three-stage period (`shocks` → `cons` → `disc`) of [`bellman-excerpt.md`](bellman-excerpt.md) §8. The aggregate / general-equilibrium closure (CPI, real exchange rate, real UIP, RoW demand, sticky-wages Phillips curve, monetary rule, NFA, current account) is fully specified equation-by-equation in `bellman-excerpt.md` §§3–4 and consolidated as the 16-equation system of §7, but is **deliberately not encoded in YAML in this PR**.

The canonical record of this scope choice — including the rationale and the explicit follow-up plan for an `aggregate-draft.yaml` — is [`bellman-excerpt.md`](bellman-excerpt.md) §13 ("Open items"). The same scope statement appears in `OpenHA.md` frontmatter (`formalization_scope: household-block-only`), [`AGENTS.md`](AGENTS.md) ("Formalization status" section and the top-of-file callout), and `OpenHA_summary.ipynb` ("Pointer to formalization layer" cell). All four documents agree.

CONTRIBUTING.md's "Formalized" tier explicitly allows a one-stage / one-block YAML; the household-only scope is sufficient for promotion. The household block is the natural unit for an Econ-ARK / HARK cross-check (the iMPC matrix **M** of `bellman-excerpt.md` §5 maps directly onto HARK's existing sequence-space-Jacobian interface).

## Reading the formalization layer

The YAML in this directory is written in **dolo-plus**, a modular-DP YAML format used by the Bellman-DDSL ecosystem. It was produced by iteration with **[Matsya](https://github.com/econ-ark/matsya)** (a DDSL-aware evaluator) starting from the corresponding excerpt; see the repo-root [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) "The formalization iteration" section for the workflow.

**Excerpt-plus-YAML pair** (household block):

- [`bellman-excerpt.md`](bellman-excerpt.md) — modular-DDSL Bellman statement: comprehensive symbol table, full portfolio-form household problem reduced to the canonical one-asset form, aggregate closure equations (E.1–E.16), iMPC chain-rule decomposition of **M**^HA-IM, three-stage household decomposition with explicit perch table, paper-grounded calibration, extensions register, and §13 Open items (canonical scope record).
- [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml) — Matsya-generated household three-stage period; `horizon: infinite-stationary`; paper-grounded calibration block (paper Table 2 + §5.2); inline `# unresolved:` flag at the `e_prime` Markov-chain declaration recording the Rouwenhorst-constructor workaround. Per CONTRIBUTING.md line 44, workarounds are flagged inline at the point of divergence rather than collected at the bottom of the file.

Inline `# unresolved:` comments in the YAML cite the relevant entry of `bellman-excerpt.md` §13 by number (currently §13.2 only — the Rouwenhorst constructor). The construction audit trail lives in [`verification.md`](verification.md), which compares the YAML to the paper section by section across nine rounds (initial pass; April 2026 paper re-read; round-8 Matsya iteration; round-9 instructor-review revisions for PR #73).

## Asset layer

- The paper PDF is **not** redistributed in this directory; the authoritative source is at [DOI: 10.3386/w28872](https://doi.org/10.3386/w28872) (the August 2024 revision is at <https://web.stanford.edu/~aauclert/ha_oe.pdf>). For AI-assisted reading, produce a local `OpenHA.mmd` from the PDF via Mathpix or pandoc — `*.mmd` is gitignored at the repo root and is each contributor's local copy (see repo-root `CONTRIBUTING.md` Asset-layer table for the rationale).
- [`bellman-excerpt.pdf`](bellman-excerpt.pdf) — pandoc-rendered PDF of `bellman-excerpt.md` for offline reading.
- [`OpenHA-perch-graphs.md`](OpenHA-perch-graphs.md) — mermaid perch-graph diagrams for both the household three-stage period (encoded in YAML) and the aggregate-block 16-equation system (specified in `bellman-excerpt.md` §§3, 7, not yet in YAML). The diagrams are embedded as fenced ` ```mermaid ` blocks inside a `.md` file rather than separate `.mmd` files because the `*.mmd` gitignore rule would otherwise ignore them.

## Index of main files

**Exposition layer** (rendered MyST page; the public-facing entry):

- [`OpenHA.md`](OpenHA.md) — MyST page assembling the four notebooks below (named `<citekey>.md` rather than `index.md` so the rendered URL slug is `/openha/` rather than the auto-deduplicated `/index-N/`).
- [`OpenHA_intro.ipynb`](OpenHA_intro.ipynb) — citation, contributor info, paper pitch.
- [`OpenHA_prior-literature.ipynb`](OpenHA_prior-literature.ipynb) — six prior-literature anchors (Galí–Monacelli, Kaplan–Moll–Violante, Auclert–Rognlie–Straub iMPC, Auclert 2019, Krugman–Taylor, de Ferra–Mitman–Romei) plus a "Further reading" cell.
- [`OpenHA_summary.ipynb`](OpenHA_summary.ipynb) — non-technical summary, "The Model" with explicit recursive formulation for the heterogeneous-agent household block, aggregate closure prose, headline analytical results (international Keynesian cross, χ-neutralities, contractionary depreciation), pointer to the formalization layer.
- [`OpenHA_subsequent-literature.ipynb`](OpenHA_subsequent-literature.ipynb) — research directions following OpenHA.

**Formalization layer** (technical artifacts):

- [`bellman-excerpt.md`](bellman-excerpt.md) — modular-DDSL Bellman statement (§§1–12) plus canonical Open-items record (§13).
- [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml) — household three-stage YAML.
- [`verification.md`](verification.md) — round-by-round Matsya-iteration record + round-9 instructor-review revisions.
- [`matsya-session.txt`](matsya-session.txt) — Matsya session pointer (`topics2026-siying99-ballpark`, 9 turns).
- [`OpenHA-perch-graphs.md`](OpenHA-perch-graphs.md) — mermaid perch-graph diagrams (household + aggregate).
- [`bellman-excerpt.pdf`](bellman-excerpt.pdf) — pandoc-rendered PDF of `bellman-excerpt.md`.

**Asset layer** (paper-source material and bibliography):

- The paper PDF is not committed (NBER WP / SSRN access; produce a local `OpenHA.mmd` for AI ingestion via Mathpix or pandoc — gitignored).
- [`Shin_ARSS.ipynb`](Shin_ARSS.ipynb) — original 2023 notebook (retained for historical reference).
- [`references.bib`](references.bib), [`self.bib`](self.bib), [`subsequent-literature.bib`](subsequent-literature.bib) — bibliography.

**Project files**:

- [`AGENTS.md`](AGENTS.md) — agent-facing brief: top-of-file scope callout, formalization status, known model features, common next tasks, workflow reminders.
- [`myst.yml`](myst.yml) — per-entry MyST site configuration (kept for local single-entry development via `myst start` inside the entry; the root `myst.yml` is authoritative for the unified site build).
