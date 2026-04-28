# Accept / edit / reject log for Opus 4.7 review

> Companion to [`opus-prompt.md`](opus-prompt.md) and [`opus-review.md`](opus-review.md).
> Discipline from CONTRIBUTING.md `verification.md` convention — one-line reasoning per suggestion.
> Recommendations below are **provisional**; the ballpark contributor has final say before commit.
>
> **Path note (post-PR-#72 review).** When this table was first written, the four formalization deliverables (`bellman-excerpt.md`, `dolo-plus-draft.yaml`, `verification.md`, `matsya-session.txt`) lived under `docs/`. After PR #72's review, they were relocated to the **item root** so that `CONTRIBUTING.md`'s automated Formalized check can find them. The link targets in the "Target file(s)" column have been updated to point at the new locations; the **judgments themselves** are unchanged.

| # | Opus suggestion (short) | Severity | Recommendation | One-line reasoning | Target file(s) |
|---|--------------------------|----------|----------------|--------------------|----------------|
| 1 | Add exposition-layer Draft skeleton (`index.md`, `_intro`, `_summary`, `references.bib`, paper pointer) | Must-fix | **Edit (partial in this PR)** | Full four-notebook refactor is out of scope for a `formalize-finalize` PR; add a minimal `index.md` stub with frontmatter + citation-count pointer, defer full exposition rewrite to a follow-up PR. | `models/.../ARMonetaryPolicyHABC/index.md` (new, minimal) |
| 2 | Rewrite `verification.md` against the published paper (not the summary) | Must-fix | **Closed (paper-grounded)** | Originally edited-and-deferred (paper PDF was not in-repo). On the `armonetarypolicyhabc-paper-grounded` branch the paper was read directly and `verification.md` was rewritten to cite specific equations: eq. (15) (utility), eq. (16) (budget), eq. (17) (`a' >= 0`), §3.3.2 (Markov calibration), §4.2 (`mu` redistribution). Three previously-open paper gaps closed (`a_min = 0`; `mu` sign rule; full Markov calibration). YAML `# unresolved:` flags propagated accordingly (HEAD `dolo-plus-draft.yaml`). The only remaining utility deferral is the spec-side CES-encoding gap, retained as item #1 below. | [`verification.md`](../verification.md), [`dolo-plus-draft.yaml`](../dolo-plus-draft.yaml), [`self.bib`](../self.bib) |
| 3 | Close the symbol-table: add CES / aggregate / inflation rows | Must-fix | **Accept** | Directly addresses CONTRIBUTING's "every object referenced" rule and unblocks downstream items. | [`bellman-excerpt.md`](../bellman-excerpt.md) |
| 4 | Resolve `Pi` (Markov) vs `Pi_t` (inflation) collision | Must-fix | **Accept** | Economics-correctness: genuine ambiguity that will derail any later general-equilibrium pass. | `bellman-excerpt.md`, `dolo-plus-draft.yaml`, `verification.md`, `docs/legacy-drafts/arg2009-improved-stage-description.md` |
| 5 | Fix `mu` domain from `R+` to `R` | Must-fix | **Accept (flagged)** | Matches the inflation-tax redistribution channel in the summary; keep the "verify sign rule in paper" note as an `# unresolved:` flag in YAML. | [`dolo-plus-draft.yaml`](../dolo-plus-draft.yaml), [`bellman-excerpt.md`](../bellman-excerpt.md) |
| 6 | Resolve `m_d` vs `m` naming across YAML and bellman-excerpt | Must-fix | **Edit** | Prefer (ii): keep `m_d` in YAML, add a symbol-table row in `bellman-excerpt.md` and a one-line YAML comment. Renaming is larger-touch and risks breaking Matsya cache. | `dolo-plus-draft.yaml`, `bellman-excerpt.md` |
| 7 | Declare `Pi` in YAML `parameters:` block | Must-fix | **Accept** | Undeclared symbol is a dolo-plus / Matsya error; trivial fix. | [`dolo-plus-draft.yaml`](../dolo-plus-draft.yaml) |
| 8 | Explicitly label identity / degenerate movers | Must-fix | **Accept** | CONTRIBUTING literally enumerates this as a reviewer-discernibility requirement. | [`bellman-excerpt.md`](../bellman-excerpt.md), [`dolo-plus-draft.yaml`](../dolo-plus-draft.yaml) |
| 9 | Add aggregate-scoping + notation-collision bullets to AGENTS.md | Must-fix | **Accept** | Closes an AGENTS.md completeness gap; grounded in files already committed. | [`AGENTS.md`](../AGENTS.md) |
| 10 | Add conditional EGM paragraph to `bellman-excerpt.md` | Nice-to-have | **Reject (defer)** | EGM channel depends on utility reconciliation (items #5-#6 upstream) and on seeing the paper's functional forms; forcing a paragraph now would over-commit. Defer to a follow-up PR after utility alignment. | [`bellman-excerpt.md`](../bellman-excerpt.md) |

---

## Top 3-5 selected for implementation in this PR

Selected to (a) respect the assignment's 3-5 accepted-changes cap and (b) maximize Formalized-tier progress per change:

1. **#3 + #4 combined — symbol table closure + `Pi` / `Pi_t` rename**.
2. **#5 + #7 combined — `mu` domain fix + `Pi` parameter declaration** (small YAML cleanups; same file; tested together).
3. **#6 — `m_d` documented vs `m`** (one-line YAML comment + bellman-excerpt symbol-table row).
4. **#8 — explicit identity-mover labels** (Stage 1 arrival→decision and Stage 2 decision→continuation).
5. **#9 — AGENTS.md completeness bullets** (aggregate scoping + notation collision pointer).

Items #1 (full exposition refactor) and #2 (paper-grounded verification) were **originally recorded as deferred** for a separate PR after the paper PDF / `.mmd` lands in-repo; a minimal `index.md` stub and a rephrased `verification.md` were included in PR #72 so the state did not over-claim.

## Update (post-PR-#72, on branch `armonetarypolicyhabc-paper-grounded`)

Item **#2 is now closed** (see status update in the table above): the paper was read in full from a user-supplied PDF (HAL preprint `hal-01170621v1`), `self.bib` was added with the BibTeX entry, `index.md` and `AGENTS.md` were enriched with DOI / journal / volume / pages / JEL, `verification.md` was rewritten line-by-line against paper §3.1.1 + eqs. (15)–(22) + §3.3.2 + §4.2, and the YAML `# unresolved:` flags for `a_min`, `P_e` calibration, and the wealth-on-hand transition were closed (or refactored into `# resolved (paper §X)` pointers). The branch's commit log is the single source of truth for what changed.

The publication year stays **2009** across the item (per ballpark contributor decision; consistent with the directory slug `ARMonetaryPolicyHABC`, the legacy-draft filenames `arg2009-*.md`, and the DOI suffix `red.2009.05.001`).

Item **#1 (full exposition refactor)** remains deferred: the canonical four-notebook layout (`<citekey>_intro.ipynb`, `_prior-literature.ipynb`, `_summary.ipynb`, `_subsequent-literature.ipynb`) is a separate ballpark-promotion task and out of scope for the `paper-grounded` branch.

The only outstanding paper-vs-formalization deferral is the **utility-kernel CES encoding** (paper eq. (15)): the YAML still uses a separable workaround. This is a *spec-side* gap (locating a canonical dolo-plus example with a CES inner aggregator under a CRRA outer wrapper) rather than a paper gap (eq. (15) is now transcribed verbatim at every relevant location).
