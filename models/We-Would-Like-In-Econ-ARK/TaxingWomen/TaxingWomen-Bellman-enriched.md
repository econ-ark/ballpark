# Bellman Equations in Guner, Kaygusuz, and Ventura (2012)

*Excerpted from: "Taxing Women: A Macroeconomic Analysis," Journal of Monetary Economics 59 (2012), 111–128, Sections 3–5.*

## Timing and Demographics

The model is a **stationary overlapping generations** economy. The model period is **5 years**. Agents are indexed by age $j \in \{1, 2, \ldots, J\}$, retire at age $J_R$, and die at age $J$. Population grows at rate $n$; the fraction of age-$j$ agents is $\mu_j$ with $\mu_{j+1} = \mu_j / (1+n)$.

Individuals are born as either **single or married**; marital status **does not change** over time (marriage is absorbing, no divorce). Spouses are assumed to be the same age.

**Important: there are no period-by-period stochastic shocks in this model.** All heterogeneity is determined at birth — types $z$, $x$, $q$, and $b$ are permanent. The model is a deterministic life-cycle problem conditional on initial types.

## State Variables and Notation

| Symbol | Meaning |
|--------|---------|
| $a$ | household assets ($a \geq 0$; $a' = 0$ at $j = J$) |
| $z \in Z$ | male intrinsic type — **permanent**, drawn once at birth; $Z \subset \mathbb{R}_{++}$ is a finite set with 4 elements corresponding to education levels: high school, some college, college, more than college |
| $x \in X$ | female intrinsic type — **permanent**, drawn once at birth; $X \subset \mathbb{R}_{++}$ is a finite set with 4 elements (same education categories) |
| $h \in H$ | female human capital (endogenous); initial value $h_1 = \zeta(x)$ depends on type |
| $q \in Q$ | utility cost of joint work — drawn **once** at start of marriage (not re-drawn); $Q \subset \mathbb{R}_{++}$ finite; distribution $\xi(q \mid z)$ is gamma, conditional on husband's type |
| $b \in \{0,1,2\}$ | childbearing status — **permanent**, assigned at birth (0 = no children, 1 = early, 2 = late) |
| $j \in \{1,\ldots,J\}$ | age; retirement at $J_R$ |
| $k \in \{0,1\}$ | children present in household: $k=1$ iff $b \in \{1,2\}$ and $j \in \{b, b{+}1, b{+}2\}$; $k=0$ otherwise |
| $k_y \in \{0,1\}$ | young (age-1) children present: $k_y = 1$ iff $b = j$ |

**Marital matching.** The fraction of marriages between type-$x$ females and type-$z$ males is $M(x,z)$, exogenously given. The fraction of single type-$z$ males is $\omega(z)$ and single type-$x$ females is $\phi(x)$.

## Children

Children are assigned exogenously at birth. Early child bearers ($b=1$) have two children at ages $j = 1, 2, 3$. Late child bearers ($b=2$) have children at $j = 2, 3, 4$. Children last for 3 model periods (15 years). Children provide no utility but impose costs:

- **Child care costs:** If a female with children works, the household pays $w \cdot d(s)$ where $s = j+1-b$ is the age of the children. Here $d(s)$ is units of child care labor per two children. The cost is incurred only when the female works: $w \cdot d(s) \cdot \chi(l)$ where $\chi(l) = \mathbf{1}\{l > 0\}$.
- **Time cost:** Young children ($s = 1$, i.e., $b = j$) impose a fixed time cost $\kappa$ on the mother regardless of work status, entering utility as $\varphi(l + k_y \kappa)^{1+1/\gamma}$.

## Prices, Technology, and Tax Parameters

**Production.** An aggregate firm operates $F(K, L_g) = K^\alpha L_g^{1-\alpha}$. Factor prices are competitive: $w = F_2(K, L_g)$, $R = F_1(K, L_g)$, and $r = R - \delta_k$.

| Symbol | Meaning |
|--------|---------|
| $w$ | competitive wage rate |
| $r$ | net return on assets ($r = R - \delta_k$) |
| $\tau_k$ | capital income tax rate |
| $\tau_p$ | payroll tax rate (flat, on individual labor income) |
| $T^S(I, k)$, $T^M(I, k)$ | income tax functions for singles and married households |

**Tax function specification (Section 5).** The effective average tax rate is

$$
\tau(\tilde{y}) = \zeta_1 + \zeta_2 \log(\tilde{y}),
$$

where $\tilde{y}$ is household income expressed as a multiple of mean household income. Total tax liabilities are $T(I, k) = \tau(\tilde{y}) \cdot \tilde{y} \cdot \bar{I}$, where $\bar{I}$ is mean household income and $\tilde{y} = I / \bar{I}$. Separate $(\zeta_1, \zeta_2)$ estimates apply by marital status and presence of children:

| Filing status | $\zeta_1$ | $\zeta_2$ |
|---------------|-----------|-----------|
| Married, no children | 0.1028 | 0.0582 |
| Married, two children | 0.0789 | 0.0763 |
| Single, no children | 0.1392 | 0.0481 |
| Single, two children (head of household) | 0.090 | 0.0819 |

The implied marginal tax rate is $\tau'(\tilde{y}) = \zeta_1 + \zeta_2(1 + \log(\tilde{y}))$, which is increasing in income (progressive).

**Taxable income** $I$ is total labor plus capital income: $I = ra + w \cdot \text{(labor earnings)}$. Social security benefits are not taxed.

**Social security.** Retired households receive type-dependent benefits $p_m^S(z)$, $p_f^S(x)$, or $p^M(x,z)$.

## Male Productivity

Each male's type $z$ is **permanent** (no stochastic transition). The age-$j$ productivity of a type-$z$ male is $\varpi_m(z, j)$, an exogenous deterministic age-efficiency profile. Males do not face human capital depreciation.

## Female Human Capital Accumulation

Each female starts with initial productivity $h_1 = \zeta(x)$ depending on her permanent type $x$. Thereafter, productivity evolves endogenously according to (Eq. 4 in the paper):

$$
h' = G(x, h, l, j) = \exp\!\bigl[\ln h + a_j^x\,\chi(l) - \delta\,(1 - \chi(l))\bigr],
$$

where:
- $\chi(l) = \mathbf{1}\{l > 0\}$ is the participation indicator
- $a_j^x$ is an age- and type-specific growth factor conditional on working (calibrated so that a female who works every period matches the male age-efficiency profile of the same type, up to a constant gender gap)
- $\delta$ is the depreciation rate from non-participation

This means: if the female works ($l > 0$), her human capital grows by $a_j^x$; if she does not work ($l = 0$), it depreciates by $\delta$. The decision is binary at the human-capital level — hours affect utility but not the growth/depreciation rate.

## Preferences

The momentary utility function for a **single female** is

$$
U_f^S(c, l, k_y) = \log(c) - \varphi\,(l + k_y \kappa)^{1+1/\gamma},
$$

and for a **single male**,

$$
U_m^S(c, l) = \log(c) - \varphi\, l^{1+1/\gamma}.
$$

For **married households**, the couple maximizes the sum of their members' utilities. When the female works, the household incurs a utility cost $q$. The married female's utility is

$$
U_f^M(c, l_f, q, k_y) = \log(c) - \varphi\,(l_f + k_y \kappa)^{1+1/\gamma} - \tfrac{1}{2}\,\chi_{\{l_f > 0\}}\, q,
$$

and the married male's utility is

$$
U_m^M(c, l_m, l_f, q) = \log(c) - \varphi\, l_m^{1+1/\gamma} - \tfrac{1}{2}\,\chi_{\{l_f > 0\}}\, q,
$$

where $\gamma > 0$ is the intertemporal (Frisch) elasticity of labor supply, $\varphi$ controls the disutility of work, $\kappa$ is the fixed time cost of young children for females, and consumption $c$ is a public good within the household. The parameters $\gamma$ and $\varphi$ are **independent of gender and marital status**.

The household objective is **unitary**: the married household maximizes $U_f^M + U_m^M$ (no bargaining).

## Calibrated Parameter Values (Table 3 of the paper)

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Population growth rate | $n$ | 1.1 (per 5-year period) |
| Discount factor | $\beta$ | 0.972 (per 5-year period) |
| Frisch elasticity of labor supply | $\gamma$ | 0.4 |
| Disutility of market work | $\varphi$ | 8.03 |
| Time cost of young children | $\kappa$ | 0.132 |
| Child care cost, young children (age $s=1$) | $d(1)$ | 0.064 |
| Child care cost, older children (age $s=2,3$) | $d(2)=d(3)$ | 0.049 |
| Human capital depreciation (females) | $\delta$ | 0.02 |
| Capital share | $\alpha$ | 0.343 |
| Capital depreciation rate | $\delta_k$ | 0.055 |
| Payroll tax rate | $\tau_p$ | 0.086 |
| Capital income tax rate | $\tau_k$ | 0.097 |
| Utility cost distribution | $\xi(q \mid z)$ | Gamma, calibrated to match LFP by education conditional on husband's type |

---

## Bellman Equation 1: Single Male

The state for a single male is $(a, z, j)$. His problem is

$$
V_m^S(a, z, j) = \max_{a', l} \Bigl\{ U_m^S(c, l) + \beta\, V_m^S(a', z, j+1) \Bigr\}
$$

subject to the budget constraint

$$
c + a' =
\begin{cases}
a\bigl(1 + r(1-\tau_k)\bigr) + w\,\varpi_m(z,j)\,l\,(1-\tau_p) - T^S\bigl(w\,\varpi_m(z,j)\,l + ra,\; 0\bigr) & \text{if } j < J_R, \\[6pt]
a\bigl(1 + r(1-\tau_k)\bigr) + p_m^S(z) - T^S(ra, 0) & \text{if } j \geq J_R,
\end{cases}
$$

and $l \geq 0$, $a' \geq 0$ (with $a' = 0$ if $j = J$).

Here $\varpi_m(z,j)$ is the age-$j$ productivity of a type-$z$ male, and $p_m^S(z)$ is his social security benefit.

---

## Bellman Equation 2: Single Female

The state for a single female is $(a, h, x, b, j)$. Her problem is

$$
V_f^S(a, h, x, b, j) = \max_{a', l} \Bigl\{ U_f^S(c, l, k_y) + \beta\, V_f^S(a', h', x, b, j+1) \Bigr\}
$$

subject to the following budget constraints:

**(i) With children** — if $b \in \{1,2\}$ and $j \in \{b,\, b{+}1,\, b{+}2\}$, then $k=1$ and

$$
c + a' = a\bigl(1+r(1-\tau_k)\bigr) + w\,h\,l\,(1-\tau_p) - T^S(w\,h\,l + ra,\; 1) - w\,d(j+1-b)\,\chi(l).
$$

Furthermore, if $b = j$ then $k_y = 1$.

**(ii) Without children, not retired** — if $b = 0$, or $b \in \{1,2\}$ and $b+2 < j < J_R$, or $b = 2$ and $j = 1$, then $k = 0$ and

$$
c + a' = a\bigl(1+r(1-\tau_k)\bigr) + w\,h\,l\,(1-\tau_p) - T^S(w\,h\,l + ra,\; 0).
$$

**(iii) Retired** — if $j \geq J_R$, then $k = 0$ and

$$
c + a' = a\bigl(1+r(1-\tau_k)\bigr) + p_f^S(x) - T^S(ra,\; 0).
$$

In addition, $h' = G(x, h, l, j)$, and $l \geq 0$, $a' \geq 0$ (with $a' = 0$ if $j = J$).

Here $d(s)$ is the per-child care cost when children are age $s$, and $\chi(l) = \mathbf{1}\{l > 0\}$.

---

## Bellman Equation 3: Married Household

The state for a married couple is $(a, h, x, z, q, b, j)$. Their problem is

$$
V^M(a, h, x, z, q, b, j) = \max_{a', l_f, l_m} \Bigl\{ \bigl[U_f^M(c, l_f, q, k_y) + U_m^M(c, l_m, l_f, q)\bigr] + \beta\, V^M(a', h', x, z, q, b, j+1) \Bigr\}
$$

subject to the following budget constraints:

**(i) With children** — if $b \in \{1,2\}$ and $j \in \{b,\, b{+}1,\, b{+}2\}$, then $k = 1$ and

$$
c + a' = a\bigl(1+r(1-\tau_k)\bigr) + w\bigl(\varpi_m(z,j)\,l_m + h\,l_f\bigr)(1-\tau_p) - T^M\bigl(w\,\varpi_m(z,j)\,l_m + w\,h\,l_f + ra,\; 1\bigr) - w\,d(j{+}1{-}b)\,\chi(l_f).
$$

Furthermore, if $b = j$ then $k_y = 1$.

**(ii) Without children, not retired** — if $b = 0$, or $b \in \{1,2\}$ and $b+2 < j < J_R$, or $b = 2$ and $j = 1$, then $k = 0$ and

$$
c + a' = a\bigl(1+r(1-\tau_k)\bigr) + w\bigl(\varpi_m(z,j)\,l_m + h\,l_f\bigr)(1-\tau_p) - T^M\bigl(w\,\varpi_m(z,j)\,l_m + w\,h\,l_f + ra,\; 0\bigr).
$$

**(iii) Retired** — if $j \geq J_R$, then $k = 0$ and

$$
c + a' = a\bigl(1+r(1-\tau_k)\bigr) + p^M(x, z) - T^M(ra,\; 0).
$$

In addition,

$$
h' = G(x, h, l_f, j),
$$

and $l_m \geq 0$, $l_f \geq 0$, $a' \geq 0$ (with $a' = 0$ if $j = J$).

---

## Key Features of the Bellman Structure

1. **No period-by-period shocks.** All heterogeneity is initial: types $z$, $x$, $q$, $b$ are drawn once at birth. Conditional on types, the life-cycle problem is fully deterministic. There is no shock-realization stage within a period.

2. **Extensive margin for married females.** The utility cost $q$ of joint work, combined with childcare costs $w\,d(s)$ and human capital depreciation $\delta$, creates a non-trivial participation decision: for high enough $q$ it is optimal for only the husband to work.

3. **Endogenous female human capital.** The law of motion $h' = G(x,h,l_f,j)$ means that non-participation today reduces future productivity, making the participation decision inherently dynamic. The human capital transition depends only on whether the female works ($\chi(l) = \mathbf{1}\{l>0\}$), not on hours conditional on participation.

4. **Both intensive and extensive margins.** Hours $l_m$, $l_f$ are continuous controls (intensive margin). The wife's participation ($l_f > 0$ vs. $l_f = 0$) is the extensive margin, governed by comparing household utility under one-earner vs. two-earner configurations. Both husbands and wives choose hours endogenously.

5. **Progressive taxation on households.** Under joint filing, the married female's effective marginal tax rate depends on her husband's income through the convex tax function $T^M(\cdot)$ with $\tau(\tilde{y}) = \zeta_1 + \zeta_2 \log(\tilde{y})$, creating a tax wedge against secondary-earner participation.

6. **Gender-based tax experiments (Section 6).** The paper replaces the progressive functions $T^M, T^S$ with proportional rates $\tau_L$ (on married female labor earnings) and $\tau_H$ (on everyone else), nesting equal treatment ($\tau_L = \tau_H = \tau$) as a special case. Capital income is taxed at $\tau_k^* = \tau_k + \tau$. Two scenarios:
   - **Narrow base:** singles pay $\tau$; married females pay $\tau_L < \tau$; married males pay $\tau_H > \tau$ to balance the budget.
   - **Broad base:** married females pay $\tau_L$; everyone else (married males and all singles) pays $\tau_H$.

   Revenue neutrality is maintained period-by-period by adjusting $\tau_H$.
