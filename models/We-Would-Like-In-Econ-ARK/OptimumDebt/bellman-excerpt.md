# Aiyagari–McGrattan (1998) — Household Stage

**Paper:** S. Rao Aiyagari and Ellen R. McGrattan, "The Optimum Quantity of Debt," *Journal of Monetary Economics* 42, 1998.

**Scope:** Household dynamic program only. Two variants are covered: **Model A** (inelastic labor, lump-sum taxes; §§1–9) and **Model B** (elastic labor, proportional taxes; §10 — the paper's benchmark). Prices $(r, \tilde{w})$ and fiscal policy $(\tau, \chi)$ are parameters pinned down outside this stage by general equilibrium.

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

The budget constraint determines end-of-period assets. The paper's equation (1) (Sec. II) has $(1+g)$ on the left-hand side:

$$
\tilde{c} + (1+g)\,\tilde{a}' = \tilde{m} \quad\Longleftrightarrow\quad \tilde{a}' = \frac{\tilde{m} - \tilde{c}}{1+g}
$$

with $\tilde{c} \in [0, \tilde{m}]$ (nonnegativity of both consumption and assets). Keeping the factor explicit rather than absorbing it into an effective discount factor matches the paper 1-to-1 and avoids a silent rescaling of the poststate.

Productivity passes through: $e$ at continuation equals $e$ at decision.

---

## 4. Movers

### Backward Mover $\mathbb{B}$: Continuation → Decision (Optimization)

The backward mover solves the consumption problem, taking the continuation value $\mathrm{v}_\succ(\tilde{a}', e)$ as given:

$$
\mathrm{v}(\tilde{m}, e) = \max_{\tilde{c} \in [0,\, \tilde{m}]} \left\{ \frac{\tilde{c}^{\,1-\nu}}{1-\nu} + \tilde{\beta}\;\mathrm{v}_\succ\!\left(\frac{\tilde{m} - \tilde{c}}{1+g},\; e\right) \right\}
$$

The first-order condition picks up a $(1+g)^{-1}$ factor from $\partial \tilde{a}'/\partial \tilde{c} = -1/(1+g)$:

$$
\tilde{c}^{\,-\nu} = \frac{\tilde{\beta}}{1+g}\,\mathrm{v}'_\succ(\tilde{a}',\, e).
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

**Step 2 — Inverse Euler (InvEuler).** Invert the FOC (which carries a $(1+g)^{-1}$ factor from the explicit growth-scaling of the poststate):

$$
\tilde{c}_{[\succ]}(\tilde{a}'_j, e_i) = \left(\frac{\tilde{\beta}}{1+g}\;\mathrm{v}'_\succ(\tilde{a}'_j, e_i)\right)^{-1/\nu}
$$

**Step 3 — Reverse transition (endogenous grid point).** Recover cash-on-hand from the budget $\tilde{c} + (1+g)\,\tilde{a}' = \tilde{m}$:

$$
\tilde{m}_{[\succ]}(\tilde{a}'_j, e_i) = (1+g)\,\tilde{a}'_j + \tilde{c}_{[\succ]}(\tilde{a}'_j, e_i)
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

## 10. Model B — Elastic Labor Supply, Proportional Taxes (Benchmark)

> **Scope notice.** Model B is documented in this section for completeness.
> It is **not encoded** in `dolo-plus-draft.yaml` and is **not covered** by
> `verification.md`. This ballpark item formalizes Model A only at the
> executable layer; see `index.md` and `AGENTS.md` for the scope decision.
> Encoding Model B as a second dolo-plus stage is tracked as an out-of-scope
> follow-up in `AGENTS.md` "Common next tasks."

Model B is the paper's benchmark specification. It keeps the same three-perch structure as Model A but adds leisure $l \in [0,1]$ as a second control and switches from lump-sum to proportional taxes (with a lump-sum transfer $\chi$).

### 10.1 Objective (growth-normalized)

$$
\max_{\{\tilde{c}_t,\, l_t,\, \tilde{a}_{t+1}\}} \quad
E\!\left[
  \sum_{t=0}^{\infty} \tilde{\beta}^{\,t}
  \frac{(\tilde{c}_t^{\,\eta}\, l_t^{\,1-\eta})^{1-\mu}}{1-\mu}
  \;\Big|\; \tilde{a}_0, e_0
\right]
$$

where $l_t \in [0,1]$ is leisure (so $1-l_t$ is labor supply), $\eta \in (0,1)$ is the consumption weight in the Cobb–Douglas composite, and $\mu > 0$ is the CRRA coefficient over the composite.

### 10.2 Budget constraint

$$
\tilde{c}_t + (1+g)\,\tilde{a}_{t+1}
  \le (1+\bar{r})\,\tilde{a}_t + \bar{w}\,e_t\,(1 - l_t) + \chi
$$

where $(\bar{r}, \bar{w})$ are steady-state after-tax prices (so the proportional tax wedges are absorbed into the prices faced by the household) and $\chi$ is a lump-sum transfer.

### 10.3 Constraints

$$
\tilde{c}_t \ge 0, \qquad \tilde{a}_t \ge 0, \qquad 0 \le l_t \le 1
$$

### 10.4 Added symbols (beyond Model A)

| Symbol | Role | Space / Domain | Description |
|--------|------|----------------|-------------|
| $l$ | control | $[0, 1]$ | Leisure (so $1-l$ is labor supply) |
| $\eta$ | parameter | $(0, 1)$ | Consumption weight in the Cobb–Douglas composite |
| $\mu$ | parameter | $\mathbb{R}_+$ | CRRA coefficient over the composite |
| $\bar r$ | parameter (from GE) | $\mathbb{R}$ | After-tax net interest rate |
| $\bar w$ | parameter (from GE) | $\mathbb{R}_+$ | After-tax wage (output-normalized) |
| $\chi$ | parameter (from govt budget) | $\mathbb{R}$ | Lump-sum transfer |

All symbols from Model A (§6) are carried over unchanged except that the household faces $(\bar r, \bar w)$ rather than $(r, \tilde w)$, and the tax instrument is $\chi$ rather than $\tau$.

### 10.5 Perch structure for Model B

The stage retains three perches; only the decision perch's control dimension and the transitions change.

**Arrival perch ($\prec$):** same as Model A — $(\tilde{a}, e)$ with $\mathcal{F}_\prec = \sigma(\tilde{a}, e)$.

**Decision perch ($\circ$):** state $(\tilde{m}, e)$; controls $(\tilde{c}, l)$.

| Role | Variable | Space | Description |
|------|----------|-------|-------------|
| state | $\tilde{m}$ | $\mathbb{R}_+$ | Cash-on-hand *exclusive* of labor income (see transition below) |
| state | $e$ | $\mathcal{E}$ | Productivity |
| control | $\tilde{c}$ | $\mathbb{R}_+$ | Consumption |
| control | $l$ | $[0, 1]$ | Leisure |

**Continuation perch ($\succ$):** same as Model A — $(\tilde{a}', e)$.

### 10.6 Transitions (Model B)

**Arrival → Decision** ($\mathrm{g}_{\prec\circ}$): labor income depends on the choice $l$, so the natural decomposition absorbs the non-labor income into $\tilde{m}$ and lets labor income enter at the decision perch via the budget:

$$
\tilde{m} = (1 + \bar r)\,\tilde{a} + \chi.
$$

**Decision → Continuation** ($\mathrm{g}_{\circ\succ}$): the budget (with the $(1+g)$ factor restored from §3) then determines end-of-period assets as a function of both controls:

$$
(1+g)\,\tilde{a}' = \tilde{m} + \bar w\,e\,(1-l) - \tilde{c} \quad\Longleftrightarrow\quad \tilde{a}' = \frac{\tilde{m} + \bar w\,e\,(1-l) - \tilde{c}}{1+g}.
$$

### 10.7 Movers (Model B)

**Backward mover $\mathbb{B}$:**

$$
\mathrm{v}(\tilde{m}, e) = \max_{\tilde{c}\in\mathbb{R}_+,\; l\in[0,1]}\left\{
\frac{(\tilde{c}^{\,\eta}\, l^{\,1-\eta})^{1-\mu}}{1-\mu}
+ \tilde{\beta}\;\mathrm{v}_\succ\!\left(\frac{\tilde{m} + \bar w\,e\,(1-l) - \tilde{c}}{1+g},\; e\right)
\right\}.
$$

At an interior optimum, the intratemporal FOC pins the consumption–leisure margin:

$$
\frac{\tilde{c}}{l} = \frac{\eta}{1-\eta}\,\bar w\,e.
$$

Substituting $l = \tilde{c}\,(1-\eta)/(\eta\,\bar w\, e)$ collapses the problem to a single effective control in $\tilde{c}$; the intertemporal (Inverse Euler) step then mirrors Model A's §5 with the composite marginal utility replacing $\tilde{c}^{-\nu}$.

**Forward mover $\mathbb{I}$:** identical in form to Model A (§4) with $r \mapsto \bar r$, $\tilde w \mapsto \bar w$, and $\tau \mapsto -\chi$:

$$
\mathrm{v}_\prec(\tilde{a}',\, e) = \sum_{e'\in\mathcal{E}} \pi(e'\mid e)\; \mathrm{v}\!\left((1+\bar r)\,\tilde{a}' + \chi,\; e'\right).
$$

Note the *arrival-to-decision* transition above places only $(1+\bar r)\tilde{a}+\chi$ into $\tilde{m}$ so labor income appears where the leisure control is actually chosen; this is one of two equivalent conventions.

### 10.8 EGM feasibility

EGM (§5) remains applicable via **conditional inversion**: for fixed $e$, the intratemporal FOC reduces the choice to $\tilde{c}$ alone; the standard EGM inversion (with the $(1+g)$ factor of §5) then recovers the endogenous $\tilde{m}$-grid. The composite marginal utility $u_c(\tilde{c}, l) = \eta\,(\tilde{c}^{\,\eta}\, l^{\,1-\eta})^{1-\mu}/\tilde{c}$ is invertible in $\tilde{c}$ at each $e$, so InvEuler remains closed-form.

### 10.5 Note on the paper's computational method (rejected from formal DP)

The paper enforces the inequality constraints $\tilde{a} \ge 0$ and $l \in [0,1]$ numerically with cubic **penalty terms** of the form $\zeta \cdot \min(\tilde{a}, 0)^3$ and $\zeta \cdot \min(1-l, 0)^3$ appended to the objective. This is a **solver-level device** for the finite-element method the authors use; the formal DP uses the hard constraints above. See `verification.md` for the "rejected" status of the penalty formulation in the formalization.
