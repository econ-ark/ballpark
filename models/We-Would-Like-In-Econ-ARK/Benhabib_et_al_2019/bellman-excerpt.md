# Bellman excerpt — Benhabib, Bisin, and Luo (2019)

> **Paper:** Jess Benhabib, Alberto Bisin, and Mi Luo, "Wealth Distribution and Social Mobility in the US: A Quantitative Approach," *American Economic Review*, 109(5), 1623–1647, 2019. [DOI: 10.1257/aer.20151684](https://doi.org/10.1257/aer.20151684)

## Purpose and scope

This document is the modular-DDSL Bellman statement of the **within-lifetime** household problem in the paper's Section I, intended as input to a Matsya iteration that will produce a [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml). It covers:

- The **per-lifetime parameterized-family** problem: for each type assignment $(\tau, r)$, a finite-horizon lifecycle consumption-savings problem with terminal warm-glow bequest.
- **Two stage templates:** an **interior stage** used for ages $t = 1, \ldots, T-1$ and a **terminal stage** used at $t = T$.
- **Three perches per stage:** arrival $\prec$, decision $\circ$, continuation $\succ$.

It **does not** cover:

- The **dynasty-level stochastic process** over generations ($(\tau^n, r^n)$ Markov chains connecting lifetime maps $a^{n} = g(a^{n-1}; \tau^n, r^n)$). That is the inter-life composition layer; see [`_summary.ipynb` → "The Model" → "Stochastic Structure"](Benhabib_et_al_2019_summary.ipynb) for its description. A dolo-plus formalization of the within-lifetime problem does not need to encode dynasty dynamics; these are handled at an outer simulation layer.
- The Section IIID extension in which $r$ depends on wealth. Flagged in "Open issues" below.

---

## Symbol table

Every symbol appearing anywhere in this document is listed. Domains are stated explicitly; parameter values where the paper's baseline calibration fixes them.

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $t$ | index | $\{1, 2, \ldots, T\}$ | Age (period within a lifetime) |
| $T$ | parameter | positive integer; paper: $T = 36$ | Deterministic lifespan |
| $n$ | index | $\{0, 1, 2, \ldots\}$ | Generation index (dynasty-level; out-of-scope for the YAML) |
| $\tau$ | type | $\{1, 2, \ldots, 10\}$ | Earnings-profile decile; drawn at birth, fixed-within-life. Source: PSID via Heathcote-Perri-Violante (2010) |
| $r$ | type / parameter of lifetime | 5-state space $\{r_1, \ldots, r_5\}$ drawn at birth; paper Table 4 estimates: $\{0.0011, 0.0094, 0.0258, 0.0560, 0.0841\}$, mean $E(r) = 3.06\%$ | Within-life rate of return; fixed-within-life, Markov across generations |
| $a_t$ | **state (arrival perch)** | $a_t \in \mathbb{R}_{\ge 0}$ | Beginning-of-period wealth (before interest accrues and before current-period earnings arrive) |
| $w_t(\tau)$ | exogenous | $w_t(\tau) \ge 0$ | Deterministic earnings at age $t$ for type $\tau$; **bracket-piecewise-constant**: 6 age brackets of 6 years each (paper Table 1, ten rows × six columns); period $t$ maps to calendar age $24 + t$ (working life 25–60); within a bracket, $w_t(\tau)$ equals the bracket-average earnings of decile $\tau$ |
| $m_t$ | **state (decision perch)** | $m_t \in \mathbb{R}_{\ge 0}$ | Cash-on-hand at decision, $m_t = (1+r)a_t + w_t(\tau)$ |
| $c_t$ | **control (decision perch)** | $c_t \in [0, m_t]$ | Consumption |
| $a_{t+1}$ | **state (continuation perch)** | $a_{t+1} \in \mathbb{R}_{\ge 0}$ | End-of-period wealth; also arrival state of period $t+1$ |
| $a_{T+1}$ | **terminal quantity (bequest)** | $a_{T+1} \in \mathbb{R}_{\ge 0}$ | Bequest at end of life; enters warm-glow payoff $e$ |
| $\sigma$ | parameter (preference) | $\sigma > 0$, $\sigma \ne 1$; paper: $\sigma = 2$ (fixed) | CRRA coefficient of consumption utility |
| $\mu$ | parameter (preference) | $\mu > 0$, $\mu \ne 1$; paper Table 4: $\mu = 0.5993$ (s.e. 0.0061) | Curvature of warm-glow bequest kernel |
| $A$ | parameter (preference) | $A > 0$; paper Table 4: $A = 0.0006$ (s.e. 0.0004) | Weight on warm-glow bequest |
| $\beta$ | parameter (preference) | $\beta \in (0, 1)$; paper: $\beta = 0.97$ (fixed, annual) | Time-discount factor |
| $u(c_t)$ | payoff (decision perch, interior) | $\mathbb{R}$ | Per-period CRRA utility; $u(c_t) = c_t^{1-\sigma}/(1-\sigma)$ |
| $e(a_{T+1})$ | payoff (decision perch, terminal) | $\mathbb{R}$ | Warm-glow bequest utility; $e(a_{T+1}) = A\, a_{T+1}^{1-\mu}/(1-\mu)$ |
| $V^{\tau,r}_{t}(a_t)$ | value function | $\mathbb{R}$ | Lifetime value at arrival perch of period $t$, for type $(\tau, r)$ |
| $V^{\tau,r}_{t}{}'(m_t)$ | marginal value | $\mathbb{R}_{>0}$ | $\partial V^{\tau,r}_t / \partial m_t$; needed for EGM |
| $\mathbb{B}_t$ | mover | backward (continuation $\succ$ → decision $\circ$) | Bellman optimization: $\max_{c_t}\{u(c_t) + \beta V^{\tau,r}_{t+1}(a_{t+1})\}$ |
| $\mathbb{I}_t$ | mover | forward (decision $\circ$ → arrival $\prec$ of $t+1$) | Identity; there are no within-life shocks to integrate over |
| $\mathbb{T}_t$ | stage operator | $\mathbb{T}_t = \mathbb{I}_t \circ \mathbb{B}_t$ | Full stage transformation of value-function backward pass |
| $g(\cdot)$ | lifetime map | $\mathbb{R}_{\ge 0} \to \mathbb{R}_{\ge 0}$ | $a_{T+1} = g(a_1; \tau, r)$: maps initial wealth to bequest given type (derived from solving the parameterized family) |

**Notation on perch tags (when used).** We write $x_\prec$, $x_\circ$, $x_\succ$ to denote the value of a quantity $x$ at the arrival, decision, or continuation perch of a stage, respectively. In this model the decomposition is deliberately written so that each quantity has one unambiguous perch (see "Perch decomposition" below), so perch tags are usually not needed in the equations.

---

## Timing convention (within one period $t$)

Because the model has **no within-life stochastic shocks** (both $\tau$ and $r$ are drawn at birth and fixed; earnings $w_t(\tau)$ are deterministic given $\tau$), the within-period timing is minimal:

1. **Arrival ($\prec$) at period $t$.** Beginning-of-period wealth $a_t$ is carried in (from period $t-1$'s continuation, or, at $t=1$, from the newborn's initial draw). No within-life shocks resolve at this point — the type $(\tau, r)$ is already known from birth.
2. **Arrival → Decision transition $\mathrm{g}_{\prec\circ}$.** Cash-on-hand $m_t \coloneqq (1+r)\,a_t + w_t(\tau)$ is deterministically formed.
3. **Decision ($\circ$).** The agent observes $m_t$ and chooses $c_t \in [0, m_t]$. The no-borrowing constraint is $0 \le c_t \le m_t$.
4. **Decision → Continuation transition $\mathrm{g}_{\circ\succ}$.** End-of-period wealth is realized: $a_{t+1} = m_t - c_t$.
5. **Continuation ($\succ$).** $a_{t+1}$ becomes the arrival state of period $t+1$ (or, at $t = T$, the bequest $a_{T+1}$ entering the warm-glow payoff).

There are no "expectation" or "shock realization" steps within a period, because the within-life environment is deterministic given the type $(\tau, r)$.

---

## Preferences (explicit forms)

Per-period consumption utility is CRRA:

$$
u(c_t) \;=\; \frac{c_t^{1-\sigma}}{1-\sigma}, \qquad \sigma > 0,\; \sigma \ne 1.
$$

Terminal warm-glow bequest utility is CRRA-like in the bequest $a_{T+1}$:

$$
e(a_{T+1}) \;=\; A\,\frac{a_{T+1}^{1-\mu}}{1-\mu}, \qquad \mu > 0,\; \mu \ne 1,\; A > 0.
$$

The paper's baseline calibration fixes $\sigma = 2$ and estimates $\mu$ and $A$ via the method of simulated moments. The relation $\mu < \sigma$ drives the paper's **differential savings rates** result (rich save proportionally more) and a **thick right tail** in the stationary wealth distribution; see paper §I, characterization of the lifetime map $g(\cdot)$.

---

## Problem structure: periods, stages, perches

For a **given type assignment $(\tau, r)$** (a point in $\{1,\ldots,10\} \times \{r_1,\ldots,r_5\}$):

- The problem is a **finite-horizon, discrete-time** lifecycle problem over $t = 1, \ldots, T$ with $T = 36$ periods.
- Per matsya evaluation (`topics2026-benhabib-demo` Turn 3), the problem uses **one stage template** applied at every age, with a **terminal boundary wiring** at $t = T$ supplying $V_{[\succ]} = e(a_{[\succ]})$ and $dV_{[\succ]} = e'(a_{[\succ]})$ in place of the iterated downstream value. A separate `terminal_stage` block is **not** used.
- The stage has **three perches**: arrival $\prec$, decision $\circ$, continuation $\succ$.
- Because there are no within-life shocks, the **forward mover** $\mathbb{I}_t$ (decision → arrival, same stage, in the value-back-propagation sense) is **deterministic** — no expectation operator. It is **not** a literal identity, however: the arrival-to-decision map $m_t = (1+r)a_t + w_t(\tau)$ is non-trivial, so the marginal-value relation $dV_{[\prec]} = (1+r)\,dV$ picks up a chain-rule factor (the level relation $V_{[\prec]} = V$ remains a pass-through). See "Movers" below.

The full within-lifetime problem is therefore the sequential composition

$$
V^{\tau,r}_1 \;=\; (\mathbb{T}_1 \circ \mathbb{T}_2 \circ \cdots \circ \mathbb{T}_{T-1} \circ \mathbb{T}_T)[\,e(\cdot)\,]
$$

where each $\mathbb{T}_t$ uses the same stage template with $w_t(\tau)$ as an age-varying parameter. At the terminal age $t = T$, the boundary wiring replaces the iterated continuation input.

---

## Interior stage (used for $t = 1, \ldots, T-1$)

### Perch decomposition

| Perch | Objects (states / controls) | Key transition or Bellman step |
|:---|:---|:---|
| **Arrival** ($\prec$) | state $a_t \in \mathbb{R}_{\ge 0}$ (beginning-of-period wealth); value $V^{\tau,r}_t(a_t)$ | $\mathrm{g}_{\prec\circ}$: $m_t = (1+r)\,a_t + w_t(\tau)$ — deterministic resource construction |
| **Decision** ($\circ$) | state $m_t \in \mathbb{R}_{\ge 0}$; control $c_t \in [0, m_t]$; value $V^{\tau,r}_t(m_t)$ (equivalent to arrival value under the deterministic transition) | $\mathbb{B}_t$: $V^{\tau,r}_t(m_t) = \max_{c_t \in [0, m_t]}\bigl\{u(c_t) + \beta\,V^{\tau,r}_{t+1}(a_{t+1})\bigr\}$ — interior-period Bellman optimization |
| **Continuation** ($\succ$) | state $a_{t+1} \in \mathbb{R}_{\ge 0}$; value $V^{\tau,r}_{t+1}(a_{t+1})$ (the next period's arrival value) | $\mathrm{g}_{\circ\succ}$: $a_{t+1} = m_t - c_t$ — savings identity; inter-period connector is identity ($a_{\prec, t+1} = a_{\succ, t}$) |

### Transitions (within-stage)

- **Arrival → Decision** ($\mathrm{g}_{\prec\circ}$): $m_t = (1+r)\,a_t + w_t(\tau)$.
- **Decision → Continuation** ($\mathrm{g}_{\circ\succ}$): $a_{t+1} = m_t - c_t$.

### Movers

- **Backward mover $\mathbb{B}_t$** (continuation → decision; the optimization):

$$
V^{\tau,r}_t(m_t) \;=\; \max_{c_t \in [0, m_t]} \Bigl\{\; u(c_t) \;+\; \beta\, V^{\tau,r}_{t+1}(a_{t+1}) \;\Bigr\},
\qquad a_{t+1} = m_t - c_t.
$$

- **Forward mover $\mathbb{I}_t$** (decision → arrival, same stage; **deterministic**, no expectation, because no within-life shocks):

$$
V^{\tau,r}_{t,\prec}(a_t) \;=\; V^{\tau,r}_t\bigl(m_t(a_t)\bigr) \;=\; V^{\tau,r}_t\bigl((1+r)\,a_t + w_t(\tau)\bigr),
$$

$$
\frac{\partial V^{\tau,r}_{t,\prec}}{\partial a_t}(a_t) \;=\; \frac{\partial V^{\tau,r}_t}{\partial m_t}\bigl(m_t(a_t)\bigr) \cdot \frac{\partial m_t}{\partial a_t} \;=\; (1+r)\;\frac{\partial V^{\tau,r}_t}{\partial m_t}\bigl(m_t(a_t)\bigr).
$$

The level relation passes through (composing $V$ with the deterministic transition renames the argument from $m$ to $a$ but leaves the value unchanged); the marginal-value relation picks up the chain-rule factor $(1+r)$.

The **inter-period connector** is a separate object: it is the identity on the poststate–prestate wiring $a_{\succ, t} \mapsto a_{\prec, t+1}$, and carries no chain-rule factor (the state itself, not a function of the state, is being re-labeled across the period boundary).

**Canonical dolo-plus idiom** (per matsya evaluation, `topics2026-benhabib-demo` Turn 1, with the chain-rule factor on `dV[<]` corrected post-Turn 4 paper review — see Open issue #1):

```yaml
dcsn_to_arvl_mover:
  Bellman: |
    V[<] = V
  ShadowBellman: |
    dV[<] = (1+r) * dV
```

The Bellman is value pass-through; the ShadowBellman carries the $(1+r)$ chain-rule factor for the reasons given above. This matches the canonical `consumption_savings_iid.md` pattern `dV[<] = R * E_{θ}(dV)` specialized to the no-shock case (expectation dropped, $R \mapsto 1+r$). Status **PROVISIONAL** — no canonical example explicitly labeled "no-shock deterministic forward mover" found in the retrieved corpus, but the structural derivation above (paper §I, eq. for the budget constraint $a' = (1+r)a + w - c$ and the resulting envelope condition) is unambiguous. The `exogenous` block is correspondingly omitted, not declared-but-empty.

### Stage operator

$$
\mathbb{T}_t \;=\; \mathbb{I}_t \circ \mathbb{B}_t.
$$

Because $\mathbb{I}_t$ is identity, $\mathbb{T}_t = \mathbb{B}_t$ effectively reduces to the Bellman operator — but we keep the composition explicit to preserve the modular-DDSL structure the YAML will encode.

### EGM channel

Because $u(c) = c^{1-\sigma}/(1-\sigma)$ has invertible marginal utility, the **endogenous grid method** applies directly:

- **Envelope condition** (at the decision perch):
$$
V^{\tau,r}_t{}'(m_t) \;=\; u'(c_t) \;=\; c_t^{-\sigma}.
$$
- **Inverse Euler** (continuation-measurable $c_t$ recovered from $V^{\tau,r}_{t+1}{}'$):
$$
c_t \;=\; \Bigl(\beta\, V^{\tau,r}_{t+1}{}'(a_{t+1})\Bigr)^{-1/\sigma}.
$$
- **Reverse transition** (endogenous $m_t$ grid from $a_{t+1}$ grid):
$$
m_{t,[\succ]} \;=\; a_{t+1} + c_t.
$$

The standard EGM iteration is: choose a grid over $a_{t+1}$, apply inverse Euler pointwise to get $c_t(a_{t+1})$, form $m_{t,[\succ]} = a_{t+1} + c_t$, and interpolate $c_t(m_t)$ on the endogenous $m_t$ grid.

---

## Terminal stage (used at $t = T$)

Per matsya evaluation (`topics2026-benhabib-demo` Turn 3; status **PROVISIONAL** — recommended pattern has no canonical example in the retrieved corpus): the terminal stage is **the same stage template as the interior stage, with a terminal boundary wiring** that supplies $V_{[\succ]}$ and $dV_{[\succ]}$ as closed-form functions of the poststate rather than as outputs of a downstream Bellman solve. A separate `terminal_stage` block is **not recommended** — it violates compositionality.

### Boundary wiring at $t = T$

At the continuation perch of period $T$ (the poststate $a_{T+1}$ carries the bequest), the value and marginal-value inputs to the backward mover are closed-form. The paper's terminal recursion is $V_T(a) = u(c) + e(a')$ with **no $\beta$** on the bequest, but the standard Bellman wiring used in the interior template, $V = \max_c \{u(c) + \beta V_{[\succ]}\}$, automatically discounts $V_{[\succ]}$ by $\beta$. To recover the paper's $V_T$ exactly we absorb the missing factor into the boundary weight (see Open Issue #9, option (i)): define the effective bequest weight $\tilde A \equiv A / \beta$, so that

$$
V_{[\succ]}(a_{T+1}) \;=\; \tilde A\,\frac{a_{T+1}^{1-\mu}}{1-\mu} \;=\; \frac{e(a_{T+1})}{\beta},
$$

$$
dV_{[\succ]}(a_{T+1}) \;=\; \tilde A\, a_{T+1}^{-\mu} \;=\; \frac{e'(a_{T+1})}{\beta}.
$$

Then $\beta V_{[\succ]}(a_{T+1}) = e(a_{T+1})$ and $\beta\, dV_{[\succ]}(a_{T+1}) = e'(a_{T+1})$ exactly, matching the paper. The $\tilde A$ absorption is used **only at the terminal boundary**; the interior template is unchanged. With the paper's calibrated $A \approx 0.0006$ and $\beta = 0.97$, $\tilde A \approx 0.000619$.

These replace the iterated $V^{\tau,r}_{T+1}$ and $dV^{\tau,r}_{T+1}$ that would be produced by a downstream stage in the interior case.

### EGM channel at the terminal boundary

Applying the same Inverse Euler as the interior stage, with the boundary $dV_{[\succ]} = \tilde A\, a_{T+1}^{-\mu}$:

$$
c_{T,[\succ]} \;=\; \Bigl(\beta\, dV_{[\succ]}(a_{T+1})\Bigr)^{-1/\sigma} \;=\; \bigl(\beta\, \tilde A\, a_{T+1}^{-\mu}\bigr)^{-1/\sigma} \;=\; \bigl(A\, a_{T+1}^{-\mu}\bigr)^{-1/\sigma} \;=\; A^{-1/\sigma}\, a_{T+1}^{\mu/\sigma},
$$

where the $\beta$ factor cancels with $1/\beta$ in $\tilde A$, recovering the paper's terminal Inverse-Euler exactly.

Reverse transition: $m_{T,[\succ]} = a_{T+1} + c_{T,[\succ]}$. This produces the endogenous $m_T$ grid at period $T$ directly — no numerical root-find is required despite $\mu \ne \sigma$, because the Inverse Euler step inverts $u'(c) = c^{-\sigma}$ (always closed-form for CRRA) regardless of the functional form of $dV_{[\succ]}$. The $\mu \ne \sigma$ case is orthogonal to EGM's applicability.

### Differential-savings result (analytical)

Combining the Inverse-Euler solution $c_T = A^{-1/\sigma} a_{T+1}^{\mu/\sigma}$ with the budget identity $a_{T+1} = m_T - c_T$:

$$
m_T \;=\; c_T + a_{T+1} \;=\; A^{-1/\sigma}\, a_{T+1}^{\mu/\sigma} + a_{T+1}.
$$

As $m_T \to \infty$, $a_{T+1} \to \infty$, and since $\mu/\sigma < 1$ (in the paper's estimated $\mu < \sigma$ regime) the $a_{T+1}$ term dominates, so $a_{T+1}/m_T \to 1$: the **savings rate tends to 1** at the top. This is the analytical root of the paper's **differential savings** result (rich save proportionally more); the effect propagates backward through the recursion to earlier ages.

---

## Composition across periods (the lifecycle nest)

The within-lifetime problem is solved by **backward induction** from the terminal stage:

$$
V^{\tau,r}_T \;=\; \mathbb{T}^{\mathrm{term}}_T[\,e(\cdot)\,] \quad\longrightarrow\quad V^{\tau,r}_{T-1} \;=\; \mathbb{T}_{T-1}[\,V^{\tau,r}_T\,] \quad\longrightarrow\quad \cdots \quad\longrightarrow\quad V^{\tau,r}_1 \;=\; \mathbb{T}_1[\,V^{\tau,r}_2\,].
$$

The interior stage template is **repeated** for $t = 1, \ldots, T-1$, with age-varying parameter $w_t(\tau)$ overriding the earnings value at each period. The terminal stage template is applied **once** at $t = T$.

**Parameters that vary by age $t$ within a lifetime:** only $w_t(\tau)$. All other parameters ($r$, $\tau$, $\beta$, $\sigma$, $\mu$, $A$) are constant within a lifetime.

**Inter-period connector:** identity. Period $t$'s continuation perch state $a_{\succ, t} = a_{t+1}$ is wired directly to period $t+1$'s arrival perch state $a_{\prec, t+1}$, with value $V^{\tau,r}_{\succ, t} = V^{\tau,r}_{\prec, t+1}$.

---

## Parameterized family structure (the $(\tau, r)$ dimension)

The **full household problem** is a **parameterized family of Bellman problems** indexed by the type $(\tau, r) \in \{1,\ldots,10\} \times \{r_1,\ldots,r_5\}$ — 50 separate fixed-point problems in the baseline calibration.

A dolo-plus YAML must handle this parameterization. Two encoding options:

- **(A) Calibration-override family (the HAFiscal pattern):** encode a single interior-stage template, and instantiate 50 copies at different calibrations (one per $(\tau, r)$ pair). This is the clean choice when $\tau$ and $r$ are genuinely constant-within-life, as they are here.
- **(B) Discrete-state-resolved-at-birth:** encode $(\tau, r)$ as discrete state variables resolved only at the initial period $t = 1$ (effectively, a MC transition with mass 1 on the identity self-loop thereafter).

**Recommended: option (A)** — per matsya evaluation (`topics2026-benhabib-demo` Turn 2; status **UNRESOLVED**): "structurally sound" given the spec's separation of calibration from stage structure, but *"the mechanism for instantiating a family (calibration overrides, model-level type indexing) is not documented"* in matsya's retrieved corpus. Option (B) is explicitly rejected — matsya's verdict: *"Not recommended — violates measurability spirit"* (types would masquerade as dynamic states).

The YAML should follow pattern (A) and include a `# workaround: family-instantiation mechanism is UNRESOLVED — canonical dolo-plus spec on calibration-override families not located as of topics2026-benhabib-demo session` comment pending location of a HAFiscal or type-heterogeneity canonical example.

---

## Deliverable for the YAML

The minimum adequate `dolo-plus-draft.yaml` formalization consists of:

1. One `stage` declaration for the **single stage template** (matsya recommendation; not two separate interior/terminal blocks). Contains perches, within-stage transitions, the backward mover $\mathbb{B}$ (Bellman), a deterministic forward mover $\mathbb{I}$ with chain-rule factor (`V[<] = V; dV[<] = (1+r) * dV` — see Open issue #1 for derivation), the EGM mover block, and a symbols-conventions block matching the Symbol table above.
2. **Terminal boundary wiring** for $t = T$: supplies $V_{[\succ]}(a_{[\succ]}) = \tilde A\,a_{[\succ]}^{1-\mu}/(1-\mu)$ and $dV_{[\succ]}(a_{[\succ]}) = \tilde A\,a_{[\succ]}^{-\mu}$ — with $\tilde A \equiv A/\beta$ to neutralize the standard Bellman's $\beta$ factor (see Open issue #9) — in place of the iterated $V^{\tau,r}_{T+1}, dV^{\tau,r}_{T+1}$ that would otherwise flow from the next age.
3. A `calibration` block that parameterizes the **family** — ten age-profiles $w_t(\tau)$ for $\tau \in \{1, \ldots, 10\}$ (paper Table 1), five values for $r$, and the preference parameters $(\sigma, \mu, A, \beta)$.
4. An outer composition specifying the **lifecycle nest** (apply the stage template at $t = 1, \ldots, T$ with age-varying $w_t(\tau)$; at $t = T$ use the terminal boundary wiring).
5. An **instantiation mechanism** for the $(\tau, r)$ family, following option (A) calibration-override — pending resolution of the UNRESOLVED canonical-idiom gap, with an inline `# workaround:` comment.

---

## Open issues / flagged gaps — status after matsya evaluation (session `topics2026-benhabib-demo`)

The items below were drafted as open questions for the first matsya round; their post-evaluation status is recorded here.

### Resolved / addressed

1. **Deterministic (no-shock) forward mover $\mathbb{I}_t$.** *Initially resolved* by matsya (Turn 1) as `V[<] = V; dV[<] = dV`; **corrected** post-Turn 4 paper review. Matsya's Turn 1 answer applied the "identity twister" dev-spec pattern (where the arrival-to-decision map is itself the identity, $g_{\prec\circ} = \mathrm{id}$). In BBL the arrival-to-decision map is *not* identity — it is $m_t = (1+r)a_t + w_t(\tau)$, a non-trivial deterministic transformation with Jacobian $(1+r)$. The two properties matsya conflated — (i) absence of stochastic integration (yes, no within-life shocks) and (ii) literal identity transformation between perch states (no, $m \ne a$) — are independent. The correct idiom is `V[<] = V; dV[<] = (1+r) * dV`: the level passes through but the marginal picks up the chain-rule factor. Status **PROVISIONAL** for syntax — the pattern matches `consumption_savings_iid.md`'s `dV[<] = R * E_{θ}(dV)` specialized to the no-shock case (expectation dropped, $R \mapsto 1+r$), but no canonical example explicitly labeled "no-shock deterministic forward mover" was located. The `exogenous` block is omitted (not declared-but-empty). The YAML should include an inline comment citing the PROVISIONAL status of the syntax (the chain-rule factor itself is unambiguous from the paper's envelope condition).

2. **Parameterized-family dimension $(\tau, r)$.** *Addressed* by matsya (Turn 2); definitively re-confirmed 2026-04-27. Option (A) calibration-override family is recommended over option (B) discrete-state-at-birth. **Data resolved:** the YAML's `calibration_family` block now carries paper-faithful values — `shared` parameters from Table 4, `by_r_type.r` from the 5-state estimate (Table 4 "State space" row), `by_tau.w` from Table 1 (10×6 earnings matrix). **Syntax UNRESOLVED definitively** — the `calibration_family` keyword and its sub-keys (`shared`, `by_r_type`, `by_tau`, `cardinality`) have no canonical analogue in the indexed dolo-plus corpus (matsya 2026-04-27 review: no HAFiscal, AgentType-style, or family-block syntax has been indexed). The structure is SPECULATIVE; sub-key names may need to be renamed once a canonical idiom appears.

3. **Warm-glow terminal closure.** *Resolved* by matsya (Turn 3). Recommended: the interior template with terminal boundary wiring $V_{[\succ]} \propto a_{[\succ]}^{1-\mu}/(1-\mu)$, $dV_{[\succ]} \propto a_{[\succ]}^{-\mu}$. A separate `terminal_stage` block is explicitly **not** recommended (violates compositionality). Status **PROVISIONAL**. **Discount-factor refinement (Open issue #9, option (i)):** matsya's Turn 3 wrote the boundary as $V_{[\succ]} = e(a)$, but the standard Bellman wiring $V = \max_c\{u(c) + \beta V_{[\succ]}\}$ would then introduce a $\beta$ factor that the paper's terminal recursion does not have. To match the paper, the boundary uses an effective bequest weight $\tilde A \equiv A/\beta$ in place of $A$; the resulting $\beta V_{[\succ]} = e(a)$ then matches paper exactly.

4. **Terminal FOC invertibility (previously flagged as a concern).** *Corrected* by matsya (Turn 3). The $\mu \ne \sigma$ case does **not** require a numerical root-find: the Inverse Euler step inverts $u'(c) = c^{-\sigma}$ regardless of the functional form of $dV_{[\succ]}$. The terminal boundary's $dV_{[\succ]}$ plugs into the same Inverse Euler the interior stage uses. This previously-flagged concern was based on thinking about fixed-grid root-finding; under EGM it is not an issue.

8. **Consumption upper-bound: paper writes $0 \le c \le a$.** Paper §I, second display equation in the recursion, writes the constraint as "$0 \le c \le a$, $t = 1, \ldots, T - 1$" — i.e., consumption bounded above by *beginning-of-period wealth* $a_t$, not by *cash-on-hand* $m_t = (1+r)a_t + w_t(\tau)$. With $r > 0$ and $w_t > 0$, this would be strictly more restrictive than the standard no-borrowing constraint. **Resolved (treated as typo).** The natural reading is that the upper-bound symbol "$a$" is a typo for "$a'$", giving the no-borrowing constraint $a_{t+1} \ge 0$, equivalent to $c_t \le m_t$. The excerpt and YAML adopt the standard interpretation $c_t \in [0, m_t]$. (See open issue #7: under this interpretation, $a_{t+1} \ge 0$ holds automatically and no redundant poststate constraint is needed.)

9. **Discount-factor convention on the terminal bequest.** Paper §I, last line of the recursion, writes $V_T(a) = u(c) + e(a')$ — bequest realized in the same period as terminal consumption, with **no $\beta$**. The excerpt's terminal-boundary wiring (single-template + $V_{[\succ]} = e(a_{[\succ]})$ flowing through the standard backward mover, whose Bellman is $V = \max_c \{u(c) + \beta V_{[\succ]}\}$) would otherwise effectively give $V_T = u(c) + \beta\, e(a')$. **Resolved with option (i): absorb $\beta$ into the boundary weight.** Define $\tilde A \equiv A / \beta$ at the terminal boundary only; the boundary becomes $V_{[\succ]} = \tilde A\, a^{1-\mu}/(1-\mu) = e(a)/\beta$ and $dV_{[\succ]} = \tilde A\, a^{-\mu} = e'(a)/\beta$, so $\beta V_{[\succ]} = e(a)$ exactly, matching the paper's $V_T$. Single-template structure is preserved; the interior template is unchanged. The paper's calibrated $A \approx 0.0006$ corresponds to $\tilde A \approx 0.000619$ at the boundary. The "Boundary wiring at $t=T$", "EGM channel at the terminal boundary", and "Differential-savings result" subsections above have been updated to use $\tilde A$; the resulting $c_T = A^{-1/\sigma} a_{T+1}^{\mu/\sigma}$ matches the paper exactly.

### Still open

5. **Lifecycle nest with age-varying $w_t(\tau)$.** *Data resolved; syntax UNRESOLVED definitively.*
   - **Data:** Paper Table 1 (10 deciles × 6 age brackets, in $thousands per year) has been transcribed into `dolo-plus-draft.yaml` as `calibration_family.by_tau.<decile>.w` (six-element list per decile). The schedule is **bracket-piecewise-constant** (not linearly interpolated as earlier drafts of this excerpt assumed): paper §IIB states agents stay in the same decile for life, and each cell of Table 1 is the bracket-average earnings of that decile. Each bracket spans 6 calendar years (T = 36 = 6 × 6); period $t$ maps to calendar age $24 + t$, so working life is ages 25–60. The age-bracket → period map is in `calibration_family.age_bracket_to_period`.
   - **Syntax:** Canonical dolo-plus mechanism for picking up the right $w_t(\tau)$ value at each $(t, \tau)$ pair on a repeated stage **does not exist in the indexed corpus** — definitively confirmed by matsya 2026-04-27 review (no `lifecycle:` block, no age-indexed calibration override, no period-template mechanism for repeating one stage with varying parameters). The data is in the YAML; the dolo-plus spec needs to add the addressing mechanism before the YAML can be runnable. **Status:** data complete; syntax UNRESOLVED at the spec level (not a search failure).

6. **Section IIID wealth-dependent $r$ extension — out of scope for baseline YAML.** The baseline formalization treats $r$ as fixed-within-life. The extension $r = r_0 + b \cdot p(a)$ (where $p(a)$ is a wealth-percentile index) is a **substantive change to the `exogenous` block** (state-contingent $r$ rather than fixed-at-birth $r$) and belongs in a **second, separate YAML** for the extension — not the baseline.

7. **Non-negativity of $a_{t+1}$ from the no-borrowing constraint.** Under the standard interpretation $0 \le c_t \le m_t$, $a_{t+1} = m_t - c_t \ge 0$ holds automatically. The YAML should not declare a redundant poststate constraint; the control-bound constraint is sufficient. No matsya input needed for this.

---

## Out-of-scope, for reference only

The **dynasty-level** composition — where $(\tau^n, r^n)$ evolves across generations via independent intergenerational Markov chains, and newborn wealth $a^n_1 = g(a^{n-1}_1; \tau^n, r^n)$ is determined by the parent's terminal wealth through the lifetime map — is **not** part of the YAML formalization. It is a simulation-layer operation on top of 50 pre-solved lifetime value functions, one per $(\tau, r)$ pair. See [`_summary.ipynb` → "The Model" → "Stochastic Structure"](Benhabib_et_al_2019_summary.ipynb) and the original paper §I for that outer structure, including the paper's Proposition relating $\mu$ vs. $\sigma$ to stationarity and Pareto-tail existence.

**Numerical dynasty-layer matrices (out-of-scope but cataloged in `dolo-plus-draft.yaml`):** the YAML's `calibration_family.population` block records what is known and where the rest lives.

- $\Pi_r$ (5 × 5): paper Table 4 reports the diagonal $\{0.0338, 0.2676, 0.1360, 0.2630, 0.0208\}$; off-diagonal structure is described in paper footnote 13 (decay in rows 1–4, constant in row 5); the **full numerical matrix is in online Appendix C.1**, which is not in the repo's `Benhabib_et_al_2019.mmd` and would need separate download from the AEA archive. The YAML flags this as `# unresolved: full off-diagonal matrix from online Appendix C.1`.
- $\Pi_\tau$ (10 × 10): from Chetty et al. (2014) reduced to a 10-state chain (paper §IIB); **full matrix is in online Appendix B.2**, also not in the .mmd. The YAML flags this as `# unresolved: full matrix entries from online Appendix B.2`.

These matrices are needed only at the dynasty-simulation layer, not for the within-lifetime Bellman, so their absence does not block formalization of the stage problem.
