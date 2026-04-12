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

### Stage Composition

The household problem is a **single-stage period**. One consumption-savings stage handles both the Markov shock realisation (at the arrival-to-decision transition) and the consumption-saving optimisation (at the decision perch). The continuation perch of period $t$ connects to the arrival perch of period $t+1$ via **identity wiring**: the outgoing state $(a', e)$ matches the incoming state $(a, e)$ of the successor period.

$$
\underbrace{\text{Arrival} \xrightarrow{g_{\prec\circ}} \text{Decision} \xrightarrow{g_{\circ\succ}} \text{Continuation}}_{\text{single stage } \mathbb{S}} = \text{Period } \mathbb{T}
$$

The **backward** (Bellman) pass composes two movers:

$$
\mathbb{T} = \mathbb{I} \circ \mathbb{B}
$$

| Operator | Direction | Role |
|----------|-----------|------|
| $\mathbb{B}$: cntn to dcsn | backward | Optimise: $v(m, e) = \max_c \{ u(c) + \beta \, v_{\succ}(m - c, e) \}$ |
| $\mathbb{I}$: dcsn to arvl | backward | Integrate: $v_{\prec}(a, e) = \mathbb{E}_{e' | e} [ v((1+r)a + e'wN, e') ]$ |

### Perch Table

| Perch | Indicator | State vector | Objects | Key transition |
|-------|-----------|-------------|---------|----------------|
| **Arrival** | $\prec$ | $(a, e)$ | $v_{\prec}(a,e)$, $v'_{\prec}(a,e)$ | Entry point; receives identity wiring from previous period's continuation |
| | | | | $g_{\prec\circ}$: $m = (1+r)a + ewN$ |
| **Decision** | $\circ$ | $(m, e)$ | $v(m,e)$, $v'(m,e)$, control $c \in [0, m - \underline{a}]$ | $v(m,e) = \max_c \{ u(c) + \beta \, v_{\succ}(m - c, e) \}$ |
| | | | | $g_{\circ\succ}$: $a' = m - c$, $a' \geq \underline{a}$ |
| **Continuation** | $\succ$ | $(a', e)$ | $v_{\succ}(a',e)$, $v'_{\succ}(a',e)$ | $v_{\succ}(a',e) = \mathbb{E}_{e' | e} [ v_{\prec}^{+}(a', e') ]$ |

where $v_{\prec}^{+}$ denotes the **next-period** arrival value.

### Key Structural Notes

1. **Shock timing.** The exogenous state $e$ follows a Markov process. The expectation over $e'|e$ sits in the dcsn-to-arvl mover $\mathbb{I}$ (pre-decision shock pattern). At the decision perch, $e$ is known and the agent conditions on it.

2. **EGM compatibility.** Because preferences are CRRA and the budget constraint $a' = m - c$ is additively separable, the Endogenous Grid Method applies:
   - InvEuler: $c_{[\succ]} = (\beta \, v'_{\succ}(a', e))^{-1/\sigma}$
   - Reverse transition: $m_{[\succ]} = a' + c_{[\succ]}$
   - Envelope: $v'(m,e) = u'(c) = c^{-\sigma}$

3. **Borrowing constraint.** The constraint $a' \geq \underline{a}$ binds when $m$ is low. At the constraint, $c = m - \underline{a}$ and the marginal value $v'(m,e) = (m - \underline{a})^{-\sigma}$ exceeds the unconstrained envelope, producing the kink that EGM must handle.

4. **Identity wiring.** The consumption stage produces continuation variable $a'$ and the next stage expects an arrival variable also called $a$. The two periods snap together: $(a', e)_{\succ} \mapsto (a, e)_{\prec}^{+}$.

### Parameters

| Symbol | Description |
|--------|-------------|
| $\beta$ | Discount factor |
| $\sigma$ | Coefficient of relative risk aversion |
| $\eta$ | Elasticity of substitution between home and foreign goods |
| $\alpha$ | Import share (home bias $= 1 - \alpha$) |
| $\varphi$ | Inverse Frisch elasticity of labor supply |
| $\psi$ | Labor disutility weight |
| $r$ | Real interest rate (taken as given by household) |
| $w$ | Real wage (taken as given by household) |
| $N$ | Hours worked (union-set, exogenous to household) |
| $\underline{a}$ | Borrowing limit |
| $\rho_e$ | Persistence of log productivity AR(1) |
| $\sigma_\varepsilon$ | Std dev of productivity innovation |
