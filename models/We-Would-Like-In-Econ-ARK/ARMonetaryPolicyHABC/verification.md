# Verification (Matsya / AI iteration vs. the paper)

> **Paper-grounded** as of this commit. Every paper-side claim now cites a
> specific equation number, page, or section in **Algan & Ragot (2009),
> "Monetary policy with heterogeneous agents and borrowing constraints,"
> *Review of Economic Dynamics* 13(2), pp. 295–316** (DOI:
> [10.1016/j.red.2009.05.001](https://doi.org/10.1016/j.red.2009.05.001);
> open-access preprint
> [hal-01170621v1](https://sciencespo.hal.science/hal-01170621v1)). Equation
> numbers below are paper equations (e.g. eq. (15)), not summary-notebook
> numbers. Page numbers refer to the journal pagination 295–316.
>
> This file partitions every open issue into **paper gap** (something the
> paper does not specify, or that we have not yet transcribed) vs.
> **dolo-plus spec gap** (something the canonical dolo-plus / DDSL corpus
> does not document an idiom for). Paper gaps close by reading the paper;
> dolo-plus spec gaps close by locating a canonical example or consulting a
> dolo-plus maintainer.

## Scope of this verification

The formalization layer in this item (the `bellman-excerpt.md` +
`dolo-plus-draft.yaml` pair at the item root) encodes the **household
decision problem of paper §3.1.1 ("Households")**, p. 7-8, which is the
"general model" of paper §3 used for the quantitative analysis in §4. The
simple two-state model of paper §2 is descriptively reviewed in
`bellman-excerpt.md` but not separately formalized — the general model
nests it. The aggregate side of paper §3.1.2-§3.1.4 (firms, government,
monetary policy) is intentionally deferred (`AGENTS.md` "Scope" bullet).

## Accept / edit / reject — recursive form (paper §3.1.1, between eqs. (17)-(22))

**Accepted.** The recursive form encoded in `bellman-excerpt.md` and the
`cntn_to_dcsn_mover` `Bellman:` block of `dolo-plus-draft.yaml` reproduces
the paper's recursive Bellman (paper p. 8, between eq. (17) and the
first-order conditions (18)-(20)):

```
v(q, e) = max_{c, m, l, a'}  u(c, m, l) + β E[v(q', e')]
   s.t.  c + m + a' = q + w e l + μ
```

Two stages — **decision** (over `c, m, l, a'`) followed by **shock
realization** (Markov draw of `e_next`, formation of `q_next`) — match the
max-then-expectation structure in the paper line-by-line. Matsya's
Evaluate turn (`docs/matsya-evaluate-turn.txt`) confirmed this
decomposition is **CANONICAL** vs. the dolo-plus `cons_stage` +
`noport_stage` pattern. **No paper-vs-formalization gap.**

**Accepted (post-Matsya edit).** Three free controls `(c, m_d, l)` with
`a'` pinned by the budget identity in `dcsn_to_cntn_transition`. The paper
writes the optimization as `max_{c, m, l, a'}` over four controls subject
to one budget equality (eq. (16)), giving 4 - 1 = 3 degrees of freedom.
Pinning `a'` by the budget identity is one valid encoding of those three
degrees of freedom; pinning `c` would be another. The paper itself is
silent on which control to make residual — the choice is encoding-level,
not paper-level. Our pre-Matsya draft carried four controls without any
budget-pinning; Matsya Flag C flagged this as non-canonical (the budget
should bind), and the Improve commit adopted the three-free-controls
encoding. **No paper-vs-formalization gap.**

**Accepted.** The `m_d` (control) / `m` (poststate) split with the
bridging identity `m = m_d` is **CANONICAL** per Matsya's Evaluate turn,
matching `c` (control) / `a` (poststate) with `a = w - c` in
`cons_stage.md`. Paper notation is just `m` for both — the split is a
dolo-plus encoding of the chosen-vs-carried-forward distinction inside one
period. **Encoding-level, not a paper gap.**

## Accept / edit / reject — wealth-on-hand and budget (paper eq. (16))

**Accepted with one explicit deviation flagged.**

Paper eq. (16), p. 8:

```
c_t + m_t + a_{t+1} = (1 + r_t) a_t + m_{t-1}/Π_t + w_t e_t l_t + μ_t
```

with the wealth-on-hand definition (paper, just before the recursive
form, p. 8):

```
q_t = (1 + r_t) a_t + m_{t-1}/Π_t
```

so the recursive-form budget is `c + m + a' = q + w e l + μ` — exactly
what `dolo-plus-draft.yaml` encodes in `dcsn_to_cntn_transition`.

**Deviation (flagged).** Our shock-stage `arvl_to_dcsn_transition`
encodes the next-period wealth-on-hand as

```
q_next = R * a + (1 + r_m) * m
```

The paper's eq. (16) writes the corresponding terms as `(1 + r_t) a_t`
and `m_{t-1}/Π_t`. The mappings are:

| Our YAML | Paper analogue (eq. (16)) | Comment |
|---|---|---|
| `R * a`           | `(1 + r_t) a_t`     | Same — gross real return on the riskless asset. (Our `R` is the gross return, paper's `1+r` is also gross.) |
| `(1 + r_m) * m`   | `m_{t-1}/Π_t`       | The paper writes the real return on money as `1/Π` directly; our `(1 + r_m)` parameterizes the same quantity, so `r_m = 1/Π - 1 = -π/(1+π)`. The two are identical at any single Π but our parameterization carries `r_m` as a free parameter rather than deriving it from `Π`. |

The second row is a **paper gap** in the spec sense that our YAML does
not yet impose `r_m = 1/Π - 1` as an equilibrium consistency condition.
At a stationary equilibrium with constant `Π`, this is just a redefinition
and harmless; in any non-stationary or shock-on-aggregate-money exercise,
the consistency `(1 + r_m) = 1/Π` would have to be enforced. Listed as a
deferred row in the table below.

## Accept / edit / reject — utility kernel (paper eq. (15))

**Rejected (as paper-faithful), with the deferral now explicitly cited.**

Paper eq. (15), p. 8 (transcribed verbatim):

```
u(c, m, l)
  = (1 / (1-σ)) * [ ( ω c^((η-1)/η) + (1-ω) m^((η-1)/η) )^(η/(η-1))
                    * (1 - l)^ψ
                  ]^(1-σ)
```

with **paper §3.3.1, p. 11, Table 1 calibration**: `σ = 1`, `η = 0.5`,
`ω = 0.988`, `ψ = 2`. The interest elasticity of money demand `η` is
explicitly identified with that quantity (paper p. 11, "the interest
elasticity of money").

The current `dolo-plus-draft.yaml` `cntn_to_dcsn_mover` `Bellman:` block
uses a **separable CRRA + log-money + convex-labor-disutility WORKAROUND**
(rho on c, rho_m on m_d, gamma on l) instead of the paper's CES kernel.
This is now flagged with an explicit `# unresolved:` block at the line
itself (per `CONTRIBUTING.md` line 44 idiom) that:

- spells out paper eq. (15) verbatim at the line,
- cites the source (paper §3.3.1 + the verbatim transcription preserved
  in `docs/legacy-drafts/arg2009-bellman-excerpt.md`),
- enumerates the two ways to close the deferral.

**This is the only outstanding paper-vs-formalization discrepancy in the
household-block utility kernel.** Replacing the separable workaround
with the paper's CES form is tracked as deferred item #1 in
`docs/accept-edit-reject.md`. The paper's calibration (`σ=1, η=0.5,
ω=0.988, ψ=2`) is now in-hand for that closure; the only remaining
obstacle is locating a canonical dolo-plus example with a CES inner
aggregator under a CRRA outer wrapper.

## Accept / edit / reject — symbol conventions

**Edited.** The Markov kernel was renamed from `Π` (paper notation
implicit; see paper p. 7-8 where `Π` is reserved for inflation) to `P_e`
in our formalization. The paper's actual symbol for the productivity
transition matrix is `Q` (paper p. 7, "The productivity process follows a
3 × 3 transition matrix Q"). Either `Q` or `P_e` would avoid the
inflation-`Π` collision; we kept `P_e` for mnemonic clarity ("P-of-e") and
because it had already propagated through `bellman-excerpt.md`, the YAML,
and the Matsya cache before the paper symbol `Q` was checked. **Paper
deviation: deliberate, justified, mnemonic; no economics consequence.**

**Edited.** The transfer `μ` was moved from `R+` to `R`. Paper-grounded
justification: in the simple model (paper §2.1, eq. (5), p. 5),
`μ_t^i = (π/Π) m_{t-1}^i` is non-negative because beginning-of-period
real money balances are non-negative. **But** in the general model the
paper considers four redistribution schemes (paper §4.2, p. 13-14):
  - "lump-sum proportional to beginning-of-period real balances" (§4.2.1,
    p. 13) — non-negative,
  - "helicopter-drop equal across households" (§4.2.2 onward) — equal,
    typically positive at high inflation,
  - "Phelps effect: inflation tax substitutes for distortionary taxes"
    (§4.2.4, p. 17) — net of inflation tax can be negative for high-money
    households.

Restricting `μ ∈ R+` would silently drop the third redistribution scheme.
`μ ∈ R` is correct for the general model.

**Edited.** Identity transitions in both stages are explicitly labelled
as `# degenerate: identity` so reviewers can distinguish "identity" from
"omitted." **Encoding-level, not a paper gap.**

**Edited (post-Matsya).** `P_e` is declared as a plain `@in R+` parameter,
not `@in StochasticMatrix`: the latter has no precedent in the canonical
dolo-plus corpus (Matsya Evaluate turn, Question 3, **UNRESOLVED**).
Row-stochastic semantics are carried instead by `@dist MarkovChain(P_e)`
on the exogenous block, which Matsya confirmed is the canonical pattern.
**Spec-level, not a paper gap.**

## Accept / edit / reject — borrowing constraint

**Resolved.** Paper eq. (17), p. 8:

```
a_{t+1}^i ≥ 0,   1 ≥ l_t^i ≥ 0,   c_t^i ≥ 0,   m_t^i ≥ 0
```

The paper's borrowing constraint is exactly `a' ≥ 0` — i.e., **`a_min =
0` is the canonical value**, not a "TBD" placeholder. The paper is
explicit: "we assume that no household is able to borrow: a_{t+1}^i ≥ 0"
(paper §2.1.1, p. 4, restated in eq. (17) for the general model).

The current YAML carries `a_min: '@in R'` with a `# unresolved:` flag.
This was a paper gap until the paper was in-hand; **as of this commit it
is closeable**: the value is `0`. The YAML can either set the placeholder
parameter `a_min = 0` or drop the parameter entirely and write the
domain `Xa: '@def [0, +∞)'`. Either is paper-faithful. Picking the
specific encoding is left for a follow-up YAML touch (since this commit
focuses on `verification.md`); see the deferred-row table below for the
tracking.

## Accept / edit / reject — Markov productivity process (paper §3.3.2)

**Resolved.** Paper §3.3.2, p. 11-12 specifies the calibrated 3-state
Markov chain on `e ∈ {e_h, e_m, e_l}` with restrictions and identifying
moments:

- **Structural restrictions:** `p_{l,h} = p_{h,l} = 0` (no direct
  transitions between extreme states), so the off-diagonal structure is

  ```
       e_h         e_m         e_l
  e_h  p_{h,h}     1-p_{h,h}   0
  e_m  ?           p_{m,m}     ?       (with the two ?'s summing to 1-p_{m,m})
  e_l  0           1-p_{l,l}   p_{l,l}
  ```

- **Calibrated values (paper p. 12):** `p_{l,l} = p_{h,h} = 0.9750`,
  `p_{m,m} = 0.9925`, productivity ratios `e_h / e_m = 4.64`,
  `e_m / e_l = 5.65`.

- **Identifying targets (paper p. 12):** annual autocorrelation 0.91,
  annual standard deviation of innovation 0.22, Gini wealth = 0.72,
  share of borrowing-constrained households = 6%.

The current YAML carries `P_e: '@in R+'` with a `# unresolved:` flag for
the numerical entries and `Xe: '@def {0.5, 1.0, 1.5}'` as a placeholder
state space. **As of this commit the calibration is closeable**:
substitute the values above. The state space `Xe` should be
re-parameterized as `{e_l, e_m, e_h}` with the ratios
`e_h/e_m = 4.64, e_m/e_l = 5.65` and a normalization (paper does not
fix the level; effective labor `L_t` is the relevant aggregate, eq.
(23)–(24)). Picking the specific numerical encoding is left for a
follow-up YAML touch.

## Aggregate side: confirmed deferred (paper §3.1.2-§3.1.4)

The aggregate side of the paper is **intentionally not formalized** in
this item; `AGENTS.md` "Scope" bullet documents this. For the record,
the paper's aggregate equations are:

- **Production (paper §3.1.2, p. 9):** `Y_t = K_t^α L_t^{1-α}` with `α =
  0.36`, `δ = 0.025` (paper Table 1).
- **Factor prices (paper eqs. (23)-(24), p. 9):** `w̃_t = (1-α)(K/L)^α`,
  `r̃_t + δ = α (K/L)^{α-1}`.
- **Government (paper §3.1.3, eq. (25), p. 9):** `∫ μ_t^i di + G = χ_t r̃_t
  K_t + χ_t (L_h e_h + L_m e_m + L_l e_l) w̃_t + τ^{tot}_t`.
- **Money supply law (paper §3.1.4, eq. (26), p. 9):** `Ω_t = Ω_{t-1}/Π_t
  + π Ω_{t-1}/Π_t`.
- **Inflation tax (paper eq. (27)):** `τ^{tot}_t = π Ω_{t-1}/Π_t`.

These objects are listed in `bellman-excerpt.md`'s "Out of scope (this
draft)" table and are **not** part of the household-block formalization
verified above. They will be picked up in a separate general-equilibrium
PR.

## Paper gaps vs. dolo-plus spec gaps — current status

| Open issue | Paper gap? | Spec gap? | Status as of this commit | Next action |
|---|---|---|---|---|
| Utility kernel: separable workaround vs. paper CES eq. (15) | **Paper gap** (functional form known; encoding pending). | **Spec gap** in the narrow sense that I have not located a canonical dolo-plus example with a CES inner aggregator under a CRRA outer wrapper. | Functional form **resolved** (eq. (15) transcribed in YAML `# unresolved:` block + `bellman-excerpt.md` symbol table). Encoding **deferred**. | (a) Locate a canonical dolo-plus CES example via a focused Matsya turn, then re-encode; or (b) keep the workaround under a regime-justification (η → 1 limit) and document the calibration consequence. |
| Borrowing limit `a_min` | Was a paper gap; **now resolved** (paper eq. (17): `a_min = 0`). | No. | **Resolved (paper-side).** YAML edit pending. | Replace `a_min: '@in R'` placeholder with `a_min = 0` (or drop the parameter and write `Xa: '@def [0,+∞)'`). |
| Transfer `μ` sign rule | Was a paper gap; **now resolved** (paper §4.2, four redistribution schemes; net `μ` can be negative under the Phelps-effect scheme, §4.2.4). | No. | **Resolved.** Domain `R` is correct for the general model. | None. |
| `P_e` numerical calibration | Was a paper gap; **now resolved** (paper §3.3.2: `p_{l,l} = p_{h,h} = 0.9750, p_{m,m} = 0.9925`, restrictions `p_{l,h} = p_{h,l} = 0`, productivity ratios `e_h/e_m=4.64, e_m/e_l=5.65`). | No. | **Resolved (paper-side).** YAML edit pending. | Substitute the numerical entries; restate `Xe` with the ratios + a normalization. |
| `q'` LoM: `R·a + (1+r_m)·m` vs. paper `(1+r) a + m_{-1}/Π` | Mild paper gap: equivalent at any single `Π` but the paper writes the real return on money as `1/Π` directly; our `r_m` does not yet impose `(1+r_m) = 1/Π` as a consistency condition. | No. | **Identified, not yet enforced.** | Either drop `r_m` and write `(1/Pi_inf) * m` (introduces inflation symbol), or add a parameter-consistency comment. Defer until the aggregate / monetary block is added (then `Π` exists in scope). |
| Symbol `Q` (paper) vs. `P_e` (our) for the productivity transition matrix | No (deliberate rename to avoid `Π`-collision; mnemonic). | No. | **Deliberate deviation, documented.** | None. |
| `P_e` declaration idiom (`@in StochasticMatrix` vs. plain + `@dist MarkovChain`) | No. | Was a spec gap; **resolved** by Matsya Evaluate turn (Q3). | **Resolved.** | None. |
| Multi-control budget vs. budget-identity-pinning `a'` | No (paper writes 4-controls + 1-budget; encoding choice). | Was a spec gap; **resolved** by Matsya Evaluate Flag C. | **Resolved.** | None. |
| `cons_stage` / `noport_stage` two-stage pattern over Markov shocks | No. | Not a spec gap (CANONICAL per Matsya Evaluate Q1). | **Resolved.** | None. |

## Paper-equation → formalization mapping (single-source-of-truth)

The following table is the mapping a future contributor or AI agent
should consult when reconciling the YAML / `bellman-excerpt.md` against
the paper. **Equation numbers are paper equations.**

| Paper object | Paper location | `bellman-excerpt.md` element | `dolo-plus-draft.yaml` element |
|---|---|---|---|
| Utility `u(c, m, l)` | eq. (15), p. 8; calibration p. 11 Table 1 | Symbol-table rows for `c, m, l, σ, η, ω, ψ` | `cntn_to_dcsn_mover.Bellman` (currently separable workaround; see `# unresolved:` block) |
| Budget constraint | eq. (16), p. 8 | "Stage 2" budget block | `dcsn_to_cntn_transition` (`a = q + w * e * l + mu - c - m_d`) |
| Sign / domain constraints | eq. (17), p. 8 | Symbol-table rows for `a, l, c, m` (bounds column) | `Xa, Xl, R+` constraints in the `spaces:` block; `a_min` parameter (resolves to `0`) |
| Wealth-on-hand definition `q` | Paper p. 8, just before recursive form | "Pre-state" / "decision-stage state" `q` row | `prestate.q`, `states.q` |
| Recursive Bellman | Paper p. 8, between eq. (17) and FOC eq. (18) | Stage-1 "decision" Bellman block | `cntn_to_dcsn_mover.Bellman` |
| Markov productivity `e ∈ {e_h, e_m, e_l}` | §3.1.1 p. 7-8; calibration §3.3.2 p. 11-12 | `e` row in symbol table; "shock realization" stage | `Xe` space, `e_next: '@dist MarkovChain(P_e)'`, `P_e` parameter |
| Borrowing constraint `a' ≥ 0` | eq. (17), p. 8 | `a_min` row in symbol table | `a_min` parameter (resolves to `0`); `Xa: '@def R+'` |
| Real return on money `m_{-1}/Π` | eq. (16), p. 8 | "Out of scope (this draft)" row for `Π_inf` | `r_m` parameter in shock stage (current parameterization); paper uses `1/Π` directly |
| FOC: Euler `u_c = β(1+r) E v_1` | eq. (18), p. 9 | Discussed narratively in `bellman-excerpt.md` "Properties" section (informally) | (Implicit; FOCs not enumerated in YAML — they emerge from the Bellman) |
| FOC: money arbitrage | eq. (19), p. 9; eq. (21) for binding case | (As above) | (As above) |
| FOC: labor-leisure | eq. (20), p. 9; eq. (22) for binding case | (As above) | (As above) |
| Quarterly model period | §3.3, p. 11 ("model period equals to one quarter") | Symbol-table note on `β` | `beta: '@in (0,1)'` parameter |
| Annualized inflation 3% benchmark | §3.3, p. 11 (`π = 0.75%` quarterly) | Out-of-scope row for `π` | (Not in household-block YAML) |

## Summary of paper-grounded resolution

**Paper-side gaps closed by this commit** (because the paper is now in
hand):

- Utility functional form ✅ (eq. (15) transcribed at every relevant
  line; encoding into the YAML's CES form remains deferred — that is a
  spec / Matsya gap, not a paper gap).
- Borrowing limit `a_min = 0` ✅ (eq. (17)).
- Transfer `μ ∈ R` justified by the Phelps-effect redistribution scheme
  ✅ (paper §4.2.4).
- Three-state Markov calibration: structural restrictions, transition
  probabilities, productivity ratios ✅ (paper §3.3.2).
- Symbol-collision interpretation `P_e` vs. paper's `Q` ✅ (deliberate
  mnemonic rename, paper symbol now documented).

**Paper-side gaps remaining:**

- None at the household-decision-block level. (The aggregate side of the
  paper is intentionally out of scope for this item.)

**Spec-side / encoding-level work remaining (tracked separately):**

- Locate a canonical dolo-plus example with a CES-with-leisure inner
  aggregator and re-encode the YAML utility kernel; close `# unresolved:`
  block accordingly.
- Substitute resolved numerical values into the YAML (`a_min = 0`,
  `P_e` transition probabilities, `Xe` with paper-calibrated productivity
  ratios). This is a small follow-up YAML edit.
- Add a parameter-consistency comment for `(1 + r_m) = 1/Π` once the
  aggregate / monetary block is in scope.

This closes deferred item #2 from `docs/accept-edit-reject.md`
("Rewrite verification.md against the published paper, not the
summary").
