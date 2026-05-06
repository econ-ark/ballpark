# GKV (2012) Married Household: DDSL Stage Decomposition

*Produced via Matsya (session: `topics2026-TaxingWomen`), following the expository template from Carroll's SolvingMicroDSOPs lecture notes (Sections 4 and 9).*

*Source: Guner, Kaygusuz, and Ventura, "Taxing Women: A Macroeconomic Analysis," JME 59 (2012), 111–128.*

---

## 1. Overview: The Period as a Stage List

The married household's period is a **branching DAG**, not a linear list. The wife's participation decision creates a fan-out that reconverges at the end of the period.

**Period short-name notation:**

$$\text{Period}_j = [\ell\text{-branch}, \; c_w \mid c_h, \; \beta]$$

Read: "labor-branch stage (with fan-out), then consumption-savings (one per branch, reconverging), then discounting."

**DAG structure:**

```
                        ┌─── cons-work ───┐
                        │                 │
arrival ─── labor-branch┤                 ├─── disc ─── next period
                        │                 │
                        └─── cons-home ───┘
```

The `labor-branch` stage is a **branching stage** with `branch_control: agent` (the household chooses $d \in \{\text{work}, \text{home}\}$ to maximize). The two `cons` stages are structurally identical EGM-amenable consumption-savings problems that receive different resources and human capital from the branch.

**Critical structural feature:** There are **no within-period stochastic shocks** in GKV (2012). All heterogeneity $(z, x, q, b)$ is permanent, drawn once at birth. Conditional on types, the life-cycle problem is fully deterministic.

---

## 2. Stage Inventory

| Short-name | Control-name | Kind | Controls | Description |
|---|---|---|---|---|
| `labor-branch` | $\ell$ | Branching (agent) | $d, l_m, l_f$ | Wife participation + joint labor supply |
| `cons-work` | $c_w$ | Sequential | $c$ | Consumption-savings, work branch |
| `cons-home` | $c_h$ | Sequential | $c$ | Consumption-savings, home branch |
| `disc` | $\beta$ | Sequential | — | Discounting (inter-period building) |

---

## 3. Rosetta Stone

### State Variables

| Math Symbol | Description | Type | Domain |
|---|---|---|---|
| $a$ | End-of-period assets | $k$-type (capital before returns) | $\mathbb{R}_+$ |
| $h$ | Wife's human capital | $k$-type (capital before returns) | $\mathbb{R}_+$ |
| $m$ | Cash-on-hand (total spendable resources) | $m$-type (after returns/taxes) | $\mathbb{R}_+$ |
| $h'$ | Next-period human capital | $k$-type (determined by branch) | $\mathbb{R}_+$ |

### Permanent Types (Parameters, Not State Variables)

| Math Symbol | Description | Domain |
|---|---|---|
| $z$ | Husband's permanent productivity type | $\mathcal{Z} = \{1, 2, 3, 4\}$ (HS, some college, college, college+) |
| $x$ | Wife's permanent productivity type | $\mathcal{X} = \{1, 2, 3, 4\}$ (same categories) |
| $q$ | Utility cost of wife's participation | $\mathbb{R}_+$ (drawn once from $\text{Gamma}(\cdot \mid z)$) |
| $b$ | Childbearing status | $\{0, 1, 2\}$ (none, early, late) |
| $j$ | Age (period index) | $\{1, \ldots, J\}$ |

### Controls

| Math Symbol | Description | Domain | Stage |
|---|---|---|---|
| $d$ | Wife's participation indicator | $\{0, 1\}$ | `labor-branch` |
| $l_m$ | Husband's labor supply | $[0, 1]$ | `labor-branch` |
| $l_f$ | Wife's labor supply | $[0, 1]$ | `labor-branch` (work branch only) |
| $c$ | Consumption | $\mathbb{R}_+$ | `cons-work`, `cons-home` |

### Structural Functions

| Math Symbol | Description | Depends on |
|---|---|---|
| $\varpi_m(z, j)$ | Husband's age-efficiency profile | Permanent type $z$, age $j$ |
| $a_j^x$ | Wife's HC growth rate (if working) | Permanent type $x$, age $j$ |
| $\delta$ | Wife's HC depreciation rate (if not working) | $= 0.02$ |
| $T^M(I, k)$ | Married tax liability: $(\zeta_1 + \zeta_2 \ln(I/\bar{I})) \cdot I$ | Total income $I$, children $k$ |
| $d(s)$ | Child care price | Child age $s = j + 1 - b$ |

### Value Functions

| Math Symbol | Perch | Description |
|---|---|---|
| $\mathrm{v}_{\prec}^{\ell}$ | Arrival at `labor-branch` | Value at period entry |
| $\mathrm{v}_{\sim}^{\ell}$ | Decision at `labor-branch` | Value after (trivial) arrival-to-decision |
| $\mathrm{v}_{\succ,w}^{\ell}$ | Continuation, work branch | Exit value toward `cons-work` |
| $\mathrm{v}_{\succ,h}^{\ell}$ | Continuation, home branch | Exit value toward `cons-home` |
| $\mathrm{v}_{\prec}^{c}$ | Arrival at `cons-*` | Value at entry to consumption stage |
| $\mathrm{v}_{\sim}^{c}$ | Decision at `cons-*` | Value of consumption-savings problem |
| $\mathrm{v}_{\succ}^{c}$ | Continuation at `cons-*` | End-of-period value |

---

## 4. Perch Tables

### Stage 1: `labor-branch` [$\ell$] — Branching (agent)

The household arrives with assets $a$ and wife's human capital $h$. No shocks resolve (all heterogeneity is permanent). The household jointly chooses participation $d$, husband's hours $l_m$, and (if $d = 1$) wife's hours $l_f$. The stage fans out into two branches with different resources and human capital transitions.

| Perch | Indicator | State | Value function | Explanation |
|---|---|---|---|---|
| Arrival | $\prec$ | $(a, h)$ | $\mathrm{v}_{\prec}^{\ell} = \mathrm{v}_{\sim}^{\ell}$ | No shocks $\Rightarrow$ identity |
| Decision | $\sim$ | $(a, h)$ | $\mathrm{v}_{\sim}^{\ell} = \max_{d} \left\{ \mathrm{v}^{\ell,w}, \; \mathrm{v}^{\ell,h} \right\}$ | Discrete max over branches |
| Continuation (work) | $\succ_w$ | $(m_w, h'_w)$ | $\mathrm{v}_{\succ,w}^{\ell}$ | Resources + HC if wife works |
| Continuation (home) | $\succ_h$ | $(m_h, h'_h)$ | $\mathrm{v}_{\succ,h}^{\ell}$ | Resources + HC if wife stays home |

The branch-conditional decision values are:

$$\mathrm{v}^{\ell,w}(a, h) \coloneqq \max_{l_m, l_f > 0} \left\{ -\varphi \frac{l_m^{1+1/\gamma}}{1+1/\gamma} - \varphi \frac{(l_f + k_y\kappa)^{1+1/\gamma}}{1+1/\gamma} - q + \mathrm{v}_{\succ,w}^{\ell}(m_w, h'_w) \right\}$$

$$\mathrm{v}^{\ell,h}(a, h) \coloneqq \max_{l_m} \left\{ -\varphi \frac{l_m^{1+1/\gamma}}{1+1/\gamma} - \varphi \frac{(k_y\kappa)^{1+1/\gamma}}{1+1/\gamma} + \mathrm{v}_{\succ,h}^{\ell}(m_h, h'_h) \right\}$$

**Transitions (decision → continuation):**

*Work branch ($d = 1$):*

$$y_m = w \cdot \varpi_m(z, j) \cdot l_m, \qquad y_f = w \cdot h \cdot l_f$$
$$I_w = y_m + y_f + r \cdot a, \qquad \text{cc} = w \cdot d(s)$$
$$m_w = a(1 + r(1 - \tau_k)) + (y_m + y_f)(1 - \tau_p) - T^M(I_w, k) - \text{cc}$$
$$h'_w = h \cdot \exp(a_j^x)$$

*Home branch ($d = 0$):*

$$y_m = w \cdot \varpi_m(z, j) \cdot l_m, \qquad y_f = 0$$
$$I_h = y_m + r \cdot a$$
$$m_h = a(1 + r(1 - \tau_k)) + y_m(1 - \tau_p) - T^M(I_h, k)$$
$$h'_h = h \cdot \exp(-\delta)$$

**Arrival mover:** Identity — $\mathrm{v}_{\prec}^{\ell}(a, h) = \mathrm{v}_{\sim}^{\ell}(a, h)$ (no shocks).

---

### Stage 2w: `cons-work` [$c_w$] — Sequential (EGM)

The household enters the work branch with resources $m_w$ and updated human capital $h'_w$. Standard consumption-savings with $\log$ utility. Human capital $h'_w$ is a pass-through state.

| Perch | Indicator | State | Value function | Explanation |
|---|---|---|---|---|
| Arrival | $\prec$ | $(m, h')$ | $\mathrm{v}_{\prec}^{c_w} = \mathrm{v}_{\sim}^{c_w}$ | No shocks |
| Decision | $\sim$ | $(m, h')$ | $\mathrm{v}_{\sim}^{c_w} = \max_{c} \left\{ \log(c) + \mathrm{v}_{\succ}^{c_w} \right\}$ | EGM-amenable |
| Continuation | $\succ$ | $(a, h')$ | $\mathrm{v}_{\succ}^{c_w}$ | End-of-period assets + HC |

**Transition (decision → continuation):** $a = m - c$, $h'$ passes through.

**EGM (InvEuler):** $c_{[\succ]} = (\mathrm{v}_{\succ}^{c_w,\partial})^{-1}$ since $u^{\partial}(c) = 1/c$.

**Reverse transition:** $m_{[\succ]} = a + c_{[\succ]}$

**MarginalBellman:** $\mathrm{v}_{\sim}^{c_w,\partial} = 1/c$

---

### Stage 2h: `cons-home` [$c_h$] — Sequential (EGM)

Structurally identical to `cons-work`. Different input $(m_h, h'_h)$, same code.

| Perch | Indicator | State | Value function | Explanation |
|---|---|---|---|---|
| Arrival | $\prec$ | $(m, h')$ | $\mathrm{v}_{\prec}^{c_h} = \mathrm{v}_{\sim}^{c_h}$ | No shocks |
| Decision | $\sim$ | $(m, h')$ | $\mathrm{v}_{\sim}^{c_h} = \max_{c} \left\{ \log(c) + \mathrm{v}_{\succ}^{c_h} \right\}$ | EGM-amenable |
| Continuation | $\succ$ | $(a, h')$ | $\mathrm{v}_{\succ}^{c_h}$ | End-of-period assets + HC |

---

### Stage 3: `disc` [$\beta$] — Discounting

| Perch | Indicator | State | Value function | Explanation |
|---|---|---|---|---|
| Arrival | $\prec$ | $\bullet$ | $\mathrm{v}_{\prec}^{\beta} = \mathrm{v}_{\sim}^{\beta}$ | No shocks |
| Decision | $\sim$ | $\bullet$ | $\mathrm{v}_{\sim}^{\beta} = \beta \cdot \mathrm{v}_{\succ}^{\beta}$ | Apply $\beta$ |
| Continuation | $\succ$ | $\bullet$ | $\mathrm{v}_{\succ}^{\beta}$ | Value at exit |

n.b.: $\bullet$ is a generic passthrough state whose type ($k$-type) is inherited from the predecessor stage's continuation state $(a, h')$.

---

## 5. Connectors

### Intra-Period Connectors

| Connector | From | To | Mapping | Type check |
|---|---|---|---|---|
| $\mathcal{C}_1^w$ | `labor-branch` $\succ_w$ | `cons-work` $\prec$ | $(m_w, h'_w) \leftrightarrow (m, h')$ | $m$-type $\to$ $m$-type ✓ |
| $\mathcal{C}_1^h$ | `labor-branch` $\succ_h$ | `cons-home` $\prec$ | $(m_h, h'_h) \leftrightarrow (m, h')$ | $m$-type $\to$ $m$-type ✓ |
| $\mathcal{C}_2^w$ | `cons-work` $\succ$ | `disc` $\prec$ | $(a, h') \leftrightarrow (a, h')$ | $k$-type $\to$ $k$-type ✓ |
| $\mathcal{C}_2^h$ | `cons-home` $\succ$ | `disc` $\prec$ | $(a, h') \leftrightarrow (a, h')$ | $k$-type $\to$ $k$-type ✓ |

### Inter-Period Connector

| Connector | From | To | Mapping | Type check |
|---|---|---|---|---|
| $\mathcal{C}_{\beta}$ | `disc` $\succ$ (period $j$) | `labor-branch` $\prec$ (period $j+1$) | $(a, h') \leftrightarrow (a, h)$ | $k$-type $\to$ $k$-type ✓ |

**Type discipline:** The labor-branch stage converts $k$-type variables $(a, h)$ into $m$-type variables $(m_w, h'_w)$ or $(m_h, h'_h)$ through the budget constraint and human capital law of motion. The consumption stage converts $m$-type back to $k$-type through the savings decision. This is the standard $k \to m \to k$ cycle from SolvingMicroDSOPs Section 4.3.

Note that $h$ and $h'$ are both $k$-type: human capital is a stock that earns returns (wages) when combined with labor, analogous to how financial capital $a$ earns returns $r$.

---

## 6. Flow Table

| Element | Transition | Action |
|---|---|---|
| `labor-branch` | $(a, h) \to \{(m_w, h'_w), (m_h, h'_h)\}$ | Choose $d, l_m, l_f$; compute taxes, child care, HC update; **fan-out** |
| $\mathcal{C}_1^w(m_w, h'_w \leftrightarrow m, h')$ | $m_w \to m$ | Rename (work branch) |
| $\mathcal{C}_1^h(m_h, h'_h \leftrightarrow m, h')$ | $m_h \to m$ | Rename (home branch) |
| `cons-work` | $m \to a$ | Choose $c$; EGM (work branch) |
| `cons-home` | $m \to a$ | Choose $c$; EGM (home branch) |
| $\mathcal{C}_2^{w,h}(a, h' \leftrightarrow a, h')$ | identity | **Fan-in** (reconverge) |
| `disc` | — | Apply $\beta$ |
| $\mathcal{C}_{\beta}(a, h' \leftrightarrow a, h)$ | $h' \to h$ | Inter-period rename |

**Period as stage list (DAG notation):**

$$\text{Period}_j = \left[\ell, \; \begin{pmatrix} c_w \\ c_h \end{pmatrix}, \; \beta \right]$$

---

## 7. DAG Diagram with Perch Detail

```
Period j
═══════════════════════════════════════════════════════════════════

  labor-branch [ℓ]
  ┌─────────────────────────────────────────────────────────┐
  │  ≺:(a,h) ──identity──▶ ∼:(a,h) ──┬── ▹_w:(m_w, h'_w) │
  │                         max{d}    │                     │
  │                                   └── ▹_h:(m_h, h'_h)  │
  └───────────────────────────────┬──────────────┬──────────┘
                                  │              │
                          C_1^w(m_w↔m)    C_1^h(m_h↔m)
                                  │              │
                                  ▼              ▼
                          cons-work [c_w]  cons-home [c_h]
                          ┌────────────┐  ┌────────────┐
                          │ ≺:(m,h')   │  │ ≺:(m,h')   │
                          │ ∼: max_c   │  │ ∼: max_c   │
                          │ ▹:(a,h')   │  │ ▹:(a,h')   │
                          └─────┬──────┘  └──────┬─────┘
                                │                │
                          C_2^w(a↔a)       C_2^h(a↔a)
                                │                │
                                └───────┬────────┘
                                        │  fan-in
                                        ▼
                                   disc [β]
                                ┌──────────┐
                                │ v_▹ = β  │
                                │ v_≺(j+1) │
                                └────┬─────┘
                                     │
                               C_β(a↔a, h'↔h)
                                     │
                                     ▼
                              Period j+1 arrival
```

---

## 8. Backward Solution Order

Solve from continuation toward arrival:

1. **Solve `disc`:** Given $\mathrm{v}_{\prec}^{\ell}(\cdot; j+1)$ from next period, compute $\mathrm{v}_{\succ}^{c}(a, h') = \beta \, \mathrm{v}_{\prec}^{\ell}(a, h'; j+1)$

2. **Solve `cons-work`:** Given $\mathrm{v}_{\succ}^{c_w}$, use EGM to compute $\mathrm{v}_{\sim}^{c_w}(m, h')$ and policy $c^*(m, h')$. Propagate $\mathrm{v}_{\prec}^{c_w} = \mathrm{v}_{\sim}^{c_w}$ (no shocks).

3. **Solve `cons-home`:** Identical EGM procedure, yielding $\mathrm{v}_{\sim}^{c_h}(m, h')$.

4. **Solve `labor-branch`:** For each $(a, h)$ on the state grid:

   a. **Work branch:** Receive $\mathrm{v}_{\succ,w}^{\ell} = \mathrm{v}_{\prec}^{c_w}$ via $\mathcal{C}_1^w$. Optimize over $(l_m, l_f)$ using the labor FOCs and the marginal value $\partial_m \mathrm{v}_{\prec}^{c_w}$. Compute $\mathrm{v}^{\ell,w}(a, h)$.

   b. **Home branch:** Receive $\mathrm{v}_{\succ,h}^{\ell} = \mathrm{v}_{\prec}^{c_h}$ via $\mathcal{C}_1^h$. Optimize over $l_m$ only. Compute $\mathrm{v}^{\ell,h}(a, h)$.

   c. **Discrete choice:** $\mathrm{v}_{\sim}^{\ell}(a, h) = \max\{\mathrm{v}^{\ell,w}(a, h), \; \mathrm{v}^{\ell,h}(a, h)\}$

   d. **Arrival:** $\mathrm{v}_{\prec}^{\ell}(a, h; j) = \mathrm{v}_{\sim}^{\ell}(a, h)$ (no shocks).

---

## 9. Modularity Properties

The three principles from SolvingMicroDSOPs Section 4.1 are satisfied:

**Principle 1 — Self-contained stages.** Each stage's internal logic (perch transitions, optimization, EGM) is defined independently. The `cons-work` and `cons-home` stages are literally the same code with different input data.

**Principle 2 — Rearrangement by rewiring.** To study a model variant where the participation decision happens *after* savings (choose $a'$ first, then decide whether wife works), only the stage order and connectors change: $[c, \; \ell\text{-branch}, \; \beta]$. No stage code is rewritten.

**Principle 3 — Namespace uniqueness.** Within the period, $a$ always means end-of-period assets ($k$-type), $m$ always means cash-on-hand ($m$-type), $h$ is beginning-of-period human capital, $h'$ is next-period human capital. The connectors handle all renaming explicitly.

---

## 10. Tax Policy Counterfactuals in the DAG

The modularity pays off for GKV's policy experiments. Switching tax regimes affects **only the `labor-branch` stage's transition equations** — the consumption stages, connectors, discounting, and DAG structure are all unchanged:

| Policy experiment | What changes | What stays |
|---|---|---|
| Joint $\to$ individual filing | $T^M(I, k) \to T^S(y_m, 0) + T^S(y_f, k)$ in `labor-branch` | `cons-*`, `disc`, all connectors |
| Flat tax ($\tau_L$ on wives, $\tau_H$ on husbands) | $T^M \to \tau_L y_f + \tau_H y_m$ in `labor-branch` | Everything else |
| Child care subsidy | $\text{cc} = w \cdot d(s) \to (1-\sigma) w \cdot d(s)$ in `labor-branch` | Everything else |
| Remove participation cost | $q = 0$ in `labor-branch` Bellman | Everything else |
