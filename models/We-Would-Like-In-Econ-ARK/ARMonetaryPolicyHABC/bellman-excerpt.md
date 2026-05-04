# Modular Bellman statement: Algan–Ragot (2009) household block (ballpark draft)

This file is the **canonical formalization artifact** for this item (per [econ-ark/ballpark `CONTRIBUTING.md`](https://github.com/econ-ark/ballpark/blob/master/CONTRIBUTING.md)). Older notes remain as supplementary context: `arg2009-bellman-excerpt.md` (utility and environment excerpt from the summary notebook) and `arg2009-improved-stage-description.md` (concise stage narrative).

## Timing (within one period)

Numbered steps:

1. **Household decision.** The agent observes beginning-of-period resources `q` and idiosyncratic productivity `e` (already realized for this decision).
2. **Shock and resource evolution.** Productivity for next period is drawn; next-period resources `q'` are formed from chosen asset positions and the shock draw.

This supports a **max-of-expectation** Bellman equation: optimize today given `e`, then take expectations over `e'`.

## Symbol table

### Household block (in scope for this draft)

| Symbol | Role | Domain / type | Description |
|--------|------|----------------|-------------|
| `q` | state | `R+` | Beginning-of-period financial resources / cash-on-hand |
| `e` | state | finite set | Current idiosyncratic productivity (Markov) |
| `c` | control (free) | `R+` | Consumption |
| `m` | control (free) / poststate | `R+` | Real money balances carried to next period (named `m_d` in YAML when viewed as the **chosen** value before the savings identity `m = m_d`; see `dolo-plus-draft.yaml`) |
| `l` | control (free) | `[0, \bar l]` | Labor supply |
| `a'` | poststate (pinned by budget) | `[a_{\min}, \infty)` | Next-period illiquid-asset position, **pinned** by the budget identity `a' = q + w\,e\,l + \mu - c - m` (per Matsya Evaluate turn, Flag C: three free controls is the canonical encoding, not four; `a'` is not itself a free control) |
| `e'` | shock | same finite set | Next-period productivity, `e' \sim P_e(\cdot\mid e)` |
| `q'` | state | `R+` | Next period's beginning-of-period resources (pre-decision state next period) |
| `w` | parameter | `R+` | Wage factor scaling `e l` |
| `mu` | parameter | `R` | **Net** transfer / policy-linked income term in the budget (can be negative when household's inflation-tax burden exceeds rebate; verify sign rule in paper) |
| `beta` | parameter | `(0,1)` | Discount factor |
| `P_e` | parameter | `R+`^{3x3} row-stochastic | Markov transitions for `e` (renamed from `Pi` to avoid collision with inflation `Pi_inf` in the aggregate side; see "Out of scope" table below). **Canonical declaration** (per Matsya Evaluate turn, Question 3): plain non-negative parameter in the `parameters:` block; row-stochastic semantics are carried by `@dist MarkovChain(P_e)` on the exogenous variable `e_next`. Do **not** invent `@in StochasticMatrix` — no precedent in canonical dolo-plus examples. |
| `a_min` | parameter | `R` | Borrowing limit (paper-specific; placeholder in draft YAML) |
| `R`, `r_m` | parameters | `R+` | Draft return factors in the law of motion for resources (see YAML; **unresolved** vs. paper) |
| `sigma` | parameter | `R+` | Outer CRRA curvature in the summary's CES-with-leisure utility |
| `eta` | parameter | `R+` | CES elasticity between consumption and real money balances |
| `omega` | parameter | `(0,1)` | CES weight on consumption in the `(c, m)` composite |
| `psi` | parameter | `R+` | Leisure exponent in the summary's utility |
| `v(q,e)` | value | `R` | Household value function |

### Out of scope for this draft (flagged for a later general-equilibrium pass)

Surfaced in `arg2009-bellman-excerpt.md` but **not** encoded in the current YAML or perch decomposition:

| Symbol | Role | Where it appears in the paper summary | Why deferred |
|--------|------|----------------------------------------|---------------|
| `K`, `alpha`, `delta` | aggregate production | `Y_t = K_t^alpha L_t^(1-alpha)`; resource constraint | Household block only in this draft |
| `Y`, `G` | aggregate quantities | Resource constraint | General-equilibrium pass |
| `Omega`, `tau^{tot}` | monetary aggregates | `Omega_t = Omega_{t-1}/Pi_inf_t + pi * Omega_{t-1}/Pi_inf_t`; `tau_t^{tot}` | Monetary block; enters `mu` via redistribution rule, still TBD |
| `Pi_inf` | gross inflation | Inflation-tax expressions (distinct from Markov `P_e`) | Disambiguated in rename above; not yet in YAML |

**Utility (from summary excerpt — not yet matched to YAML).** The summary notebook records a CES–leisure structure parameterized by `(sigma, eta, omega, psi)`; see `arg2009-bellman-excerpt.md`. The draft `dolo-plus-draft.yaml` currently uses a **separable placeholder** for tractability—flagged there as unresolved relative to the paper.

## Stages, perches, transitions, movers

### Stage 1 — Household decision

| Perch | Carried objects | Value | Notes |
|-------|-----------------|-------|--------|
| **arrival** | `(q, e)` | `V` | Shocks relevant to the decision are already embedded in observed `e`. |
| **decision** | `(q, e)` | `V` | Choose **three** free controls `(c, m, l)` subject to the borrowing constraint; `a'` is determined by the budget identity (not free). |
| **continuation** | `(a', m, e)` | `V_>` | Post-decision objects feed the next stage. |

- **Arrival → decision** (`g_{≺∘}`): **identity (degenerate)** on `(q, e)` — no within-stage shock between **arrival** and **decision** in this draft; carried forward unchanged.
- **Decision → continuation** (`g_{∘≻}`): `(a', m, e)` from the **budget identity** `a' = q + w\,e\,l + \mu - c - m` (this pins `a'`), the savings identity `m = m_d` (mapping the decision-perch control `m_d` to the continuation-perch poststate `m`), and current `e` passed through. Per the Matsya Evaluate turn (docs/matsya-evaluate-turn.txt, Flag C), eliminating `a'` via the budget is the canonical encoding and matches the `a = w - c` pattern in `cons_stage`.

**Backward mover (continuation → decision):** Bellman maximization over feasible controls.

**Forward mover (decision → arrival):** identity on value at the **decision** perch in this draft (`V[<] = V` in YAML).

**Stage operator (Stage 1):** `\mathbb T_{\text{dec}} = \mathbb I_{\text{dec→arvl}} \circ \mathbb B_{\text{cntn→dec}}`.

### Stage 2 — Shock realization and next-period resources

| Perch | Carried objects | Value | Notes |
|-------|-----------------|-------|--------|
| **arrival** | `(a, m, e)` | `V` | Enters after Stage 1 continuation. |
| **decision** | `(q', e')` | `V` | Degenerate **decision** perch: no optimization; nature draws `e'` and implied `q'` is formed. |
| **continuation** | `(q', e')` | `V` | Feeds the next period’s **arrival** state. |

- **Arrival → decision:** draw `e' \sim P_e(\cdot\mid e)`; map `(a, m, e')` into `q'` (draft: `q' = R a + (1+r_m) m` in YAML — **unresolved** vs. paper).
- **Decision → continuation:** **identity (degenerate)** on `(q', e')`.

**Backward mover:** pass-through (`V = V[>]` in YAML).

**Forward mover:** expectation over `e'` (`V[<] = E_{e'}[V]` in YAML).

**Stage operator (Stage 2):** `\mathbb T_{\text{shock}} = \mathbb I_{\text{E}} \circ \mathbb B_{\text{pass}}`.

### Period composition

Let `\mathbb T_{\text{period}} = \mathbb T_{\text{shock}} \circ \mathbb T_{\text{dec}}`. The infinite-horizon problem iterates `\mathbb T_{\text{period}}` on the **arrival** state `(q, e)`.

## Bellman equation (compact)

$$
v(q,e) = \max_{c,\,m,\,l} \Big\{ u(c,m,l) + \beta \, \mathbb{E}_{e' \mid e}\big[ v(q', e') \big] \Big\}
$$

with the budget identity pinning `a'` and the borrowing constraint:

`a' = q + w e l + mu - c - m`, `a' \ge a_{\min}`,

with `q'` determined in the shock stage (draft law of motion in `dolo-plus-draft.yaml`).

## Stage composition (link to SolvingMicroDSOPs §§12–13)

The household problem nests as **optimize then expect**: Stage 1 supplies the continuation value as a function of `(a', m, e)`; Stage 2 integrates over `e'` and maps into `(q', e')` for the next period. A full **EGM** discussion is deferred until the utility specification and constraints are pinned to the paper (the CES–leisure block in the summary is not yet encoded in the YAML).
