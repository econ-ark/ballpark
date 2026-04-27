# Verification of `dolo-plus-draft.yaml` against Benhabib, Bisin, and Luo (2019)

**Matsya session:** `topics2026-benhabib-demo` (6 turns; latest 2026-04-27).
- Turns 1–3 (2026-04-19): forward-mover idiom, parameterized-family analysis, terminal-closure recommendation.
- Turn 4 (2026-04-19): full first-pass YAML draft.
- Turn 5 (2026-04-27): self-assessment of paper-side gaps in the Turn-4 draft.
- Turn 6 (2026-04-27): definitive syntax-status review of residual UNRESOLVED items.

**Source compared:** published paper (`Benhabib_et_al_2019.mmd` / `.pdf`), §I (theoretical framework), §IIB (data sources), Table 1 (earnings), Table 4 (estimated parameters), and footnote 13 ($r$-chain off-diagonal structure).

## Accepted from matsya's YAML

- **Stage structure** — single-stage template with perches (arrival `a`, decision `m`, continuation `a_next`), within-stage transitions (`m = (1+r)*a + w`, `a_next = m - c`), backward mover (Bellman + EGM block), and forward mover with chain-rule factor (`V[<] = V`, `dV[<] = (1+r) * dV` — see "Refined post-paper-review" below). Matches paper §I equations.
- **CRRA utility** `u(c) = c^(1-sigma)/(1-sigma)` matches paper §I exactly.
- **Warm-glow bequest kernel** `e(a) = A*a^(1-mu)/(1-mu)` matches paper §I exactly.
- **EGM sub-equations** (InvEuler, reverse transition `m[>] = a_next + c[>]`, MarginalBellman envelope `dV = c^(-sigma)`) — textbook-standard for CRRA buffer-stock problems.
- **Omission of `exogenous` block** is correct — paper §I states "$r$ and $w$ are stochastic over generations only: agents face no uncertainty within their life span."
- **Canonical structural reference for the forward mover** (matsya Turn 6): `consumption_savings_iid.md`'s `dV[<] = r * E_{y}(dV)`. The YAML uses the no-shock specialization (drop expectation; substitute $(1+r)$ for $r$). Status **CANONICAL-structure**; no canonical example explicitly labels the no-shock degenerate case.

## Refined post-paper-review (2026-04-27)

Three corrections to matsya's Turn-1–4 recommendations following direct paper audit:

1. **Chain-rule factor on `dV[<]`** (Open Issue #1). Matsya Turn 1 recommended `dV[<] = dV` per the "identity twister" dev-spec, but BBL's arrival-to-decision map $m = (1+r)a + w$ is non-trivial. Paper's envelope condition gives $V'_t(a) = (1+r)\, V'_t(m)$, so the correct idiom is `dV[<] = (1+r) * dV`. Patched in YAML and excerpt.

2. **Consumption upper-bound typo** (Open Issue #8). Paper §I writes `0 ≤ c ≤ a` in the recursion, which would force $a' \ge ra + w > 0$ (unusual savings floor). Treated as a typo for the standard `a' ≥ 0` ⟺ `c ≤ m`; the YAML adopts `c ∈ [0, m]`.

3. **β on terminal bequest** (Open Issue #9, option (i)). Paper writes $V_T(a) = u(c) + e(a')$ (no β); standard backward-mover wiring would otherwise give $V_T = u(c) + \beta\, e(a')$. Resolved by absorbing $1/\beta$ into the boundary weight: $\tilde A \equiv A/\beta$. Boundary expressions: `(A / beta) * a_next^(1-mu) / (1-mu)`. Single-template structure preserved; paper's calibrated $A \approx 0.0006$ corresponds to $\tilde A \approx 0.000619$ at the terminal boundary only; the interior template is unchanged.

Plus one structural simplification: replaced the verbose `instances: [...]` array (50 entries, 49 of them carrying redundant copies of the shared parameters) with an axis-product representation (`shared` + `by_r_type` + `by_tau` + `age_bracket_to_period`).

## Paper-calibrated values (2026-04-27)

YAML now carries paper-faithful numerical values where the paper provides them:

- **Shared parameters** (Table 4): $\beta = 0.97$, $\sigma = 2$, $\mu = 0.5993$ (s.e. 0.0061), $A = 0.0006$ (s.e. 0.0004), $T = 36$.
- **Rate-of-return state space** (Table 4 "State space"): $r \in \{0.0011, 0.0094, 0.0258, 0.0560, 0.0841\}$.
- **Earnings schedule** (Table 1): full 10×6 matrix in $thousands/year inlined as `calibration_family.by_tau`. **Bracket-piecewise-constant** per paper §IIB ("agents stay in the same decile for their whole lifetime"); 6 brackets of 6 years each. Period $t$ ↔ calendar age $24 + t$ (working life ages 25–60).
- **$\Pi_r$ diagonal** (Table 4 "Transition diagonal"): $\{0.0338, 0.2676, 0.1360, 0.2630, 0.0208\}$.

YAML parses cleanly via `yaml.safe_load` (verified). Paper values spot-checked at decile-1/bracket-1, decile-5/bracket-6, and decile-10/bracket-4 — all match paper Table 1 exactly.

## Edited (relative to the paper's own notation)

- **Decision-perch state `m` introduced** for the value-function argument and constraint bound. The paper's `a' = (1+r)a - c + w` with `0 ≤ c ≤ a` carries the inconsistency resolved in `_summary.ipynb` and post-paper-review confirmed (Open Issue #8).
- **Poststate named `a_next`** rather than the paper's `a'`; equivalent but avoids YAML quote-mark ambiguity.
- **Parameterized-family structure made explicit** via `calibration_family` block with paper values for all 50 instances. The paper itself solves these 50 problems in baseline estimation without naming them a family.
- **Terminal bequest weight $\tilde A = A/\beta$** at the boundary only, per Open Issue #9 option (i) — preserves single-template structure while matching paper's no-β-on-bequest convention.

## Rejected

Nothing from matsya's output was rejected outright. The corrections in "Refined post-paper-review" above (Open Issues #1 and #9) are refinements of matsya's structural framework, not rejections.

## Flagged as `# unresolved:` (dolo-plus spec gaps, not paper gaps)

Per matsya Turn 6 (2026-04-27), the items below are **definitively UNRESOLVED in the dolo-plus spec corpus** — not search failures.

1. **`terminal:` block keyword.** Matsya Turn 6: no `terminal:` or `boundary:` top-level key, no terminal-boundary recipe in `07-appendix-a-recipes.md`. Our placeholder block with sub-keys `parameters:`, `V[>]:`, `dV[>]:` is SPECULATIVE.

2. **β-aware boundary mechanism.** No mechanism for the boundary to know it is being plugged into a $\beta$-weighted backward mover. The $A/\beta$ absorption (Open Issue #9, option (i)) is an economically correct workaround.

3. **`calibration_family:` block keyword.** Paper values inlined; keyword and sub-keys (`shared`, `by_r_type`, `by_tau`, `cardinality`, `age_bracket_to_period`, `population`) remain SPECULATIVE per matsya's definitive 2026-04-27 confirmation that no canonical example has been indexed.

4. **Per-age parameter overrides on a repeated stage.** Paper Table 1 fully transcribed in `calibration_family.by_tau`; what's missing is the dolo-plus mechanism for addressing the right entry at each $(t, \tau)$ pair. No `lifecycle:` block, no age-indexed override, no repeating-stage period template surfaced.

5. **Sub-equation naming: `ShadowBellman` vs `MarginalBellman`** (matsya Turn 6 new finding). The system prompt says `ShadowBellman:` belongs in `dcsn_to_arvl_mover` while `MarginalBellman:` belongs in `cntn_to_dcsn_mover`. The canonical example (`solving-conjugates.md`) uses `MarginalBellman:` in the same structural position as our `ShadowBellman:`. Conflict noted; YAML retains `ShadowBellman:` per system prompt.

## Open items not yet in the YAML

- **Section IIID wealth-dependent $r$ extension.** Explicitly out of scope for this baseline YAML. Would require a separate YAML with state-contingent (rather than fixed-at-birth) $r$.
- **Online appendix matrices** — $\Pi_r$ off-diagonals (Appendix C.1; structure described in paper footnote 13: decay in rows 1–4, constant in row 5) and $\Pi_\tau$ full matrix (Appendix B.2; from Chetty et al. 2014, reduced to 10 states). Dynasty-layer; not blocking the within-lifetime stage formalization.

## Verdict

**The within-lifetime stage problem is mathematically and numerically paper-faithful as of 2026-04-27.** The within-stage equations, the EGM channel, the terminal boundary (with the $A/\beta$ refinement), and the calibration values match the paper exactly.

Remaining gaps:
- **Five dolo-plus spec-level syntactic gaps** (above) — definitively UNRESOLVED per matsya 2026-04-27 review. Closing them requires either dolo-plus spec extension (canonical syntax for terminal-boundary blocks, type-indexed families, per-age overrides, sub-equation naming) or maintainer discussion, not further model work.
- **Two dynasty-layer matrices** in online appendices, not yet downloaded. Outside the within-Bellman scope.

Per `CONTRIBUTING.md` Formalized-tier definition: this YAML parses (`yaml.safe_load` confirmed), encodes what is canonically encodable, carries paper-faithful numerical values where the paper provides them, and flags spec-level gaps with inline `# unresolved:` comments rather than silently fabricating non-canonical syntax.
