# Bellman Excerpt: Auclert, Rognlie, Souchier, and Straub (ARSS)

**Paper.** Auclert, A., Rognlie, M., Souchier, M., and Straub, L. (2024), "Exchange Rates and Monetary Policy with Heterogeneous Agents: Sizing up the Real Income Channel," NBER Working Paper 28872 (also SSRN 3856853).

**Source.** The August 2024 revision of the working paper, retrieved from the author's Stanford website at <https://web.stanford.edu/~aauclert/ha_oe.pdf>. Paper equations are referenced below with the same numbering as the PDF (e.g. "paper eq. (1)").

**Purpose.** This document gives a self-contained modular-DDSL statement of the full model — household problem, aggregate block, monetary policy, market clearing, intertemporal MPC apparatus, and the main analytical shock-response results — sufficient for Matsya (or an equivalent formalizer) to produce a Dolo Plus description covering each block. The SolvingMicroDSOPs-style perch decomposition of the household problem (section 8 below) is the authoritative stage structure for the incomplete-markets household block.

**Scope.** The document covers the **benchmark (Sections 2–4) model** of the paper: baseline heterogeneous-agent New Keynesian small-open-economy model with flexible prices, sticky wages, perfect exchange-rate pass-through, constant-real-rate monetary rule, and static CES demand. Extensions developed in Section 5 of the paper (delayed substitution, sticky domestic and import prices, non-homothetic preferences, unequal incidence, inertial Taylor rule) are summarised in section 9.5 below but are **not** included in the baseline stage decomposition.

**Scope of the companion YAML — household block only.** The companion `dolo-plus-draft.yaml` in this directory **encodes the household block only** (the three-stage period of section 8 below: `shocks` → `cons` → `disc`). The aggregate / general-equilibrium closure (CPI, real exchange rate, real UIP, RoW demand, sticky-wages Phillips curve, monetary rule, NFA, current account) is fully specified equation-by-equation in sections 3–4 below and consolidated as a 16-equation system in section 7, but is **deliberately not encoded in YAML in this PR** — see [Open items](#13-open-items-canonical-scope-record) for the rationale and the explicit plan for a follow-up `aggregate-draft.yaml`. CONTRIBUTING.md's "Formalized" tier explicitly allows a one-stage / one-block YAML, so the household-only YAML is sufficient for promotion. The `index.md` / `OpenHA.md` frontmatter and `AGENTS.md` "Formalization status" section both record the same scope choice, and this `bellman-excerpt.md` "Open items" section (§13) is the **canonical** record of that scope decision.

---

## 1. Symbols and notation

**Convention.** Lowercase letters denote individual-household objects; uppercase letters denote aggregates. Time subscripts $t$ are omitted where context makes them unambiguous. A superscript $\ast$ marks rest-of-world variables.

### 1.1 Household-level variables

| Symbol | Role | Definition / domain |
|---|---|---|
| $a_{it}^p$ | state | beginning-of-period real asset position, *including* returns (see paper eq. (8)) |
| $a_{it}'$ | control (reduced form) | end-of-period real asset position; $a_{i,t+1}^p = (1+r_t)\,a_{it}'$ |
| $s_{it}, B_{it}^H, B_{it}^F$ | disaggregated asset positions | stock, domestic nominal bond, foreign nominal bond; under no-arbitrage (paper eq. (5)) the portfolio split is indeterminate and only $a^p$ matters for consumption-savings |
| $c_{it}$ | control | real consumption (CES basket of $c_H$ and $c_F$) |
| $c_{Ft}, c_{Ht}$ | derived | CES expenditure shares; determined mechanically by $c_{it}$ and relative prices (paper eqs. (10)–(11)) |
| $e_{it}$ | exogenous state | idiosyncratic productivity; first-order Markov chain, $\mathbb{E}\,e_{it}=1$ |
| $n_{it}$ | **not chosen** | individual hours; set by the union, with $n_{it}=N_t$ for all $i$ |
| $V_t$ | value function | lifetime utility, written as $V_t(a^p,e)$ in reduced form (paper eq. (9)) |

### 1.2 Aggregate domestic variables

| Symbol | Role | Definition |
|---|---|---|
| $C_t$ | aggregate consumption | $C_t\equiv \int c_t(a^p,e)\,\mathrm{d}\mathcal{D}_t(a^p,e)$ |
| $C_{Ht}, C_{Ft}$ | aggregate home/foreign-goods demand | CES aggregates |
| $Y_t$ | aggregate output | domestic production |
| $N_t$ | aggregate labour | $Y_t=N_t$ (paper eq. (13)) |
| $A_t$ | aggregate real assets | $A_t\equiv \int a_t(a^p,e)\,\mathrm{d}\mathcal{D}_t(a^p,e)$ |
| $p_t$ | real stock price | real price of the representative share |
| $d_t$ | real dividend | paper eq. (15) |
| $\mathrm{nfa}_t$ | net foreign assets | $\mathrm{nfa}_t\equiv A_t - p_t$ (paper eq. (22)) |
| $\mathrm{NX}_t$ | real net exports | $\mathrm{NX}_t\equiv \tfrac{P_{Ht}}{P_t}Y_t - C_t$ |
| $\mathcal{D}_t$ | distribution | joint measure over $(a^p,e)$ |

### 1.3 Prices, rates, exchange rate

| Symbol | Role | Definition |
|---|---|---|
| $P_t$ | domestic CPI | paper eq. (4) |
| $P_{Ht}, P_{Ft}$ | prices of home and foreign goods in domestic currency | — |
| $\mathcal{E}_t$ | nominal exchange rate | price of foreign currency in domestic currency; increase = nominal depreciation |
| $Q_t$ | real exchange rate | $Q_t\equiv \mathcal{E}_t P_t^{\ast}/P_t$ (paper eq. (6)); increase = real depreciation |
| $\iota_t, \iota_t^{\ast}$ | nominal interest rates | domestic / foreign |
| $r_t, r_t^{\ast}$ | ex-ante real interest rates | $1+r_t\equiv (1+\iota_t)\,P_t/P_{t+1}$, analogously for foreign |
| $W_t$ | nominal wage | — |
| $\pi_t, \pi_t^w, \pi_{Ht}$ | inflation rates | CPI, wages, producer prices |
| $D_t, d_t$ | nominal/real dividend | $d_t\equiv D_t/P_t$ |

### 1.4 Rest-of-world variables

| Symbol | Role | Definition |
|---|---|---|
| $C^{\ast}$ | RoW consumption | constant under paper's assumption $P_t^{\ast}=1,\,C_t^{\ast}=C^{\ast}$ |
| $P^{\ast}_t$ | RoW CPI | normalized to 1 under paper's foreign monetary policy assumption |
| $P^{\ast}_{Ht}$ | foreign-currency price of home goods abroad | $P^{\ast}_{Ht}=P_{Ht}/\mathcal{E}_t$ under law of one price (paper eq. (17)) |
| $C^{\ast}_{Ht}$ | foreign demand for home goods | paper eq. (12) |
| $\mathcal{B}_t$ | foreign preference shifter | discount-factor shock that acts as primitive for $\iota_t^{\ast}$ shocks |

### 1.5 Structural parameters

| Symbol | Role | Value in benchmark calibration | Meaning |
|---|---|---|---|
| $\sigma$ | preferences | $1$ | inverse elasticity of intertemporal substitution |
| $\varphi$ | preferences | $2$ | inverse Frisch elasticity of labor supply |
| $\psi$ | preferences | normalized | labor-disutility weight |
| $\beta$ | preferences | $0.965$ | household discount factor (calibrated to clear asset market) |
| $\beta^{\ast}$ | preferences | $0.990$ | RoW discount factor; pins down steady-state $r_{ss}$ |
| $\alpha$ | openness | $0.40$ | import share / openness (home bias = $1-\alpha$) |
| $\eta$ | demand | varies | elasticity of substitution for domestic households between home and foreign goods |
| $\gamma$ | demand | varies | elasticity of substitution for RoW between home and foreign goods |
| $\chi$ | demand | $\chi\equiv \eta(1-\alpha)+\gamma$ | **trade elasticity** (paper eq. (36)) |
| $\rho_e$ | income process | $0.912$ | persistence of log productivity AR(1) |
| $\sigma_e$ | income process | $0.883$ | cross-sectional std. dev. of log income |
| $\underline{a}$ | constraint | $0$ | borrowing limit on end-of-period net assets |
| $\mu$ | production | $1.043$ | gross markup (price over nominal marginal cost) |
| $\epsilon$ | production | — | elasticity across home-good varieties; $\mu\equiv\epsilon/(\epsilon-1)$ |
| $\theta_w$ | wage setting | $0.938$ | Calvo probability of no wage adjustment |
| $\kappa_w$ | wage setting | — | wage Phillips-curve slope; $\kappa_w=(1-\beta\theta_w)(1-\theta_w)/\theta_w$ |
| $\mu_w$ | wage setting | — | wage markup (static under the union objective used) |
| $r_{ss}$ | monetary | — | steady-state real interest rate; $1+r_{ss}=1/\beta^{\ast}$ |
| $\epsilon_t$ | monetary | — | domestic monetary policy shock |

### 1.6 Aggregate objects introduced in Sections 2.3 onward (iMPC apparatus)

| Symbol | Role | Definition |
|---|---|---|
| $\mathcal{C}$ | consumption functional | $C_t=\mathcal{C}_t\!\left(\{\tfrac{P_{Hs}}{P_s}Y_s\}_{s=0}^{\infty},\{r_s\}_{s=0}^{\infty}\right)$ (paper Proposition 1) |
| $\mathbf{M}$ | intertemporal MPC matrix | Fréchet derivative of $\mathcal{C}$ w.r.t. real income $\tfrac{P_{H}}{P}Y$; $M_{t,s}=\partial C_t/\partial(\tfrac{P_{Hs}}{P_s}Y_s)$ |
| $\mathbf{M}^r$ | interest-rate Jacobian | $(1+r)$ × Fréchet derivative of $\mathcal{C}$ w.r.t. $r$ |
| $d\mathbf{X}$ | vector notation | $(dX_0, dX_1, dX_2, \ldots)^{\top}$, impulse response of $X$ to an MIT shock at date 0 |

---

## 2. Household problem

### 2.1 Full dynamic program (three assets, paper eq. (1))

A household with incoming stock position $s$, domestic nominal bond position $B^H$, foreign nominal bond position $B^F$, and productivity $e$ at time $t$ solves

$$
\tilde V_t(s,B^H,B^F,e) \;=\; \max_{c_F,c_H,s',B^{H\prime},B^{F\prime}} \; u(c_F,c_H) - v(N_t) + \beta\,\mathbb{E}_t\!\left[\tilde V_{t+1}(s',B^{H\prime},B^{F\prime},e')\,\big|\,e\right]
$$

subject to the budget constraint

$$
P_{Ft}\,c_F + P_{Ht}\,c_H + P_t\,s' + B^{H\prime} + \mathcal{E}_t\,B^{F\prime}
\;=\; (P_t + D_t)\,s + (1+\iota_{t-1})\,B^H + (1+\iota^{\ast}_{t-1})\,\mathcal{E}_t\,B^F + e\,W_t\,N_t
$$

and the net-asset borrowing constraint

$$
P_t\,s' + B^{H\prime} + \mathcal{E}_t\,B^{F\prime} \;\ge\; 0.
$$

Preferences are

$$
u(c_F,c_H) \;=\; \frac{c^{1-\sigma}}{1-\sigma}, \qquad v(N) \;=\; \psi\,\frac{N^{1+\varphi}}{1+\varphi},
$$

where $c$ is the CES consumption basket (paper eq. (3))

$$
c \;=\; \left[\, \alpha^{1/\eta}\,c_F^{(\eta-1)/\eta} + (1-\alpha)^{1/\eta}\,c_H^{(\eta-1)/\eta}\, \right]^{\eta/(\eta-1)},
$$

with associated consumer price index (paper eq. (4))

$$
P_t \;=\; \left[\, \alpha\,P_{Ft}^{\,1-\eta} + (1-\alpha)\,P_{Ht}^{\,1-\eta}\, \right]^{1/(1-\eta)}.
$$

### 2.2 Reduction to canonical form

Under no aggregate uncertainty, **no-arbitrage** equates nominal returns across all three assets (paper eq. (5))

$$
1+\iota_t \;=\; (1+\iota^{\ast}_t)\,\frac{\mathcal{E}_{t+1}}{\mathcal{E}_t} \;=\; \frac{P_{t+1} + D_{t+1}}{P_t},
$$

which in real terms (dividing by $P_{t+1}/P_t$) becomes (paper eq. (7))

$$
1+r_t \;=\; (1+r^{\ast}_t)\,\frac{Q_{t+1}}{Q_t} \;=\; \frac{p_{t+1} + d_{t+1}}{p_t}.
$$

The first equality is the real uncovered interest parity (UIP) condition; the second is the stock-pricing equation. Because all three assets have identical real returns, the household's portfolio split is indeterminate: only the total real asset position matters. Define real end-of-period assets and real beginning-of-period assets *including* returns (paper eq. (8))

$$
a'_t \;\equiv\; \frac{P_t\,s' + B^{H\prime} + \mathcal{E}_t\,B^{F\prime}}{P_t},
\qquad
a^p_t \;\equiv\; \frac{(P_t+D_t)\,s + (1+\iota_{t-1})\,B^H + (1+\iota^{\ast}_{t-1})\,\mathcal{E}_t\,B^F}{P_t}.
$$

Then $a^p_t=(1+r_{t-1})\,a'_{t-1}$, and the household problem (2.1) reduces to the **canonical form** (paper eq. (9)):

$$
\boxed{\quad
V_t(a^p, e) \;=\; \max_{c}\; u(c) - v(N_t) + \beta\,\mathbb{E}_t\!\left[V_{t+1}\bigl((1+r_t)\,a'\bigm.,e'\bigr)\,\big|\,e\right]
\quad}
$$

subject to

$$
a' \;=\; a^p + e\,\frac{W_t}{P_t}\,N_t - c, \qquad a' \;\ge\; \underline{a} \;=\; 0.
$$

The **single effective control** is $c$; savings $a'$ is pinned down by the budget identity. The CES home/foreign split is pinned down by paper eqs. (10)–(11),

$$
c_{Ft}(a^p,e) \;=\; \alpha\left(\frac{P_{Ft}}{P_t}\right)^{-\eta} c_t(a^p,e),
\qquad
c_{Ht}(a^p,e) \;=\; (1-\alpha)\left(\frac{P_{Ht}}{P_t}\right)^{-\eta} c_t(a^p,e),
$$

so $c_F,c_H$ are *derived quantities*, not controls at the decision perch.

### 2.3 Idiosyncratic productivity process

$e_{it}$ is a first-order Markov chain with

$$
\mathbb{E}\,e_{it} = 1, \qquad \log e_{it+1} = \rho_e\,\log e_{it} + \varepsilon_{it+1}, \quad \varepsilon_{it+1}\sim \mathcal{N}(0,\sigma_\varepsilon^{\,2}).
$$

The AR(1) is discretised (Rouwenhorst) on 7 grid points into a finite-state Markov chain with transition matrix $\Pi(e'\mid e)$. The finite-state discretisation is the object the formalization layer consumes.

### 2.4 Policy functions and the distribution

Let $c_t(a^p,e)$ and $a'_t(a^p,e)$ denote the consumption and savings policy functions that solve (2.2). Given an initial distribution $\mathcal{D}_0(a^p,e)$ over $(a^p,e)$ at $t=0$, the optimal policies induce a law of motion

$$
\mathcal{D}_{t+1}(a^{p\prime},e') \;=\; \sum_{e}\, \mathcal{D}_t\!\left(\tfrac{a^{p\prime}}{1+r_t},\,e\right)\cdot \Pi(e,e'),
$$

fully characterising the household sector.

---

## 3. Aggregate closure

### 3.1 Domestic production and price setting (paper eqs. (13)–(15))

Home goods are produced from domestic labour with constant productivity,

$$
Y_t \;=\; N_t.
$$

A continuum of monopolistically competitive firms set price at a constant markup $\mu$ over nominal marginal cost,

$$
P_{Ht} \;=\; \mu\,W_t, \qquad \mu \;=\; \frac{\epsilon}{\epsilon-1}.
$$

Real dividends equal

$$
d_t \;=\; \frac{P_{Ht}\,Y_t - W_t\,N_t}{P_t} + \frac{\mathcal{E}_t\,P^{\ast}_{Ht} - P_{Ht}}{P_t}\,C^{\ast}_{Ht}.
$$

The first term is domestic profits; the second is the exporter's unhedged currency exposure (zero under the law of one price, paper eq. (17)). Shares are in unit supply with end-of-period real price $p_t$; firms maximize shareholder value $d_t+p_t$.

### 3.2 Rest-of-world demand for home goods (paper eq. (12))

$$
C^{\ast}_{Ht} \;=\; \alpha\,\left(\frac{P^{\ast}_{Ht}}{P^{\ast}_t}\right)^{\!-\gamma}\,C^{\ast}_t.
$$

The RoW is modelled as a continuum of countries each with a CES aggregator of global goods; $\gamma$ is the RoW's elasticity of substitution between home and foreign varieties. The home country is small enough not to affect $P^{\ast}_t$.

### 3.3 Rest-of-world monetary policy (paper eq. (16))

RoW monetary policy keeps $P^{\ast}_t=P^{\ast}_{Ft}=1$ and $C^{\ast}_t=C^{\ast}$ at all dates, requiring

$$
1+\iota^{\ast}_t \;=\; 1+r^{\ast}_t \;=\; \frac{1}{\beta^{\ast}}\,\frac{\mathcal{B}_t}{\mathcal{B}_{t+1}},
$$

where $\mathcal{B}_t$ is an exogenous shifter of RoW intertemporal preferences. The $\iota^{\ast}$ and $\mathcal{B}$ sequences can be used interchangeably as primitives.

### 3.4 Law of one price and perfect pass-through (baseline) (paper eq. (17))

Imports are denominated in foreign currency with perfect exchange-rate pass-through:

$$
P_{Ft} \;=\; \mathcal{E}_t,
\qquad
P^{\ast}_{Ht} \;=\; \frac{P_{Ht}}{\mathcal{E}_t}.
$$

The baseline model therefore features nominal rigidity only in domestic currency. (Section 5 of the paper relaxes this; see section 9.5 below.)

### 3.5 Sticky wages and the wage Phillips curve (paper eq. (18))

A union employs all households for equal hours $N_t$ and sets the nominal wage $W_t$ à la Calvo, with objective aligned with the utility of an agent holding average consumption $C_t$. Denote nominal wage inflation $\pi^w_t\equiv W_t/W_{t-1}-1$. The resulting wage Phillips curve is

$$
\pi^w_t \;=\; \kappa_w\!\left(\, \frac{v'(N_t)}{\tfrac{1}{\mu_w}\,\tfrac{W_t}{P_t}\,u'(C_t)} \;-\; 1 \,\right) \;+\; \beta\,\pi^w_{t+1},
$$

with $\kappa_w=(1-\beta\theta_w)(1-\theta_w)/\theta_w$. The union sets $N_t$ to the level demanded by firms; individual hours satisfy $n_{it}=N_t$.

### 3.6 Domestic monetary policy

**Baseline (analytical) rule (paper eq. (19)).** Constant real interest rate with shock:

$$
\iota_t \;=\; r_{ss} + \pi_{t+1} + \epsilon_t
\quad \Longleftrightarrow \quad
r_t \;=\; r_{ss} + \epsilon_t.
$$

**Alternative (quantitative) rule (paper eq. (20)).** Inertial CPI Taylor rule:

$$
\iota_t \;=\; \rho_m\,\iota_{t-1} + (1-\rho_m)(r_{ss} + \phi\,\pi_{t+1}) + \epsilon_t, \quad \phi>1.
$$

The baseline results in sections 4–6 use rule (3.6a).

### 3.7 Market clearing, NFA, and current account

**Domestic-goods market clearing (paper eq. (21)):**

$$
C_{Ht} + C^{\ast}_{Ht} \;=\; Y_t.
$$

Substituting the demand aggregations (paper eq. (11)–(12)), the law of one price, and RoW monetary policy, this becomes (paper eq. (33)):

$$
Y_t \;=\; (1-\alpha)\,\left(\frac{P_{Ht}}{P_t}\right)^{\!-\eta}\,C_t \;+\; \alpha\,\left(\frac{P_{Ht}}{\mathcal{E}_t}\right)^{\!-\gamma}\,C^{\ast}.
$$

**Net foreign assets and current account (paper eqs. (22)–(23)):**

$$
\mathrm{nfa}_t \;\equiv\; A_t - p_t,
\qquad
\mathrm{nfa}_t - \mathrm{nfa}_{t-1} \;=\; \underbrace{\frac{P_{Ht}}{P_t}Y_t - C_t}_{\mathrm{NX}_t} \;+\; r_{t-1}\,\mathrm{nfa}_{t-1}, \quad t\ge 1.
$$

Domestic bonds are in zero net supply; the government does not spend, tax, or transfer. The steady-state NFA is zero.

### 3.8 Real-income derived relations (paper eqs. (28)–(29))

Combining (3.1) and the production function,

$$
\frac{W_t}{P_t}\,N_t \;=\; \frac{1}{\mu}\,\frac{P_{Ht}}{P_t}\,Y_t,
\qquad
d_t \;=\; \left(1-\frac{1}{\mu}\right)\,\frac{P_{Ht}}{P_t}\,Y_t.
$$

Real wage income and real dividends are therefore both fixed fractions of aggregate real income $\tfrac{P_{Ht}}{P_t}Y_t$. This is the single macro quantity that closes the household problem into the aggregate block.

### 3.9 Closed-form exchange-rate determination (paper eq. (30))

Iterating the real UIP (3.2) with the long-run restriction $Q_\infty = Q_{ss}=1$:

$$
Q_t \;=\; \mathcal{B}_t \cdot \prod_{s\ge t}\frac{1+r_{ss}}{1+r_s}.
$$

Under the constant-real-rate rule (3.6a) with $r_t=r_{ss}$, this simplifies to $Q_t=\mathcal{B}_t$, which makes $Q_t$ effectively exogenous for the purposes of the analysis in Section 4.

---

## 4. Equilibrium and steady state

### 4.1 Equilibrium definition

Given sequences $\{\mathcal{B}_t\}$ (or equivalently $\{\iota^{\ast}_t\}$) and monetary shocks $\{\epsilon_t\}$, and an initial wealth distribution $\mathrm{d}\tilde{\mathcal{D}}_{i0}(s,B^H,B^F,e)$, a competitive equilibrium is a collection of

- household policies $\{c_{Hit}, c_{Fit}, c_{it}, a_{it+1}\}$ and distributions $\mathcal{D}_{it}(a^p,e)$,
- prices $\{\mathcal{E}_t, Q_t, P_t, P_{Ht}, P_{Ft}, W_t, r_t, \iota_t\}$,
- aggregate quantities $\{C_t, C_{Ht}, C_{Ft}, Y_t, A_t, p_t, d_t, \mathrm{nfa}_t\}$,

such that households optimize given prices, distributions evolve consistently with policies, firms optimize, and the domestic-goods market clears (3.7). The equilibrium selection rule is $Q_\infty = Q_{ss}$.

### 4.2 Steady state

A steady state with no inflation and zero net foreign assets is considered. Normalize prices to unity: $P_{Hss}=P_{Fss}=P_{ss}=P^{\ast}_{Hss}=\mathcal{E}_{ss}=Q_{ss}=1$. Normalize $Y_{ss}=1$, so $C_{ss}=C^{\ast}=1$. The steady-state real rate is

$$
r_{ss} \;=\; \frac{1}{\beta^{\ast}} - 1.
$$

The household discount factor $\beta$ is calibrated to clear the domestic asset market given this $r_{ss}$ and the idiosyncratic income process.

### 4.3 Initial portfolios (incomplete markets, baseline)

The portfolio indeterminacy is resolved at $t=0$ by assuming all agents hold domestic equity only: $a'=p\,s'$ and $B^H=B^F=0$. This is the **HA-IM** model. The alternative HA-CM model (Section 2.1–2.2 of the paper) allows endogenous date-0 portfolios that hedge aggregate risk; its steady state is identical, and the equations differ only in an agent-specific Backus–Smith condition (paper eq. (24)) that pins down initial $a^p_{i0}$.

---

## 5. Intertemporal MPCs and the aggregate consumption function

### 5.1 The consumption function (paper Proposition 1)

Under the reductions in section 3.8, the time-varying aggregates that enter the household Bellman (2.2) are exactly the real-income sequence $\{\tfrac{P_{Hs}}{P_s}Y_s\}$ and the real-rate sequence $\{r_s\}$. Hence there exists a functional $\mathcal{C}$ such that, for all $t\ge 0$,

$$
C_t \;=\; \mathcal{C}_t\!\left(\left\{\frac{P_{Hs}}{P_s}Y_s\right\}_{s=0}^{\infty},\; \{r_s\}_{s=0}^{\infty}\right).
$$

### 5.2 Intertemporal MPC matrix

Around the steady state, let $\mathbf{M}$ be the Fréchet derivative of $\mathcal{C}$ with respect to the real-income path and $\mathbf{M}^{r}$ be $(1+r)$ times the Fréchet derivative with respect to $\{r_s\}$:

$$
M_{t,s} \;\equiv\; \frac{\partial C_t}{\partial (P_{Hs}Y_s/P_s)},
\qquad
M^{r}_{t,s} \;\equiv\; (1+r)\cdot \frac{\partial C_t}{\partial r_s}.
$$

$M_{t,s}$ is the date-$t$ aggregate-consumption response to a date-$s$ marginal increase in aggregate real income. Non-negativity $\mathbf{M}\ge 0$ is established for RA and TA cases and assumed for HA (paper Assumption 1).

### 5.3 Derivation of $\mathbf{M}^{\text{HA-IM}}$ (paper eq. (A.67))

Let $\mathbf{M}^{\text{labor}}_{t,s}\equiv \partial \tilde C_t / \partial(W_s N_s/P_s)$ be the standard intertemporal MPC out of labour income, and $\mathbf{m}^{\text{cap}}_t\equiv \partial \tilde C_t / \partial(\tfrac{P_0+D_0}{P_0})$ the vector of date-0-wealth-revaluation MPCs. Then, using $W_sN_s/P_s = \tfrac{1}{\mu}\tfrac{P_{Hs}}{P_s}Y_s$ (eq. (3.8)) and $\tfrac{P_0+D_0}{P_0} = (1-\tfrac{1}{\mu})\cdot q^\top \tfrac{P_H}{P}Y$ (where $q$ is the discount vector), the chain rule gives

$$
\mathbf{M}^{\text{HA-IM}} \;=\; \frac{1}{\mu}\,\mathbf{M}^{\text{labor}} \;+\; \left(1-\frac{1}{\mu}\right)\,\mathbf{m}^{\text{cap}}\,q^{\top}.
$$

This is the entry point for HARK's sequence-space Jacobian interface: $\mathbf{M}^{\text{labor}}$ and $\mathbf{m}^{\text{cap}}$ are exactly what HARK's HA consumption block exposes.

---

## 6. Analytical shock-response results

### 6.1 Exchange-rate shock: RA-CM benchmark (paper Proposition 2)

Under the constant-real-rate rule $r_t=r_{ss}$ in the representative-agent complete-markets model, $dC_t=0$ and

$$
dY^{\text{RA-CM}}_t \;=\; \frac{\alpha}{1-\alpha}\,\chi\,dQ_t, \qquad \chi \;\equiv\; \eta(1-\alpha)+\gamma.
$$

All output response is from expenditure switching. $\chi$ is the trade elasticity.

### 6.2 General case — the international Keynesian cross (paper Propositions 3–4)

Under the same rule but with general consumption function, the impulse responses $d\mathbf{C}, d\mathbf{Y}$ to an exchange-rate shock $d\mathbf{Q}$ satisfy the pair of linearised equations

$$
\boxed{\quad
d\mathbf{C} \;=\; \underbrace{-\,\frac{\alpha}{1-\alpha}\,\mathbf{M}\,d\mathbf{Q}}_{\text{Real income}} \;+\; \underbrace{\mathbf{M}\,d\mathbf{Y}}_{\text{Multiplier}}
\quad}
$$

$$
\boxed{\quad
d\mathbf{Y} \;=\; \underbrace{\frac{\alpha}{1-\alpha}\,\chi\,d\mathbf{Q}}_{\text{Exp. switching}} \;-\; \underbrace{\alpha\,\mathbf{M}\,d\mathbf{Q}}_{\text{Real income}} \;+\; \underbrace{(1-\alpha)\,\mathbf{M}\,d\mathbf{Y}}_{\text{Multiplier}}
\quad}
$$

Solving,

$$
d\mathbf{Y} \;=\; \frac{\alpha}{1-\alpha}\,d\mathbf{Q} \;+\; \frac{\alpha}{1-\alpha}\,(\chi-1)\,\sum_{k\ge 0}(1-\alpha)^k\,\mathbf{M}^k\,d\mathbf{Q}
\;=\; \frac{\alpha}{1-\alpha}\,d\mathbf{Q} \;+\; \frac{\alpha}{1-\alpha}(\chi-1)\bigl(\mathbf{I}-(1-\alpha)\mathbf{M}\bigr)^{-1}d\mathbf{Q}.
$$

### 6.3 Neutrality at $\chi=1$ (paper Proposition 5)

If $\chi=1$, then $d\mathbf{Y}=\tfrac{\alpha}{1-\alpha}\,d\mathbf{Q}$ and $d\mathbf{C}=0$, with $d\mathrm{NX}=0$, **independent of $\mathbf{M}$** (and hence of the market structure). This is the first neutrality result of the paper.

### 6.4 Contractionary depreciation (paper Proposition 6 — sign of output response)

Given $\mathbf{M}\ge 0$ and a depreciation shock $d\mathbf{Q}\ge 0$:

$$
d\mathbf{Y}\lessgtr d\mathbf{Y}^{\text{RA}} \quad\text{and}\quad d\mathbf{C}\lessgtr 0 \quad\Longleftrightarrow\quad \chi \lessgtr 1.
$$

Further, if $\chi<1-\alpha$, the present-value output response is negative: $\sum_{t\ge 0}(1+r_{ss})^{-t}dY_t<0$ in the HA model. On impact, $dY_0<0$ whenever $\chi<\chi^{\ast}$ for some threshold $\chi^{\ast}\in((1-\alpha)M_{0,0},\,1)$.

### 6.5 Monetary policy (paper eq. (44) and Proposition 9)

Assuming $\sigma=1$ and the constant-real-rate rule, a monetary policy shock $d\mathbf{r}$ produces a real exchange-rate response $d\mathbf{Q}=-\mathbf{U}d\mathbf{r}$ (where $\mathbf{U}$ has ones on and above the diagonal, reflecting eq. (3.9)) and an output response satisfying the generalised international Keynesian cross

$$
d\mathbf{Y} \;=\; \underbrace{(1-\alpha)\,\mathbf{M}^{r}\,d\mathbf{r}}_{\text{Interest rate}} \;+\; \underbrace{\frac{\alpha}{1-\alpha}\,\chi\,d\mathbf{Q}}_{\text{Exp. switching}} \;-\; \underbrace{\alpha\,\mathbf{M}\,d\mathbf{Q}}_{\text{Real income}} \;+\; \underbrace{(1-\alpha)\,\mathbf{M}\,d\mathbf{Y}}_{\text{Multiplier}}.
$$

**Neutrality at $\chi=2-\alpha$ (Proposition 9).** If $\sigma=1$ and $\chi=2-\alpha$, all aggregate quantities and prices in the RA-CM and HA-IM models coincide. For an accommodative shock $d\mathbf{r}<0$,

$$
d\mathbf{Y}^{\text{HA-IM}}\lessgtr d\mathbf{Y}^{\text{RA-CM}} \quad\Longleftrightarrow\quad \chi\lessgtr 2-\alpha.
$$

The threshold $\chi=2-\alpha$ generalises the Cole–Obstfeld (1991) point ($\eta=\gamma=\sigma=1$) and extends Werning's (2015) closed-economy neutrality result to the open economy.

### 6.6 "Stealing demand from the future" (paper Proposition 10)

If $dQ_{t+s}=0$ for all $s\ge 1$, the present value of consumption and output satisfies

$$
\sum_{s\ge 1}(1+r_{ss})^{-s}\,dC_{t+s} \;=\; \frac{1}{\alpha}\,d\mathrm{nfa}_t,
\qquad
\sum_{s\ge 1}(1+r_{ss})^{-s}\,dY_{t+s} \;=\; \frac{1-\alpha}{\alpha}\,d\mathrm{nfa}_t.
$$

Current-account deficits accumulated during monetary easing must be repaid later through suppressed aggregate demand.

---

## 7. Consolidated system of baseline equations

For reference, the baseline model's equilibrium conditions in linearized sequence-space form:

| # | Equation | Source |
|---|---|---|
| E.1 | $C_t=\mathcal{C}_t(\{\tfrac{P_{Hs}}{P_s}Y_s\},\{r_s\})$ | consumption functional |
| E.2 | $Y_t=(1-\alpha)(P_{Ht}/P_t)^{-\eta}C_t + \alpha(P_{Ht}/\mathcal{E}_t)^{-\gamma}C^{\ast}$ | goods market clearing |
| E.3 | $P_t^{\,1-\eta} = \alpha P_{Ft}^{\,1-\eta}+(1-\alpha)P_{Ht}^{\,1-\eta}$ | CPI |
| E.4 | $P_{Ft}=\mathcal{E}_t$ | LOP (import) |
| E.5 | $P^{\ast}_{Ht}=P_{Ht}/\mathcal{E}_t$ | LOP (export) |
| E.6 | $Q_t=\mathcal{E}_t/P_t$ | real exchange rate |
| E.7 | $1+r_t=(1+r^{\ast}_t)Q_{t+1}/Q_t$ | UIP |
| E.8 | $P_{Ht}=\mu W_t$ | price setting |
| E.9 | $\pi^w_t=\kappa_w(v'(N_t)/(\tfrac{1}{\mu_w}\tfrac{W_t}{P_t}u'(C_t))-1)+\beta \pi^w_{t+1}$ | wage Phillips curve |
| E.10 | $Y_t=N_t$ | production |
| E.11 | $\iota_t=r_{ss}+\pi_{t+1}+\epsilon_t$ | monetary rule |
| E.12 | $1+\iota^{\ast}_t=1/(\beta^{\ast})\cdot\mathcal{B}_t/\mathcal{B}_{t+1}$ | RoW monetary |
| E.13 | $d_t=(1-1/\mu)\,(P_{Ht}/P_t)\,Y_t$ | dividends |
| E.14 | $\mathrm{nfa}_t=A_t-p_t$; $\mathrm{nfa}_t-\mathrm{nfa}_{t-1}=\mathrm{NX}_t+r_{t-1}\mathrm{nfa}_{t-1}$ | NFA / current account |
| E.15 | $(P_t+D_t)/P_t$ pricing: $1+r_t=(p_{t+1}+d_{t+1})/p_t$ | stock pricing |
| E.16 | $\mathrm{nfa}_\infty=0$, $Q_\infty=Q_{ss}$ | terminal conditions |

---

## 8. Stage decomposition of the household block (SolvingMicroDSOPs-polished)

This section provides the authoritative modular-DDSL stage structure for the incomplete-markets household block (section 2.2), following the three-perch convention of SolvingMicroDSOPs: each stage has an **arrival** perch $\prec$, a **decision** perch $\sim$, and a **continuation** perch $\succ$. The household problem has one control ($c$) together with non-trivial shock structure (Markov productivity $e$), so a single period is decomposed into **three stages**: a discounting stage, a shocks-only stage, and a shock-free consumption stage.

Define **market resources** (cash-on-hand)

$$
m_t \;\equiv\; (1+r_{t-1})\,a'_{t-1} + e_t\,\tfrac{W_t}{P_t}\,N_t,
$$

and end-of-period savings

$$
\psi_t \;\equiv\; m_t - c_t.
$$

Both $\psi$ and $a^p$ are $\psi$-type variables (investable assets before returns); $m$ is an $m$-type variable (spendable resources after returns). The between-period connector is the identity

$$
a^p_{t+1} \;=\; (1+r_t)\,\psi_t.
$$

### 8.1 Discounting stage (disc)

| Perch | Indicator | State | Value function | Explanation |
|---|---|---|---|---|
| Arrival | $\prec$ | $\bullet$ | $v_{\prec} = v_{\sim}$ | identity |
| Decision | $\sim$ | $\bullet$ | $v_{\sim} = \beta\,v_{\succ}$ | apply $\beta$ |
| Continuation | $\succ$ | $\bullet$ | $v_{\succ}$ | value at exit |

$\bullet$ is a passthrough state whose type is inherited from the predecessor stage's continuation state. No permanent-income growth ($\Gamma=1$), so the discount factor is simply $\beta$.

### 8.2 Shocks-only stage

| Perch | Indicator | State | Value function | Explanation |
|---|---|---|---|---|
| Arrival | $\prec$ | $(a^p, e)$ | $v_{\prec}(a^p,e) = \mathbb{E}_{\prec}[v_{\succ}(\check m, e')\mid e]$ | pre-shock expectation; $e$ conditions the Markov draw |
| Decision | $\sim$ | $(a^p, e)$ | — | no choice |
| Continuation | $\succ$ | $(\check m, e')$ | $v_{\succ}(\check m, e')$ | post-shock value |

Given the current Markov state $e$, the arrival value function is the expectation over next-period productivity realisations:

$$
v_{\prec}(a^p,e) \;=\; \mathbb{E}_{\prec}\!\left[v_{\succ}\!\left(a^p + e'\,\tfrac{W}{P}\,N\right)\,\Big|\,e\right]
\;=\; \sum_{e'} \Pi(e'\mid e)\cdot v_{\succ}\!\left(a^p + e'\,\tfrac{W}{P}\,N\right).
$$

Once the shock is realised, the continuation state $\check m = a^p + e'\,\tfrac{W}{P}\,N$ is deterministic. The hat indicates an $m$-type variable (spendable resources after shocks are realised). No return factor appears inside the shocks-only stage: returns are applied by the **between-period connector** $a^p_{t+1}=(1+r_t)\,\psi_t$ (see section 8.4).

This stage is a specialisation of the SolvingMicroDSOPs `portable` stage with no portfolio optimisation: the labour-income term $e'\tfrac{W}{P}N$ plays the role of the transitory shock, and the randomness enters through the Markov state $e$ alone. The aggregate objects $W, P, N$ are equilibrium quantities taken as given by the household.

### 8.3 Consumption stage (cons-noshocks)

| Perch | Indicator | State | Value function | Explanation |
|---|---|---|---|---|
| Arrival | $\prec$ | $m$ | $v_{\prec} = v_{\sim}$ | identity (no shocks) |
| Decision | $\sim$ | $m$ | $v_{\sim}(m)=\max_c\; u(c)-v(N)+v_{\succ}(m-c)$ | choose $c$ |
| Continuation | $\succ$ | $\psi$ | $v_{\succ}(\psi)$ | value at exit |

Since $v(N)$ does not depend on $c$ (union-set hours), the first-order condition reduces to the standard CRRA intertemporal Euler:

$$
u'(c) \;=\; v'_{\succ}(\psi), \quad\text{i.e.}\quad c^{-\sigma} \;=\; v'_{\succ}(m-c),
$$

which is EGM-compatible:

- **InvEuler** (policy in closed form): $c_{\succ}(\psi) = (v'_{\succ}(\psi))^{-1/\sigma}$.
- **Endogenous grid**: $m = \psi + c_{\succ}(\psi)$.
- **Envelope**: $v'_{\sim}(m) = u'(c) = c^{-\sigma}$.

The borrowing constraint $\psi\ge\underline{a}=0$ binds when $m$ is low; at the constraint, $c=m$.

### 8.4 Period structure and connectors

The period is the stage list $[\text{shocks-only}, \mathcal{C}(\check m\leftrightarrow m), \text{cons-noshocks}, \text{disc}]$:

| Element | Transition | Action |
|---|---|---|
| shocks-only | $a^p \to \check m$ | shocks realise; no choice |
| $\mathcal{C}(\check m\leftrightarrow m)$ | $\check m \to m$ | rename (within-period identity) |
| cons-noshocks | $m \to \psi$ | choose $c$ |
| disc | $\psi \to \psi$ | apply $\beta$ |

Pipeline:

```
a^p ─[shocks-only]→ m̌ ─[id]→ m ─[cons-noshocks]→ ψ ─[disc]→ exit
```

Between-period connector: $a^p_{t+1} = (1+r_t)\,\psi_t$.

### 8.5 Rationale

- **Shock timing.** Productivity $e$ is realised at the arrival perch of the shocks-only stage — not between periods, and not inside the consumption decision.
- **Ordering (shocks-only before cons-noshocks).** The cons-noshocks stage then receives a continuation value $v_{\succ}(\psi)$ with shocks already integrated out; EGM inverts the FOC directly, with no inner expectation loop.
- **EGM compatibility.** CRRA utility + additively separable budget $\psi=m-c$ makes the Endogenous Grid Method apply directly.
- **Identity wiring.** The disc stage preserves $\psi$; the next period's shocks-only stage expects $a^p$; they snap together via the identity $a^p_{t+1}=(1+r_t)\psi_t$.

---

## 9. Extensions (Section 5 of the paper — summarised, not formalised here)

The baseline stage decomposition covers Sections 2–4 of the paper. Section 5's quantitative model adds the following, each of which would extend the Dolo Plus description in a well-defined way but is **not** part of the baseline formalization:

1. **Non-homothetic preferences (Stone-Geary).** Replace the CES aggregator with $c=[\alpha^{1/\eta}(c_F-\underline{c})^{(\eta-1)/\eta}+(1-\alpha)^{1/\eta}c_H^{(\eta-1)/\eta}]^{\eta/(\eta-1)}$ with subsistence level $\underline{c}$ of imports. Affects the expenditure-share equations; leaves the household Bellman form unchanged if $\sigma=1$.
2. **Unequal incidence of aggregate shocks on workers.** Replace $e\,(W/P)\,N$ in labour income with $\,\tilde e(e,W_t N_t/P_t)\,$ from paper eq. (48), with elasticity parameter $\zeta<0$. Affects only the shocks-only stage's income-realisation formula.
3. **Sticky domestic prices (paper eq. (49)).** Phillips curve $\pi_{Ht}=\kappa_H(\mu W_t/(Z_tP_{Ht})-1)+(1+r)^{-1}\mathbb{E}_t[\pi_{H,t+1}]$ replaces (3.1)'s constant markup. Changes the aggregate block; does not affect the household Bellman.
4. **Imperfect exchange-rate pass-through (paper eqs. (50)–(51)).** Sticky import and export prices $P_{Ft}, P^{\ast}_{Ht}$ with Calvo parameters $\theta_F,\theta_{H^{\ast}}$. Changes equations (E.4) and (E.5) from LOP to Phillips curves.
5. **Delayed substitution (paper eqs. (52)–(55)).** Households re-optimise the home/foreign consumption split only with Calvo probability $1-\theta$. Introduces two auxiliary state variables $\log\hat x_{Ht}$ and $\log\hat x^{\ast}_{Ht}$ into the aggregate block, and makes the trade elasticity effectively time- and shock-dependent.
6. **Inertial Taylor rule (paper eq. (20)).** Replaces the constant-real-rate rule with $\iota_t=\rho_m \iota_{t-1}+(1-\rho_m)(r_{ss}+\phi \pi_{t+1})+\epsilon_t$.

---

## 10. Calibration values (paper Table 2)

Benchmark model values used in the analytical results (sections 2–4 of the paper):

| Parameter | Value | Notes |
|---|---:|---|
| $\sigma$ | 1.00 | log preferences |
| $\varphi$ | 2.00 | Frisch elasticity = 0.5 |
| $\eta=\gamma$ | $\{0.1, 0.5, 1, 2-\alpha\}$ | swept across; benchmark figures use several values |
| $\beta^{\ast}$ | 0.990 | RoW discount factor; implies annual $r_{ss}=4\%$ |
| $\beta$ | 0.965 | calibrated to clear asset market |
| $\alpha$ | 0.40 | from Galí-Monacelli (2005) |
| $\theta_w$ | 0.938 | wage Calvo parameter |
| $\mu$ | 1.043 | price markup, calibrated to match quarterly MPC = 0.20 |
| $\sigma_e$ | 0.883 | std of log income (Mexico, adjusted for taxes) |
| $\rho_e$ | 0.912 | AR(1) persistence of log income |
| $\underline{a}$ | 0 | borrowing constraint |

**Moments matched (HA-IM benchmark).** Average quarterly MPC of 0.20 (Hong 2023, Peru); std of log annual post-tax income 0.84 (Guvenen-Pistaferri-Violante 2022, Mexico, adjusted); AR(1) coefficient 0.78; average import share 0.40 (Galí-Monacelli 2005).

The quantitative model additionally calibrates $\theta=0.976$, $\zeta=-0.196$, $\theta_H=\theta_{H^{\ast}}=0.66$, $\underline{c}=0.085$, $\rho_m=0.8$, $\phi=1.5$, $\alpha=0.344$ — see Section 5.2 of the paper.

---

## 11. Answers to Matsya's prior questions (session `topics2026-siying99-ballpark`)

Matsya's turn-5 reply (2026-04-12) accepted the household perch structure, transitions, preferences, Bellman, continuation value, borrowing constraint, and EGM applicability, and identified one remaining blocker plus three secondary choices. The expanded document now resolves all of them:

| Matsya question (turn 5) | Resolution |
|---|---|
| **Markov process for $e$** — discrete or continuous? if continuous, what AR(1) parameters and what discretisation? | **AR(1) in log productivity, Rouwenhorst-discretised to a 7-state finite Markov chain.** Persistence $\rho_e=0.912$, cross-sectional std $\sigma_e=0.883$ (paper Table 2; matched to Mexico GRID-project moments). Cross-sectional mean $\mathbb{E}\,e_{it}=1$ enforced by re-normalisation post-discretisation. See §2.3. |
| **EGM sub-equations** — include `InvEuler`, `MarginalBellman`, `cntn_to_dcsn_transition`? | **Yes — all three.** CRRA + additively separable budget makes EGM the natural channel. See §8.3 for the explicit FOC, InvEuler closed form, endogenous-grid step, and envelope condition. |
| **Parameter values** — leave as named symbols with calibration stub? | **Yes — named symbols in the YAML, with a calibration block populated from paper Table 2** (§10 here). The benchmark column is the appropriate baseline. |
| **Notation** — ASCII or Unicode? | **ASCII for the YAML** (matches existing `dolo-plus-draft.yaml`); Unicode/LaTeX in this document for human readers. |

Matsya's turn-6 perch table used a **single-stage** decomposition $(\prec, \circ, \succ)$. The verification step (recorded in `verification.md`) **rejected** the single-stage form in favour of the SolvingMicroDSOPs three-stage form `[shocks-only, cons-noshocks, disc]` documented in §8 here, on the grounds that the three-stage form makes the EGM channel exactly $\mathbb{B}$-applicable in the cons-noshocks stage with no inner expectation, and isolates the discount-factor application as a separate `disc` stage. A formalizer should treat §8 as authoritative; the single-stage form is the equivalent compact representation and either is acceptable in YAML.

## 12. Pointers for Matsya / formalizer

1. **Household block is fully specified in section 8.** The stage decomposition is modular-DDSL-ready: three stages, explicit perches, between-period connector $a^p_{t+1}=(1+r_t)\psi_t$.
2. **Aggregate block is specified equation-by-equation in sections 3–4 and consolidated in section 7.** These are ready to be grouped into stages or written as a system of sequence-space equations for the SSJ apparatus.
3. **The iMPC matrix $\mathbf{M}$ of section 5 is the bridge object.** Under the chain-rule decomposition (eq. (A.67) in the paper, reproduced in section 5.3 here), $\mathbf{M}^{\text{HA-IM}}$ can be constructed from standard objects that HARK's incomplete-markets household block already exposes — $\mathbf{M}^{\text{labor}}$ and $\mathbf{m}^{\text{cap}}$ — so no new numerical machinery is needed once the household block is implemented.
4. **Assumption 1 ($\mathbf{M}\ge 0$) is invoked in the sign results of section 6.** The Dolo Plus description should declare $\mathbf{M}\ge 0$ as a maintained assumption rather than re-deriving it.
5. **The RoW-monetary normalisation $P^{\ast}_t=1, C^{\ast}_t=C^{\ast}$ is a modelling choice, not a numerical one.** It should appear in the Dolo Plus preamble as an assumption on the block structure, not as a Phillips-curve equation.
6. **Terminal conditions.** $\mathrm{nfa}_\infty=0$ and $Q_\infty=Q_{ss}$ enforce equilibrium selection. These are horizon-end constraints in a stationary infinite-horizon problem.

---

## 13. Open items (canonical scope record)

This section is the **canonical** record of every part of the paper that is *specified* in this excerpt but *not yet encoded* in the companion `dolo-plus-draft.yaml`, plus every workaround / non-canonical-syntax choice made in the YAML. It is the source of truth: `index.md` / `OpenHA.md` frontmatter, `AGENTS.md` "Formalization status", and the YAML's preamble all defer here for the rationale and the follow-up plan. Inline `# unresolved:` comments at the point of divergence in the YAML cite the relevant item below by number.

### 13.1 Aggregate block: out-of-scope for this YAML, deliberately

**Status.** The household three-stage period of §8 is encoded in `dolo-plus-draft.yaml`. The aggregate / GE closure of §§3–4 — equations E.1–E.16 in the consolidated system of §7 — is **not** encoded.

**Why this is the right scope choice for this PR.**

- CONTRIBUTING.md's "Formalized" tier explicitly allows a one-stage / one-block YAML; the entry's promotional checklist is satisfied by a paper-grounded household-block YAML alone.
- The household block is the part of OpenHA that maps cleanly onto HARK's existing incomplete-markets consumption block (the iMPC matrix $\mathbf{M}$ of §5, which is exactly the sequence-space-Jacobian object HARK already exposes). It is the *natural unit* for an Econ-ARK / HARK cross-check, and the natural starting point for any REMARK replication.
- The aggregate block requires non-trivial dolo-plus modelling choices (how to encode the wage Phillips curve as a stage equation; whether the real-UIP arbitrage is a between-period or within-period equation; how to wire the household-block iMPC matrix into the aggregate-block GE solver) that are independent of the household-block work and are best resolved in a separate follow-up PR with their own Matsya iteration.

**What the follow-up PR should contain.**

- A new `aggregate-draft.yaml` in this directory implementing the 16 equations consolidated in §7 above. The natural composition is (a) one block grouping E.3–E.7 (price/exchange-rate identities), (b) one block grouping E.8–E.10 + E.13 (firm/dividend/production), (c) one block for E.9 (wage Phillips curve), (d) one block for E.11–E.12 (monetary rules), (e) one block for E.2 (goods-market clearing), (f) one block for E.14–E.16 (NFA/current-account/terminal conditions).
- Wiring of `dolo-plus-draft.yaml` (household) and `aggregate-draft.yaml` (aggregate) into a higher-level GE composition file. The household-block `r`, `w`, `N` parameters become inputs from the aggregate block; the household-block aggregate consumption $C_t$ becomes an input to the aggregate-block goods-market-clearing equation E.2.
- A renewed Matsya pass (continue session `topics2026-siying99-ballpark`) on the full `bellman-excerpt.md` to flag any DDSL issues with §§3, 5, 6, 7 that did not surface in the household-block-only round 8 iteration.

### 13.2 Rouwenhorst higher-level constructor (non-blocking spec gap)

**Status.** The household YAML declares the idiosyncratic-productivity Markov shock as `@dist MarkovChain(Pi, e)` (Stage `shocks`, line 53), with the assumption that $\Pi$ is built externally from $(\rho_e, \sigma_\varepsilon, n_e)$ via Rouwenhorst.

**Why this is a workaround, not a fudge.** A higher-level constructor of the form `@dist Rouwenhorst(rho_e, sigma_eps, n_e)` would be cleaner — the Markov chain $\Pi$ is fully specified by $(\rho_e, \sigma_\varepsilon, n_e)$ + the Rouwenhorst (1995) algorithm — but is **not yet canonical in the dolo-plus spec**. Conservative choice retained; revisit when the spec evolves.

**Inline flag.** The YAML carries an inline `# unresolved: see bellman-excerpt.md §13.2` comment at line 53 (the `e_prime` declaration), per the CONTRIBUTING.md (line 44) requirement that workarounds be flagged at the point of divergence.

### 13.3 Horizon: explicit declaration

**Status.** The household YAML now carries an explicit `horizon: infinite-stationary` declaration in its preamble (per CONTRIBUTING.md / dolo-plus convention). The model is the infinite-horizon stationary problem of paper §2 (continuum of households, no death, no birth, fixed Markov productivity process); a terminal-period stage is therefore not present.

**Why this is the right horizon choice for OpenHA.** The paper's analytical apparatus (§§3–6 in `bellman-excerpt.md`) treats the stochastic steady state with an MIT shock around it; the household block is the infinite-horizon stationary policy. A finite-horizon variant would require a terminal-period stage with bequest weight or warm-glow utility, neither of which appears in the paper. The infinite-stationary choice is therefore *paper-grounded*, not a default.

### 13.4 Time-varying equilibrium prices declared as parameters

**Status.** The household YAML declares the equilibrium prices `w`, `N`, `r` as `parameters` (calibration block) rather than as inputs from an aggregate stage.

**Why this is consistent with §13.1.** This YAML covers the household block only; in a one-block compilation the prices that would in a full GE loop come from the aggregate block are necessarily exogenous to the household block. The follow-up `aggregate-draft.yaml` (§13.1) would supply them as time-varying exogenous inputs to the household stage. Inline comment at the YAML preamble records this; a `# unresolved: see bellman-excerpt.md §13.4` flag is **not** added at the parameter declarations themselves because the parameter form is the *correct* representation under the household-only scope, not a workaround.
