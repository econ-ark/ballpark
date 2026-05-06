# Household Bellman Problem - Dupor et al. (2023)

Excerpted from `Subfiles/model.tex` (Section 4), written as a **partial-equilibrium household problem** with explicit stage decomposition following the SolvingMicroDSOPs / dolo-plus pedagogical style. The regional mutual fund, intermediate firms, and all aggregate prices are exogenous.

---

## Timing Within a Period

The usual analysis packs many events into a single complex decision. Following the approach of SolvingMicroDSOPs, we decompose everything that happens within a period into distinct operations so that each element can be understood in isolation.

1. **Arrival perch** prec: The household enters the period with assets *a* from last period's savings decision. The Markov productivity state *x* has not yet been revealed.
2. **Shock realization** (arrival → decision transition): Nature draws the new productivity *x'* from the Markov law given last period's *x*. Non-labour market resources *m* are then determined (see Step 1).
3. **Decision perch** dec: The household observes *(m, x')* and jointly chooses consumption *c* and labour supply *h*. The full budget is market resources plus after-tax labour income:

$$
c + a' = m + (1-\tau) w x' h
$$

1. **Continuation perch** cntn: End-of-period assets *a' = m + (1 - tau) w x' h - c* are determined. The household carries *(a', x')* into the next period's arrival perch.

---

## Stage Flow Diagram

```
  +--------------+   Pi(x'|x)   +--------------+  max c,h   +--------------+
  | Arrival [prec] |--------->| Decision [dec] |----------->| Cont. [cntn] |
  |    (a, x)      |  m = ...  |   (m, x')     | a' = ...   |   (a', x')   |
  +--------------+            +--------------+            +--------------+
        ^                                                        |
        +------------------------ next period -------------------+
```

---

## State and Control Spaces


| Perch             | Variable | Domain      | Description                                         |
| ----------------- | -------- | ----------- | --------------------------------------------------- |
| Arrival prec      | *a*      | nonnegative | Beginning-of-period assets                          |
| Arrival prec      | *x*      | finite set  | Last period's Markov productivity (conditions *x'*) |
| Exogenous         | *x'*     | finite set  | Markov draw (resolves at arrival → decision)        |
| Decision dec      | *m*      | nonnegative | Non-labour market resources (constructed)           |
| Decision dec      | *x'*     | finite set  | Realised productivity                               |
| Control           | *c*      | positive    | Consumption                                         |
| Control           | *h*      | 0 to 1      | Labour supply (fraction of time endowment)          |
| Continuation cntn | *a'*     | nonnegative | End-of-period assets                                |
| Continuation cntn | *x'*     | finite set  | Realised productivity (carry-forward)               |


The Markov index *x* appears at both arrival and continuation perches: the current realisation *x'* passes through as a sufficient statistic for next period's Markov draw.

---

## Step 1: Arrival → Decision Transition

The household arrives with assets *a* and last period's Markov index *x*. Nature draws the new productivity:

$$
x' \sim \Pi(\cdot \mid x)
$$

*(Shock draw.)*

Non-labour market resources *m* are the sum of: (i) gross return on assets *(1 + r) a*, (ii) after-tax profit-sharing income *(1 - tau) (x' / xbar) (1 - omega) D*, and (iii) lump-sum transfer *T*:

$$
m = (1+r)a + (1-\tau)\frac{x'}{\bar{x}}(1-\omega)D + T
$$

*(Arrival to decision: construction of m.)*

The variable *m* bundles all non-labour resources into a single sufficient statistic, analogous to "market resources" (or "cash-on-hand") in SolvingMicroDSOPs. After this transition the decision-perch state is *(m, x')*.

**Information at the decision perch:** the household observes both *m* and *x'* before choosing *(c, h)*.

---

## Step 2: The Decision Problem (Bellman Equation)

Given *(m, x')*, the household solves:

$$  
V(m,x') = \max_{c,h} \left( u(c,h) + \beta V(a',x') \right)  
$$

Paper eq. 4.3: value at the decision perch; *V(a',x')* on the right-hand side is the continuation value.

subject to the budget constraint:

$$
a' = m + (1-\tau) w x' h - c
$$

*(Paper eq. 4.4.)*

and the bounds:

$$
c > 0,\quad h \in [0,1],\quad a' \geq 0
$$

*(Paper eq. 4.5.)*

### Period Utility

$$
u(c,h) = \log(c) + \psi \frac{(1-h)^{1-\theta}}{1-\theta}
$$

where *log(c)* gives unit elasticity of intertemporal substitution, and *theta* governs the Frisch elasticity of labour supply.

### The Joint *(c, h)* Choice

Unlike the standard buffer-stock model (which has a single control *c*), this problem has two controls chosen simultaneously. The intratemporal first-order condition for *h* is:

$$
\psi (1-h)^{-\theta} = \frac{(1-\tau) w x'}{c}
$$

which pins down *h* as a function of *c* and *x'*:

$$
h = 1 - \left( \frac{c \psi}{(1-\tau) w x'} \right)^{1/\theta}
$$

This analytical reduction means the problem can (in principle) be reduced to a single effective control *c*, with *h* determined by the intratemporal condition. The EGM inversion step is non-standard because labour income *w x' h* depends on the control.

---

## Step 3: Decision → Continuation Transition

Given optimal choices *c* and *h* (solution values), end-of-period assets are:

$$
a' = m + (1-\tau) w x' h^* - c^*
$$

*(Decision to continuation.)*

The continuation-perch state is *(a', x')*. The household carries both into the next period's arrival perch, where *a'* becomes next period's *a* and *x'* becomes next period's conditioning variable for the Markov draw.

---

## Step 4: Continuation → Arrival Mover (Expectation)

The arrival value function integrates over the pre-decision Markov shock:

$$
V(a,x) = E_{x'|x}\left[ V(m(a,x'), x') \right] = \sum_{x'} \Pi(x'|x) V(m(a,x'), x')
$$

Expectation over *x'* given *x*; paper timing: shock before choice.

Because the Markov shock is **pre-decision** (resolves at arrival → decision), the expectation sits in the continuation-to-arrival step, not inside the max. The decision-perch problem is deterministic conditional on *(m, x')*.

The marginal (envelope) condition for the arrival value is:

$$
V_a(a,x) = E_{x'|x}\left[ \frac{1+r}{c^*(m(a,x'), x')} \right]
$$

This marginal value is the object that the Euler equation from the previous period's decision perch must satisfy.

---

## Exogenous Parameters (from GE)

These are determined in general equilibrium but are fixed from the household's perspective:


| Symbol  | Meaning                      | Origin                                           |
| ------- | ---------------------------- | ------------------------------------------------ |
| *w*     | Real wage                    | Labour-market clearing (intermediate firms)      |
| *r*     | Real return on savings       | Mutual-fund no-arbitrage: *1 + r = (1+R)/(1+pi)* |
| *D*     | Per-capita real dividends    | Intermediate firms' profits                      |
| *omega* | Dividend retention share     | Mutual-fund structure                            |
| *tau*   | Proportional income-tax rate | Government budget constraint                     |
| *T*     | Lump-sum transfer            | Government budget constraint                     |
| *x* bar | Mean productivity            | Normalisation                                    |


---

## Preference and Process Parameters


| Symbol           | Meaning                                                                   |
| ---------------- | ------------------------------------------------------------------------- |
| *beta*           | Discount factor (two types per region, solved separately)                 |
| *psi*            | Leisure utility weight                                                    |
| *theta*          | Leisure curvature (Frisch elasticity parameter)                           |
| *Pi(x' given x)* | Markov transition for *x* (discretised AR(1): log *x' = rho log x + eta*) |
| *rho*            | Productivity persistence                                                  |
| *sigma_eta*      | Productivity innovation s.d.                                              |


---

## Structural Summary


| Design question      | Dupor2023 answer                                          | DDSL rationale                                          |
| -------------------- | --------------------------------------------------------- | ------------------------------------------------------- |
| Shock timing         | Pre-decision (Markov *x'* resolves at arrival → decision) | Expectation in `dcsn_to_arvl_mover`, not inside max     |
| Decision variables   | Joint *(c, h)*                                            | Single decision perch, two controls                     |
| State at decision    | *(m, x')* (constructed)                                   | *m* bundles asset return + dividends + transfer         |
| Continuation state   | *(a', x')*                                                | *a'* endogenous poststate; *x'* exogenous carry-forward |
| Budget constraint    | *a' = m + (1-tau) w x' h - c*                             | `dcsn_to_cntn_transition`                               |
| Borrowing constraint | *a' >= 0*                                                 | Poststate domain bound                                  |
| PE vs GE             | *w, r, D, T* exogenous                                    | Clean interface for GE extension                        |


---

*Source*: Dupor, Karabarbounis, Kudlyak, and Mehkari (2023), "Regional Consumption Responses and the Aggregate Fiscal Multiplier," Section 4.

*Stage decomposition style*: Following Carroll (2024), "Solving Microeconomic Dynamic Stochastic Optimization Problems," Section 1 ("The Problem").