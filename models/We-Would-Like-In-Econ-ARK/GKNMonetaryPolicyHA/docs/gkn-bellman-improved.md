# GKN Household Problem: A Stage-Oriented Decomposition

Source: Gornemann, Kuester, and Nakajima (2012), Section 2.

## 1. The Full Problem

A household with employment status \(e \in \{0,1\}\), skill \(s \in S\), and mutual-fund shares \(a \geq 0\) solves

\[
W(X, e, s, a) =
\max_{c,\; a' \geq 0}
\left\{
\frac{c^{1-\sigma}}{1-\sigma}
+ \beta\,\mathbb{E}\!\left[
  \pi^e_{1}(\tilde{X}')\, W(X', 1, s', a')
  + \pi^e_{0}(\tilde{X}')\, W(X', 0, s', a')
\right]
\right\}
\]

subject to

\[
c + p_a(X)\,a' = \bigl(p_a(X) + d_a(X)\bigr)\,a + y(e, s, X),
\]

where \(\pi^e_1, \pi^e_0\) are the employment transition probabilities (defined in Section 4 below) and the expectation is over \((Z', D', s')\).

The aggregate state is \(X = (K, N, Z, D, \mu)\). The paper distinguishes a pre-transition state \(\tilde{X}\) from the post-transition state \(X\); see Section 3.

This section decomposes \(W\) into three sub-value functions — one at each perch — following a backward stage structure analogous to SolvingMicroDSOPs §12–13.

---

## 2. Stage Decomposition: Overview

Working backward from the end of the period:

\[
\boxed{v_{\succ}(e,s,a',X')}
\;\xrightarrow{\;\mathbb{B}\;}\;
\boxed{v(e,s,m,X')}
\;\xrightarrow{\;\mathbb{I}\;}\;
\boxed{v_{\prec}(e_{\text{old}},s_{\text{old}},a,X)}
\]

| Stage | Perch | State | Operation |
|---|---|---|---|
| 3 → 2 | Continuation → Decision | \((e,s,a',X') \to (e,s,m,X')\) | \(\mathbb{B}\): optimize over \(c\) |
| 2 → 1 | Decision → Arrival | \((e,s,m,X') \to (e_{\text{old}},s_{\text{old}},a,X)\) | \(\mathbb{I}\): integrate over shocks |

The full-period operator is \(\mathbb{T} = \mathbb{I} \circ \mathbb{B}\), closed by the identity \(v_{\succ} = v_{\prec}^{\text{next period}}\).

---

## 3. Continuation Perch — \(v_{\succ}(e, s, a', X')\)

**State:** \((e, s, a', X')\) — post-decision employment, skill, chosen shares, and next-period aggregate state.

The continuation value is defined as the value of entering the next period:

\[
v_{\succ}(e, s, a', X') \;\equiv\; v_{\prec}^{\text{next}}(e, s, a', X').
\]

This is the "end-of-period" value function.  At this perch the household has already chosen \(a'\) and all current-period actions are complete.  The mapping to the next period's arrival is a rename: \(a' \to a\), \(X' \to X\), \(e \to e_{\text{old}}\), \(s \to s_{\text{old}}\).

---

## 4. Decision Perch — \(v(e, s, m, X')\)

**State:** \((e, s, m, X')\) — realized employment, skill, market resources, and (post-transition) aggregate state.

**Mover \(\mathbb{B}\)** (backward, from continuation to decision): a pure optimization, no integration.

\[
v(e, s, m, X') = \max_{c \in [0,\, m]}
\left\{
\frac{c^{1-\sigma}}{1-\sigma} + \beta\, v_{\succ}(e, s, m - c, X')
\right\}
\]

**Transition** (decision → continuation):

\[
a' = m - c, \qquad e_{\text{post}} = e, \qquad s_{\text{post}} = s, \qquad X_{\text{post}} = X'.
\]

Employment and skill pass through unchanged — they are not chosen at this stage.

### Solution via EGM

The first-order condition \(c^{-\sigma} = \beta\, v'_{\succ}(e, s, a', X')\) can be inverted:

\[
c^{*}(a') = \bigl(\beta\, v'_{\succ}(e, s, a', X')\bigr)^{-1/\sigma}.
\]

The endogenous grid point for \(m\) is recovered from the budget identity:

\[
m^{*}(a') = a' + c^{*}(a').
\]

The envelope condition delivers the marginal value of resources:

\[
v'(e, s, m, X') = c^{-\sigma}.
\]

---

## 5. Arrival Perch — \(v_{\prec}(e_{\text{old}}, s_{\text{old}}, a, X)\)

**State:** \((e_{\text{old}}, s_{\text{old}}, a, X)\) — beginning-of-period employment, skill, share holdings, and pre-transition aggregate state.

**Mover \(\mathbb{I}\)** (integration, from decision to arrival): expectation over all pre-decision shocks.

\[
v_{\prec}(e_{\text{old}}, s_{\text{old}}, a, X)
= \mathbb{E}_{e, s, Z', D'}\!\Big[\,
v\!\bigl(e,\; s,\; m(e, s, a, X'),\; X'\bigr)
\Big]
\]

### 5.1 Shock draws

| Variable | Draw | Distribution |
|---|---|---|
| \(e\) | Employment status | \(P_e(\cdot \mid e_{\text{old}}, \tilde{X}')\) — see below |
| \(s\) | Skill level | \(\pi_{s_{\text{old}}, \cdot}\) — Markov chain, independent of \(e, X\) |
| \(Z'\) | TFP | AR(1): \(\log Z' = (1-\rho_Z)\log\bar{Z} + \rho_Z\log Z + \varepsilon_Z\) |
| \(D'\) | Monetary shock | AR(1): \(\log D' = \rho_D \log D + \varepsilon_D\) |

### 5.2 Aggregate state transition

After shocks draw, the aggregate state updates:

\[
X' = H(X, Z', D').
\]

In practice \(H\) is the Krusell-Smith log-linear forecasting rule approximating the full law of motion.

### 5.3 Resource formation

Market resources depend on employment status:

\[
m = \bigl(p_a(X') + d_a(X')\bigr)\,a + y(e, s, X'),
\]

where

\[
y(e, s, X') =
\begin{cases}
w(X')\,s\,\bigl(1 - \tau(X')\bigr) & \text{if } e = 1 \text{ (employed)}, \\
b\,s & \text{if } e = 0 \text{ (unemployed)}.
\end{cases}
\]

### 5.4 Shadow marginal value

For EGM in a prior (or outer) problem, the marginal value of shares at the arrival perch is:

\[
v'_{\prec}(e_{\text{old}}, s_{\text{old}}, a, X)
= \mathbb{E}_{e, s, Z', D'}\!\Big[
\bigl(p_a(X') + d_a(X')\bigr)\, v'(e, s, m, X')
\Big].
\]

The return factor \((p_a + d_a)\) enters via the chain rule on the budget constraint.

---

## 6. Employment Transitions

The paper's within-period timing (Figure 1) generates the following transition probabilities, evaluated at the pre-transition aggregate state \(\tilde{X}'\) of the next period.

**From employed** (\(e_{\text{old}} = 1\)):

\[
\Pr(e = 1 \mid e_{\text{old}}=1) = 1 - \lambda + \lambda\,f(\tilde{X}'), \qquad
\Pr(e = 0 \mid e_{\text{old}}=1) = \lambda\bigl(1 - f(\tilde{X}')\bigr).
\]

An employed household is separated with probability \(\lambda\), but a separated household can immediately re-match with probability \(f(\tilde{X}')\).

**From unemployed** (\(e_{\text{old}} = 0\)):

\[
\Pr(e = 1 \mid e_{\text{old}}=0) = f(\tilde{X}'), \qquad
\Pr(e = 0 \mid e_{\text{old}}=0) = 1 - f(\tilde{X}').
\]

### Job-finding rate

\[
f(\tilde{X}) = \frac{\gamma\bigl(U(\tilde{X}) + \lambda N(\tilde{X})\bigr)^{\alpha}\, V(\tilde{X})^{1-\alpha}}{U(\tilde{X}) + \lambda N(\tilde{X})},
\]

where vacancies \(V(\tilde{X})\) satisfy a free-entry condition from the firm side.

---

## 7. Functional Forms and Calibration

### Preferences

\[
u(c) = \frac{c^{1-\sigma}}{1-\sigma}, \qquad \sigma = 1.5, \quad \beta = 0.966.
\]

Labor supply is inelastic.

### Skill grid and transition matrix

Four levels \(s \in \{0.123,\; 0.421,\; 1.435,\; 34.65\}\).  Transition matrix (Table 2):

\[
\pi = \begin{pmatrix}
0.9719 & 0.0275 & 0.0000 & 0.0006 \\
0.0275 & 0.9444 & 0.0275 & 0.0006 \\
0.0000 & 0.0275 & 0.9719 & 0.0006 \\
0.0183 & 0.0183 & 0.0183 & 0.9450
\end{pmatrix}.
\]

### Wage function

\[
\log w(X) - \log \bar{w} = \varepsilon_w\bigl(\log y(X) - \log\bar{y}\bigr), \qquad \varepsilon_w = 0.45,\; \bar{w} = 0.637.
\]

### Other parameters

| Symbol | Value | Description |
|---|---|---|
| \(\lambda\) | 0.10 | Separation rate |
| \(b\) | 0.446 | UI benefit per efficiency unit |
| \(\alpha\) | 0.60 | Matching elasticity |
| \(\gamma\) | 0.645 | Matching efficiency |
| \(\rho_Z\) | 0.95 | TFP persistence |
| \(\sigma_Z\) | 0.006 | TFP std. dev. |
| \(\rho_D\) | 0.70 | Monetary-shock persistence |
| \(\sigma_D\) | 6.25e-4 | Monetary-shock std. dev. |
| \(\rho_\Pi\) | 1.20 | Taylor-rule inflation response |
| \(\bar{\Pi}\) | 1.005 | Inflation target (quarterly gross) |

Borrowing constraint: \(a' \geq 0\).
