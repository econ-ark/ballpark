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

- Nothing from matsya's YAML output was rejected outright. The two unresolved-syntax blocks (`terminal:`, `calibration_family:`) are preserved with inline `# unresolved:` comments per `CONTRIBUTING.md`'s rule (line 44) that uncanonical features be flagged rather than silently fudged. (The first matsya draft used `# SPECULATIVE` markers; these have been converted to the canonical `# unresolved:` idiom as a copy-edit.)

## Flagged as `# unresolved:` (not paper gaps — dolo-plus spec gaps)

The YAML carries inline `# unresolved:` flags on three families of items:

1. **`terminal:` block.** The terminal boundary wiring $V_{[\succ]} = e(a_{[\succ]})$, $dV_{[\succ]} = A\,a_{[\succ]}^{-\mu}$ is the **correct pattern** per matsya's Turn 3 recommendation, but no canonical dolo-plus syntax for terminal-boundary blocks was located in matsya's retrieved corpus. The paper is **not** the bottleneck — the bequest kernel is fully specified; what's missing is the dolo-plus idiom for the keyword `terminal:` and its sub-keys.

2. **`calibration_family:` block.** The option-A calibration-override pattern (per matsya Turn 2) is the **correct approach** for a fixed-at-birth $(\tau, r)$ type family, but no canonical dolo-plus syntax for such families was located. Again, the paper is not the bottleneck — the paper specifies the 10 × 5 type space and the within-life-constant structure fully; what's missing is the dolo-plus idiom for instantiating the template across the family. The placeholder $\Pi_\tau$ and $\Pi_r$ matrices in the `population:` sub-block are 2×2 stubs and explicitly flagged: the paper baselines are 10×10 and 5×5 with the off-diagonal decay structure of footnote 13.

3. **`w` parameter as scalar.** The paper has an age-varying earnings profile $w_t(\tau)$ for $\tau \in \{1,\ldots,10\}$ and $t \in \{1,\ldots,36\}$ — a 36 × 10 schedule (paper Table 1, interpolated linearly within bracket). The YAML's `parameters:` block carries `w` as a scalar with an inline `# unresolved:` comment recording the gap; closing it requires either (a) locating a HAFiscal-style canonical example for age-varying calibration overrides, or (b) declaring `w` as a function of $t$ and $\tau$ via an external table reference.

## Open items not yet in the YAML

Items from `bellman-excerpt.md` → "Still open" that remain outside this draft:

- **Lifecycle nest with age-varying $w_t(\tau)$.** Now flagged inline in the YAML's `parameters:` and `calibration_family:` blocks (see item 3 above). The 36 per-age × 10-type entries are not inlined; a complete YAML would reference paper Table 1 via interpolation.
- **Section IIID wealth-dependent $r$ extension.** Explicitly out of scope for this baseline YAML (see `bellman-excerpt.md` → "Still open" §6). Would require a separate YAML with a state-contingent (rather than fixed-at-birth) $r$ exogenous process.

## Verdict

**The paper's description of its model is sufficient to construct a dolo-plus YAML formalization.** Matsya did not request any additional model information beyond what was provided in `bellman-excerpt.md`. The remaining gaps are **dolo-plus spec gaps** (canonical syntax for terminal-boundary blocks, calibration-family instantiation, and age-varying parameter overrides), not paper gaps.

The committed `dolo-plus-draft.yaml` is a Formalized-tier draft per `CONTRIBUTING.md`'s definition: it parses as YAML (verified via `yaml.safe_load`), encodes what is canonically encodable, and flags what is not with inline `# unresolved:` comments rather than silently fabricating. A full cleanup of the unresolved blocks would require either (a) locating a HAFiscal-style canonical dolo-plus example for type-indexed families and per-age overrides, or (b) a discussion with the dolo-plus maintainers on the intended idiom for these patterns.
