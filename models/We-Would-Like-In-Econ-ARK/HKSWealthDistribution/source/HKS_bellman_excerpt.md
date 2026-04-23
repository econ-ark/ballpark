# HKS (2018) — Bellman Problem (Explicit Mathematical Excerpt)

Faithful mathematical excerpt of the household decision problem in Hubmer, Krusell, and Smith (2018), *A Comprehensive Quantitative Theory of the U.S. Wealth Distribution*. Notation follows the paper’s Section “Consumers” and the surrounding equilibrium discussion. Cross-checked against `Acalin_HKS.ipynb` (Cell 4) only as a summary check.

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
- **Idiosyncratic return shock** $\eta_t$: standard normal, i.i.d. across agents and time (independent of other shocks, conditional on the model’s timing).

The Bellman value function is written as $V_t(x_t, p_t, \beta_t)$: given cash-on-hand $x_t$, the optimal policy and continuation value depend on $(p_t, \beta_t)$ as the persistent individual states entering the problem at the decision node. Conditional on $(p_t, \beta_t)$, the expectation in the Bellman equation integrates over $(p_{t+1}, \beta_{t+1}, \nu_{t+1}, \eta_{t+1})$.

**What is aggregate or otherwise taken as given by the household**

The household takes as given sequences (or, in transition experiments, a known or perceived path) of:

- **Wage per efficiency unit** $w_t$ (from competitive firms).
- **Aggregate return component on capital** $r_t$ (marginal product of capital net of depreciation in the aggregate technology; in this model $r_t$ is not generally a function of aggregate capital alone when excess returns $r^X_t(\cdot)$ are non-trivial—capital-market clearing links the distribution of assets to $r_t$).
- **Income-tax schedule** $\tau_t(\cdot)$ mapping ordinary gross income into tax liability.
- **Flat tax on the mean-zero stochastic return component** $\tilde{\tau}_t$.
- **Uniform lump-sum transfer** $T_t$.
- **Excess-return schedules** $r^X_t(\cdot)$ and $\sigma^X(\cdot)$, treated as exogenous reduced forms of portfolio heterogeneity (taken from data in the quantitative work).

These objects are **not** arguments of $V_t$ in the paper’s Bellman equation; they enter through the laws of motion for $x_{t+1}$ and through the tax and transfer terms. In equilibrium they are jointly determined with the cross-sectional distribution of households; for the **single household’s** problem they play the role of **prices and policy variables** taken as given when solving the Bellman equation.

---

## Control variable, consumption, and borrowing constraint

**Control (choice variable).** The only endogenous choice variable in the household problem is the **end-of-period asset position** $a_{t+1}$ (the paper’s “overall level of savings” carried into $t+1$).

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

The household’s problem has the recursive form

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

The inner expectation is over $(p_{t+1}, \beta_{t+1}, \nu_{t+1}, \eta_{t+1})$ conditional on $(p_t, \beta_t)$, consistent with the paper’s statement that conditional on $(p_t, \beta_t)$ uncertainty about future persistent states and transitory shocks is integrated in the continuation value.

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

The Bellman equation above is written with choice $a_{t+1}$; the paper’s transition for income at $t+1$ uses $a_{t+1}$ in $r^X_{t+1}(a_{t+1})$, $\sigma^X(a_{t+1})$, and $\eta_{t+1}$ when defining $y_{t+1}$ and $\tilde{y}_{t+1}$.

---

## Transition laws for individual states and cash-on-hand

### Stochastic components (exogenous dynamics)

$$
\begin{aligned}
p_{t+1} &\sim \Gamma_p(\cdot \mid p_t), \\
\beta_{t+1} &\sim \Gamma_\beta(\cdot \mid \beta_t), \\
\nu_{t+1} &\sim \Gamma_\nu(\cdot) \quad \text{(i.i.d.)}, \\
\eta_{t+1} &\sim \mathcal{N}(0,1) \quad \text{(i.i.d.)}.
\end{aligned}
$$

### Income definitions at $t+1$

**Ordinary gross income** (taxed by the progressive schedule $\tau_{t+1}$):

$$
y_{t+1}
= \bigl(r_{t+1} + r^X_{t+1}(a_{t+1})\bigr)\,a_{t+1}
  + w_{t+1}\,l_{t+1}(p_{t+1}, \nu_{t+1}).
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

Fix a period $t$ at the household’s decision node.

1. **Information at the decision.** The household observes **cash-on-hand** $x_t$ and knows the persistent states **$(p_t, \beta_t)$** that index the continuation problem. Transitory labour productivity $\nu_t$ has already determined **current** labour income embedded in $x_t$ (equivalently, $x_t$ is sufficient for the static split between $c_t$ and $a_{t+1}$ given the value function).

2. **Choice.** The household chooses **$a_{t+1}$** subject to $a_{t+1} \in [\underline{a}, x_t]$, implying **$c_t = x_t - a_{t+1}$**.

3. **Resolution of uncertainty for $t{+}1$.** Draws $(p_{t+1}, \beta_{t+1}, \nu_{t+1}, \eta_{t+1})$ are realised; aggregate prices and policy objects $(w_{t+1}, r_{t+1}, T_{t+1}, \tau_{t+1}, \tilde{\tau}_{t+1})$ relevant for that period are realised according to the equilibrium concept (perfect foresight vs. myopic transition, as discussed in the paper’s equilibrium section).

4. **Next cash-on-hand.** Income components $y_{t+1}$ and $\tilde{y}_{t+1}$ are formed and **$x_{t+1}$** is determined by the recursion above.

The Bellman expectation $\mathbb{E}[\cdot \mid p_t, \beta_t]$ therefore integrates over next period’s persistent states and transitory shocks, conditional on information $(p_t, \beta_t)$ at the time of choosing $a_{t+1}$.

---

## Taxes and transfers (as in the paper’s household problem)

- **$\tau_t(y)$** — nonlinear tax on **ordinary gross income** $y_t$.
- **$\tilde{\tau}_t$** — flat tax rate on the **mean-zero** stochastic capital-income component $\tilde{y}_t$.
- **$T_t$** — uniform lump-sum transfer (in equilibrium tied to aggregate revenues; for the household it is an additive term in the $x_{t+1}$ recursion).

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

## Source materials

- **Primary:** Hubmer, Krusell, and Smith (2018), *A Comprehensive Quantitative Theory of the U.S. Wealth Distribution* — consumer problem and notation in the “Consumers” subsection (preferences, stochastic discounting, return process, recursive problem, and constraints for $x_{t+1}$, $y_{t+1}$, $\tilde{y}_{t+1}$), plus the following “Production, government, and equilibrium” discussion for objects $(w_t, r_t, T_t)$ and clearing.
- **Supporting summary:** `Acalin_HKS.ipynb`, Cell 4.
