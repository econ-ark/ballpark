# Bellman Excerpt: Auclert, Rognlie, Souchier, and Straub (ARSS)

**Paper:** Auclert, Rognlie, Souchier, and Straub, "Exchange Rates and Monetary Policy with Heterogeneous Agents" (Working paper)

**Source:** `models/We-Would-Like-In-Econ-ARK/OpenHA/Shin_ARSS.md`

## Household dynamic program

A continuum of households face uninsurable idiosyncratic productivity shocks $e$. A household with assets $a$ and productivity $e$ at time $t$ solves:

$$
\begin{aligned}
V_t(a, e) = & \max_{c_F, c_H, a'} \; u(c_F, c_H) - v(N_t) + \beta \mathbb{E}_t\left[V_{t+1}(a', e')\right] \\
\text{s.t.} \quad & \frac{P_{Ft}}{P_t} c_F + \frac{P_{Ht}}{P_t} c_H + a' = (1 + r_t^p) a + e \frac{W_t}{P_t} N_t \\
& a' \geq \underline{a}
\end{aligned}
$$

### State variables

| Variable | Description |
|----------|-------------|
| $a$ | Real asset holdings (beginning of period) |
| $e$ | Idiosyncratic productivity level (stochastic, uninsurable) |

### Control variables

| Variable | Description |
|----------|-------------|
| $c_F$ | Consumption of foreign goods (Ford cars) |
| $c_H$ | Consumption of home goods (Brazil nuts) |
| $a'$ | End-of-period asset holdings (saving decision) |

### Shocks

| Variable | Description |
|----------|-------------|
| $e'$ | Idiosyncratic productivity shock (realized at start of next period) |

Aggregate prices ($P_{Ft}, P_{Ht}, P_t, W_t, r_t^p, N_t$) are taken as given by the household.

### Utility

Consumption utility is CRRA over a CES consumption basket:

$$
u(c_F, c_H) = \frac{c^{1-\sigma}}{1-\sigma}
$$

where the composite consumption good $c$ is:

$$
c = \left[\alpha^{1/\eta} c_F^{(\eta-1)/\eta} + (1-\alpha)^{1/\eta} c_H^{(\eta-1)/\eta}\right]^{\eta/(\eta-1)}
$$

Labor disutility (separable, taken as given by the household since hours $N_t$ are set by the union):

$$
v(N) = \psi \frac{N^{1+\varphi}}{1+\varphi}
$$

### Intratemporal optimality (demand system)

Given total expenditure, the household splits purchases:

$$
\begin{aligned}
c_{Ft}(a,e) &= \alpha\left(\frac{P_{Ft}}{P_t}\right)^{-\eta} c_t(a,e) \\
c_{Ht}(a,e) &= (1-\alpha)\left(\frac{P_{Ht}}{P_t}\right)^{-\eta} c_t(a,e)
\end{aligned}
$$

This means the household effectively chooses **total real consumption** $c$ and **savings** $a'$, with the $c_F / c_H$ split determined mechanically by relative prices.

### Budget constraint (reduced form)

Using the CPI $P_t = [\alpha P_{Ft}^{1-\eta} + (1-\alpha) P_{Ht}^{1-\eta}]^{1/(1-\eta)}$, the budget constraint reduces to:

$$
c + a' = (1 + r_t^p) a + e \frac{W_t}{P_t} N_t
$$

where $c$ is total real consumption.

### Borrowing constraint

$$
a' \geq \underline{a}
$$

### Parameters

| Symbol | Description |
|--------|-------------|
| $\beta$ | Discount factor |
| $\sigma$ | Coefficient of relative risk aversion |
| $\eta$ | Elasticity of substitution between home and foreign goods |
| $\alpha$ | Import share (home bias $= 1-\alpha$) |
| $\varphi$ | Inverse Frisch elasticity of labor supply |
| $\psi$ | Labor disutility weight |
| $\underline{a}$ | Borrowing limit |

### Key simplification

Because $N_t$ is set by the union (not chosen by the household) and the $c_F/c_H$ split follows mechanically from relative prices, the household's **effective** dynamic problem reduces to choosing **total consumption $c$ and savings $a'$**, given states $(a, e)$:

$$
V_t(a,e) = \max_{c, a'} \; \frac{c^{1-\sigma}}{1-\sigma} - v(N_t) + \beta \mathbb{E}_t[V_{t+1}(a', e')]
$$
$$
\text{s.t.} \quad c + a' = (1+r_t^p)a + e \frac{W_t}{P_t} N_t, \quad a' \geq \underline{a}
$$
