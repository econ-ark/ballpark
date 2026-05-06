# Bellman excerpt — Wong (2021), "Refinancing and the Transmission of Monetary Policy to Consumption"

> Standalone modular-DDSL Bellman statement of the household stage in Wong (2021).
> Scope: one (interior) working-age stage of the life-cycle problem. Retirement and the terminal bequest age are separate stages, stubbed at the bottom.
> Source of truth: `Arlene-Wong-refinancing.mmd` §4, Eqs. (5)–(17). The `_summary.ipynb` §"The Model" is aligned with this excerpt and may be read as its verbose companion.
> Intended consumer: [Matsya](https://github.com/econ-ark/matsya), `--session PopMP`.

---

## 1. Symbol table

### 1a. Indices

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $j$ | index | $\mathbb{N}$ | Household identifier (continuum). |
| $a$ | index / state | $\{1, \ldots, T\}$ | Age in years; period $a=1$ corresponds to calendar age 25. |
| $t$ | index | $\mathbb{N}$ | Calendar period. Model period is annual. |
| $T$ | parameter | $\mathbb{N}$ | Maximum life length. Calibrated $T = 61$ (calendar age 25–85). |
| $T_y$ | parameter | $\mathbb{N}$ | Last working-age period. Calibrated $T_y = 40$. |
| $d(a)$ | derived | $\{1, \ldots, T\}$ | Remaining-life mortgage duration for an agent originating at age $a$: $d(a) = T - a$. |

### 1b. Household states at the arrival perch $\prec$

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $s_{j, a-1, t-1}$ | state | $[-\underline{s},\, +\infty)$ | Short-term liquid asset balance carried into period $t$. |
| $h^{\mathrm{own}}_{j, a-1, t-1}$ | state | $[0,\, +\infty)$ | Stock of owned housing carried in (before within-period depreciation). |
| $b_{j, a-1, t-1}$ | state | $[0,\, +\infty)$ | Outstanding mortgage balance carried in. |
| $R_{j, a-1, t-1}$ | state | $(0,\, 1)$ | Fixed coupon on the existing mortgage. Household-specific, not a market rate. |
| $\eta_{j, a-1, t-1}$ | state | $\mathbb{R}$ | Persistent idiosyncratic component of log earnings carried in. |

### 1c. Aggregate state at the arrival perch

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $S_{t-1}$ | state | $\mathbb{R}^{3}$ | Lagged aggregate state $(\log y_{t-1},\, \log p_{t-1},\, r_{t-1})$. |

### 1d. Shocks resolved between arrival $\prec$ and decision $\circ$

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $u_t$ | shock | $\mathcal{N}(0,\, V)\ \subset \mathbb{R}^{3}$ | Aggregate VAR innovation. In practice discretized (Tauchen, 18 states). |
| $\psi_{jt}$ | shock | $\mathcal{N}(0,\, \sigma_\eta^{2})$ | Idiosyncratic persistent-earnings innovation. |

### 1e. Realized derived quantities at the decision perch $\circ$

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $S_t$ | derived | $\mathbb{R}^{3}$ | Current aggregate state $(\log y_t,\, \log p_t,\, r_t) = A_0 + A_1 S_{t-1} + u_t$. |
| $\eta_{j a t}$ | derived | $\mathbb{R}$ | Persistent earnings component: $\eta_{j a t} = \rho_\eta\, \eta_{j, a-1, t-1} + \psi_{j t}$. |
| $y_{j a t}$ | derived | $\mathbb{R}_{+}$ | Labor income: $\log y_{j a t} = \chi_a + \eta_{j a t} + \phi_a(y_t)$ when working; deterministic retirement transfer when $a > T_y$. |
| $r_t^{d(a)}$ | derived | $\mathbb{R}$ | Duration-$d(a)$ mortgage rate: $r_t^{d(a)} = f^{d(a)}(S_t) = a_0^{d(a)} + a_1^{d(a)} r_t + a_2^{d(a)} \log y_t$. |
| $p_t^{r}$ | derived | $\mathbb{R}_{+}$ | Rental rate: $\log p_t^{r} = \alpha_0 + \alpha_1 r_t + \alpha_2 \log y_t + \alpha_3 \log p_t$. |
| $p_t$ | derived | $\mathbb{R}_{+}$ | House price: $\exp(\log p_t)$, a component of $S_t$. |
| $M_{j a t}$ | derived | $\mathbb{R}_{+}$ | Scheduled mortgage payment (mechanical annuity from $b, R, d(a)$; see §4). Defined only in the `no-refi` regime. |

### 1f. Controls at the decision perch $\circ$

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $\mathrm{reg}_{j a t}$ | discrete control | $\{\mathrm{rent},\, \mathrm{no\text{-}refi},\, \mathrm{refi},\, \mathrm{purchase}\}$ | Housing-tenure / mortgage-adjustment regime. |
| $c_{j a t}$ | continuous control | $\mathbb{R}_{+}$ | Non-durable consumption (all regimes). |
| $h^{\mathrm{rent}}_{j a t}$ | continuous control | $\mathbb{R}_{+}$ | Rented housing services (rent regime only). |
| $h^{\mathrm{own}}_{j a t}$ | continuous control | $\mathbb{R}_{+}$ | End-of-period owned housing stock (purchase regime chooses freely; carried through depreciated in `no-refi`/`refi`; zero in `rent`). |
| $s_{j a t}$ | continuous control | $[-\underline{s},\, +\infty)$ | End-of-period short-term asset. |
| $b_{j a t}$ | continuous control | $[0,\, +\infty)$ | End-of-period mortgage balance (free in `refi` / `purchase`; mechanical in `no-refi`; zero in `rent`). |

### 1g. States at the continuation perch $\succ$

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $s_{j a t}$ | state | $[-\underline{s},\, +\infty)$ | Short-term asset (carried to next period). |
| $h^{\mathrm{own}}_{j a t}$ | state | $[0,\, +\infty)$ | Owned housing stock (carried to next period; will depreciate at arrival of $t+1$). |
| $b_{j a t}$ | state | $[0,\, +\infty)$ | Mortgage balance carried forward. |
| $R_{j a t}$ | state | $(0,\, 1)$ | Coupon carried forward (reset under `refi`/`purchase`; passed through under `no-refi`; undefined after `rent`). |
| $\eta_{j a t}$ | state | $\mathbb{R}$ | Persistent earnings component. |
| $S_t$ | state | $\mathbb{R}^{3}$ | Aggregate state (becomes lagged state at next arrival). |

### 1h. Parameters

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $\beta$ | parameter | $(0, 1)$ | Discount factor. Calibrated $0.962$. |
| $\sigma$ | parameter | $\mathbb{R}_{+}$ | CRRA curvature. |
| $\alpha$ | parameter | $(0, 1)$ | Cobb-Douglas share on non-durable consumption. Calibrated $0.88$. |
| $\delta$ | parameter | $[0, 1]$ | Housing depreciation rate. Calibrated $0.03$. |
| $\phi$ | parameter | $[0, 1]$ | Minimum equity / down-payment fraction. Calibrated $0.20$. |
| $\underline{s}$ | parameter | $\mathbb{R}_{+}$ | Short-term borrowing limit (absolute value). Calibrated $0$. |
| $B$ | parameter | $\mathbb{R}_{+}$ | Warm-glow bequest weight. Calibrated $\approx 2$. |
| $\kappa^{\mathrm{new}}$ | parameter | $\mathbb{R}_{+}$ | Proportional new-home transaction cost. Calibrated $0.05$. |
| $F_f^{\mathrm{refi}}$ | parameter | $\mathbb{R}_{+}$ | Fixed refinancing cost. Calibrated $\approx \$2{,}100$. |
| $F_v^{\mathrm{refi}}$ | parameter | $\mathbb{R}_{+}$ | Variable refinancing cost (fraction of balance). Calibrated $\approx 0$ in baseline. |
| $\pi_a$ | parameter | $[0, 1]$ | Age-$a$ survival probability. From U.S. SSA life tables. |
| $\chi_a$ | parameter | $\mathbb{R}$ | Deterministic age profile of log earnings. From Guvenen et al. (2015). |
| $\phi_a$ | parameter | $\mathbb{R}$ | Age-specific loading on aggregate income in the earnings equation. |
| $\rho_\eta$ | parameter | $(0, 1)$ | AR(1) persistence of idiosyncratic earnings. Calibrated $0.91$. |
| $\sigma_\eta$ | parameter | $\mathbb{R}_{+}$ | Idiosyncratic earnings innovation s.d. Calibrated $0.21$. |
| $A_0,\, A_1$ | parameter | $\mathbb{R}^3,\, \mathbb{R}^{3\times 3}$ | Aggregate VAR intercept and coefficient matrix. |
| $V$ | parameter | $\mathbb{R}^{3\times 3}$ | Aggregate-innovation covariance. |
| $a_0^{d},\, a_1^{d},\, a_2^{d}$ | parameter | $\mathbb{R}$ | Duration-$d$ mortgage-rate loadings in $f^d(\cdot)$. Estimated for $d \in \{1, 15, 30\}$. |
| $\alpha_0,\, \alpha_1,\, \alpha_2,\, \alpha_3$ | parameter | $\mathbb{R}$ | Rental-rate loadings in $f^{pr}(\cdot)$. |

### 1i. Value functions

| Symbol | Role | Description |
|---|---|---|
| $V_{j a t}$ | value | Pre-regime-choice age-$a$ value: the $\max$ over the four regime-specific values. |
| $V_{j a t}^{\mathrm{rent}}$ | value | Regime-conditional value: rent. |
| $V_{j a t}^{\mathrm{own\&no\text{-}refi}}$ | value | Regime-conditional value: own without refinancing. |
| $V_{j a t}^{\mathrm{own\&refi}}$ | value | Regime-conditional value: own and refinance. |
| $V_{j a t}^{\mathrm{purchase}}$ | value | Regime-conditional value: purchase a new home. |
| $V^{\mathrm{beq}}$ | value | Terminal warm-glow bequest: $V^{\mathrm{beq}}(W) = B\,(W-1)^{1-\sigma}/(1-\sigma)$. |
| $\tilde V$ | value | Survival-weighted continuation: $\tilde V = \pi_a V + (1-\pi_a) V^{\mathrm{beq}}$. |

---

## 2. Timing convention (one period, interior working-age stage)

Numbered steps within period $t$ at age $a$:

1. **Arrival ($\prec$).** Household state is $(s_{j, a-1, t-1},\, h^{\mathrm{own}}_{j, a-1, t-1},\, b_{j, a-1, t-1},\, R_{j, a-1, t-1},\, \eta_{j, a-1, t-1})$; aggregate state is $S_{t-1}$.
2. **Shock block.** $u_t$ is drawn; $S_t = A_0 + A_1 S_{t-1} + u_t$ is realized. $\psi_{jt}$ is drawn; $\eta_{jat}$ and $y_{jat}$ are realized. $r_t^{d(a)} = f^{d(a)}(S_t)$ and $p_t^r = \exp f^{pr}(S_t)$ are implied.
3. **Decision ($\circ$).** Household observes the full realized state $(a,\, S_t,\, y_{jat},\, s_{j, a-1, t-1},\, h^{\mathrm{own}}_{j, a-1, t-1},\, b_{j, a-1, t-1},\, R_{j, a-1, t-1},\, \eta_{jat})$ and chooses $\mathrm{reg}_{jat} \in \{\mathrm{rent},\, \mathrm{no\text{-}refi},\, \mathrm{refi},\, \mathrm{purchase}\}$ together with the continuous controls conditional on the regime.
4. **Mechanical deduction.** Under `no-refi`, $M_{jat}$ is computed from $(b_{j, a-1, t-1},\, R_{j, a-1, t-1},\, d(a))$ via the annuity identity (§4); flow utility is paid; budget constraint closes.
5. **Post-state update ($\succ$).** End-of-period $(s_{jat},\, h^{\mathrm{own}}_{jat},\, b_{jat},\, R_{jat})$ is set per the regime's law of motion. Survival $\pi_a$ resolves.
6. **Continuation.** With probability $\pi_a$ the household enters period $t+1$ at age $a+1$ with post-state as new arrival state; with probability $1-\pi_a$ the terminal bequest $V^{\mathrm{beq}}$ applies to $W_{jat}$.

---

## 3. Perch decomposition

### 3a. Arrival perch $\prec$

- **States carried:** $(s_{j, a-1, t-1},\, h^{\mathrm{own}}_{j, a-1, t-1},\, b_{j, a-1, t-1},\, R_{j, a-1, t-1},\, \eta_{j, a-1, t-1},\, S_{t-1})$, plus the age index $a$.
- **Value function:** $V^{\prec}_{jat}$, the pre-shock expected value.
- **Control:** none.

### 3b. Decision perch $\circ$

- **States carried:** all arrival-perch states plus the realized shock block $(S_t,\, \eta_{jat},\, y_{jat},\, r_t^{d(a)},\, p_t^r,\, p_t)$. Everything needed to evaluate the four regime-conditional value functions is in this state.
- **Value function:** $V_{jat}(z_{jat}) = \max\{V_{jat}^{\mathrm{rent}},\, V_{jat}^{\mathrm{own\&no\text{-}refi}},\, V_{jat}^{\mathrm{own\&refi}},\, V_{jat}^{\mathrm{purchase}}\}$.
- **Control:** $(\mathrm{reg}_{jat},\, c_{jat},\, h^{\mathrm{rent}}_{jat},\, h^{\mathrm{own}}_{jat},\, s_{jat},\, b_{jat})$, with several components degenerate or unused depending on the regime.

### 3c. Continuation perch $\succ$

- **States carried:** $(s_{jat},\, h^{\mathrm{own}}_{jat},\, b_{jat},\, R_{jat},\, \eta_{jat},\, S_t)$, plus the age index $a$.
- **Value function:** $V^{\succ}_{jat}$, the end-of-period expected continuation value.
- **Control:** none.

### 3d. Within-stage transitions

- **$\mathrm{g}_{\prec\circ}$: arrival → decision.** Draws $(u_t,\, \psi_{jt})$, computes $(S_t,\, \eta_{jat},\, y_{jat})$ from the VAR and the earnings recursion, then evaluates the reduced-form mortgage-rate and rental-rate functions to get $(r_t^{d(a)},\, p_t^r)$. This is a **non-trivial** transition (it is where all period-$t$ shocks are resolved).
- **$\mathrm{g}_{\circ\succ}$: decision → continuation.** Regime-contingent post-state identity:

  - `rent`: $s_{jat} = $ chosen; $h^{\mathrm{own}}_{jat} = 0$; $b_{jat} = 0$; $R_{jat} = \varnothing$.
  - `no-refi`: $s_{jat} = $ chosen; $h^{\mathrm{own}}_{jat} = (1-\delta) h^{\mathrm{own}}_{j, a-1, t-1}$; $b_{jat} = b_{j, a-1, t-1}(1 + R_{j, a-1, t-1}) - M_{jat}$; $R_{jat} = R_{j, a-1, t-1}$.
  - `refi`: $s_{jat},\, b_{jat} = $ chosen; $h^{\mathrm{own}}_{jat} = (1-\delta) h^{\mathrm{own}}_{j, a-1, t-1}$; $R_{jat} = r_t^{d(a)}$.
  - `purchase`: $s_{jat},\, h^{\mathrm{own}}_{jat},\, b_{jat} = $ chosen; $R_{jat} = r_t^{d(a)}$.

  Because $R_{jat}$ is set state-contingently by the discrete choice (market rate under `refi`/`purchase`, carried under `no-refi`, undefined after `rent`), $\mathrm{g}_{\circ\succ}$ has a **state-contingent shock / transition structure** — one of CONTRIBUTING.md's three canonical workaround categories.

### 3e. Movers

- **Backward mover $\mathbb{B}$: continuation → decision.** Performs the constrained $\max$ over the four-regime discrete choice stacked with the regime-conditional continuous choice:

$$
V_{jat}(z_{jat}) = \mathbb{B}\bigl[V^{\succ}_{jat}\bigr](z_{jat}) = \max_{\mathrm{reg},\, c,\, h^{\mathrm{rent}},\, h^{\mathrm{own}\prime},\, s',\, b'}\; u(c,\, h_{jat}(\mathrm{reg})) + \beta\, E\bigl[\tilde V^{\succ}_{jat}\bigr],
$$

subject to the regime-specific budget and constraint blocks listed in §5. $\mathbb{B}$ is a two-stage operator (discrete then continuous), but the decomposition is conventional.

- **Arrival / forward mover $\mathbb{I}$: decision → arrival.** Integrates over the next-period shock block $(u_{t+1},\, \psi_{j, t+1})$:

$$
V^{\prec}_{j, a+1, t+1}\bigl(s,\, h^{\mathrm{own}},\, b,\, R,\, \eta,\, S\bigr) = \mathbb{I}\bigl[V_{j, a+1, t+1}\bigr] = E\bigl[\, V_{j, a+1, t+1}\bigl(a+1,\, A_0 + A_1 S + u_{t+1},\, y_{j, a+1, t+1},\, (s,\, h^{\mathrm{own}},\, b,\, R)\bigr)\,\bigr].
$$

$\mathbb{I}$ is non-trivial here (shocks are resolved every period). Survival $\pi_a$ is composed with $\mathbb{I}$ via the $\tilde V$ operator.

### 3f. Stage operator

$$
\mathbb{T} = \mathbb{I} \circ \mathbb{B}.
$$

Applied once per age, this yields the age-$a$ recursive problem. The life cycle is the composition $\mathbb{T}_T \circ \mathbb{T}_{T-1} \circ \cdots \circ \mathbb{T}_1$ with terminal condition $V^{\prec}_{j, T+1, t+1} \equiv V^{\mathrm{beq}}$. Retirement is implemented as a separate family of stages ($a > T_y$) in which the earnings process is replaced by a deterministic transfer — no other perch or mover changes.

---

## 4. Mechanical deduction: the mortgage annuity

$M_{jat}$ is **not a choice variable**. It is the level annuity satisfying

$$
b_{jat} = M_{jat} \sum_{k=1}^{d(a)} \frac{1}{(1 + R_{jat})^{k}}
\;\;\Longrightarrow\;\;
M_{jat} = b_{jat} \left[\sum_{k=1}^{d(a)} \frac{1}{(1 + R_{jat})^{k}}\right]^{-1}.
$$

In the `no-refi` regime, $(b_{jat},\, R_{jat}) = (b_{j, a-1, t-1},\, R_{j, a-1, t-1})$ and the residual balance updates as $b_{j, a+1, t+1} = b_{jat}(1 + R_{jat}) - M_{jat}$. In the `refi` and `purchase` regimes $M_{jat}$ is not evaluated (the full balance is paid off and a fresh loan is originated). In the `rent` regime $M_{jat}$ is not evaluated (the full balance is paid off via the budget constraint and no new loan is originated).

In a dolo-plus YAML this should be flagged inline as a `# workaround: mechanical (non-optimized) deduction` when the balance-and-payment block is encoded.

---

## 5. Explicit utility, bequest, and regime-conditional Bellman equations

### 5a. Utility and bequest

$$
u(c,\, h) = \frac{\left(c^{\alpha}\, h^{1-\alpha}\right)^{1-\sigma} - 1}{1 - \sigma},
\qquad
V^{\mathrm{beq}}(W) = B\, \frac{(W - 1)^{1-\sigma}}{1-\sigma}.
$$

Upon death, $W_{jat} = (1-\delta)\, p_t\, h^{\mathrm{own}}_{j, a-1, t-1} + (1+r_t)\, s_{j, a-1, t-1} - b_{j, a-1, t-1}(1 + R_{j, a-1, t-1})$.

### 5b. Rent regime (Wong Eq. 12)

$$
V_{jat}^{\mathrm{rent}}(z_{jat}) = \max_{c,\, h^{\mathrm{rent}},\, s'}\; u(c,\, h^{\mathrm{rent}}) + \beta\, E[\tilde V_{j, a+1, t+1}],
$$

s.t.

$$
c + s' + p_t^r\, h^{\mathrm{rent}} = y_{jat} + (1-\delta) p_t\, h^{\mathrm{own}}_{j, a-1, t-1} + (1 + r_t)\, s_{j, a-1, t-1} - b_{j, a-1, t-1}(1 + R_{j, a-1, t-1}),
$$

$h^{\mathrm{own}\prime} = 0,\;\; b' = 0,\;\; s' \geq -\underline{s}$.

### 5c. Own & no-refi regime (Wong Eq. 15)

$$
V_{jat}^{\mathrm{own\&no\text{-}refi}}(z_{jat}) = \max_{c,\, s'}\; u\bigl(c,\, (1-\delta) h^{\mathrm{own}}_{j, a-1, t-1}\bigr) + \beta\, E[\tilde V_{j, a+1, t+1}],
$$

s.t.

$$
\begin{aligned}
c + s' &= y_{jat} + (1+r_t)\, s_{j, a-1, t-1} - M_{jat}, \\
h^{\mathrm{own}\prime} &= (1-\delta) h^{\mathrm{own}}_{j, a-1, t-1}, \\
b' &= b_{j, a-1, t-1}(1 + R_{j, a-1, t-1}) - M_{jat}, \\
R' &= R_{j, a-1, t-1}, \;\; s' \geq -\underline{s}.
\end{aligned}
$$

### 5d. Own & refi regime (Wong Eq. 14)

$$
V_{jat}^{\mathrm{own\&refi}}(z_{jat}) = \max_{c,\, s',\, b'}\; u\bigl(c,\, (1-\delta) h^{\mathrm{own}}_{j, a-1, t-1}\bigr) + \beta\, E[\tilde V_{j, a+1, t+1}],
$$

s.t.

$$
\begin{aligned}
c + s' - b' + F^{\mathrm{refi}} &= y_{jat} + (1+r_t)\, s_{j, a-1, t-1} - b_{j, a-1, t-1}(1 + R_{j, a-1, t-1}), \\
h^{\mathrm{own}\prime} &= (1-\delta) h^{\mathrm{own}}_{j, a-1, t-1}, \\
b' &\leq (1-\phi)\, p_t\, h^{\mathrm{own}\prime}, \\
R' &= r_t^{d(a)},\;\; s' \geq -\underline{s}, \\
F^{\mathrm{refi}} &= F_f^{\mathrm{refi}} + F_v^{\mathrm{refi}}\, b'.
\end{aligned}
$$

### 5e. Purchase regime (Wong Eq. 13)

$$
V_{jat}^{\mathrm{purchase}}(z_{jat}) = \max_{c,\, s',\, h^{\mathrm{own}\prime},\, b'}\; u(c,\, h^{\mathrm{own}\prime}) + \beta\, E[\tilde V_{j, a+1, t+1}],
$$

s.t.

$$
\begin{aligned}
c + s' + p_t\, h^{\mathrm{own}\prime} - b' + F^{\mathrm{new}} &= y_{jat} + (1-\delta) p_t\, h^{\mathrm{own}}_{j, a-1, t-1} + (1+r_t)\, s_{j, a-1, t-1} - b_{j, a-1, t-1}(1 + R_{j, a-1, t-1}), \\
b' &\leq (1-\phi)\, p_t\, h^{\mathrm{own}\prime}, \\
R' &= r_t^{d(a)},\;\; s' \geq -\underline{s}, \\
F^{\mathrm{new}} &= \kappa^{\mathrm{new}}\, p_t\, h^{\mathrm{own}\prime}.
\end{aligned}
$$

### 5f. Pre-regime-choice value

$$
V_{jat}(z_{jat}) = \max\!\left\{ V_{jat}^{\mathrm{rent}},\; V_{jat}^{\mathrm{own\&no\text{-}refi}},\; V_{jat}^{\mathrm{own\&refi}},\; V_{jat}^{\mathrm{purchase}} \right\}\!(z_{jat}),
$$

with continuation

$$
\tilde V_{j, a+1, t+1} = \pi_a\, V_{j, a+1, t+1} + (1 - \pi_a)\, V^{\mathrm{beq}}(W_{j, a+1, t+1}).
$$

---

## 6. Notes for the formalizer (known workarounds)

- **State-contingent coupon update.** $R'$ is $r_t^{d(a)}$ under `refi`/`purchase` and $R_{j, a-1, t-1}$ under `no-refi`. This is a **state-contingent shock / transition** (CONTRIBUTING.md workaround category 3) and should be flagged inline in any dolo-plus YAML.
- **$M_{jat}$ as a mechanical deduction.** See §4. Flag as workaround category 1.
- **$r_t^{d(a)}$ and $p_t^r$ as reduced-form functions of $S_t$.** These are not additional state variables; they are tabulated on the $S_t$ grid. Encode as deterministic derived quantities, not as independent shocks.
- **Aggregate block as 18-state Markov chain.** Encode $S_t$ via its discretized transition matrix, not as continuous Gaussian innovations. Keeping the continuous form in the Bellman statement is fine; the YAML should use the discrete form.
- **Degenerate elements of the post-state.** Under `rent`, $(h^{\mathrm{own}\prime},\, b',\, R')$ collapse to $(0,\, 0,\, \varnothing)$. Label $R'$ as degenerate under `rent` explicitly in the perch table; do not omit it.
- **EGM applicability.** The utility kernel $u(c, h) = (c^\alpha h^{1-\alpha})^{1-\sigma}/(1-\sigma) - 1/(1-\sigma)$ is invertible in $c$ for each regime. The interior-FOC in $c$ is standard CRRA once housing services are fixed within a regime (trivially in `rent` where $h^{\mathrm{rent}}$ is chosen, and with $h = (1-\delta) h^{\mathrm{own}}_{j, a-1, t-1}$ fixed in `no-refi` and `refi`). The `purchase` regime has $h^{\mathrm{own}\prime}$ as a simultaneous choice with $c$, so a full EGM pass requires solving a nested inner problem; discuss this in the SMD-polished follow-up.

---

## 7. Out-of-scope stages

The following life-cycle stages are separate and are **not** specified in this excerpt:

- **Retirement stages $a \in \{T_y + 1,\, \ldots,\, T\}$.** Structurally identical to the working-age stage above but with labor income replaced by a deterministic Social Security transfer (modeled as in Guvenen and Smith 2014).
- **Terminal age $a = T$.** The continuation collapses to $V^{\mathrm{beq}}$ with probability 1.
- **Initialization at $a = 1$.** Initial distribution of $(s,\, h^{\mathrm{own}},\, b,\, R,\, \eta)$ calibrated to the 2004 SCF 20–29 age bracket.
