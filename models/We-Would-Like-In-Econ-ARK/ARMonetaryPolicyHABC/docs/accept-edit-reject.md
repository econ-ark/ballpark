# Accept / edit / reject log for Opus 4.7 review

> Companion to [`opus-prompt.md`](opus-prompt.md) and [`opus-review.md`](opus-review.md).
> Discipline from CONTRIBUTING.md `verification.md` convention — one-line reasoning per suggestion.
> Recommendations below are **provisional**; the ballpark contributor has final say before commit.
>
> **Path note (post-PR-#72 review).** When this table was first written, the four formalization deliverables (`bellman-excerpt.md`, `dolo-plus-draft.yaml`, `verification.md`, `matsya-session.txt`) lived under `docs/`. After PR #72's review, they were relocated to the **item root** so that `CONTRIBUTING.md`'s automated Formalized check can find them. The link targets in the "Target file(s)" column have been updated to point at the new locations; the **judgments themselves** are unchanged.

| # | Opus suggestion (short) | Severity | Recommendation | One-line reasoning | Target file(s) |
|---|--------------------------|----------|----------------|--------------------|----------------|
| 1 | Add exposition-layer Draft skeleton (`index.md`, `_intro`, `_summary`, `references.bib`, paper pointer) | Must-fix | **Edit (partial in this PR)** | Full four-notebook refactor is out of scope for a `formalize-finalize` PR; add a minimal `index.md` stub with frontmatter + citation-count pointer, defer full exposition rewrite to a follow-up PR. | `models/.../ARMonetaryPolicyHABC/index.md` (new, minimal) |
| 2 | Rewrite `verification.md` against the published paper (not the summary) | Must-fix | **Edit** | The paper PDF / `.mmd` is not yet in-repo; rephrase the existing paragraph to state explicitly that verification against the **paper** is a deferred next step, so the file no longer over-claims. | [`verification.md`](../verification.md) |
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

Items #1 (full exposition refactor) and #2 (paper-grounded verification) are **recorded as deferred** for a separate PR after the paper PDF / `.mmd` lands in-repo; a minimal `index.md` stub and a rephrased `verification.md` will still be included in this PR so the current state does not over-claim.
