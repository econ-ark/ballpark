# Bellman Equations in Guner, Kaygusuz, and Ventura (2012)

*Excerpted from: "Taxing Women: A Macroeconomic Analysis," Journal of Monetary Economics 59 (2012), 111–128, Sections 3–4.*

## State Variables and Notation

| Symbol | Meaning |
|--------|---------|
| $a$ | household assets |
| $z \in Z$ | male intrinsic type (permanent) |
| $x \in X$ | female intrinsic type (permanent) |
| $h \in H$ | female human capital (endogenous) |
| $q \in Q$ | utility cost of joint work (drawn once at start of marriage) |
| $b \in \{0,1,2\}$ | childbearing status (0 = none, 1 = early, 2 = late) |
| $j \in \{1,\ldots,J\}$ | age; retirement at $J_R$ |
| $k \in \{0,1\}$ | children present in household (determined by $b$ and $j$) |
| $k_y \in \{0,1\}$ | young (age-1) children present |

## Prices and Tax Parameters

| Symbol | Meaning |
|--------|---------|
| $w$ | competitive wage rate |
| $r$ | net return on assets ($r = R - \delta_k$) |
| $\tau_k$ | capital income tax rate |
| $\tau_p$ | payroll tax rate |
| $T^S(I, k)$, $T^M(I, k)$ | income tax functions for singles and married households |

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

where $\gamma > 0$ is the intertemporal elasticity of labor supply, $\varphi$ controls the disutility of work, $\kappa$ is the fixed time cost of young children for females, and consumption $c$ is a public good within the household.

## Female Human Capital Accumulation

Female productivity evolves endogenously according to

$$
h' = G(x, h, l, j) = \exp\!\bigl[\ln h + a_j^x\,\chi(l) - \delta\,(1 - \chi(l))\bigr],
$$

where $a_j^x$ is an age- and type-specific growth factor conditional on working, $\delta$ is the depreciation rate from non-participation, and $\chi(l) = \mathbf{1}\{l > 0\}$.

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

1. **Extensive margin for married females.** The utility cost $q$ of joint work, combined with childcare costs $w\,d(s)$ and human capital depreciation $\delta$, creates a non-trivial participation decision: for high enough $q$ it is optimal for only the husband to work.

2. **Endogenous female human capital.** The law of motion $h' = G(x,h,l_f,j)$ means that non-participation today reduces future productivity, making the participation decision inherently dynamic.

3. **Progressive taxation on households.** Under joint filing, the married female's effective marginal tax rate depends on her husband's income through the convex tax function $T^M(\cdot)$, creating a tax wedge against secondary-earner participation.

4. **Gender-based tax experiments.** The paper replaces the progressive functions $T^M, T^S$ with proportional rates $\tau_H$ (on males/other) and $\tau_L$ (on married females), nesting equal treatment ($\tau_L = \tau_H$) as a special case, to evaluate the effects of differential taxation.
