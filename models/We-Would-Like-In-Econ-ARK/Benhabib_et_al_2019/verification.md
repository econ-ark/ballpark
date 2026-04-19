# Verification of `dolo-plus-draft.yaml` against Benhabib, Bisin, and Luo (2019)

**Matsya session:** `topics2026-benhabib-demo` (Turn 4 produced the YAML; see `matsya-session.txt`).

**Source compared:** the published paper (`Benhabib_et_al_2019.mmd` / `.pdf`), §I (theoretical framework), not merely `_summary.ipynb`.

## Accepted from matsya's YAML

- **Stage structure** — the single-stage template with perches (arrival `a`, decision `m`, continuation `a_next`), within-stage transitions (`m = (1+r)*a + w`; `a_next = m - c`), backward mover (Bellman + EGM block), and identity forward mover (`V[<] = V`; `dV[<] = dV`) correctly encodes the paper's within-life deterministic lifecycle problem. Matches paper §I equations (2)–(5).
- **CRRA utility** `u(c) = c^(1-sigma)/(1-sigma)` matches paper §I exactly.
- **Warm-glow bequest kernel** `e(a) = A*a^(1-mu)/(1-mu)` matches paper §I exactly.
- **EGM sub-equations** (InvEuler, reverse transition `m[>] = a_next + c[>]`, MarginalBellman envelope `dV = c^(-sigma)`) are textbook-standard for CRRA buffer-stock problems, and match the pattern used in the instructor worked example (`workspace-course-topics/artifacts/matsya-workflow-example-benhabib-2019/dolo-plus-interior-stage-draft.yaml`).
- **Omission of `exogenous` block** is correct — the paper's §I explicitly states "$r$ and $w$ are stochastic over generations only: agents face no uncertainty within their life span."

## Edited (relative to the paper's own notation)

- **Decision-perch state `m` introduced** in place of the paper's implicit use of `a` as both value-function state and constraint bound. The paper writes `a' = (1+r)a - c + w` with constraint `0 ≤ c ≤ a` — internally inconsistent as written (see `_summary.ipynb` → "The Model" → "Notation convention" for the resolution). The YAML adopts the clean convention, consistent with `bellman-excerpt.md`.
- **Poststate named `a_next`** rather than the paper's `a'`; equivalent but avoids the quote-mark ambiguity in YAML syntax.
- **Parameterized-family structure made explicit** — the paper states but does not emphasize that the within-life problem is indexed by a $(\tau, r)$ type drawn at birth. The YAML surfaces this via a (speculative) `calibration_family` block; the paper itself solves 50 such problems in the baseline estimation without naming them a family.

## Rejected

- Nothing from matsya's YAML output was rejected outright. The two speculative blocks (`terminal`, `calibration_family`) are preserved **with matsya's `# SPECULATIVE` flags intact**, per CONTRIBUTING.md's rule that uncanonical features be flagged rather than silently fudged.

## Flagged as speculative (not paper gaps — dolo-plus spec gaps)

Matsya's YAML flags two blocks as lacking canonical dolo-plus syntax:

1. **`terminal:` block.** The terminal boundary wiring $V_{[\succ]} = e(a_{[\succ]})$, $dV_{[\succ]} = A\,a_{[\succ]}^{-\mu}$ is the **correct pattern** per matsya's Turn 3 recommendation, but no canonical dolo-plus syntax for terminal-boundary blocks was found in matsya's retrieved corpus. The paper is **not** the bottleneck here — the bequest kernel is fully specified; what's missing is the dolo-plus idiom.

2. **`calibration_family:` block.** The option-A calibration-override pattern (per matsya Turn 2) is the **correct approach** for a fixed-at-birth $(\tau, r)$ type family, but no canonical dolo-plus syntax for such families was found. Again, the paper is not the bottleneck — the paper specifies the 10 × 5 type space and the within-life-constant structure fully; what's missing is the dolo-plus idiom for instantiating the template across the family.

## Open items not yet in the YAML

Items from `bellman-excerpt.md` → "Still open" that remain outside this draft:

- **Lifecycle nest with age-varying $w_t(\tau)$.** The YAML has `w` as a scalar parameter; 36 per-age values times 10 types = 360 calibration entries would be needed. The paper provides these as a 10 × 6 age-bracket table (paper Table 1); a complete YAML would reference this table via interpolation rather than hard-coding. Dolo-plus syntax for per-age parameter overrides on a repeated stage was not asked of matsya in this iteration.
- **Section IIID wealth-dependent $r$ extension.** Explicitly out of scope for this baseline YAML (see `bellman-excerpt.md` → "Still open" §6). Would require a separate YAML with a state-contingent (rather than fixed-at-birth) $r$ exogenous process.

## Verdict

**The paper's description of its model is sufficient to construct a dolo-plus YAML formalization.** Matsya did not request any additional model information beyond what was provided in `bellman-excerpt.md`. The remaining gaps are **dolo-plus spec gaps** (canonical syntax for terminal-boundary blocks and calibration-family instantiation), not paper gaps.

The committed `dolo-plus-draft.yaml` is a Formalized-tier draft per `CONTRIBUTING.md`'s definition: it encodes what is canonically encodable, and flags what is not with inline `# SPECULATIVE` comments rather than silently fabricating. A full cleanup of the two speculative blocks would require either (a) locating a HAFiscal-style canonical dolo-plus example for type-indexed families, or (b) a discussion with the dolo-plus maintainers on the intended idiom for these two patterns.
