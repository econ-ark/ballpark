# Household Bellman Problem — Excerpt from Gornemann, Kuester, Nakajima (2012)

Faithful summary of the household dynamic program in Section 2 of the paper.

## States

**Aggregate state** (post labor-market transitions):

\[
X = (K,\; N,\; Z,\; D,\; \mu),
\]

where \(K\) is capital, \(N\) is employment, \(Z\) is TFP, \(D\) is the monetary-policy shock, and \(\mu\) is the cross-sectional distribution of households.

**Individual state:** \((e,\, s,\, a)\) — employment status \(e \in \{0,1\}\), skill level \(s \in S\), and mutual-fund shares \(a \in A \subseteq \mathbb{R}\).

The paper also defines a **pre-transition** aggregate state \(\tilde{X} = (K, \tilde{N}, Z, D, \tilde{\mu})\), measured at the start of the period before separations and matching occur.

## Timing

1. Households enter the period with state \((\tilde{e}, s, a)\) and observe \(\tilde{X}\).
2. Employed households are separated with probability \(\lambda\).
3. All jobless households (including newly separated) search; matches form with probability \(f(\tilde{X})\). The aggregate state updates to \(X = \hat{G}(\tilde{X})\).
4. Households choose consumption \(c\) and next-period shares \(a'\). Production occurs.
5. New shocks \((Z', D', s')\) are drawn; the economy enters next period at \(\tilde{X}'\).

## Employment Transitions

For a household that is **employed** at the consumption stage, next-period employment probabilities are:

- Stays employed: \(1 - \lambda + \lambda\, f(\tilde{X}')\) — keeps job, or separates but re-matches immediately.
- Becomes unemployed: \(\lambda\bigl(1 - f(\tilde{X}')\bigr)\) — separates and fails to match.

For an **unemployed** household:

- Becomes employed: \(f(\tilde{X}')\).
- Stays unemployed: \(1 - f(\tilde{X}')\).

## Employed Household Bellman (eq. 1)

\[
W(X, 1, s, a) =
\max_{c,\; a' \geq 0}
\left\{
u(c) + \beta\,\mathbb{E}\!\left[
  \bigl(1 - \lambda + \lambda\, f(\tilde{X}')\bigr)\, W(X', 1, s', a')
  + \lambda\bigl(1 - f(\tilde{X}')\bigr)\, W(X', 0, s', a')
\right]
\right\}
\]

subject to the budget constraint

\[
c + p_a(X)\,a' = \bigl(p_a(X) + d_a(X)\bigr)\,a \;+\; w(X)\,s\,\bigl(1 - \tau(X)\bigr).
\]

## Unemployed Household Bellman (eq. 3)

\[
W(X, 0, s, a) =
\max_{c,\; a' \geq 0}
\left\{
u(c) + \beta\,\mathbb{E}\!\left[
  f(\tilde{X}')\, W(X', 1, s', a')
  + \bigl(1 - f(\tilde{X}')\bigr)\, W(X', 0, s', a')
\right]
\right\}
\]

subject to

\[
c + p_a(X)\,a' = \bigl(p_a(X) + d_a(X)\bigr)\,a \;+\; b\,s.
\]

## Preferences

Period utility is CRRA:

\[
u(c) = \frac{c^{1-\sigma}}{1-\sigma}, \qquad \sigma = 1.5.
\]

Labor supply is inelastic: a household works full-time (\(e=1\)) or not at all (\(e=0\)). The time-discount factor is \(\beta = 0.966\).

## Skill Process

There are four discrete skill levels, \(s \in S = \{s_1, s_2, s_3, s_4\}\):

| Level | Value | Interpretation |
|---|---|---|
| \(s_1\) | 0.123 | Low |
| \(s_2\) | 0.421 | Medium |
| \(s_3\) | 1.435 | High |
| \(s_4\) | 34.65 | Super-skilled |

Skills evolve according to a Markov chain with transition matrix \(\pi_{s,s'}\) (Table 2 of the paper):

\[
\pi = \begin{pmatrix}
0.9719 & 0.0275 & 0.0000 & 0.0006 \\
0.0275 & 0.9444 & 0.0275 & 0.0006 \\
0.0000 & 0.0275 & 0.9719 & 0.0006 \\
0.0183 & 0.0183 & 0.0183 & 0.9450
\end{pmatrix}.
\]

The lower three levels are obtained by discretizing an AR(1) for log productivity (Tauchen method). The super-skilled state is calibrated to match U.S. wealth concentration. Skill transitions are drawn at the end of each period; they do not depend on employment status or aggregate state.

## Wage Function

The wage per efficiency unit is a reduced-form function of aggregate output (eq. 39):

\[
\log w(X) - \log \bar{w} = \varepsilon_w \bigl(\log y(X) - \log \bar{y}\bigr), \qquad \varepsilon_w = 0.45,
\]

where \(\bar{w}\) and \(\bar{y}\) are steady-state values. Values of \(\varepsilon_w < 1\) capture wage stickiness.

## Budget Constraint Notation

| Symbol | Meaning |
|---|---|
| \(p_a(X)\) | Ex-dividend mutual-fund share price |
| \(d_a(X)\) | Dividends per share |
| \(w(X)\) | Wage per efficiency unit |
| \(\tau(X)\) | Proportional payroll tax |
| \(b\) | Unemployment benefit per efficiency unit |

The short-sale constraint \(a' \geq 0\) rules out borrowing. The expectation \(\mathbb{E}\) is over \((Z', D', s')\); the household takes as given the laws of motion \(\tilde{X}' = \tilde{G}(X)\) and \(X' = G(X)\).

## Job-Finding Probability and Aggregate Law of Motion

Matches are created by a Cobb–Douglas matching function:

\[
M(\tilde{X}, V) = \gamma\bigl(U(\tilde{X}) + \lambda\, N(\tilde{X})\bigr)^{\alpha}\, V^{1-\alpha},
\]

so the job-finding rate is

\[
f(\tilde{X}) = \frac{M\bigl(\tilde{X},\, V(\tilde{X})\bigr)}{U(\tilde{X}) + \lambda\, N(\tilde{X})},
\]

where vacancies \(V(\tilde{X})\) satisfy a free-entry condition. Three aggregate mappings link the within- and across-period states:

- \(X = \hat{G}(\tilde{X})\): pre-transition to post-transition (within period).
- \(\tilde{X}' = \tilde{G}(X)\): post-transition to start of next period.
- \(X' = G(X) = \hat{G}\bigl(\tilde{G}(X)\bigr)\): composite law of motion.

Employment evolves as \(N = (1-\lambda)\,\tilde{N} + M(\tilde{X}, V)\), and the type distribution \(\mu\) updates through employment transitions and household saving decisions (equations 28–30 of the paper).

## Perceived Law of Motion

The household takes the aggregate laws of motion \(\tilde{X}' = \tilde{G}(X)\) and \(X' = G(X)\) as given. In practice these are approximated numerically using the method of Krusell and Smith (1998): the infinite-dimensional distribution \(\mu\) is summarized by a finite set of moments, and log-linear forecasting rules are estimated from simulated data. The paper does not specify the forecasting-rule functional form in the main text; details are in Appendix B.

## Key Calibration Parameters

From Tables 1–2 of the paper (one period = one quarter):

| Parameter | Value | Description |
|---|---|---|
| \(\sigma\) | 1.5 | Relative risk aversion |
| \(\beta\) | 0.966 | Time-discount factor |
| \(\lambda\) | 0.10 | Exogenous separation rate |
| \(b\) | 0.446 | UI benefit per efficiency unit |
| \(\alpha\) | 0.60 | Matching elasticity (searchers) |
| \(\gamma\) | 0.645 | Matching efficiency |
| \(\bar{w}\) | 0.637 | Steady-state wage per eff. unit |
| \(\varepsilon_w\) | 0.45 | Wage elasticity w.r.t. output |
| \(\rho_D\) | 0.70 | Monetary-shock persistence |
| \(\sigma_D\) | 6.25e-4 | Monetary-shock std. dev. |
| \(\rho_Z\) | 0.95 | TFP persistence |
| \(\sigma_Z\) | 0.006 | TFP std. dev. |
| \(\rho_\Pi\) | 1.20 | Taylor-rule inflation response |
| \(\bar{\Pi}\) | 1.005 | Inflation target (quarterly gross) |

Borrowing constraint: \(a' \geq 0\) (no borrowing).
