# Bellman Excerpt (SMD-polished): Auclert, Rognlie, Souchier, and Straub (ARSS)

**Paper:** Auclert, Rognlie, Souchier, and Straub, "Exchange Rates and Monetary Policy with Heterogeneous Agents" (Working paper)

**Source:** `models/We-Would-Like-In-Econ-ARK/OpenHA/Shin_ARSS.md`

**Template:** SolvingMicroDSOPs Sections 12–13 (modular stage architecture)

## Household dynamic program

A continuum of households face uninsurable idiosyncratic productivity shocks $e$. A household with assets $a$ and productivity $e$ at time $t$ solves:

$$
V_t(a, e) = \max_{c_t, a'} u(c_t) - v(N_t) + \beta \mathbb{E}_t \left[ V_{t+1}(a', e') \right]
$$
$$
\text{s.t.} \quad c_t + a' = (1 + r_t^p) a + e \frac{W_t}{P_t} N_t, \quad a' \geq \underline{a}
$$

where the per-period utility functions are:

$$
u(c_t) = \frac{c_t^{1-\sigma}}{1-\sigma}, \quad v(N_t) = \psi \frac{N_t^{1+\varphi}}{1+\varphi}
$$

and $c_t$ is the CES consumption basket:

$$
c_t = \left[ \alpha^{1/\eta} c_F^{(\eta-1)/\eta} + (1-\alpha)^{1/\eta} c_H^{(\eta-1)/\eta} \right]^{\eta/(\eta-1)}
$$

The household splits purchases between foreign and home goods according to:

$$
c_{Ft}(a,e) = \alpha \left( \frac{P_{Ft}}{P_t} \right)^{-\eta} c_t(a,e), \quad c_{Ht}(a,e) = (1-\alpha) \left( \frac{P_{Ht}}{P_t} \right)^{-\eta} c_t(a,e)
$$

This split is mechanical given relative prices, so the household effectively chooses **total real consumption** $c_t$ and **savings** $a'$. Hours $N_t$ are set by the union and are not chosen by the household.

### Markov process for $e$

$$
\log e' = \rho_e \log e + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \sigma_\varepsilon^2)
$$

Discretized into a finite-state Markov chain with transition matrix $\Pi(e'|e)$ via Rouwenhorst.

## Stage Decomposition: ARSS Consumption-Savings

The household problem has one choice variable ($c$) together with a non-trivial shock structure (Markov productivity $e$). Following the SolvingMicroDSOPs modular architecture (Sections 4 and 9.2), we decompose a single period into **three stages**: a discounting stage, a shocks-only stage, and a shock-free consumption stage. Each stage has three perches: **arrival** ($\prec$), **decision** ($\sim$), and **continuation** ($\succ$).

Let $m$ denote real market resources (cash-on-hand):

$$
m = (1 + r^p) a + e \frac{W}{P} N
$$

and let $\psi = m - c$ denote assets after the consumption decision (end-of-period savings, before discounting).

### 3.1 The Discounting Stage (disc)

**Table 1. Discounting Stage Perches**

| Perch | Indicator | State | Value functions | Explanation |
|-------|-----------|-------|-----------------|-------------|
| Arrival | $\prec$ | $\bullet$ | $v_\prec = v_\sim$ | no shocks |
| Decision | $\sim$ | $\bullet$ | $v_\sim = \beta v_\succ$ | apply $\beta$ |
| Continuation | $\succ$ | $\bullet$ | $v_\succ$ | value at exit |

Here $\bullet$ is a generic passthrough state whose type ($\psi$-type or $m$-type) is inherited from the predecessor stage's continuation state. The discounting stage applies the discount factor $\beta$ to the continuation value. Since the ARSS model has no permanent income growth ($\Gamma = 1$), the discount factor is simply $\beta$.

### 3.2 The Shocks-only Stage

**Table 2. Shocks-only Stage Perches**

| Perch | Indicator | State | Value functions | Explanation |
|-------|-----------|-------|-----------------|-------------|
| Arrival | $\prec$ | $a$ | $v_\prec(a) = \sum_{e'} \Pi(e' \mid e) \, v_\succ(a, e')$ | pre-shock value; expectation over $e'$ |
| Decision | $\sim$ | $a$ | (none) | no choice |
| Continuation | $\succ$ | $\check{m}$ | $v_\succ$ | post-shock value |

The arrival value function takes the expectation over the Markov productivity shock: $v_\prec(a) = \sum_{e'} \Pi(e' \mid e) \, v_\succ((1 + r^p) a + e' \frac{W}{P} N, \, e')$. Once the shock $e$ is realized, the continuation state $\check{m} = (1 + r^p) a + e \frac{W}{P} N$ is fully determined (deterministic). The notation $\check{m}$ indicates that this is an $m$-type variable (market resources after shocks are realized).

This shocks-only stage is a specialization of the `portable` stage in SolvingMicroDSOPs with no portfolio optimization. The correspondence is:
- The return factor $(1 + r^p)$ plays the role of $R$ (with $\Gamma = 1$ and no risky-share choice).
- The labor income $e \frac{W}{P} N$ plays the role of the transitory shock, where the randomness comes from the Markov state $e$.
- The equilibrium objects $r^p$, $W$, $P$, $N$ are taken as given by the household — only $e$ is stochastic from the household's perspective.

### 3.3 The Shock-free Consumption Stage (cons-noshocks)

With shocks handled in the preceding stage, the consumption stage has arrival state $m$ and no shocks between arrival and decision, so $v_\prec = v_\sim$.

**Table 3. Cons-noshocks Stage Perches**

| Perch | Indicator | State | Value functions | Explanation |
|-------|-----------|-------|-----------------|-------------|
| Arrival | $\prec$ | $m$ | $v_\prec = v_\sim$ | no shocks; identity |
| Decision | $\sim$ | $m$ | $v_\sim(m) = \max_c u(c) - v(N) + v_\succ(m - c)$ | choose consumption |
| Continuation | $\succ$ | $\psi$ | $v_\succ$ | value at exit |

The household chooses $c$ to maximize $u(c) - v(N) + v_\succ(\psi)$ where $\psi = m - c$. Since $v(N)$ does not depend on $c$ (hours are set by the union), the first-order condition is $u'(c) = v'_\succ(\psi)$, i.e. $c^{-\sigma} = v'_\succ(m - c)$. This is the standard EGM-compatible form:

- InvEuler: $c_\succ(\psi) = (v'_\succ(\psi))^{-1/\sigma}$
- Endogenous grid: $m = \psi + c_\succ(\psi)$
- Envelope: $v'_\sim(m) = u'(c) = c^{-\sigma}$

The borrowing constraint $\psi \geq \underline{a}$ binds when $m$ is low. At the constraint, $c = m - \underline{a}$.

### 3.4 The Three-stage Period

The period is defined by the stage list [shocks-only, $\mathcal{C}(\check{m} \leftrightarrow m)$, cons-noshocks, disc]:

| Element | Transition | Action |
|---------|------------|--------|
| shocks-only | $a \rightarrow \check{m}$ | productivity shock $e$ realizes (no choice) |
| $\mathcal{C}(\check{m} \leftrightarrow m)$ | $\check{m} \rightarrow m$ | rename |
| cons-noshocks | $m \rightarrow \psi$ | choose $c$ |
| disc | | apply $\beta$ |

The full pipeline within a period:

$$
a \xrightarrow{\text{shocks-only}} \check{m} \xrightarrow{\text{cons-noshocks}} \psi \xrightarrow{\text{disc}} \text{exit}
$$

### 3.5 Connectors

**Within-period connectors** are specified above: $\mathcal{C}(\check{m} \leftrightarrow m)$ renames the post-shock resources to the consumption stage's arrival state.

**Between-period connector:** The period ends after the disc stage with exit state $\psi$. The next period's shocks-only stage arrives with state $a$. The between-period connector is $\mathcal{C}(\psi \leftrightarrow a)$, which is the identity $a_{t+1} = \psi_t$.

### Key Structural Notes

1. **Shock timing.** The productivity shock $e$ is realized at the arrival perch of the shocks-only stage — not between periods, and not at a separate decision point. Once $e$ is known, market resources $m$ are determined, and the consumption stage proceeds without further uncertainty.

2. **Why this ordering (shocksonly-consnoshocks).** In this ordering, the cons-noshocks stage receives a continuation value $v_\succ(\psi)$ that already has shocks integrated out by the preceding shocks-only stage. The first-order condition $u'(c) = v'_\succ(\psi)$ can be inverted directly via EGM without any inner expectation loop. In the reverse ordering, the consumption FOC would involve a continuation value with unresolved shocks, requiring numerical root-finding inside an expectation integral.

3. **EGM compatibility.** Because preferences are CRRA and the budget constraint $\psi = m - c$ is additively separable, the Endogenous Grid Method applies directly in the cons-noshocks stage.

4. **Identity wiring.** The disc stage produces exit state $\psi$, and the next period's shocks-only stage expects arrival state $a$. These snap together via the identity $a_{t+1} = \psi_t$.

### Parameters

| Symbol | Description |
|--------|-------------|
| $\beta$ | Discount factor |
| $\sigma$ | Coefficient of relative risk aversion |
| $\eta$ | Elasticity of substitution between home and foreign goods |
| $\alpha$ | Import share (home bias $= 1 - \alpha$) |
| $\varphi$ | Inverse Frisch elasticity of labor supply |
| $\psi$ | Labor disutility weight |
| $r^p$ | Real portfolio return (taken as given by household) |
| $W/P$ | Real wage (taken as given by household) |
| $N$ | Hours worked (union-set, exogenous to household) |
| $\underline{a}$ | Borrowing limit |
| $\rho_e$ | Persistence of log productivity AR(1) |
| $\sigma_\varepsilon$ | Std dev of productivity innovation |
