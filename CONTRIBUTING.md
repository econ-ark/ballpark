# Contributing a ballpark item

A **ballpark item** is a single paper's entry point into the Econ-ARK ecosystem: enough structure, context, and formalization that an ambitious graduate student can progress the paper from "interesting" through "formal recursive model" toward a [REMARK](https://github.com/econ-ark/REMARK) or [DemARK](https://github.com/econ-ark/DemARK) candidate in one semester.

This file specifies what a ballpark item should contain and how to submit one. For background on the project, see [README.md](README.md).

---

## Before you start

1. **Is the paper in scope?** Ballpark items are papers that are either (a) serious structural models producing interesting quantitative results, or (b) strong empirical evidence that begs for a model. See [README.md](README.md) for the two tracks (`models/` vs `empirical/`).
2. **Is it already here?** Check `models/We-Would-Like-In-Econ-ARK/` for an existing subdirectory under the paper's citekey. If one exists, open a PR improving it rather than creating a parallel entry.
3. **Is it listed but not yet claimed?** If there is a subdirectory but it is thin (legacy "slideware" — one notebook of markdown + figures), your contribution can be to refactor it to the canonical structure below.
4. **None of the above?** Open an issue naming the paper, the DOI, and the track (`models` / `empirical`), and we will confirm before you invest effort.

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

## Minimum viable contribution

Not every contributor will produce every layer. For a PR to be mergeable:

- **Minimum:** `index.md` + `<citekey>_intro.ipynb` (with explicit provenance) + `<citekey>_summary.ipynb` with an explicit "The Model" section + `references.bib` + paper PDF or DOI pointer.
- **Stretch (coursework-grade):** above + the full formalization layer.
- **REMARK-ready:** above + a working `replication/` subdir.

---

## Pre-merge checklist

Before opening a PR, confirm:

- [ ] `index.md` `{include}`s exactly the four exposition notebooks, in order.
- [ ] `myst.yml` builds the item without errors (`myst build` in the item directory).
- [ ] Every `{cite:t}` reference resolves against the bib files.
- [ ] Every figure the notebooks reference exists and renders.
- [ ] Paper PDF is either committed or replaced by a DOI pointer with a license note.
- [ ] `_intro.ipynb` carries visible **Original ballpark author** and (if applicable) **Updated by** lines.
- [ ] If the formalization layer is included: `dolo-plus-draft.yaml` flags all unresolved features with inline `# workaround:` / `# unresolved:` comments, and `verification.md` compares Matsya output to the published paper (not only the ballpark summary).
- [ ] No `_build/`, UUID build directories, or `.slides.html` files are committed.

---

## Submitting

1. Fork the repo and branch from `master` with a descriptive name (e.g. `add-<citekey>` or `refactor-<citekey>`).
2. Commit the item in its own directory under `models/We-Would-Like-In-Econ-ARK/<citekey>/` (or `empirical/<citekey>/`).
3. Open a PR titled `Add <citekey>` or `Refactor <citekey>`.
4. In the PR description, state which layers you produced and which you intentionally skipped.
