# HKS (2018) — Bellman Problem

Faithful mathematical excerpt of the household decision problem in Hubmer, Krusell, and Smith (2018), published as *Sources of U.S. Wealth Inequality: Past, Present, and Future* (working-paper title: *A Comprehensive Quantitative Theory of the U.S. Wealth Distribution*). Notation follows the paper's Section "Consumers" and the surrounding equilibrium discussion. Cross-checked against `Acalin_HKS.ipynb` (Cell 4) only as a summary check.

---

## Preferences and lifetime objective

Time is discrete. Preferences are CRRA over consumption:

$$
u(c) = \frac{c^{1-\gamma}}{1-\gamma}, \qquad \gamma > 0.
$$

The discount factor is idiosyncratic and stochastic: $\beta_t$ is drawn from a Markov process with conditional law $\Gamma_\beta(\beta_{t+1} \mid \beta_t)$. The household chooses a consumption plan $(c_t)_{t=0}^{\infty}$ to maximise

$$
\max_{(c_t)_{t=0}^{\infty}}
\left\{
  u(c_0)
  + \mathbb{E}_0\!\left[
      \sum_{t=1}^{\infty}
      \left(\prod_{s=0}^{t-1} \beta_s\right) u(c_t)
    \right]
\right\}.
$$

Labor supply is exogenous (no intensive margin).

---

## Individual states versus aggregate prices and equilibrium objects

**What is individual (idiosyncratic) in the recursive problem**

- **Cash-on-hand** $x_t$: all resources the household can allocate in period $t$ between consumption and end-of-period assets.
- **Persistent earnings component** $p_t$: Markov with $\Pr(p_{t+1} \in \cdot \mid p_t) = \Gamma_p(\cdot \mid p_t)$.
- **Current discount factor** $\beta_t$: Markov with $\Pr(\beta_{t+1} \in \cdot \mid \beta_t) = \Gamma_\beta(\cdot \mid \beta_t)$.
- **Transitory earnings shock** $\nu_t$: drawn each period from $\Gamma_\nu$; labour supply in efficiency units is $l_t = l_t(p_t, \nu_t)$.
- **Idiosyncratic return shock** $\eta_t$: standard normal, i.i.d. across agents and time (independent of other shocks, conditional on the model's timing).

The Bellman value function is written as $V_t(x_t, p_t, \beta_t)$: given cash-on-hand $x_t$, the optimal policy and continuation value depend on $(p_t, \beta_t)$ as the persistent individual states entering the problem at the decision node. Conditional on $(p_t, \beta_t)$, the expectation in the Bellman equation integrates over $(p_{t+1}, \beta_{t+1}, \nu_{t+1}, \eta_{t+1})$.

**What is aggregate or otherwise taken as given by the household**

The household takes as given sequences (or, in transition experiments, a known or perceived path) of:

- **Wage per efficiency unit** $w_t$ (from competitive firms).
- **Aggregate return component on capital** $r_t$ (marginal product of capital net of depreciation in the aggregate technology; in this model $r_t$ is not generally a function of aggregate capital alone when excess returns $r^X_t(\cdot)$ are non-trivial — capital-market clearing links the distribution of assets to $r_t$).
- **Income-tax schedule** $\tau_t(\cdot)$ mapping ordinary gross income into tax liability.
- **Flat tax on the mean-zero stochastic return component** $\tilde{\tau}_t$.
- **Uniform lump-sum transfer** $T_t$.
- **Excess-return schedules** $r^X_t(\cdot)$ and $\sigma^X(\cdot)$, treated as exogenous reduced forms of portfolio heterogeneity (taken from data in the quantitative work).

These objects are **not** arguments of $V_t$ in the paper's Bellman equation; they enter through the laws of motion for $x_{t+1}$ and through the tax and transfer terms. In equilibrium they are jointly determined with the cross-sectional distribution of households; for the **single household's** problem they play the role of **prices and policy variables** taken as given when solving the Bellman equation.

---

## Control variable, consumption, and borrowing constraint

**Control (choice variable).** The only endogenous choice variable in the household problem is the **end-of-period asset position** $a_{t+1}$ (the paper's "overall level of savings" carried into $t+1$).

**Borrowing constraint.**

$$
a_{t+1} \ge \underline{a},
$$

where $\underline{a}$ is the exogenous borrowing limit.

**How consumption is determined.** Given cash-on-hand $x_t$ and a feasible choice $a_{t+1}$, consumption is **residual**:

$$
c_t = x_t - a_{t+1}.
$$

Feasibility requires $c_t \ge 0$, equivalently $a_{t+1} \le x_t$. Together with $a_{t+1} \ge \underline{a}$, the choice set for $a_{t+1}$ is

$$
a_{t+1} \in \bigl[\underline{a},\, x_t\bigr].
$$

**Budget / resource relationship within the period.** The within-period allocation satisfies the accounting identity

$$
c_t + a_{t+1} = x_t,
$$

with $c_t \ge 0$ and $a_{t+1}$ satisfying the borrowing constraint above. This is the static budget constraint linking the control to consumption given $x_t$.

---

## Bellman equation (recursive formulation)

The household's problem has the recursive form

$$
\begin{aligned}
V_t(x_t, p_t, \beta_t)
&= \max_{a_{t+1} \in [\underline{a},\, x_t]}
\Big\{
  u(x_t - a_{t+1})
  + \beta_t\,
    \mathbb{E}\!\left[
      V_{t+1}(x_{t+1}, p_{t+1}, \beta_{t+1})
      \;\middle|\;
      p_t,\, \beta_t
    \right]
\Big\}
\end{aligned}
$$

where $x_{t+1}$ is determined by the transition equations below given $a_{t+1}$ and the realisations of next-period shocks and aggregate objects.

The inner expectation is over $(p_{t+1}, \beta_{t+1}, \nu_{t+1}, \eta_{t+1})$ conditional on $(p_t, \beta_t)$, consistent with the paper's statement that conditional on $(p_t, \beta_t)$ uncertainty about future persistent states and transitory shocks is integrated in the continuation value.

---

## Asset returns (technology for the savings choice)

Conditional on holding assets $a_t$ through period $t$, the **gross return** on those assets is

$$
1 + r_t + r^X_t(a_t) + \sigma^X(a_t)\,\eta_t,
$$

where:

- $r_t$ is the **aggregate** component of the return (linked to the aggregate production function in equilibrium);
- $r^X_t(\cdot)$ shifts the **mean excess return** as a function of wealth (reduced form of portfolio heterogeneity);
- $\sigma^X(\cdot)$ controls the **standard deviation** of the excess return as a function of wealth;
- $\eta_t \sim \mathcal{N}(0,1)$ is the idiosyncratic return shock.

The Bellman equation above is written with choice $a_{t+1}$; the paper's transition for income at $t+1$ uses $a_{t+1}$ in $r^X_{t+1}(a_{t+1})$, $\sigma^X(a_{t+1})$, and $\eta_{t+1}$ when defining $y_{t+1}$ and $\tilde{y}_{t+1}$.

### Return schedule detail (Section 6.4)

The mean excess return is a portfolio-weighted sum over four asset classes $\mathcal{C} = \{\text{risk-free, public equity, private equity, housing}\}$:

$$
r^X_t(a) = \sum_{c \in \mathcal{C}} w_c(a)\,\bigl(\bar{r}_{c,t} + \tilde{r}^X_c(a)\bigr),
$$

where $w_c(a)$ is the portfolio weight on class $c$ at wealth level $a$, $\bar{r}_{c,t}$ is the aggregate excess return on class $c$ (time-varying; 10-year moving averages of realised returns), and $\tilde{r}^X_c(a)$ captures within-class return heterogeneity. Portfolio weights and within-class heterogeneity are fixed over time, calibrated from Bach et al. (2015) and **tabulated by wealth percentile** (Figure 7, Table 8 in the paper's appendix).

The idiosyncratic return standard deviation is

$$
\bigl(\sigma^X(a)\bigr)^2 = \sum_{c \in \mathcal{C}} \bigl(w_c(a)\,\tilde{\sigma}^X_c(a)\bigr)^2,
$$

also tabulated by wealth percentile. Private equity volatility is rescaled by $\phi = 0.52$ in the benchmark model. Housing volatility is set to 0.14 across the wealth distribution.

### Excess return schedule data (Appendix C, Table 8)

The paper provides the full tabulation across 13 wealth-percentile bins. Column headers: P0-P40, P40-P50, P50-P60, P60-P70, P70-P80, P80-P90, P90-P95, P95-P97.5, P97.5-P99, P99-P99.5, P99.5-P99.9, P99.9-P99.99, Top 0.01%.

**Fixed portfolio weights $w_c(a)$:**

| Asset class | P0-40 | P40-50 | P50-60 | P60-70 | P70-80 | P80-90 | P90-95 | P95-97.5 | P97.5-99 | P99-99.5 | P99.5-99.9 | P99.9-99.99 | Top 0.01% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Risk-free | 0.722 | 0.412 | 0.248 | 0.182 | 0.156 | 0.134 | 0.115 | 0.102 | 0.090 | 0.079 | 0.071 | 0.051 | 0.029 |
| Housing | 0.162 | 0.394 | 0.580 | 0.662 | 0.678 | 0.674 | 0.658 | 0.626 | 0.572 | 0.482 | 0.363 | 0.253 | 0.155 |
| Public equity | 0.113 | 0.189 | 0.165 | 0.147 | 0.153 | 0.170 | 0.189 | 0.207 | 0.219 | 0.232 | 0.230 | 0.185 | 0.179 |
| Private equity | 0.002 | 0.005 | 0.007 | 0.009 | 0.013 | 0.021 | 0.038 | 0.065 | 0.118 | 0.207 | 0.336 | 0.511 | 0.637 |

**Within-class return heterogeneity $\tilde{r}^X_c(a)$ (difference from aggregate return):**

| Asset class | P0-40 | P40-50 | P50-60 | P60-70 | P70-80 | P80-90 | P90-95 | P95-97.5 | P97.5-99 | P99-99.5 | P99.5-99.9 | P99.9-99.99 | Top 0.01% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Risk-free | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Housing | 0.000 | 0.000 | 0.002 | 0.004 | 0.005 | 0.007 | 0.009 | 0.010 | 0.010 | 0.011 | 0.010 | 0.010 | 0.011 |
| Public equity | 0.000 | 0.000 | 0.001 | 0.002 | 0.003 | 0.005 | 0.008 | 0.012 | 0.014 | 0.015 | 0.016 | 0.016 | 0.016 |
| Private equity | 0.000 | 0.000 | -0.019 | -0.030 | -0.054 | -0.055 | -0.049 | -0.066 | -0.064 | -0.063 | -0.063 | -0.059 | -0.060 |

**Within-class return standard deviation $\tilde{\sigma}^X_c(a)$:**

| Asset class | P0-40 | P40-50 | P50-60 | P60-70 | P70-80 | P80-90 | P90-95 | P95-97.5 | P97.5-99 | P99-99.5 | P99.5-99.9 | P99.9-99.99 | Top 0.01% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Risk-free | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Housing | 0.140 | 0.140 | 0.140 | 0.140 | 0.140 | 0.140 | 0.140 | 0.140 | 0.140 | 0.140 | 0.140 | 0.140 | 0.140 |
| Public equity | 0.035 | 0.035 | 0.031 | 0.031 | 0.031 | 0.031 | 0.032 | 0.033 | 0.035 | 0.038 | 0.042 | 0.046 | 0.053 |
| Private equity | 0.664 | 0.664 | 0.621 | 0.595 | 0.544 | 0.525 | 0.518 | 0.480 | 0.474 | 0.470 | 0.474 | 0.492 | 0.443 |
| Private equity (rescaled, $\phi=0.52$) | 0.345 | 0.345 | 0.323 | 0.309 | 0.283 | 0.273 | 0.269 | 0.249 | 0.246 | 0.245 | 0.246 | 0.256 | 0.230 |

**Resulting 1967 steady-state excess return schedule:**

| | P0-40 | P40-50 | P50-60 | P60-70 | P70-80 | P80-90 | P90-95 | P95-97.5 | P97.5-99 | P99-99.5 | P99.5-99.9 | P99.9-99.99 | Top 0.01% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mean excess return | 0.000 | 0.011 | 0.017 | 0.020 | 0.022 | 0.026 | 0.031 | 0.035 | 0.041 | 0.050 | 0.062 | 0.079 | 0.091 |
| Std dev | 0.023 | 0.056 | 0.081 | 0.093 | 0.095 | 0.095 | 0.094 | 0.093 | 0.098 | 0.119 | 0.167 | 0.254 | 0.283 |
| Std dev (priv. eq. rescaled) | 0.023 | 0.056 | 0.081 | 0.093 | 0.095 | 0.095 | 0.093 | 0.089 | 0.086 | 0.085 | 0.098 | 0.136 | 0.149 |

---

## Transition laws for individual states and cash-on-hand

### Stochastic components (exogenous dynamics)

**Persistent earnings component** $p_t$: Gaussian AR(1) (Section 6.2),

$$
p_{t+1} = \rho_P\, p_t + (1 - \rho_P)\,\mu_P + \sigma^P_t\,\epsilon^p_{t+1},
\qquad \epsilon^p_{t+1} \sim N(0,1).
$$

$\rho_P$ is fixed over time; $\sigma^P_t$ is time-varying (estimated by Heathcote, Storesletten, and Violante 2010). The paper does not report $\rho_P$ as a number; it references HSV (2010) directly. Figure 4 (left panel) shows the cross-sectional standard deviation of $p$ rising from roughly 0.35 in 1967 to about 0.55 by 2000, but innovation standard deviations $\sigma^P_t$ are not tabulated. Time-varying variances are held constant after 2000.

**Discount factor** $\beta_t$: Gaussian AR(1) (Section 6.5),

$$
\beta_{t+1} = \rho_\beta\, \beta_t + (1 - \rho_\beta)\,\mu_\beta + \sigma_\beta\,\epsilon^\beta_{t+1},
\qquad \epsilon^\beta_{t+1} \sim N(0,1).
$$

Benchmark calibration: $\mu_\beta = 0.944$, $\rho_\beta = 0.992$, $\sigma_\beta = 0.0006$.

**Transitory earnings shock** $\nu_t$ (Section 6.2):

$$
\nu_t \sim N\!\bigl(0,\, (\sigma^T_t)^2\bigr) \quad \text{(i.i.d.)},
$$

with $\sigma^T_t$ time-varying (Heathcote et al. 2010). Figure 4 (left panel) shows the cross-sectional standard deviation of the transitory component rising from roughly 0.25 in 1967 to about 0.40 by 2000. Innovation standard deviations are not tabulated; held constant after 2000.

**Idiosyncratic return shock:**

$$
\eta_{t+1} \sim \mathcal{N}(0,1) \quad \text{(i.i.d.)}.
$$

### Labour supply function (Section 6.2)

Labour supply in efficiency units is

$$
l_t(p_t, \nu_t) = \psi_t(p_t)\,\exp(\nu_t),
$$

where $\psi_t$ maps the persistent component to efficiency units:

$$
\psi_t(p) =
\begin{cases}
\exp(p) & \text{if } F_{p_t}(p) \le 0.9, \\[4pt]
F^{-1}_{\text{Pareto}(\kappa_t)}\!\!\left(\dfrac{F_{p_t}(p) - 0.9}{0.1}\right) & \text{if } F_{p_t}(p) > 0.9.
\end{cases}
$$

Here $F_{p_t}$ is the CDF of $p_t$ and $\kappa_t$ is a time-varying Pareto shape coefficient calibrated to top labour income shares (Piketty & Saez 2003). Below the 90th percentile, earnings are log-normal; above it, a Pareto tail is grafted on. Figure 4 (right panel) shows $\kappa_t$ declining from roughly 2.7 in 1967 to about 1.7 by 2011 (a thicker tail over time). Exact year-by-year values are not tabulated in the paper.

A zero-earnings state occurs with probability $\chi = 0.075$, independently of $(p_t, \nu_t)$.

### Income definitions at $t+1$

**Ordinary gross income** (taxed by the progressive schedule $\tau_{t+1}$):

$$
y_{t+1}
= \bigl(r_{t+1} + r^X_{t+1}(a_{t+1})\bigr)\,a_{t+1}
  + w_{t+1}\,\psi_{t+1}(p_{t+1})\,\exp(\nu_{t+1}).
$$

**Mean-zero stochastic return component** (subject to the flat tax $\tilde{\tau}_{t+1}$):

$$
\tilde{y}_{t+1} = \sigma^X(a_{t+1})\,\eta_{t+1}\,a_{t+1}.
$$

### Cash-on-hand next period

$$
x_{t+1}
= a_{t+1}
  + y_{t+1} - \tau_{t+1}(y_{t+1})
  + (1 - \tilde{\tau}_{t+1})\,\tilde{y}_{t+1}
  + T_{t+1}.
$$

Given $(x_t, p_t, \beta_t)$ and a choice $a_{t+1}$, the next-period individual states $(x_{t+1}, p_{t+1}, \beta_{t+1})$ are determined by: (i) the Markov transitions for $(p_{t+1}, \beta_{t+1})$; (ii) the draws $(\nu_{t+1}, \eta_{t+1})$; (iii) the cash-on-hand recursion above with $(w_{t+1}, r_{t+1}, T_{t+1}, \tau_{t+1}, \tilde{\tau}_{t+1}, r^X_{t+1}, \sigma^X)$ taken as given at $t+1$.

**Markets.** Asset markets are incomplete: the household cannot purchase full insurance against $(p_t, \nu_t, \eta_t, \beta_t)$ shocks beyond the single asset position $a_{t+1}$.

---

## Within-period timing and information structure

Fix a period $t$ at the household's decision node.

1. **Information at the decision.** The household observes **cash-on-hand** $x_t$ and knows the persistent states **$(p_t, \beta_t)$** that index the continuation problem. Transitory labour productivity $\nu_t$ has already determined **current** labour income embedded in $x_t$ (equivalently, $x_t$ is sufficient for the static split between $c_t$ and $a_{t+1}$ given the value function).

2. **Choice.** The household chooses **$a_{t+1}$** subject to $a_{t+1} \in [\underline{a}, x_t]$, implying **$c_t = x_t - a_{t+1}$**.

3. **Resolution of uncertainty for $t{+}1$.** Draws $(p_{t+1}, \beta_{t+1}, \nu_{t+1}, \eta_{t+1})$ are realised; aggregate prices and policy objects $(w_{t+1}, r_{t+1}, T_{t+1}, \tau_{t+1}, \tilde{\tau}_{t+1})$ relevant for that period are realised according to the equilibrium concept (perfect foresight vs. myopic transition, as discussed in the paper's equilibrium section).

4. **Next cash-on-hand.** Income components $y_{t+1}$ and $\tilde{y}_{t+1}$ are formed and **$x_{t+1}$** is determined by the recursion above.

The Bellman expectation $\mathbb{E}[\cdot \mid p_t, \beta_t]$ therefore integrates over next period's persistent states and transitory shocks, conditional on information $(p_t, \beta_t)$ at the time of choosing $a_{t+1}$.

---

## Taxes and transfers (Section 6.3)

- **$\tau_t(y)$** — nonlinear **progressive income tax** on ordinary
  gross income $y_t$. In the paper this is a **step-wise function with
  11 brackets**, calibrated year-by-year from Piketty & Saez (2007)
  effective federal tax rates (individual income + corporate income +
  estate/gift + payroll). Bracket thresholds match income shares;
  marginal rates match average rates per bracket. Time-varying
  1967-2000, held constant thereafter. **Not a parametric closed form.**

- **$\tilde{\tau}_t$** — flat tax rate on the **mean-zero** stochastic
  capital-income component $\tilde{y}_t$. Time-varying; set to the
  average effective capital gains tax rate (U.S. Treasury data).

- **$T_t$** — uniform lump-sum transfer equal to a fraction
  $\lambda = 0.6$ of aggregate tax revenues.

---

## Production side (aggregate, brief)

Firms are competitive with aggregate CRS technology $F(K_t, L)$ and $L$ normalised to one. Factor prices satisfy

$$
w_t = \frac{\partial F(K_t, 1)}{\partial L},
\qquad
r_t = \frac{\partial F(K_t, 1)}{\partial K} - \delta,
\qquad \delta \in (0,1).
$$

In equilibrium, $K_t$ equals the aggregate of individual asset holdings; with wealth-dependent $r^X_t(\cdot)$, the scalar $r_t$ that clears the capital market need not be a simple function of $K_t$ alone.

---

## Calibration (Sections 6.1-6.5)

| Parameter | Value | Source / Notes |
|---|---|---|
| $\gamma$ | 1.5 | CRRA coefficient |
| $\alpha$ | 0.36 | Capital share in CRS production $F(K,L) = K^\alpha L^{1-\alpha}$ |
| $\delta$ | 0.048 | Annual depreciation rate |
| $\underline{a}$ | $-0.22$ | Exogenous borrowing limit (fraction of average annual income) |
| $\chi$ | 0.075 | Probability of zero-earnings state |
| $\lambda$ | 0.6 | Fraction of tax revenue returned as lump-sum transfer |
| $\phi$ | 0.52 | Private equity volatility rescaling factor |
| $\rho_P$ | (from HSV 2010) | Persistence of persistent earnings AR(1); time-invariant |
| $\sigma^P_t$ | (from HSV 2010) | Innovation std dev of persistent earnings; time-varying |
| $\sigma^T_t$ | (from HSV 2010) | Std dev of transitory earnings shock; time-varying |
| $\kappa_t$ | (from PS 2003) | Pareto tail shape for top earnings; time-varying |
| $\mu_\beta$ | 0.944 | Unconditional mean of discount factor |
| $\rho_\beta$ | 0.992 | Persistence of discount factor AR(1) |
| $\sigma_\beta$ | 0.0006 | Innovation std dev of discount factor |
| $w_c(a)$ | (tabulated) | Portfolio weights by asset class and wealth percentile |
| $\bar{r}_{c,t}$ | (tabulated) | Aggregate excess returns by asset class; 10-yr moving avg |
| $\tilde{r}^X_c(a)$ | (tabulated) | Within-class return heterogeneity by wealth percentile |
| $\tilde{\sigma}^X_c(a)$ | (tabulated) | Within-class return volatility by wealth percentile |
| $\tau_t(\cdot)$ | (11-bracket step function) | Progressive tax; year-by-year from PS 2007 |
| $\tilde{\tau}_t$ | (time-varying) | Flat capital gains tax; U.S. Treasury data |

"HSV 2010" = Heathcote, Storesletten, and Violante (2010). "PS 2003/2007" = Piketty and Saez.

---

## Numerical implementation (Appendix A)

The paper solves the household problem via **value-function iteration** using the **endogenous grid-point method** (EGM, Carroll 2006) on grids for cash-on-hand and persistent shocks.

| Object | Grid / Method | Details |
|---|---|---|
| Cash-on-hand $x$ | 100-point log-spaced grid | Upper bound = $10^6 \times$ average wealth |
| End-of-period assets $a$ | 100-point grid (EGM) | Finer 1000-point grid for inverse savings function |
| Persistent earnings $p$ | 17-point grid | At quantiles 0.0001, 0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.925, 0.95, 0.975, 0.99, 0.999, ..., 0.99999999 of cross-sectional $p$-distribution |
| Discount factor $\beta$ | 15-point Gauss-Hermite | Quadrature points of unconditional $\beta$-distribution |
| Integration over $p'\mid p$ | 10-point Gauss-Hermite | Linear interpolation in $\psi(p)$-space |
| Integration over $\beta'\mid\beta$ | Gauss-Hermite | Linear interpolation in $\beta$-space |
| Integration over $\nu$, $\eta$ | Gauss-Hermite | Both are normal i.i.d. shocks |
| Value function interpolation | Cubic splines | Along the wealth dimension |

---

## Information still external to this paper

The following objects are referenced by the paper but their numerical values come from external sources and are **not tabulated** in HKS (2018) itself:

1. **$\rho_P$, $\sigma^P_t$, $\sigma^T_t$** (earnings process parameters) — from Heathcote, Storesletten, and Violante (2010). Cross-sectional dispersions are shown in Figure 4 but innovation standard deviations and $\rho_P$ are not reported as numbers.
2. **$\kappa_t$** (Pareto tail shape for top earnings) — calibrated to match Piketty & Saez (2003) top wage shares; Figure 4 (right panel) shows the time path but no year-by-year table is provided.
3. **11-bracket tax schedule** $\tau_t(\cdot)$ — effective federal tax rates from Piketty & Saez (2007), translated into step-wise thresholds and marginal rates. The method is described in Section 6.3 but the actual bracket values are not in the paper.
4. **$\tilde{\tau}_t$** (flat capital gains tax rate time series) — from U.S. Department of the Treasury (2016); not reproduced in the paper.
5. **Aggregate excess returns** $\bar{r}_{c,t}$ — Figure 8 shows 10-year moving averages of excess returns for housing, public equity, and private equity over 1967-2017, but the underlying numbers are not tabulated.

---

## Source materials

- **Primary:** Hubmer, Krusell, and Smith (2018), *Sources of U.S. Wealth Inequality: Past, Present, and Future* (working-paper title: *A Comprehensive Quantitative Theory of the U.S. Wealth Distribution*) — Sections 4.2-4.3 (consumer problem, production, equilibrium), Sections 6.1-6.5 (calibration of all processes and schedules), Appendix A (numerical implementation), and Appendix C / Table 8 (excess return schedule data).
- **Supporting summary:** `Acalin_HKS.ipynb`, Cell 4.
- **External data sources referenced by the paper:** Heathcote, Storesletten, and Violante (2010) for earnings process parameters; Piketty and Saez (2003, 2007) for top earnings shares and effective tax rates; Bach et al. (2015) for portfolio weights and return heterogeneity; U.S. Department of the Treasury (2016) for capital gains tax rates; Kartashova (2014) for private equity premium; Jorda et al. (2017) for housing returns.
