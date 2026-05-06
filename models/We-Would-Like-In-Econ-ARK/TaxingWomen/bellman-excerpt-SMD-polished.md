# Bellman excerpt, SMD-polished — TaxingWomen (working draft)

Paper: Guner, Kaygusuz, Ventura (2012), "Taxing Women: A Macroeconomic Analysis," *Journal of Monetary Economics* 59(1), 111–128. [DOI 10.1016/j.jmoneco.2011.10.002](https://doi.org/10.1016/j.jmoneco.2011.10.002).

This file presents the within-period recursive problem in the style of `SolvingMicroDSOPs` §§12–13, using the modular perch architecture. The terse terminal Bellman statements and the full symbol table are in `bellman-excerpt.md`; the Dolo+ encoding is in `dolo-plus-draft.yaml`.

The presentation below is for the **working-age married household**, $j < J_R$. Singles are a strict subset (single male drops the female-labor stage and the human-capital transition; single female drops the male-labor stage). Retirement $j \ge J_R$ collapses to consumption-savings and discounting with no labor stages.

## 1. The paper's recursive problem, recalled

The married household solves

$$
V^M(a, h, x, z, q, b, j) \;=\; \max_{a', l_f, l_m \ge 0}\;\Big\{U^M(c, l_m, l_f;\, k_y, q) \,+\, \beta\, V^M(a', h', x, z, q, b, j+1)\Big\},
$$

with the **unitary** period utility

$$
U^M(c, l_m, l_f;\, k_y, q) \;=\; \ln c \;-\; \varphi\,\frac{l_m^{1+1/\gamma}}{1+1/\gamma} \;-\; \varphi\,\frac{(l_f + k_y\kappa)^{1+1/\gamma}}{1+1/\gamma} \;-\; q\,\chi(l_f),
$$

the wife's human-capital law of motion $h' = G(x, h, l_f, j) = \exp\!\big(\ln h + a_j^x\chi(l_f) - \delta(1-\chi(l_f))\big)$, and the resource constraint

$$
c + a' \;=\; a(1+r(1-\tau_k)) \,+\, w(\varpi_m(z,j)l_m + h\,l_f)(1-\tau_p) \,-\, T^M(I, k_y) \,-\, w\,d(j+1-b)\,\chi(l_f)\cdot k_y,
$$

with $I = w\varpi_m(z,j)l_m + w h l_f + r a$, $T^M(I, k) = \tau(I/\bar I)\cdot I$, $\tau(\tilde y) = \zeta_1 + \zeta_2 \ln \tilde y$. The retired and no-young-children legs drop the labor or child-care terms accordingly. Permanent types $(x, z, q, b)$ are drawn once and there is no new within-period shock; the arrival-to-decision mover is the identity on every stage.

## 2. Why a four-stage decomposition

Three within-period controls $(l_f, l_m, a')$ sit inside one maximization. A modular stage architecture exposes each economic decision separately while remaining equivalent to the paper's recursion. The ordering chosen here is

$$
\text{female\_labor} \;\to\; \text{male\_labor} \;\to\; \text{consumption\_savings} \;\to\; \text{disc}.
$$

The ordering matters for two reasons:

1. **Female labor changes the endogenous next-period state** through $G(x, h, l_f, j)$, while male labor does not. Placing `female_labor` first makes the effect of $l_f$ on $h'$ explicit in the continuation value passed through `consumption_savings`.
2. **Consumption-savings is the only EGM-amenable stage.** Once $(l_f, l_m)$ are fixed and the budget constraint is evaluated at those choices, the $a'$ problem reduces to a one-dimensional consumption-savings subproblem with log utility, admitting the closed-form Euler inversion $c = 1/(\beta\, v'_\succ(a', h', x, z, q, b))$.

The discount factor is handled in its own stub stage `disc`, following `SolvingMicroDSOPs`, so that $\beta$ is a stage operator rather than a silent factor inside a continuation value.

Because there are no within-period shocks, every stage's arrival perch coincides with its decision perch ($W^\prec = W^\sim$). The one-period operator factors as $\mathbb{T} = \mathbb{I} \circ \mathbb{B}$ where $\mathbb{I}$ is the (degenerate, identity) integration operator and $\mathbb{B}$ is the Bellman choice map.

## 3. Perch tables

Notation. Within-period stage values are denoted $W^{s, \cdot}$ where $s$ labels the stage and $\cdot \in \{\prec, \sim, \succ\}$ labels the perch. Age subscript $j$ is suppressed when unambiguous; it re-enters through age-dependent primitives such as $k_y(b, j)$, $\varpi_m(z, j)$, $d(j+1-b)$, $a_j^x$.

### Stage 1: `female_labor`

| Perch | State | Value function | Key transition or Bellman step |
|---|---|---|---|
| $\prec$ | $(a, h, x, z, q, b)$ | $W^{f,\prec} = W^{f,\sim}$ | degenerate arrival mover (identity; no within-period shock) |
| $\sim$ | $(a, h, x, z, q, b)$ | $W^{f,\sim} = \max_{l_f \ge 0}\Big\{-\varphi\,\frac{(l_f + k_y\kappa)^{1+1/\gamma}}{1+1/\gamma} - q\,\chi(l_f) + W^{f,\succ}\Big\}$ | wife's labor choice; extensive margin handled by corner $l_f = 0$ |
| $\succ$ | $(a, h, x, z, q, b, l_f)$ | $W^{f,\succ} = W^{m,\prec}$ | identity forward to `male_labor` |

**EGM amenability.** Not EGM-amenable. The log-progressive tax wedge $\tau(\tilde y) = \zeta_1 + \zeta_2 \ln \tilde y$ renders the wife's first-order condition in $l_f$ implicit; root-find.

### Stage 2: `male_labor`

| Perch | State | Value function | Key transition or Bellman step |
|---|---|---|---|
| $\prec$ | $(a, h, x, z, q, b, l_f)$ | $W^{m,\prec} = W^{m,\sim}$ | degenerate arrival mover |
| $\sim$ | $(a, h, x, z, q, b, l_f)$ | $W^{m,\sim} = \max_{l_m \ge 0}\Big\{-\varphi\,\frac{l_m^{1+1/\gamma}}{1+1/\gamma} + W^{m,\succ}\Big\}$ | husband's labor choice |
| $\succ$ | $(a, h, x, z, q, b, l_f, l_m)$ | $W^{m,\succ} = W^{c,\prec}$ | identity forward to `consumption_savings` |

**EGM amenability.** Not EGM-amenable for the same reason as Stage 1; the husband's intratemporal FOC in $l_m$ involves the same tax wedge evaluated at total family income.

### Stage 3: `consumption_savings`

| Perch | State | Value function | Key transition or Bellman step |
|---|---|---|---|
| $\prec$ | $(a, h, x, z, q, b, l_f, l_m)$ | $W^{c,\prec} = W^{c,\sim}$ | degenerate arrival mover |
| $\sim$ | $(a, h, x, z, q, b, l_f, l_m)$ | $W^{c,\sim} = \max_{a' \ge 0}\big\{\ln c + W^{c,\succ}(a', h', x, z, q, b)\big\}$ subject to $c + a' = \mathrm{NetResources}(a, h, l_f, l_m, x, z, b, j)$ | consumption-savings choice; $h' = G(x, h, l_f, j)$ |
| $\succ$ | $(a', h', x, z, q, b)$ | $W^{c,\succ} = W^{\beta,\prec}$ | identity forward to `disc` |

**EGM amenability.** **Yes.** With log utility, the Euler equation gives $1/c = \beta\, v'_\succ(a', h', x, z, q, b)$ so $c(a', \cdot) = 1/\big(\beta\, v'_\succ(a', h', x, z, q, b)\big)$, and the endogenous grid on $a'$ maps back to $a$ through the resource constraint evaluated at the stage's state. This is the only EGM-amenable stage in the period and the reason to place it third.

### Stage 4: `disc`

| Perch | State | Value function | Key transition or Bellman step |
|---|---|---|---|
| $\prec$ | $(a', h', x, z, q, b)$ | $W^{\beta,\prec} = W^{\beta,\sim}$ | degenerate arrival mover |
| $\sim$ | $(a', h', x, z, q, b)$ | $W^{\beta,\sim} = \beta\, W^{\beta,\succ}$ | no economic choice; applies $\beta$ |
| $\succ$ | $(a', h', x, z, q, b)$ | $W^{\beta,\succ} = V^{M,\prec}_{j+1}\big(C_j^M(a', h', x, z, q, b)\big)$ | inter-period connector $C_j^M$ |

### Inter-period connector (not a stage)

The connector is the pure rename $C_j^M: (a', h', x, z, q, b) \leftrightarrow (a, h, x, z, q, b)$ at age $j+1$. At $j = J$ the connector is terminal: $V^{M,\prec}_{J+1} \equiv 0$.

## 4. Rosetta Stone: paper notation ↔ stage notation

| Paper object | Stage object | Where it lives |
|---|---|---|
| $V^M(a, h, x, z, q, b, j)$ | $V^{M,\prec}_j(\cdot) = W^{f,\prec}_j(\cdot)$ | entry perch of `female_labor` |
| $\max_{l_f}$ over the $l_f$-dependent terms of $U^M$ | `female_labor` decision perch | Stage 1, $\sim$ |
| $\max_{l_m}$ over the $l_m$-dependent term of $U^M$ | `male_labor` decision perch | Stage 2, $\sim$ |
| $\max_{a'}$ over $\ln c$ subject to the budget constraint | `consumption_savings` decision perch | Stage 3, $\sim$ |
| $\beta V^M(a', h', x, z, q, b, j+1)$ | $W^{\beta,\sim}$ then connector to $V^{M,\prec}_{j+1}$ | Stage 4 |
| $h' = G(x, h, l_f, j)$ | `consumption_savings` $\succ$-state update | Stage 3 $\succ$ |
| Budget constraint evaluated at $(l_f, l_m)$ | `consumption_savings` decision perch constraint | Stage 3 $\sim$ |

## 5. Stage composition and equivalence with the paper's recursion

Stacking the four stages:

$$
\begin{aligned}
W^{f,\sim}_j(a,h,x,z,q,b) &= \max_{l_f \ge 0}\Big\{-\varphi\,\tfrac{(l_f + k_y\kappa)^{1+1/\gamma}}{1+1/\gamma} - q\,\chi(l_f) + W^{m,\prec}_j(a,h,x,z,q,b,l_f)\Big\},\\
W^{m,\prec}_j &= W^{m,\sim}_j = \max_{l_m \ge 0}\Big\{-\varphi\,\tfrac{l_m^{1+1/\gamma}}{1+1/\gamma} + W^{c,\prec}_j(a,h,x,z,q,b,l_f,l_m)\Big\},\\
W^{c,\prec}_j &= W^{c,\sim}_j = \max_{a' \ge 0}\big\{\ln c + W^{\beta,\prec}_j(a',G(x,h,l_f,j),x,z,q,b)\big\},\\
W^{\beta,\prec}_j &= W^{\beta,\sim}_j = \beta\, V^{M,\prec}_{j+1}(a',h',x,z,q,b),
\end{aligned}
$$

subject to $c + a' = \mathrm{NetResources}$ and $V^{M,\prec}_{J+1} \equiv 0$.

Substituting from the bottom up reproduces the paper's single-maximization Bellman equation. The only non-trivial step is observing that the $\ln c$ term and the resource constraint live together in the `consumption_savings` stage; this is consistent with the paper because $c$ in the paper's $U^M$ is a function of $(a, a', l_f, l_m, \cdot)$ via the budget constraint, and the modular form just exposes this dependency by making $a'$ the stage-internal control.

## 6. Singles as restrictions of the married decomposition

- **Single male** ($j < J_R$): drop `female_labor`; use $U_m^S(c, l) = \ln c - \varphi\, l^{1+1/\gamma}/(1+1/\gamma)$ in `male_labor`; drop the human-capital state $h$ and the human-capital transition from `consumption_savings`. Period flow: `male_labor` → `consumption_savings` → `disc`.
- **Single female** ($j < J_R$): drop `male_labor`; use $U_f^S(c, l, k_y) = \ln c - \varphi\,(l + k_y\kappa)^{1+1/\gamma}/(1+1/\gamma)$ in `female_labor`. Keep the human-capital transition in `consumption_savings`. Period flow: `female_labor` → `consumption_savings` → `disc`.
- **Retired** ($j \ge J_R$): both labor stages drop; use the retired budget with pension $p$ and tax $T(ra, 0)$. Period flow: `consumption_savings` → `disc`. The `consumption_savings` stage should be instantiated with the retired resource constraint (no labor income); the closed-form Euler inversion still applies.

## 7. EGM discussion and per-stage computational channel

| Stage | EGM-amenable? | Channel |
|---|---|---|
| `female_labor` | No | tax wedge $\zeta_2 \ln(I/\bar I)$ makes FOC in $l_f$ implicit; root-find |
| `male_labor` | No | same tax wedge, now on total family $I$; root-find in $l_m$ given $l_f$ |
| `consumption_savings` | **Yes** | log utility ⇒ $c = 1/(\beta\, v'_\succ)$ closed form; endogenous grid on $a'$ |
| `disc` | n/a | pure scalar multiplication |

The computational payoff from placing `consumption_savings` third is that once the two labor choices are fixed, the one-dimensional savings problem has an explicit Euler inversion and can be solved on an endogenous $a'$-grid without a nested root-find.

## 8. Workarounds and unresolved items

- `# workaround:` tax function $\tau(I/\bar I)$ is singular as $I \to 0$; guard low-asset retiree and zero-labor grid cells with $\max(I, \varepsilon)$. See `dolo-plus-draft.yaml` parameter block.
- `# workaround:` $(\zeta_1, \zeta_2)$ are indexed by filing status × young-children indicator (GKV 2012 Table 2). Dolo+ has no canonical syntax for parameter switching conditional on a state-computed indicator; in `dolo-plus-draft.yaml` this is handled by instantiating the consumption-savings stage four times, one per (filing, kids) cell, and routing grid points by the computed indicator.
- `# unresolved:` the labor FOCs in both `female_labor` and `male_labor` are implicit under the log-progressive tax; the canonical Dolo+ solver interface should expose a root-find option per stage.
- `# unresolved:` the extensive margin at $l_f = 0$ is a corner of the continuous optimization, not a separate discrete branch. This Kuhn–Tucker treatment is equivalent to a branching formulation but keeps the stage interface continuous; an alternative branching formulation is noted for reference but not adopted here because the bellman-stages draft already demonstrates that the corner treatment is sufficient.
- `# unresolved:` calibration parameters (Frisch $\gamma$, labor-disutility scale $\varphi$, $\kappa$, $\delta$, the grids for $z, x, q, b$, the $(\zeta_1, \zeta_2)$ table) should be migrated to a separate `calibration.yaml` or into the `parameters:` block of `dolo-plus-draft.yaml` rather than staying in free text. GKV 2012 Table 3 is the paper-anchored source.

## 9. Provenance

- Primitives: `TaxingWomen_Summary.ipynb` §II.0.
- Bellman equations: `TaxingWomen_Summary.ipynb` §II.1–§II.3.
- Stage decomposition: `TaxingWomen_bellman-stages.ipynb` (companion notebook, non-branching four-stage SMD-style decomposition), with the married-household utility aligned to the single-$\ln c$ unitary objective per the verification discipline in `verification.md`.
- Framework conventions: `llorracc/ballpark/CONTRIBUTING.md` §Formalized; `SolvingMicroDSOPs` §§12–13.
