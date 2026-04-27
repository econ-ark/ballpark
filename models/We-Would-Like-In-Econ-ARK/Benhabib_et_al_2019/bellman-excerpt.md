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
| $\tau$ | type | $\{1, 2, \ldots, 10\}$ | Earnings-profile type; drawn at birth, fixed-within-life |
| $r$ | type / parameter of lifetime | 5-state space $\{r_1, \ldots, r_5\}$ drawn at birth; $r_i > -1$ | Within-life rate of return; fixed-within-life, Markov across generations |
| $a_t$ | **state (arrival perch)** | $a_t \in \mathbb{R}_{\ge 0}$ | Beginning-of-period wealth (before interest accrues and before current-period earnings arrive) |
| $w_t(\tau)$ | exogenous | $w_t(\tau) \ge 0$ | Deterministic earnings at age $t$ for type $\tau$; calibrated from PSID (paper Table 1) |
| $m_t$ | **state (decision perch)** | $m_t \in \mathbb{R}_{\ge 0}$ | Cash-on-hand at decision, $m_t = (1+r)a_t + w_t(\tau)$ |
| $c_t$ | **control (decision perch)** | $c_t \in [0, m_t]$ | Consumption |
| $a_{t+1}$ | **state (continuation perch)** | $a_{t+1} \in \mathbb{R}_{\ge 0}$ | End-of-period wealth; also arrival state of period $t+1$ |
| $a_{T+1}$ | **terminal quantity (bequest)** | $a_{T+1} \in \mathbb{R}_{\ge 0}$ | Bequest at end of life; enters warm-glow payoff $e$ |
| $\sigma$ | parameter (preference) | $\sigma > 0$, $\sigma \ne 1$; paper: $\sigma = 2$ (fixed) | CRRA coefficient of consumption utility |
| $\mu$ | parameter (preference) | $\mu > 0$, $\mu \ne 1$; paper: $\mu \approx 0.60$ (estimated) | Curvature of warm-glow bequest kernel |
| $A$ | parameter (preference) | $A > 0$; paper: $A \approx 0.0006$ (estimated) | Weight on warm-glow bequest |
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
- Because there are no within-life shocks, the **forward mover** $\mathbb{I}_t$ (decision → arrival of $t+1$) is an **identity**; this is an explicitly degenerate but legitimate mover in the modular-DDSL formalism.

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

- **Forward mover $\mathbb{I}_t$** (decision → arrival of $t+1$; **identity**, because no within-life shocks):

$$
V^{\tau,r}_{t,\prec}(a_t) \;=\; V^{\tau,r}_t\bigl(m_t(a_t)\bigr) \;=\; V^{\tau,r}_t\bigl((1+r)\,a_t + w_t(\tau)\bigr).
$$

Equivalently, in compact form, the inter-period connector $\mathbb{I}_t$ is the identity on the poststate–prestate wiring $a_{\succ, t} \mapsto a_{\prec, t+1}$.

**Canonical dolo-plus idiom** (per matsya evaluation, `topics2026-benhabib-demo` Turn 1; status **PROVISIONAL** — structurally valid per the "identity twister" dev-spec, no canonical example explicitly labeled identity-mover found in the corpus):

```yaml
dcsn_to_arvl_mover:
  Bellman: |
    V[<] = V
  ShadowBellman: |
    dV[<] = dV
```

(i.e., pure value pass-through, no expectation operator.) The `exogenous` block is correspondingly omitted, not declared-but-empty.

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

At the continuation perch of period $T$ (the poststate $a_{T+1}$ carries the bequest), the value and marginal-value inputs to the backward mover are closed-form:

$$
V_{[\succ]}(a_{T+1}) \;=\; e(a_{T+1}) \;=\; A\,\frac{a_{T+1}^{1-\mu}}{1-\mu},
$$

$$
dV_{[\succ]}(a_{T+1}) \;=\; e'(a_{T+1}) \;=\; A\, a_{T+1}^{-\mu}.
$$

These replace the iterated $V^{\tau,r}_{T+1}$ and $dV^{\tau,r}_{T+1}$ that would be produced by a downstream stage in the interior case.

### EGM channel at the terminal boundary

Applying the same Inverse Euler as the interior stage, with the boundary $dV_{[\succ]}$:

$$
c_{T,[\succ]} \;=\; \Bigl(\beta\, dV_{[\succ]}(a_{T+1})\Bigr)^{-1/\sigma} \;=\; \bigl(\beta\, A\, a_{T+1}^{-\mu}\bigr)^{-1/\sigma} \;=\; (\beta A)^{-1/\sigma}\, a_{T+1}^{\mu/\sigma}.
$$

Reverse transition: $m_{T,[\succ]} = a_{T+1} + c_{T,[\succ]}$. This produces the endogenous $m_T$ grid at period $T$ directly — no numerical root-find is required despite $\mu \ne \sigma$, because the Inverse Euler step inverts $u'(c) = c^{-\sigma}$ (always closed-form for CRRA) regardless of the functional form of $dV_{[\succ]}$. The $\mu \ne \sigma$ case is orthogonal to EGM's applicability.

### Differential-savings result (analytical)

Combining the Inverse-Euler solution $c_T = (\beta A)^{-1/\sigma} a_{T+1}^{\mu/\sigma}$ with the budget identity $a_{T+1} = m_T - c_T$:

$$
m_T \;=\; c_T + a_{T+1} \;=\; (\beta A)^{-1/\sigma}\, a_{T+1}^{\mu/\sigma} + a_{T+1}.
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

1. One `stage` declaration for the **single stage template** (matsya recommendation; not two separate interior/terminal blocks). Contains perches, within-stage transitions, the backward mover $\mathbb{B}$ (Bellman), an explicitly-identity forward mover $\mathbb{I}$ (`V[<] = V; dV[<] = dV`), the EGM mover block, and a symbols-conventions block matching the Symbol table above.
2. **Terminal boundary wiring** for $t = T$: supplies $V_{[\succ]}(a_{[\succ]}) = A\,a_{[\succ]}^{1-\mu}/(1-\mu)$ and $dV_{[\succ]}(a_{[\succ]}) = A\,a_{[\succ]}^{-\mu}$ in place of the iterated $V^{\tau,r}_{T+1}, dV^{\tau,r}_{T+1}$ that would otherwise flow from the next age.
3. A `calibration` block that parameterizes the **family** — ten age-profiles $w_t(\tau)$ for $\tau \in \{1, \ldots, 10\}$ (paper Table 1), five values for $r$, and the preference parameters $(\sigma, \mu, A, \beta)$.
4. An outer composition specifying the **lifecycle nest** (apply the stage template at $t = 1, \ldots, T$ with age-varying $w_t(\tau)$; at $t = T$ use the terminal boundary wiring).
5. An **instantiation mechanism** for the $(\tau, r)$ family, following option (A) calibration-override — pending resolution of the UNRESOLVED canonical-idiom gap, with an inline `# workaround:` comment.

---

## Open issues / flagged gaps — status after matsya evaluation (session `topics2026-benhabib-demo`)

The items below were drafted as open questions for the first matsya round; their post-evaluation status is recorded here.

### Resolved / addressed

1. **Degenerate forward mover $\mathbb{I}_t = \mathrm{id}$.** *Resolved* by matsya (Turn 1). Canonical YAML idiom is the value pass-through pattern `V[<] = V; dV[<] = dV`, with the `exogenous` block omitted (not declared-but-empty). Status **PROVISIONAL** — no canonical example explicitly labeled "identity mover" found, but the pattern is structurally valid per the "identity twister" dev-spec. The YAML should include an inline comment citing the PROVISIONAL status.

2. **Parameterized-family dimension $(\tau, r)$.** *Addressed* by matsya (Turn 2). Option (A) calibration-override family is recommended over option (B) discrete-state-at-birth. Status **UNRESOLVED** — mechanism for instantiation not found in matsya's retrieved corpus. The YAML should include a `# workaround:` comment flagging the gap.

3. **Warm-glow terminal closure.** *Resolved* by matsya (Turn 3). Recommended: the interior template with terminal boundary wiring $V_{[\succ]} = e(a_{[\succ]})$, $dV_{[\succ]} = A\,a_{[\succ]}^{-\mu}$. A separate `terminal_stage` block is explicitly **not** recommended (violates compositionality). Status **PROVISIONAL**.

4. **Terminal FOC invertibility (previously flagged as a concern).** *Corrected* by matsya (Turn 3). The $\mu \ne \sigma$ case does **not** require a numerical root-find: the Inverse Euler step inverts $u'(c) = c^{-\sigma}$ regardless of the functional form of $dV_{[\succ]}$. The terminal boundary's $dV_{[\succ]} = A\,a_{[\succ]}^{-\mu}$ plugs into the same Inverse Euler the interior stage uses. This previously-flagged concern was based on thinking about fixed-grid root-finding; under EGM it is not an issue.

### Still open

5. **Lifecycle nest with age-varying $w_t(\tau)$.** The paper provides $w_t(\tau)$ as a $10 \times 6$ age-bracket matrix (paper Table 1), interpolated linearly within bracket; the YAML should reference this table. Canonical dolo-plus syntax for per-age parameter overrides on a repeated stage was not asked of matsya in this round; a follow-up query may be needed. **Status:** flagged inline as `# unresolved:` in the YAML's `parameters:` block and in each `calibration_family:` instance — pending the canonical-syntax follow-up.

6. **Section IIID wealth-dependent $r$ extension — out of scope for baseline YAML.** The baseline formalization treats $r$ as fixed-within-life. The extension $r = r_0 + b \cdot p(a)$ (where $p(a)$ is a wealth-percentile index) is a **substantive change to the `exogenous` block** (state-contingent $r$ rather than fixed-at-birth $r$) and belongs in a **second, separate YAML** for the extension — not the baseline.

7. **Non-negativity of $a_{t+1}$ from the no-borrowing constraint.** The constraint $0 \le c_t \le m_t$ implies $a_{t+1} = m_t - c_t \ge 0$ automatically. The YAML should not declare a redundant poststate constraint; the control-bound constraint is sufficient. No matsya input needed for this.

---

## Out-of-scope, for reference only

The **dynasty-level** composition — where $(\tau^n, r^n)$ evolves across generations via independent intergenerational Markov chains, and newborn wealth $a^n_1 = g(a^{n-1}_1; \tau^n, r^n)$ is determined by the parent's terminal wealth through the lifetime map — is **not** part of the YAML formalization. It is a simulation-layer operation on top of 50 pre-solved lifetime value functions, one per $(\tau, r)$ pair. See [`_summary.ipynb` → "The Model" → "Stochastic Structure"](Benhabib_et_al_2019_summary.ipynb) and the original paper §I for that outer structure, including the paper's Proposition relating $\mu$ vs. $\sigma$ to stationarity and Pareto-tail existence.
