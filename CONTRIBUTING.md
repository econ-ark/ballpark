# Contributing a ballpark item

A **ballpark item** is a single paper's entry point into the Econ-ARK ecosystem: enough structure, context, and formalization that an ambitious graduate student can progress the paper from "interesting" through "formal recursive model" toward a [REMARK](https://github.com/econ-ark/REMARK) or [DemARK](https://github.com/econ-ark/DemARK) candidate in one semester.

This file specifies what a ballpark item should contain and how to submit one. For background on the project, see [README.md](README.md).

---

## Before you start

1. **Is the paper in scope?** Ballpark items are papers that are either (a) serious structural models producing interesting quantitative results, or (b) strong empirical evidence that begs for a model. See [README.md](README.md) for the two tracks (`models/` vs `empirical/`).
2. **Has the paper been cited enough to matter?** The paper must have **at least 3 citations in Google Scholar** to be eligible as a ballpark candidate. This is a hard gate: it filters for papers whose ideas have begun to circulate in the literature, without excluding recent papers that have not yet accumulated many citations. Paste the Google Scholar citation count (as of submission date) into the submission PR description.
3. **Is it already here?** Check `models/We-Would-Like-In-Econ-ARK/` for an existing subdirectory under the paper's citekey. If one exists, open a PR improving it rather than creating a parallel entry.
4. **Is it listed but not yet claimed?** If there is a subdirectory but it is thin (legacy "slideware" — one notebook of markdown + figures), your contribution can be to refactor it to the canonical structure below.
5. **None of the above?** Open an issue naming the paper, the DOI, and the track (`models` / `empirical`), and we will confirm before you invest effort.

---

## Three layers of a ballpark item

A canonical ballpark item has three layers. The *exposition* layer is required; the *formalization* layer turns a summary into a modular-DP scaffold (this is the output of a course-project workflow); the *asset* layer holds source material for human and AI re-reading.

### 1. Exposition layer — required

Four notebooks assembled by one `index.md`. Name them with the paper's citekey prefix, e.g. `benhabib2019_intro.ipynb`.

| File | Content |
|------|---------|
| `index.md` | MyST page with `{include}` directives for the four notebooks below (in order), plus YAML frontmatter giving the rendered title. |
| `<citekey>_intro.ipynb` | Full citation with DOI link. **Original ballpark author** (name + date). **Updated by** (latest + date). 3-sentence pitch: why the paper is in-ballpark for Econ-ARK. |
| `<citekey>_prior-literature.ipynb` | Where the paper sits in the foundational literature (Bewley / Huggett / Aiyagari / de Nardi / ...). Use `{cite:t}` citations rendered from `references.bib`. |
| `<citekey>_summary.ipynb` | Non-technical motivation + a **"The Model"** section stating the recursive formulation **explicitly**: no `u(c)` placeholders, explicit CRRA or EZ kernel, explicit bequest function, explicit transitions, explicit shock distributions, explicit constraint set. This section is what the formalization layer will build on. |
| `<citekey>_subsequent-literature.ipynb` | Research directions that followed the paper. Cite from `subsequent-literature.bib`. |

The [Benhabib_et_al_2019](models/We-Would-Like-In-Econ-ARK/Benhabib_et_al_2019/) item is the reference instance of this layer.

### 2. Formalization layer — stretch (recommended for coursework)

Five files that take the explicit recursive formulation from `_summary.ipynb` and lift it toward a dolo-plus stage.

| File | Content |
|------|---------|
| `bellman-excerpt.md` | A standalone modular-DDSL Bellman statement: symbol table, timing convention (numbered steps within one period), perch decomposition (arrival $\prec$ / decision $\circ$ / continuation $\succ$), a single table listing state, control, shock, constraint, payoff at their native perches, the stage operator $\mathbb{T} = \mathbb{I} \circ \mathbb{B}$, and any explicit utility/bequest forms. This is the file you feed to [Matsya](https://github.com/econ-ark/matsya) for stage decomposition. |
| `bellman-excerpt-SMD-polished.md` | Post-Matsya revision aligned to [SolvingMicroDSOPs](https://github.com/llorracc/SolvingMicroDSOPs) §§12–13: a "Stage composition" subsection and a perch table with a *Key transition or Bellman step* column. EGM channel discussion if the utility is invertible. |
| `dolo-plus-draft.yaml` | A minimal one-stage YAML (interior period only is acceptable). Any features that do not map cleanly onto canonical dolo-plus syntax **must be flagged inline with a `# workaround:` or `# unresolved:` comment** rather than silently fudged. |
| `verification.md` | One paragraph stating what was **accepted**, **edited**, or **rejected** from Matsya's output, and why — verified against the published paper, not only the ballpark summary. |
| `matsya-session.txt` | A single line: the `--session` string used on every Matsya call for this item (e.g. `topics2026-<citekey>`). Staff can inspect the server-side conversation by session name; you do not paste the transcript. |

The three workaround categories you are most likely to hit are **mechanical (non-optimized) deductions**, **$\hat{\Gamma}^{1-\gamma}$-style value-function scaling inside expectations**, and **state-contingent shock distributions**. Flag them; do not hide them.

### 3. Asset layer — required in part

| File | Required? | Content |
|------|-----------|---------|
| `<citekey>.pdf` | required | The paper. If license forbids redistribution, replace with a DOI-only pointer in `_intro.ipynb`. |
| `<citekey>.mmd` | recommended | Pandoc-converted markdown of the paper. Much easier for Cursor / Claude / Matsya to ingest than PDF. Produce via `pandoc <citekey>.pdf -o <citekey>.mmd` or equivalent. |
| `references.bib` | required | Bib entries cited from `_prior-literature.ipynb` and `_summary.ipynb`. |
| `self.bib` | recommended | The paper's own bib entry. Keeps the paper citation separable from its context. |
| `subsequent-literature.bib` | required if the notebook is non-empty | Bib entries cited from `_subsequent-literature.ipynb`. |
| Figures / tables (e.g. `fig1.png`, `Table2.png`) | as needed | Use paper's own labels where possible. |

### 4. REMARK-ready extension — optional

If the formalization layer has stabilized and you have working code, add a `replication/` subdirectory with `reproduce.sh`, `CITATION.cff`, `binder/environment.yml`, and a validated (not draft) dolo-plus stage. At that point you are eligible to move the item to [REMARK](https://github.com/econ-ark/REMARK) or [DemARK](https://github.com/econ-ark/DemARK) per the criteria in those repos.

---

## Machine-readable metadata (for AI indexing)

Ballpark entries are designed to be discovered and cited by both humans and AI agents. The `index.md` frontmatter and an optional `AGENTS.md` provide the structured signals that make this work.

### Required frontmatter fields on `index.md`

```yaml
---
title: "<Paper title> — Ballpark Entry"
schema_type: ScholarlyArticle              # schema.org type; Dataset also acceptable
about:
  doi: 10.XXXX/YYYY                        # paper DOI
  authors: [LastName, LastName, LastName]
  year: 2019
  journal: American Economic Review
keywords: [kebab-case, tags]               # free-form topical tags
econ_ark_topic:                            # controlled vocabulary — pick from:
  - HA-macro                               #   HA-macro, lifecycle, wealth-distribution,
  - wealth-distribution                    #   monetary, fiscal-policy, optimal-taxation,
  - lifecycle                              #   housing, labor, business-cycles,
                                           #   computational-methods, open-economy,
                                           #   liquidity-trap, demographics,
                                           #   financial-crisis, inequality
jel: [D31, E21, J62]                       # JEL codes (array)
difficulty: stretch                        # good-first-ballpark | stretch | research-grade
tier: formalized                           # draft | primer | formalized — see "Ballpark tiers" below
has_formalization_layer: true              # true iff the formalization-layer files exist
ballpark_contributor:
  name: "<name>"
  orcid: "0000-0000-0000-0000"             # optional but strongly encouraged
updated_by:                                # one entry per material revision; most recent last
  - name: "<name>"
    orcid: "..."
    date: 2026-01-27
---
```

MyST renders this frontmatter as JSON-LD on the published page, which Google Scholar, LLM training pipelines, and retrieval agents recognize. The same frontmatter powers the browsable catalog's filter UI (one source of truth).

### Optional frontmatter extensions (recommended)

```yaml
doi: 10.5281/zenodo.XXXXXXX                # Zenodo DOI for this ballpark entry itself
superseded_by: https://github.com/econ-ark/REMARK/...   # once promoted
requires: [CRRA, EGM, bequest-utility]     # model features — free-form tags
```

### `AGENTS.md` (required for items with a formalization layer; recommended otherwise)

A short structured brief aimed at coding agents (Claude Code, Cursor, etc.) that a user's local session will read when the directory is opened. Distinct from the human-readable `index.md`. See the [Benhabib_et_al_2019 worked example](models/We-Would-Like-In-Econ-ARK/Benhabib_et_al_2019/AGENTS.md).

Purpose:

- Point agents at the **right file to read first** (the SMD-polished excerpt, not the paper PDF).
- Surface the **Matsya session name** so new calls continue the existing thread.
- List **known workarounds** / unresolved features so agents don't re-discover them.
- Suggest **common next tasks** so agents proposing work have a grounded starting point.

#### How to produce your `AGENTS.md`

Copy the template below into `AGENTS.md` in your item directory and fill in the six sections. Every section has a grounded source in files you have already produced — you should not be inventing content.

| Section | Where its content comes from |
|---|---|
| **Paper** | `<citekey>_intro.ipynb` — citation, DOI, one-sentence pitch of why the paper is in-ballpark. Copy verbatim; this is the one place duplication with `index.md` is intentional, because the agent may open `AGENTS.md` first. |
| **If a user asks to work on this item** | `<citekey>_summary.ipynb` (section "The Model") is the authoritative recursive statement. `<citekey>.mmd` is the AI-friendly paper source. If your formalization layer is present, point at `bellman-excerpt-SMD-polished.md` as "read first" instead of the summary notebook. |
| **Formalization status** | Tick which layer files you committed: `bellman-excerpt.md`, `bellman-excerpt-SMD-polished.md`, `dolo-plus-draft.yaml`, `verification.md`, `matsya-session.txt`. Be honest about what is not yet present. |
| **Known model features requiring attention** | Pull from `verification.md` (the items you rejected or edited) and from the inline `# workaround:` / `# unresolved:` comments in `dolo-plus-draft.yaml`. This is the single most useful section for an agent — it is the list of things it should not re-discover. If the formalization layer is absent, list the model features you already know will be awkward (state-contingent shocks, mechanical deductions, non-standard normalizations, etc.). |
| **Common next tasks** | List what you intentionally left undone. Examples from real items: *"add terminal-period stage to YAML"*, *"formalize the dynasty wrapper"*, *"add age-varying wage overrides"*. Cite the specific file or line a next-task should touch. Do **not** list tasks you would have liked to do but have no grounding for. |
| **Workflow reminders** | Mostly boilerplate. Keep the Matsya session-naming convention (`topics2026-<slug>` for coursework), the paper-verification reminder, and the workaround-comment convention. Delete anything that does not apply to your item. |

**Template** (copy and fill in):

````markdown
# Ballpark entry: <Authors> (<Year>)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing content lives in [`index.md`](index.md).

## Paper

- **Citation:** <Authors (Year), "Title," Journal vol(issue), pages>.
- **DOI:** [<doi>](https://doi.org/<doi>)
- **Core model:** <one-sentence description: lifecycle / HA / OLG / ..., key state and control, what's stochastic, what closes the problem>.
- **Why in-ballpark:** <one sentence: what makes this paper interesting for Econ-ARK>.

## If a user asks to work on this item

1. **Read first:** <file> — <why this is authoritative>.
2. **Paper source for AI ingestion:** `<citekey>.mmd` (Pandoc-converted). Prefer this over `<citekey>.pdf`.

## Formalization status

- Explicit recursive formulation: <present in `_summary.ipynb` | not yet stated>.
- `bellman-excerpt.md`: <committed | not committed>.
- `dolo-plus-draft.yaml`: <committed | not committed>.
- `verification.md`: <committed | not committed>.
- `matsya-session.txt`: <committed | not committed>.

## Known model features requiring attention in a formalization pass

- <feature 1>: <what's awkward and why; how you worked around it or plan to>.
- <feature 2>: ...
- <feature 3>: ...

## Common next tasks (grounded)

1. <task 1, tied to a specific file or section>.
2. <task 2>.
3. <task 3>.

## Workflow reminders

- **Matsya session:** use `topics2026-<slug>` for new work on this item.
- **Paper verification:** Matsya output must be checked against the paper PDF (or `.mmd`), not only against the ballpark `_summary.ipynb`.
- **When flagging workarounds in YAML:** use inline `# workaround:` or `# unresolved:` comments rather than silently fudging non-canonical syntax.
````

**AI-assisted drafting (recommended).** Once your formalization layer is present, ask a coding agent (Claude Code, Cursor) to draft `AGENTS.md` from your item's files:

> Read `index.md`, `<citekey>_intro.ipynb`, `<citekey>_summary.ipynb`, `bellman-excerpt-SMD-polished.md`, `dolo-plus-draft.yaml`, and `verification.md` in this directory. Draft an `AGENTS.md` following the template in the repo-root `CONTRIBUTING.md`. Do not invent content — if a section lacks a grounded source in these files, write **TBD** for that section and explain what you would need.

**Then review carefully.** Agents occasionally invent plausible-sounding "next tasks" or "workarounds" that are not grounded in your verification notes. Rewrite anything you cannot trace to a specific file. The point of `AGENTS.md` is that a later agent can trust it; that trust is wasted if you pass through hallucinations.

### Repo-level artifacts (maintained centrally, not per item)

- [`llms.txt`](llms.txt) at the repo root — a plain-text sitemap for LLMs following the [llmstxt.org](https://llmstxt.org) convention. Update this file when you add or rename an item.
- `items.json` (auto-generated from frontmatter during the MyST build) — machine-readable catalog; one object per item with the full frontmatter flattened.
- `sitemap.xml` and `atom.xml` — emitted by the MyST build.

### Content-form conventions for LLM legibility

- **Every committed `.ipynb` is also exported to `.md`** at build time. Reviewers and LLMs read the `.md`; the `.ipynb` remains authoritative.
- **Paper ships as `.mmd` alongside `.pdf`** where license permits (Pandoc-converted markdown — much easier for Cursor / Claude / Matsya to ingest than PDF).
- **Every equation carries an `:alt:` attribute** describing it in prose, for models that can't render LaTeX but can read HTML.
- **Every figure has alt-text** (WCAG and LLM indexability are the same action).

### Model structure as first-class data (stretch)

For items with a committed `dolo-plus-draft.yaml`, a generated `model.json` extracts the stage(s) into a programmatic form. This lets retrieval agents answer structural queries like *"find all ballpark items with an EGM-compatible interior stage"* or *"which items have Markov-chain employment states."* The extractor is maintained centrally; contributors do not hand-write `model.json`.

### AI provenance (optional)

If AI tools materially shaped the formalization layer, add `ai-provenance.md` documenting which tools played which role and linking the session artifacts. This gives both credit and traceability.

---

## What does **not** belong in a ballpark item

- `_build/` — gitignored.
- Build-artifact directories named by UUID (e.g. LaTeX `*.aux`, `*.out`, `*.synctex.gz` trees) — gitignored.
- `*.slides.html` — generated on demand; the source `.ipynb` is authoritative.
- Duplicate summary notebooks from older naming conventions (e.g. both `<citekey>_summary.ipynb` and `<ShortName>_summary.ipynb`) — delete the duplicate at refactor time.
- `<citekey>.zip` — the `.pdf` is enough; `.zip` is only appropriate if it contains replication code, in which case it belongs under `replication/`.
- An item-level `README.md` duplicating the project `README.md` — `index.md` is the entry point; an item-level `README.md` is redundant.

---

## Authorship and provenance

The intro notebook carries provenance as visible section content, not buried frontmatter:

```markdown
**Original ballpark author:** <name>, <YYYY-MM-DD>
**Updated by:** <name>, <YYYY-MM-DD>
**Superseded by:** <link to REMARK / DemARK if promoted>
```

When you revise an existing item, add (do not overwrite) an **Updated by** line. When an item is promoted to REMARK or DemARK, add a **Superseded by** pointer rather than deleting the ballpark entry — the ballpark retains historical interest.

---

## Ballpark tiers

Ballpark items progress through three tiers of increasing formalization completeness — analogous in spirit to REMARK's standard/published distinction but scoped entirely to *pre-implementation* work. The ballpark's job is to land a well-specified model ready for a coder; the implementation step (working `reproduce.sh`, `CITATION.cff`, `binder/environment.yml`) happens in [REMARK](https://github.com/econ-ark/REMARK) / [DemARK](https://github.com/econ-ark/DemARK), not here.

Each tier is a **plateau** with a concrete, reviewable qualifying checklist. Contributors can stop at any tier indefinitely.

| Tier | One-line characterization | Typical effort from the previous tier (AI-assisted, PhD-course-assignment units) |
|------|---------------------------|----------------------------------------------------------------------------------|
| **Draft** | Paper identified, claimed, and minimally cataloged. | **≈ 1 weekly assignment** (from zero / from a `wanted-ballpark` issue). |
| **Primer** | A reader can understand the paper and its context without reading the paper. | **≤ 2 weekly assignments** (from Draft). |
| **Formalized** | The model is stated in modular-DDSL form, with a dolo-plus YAML draft. | **≤ 2 weekly assignments** (from Primer). |

Each name presupposes the tier below it: a *primer* is a completed introductory treatment of what a *draft* only sketches; a *formalized* specification is the rigorous re-expression of what the *primer* states informally. Rank order is unambiguous from the names alone.

(A pre-tier state, **Wanted**, is an open issue labeled `wanted-ballpark` with bibliographic info. It has no directory.)

### Draft

*"I am claiming this paper and committing to minimal cataloging."*

Qualifying checklist:

- [ ] Item directory exists under `models/We-Would-Like-In-Econ-ARK/<citekey>/` (or `empirical/<citekey>/`).
- [ ] `index.md` with required frontmatter (including `tier: draft`).
- [ ] `<citekey>_intro.ipynb` with citation, DOI link, **Original ballpark author + date**, and a 3-sentence pitch of why the paper is in-ballpark for Econ-ARK.
- [ ] `references.bib` (may be empty at Draft).
- [ ] Paper committed as `<citekey>.pdf` OR replaced by a DOI pointer with a license note in `_intro.ipynb`.

Draft is the minimum mergeable contribution. It converts a `wanted-ballpark` issue into a claimed directory.

### Primer

*"A graduate student can orient themselves around this paper without reading it."*

Qualifying checklist — everything in Draft, plus:

- [ ] `<citekey>_prior-literature.ipynb` situating the paper in its foundational literature, with `{cite:t}` citations resolving from `references.bib`. **Cite at least 3 and no more than 6 prior papers** — enough to establish context, few enough that the notebook stays focused.
- [ ] `<citekey>_summary.ipynb` with (a) a non-technical motivation + findings overview, and (b) a **"The Model"** section stating the recursive formulation **explicitly**: no `u(c)` placeholders, explicit CRRA or EZ kernel, explicit bequest function (if any), explicit transitions, explicit shock distributions, explicit constraint set.
- [ ] `<citekey>_subsequent-literature.ipynb` + `subsequent-literature.bib`. **No hard citation count is required**, since recent papers may have few subsequent citations; the notebook should cite whatever subsequent work exists (typically 0–6 papers) and note explicitly if the paper is too recent to have accumulated much. (Paper eligibility itself is gated by the Google-Scholar-≥3 rule in "Before you start.")
- [ ] `self.bib` with the paper's own bib entry.
- [ ] `<citekey>.mmd` (Pandoc-converted markdown of the paper) unless license forbids — this is what Cursor / Claude / Matsya read most effectively.
- [ ] `myst.yml` configured; `myst build` completes cleanly.
- [ ] `index.md` `{include}`s all four exposition notebooks in order.

Primer is the current aspirational target for the typical legacy-slideware refactor. [`Benhabib_et_al_2019`](models/We-Would-Like-In-Econ-ARK/Benhabib_et_al_2019/) is the reference instance of this tier.

### Formalized

*"The model has been translated into a modular-DP specification ready for a coder."*

Qualifying checklist — everything in Primer, plus:

- [ ] `bellman-excerpt.md` — standalone modular-DDSL Bellman statement (symbol table, timing, perch decomposition, stage operator).
- [ ] `bellman-excerpt-SMD-polished.md` — post-Matsya SMD-aligned revision with perch table and EGM channel discussion.
- [ ] `dolo-plus-draft.yaml` — one-stage YAML (interior period sufficient); all unresolved features flagged with inline `# workaround:` or `# unresolved:` comments.
- [ ] `verification.md` — one paragraph stating what was accepted / edited / rejected from Matsya's output, compared against the published paper (not only the `_summary.ipynb`).
- [ ] `matsya-session.txt` — the `--session` string used, if AI-assisted; or a file containing `N/A — hand-written` otherwise.
- [ ] **`AGENTS.md` — required at Formalized.** See the section above for how to produce it.

Formalized is the ballpark's top tier. A *Formalized* item is ready to be picked up by a coder (human or agent) and promoted to REMARK or DemARK — the implementation work happens there, not here.

### Beyond Formalized: promotion out of the ballpark

Once a Formalized item has working code reproducing paper results, it is eligible for promotion to [REMARK](https://github.com/econ-ark/REMARK) (for substantial replications) or [DemARK](https://github.com/econ-ark/DemARK) (for demonstrations). REMARK itself has a tiering (*standard* vs. *published*-with-DOI); those criteria are documented at the REMARK repo and are not this repository's concern.

When an item is promoted, add a **Superseded by** pointer in `_intro.ipynb` rather than deleting the ballpark entry — the entry retains historical and pedagogical interest.

### Promotion mechanics within the ballpark

- Each tier is a plateau; indefinite residence is fine.
- A **promotion PR** adds the next tier's files and updates `tier:` in the frontmatter.
- PR title pattern: `Promote <citekey> to Primer` / `Promote <citekey> to Formalized`.
- The PR body quotes the qualifying checklist for the target tier and ticks each box with a file-line citation.
- **Tier regression** (e.g. Formalized → Primer) is allowed when an item's formalization is found to be incorrect and is being withdrawn for revision; it should be rare and the PR must explain the defect.

### Badges

Each item's rendered page carries a tier badge (`Draft` / `Primer` / `Formalized`) at the top. Catalog cards show the badge so visitors can filter by tier (e.g. *"show me all Primer items that need promotion to Formalized"* — a natural call-to-contribute).

The badge derives from the `tier:` frontmatter field; the MyST build pipeline renders it automatically. Contributors do not hand-insert badge markdown.

### Effort calibration (for contributors and instructors)

Effort is expressed in PhD-course-assignment units assuming AI-assisted workflow (Cursor + Claude + Matsya). These estimates are generous upper bounds:

| Step | Upper bound |
|------|-------------|
| → Draft | 1 weekly assignment |
| Draft → Primer | ≤ 2 weekly assignments |
| Primer → Formalized | ≤ 2 weekly assignments |
| Total from zero to Formalized | ≤ 5 weekly assignments |

These estimates guide course-project scoping: a full semester leaves ample room for a student to take a paper all the way to Formalized and start on the replication step (which then belongs in REMARK, not here).

---

## Pre-merge checklist

The target tier determines the checklist. Copy the target tier's qualifying checklist from the section above into your PR body and tick each box with a file-line citation. **In addition**, every PR (regardless of tier) must confirm:

- [ ] `index.md` `{include}`s exactly the four exposition notebooks, in order (T2 and above).
- [ ] `myst.yml` builds the item without errors (`myst build` in the item directory).
- [ ] Every `{cite:t}` reference resolves against the bib files.
- [ ] Every figure the notebooks reference exists and renders.
- [ ] `_intro.ipynb` carries visible **Original ballpark author** and (if applicable) **Updated by** lines.
- [ ] No `_build/`, UUID build directories, or `.slides.html` files are committed.

---

## Submitting

1. Fork the repo and branch from `master` with a descriptive name (e.g. `add-<citekey>` or `refactor-<citekey>`).
2. Commit the item in its own directory under `models/We-Would-Like-In-Econ-ARK/<citekey>/` (or `empirical/<citekey>/`).
3. Open a PR titled `Add <citekey>` or `Refactor <citekey>`.
4. In the PR description, state which layers you produced and which you intentionally skipped.
