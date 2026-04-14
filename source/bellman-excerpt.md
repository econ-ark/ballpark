# Bellman Excerpt — Aiyagari & McGrattan (1998)

**Paper:** S. Rao Aiyagari and Ellen R. McGrattan, "The Optimum Quantity of Debt," *Journal of Monetary Economics* 42, 1998.

**Scope:** Household dynamic program only (prices and government policy treated as parameters for the stage). Two variants: Model A (inelastic labor) and Model B (elastic labor, benchmark).

---

## Model A — Inelastic Labor Supply, Lump-Sum Taxes

### Objective (sequence form, growth-normalized)

$$
\max_{\{\tilde{c}_t,\, \tilde{a}_{t+1}\}} \quad
E\!\left[
  Y_0^{1-\nu} \sum_{t=0}^{\infty}
  \bigl[\beta (1+g)^{1-\nu}\bigr]^t
  \frac{\tilde{c}_t^{\,1-\nu}}{1-\nu}
  \;\Big|\; \tilde{a}_0, e_0
\right]
$$

### Budget constraint

$$
\tilde{c}_t + (1+g)\,\tilde{a}_{t+1}
  \le (1+r)\,\tilde{a}_t + \tilde{w}\,e_t - \tau
$$

### Nonnegativity and borrowing constraint

$$
\tilde{c}_t \ge 0, \qquad \tilde{a}_t \ge 0, \qquad t \ge 0
$$

### State variables

| Variable | Description |
|----------|-------------|
| $\tilde{a}_t$ | Output-normalized per capita assets |
| $e_t$ | Idiosyncratic labor productivity (finite-state Markov chain with transition matrix $\Pi$) |

### Control variables

| Variable | Description |
|----------|-------------|
| $\tilde{c}_t$ | Output-normalized per capita consumption |
| $\tilde{a}_{t+1}$ | Next-period assets (equivalently, savings choice) |

### Parameters (treated as given for the household stage)

| Symbol | Description |
|--------|-------------|
| $\beta$ | Discount factor |
| $g$ | Rate of technical progress |
| $\nu$ | Relative risk aversion (CRRA coefficient) |
| $r$ | Interest rate on assets (from GE) |
| $\tilde{w}$ | Output-normalized wage (from GE) |
| $\tau$ | Lump-sum tax (from government budget) |

### Effective discount factor

$$
\tilde{\beta} \equiv \beta(1+g)^{1-\nu}
$$

The recursive (Bellman) form of the problem requires $\tilde{\beta} < 1$.

### Recursive Bellman equation (implied)

$$
V(\tilde{a}, e) = \max_{\tilde{c},\,\tilde{a}'}
\left\{
  \frac{\tilde{c}^{\,1-\nu}}{1-\nu}
  + \tilde{\beta}\; E\!\bigl[V(\tilde{a}', e') \mid e\bigr]
\right\}
$$

subject to the budget and nonnegativity constraints above.

### Shock process

$e_t$ follows a finite-state Markov chain: $e \in \mathcal{E} = \{e_1, \ldots, e_N\}$ with transition probabilities $\pi_{ij} = \Pr(e_{t+1} = e_j \mid e_t = e_i)$.

### Welfare criterion (steady state)

$$
\Omega = \iint V(a, e)\, dH(a, e)
$$

where $H(a,e)$ is the steady-state joint distribution of assets and productivity.

---

## Model B — Elastic Labor Supply, Proportional Taxes (Benchmark)

### Objective (growth-normalized, computational form from the paper)

$$
\max_{\{\tilde{c}_t,\, l_t,\, \tilde{a}_{t+1}\}} \quad
E\!\left[
  \sum_{t=0}^{\infty} \tilde{\beta}^{\,t}
  \frac{(\tilde{c}_t^{\,\eta}\, l_t^{\,1-\eta})^{1-\mu}}{1-\mu}
  \;\Big|\; \tilde{a}_0, e_0
\right]
$$

where $l_t \in [0,1]$ is leisure, $\eta \in (0,1)$ is the consumption weight, and $\mu > 0$ is CRRA over the composite.

### Budget constraint

$$
\tilde{c}_t + (1+g)\,\tilde{a}_{t+1}
  \le (1+\bar{r})\,\tilde{a}_t + \bar{w}\,e_t\,(1 - l_t) + \chi
$$

where $\bar{r}$, $\bar{w}$ are steady-state prices and $\chi$ is a lump-sum transfer.

### Constraints

$$
\tilde{c}_t \ge 0, \qquad \tilde{a}_t \ge 0, \qquad 0 \le l_t \le 1
$$

### Additional controls

| Variable | Description |
|----------|-------------|
| $l_t$ | Leisure (so $1 - l_t$ is labor supply) |

### Note on the paper's computational method

The paper uses cubic **penalty terms** ($\zeta \cdot \min(a,0)^3$ and $\zeta \cdot \min(1-l,0)^3$) to enforce the inequality constraints numerically. This is a **solver-level device**; the formal DP uses the hard constraints listed above.

---

## General Equilibrium Closure (not part of the household stage)

The household stage takes $(r, \tilde{w}, \tau, \chi)$ as parameters. In general equilibrium these are pinned down by:

- **Firm FOCs:** $r = F_K(K,L) - \delta$, $\tilde{w} = F_L(K,L)$
- **Government budget:** $\tau$ (or $\chi$) consistent with debt $B$ and spending $G$
- **Market clearing:** $K + B = \int a\, dH(a,e)$, $L = \int e\, dH(a,e)$

These conditions sit **outside** the household stage definition.
