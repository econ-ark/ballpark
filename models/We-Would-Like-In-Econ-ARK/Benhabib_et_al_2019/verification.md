# Verification of `dolo-plus-draft.yaml` against Benhabib, Bisin, and Luo (2019)

**Matsya session:** `topics2026-benhabib-demo` (6 turns; latest 2026-04-27).
- Turns 1–3 (2026-04-19): forward-mover idiom, parameterized-family analysis, terminal-closure recommendation.
- Turn 4 (2026-04-19): full first-pass YAML draft.
- Turn 5 (2026-04-27): self-assessment of paper-side gaps in the Turn-4 draft.
- Turn 6 (2026-04-27): definitive syntax-status review of residual UNRESOLVED items.

**Source compared:** the published paper itself (accessed via [DOI: 10.1257/aer.20151684](https://doi.org/10.1257/aer.20151684); a local Mathpix `.mmd` conversion was used during the comparison, but `.mmd` files are gitignored and not redistributed here). Sections compared: §I (theoretical framework), §IIB (data sources), Table 1 (earnings), Table 4 (estimated parameters), footnote 13 ($r$-chain off-diagonal structure), and online Appendix A.1 (numerical solution method) plus C.1 ($\Pi_r$ matrix).

## Accepted from matsya's YAML

- **Stage structure** — single-stage template with perches (arrival `a`, decision `m`, continuation `a_next`), within-stage transitions (`m = a` identity, `a_next = (1+r)*(m - c) + w` per online appendix A.1), backward mover (Bellman + EGM block), and forward mover as literal pass-through (`V[<] = V`, `dV[<] = dV` — both level and marginal pass through because $m = a$ identity). Matches the paper's appendix-A.1 model.
- **CRRA utility** `u(c) = c^(1-sigma)/(1-sigma)` matches paper §I exactly.
- **Warm-glow bequest kernel** `e(a) = A*a^(1-mu)/(1-mu)` matches paper §I exactly.
- **EGM sub-equations** under appendix model: InvEuler `c[>] = (beta * (1+r) * dV[>])^(-1/sigma)` (the $(1+r)$ enters the FOC because $\partial a'/\partial c = -(1+r)$ in the appendix budget); reverse transition `m[>] = c[>] + (a_next - w)/(1+r)`; MarginalBellman envelope `dV = c^(-sigma)` (no $(1+r)$ in the envelope under appendix model since $\partial m/\partial a = 1$).
- **Omission of `exogenous` block** is correct — paper §I states "$r$ and $w$ are stochastic over generations only: agents face no uncertainty within their life span."
- **Canonical structural reference for the forward mover** (matsya Turn 6): `consumption_savings_iid.md`'s `dV[<] = r * E_{y}(dV)`. Under the appendix model with $m = a$ identity, the YAML's `dV[<] = dV` is the no-shock + identity-transition specialization (drop the expectation AND drop the chain-rule factor). Status **CANONICAL-structure**; no canonical example explicitly labels this fully-degenerate case.

## Refined post-paper-and-appendix-review (2026-04-27)

Three model-side corrections after direct paper + appendix audit (see Open Issues #1, #8, #9, #10 in `bellman-excerpt.md` for full audit trails):

1. **Budget-equation discrepancy: paper §I vs. online appendix A.1** (Open Issue #10). Paper §I writes $a' = (1+r)a - c + w$; the online appendix (= the authors' actual numerical solution) writes $a' = (1+r)(a-c) + w$. These are different models. **Resolution: match the online appendix** since it describes the collocation method that produces the published results. Paper §I's compact statement appears to have a typo (missing $(1+r)$ on the $c$ term, which would make it consistent with the $c \le a$ constraint). YAML and excerpt now encode the appendix model:
   - $\mathrm{g}_{\prec\circ}$: $m_t = a_t$ (identity)
   - $\mathrm{g}_{\circ\succ}$: $a_{t+1} = (1+r)(m_t - c_t) + w_t(\tau)$
   - EGM Inverse Euler: $c_t = (\beta(1+r)\,V'_{t+1}(a_{t+1}))^{-1/\sigma}$
   - EGM reverse: $m_t = c_t + (a_{t+1} - w_t)/(1+r)$
   - Forward mover: `V[<] = V; dV[<] = dV` (literal pass-through; no chain-rule factor since $m = a$ identity)

2. **Re-resolution of Open Issue #1 (chain-rule factor).** Under the appendix model adopted in #10, $m = a$ is identity, so the arrival-to-decision Jacobian is 1 — there is **no chain-rule factor**. Matsya Turn 1's original `dV[<] = dV` advice is correct after all. The earlier "correction" to `(1+r) * dV` was based on paper §I literal reading; reverted.

3. **Re-resolution of Open Issue #8 (consumption upper bound).** Under the appendix model, paper's `c ≤ a` is **genuine, not a typo**. The actual typo in paper §I is in the budget equation (missing $(1+r)$ on $c$), which would then make `c ≤ a` consistent. Since the YAML uses $m_t = a_t$ identity, the constraint `c ∈ [0, m]` is equivalent to `c ∈ [0, a]` — implementation correct.

4. **β on terminal bequest** (Open Issue #9, option (i)). Unchanged from morning's resolution: absorb $1/\beta$ into the boundary weight, $\tilde A \equiv A/\beta$, so $\beta V_{[\succ]} = e(a)$ matches paper's no-β-on-bequest terminal recursion. Under the appendix model, the resulting terminal Inverse Euler is $c_T = ((1+r)A)^{-1/\sigma} a_{T+1}^{\mu/\sigma}$.

Plus one structural simplification: replaced the verbose `instances: [...]` array (50 entries, 49 of them carrying redundant copies of the shared parameters) with an axis-product representation (`shared` + `by_r_type` + `by_tau` + `age_bracket_to_period`).

## Paper-calibrated values (2026-04-27)

YAML now carries paper-faithful numerical values where the paper provides them:

- **Shared parameters** (Table 4): $\beta = 0.97$, $\sigma = 2$, $\mu = 0.5993$ (s.e. 0.0061), $A = 0.0006$ (s.e. 0.0004), $T = 36$.
- **Rate-of-return state space** (Table 4 "State space"): $r \in \{0.0011, 0.0094, 0.0258, 0.0560, 0.0841\}$.
- **Earnings schedule** (Table 1): full 10×6 matrix in $thousands/year inlined as `calibration_family.by_tau`. **Bracket-piecewise-constant** per paper §IIB ("agents stay in the same decile for their whole lifetime"); 6 brackets of 6 years each. Period $t$ ↔ calendar age $24 + t$ (working life ages 25–60).
- **$\Pi_r$ full 5×5 matrix** (online Appendix C.1, downloaded 2026-04-27): each row is row-stochastic; diagonal $\{0.0338, 0.2676, 0.1360, 0.2630, 0.0208\}$ matches Table 4. Off-diagonals show the decay structure of paper footnote 13 (rows 1–4 symmetric around diagonal; row 5 constant 0.2448).

YAML parses cleanly via `yaml.safe_load` (verified). Paper values spot-checked at decile-1/bracket-1, decile-5/bracket-6, and decile-10/bracket-4 — all match paper Table 1 exactly. $\Pi_r$ row sums verified at 1.0 (one row 1.0002 within rounding).

## Edited (relative to the paper's own notation)

- **Decision-perch state `m` introduced as a perch label** with $m_t = a_t$ identity transition (under appendix model). Distinguishes the dolo-plus three-perch slots while remaining mathematically a single-state model.
- **Budget equation taken from online appendix A.1**, not paper §I literal — the appendix is authoritative for the numerical solution. Paper §I's $a' = (1+r)a - c + w$ is treated as a typo for the appendix's $a' = (1+r)(a-c) + w$. See Open Issue #10.
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
- **$\Pi_\tau$ full 10×10 matrix.** Online Appendix B.2 describes the construction procedure (collapse Chetty et al. 2014's 100×100 matrix to 10×10) but does not tabulate the result. Reconstruction would require either Chetty et al.'s `online_data_tables.xls` or the BBL replication package at `https://doi.org/10.3886/E113112V1`. Dynasty-layer; not blocking the within-lifetime stage formalization. ($\Pi_r$ has been transcribed from Appendix C.1 as of 2026-04-27.)

## Verdict

**The within-lifetime stage problem is mathematically and numerically paper-faithful as of 2026-04-27.** The within-stage equations, the EGM channel, the terminal boundary (with the $A/\beta$ refinement), and the calibration values match the paper exactly.

Remaining gaps:
- **Five dolo-plus spec-level syntactic gaps** (above) — definitively UNRESOLVED per matsya 2026-04-27 review. Closing them requires either dolo-plus spec extension (canonical syntax for terminal-boundary blocks, type-indexed families, per-age overrides, sub-equation naming) or maintainer discussion, not further model work.
- **Two dynasty-layer matrices** in online appendices, not yet downloaded. Outside the within-Bellman scope.

Per `CONTRIBUTING.md` Formalized-tier definition: this YAML parses (`yaml.safe_load` confirmed), encodes what is canonically encodable, carries paper-faithful numerical values where the paper provides them, and flags spec-level gaps with inline `# unresolved:` comments rather than silently fabricating non-canonical syntax.
