# HKS (2018) — Stage-Structured Bellman Problem

Improved stage-structured description of the household decision problem
in Hubmer, Krusell, and Smith (2018), *A Comprehensive Quantitative
Theory of the U.S. Wealth Distribution*.

Derived from `HKS_bellman_excerpt.md` (the faithful mathematical excerpt)
and rewritten following the modular stage architecture described in
SolvingMicroDSOPs (Sections 12–13): arrival / decision / continuation
perches, explicit state vectors at each perch, clear identification of
controls and transitions.

Cross-checked against `Acalin_HKS.ipynb` (Cell 4) as a supporting
summary.

---

## 1. The Household Bellman Equation

The household's recursive problem (faithful to HKS notation):

$$
V_t(x_t, p_t, \beta_t)
= \max_{a_{t+1} \in [\underline{a},\, x_t]}
\Big\{
  u(x_t - a_{t+1})
  + \beta_t\,
    \mathbb{E}\!\left[
      V_{t+1}(x_{t+1}, p_{t+1}, \beta_{t+1})
      \;\middle|\;
      p_t,\, \beta_t
    \right]
\Big\}
$$

with $u(c) = c^{1-\gamma}/(1-\gamma)$, and next-period cash-on-hand:

$$
x_{t+1}
= a_{t+1}
  + y_{t+1} - \tau_{t+1}(y_{t+1})
  + (1 - \tilde{\tau}_{t+1})\,\tilde{y}_{t+1}
  + T_{t+1}
$$

where

$$
y_{t+1}
= \bigl(r_{t+1} + r^X_{t+1}(a_{t+1})\bigr)\,a_{t+1}
  + w_{t+1}\,l(p_{t+1}, \nu_{t+1}),
\qquad
\tilde{y}_{t+1}
= \sigma^X(a_{t+1})\,\eta_{t+1}\,a_{t+1}.
$$

**Individual states:** $(x_t, p_t, \beta_t)$.
**Control:** $a_{t+1}$.
**Shocks:** $(p_{t+1}, \beta_{t+1}, \nu_{t+1}, \eta_{t+1})$.

**Aggregate prices / policy (taken as given by the household):**
$(w_t,\, r_t,\, T_t,\, \tau_t(\cdot),\, \tilde{\tau}_t,\,
r^X_t(\cdot),\, \sigma^X(\cdot))$.

---

## 2. Two-Stage Decomposition

Following the modular architecture of SolvingMicroDSOPs (Sections
12–13), each period is decomposed into two stages composed in sequence:

$$
\text{Period}_t
= \underbrace{\text{Consumption stage}}_{\text{decision: choose } a}
\;\circ\;
\underbrace{\text{Shock-resolution stage}}_{\text{no decision: shocks resolve, form } x'}
$$

**Backward solution** proceeds right-to-left: solve the
shock-resolution stage first (forming the expected continuation value),
then solve the consumption stage (optimizing over $a$).

**Forward simulation** proceeds left-to-right: consumption stage first,
then shock-resolution.

---

## 3. Consumption Stage

This stage contains the **only decision** in the period. It is
analogous to the standard consumption stage in SolvingMicroDSOPs, with
end-of-period assets $a$ as the sole control.

### Perch table

| Perch | State vector | Value function |
|---|---|---|
| Arrival $[\prec]$ | $(x,\, p,\, \beta)$ | $\mathrm{v}^{\text{cons}}_\prec(x, p, \beta)$ |
| Decision | $(x,\, p,\, \beta)$ | $\mathrm{v}^{\text{cons}}(x, p, \beta)$ |
| Continuation $[\succ]$ | $(a,\, p,\, \beta)$ | $\mathrm{v}^{\text{cons}}_\succ(a, p, \beta)$ |

### Arrival → Decision transition

Identity map — no shocks resolve, no new information:

$$
(x, p, \beta) \;\mapsto\; (x, p, \beta).
$$

Hence $\mathrm{v}^{\text{cons}}_\prec = \mathrm{v}^{\text{cons}}$.

### Decision perch: optimisation

**Control:** $a \in [\underline{a},\, x]$.

**Residual consumption:** $c = x - a$.

**Bellman equation at the decision perch:**

$$
\mathrm{v}^{\text{cons}}(x, p, \beta)
= \max_{a \in [\underline{a},\, x]}
\Big\{
  u(x - a)
  + \beta \cdot \mathrm{v}^{\text{cons}}_\succ(a, p, \beta)
\Big\}
$$

$\beta$ appears as a **state-dependent discount factor** multiplying the
continuation value, not as a fixed parameter.

### Decision → Continuation transition

Deterministic. The control $a$ becomes the post-state; persistent states
pass through:

$$
(x, p, \beta, a) \;\mapsto\; (a, p, \beta).
$$

### Continuation value (inter-stage connector)

$$
\mathrm{v}^{\text{cons}}_\succ(a, p, \beta)
= \mathrm{v}^{\text{shock}}_\prec(a, p, \beta).
$$

The consumption stage's continuation is wired directly to the
shock-resolution stage's arrival.

---

## 4. Shock-Resolution Stage

This stage has **no decision**. All four shocks resolve; income
components are computed; next-period cash-on-hand $x'$ is formed. It is
a pure "twister" stage: draw forward, integrate backward.

### Perch table

| Perch | State vector | Value function |
|---|---|---|
| Arrival $[\prec]$ | $(a,\, p,\, \beta)$ | $\mathrm{v}^{\text{shock}}_\prec(a, p, \beta)$ |
| Decision | $(a,\, p',\, \beta',\, \nu',\, \eta')$ | $\mathrm{v}^{\text{shock}}(a, p', \beta', \nu', \eta')$ |
| Continuation $[\succ]$ | $(x',\, p',\, \beta')$ | $\mathrm{v}^{\text{shock}}_\succ(x', p', \beta')$ |

### Arrival → Decision transition (stochastic)

Four shocks resolve simultaneously, conditional on persistent states:

$$
\begin{aligned}
p'      &\sim \Gamma_p(\cdot \mid p), \\
\beta'  &\sim \Gamma_\beta(\cdot \mid \beta), \\
\nu'    &\sim \Gamma_\nu(\cdot), \\
\eta'   &\sim \mathcal{N}(0,1).
\end{aligned}
$$

After realisation, the full vector $(a, p', \beta', \nu', \eta')$ is
known at the decision perch. The **backward mover** (arrival from
decision) is pure expectation:

$$
\mathrm{v}^{\text{shock}}_\prec(a, p, \beta)
= \mathbb{E}\!\left[
    \mathrm{v}^{\text{shock}}(a, p', \beta', \nu', \eta')
    \;\middle|\; p, \beta
  \right].
$$

### Decision perch: no optimisation

No control is chosen. The decision perch evaluates the deterministic map
to continuation:

$$
\mathrm{v}^{\text{shock}}(a, p', \beta', \nu', \eta')
= \mathrm{v}^{\text{shock}}_\succ(x', p', \beta')
$$

where $x'$ is computed below.

### Decision → Continuation transition (deterministic)

Given realised shocks and aggregate prices
$(w', r', T', \tau'(\cdot), \tilde{\tau}', r^{X\prime}(\cdot),
\sigma^X(\cdot))$:

$$
\begin{aligned}
y'        &= \bigl(r' + r^{X\prime}(a)\bigr)\,a
             + w'\,l(p', \nu'), \\
\tilde{y}' &= \sigma^X(a)\,\eta'\,a, \\
x'        &= a + y' - \tau'(y')
             + (1 - \tilde{\tau}')\,\tilde{y}' + T'.
\end{aligned}
$$

The continuation state is $(x', p', \beta')$.

### Continuation value (inter-period connector)

$$
\mathrm{v}^{\text{shock}}_\succ(x', p', \beta')
= V_{t+1}(x', p', \beta')
$$

This is the arrival value of the **next period's** consumption stage.

---

## 5. Period Composition

Composing the two stages and writing the backward recursion explicitly:

$$
V_t(x, p, \beta)
= \max_{a \in [\underline{a},\, x]}
\left\{
  u(x - a)
  + \beta \cdot
    \mathbb{E}\!\left[
      V_{t+1}(x', p', \beta')
      \;\middle|\; p, \beta
    \right]
\right\}
$$

which recovers the original HKS Bellman equation exactly. The
decomposition makes explicit that:

- **Consumption stage backward mover** ($\mathbb{B}^{\text{cons}}$):
  maximisation over $a$.
- **Shock-resolution stage backward mover**
  ($\mathbb{B}^{\text{shock}}$): expectation over
  $(p', \beta', \nu', \eta')$.
- **Period operator:**
  $\mathbb{T}_t = \mathbb{B}^{\text{cons}} \circ
  \mathbb{B}^{\text{shock}}$.

---

## 6. Individual States vs. Aggregate Objects

| Category | Objects | Role in stage equations |
|---|---|---|
| **Individual states** | $x,\, p,\, \beta$ | Arguments of $V_t$; evolve stochastically |
| **Individual control** | $a$ | Chosen at consumption-stage decision perch |
| **Idiosyncratic shocks** | $p',\, \beta',\, \nu',\, \eta'$ | Resolve at shock-stage arrival → decision |
| **Aggregate prices** | $w_t,\, r_t$ | Enter $x'$ transition; from firms' FOCs |
| **Fiscal policy** | $\tau_t(\cdot),\, \tilde{\tau}_t,\, T_t$ | Enter $x'$ transition; exogenous to household |
| **Return schedules** | $r^X_t(\cdot),\, \sigma^X(\cdot)$ | Wealth-dependent; enter $y',\, \tilde{y}'$ |

---

## 7. Paper-Supported Calibration and Process Details

Extracted from HKS (2018), Sections 6.1–6.5 and Appendix A.

### Basic parameters

| Symbol | Value | Source |
|---|---|---|
| $\alpha$ | 0.36 | Capital share; $F(K,L) = K^\alpha L^{1-\alpha}$ |
| $\delta$ | 0.048 | Annual depreciation |
| $\gamma$ | 1.5 | CRRA coefficient |
| $\underline{a}$ | $-0.22$ | Borrowing limit (benchmark model) |
| $\lambda$ | 0.6 | Fraction of tax revenue redistributed as $T_t$ |
| $\chi$ | 0.075 | Probability of zero-earnings state |

### Earnings process

Labour supply in efficiency units:

$$
l_t(p_t, \nu_t) = \psi_t(p_t) \exp(\nu_t),
$$

where $\psi_t$ maps the persistent component to efficiency units via

$$
\psi_t(p) =
\begin{cases}
\exp(p) & \text{if } F_{p_t}(p) \le 0.9, \\
F^{-1}_{\text{Pareto}(\kappa_t)}\!\left(\frac{F_{p_t}(p) - 0.9}{0.1}\right) & \text{if } F_{p_t}(p) > 0.9,
\end{cases}
$$

with $F_{p_t}$ the CDF of $p_t$ and $\kappa_t$ a time-varying Pareto
shape coefficient (calibrated to top labour income shares from Piketty
& Saez 2003).

**Persistent component** $p_t$: Gaussian AR(1),

$$
p_{t+1} = \rho_P\, p_t + (1 - \rho_P)\,\mu_P
           + \sigma^P_t\, \epsilon^p_{t+1},
\quad \epsilon^p \sim N(0,1).
$$

$\rho_P$ is fixed over time; $\sigma^P_t$ is time-varying (from
Heathcote, Storesletten, and Violante 2010). The paper uses a 17-point
grid in $\psi(p)$-space with quantile-based placement emphasising the
right tail.

**Transitory component** $\nu_t$:

$$
\nu_t \sim N\bigl(0,\, (\sigma^T_t)^2\bigr),
$$

with $\sigma^T_t$ also time-varying (Heathcote et al. 2010).

### Discount factor process

Gaussian AR(1):

$$
\beta_{t+1} = \rho_\beta\, \beta_t + (1 - \rho_\beta)\,\mu_\beta
               + \sigma_\beta\, \epsilon^\beta_{t+1},
\quad \epsilon^\beta \sim N(0,1).
$$

| Parameter | Benchmark value |
|---|---|
| $\mu_\beta$ | 0.944 |
| $\rho_\beta$ | 0.992 |
| $\sigma_\beta$ | 0.0006 |

Cross-sectional standard deviation of $\beta$: 0.0050. The paper uses a
15-point Gauss-Hermite grid for $\beta$. Distributions are truncated in
the numerical implementation to ensure finite utility and a stationary
wealth distribution.

### Tax system

**Progressive income tax** $\tau_t(\cdot)$: a step-wise function with
11 brackets, calibrated from Piketty & Saez (2007) effective federal
tax rates (individual income + corporate income + estate/gift +
payroll). Thresholds match income shares; marginal rates match average
rates per bracket. Time-varying 1967–2000, constant thereafter. **Not a
parametric closed form** — it is a piecewise schedule from data.

**Flat capital gains tax** $\tilde{\tau}_t$: time-varying; average
effective capital gains tax rate from U.S. Treasury data.

**Lump-sum transfer** $T_t = \lambda \cdot \text{(aggregate tax
revenues)}$, with $\lambda = 0.6$.

### Return schedules

**Mean excess return:**

$$
r^X_t(a) = \sum_{c \in \mathcal{C}} w_c(a)\,
\bigl(\bar{r}_{c,t} + \tilde{r}^X_c(a)\bigr),
$$

where $\mathcal{C} = \{\text{risk-free, public equity, private equity,
housing}\}$. Portfolio weights $w_c(\cdot)$ and within-class
heterogeneity $\tilde{r}^X_c(\cdot)$ are fixed over time, calibrated
from Bach et al. (2015), **tabulated by wealth percentile** (Figure 7,
Table 8 in appendix). Aggregate excess returns $\bar{r}_{c,t}$ are
time-varying (10-year moving averages).

**Return volatility:**

$$
\bigl(\sigma^X(a)\bigr)^2
= \sum_{c \in \mathcal{C}} \bigl(w_c(a)\,\tilde{\sigma}^X_c(a)\bigr)^2,
$$

also tabulated by wealth percentile. Private equity volatility rescaled
by $\phi = 0.52$ in the benchmark model. Housing volatility: 0.14
across all wealth levels.

### Numerical implementation (from Appendix A)

- EGM (Carroll 2006) on cash-on-hand grid
- 100 log-spaced points for $x$ (upper bound: $10^6 \times$ average
  wealth)
- 17 quantile-based points for $p$ (in $\psi(p)$-space)
- 15 Gauss-Hermite points for $\beta$
- Gauss-Hermite quadrature for $\nu$ and $\eta$
- Cubic spline interpolation along the wealth dimension

---

## 8. Open Questions for YAML

Items that remain **unresolved** for a dolo-plus representation, even
after extracting the calibration above.

1. **Stochastic $\beta_t$ as discount factor.** In canonical DDSL,
   $\beta$ is a scalar parameter in the mover. Here it is a **Markov
   state** that multiplies the continuation value. The draft YAML
   encodes $\beta$ as a state (`b`) in the Bellman body
   ($u(c) + b \cdot V_{[\succ]}$). This is a **non-standard design
   choice** with no canonical dolo-plus precedent.

2. **Function-valued objects.** $\tau_t(\cdot)$, $r^X_t(\cdot)$,
   $\sigma^X(\cdot)$, and $\psi_t(\cdot)$ are functions, not scalars.
   The paper uses piecewise/tabulated schedules, not parametric closed
   forms. The YAML drafts mark these as `# PLACEHOLDER`. Making them
   executable requires either parametric approximations or a
   table-lookup convention not currently in the dolo-plus spec.

3. **Aggregate price treatment.** For partial equilibrium (the YAML
   draft's assumption): $w$, $r$, $T$, $\tilde{\tau}$ are fixed
   `parameters`. For transition dynamics they would be time-indexed
   `exogenous` sequences. This is a scope decision.

4. **EGM feasibility.** The paper uses EGM, but the wealth-dependent
   returns $r^X(a)$, $\sigma^X(a)$ create a non-standard envelope
   condition. The YAML drafts omit `InvEuler` / `MarginalBellman`
   sub-equations pending analysis of whether the Euler inversion is
   well-posed.

5. **Time-varying parameters.** The paper's transition experiments use
   time-varying $\sigma^P_t$, $\sigma^T_t$, $\kappa_t$,
   $\bar{r}_{c,t}$, $\tilde{\tau}_t$, $\tau_t(\cdot)$. The YAML
   drafts assume stationary (steady-state) formulation; extending to
   time-varying requires additional structure.

---

## Sources

- **Paper:** Hubmer, Krusell, and Smith (2018), Sections 4.2–4.3
  (model) and Sections 6.1–6.5 (calibration), Appendix A (numerics).
- **Notebook summary:** `Acalin_HKS.ipynb`, Cell 4.
- **Stage template:** SolvingMicroDSOPs, Sections 12–13.
- **Stage decomposition:** Matsya session
  `topics2026-improve-hks-wealth-distribution-rubyzheng`.
- **YAML drafts:** `hks_consumption.yaml`, `hks_shock_resolution.yaml`
  (in this directory).
