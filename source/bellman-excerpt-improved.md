# Aiyagari–McGrattan (1998) — Model A Household Stage

**Paper:** S. Rao Aiyagari and Ellen R. McGrattan, "The Optimum Quantity of Debt," *Journal of Monetary Economics* 42, 1998.

**Scope:** Household dynamic program only (Model A: inelastic labor, lump-sum taxes). Prices $(r, \tilde{w})$ and fiscal policy $(\tau)$ are parameters pinned down outside this stage by general equilibrium.

---

## 1. Stage Overview

The household problem is a **single consumption-savings stage** with a persistent discrete Markov shock on labor productivity. Growth normalization (tilde variables) renders the problem stationary. The stage is EGM-amenable: CRRA utility with a single continuous control and a linear budget constraint.

**Effective discount factor:**

$$
\tilde{\beta} \coloneqq \beta(1+g)^{1-\nu}, \qquad \tilde{\beta} < 1 \text{ required.}
$$

**Instantaneous utility:**

$$
u(\tilde{c}) \coloneqq \frac{\tilde{c}^{\,1-\nu}}{1-\nu}
$$

---

## 2. Perch Structure and Information Sets

The stage has three perches. Each perch defines an information set — the set of variables the agent (or the modeler) can condition on at that point.

### Arrival Perch ($\prec$)

The agent enters the period knowing assets and productivity.

| Variable | Space | Description |
|----------|-------|-------------|
| $\tilde{a}$ | $\mathsf{X}_{\tilde{a}} \coloneqq \mathbb{R}_+$ | Output-normalized beginning-of-period assets |
| $e$ | $\mathcal{E} = \{e_1, \ldots, e_N\}$ | Idiosyncratic productivity (already realized) |

**Information set:** $\mathcal{F}_\prec = \sigma(\tilde{a}, e)$. Both variables are known. No decisions have been made; no new shocks resolve here.

### Decision Perch ($\circ$)

The agent observes cash-on-hand (constructed from arrival states) and chooses consumption.

| Role | Variable | Space | Description |
|------|----------|-------|-------------|
| **state** | $\tilde{m}$ | $\mathsf{X}_{\tilde{m}} \coloneqq \mathbb{R}_+$ | Cash-on-hand (market resources) |
| **state** | $e$ | $\mathcal{E}$ | Productivity (carried through, conditions continuation value) |
| **control** | $\tilde{c}$ | $\mathbb{R}_+$ | Consumption |

**Information set:** $\mathcal{F}_\circ = \sigma(\tilde{m}, e)$. Cash-on-hand is a deterministic function of arrival states, so no new uncertainty resolves, but the *representation* of the state changes.

**Why carry $e$ separately?** Cash-on-hand $\tilde{m}$ is a sufficient statistic for the *budget constraint*, but not for the *continuation value*: the conditional expectation $\mathbb{E}_{e'|e}[\cdot]$ depends on which row of $\Pi$ we are in. So $(\tilde{m}, e)$ is the minimal decision-perch state.

### Continuation Perch ($\succ$)

After the consumption decision, the agent holds end-of-period assets.

| Variable | Space | Description |
|----------|-------|-------------|
| $\tilde{a}'$ | $\mathsf{X}_{\tilde{a}} = \mathbb{R}_+$ | End-of-period assets |
| $e$ | $\mathcal{E}$ | Productivity (carried forward; conditions the Markov draw) |

**Information set:** $\mathcal{F}_\succ = \sigma(\tilde{a}', e)$. The consumption decision has been made; $\tilde{a}'$ is determined. The next-period shock $e'$ has **not** yet been drawn.

---

## 3. Transitions Between Perches

### Arrival → Decision ($\mathrm{g}_{\prec\circ}$)

Construct cash-on-hand from assets and the realized productivity shock:

$$
\tilde{m} = (1 + r)\,\tilde{a} + \tilde{w}\,e - \tau
$$

This is a deterministic, non-invertible map: many $(\tilde{a}, e)$ pairs can produce the same $\tilde{m}$, but the pair $(\tilde{m}, e)$ is recoverable given $e$.

### Decision → Continuation ($\mathrm{g}_{\circ\succ}$)

The budget constraint determines end-of-period assets:

$$
\tilde{a}' = \tilde{m} - \tilde{c}
$$

with $\tilde{c} \in [0, \tilde{m}]$ (nonnegativity of both consumption and assets).

Productivity passes through: $e$ at continuation equals $e$ at decision.

---

## 4. Movers

### Backward Mover $\mathbb{B}$: Continuation → Decision (Optimization)

The backward mover solves the consumption problem, taking the continuation value $\mathrm{v}_\succ(\tilde{a}', e)$ as given:

$$
\mathrm{v}(\tilde{m}, e) = \max_{\tilde{c} \in [0,\, \tilde{m}]} \left\{ \frac{\tilde{c}^{\,1-\nu}}{1-\nu} + \tilde{\beta}\;\mathrm{v}_\succ(\tilde{m} - \tilde{c},\; e) \right\}
$$

**Envelope condition (marginal value at decision perch):**

$$
\mathrm{v}'(\tilde{m}, e) = \tilde{c}(\tilde{m}, e)^{-\nu}
$$

### Forward Mover $\mathbb{I}$: Decision → Arrival (Expectation)

The forward mover integrates over next-period productivity using the Markov kernel $\Pi$:

$$
\mathrm{v}_\prec(\tilde{a}', e) = \sum_{e' \in \mathcal{E}} \pi(e' \mid e)\;\mathrm{v}\!\left((1+r)\,\tilde{a}' + \tilde{w}\,e' - \tau,\; e'\right)
$$

**Marginal (shadow) value at arrival:**

$$
\mathrm{v}'_\prec(\tilde{a}', e) = (1+r) \sum_{e' \in \mathcal{E}} \pi(e' \mid e)\;\mathrm{v}'\!\left((1+r)\,\tilde{a}' + \tilde{w}\,e' - \tau,\; e'\right)
$$

**Stage operator:** $\mathbb{T} = \mathbb{I} \circ \mathbb{B}$.

---

## 5. EGM Inversion Recipe

For each productivity state $e_i$ and each point $\tilde{a}'_j$ on the exogenous asset grid:

**Step 1 — Marginal continuation value.** Compute $\mathrm{v}'_\succ(\tilde{a}'_j, e_i)$ from the forward mover (ShadowBellman evaluated on the poststate grid).

**Step 2 — Inverse Euler (InvEuler).** Invert the FOC:

$$
\tilde{c}_{[\succ]}(\tilde{a}'_j, e_i) = \left(\tilde{\beta}\;\mathrm{v}'_\succ(\tilde{a}'_j, e_i)\right)^{-1/\nu}
$$

**Step 3 — Reverse transition (endogenous grid point).** Recover cash-on-hand:

$$
\tilde{m}_{[\succ]}(\tilde{a}'_j, e_i) = \tilde{a}'_j + \tilde{c}_{[\succ]}(\tilde{a}'_j, e_i)
$$

**Step 4 — Envelope condition.** Marginal value at the endogenous decision-perch point:

$$
\mathrm{v}'(\tilde{m}_{[\succ]}, e_i) = \tilde{c}_{[\succ]}^{\;-\nu}
$$

**Output:** For each $e_i$, the EGM produces an irregular grid of $(\tilde{m}, \tilde{c})$ pairs. Interpolation onto a regular $\tilde{m}$-grid yields the consumption policy and marginal value.

---

## 6. Parameters

| Symbol | Description | Role |
|--------|-------------|------|
| $\beta$ | Raw discount factor | Structural |
| $g$ | Rate of technical progress | Structural |
| $\nu$ | CRRA coefficient | Structural |
| $\tilde{\beta} = \beta(1+g)^{1-\nu}$ | Effective discount factor | Derived |
| $r$ | Net interest rate | From GE |
| $\tilde{w}$ | Output-normalized wage | From GE |
| $\tau$ | Lump-sum tax | From govt budget |
| $\Pi$ | Markov transition matrix for $e$ | Exogenous process |

---

## 7. Shock Process

Idiosyncratic productivity $e_t$ follows a finite-state Markov chain:

$$
e \in \mathcal{E} = \{e_1, \ldots, e_N\}, \qquad \pi_{ij} = \Pr(e_{t+1} = e_j \mid e_t = e_i)
$$

The shock is **pre-decision**: $e_t$ is known when the agent chooses $\tilde{c}_t$. The *transition* to $e_{t+1}$ occurs between the continuation perch of period $t$ and the arrival perch of period $t+1$.

---

## 8. Welfare Criterion (Steady State)

$$
\Omega = \iint V(\tilde{a}, e)\, dH(\tilde{a}, e)
$$

where $H(\tilde{a}, e)$ is the steady-state joint distribution of assets and productivity.

---

## 9. General Equilibrium Closure (Outside This Stage)

- **Firm FOCs:** $r = F_K(K,L) - \delta$, $\quad \tilde{w} = F_L(K,L)$
- **Government budget:** $\tau$ consistent with debt $B$ and spending $G$
- **Market clearing:** $K + B = \int \tilde{a}\, dH(\tilde{a},e)$, $\quad L = \int e\, dH(\tilde{a},e)$

---

## 10. Note on Model B (Elastic Labor)

Model B adds leisure $l \in [0,1]$ as a second control with composite utility $u(\tilde{c}, l) = (\tilde{c}^\eta l^{1-\eta})^{1-\mu}/(1-\mu)$. This does **not** change the perch structure — it remains a single stage with three perches. The structural differences are:

1. Two controls $(\tilde{c}, l)$ at the decision perch
2. Budget constraint becomes $\tilde{a}' = \tilde{m} - \bar{w}\,e\,l - \tilde{c}$
3. Intratemporal FOC pins down $\tilde{c}/l = \eta\,\bar{w}\,e/(1-\eta)$, reducing to one effective control
4. EGM remains feasible via conditional inversion
