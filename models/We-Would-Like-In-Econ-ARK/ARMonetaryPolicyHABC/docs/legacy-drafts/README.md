# Legacy drafts (superseded; retained for history)

These files are **pre-iteration** drafts for Algan-Ragot
(2009), produced before the Opus 4.7 review, the Matsya Evaluate
turn, and the Primer-tier exposition layer. They are kept here so a
reader can trace how the formalization and the four-notebook layout
converged, but they are **not** the canonical statement for this
item.

The single canonical Bellman statement for this item, as
[`CONTRIBUTING.md`](../../../../CONTRIBUTING.md) line 52 requires, is

    ../../bellman-excerpt.md

at the item root, alongside `dolo-plus-draft.yaml`, `verification.md`,
`matsya-session.txt`, and `AGENTS.md`.

## Why they are kept

| File | What it has that the canonical one does not |
|------|---------------------------------------------|
| `arg2009-bellman-excerpt.md`            | Verbatim transcription of the paper's CES-with-leisure utility kernel `u(c,m,l) = (1/(1-sigma)) * [ (omega*c^((eta-1)/eta) + (1-omega)*m^((eta-1)/eta))^(eta/(eta-1)) * (1-l)^psi ]^(1-sigma)` from `ToramanSY_AlganRagot2009_Summary.ipynb`. The canonical `bellman-excerpt.md` carries this in its symbol-table and timing form, but the verbatim equation here is convenient when reconciling against the paper's `.mmd`/`.pdf` (deferred). |
| `arg2009-improved-stage-description.md` | The original four-control encoding (`c, m, l, a_next`) before the Matsya Evaluate turn (Flag C, PROVISIONAL → resolved) recommended eliminating `a_next` and pinning it via the budget identity. Useful as a record of the iteration step. |
| `ToramanSY_AlganRagot2009_Summary.ipynb` | Single-notebook ballpark digest produced by S. Y. Toraman in 2020 — the original Primer-tier-style summary of the paper's model, results, and conclusion. Superseded by the four-notebook exposition layer (`../../ARMonetaryPolicyHABC_intro.ipynb`, `_prior-literature.ipynb`, `_summary.ipynb`, `_subsequent-literature.ipynb`); the model statement in the canonical `_summary.ipynb` is adapted from this digest with explicit credit. Kept here for authorship provenance and to make the original Toraman wording recoverable. |

## Why they should not be promoted back to the item root

`CONTRIBUTING.md` line 52:
> `bellman-excerpt.md` is the **single evolving artifact** that this
> loop produces — **not two separate files** for "before Matsya" and
> "after Matsya."

The two Bellman drafts are exactly the "before Matsya" version that
line 52 warns against keeping at the item root. They are demoted here
to honour that constraint while still preserving the iteration
history.

The Toraman 2020 single-notebook digest is demoted by an analogous
rule for the exposition layer: `CONTRIBUTING.md`'s Primer-tier section
expects exactly four canonically-named notebooks (`_intro.ipynb`,
`_prior-literature.ipynb`, `_summary.ipynb`,
`_subsequent-literature.ipynb`) at the item root. A second summary
notebook with a different naming convention would be picked up by
auto-discovery tooling alongside the canonical files (this is the
exact issue PR #66 ran into with `BBL_summary.ipynb`, resolved by
deletion in commit `f21c5e2`). Demoting rather than deleting preserves
authorship credit; the canonical `_summary.ipynb` cites this file
explicitly in its preamble.
