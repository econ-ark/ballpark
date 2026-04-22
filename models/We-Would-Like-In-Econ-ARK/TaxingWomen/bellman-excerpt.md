# Bellman excerpt — TaxingWomen (working draft)

Source paper: Guner, Kaygusuz, Ventura (2012), "Taxing Women: A Macroeconomic Analysis," *Journal of Monetary Economics* 59(1), 111–128. [DOI 10.1016/j.jmoneco.2011.10.002](https://doi.org/10.1016/j.jmoneco.2011.10.002).

This file collects the paper's three recursive problems in the form needed by a modular DP layer: a symbol table first, then the three Bellman equations as they appear in the paper, then a terse statement of the within-period perch decomposition. The polished SMD-style version is in `bellman-excerpt-SMD-polished.md`; the Dolo+ encoding is in `dolo-plus-draft.yaml`.

Primitives (preferences, tax function, human-capital law of motion, permanent-types structure, terminal condition, equilibrium concept) are in `TaxingWomen_Summary.ipynb` §II.0.

## Symbol table

### States

| Symbol | Household | Meaning |
|---|---|---|
| $a$ | all | assets entering the period |
| $h$ | single female, married | wife's human capital |
| $x$ | single female, married | wife's permanent productivity type, drawn once |
| $z$ | single male, married | husband's permanent productivity type, drawn once |
| $q$ | married | wife's permanent utility cost of joint work, drawn once at marriage, $q \sim \text{Gamma}(\cdot\mid z)$ |
| $b$ | single female, married | birth year of first child, drawn once |
| $j$ | all | age |

### Controls

| Symbol | Household | Meaning |
|---|---|---|
| $l$ | singles | own labor supply |
| $l_f$ | married | wife's labor supply |
| $l_m$ | married | husband's labor supply |
| $a'$ | all | next-period assets |

### Parameters and auxiliary functions

| Symbol | Role |
|---|---|
| $\beta$ | time discount |
| $\varphi,\gamma$ | labor-disutility scale and Frisch elasticity |
| $\kappa$ | wife's young-child time cost $^{\dagger}$ |
| $\delta = 0.02$ | human-capital atrophy per period out of the workforce |
| $a_j^x$ | age- and type-dependent human-capital accumulation rate while participating |
| $\chi(l) = \mathbf{1}\{l > 0\}$ | participation indicator |
| $G(x, h, l_f, j) = \exp\!\big(\ln h + a_j^x \chi(l_f) - \delta(1-\chi(l_f))\big)$ | wife's human-capital law of motion |
| $d(s)$ | child-care goods cost per unit of wife's time, $s = j+1-b$; $d(1) = 0.064$, $d(2)=d(3)=0.049$ |
| $w, r$ | equilibrium wage and interest rate |
| $\tau_k, \tau_p$ | capital- and payroll-tax rates |
| $\varpi_m(z, j)$ | husband's age- and type-specific productivity |
| $T^S(I, k),\;T^M(I, k)$ | income tax for singles / married, conditioned on presence of young children $k \in \{0,1\}$; both equal to $\tau(\tilde y)\cdot I$ with $\tilde y = I/\bar I$, $\tau(\tilde y) = \zeta_1 + \zeta_2 \ln \tilde y$, $(\zeta_1, \zeta_2)$ indexed by filing status × children (GKV 2012 Table 2) |
| $p_m^S(z), p_f^S(x), p^M(x,z)$ | retirement benefits |
| $J_R, J$ | retirement age; terminal age |
| $V_{J+1} \equiv 0$ | terminal condition (no bequest motive) |

$^{\dagger}$ The exact channel through which $\kappa$ enters (the additive form $(l + k_y \kappa)$) and the exact additive form of the wife's participation cost $q\cdot\chi(l_f)$ in the married-household objective are recorded here from the authors' notes and are consistent with the calibration in GKV 2012 Table 3; they should be confirmed against GKV 2012 eq. (3) before the Dolo+ encoding is treated as paper-verified. See `verification.md`.

## Bellman equations as written in the paper

### 1. Single male

$$
V_m^S(a, z, j) = \max_{a', l \ge 0}\;\Big\{U_m^S(c, l) + \beta\, V_m^S(a', z, j+1)\Big\},
$$

with

$$
U_m^S(c, l) = \ln c - \varphi\,\frac{l^{1+1/\gamma}}{1+1/\gamma},
$$

subject to

$$
c + a' = \begin{cases}
a(1+r(1-\tau_k)) + w\varpi_m(z,j)\,l\,(1-\tau_p) - T^S(w\varpi_m(z,j)l + ra,\,0), & j < J_R, \\
a(1+r(1-\tau_k)) + p_m^S(z) - T^S(ra,\,0), & j \ge J_R,
\end{cases}
$$

with $a' \ge 0$ (strict equality if $j = J$) and $V_{J+1}^{S,m} \equiv 0$.

### 2. Single female

$$
V_f^S(a, h, x, b, j) = \max_{a', l \ge 0}\;\Big\{U_f^S(c, l, k_y) + \beta\, V_f^S(a', h', x, b, j+1)\Big\},
$$

with

$$
U_f^S(c, l, k_y) = \ln c - \varphi\,\frac{(l + k_y\kappa)^{1+1/\gamma}}{1+1/\gamma},
\qquad
h' = G(x, h, l, j),
$$

subject to the paper's three budget branches (with young child; working-age no young child; retired) exactly as in `TaxingWomen_Summary.ipynb` §II.2.

### 3. Married household (working-age leg, unitary objective)

$$
V^M(a, h, x, z, q, b, j) = \max_{a', l_f, l_m \ge 0}\;\Big\{U^M(c, l_m, l_f;\, k_y, q) + \beta\, V^M(a', h', x, z, q, b, j+1)\Big\},
$$

with a **single** $\ln c$ rather than $u_f + u_m$:

$$
U^M(c, l_m, l_f;\, k_y, q) = \ln c - \varphi\,\frac{l_m^{1+1/\gamma}}{1+1/\gamma} - \varphi\,\frac{(l_f + k_y\kappa)^{1+1/\gamma}}{1+1/\gamma} - q\,\chi(l_f),
$$

$$
h' = G(x, h, l_f, j),
$$

subject to the paper's three budget branches as in `TaxingWomen_Summary.ipynb` §II.3.

The retired leg $j \ge J_R$ uses $p^M(x, z) - T^M(ra, 0)$ on the resource side and drops the labor controls.

## Within-period perch decomposition (working-age married)

Because permanent types $(x, z, q, b)$ are drawn once and there are no within-period shocks, the arrival-to-decision mover is the identity on every stage. The one-period operator factors as $\mathbb{T} = \mathbb{I} \circ \mathbb{B}$ where $\mathbb{I}$ is (degenerate) integration and $\mathbb{B}$ is the Bellman choice map.

The working-age married period decomposes into four stages flowing forward as

$$
\text{female\_labor} \;\to\; \text{male\_labor} \;\to\; \text{consumption\_savings} \;\to\; \text{disc} \;\to\; [\text{connector}].
$$

Each stage has three perches: arrival ($\prec$), decision ($\sim$), continuation ($\succ$). Because there are no within-period shocks, arrival $=$ decision on every stage. See `bellman-excerpt-SMD-polished.md` for the full perch tables, transitions, and a per-stage EGM-amenability discussion.

Intuitively:

- `female_labor` handles the part of period utility that depends on $l_f$ and carries $l_f$ forward because it determines the wife's next-period human capital through $G$.
- `male_labor` handles the part of period utility that depends on $l_m$; it does not change the endogenous transition.
- `consumption_savings` evaluates the budget constraint (current net resources given $(l_f, l_m)$) and chooses $a'$; only this stage is EGM-amenable and has the closed form $c = 1/(\beta\, v'_\succ(a', h', x, z, q, b))$ from log utility.
- `disc` is a stub stage applying $\beta$; the connector renames $(a', h') \mapsto (a, h)$ at age $j+1$.

The singles' problems drop the `male_labor` stage and use $U_m^S$ or $U_f^S$ respectively in `female_labor`; for the single male the human-capital transition also drops.

## Workarounds and unresolved items

- `# workaround:` The tax function $\tau(\tilde y) = \zeta_1 + \zeta_2 \ln(I/\bar I)$ is singular as $I \to 0$. Guard low-asset retiree grid points with $\max(I, \varepsilon)$ for a small $\varepsilon$; documented inline in `dolo-plus-draft.yaml`.
- `# workaround:` $(\zeta_1, \zeta_2)$ switch on (filing status × young-children indicator). This parameter switching has no canonical Dolo+ syntax, so `dolo-plus-draft.yaml` instantiates the consumption-savings stage four times, once per (filing, kids) cell.
- `# unresolved:` The single male's intratemporal FOC in $l$ is not EGM-invertible because the log-progressive tax wedge makes marginal after-tax wage a function of $l$ itself. Root-find rather than invert. The single female and the married household have the same feature on their labor stages.
- `# unresolved:` The final-period continuation perch at $j = J$ is degenerate ($V_{J+1} \equiv 0$); label the connector at age $J$ as a terminal connector in the YAML.

## Provenance

- Primitives: `TaxingWomen_Summary.ipynb` §II.0 (committed 2026-04-21 under the Item 1 fix).
- Bellman equations: `TaxingWomen_Summary.ipynb` §II.1–§II.3 (as inherited from the paper).
- Stage decomposition: adapted from the married-household four-stage SMD-style draft in `TaxingWomen_bellman-stages.ipynb` (companion notebook), with the married-household utility aligned to the single-$\ln c$ unitary objective.
- Framework conventions (perch naming, $\mathbb{T} = \mathbb{I} \circ \mathbb{B}$ factoring, degenerate-perch labelling): `llorracc/ballpark/CONTRIBUTING.md` §Formalized.
