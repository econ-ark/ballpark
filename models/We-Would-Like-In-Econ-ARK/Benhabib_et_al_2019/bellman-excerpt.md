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
- The problem admits **two stage templates**:
  - **Interior stage** (used at $t = 1, \ldots, T-1$): Bellman optimization with continuation value $V^{\tau,r}_{t+1}$.
  - **Terminal stage** (used at $t = T$): Bellman optimization with warm-glow closure $e(a_{T+1})$ replacing the continuation value.
- Each stage has **three perches**: arrival $\prec$, decision $\circ$, continuation $\succ$.
- Because there are no within-life shocks, the **forward mover** $\mathbb{I}_t$ (decision → arrival of $t+1$) is an **identity**; this is an explicitly degenerate but legitimate mover in the modular-DDSL formalism.

The full within-lifetime problem is therefore the sequential composition

$$
V^{\tau,r}_1 \;=\; (\mathbb{T}_1 \circ \mathbb{T}_2 \circ \cdots \circ \mathbb{T}_{T-1} \circ \mathbb{T}^{\mathrm{term}}_T)[\,e(\cdot)\,]
$$

where each interior $\mathbb{T}_t$ uses the interior stage template with $w_t(\tau)$ as an age-varying parameter, and $\mathbb{T}^{\mathrm{term}}_T$ uses the terminal stage template.

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

### Perch decomposition

| Perch | Objects | Key transition or Bellman step |
|:---|:---|:---|
| **Arrival** ($\prec$) | state $a_T \in \mathbb{R}_{\ge 0}$; value $V^{\tau,r}_T(a_T)$ | $\mathrm{g}_{\prec\circ}$: $m_T = (1+r)\,a_T + w_T(\tau)$ |
| **Decision** ($\circ$) | state $m_T$; control $c_T \in [0, m_T]$; terminal value | $\mathbb{B}_T^{\mathrm{term}}$: $V^{\tau,r}_T(m_T) = \max_{c_T \in [0, m_T]}\bigl\{u(c_T) + e(a_{T+1})\bigr\}$ |
| **Continuation** ($\succ$) | state $a_{T+1} \in \mathbb{R}_{\ge 0}$ (the bequest); warm-glow payoff $e(a_{T+1})$ applied | $\mathrm{g}_{\circ\succ}$: $a_{T+1} = m_T - c_T$ — savings identity; no inter-period connector (life ends) |

### Movers

- **Backward mover $\mathbb{B}_T^{\mathrm{term}}$** (continuation → decision at $T$; the terminal optimization):

$$
V^{\tau,r}_T(m_T) \;=\; \max_{c_T \in [0, m_T]} \Bigl\{\; u(c_T) \;+\; e(a_{T+1}) \;\Bigr\},
\qquad a_{T+1} = m_T - c_T.
$$

- **Forward mover $\mathbb{I}_T$:** **not applicable** — the agent does not survive to a period $T+1$, so there is no arrival of $t+1$ to integrate into. The terminal stage's continuation perch directly produces the bequest $a_{T+1}$ as the terminal-payoff input.

### EGM channel (terminal period)

The first-order condition at $t = T$ equates the marginal utility of consumption to the marginal warm-glow utility of bequeathing:

$$
u'(c_T) \;=\; \frac{\partial e(a_{T+1})}{\partial a_{T+1}} \quad\Longleftrightarrow\quad c_T^{-\sigma} \;=\; A\, a_{T+1}^{-\mu}.
$$

Combined with the budget identity $a_{T+1} = m_T - c_T$, this gives a one-dimensional root-find in $c_T$ (or, equivalently, a one-dimensional EGM inversion with the terminal FOC replacing the continuation-value envelope).

### Differential-savings result

The relationship $c_T^{-\sigma} = A\, a_{T+1}^{-\mu}$ implies

$$
a_{T+1} \;=\; A^{1/\mu}\, c_T^{\sigma/\mu}.
$$

When $\mu < \sigma$ (the paper's estimated regime), $\sigma/\mu > 1$, so the bequest-to-consumption ratio is **increasing** in $c_T$, which itself grows with $m_T$ — hence the paper's **differential savings rate (rich save proportionally more)** emerges from the curvature mismatch at the terminal stage and propagates backward through the recursion.

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

- **(A) Calibration-override family (the HAFiscal pattern):** encode a single interior-stage template and a single terminal-stage template, and instantiate 50 copies at different calibrations (one per $(\tau, r)$ pair). This is the clean choice when $\tau$ and $r$ are genuinely constant-within-life, as they are here.
- **(B) Discrete-state-resolved-at-birth:** encode $(\tau, r)$ as discrete state variables resolved only at the initial period $t = 1$ (effectively, a MC transition with mass 1 on the identity self-loop thereafter). Less clean but semantically equivalent.

**Recommended:** option (A). Option (B) would misleadingly suggest within-life uncertainty in $(\tau, r)$, which there is none of.

---

## Deliverable for the YAML

The minimum adequate `dolo-plus-draft.yaml` formalization consists of:

1. One `stage` declaration for the **interior period template**, with perches, transitions, movers (including an explicit identity forward mover), the EGM mover block, and a symbols-conventions block matching the Symbol table above.
2. One `stage` declaration for the **terminal period**, with the warm-glow closure and the terminal FOC.
3. A `calibration` block that parameterizes the **family** — ten values for $w_t(\tau)$ at each age, five values for $r$, and the preference parameters $(\sigma, \mu, A, \beta)$.
4. An outer composition specifying **lifecycle nest** (repeat interior for $t = 1, \ldots, T-1$; terminal at $T$).

---

## Open issues / flagged gaps for the Matsya iteration

Items the Matsya iteration should explicitly validate or flag as workarounds:

1. **Degenerate forward mover $\mathbb{I}_t = \mathrm{id}$.** There are no within-life shocks. Matsya should confirm the dolo-plus `exogenous` block can be omitted (not just empty-but-declared) and that a pure-identity $\mathbb{I}_t$ is canonical. The `cons_stage_no_shocks` or `deterministic_lifecycle` template, if it exists, is the appropriate reference.

2. **Parameterized-family dimension $(\tau, r)$.** Matsya should confirm whether dolo-plus's calibration-override family (option A above) is the canonical encoding for parameters that are drawn at birth but fixed within a life. The HAFiscal formalization uses this pattern for $(\beta_i, e)$; the mechanism should transfer.

3. **Warm-glow terminal closure.** Matsya should confirm the canonical idiom for a terminal period whose continuation is a closed-form function $e(a_{T+1})$ rather than a continuation value. Candidates: (i) treating $e$ as the "next period's arrival value" and running the interior template with a degenerate terminal wiring; (ii) a dedicated `terminal_stage` block. The worked example `cons_stage` patterns may favor one.

4. **Lifecycle nest with age-varying $w_t(\tau)$.** Matsya should confirm the canonical syntax for overriding a single parameter ($w_t$) at each repetition of the interior template across $t$. The paper provides $w_t(\tau)$ as a $10 \times 6$ age-bracket matrix (Table 1), interpolated linearly within bracket; the YAML should reference this table rather than hard-code 36 values.

5. **Section IIID wealth-dependent $r$ extension — out of scope.** The baseline formalization treats $r$ as fixed-within-life. The Section IIID extension allows $r = r_0 + b \cdot p(a)$ where $p(a)$ is a wealth-percentile index and $b$ is estimated. This is a **substantive change to the exogenous block** (state-contingent $r$ rather than fixed-at-birth $r$) and belongs in a **second, separate YAML** for the extension — not the baseline.

6. **Terminal FOC invertibility.** The terminal FOC $c_T^{-\sigma} = A\, a_{T+1}^{-\mu}$ with budget $a_{T+1} = m_T - c_T$ has a unique solution in $c_T$ for all $m_T > 0$, but no closed form (because $\sigma \ne \mu$ in the paper's estimated regime). Matsya should confirm whether dolo-plus's EGM block supports the terminal FOC pattern $u'(c_T) = e'(a_{T+1})$ directly, or whether a numerical one-dimensional root-find must be coded inline.

7. **Non-negativity of $a_{t+1}$ from the no-borrowing constraint.** The constraint $0 \le c_t \le m_t$ implies $a_{t+1} = m_t - c_t \ge 0$ automatically. The YAML should not declare a redundant poststate constraint; the control-bound constraint is sufficient.

---

## Out-of-scope, for reference only

The **dynasty-level** composition — where $(\tau^n, r^n)$ evolves across generations via independent intergenerational Markov chains, and newborn wealth $a^n_1 = g(a^{n-1}_1; \tau^n, r^n)$ is determined by the parent's terminal wealth through the lifetime map — is **not** part of the YAML formalization. It is a simulation-layer operation on top of 50 pre-solved lifetime value functions, one per $(\tau, r)$ pair. See [`_summary.ipynb` → "The Model" → "Stochastic Structure"](Benhabib_et_al_2019_summary.ipynb) and the original paper §I for that outer structure, including the paper's Proposition relating $\mu$ vs. $\sigma$ to stationarity and Pareto-tail existence.
