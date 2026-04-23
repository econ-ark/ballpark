# Verification (Matsya / AI iteration vs. the paper)

This file records, for each element of the formalization layer, whether the gap
is a **paper gap** (something the paper does not specify or the summary has not
yet surfaced) or a **dolo-plus spec gap** (something the canonical dolo-plus /
DDSL corpus does not yet document an idiom for). The distinction matters: paper
gaps close by reading the paper; dolo-plus spec gaps close by locating a
canonical example or consulting a dolo-plus maintainer.

## Accept / edit / reject — stage structure

**Accepted.** Matsya's two-stage decomposition — **decision** followed by
**shock realization** — matches the max-then-expectation structure in the
household Bellman statement summarized in
`ToramanSY_AlganRagot2009_Summary.ipynb` and keeps optimization separate from
the Markov update on productivity. The Matsya Evaluate turn (Turn captured in
`docs/matsya-evaluate-turn.txt`) explicitly confirmed this decomposition as
**CANONICAL**, matching the `cons_stage` + `noport_stage` pattern in the
retrieved dolo-plus corpus.

**Accepted.** The `m_d` (control) / `m` (poststate) split with the bridging
identity `m = m_d` is **CANONICAL** per Matsya's Evaluate turn, matching
`c` (control) / `a` (poststate) with `a = w - c` in `cons_stage.md`.

**Accepted (post-Matsya edit).** Three free controls `(c, m_d, l)` with `a'`
pinned by the budget identity in `dcsn_to_cntn_transition`. The pre-Matsya
draft carried four controls (including `a_next`); Matsya Flag C flagged this
as non-canonical, and the Improve commit adopted the recommended pattern.

## Accept / edit / reject — symbol conventions

**Edited.** The Markov kernel was renamed from `Pi` to `P_e` to remove a
collision with the inflation series `Pi_inf` on the aggregate side (deferred
to a later general-equilibrium pass; see `AGENTS.md`).

**Edited.** The transfer `mu` was moved from `R+` to `R` to accommodate the
inflation-tax redistribution channel, which can make net transfers negative
for some households.

**Edited.** Identity transitions in both stages are explicitly labelled as
`# degenerate: identity` so reviewers can distinguish "identity" from
"omitted."

**Edited (post-Matsya).** `P_e` is declared as a plain `@in R+` parameter, not
`@in StochasticMatrix`: the latter has no precedent in the canonical dolo-plus
corpus (Matsya Evaluate turn, Question 3, **UNRESOLVED**). Row-stochastic
semantics are carried instead by `@dist MarkovChain(P_e)` on the exogenous
block, which Matsya confirmed is the canonical pattern.

## Accept / edit / reject — utility kernel

**Rejected (as paper-faithful).** The separable CRRA + labor-disutility kernel
in `docs/dolo-plus-draft.yaml` is **not** paper-identical. The summary's
Bellman excerpt records a **CES composite over consumption and money with
leisure** parameterized by `(sigma, eta, omega, psi)` (rows now in
`docs/bellman-excerpt.md` symbol table). The current YAML therefore remains a
**computational scaffold** with explicit `# workaround:` flags. Replacing the
utility block with the paper's CES-with-leisure form is deferred item #1 in
`docs/accept-edit-reject.md`.

## Paper gaps vs. dolo-plus spec gaps

| Open issue | Paper gap? | Spec gap? | Next action |
|---|---|---|---|
| Utility kernel (CES-with-leisure vs. separable placeholder) | **Paper gap** — the paper specifies CES-with-leisure; our YAML uses a placeholder until we have the paper PDF / `.mmd` in-repo. | No — the CES form is expressible in dolo-plus. | Align YAML with the summary's CES block; flag any specific calibration values still missing from the paper. |
| Next-period resource mapping `q' = R·a + (1+r_m)·m` | **Paper gap** — the draft LoM has not been cross-checked against the paper's exact timing / return structure. | No. | Cross-check against Algan–Ragot (2009) §II when the paper is in-repo; amend YAML if needed. |
| Borrowing limit `a_min` | **Paper gap** — the paper-specific rule has not been transcribed. | No. | Transcribe from paper. |
| Transfer `mu` sign rule at the household level | **Paper gap** — net-transfer sign depends on the redistribution rule in the paper, which is summary-level. | No. | Transcribe from paper. |
| `P_e` numerical calibration (3×3 row-stochastic) | **Paper gap**. | No. | Transcribe from paper. |
| `P_e` declaration idiom (`@in StochasticMatrix` vs. plain + `@dist MarkovChain`) | No. | **Previously spec gap; now resolved** — Matsya Evaluate turn, Question 3. | Closed in the Improve commit. |
| Multi-control budget vs. budget-identity-pinning `a'` | No. | **Previously spec gap; now resolved** — Matsya Evaluate Flag C. | Closed in the Improve commit. |
| `cons_stage` / `noport_stage` two-stage pattern over Markov shocks | No. | **Not a spec gap** — Matsya confirmed CANONICAL in Turn 1. | No action. |

## Note on paper-grounding

CONTRIBUTING.md asks that verification compare against the **published paper**,
not only the ballpark summary. The paper PDF / `.mmd` is not yet in this item
directory, so every **paper-side** claim in the tables above is currently
grounded in the summary notebook and the `docs/arg2009-*.md` excerpts only.
Rewriting the accept / edit / reject lines to cite specific equation numbers
from Algan–Ragot (2009) is tracked as deferred item #2 in
`docs/accept-edit-reject.md` and is the single most-important verification
upgrade outstanding. The **spec-side** claims are grounded in the Matsya
Evaluate turn (`docs/matsya-evaluate-turn.txt`), which cites 15 chunks from
the `bellman-ddsl` and related repos.
