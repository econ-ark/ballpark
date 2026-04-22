# HKS (2018) — Bellman Excerpt 

Canonical modular-DDSL statement of the household problem in Hubmer, Krusell, and Smith (2018), *Sources of U.S. Wealth Inequality: Past, Present, and Future* (working-paper title: *A Comprehensive Quantitative Theory of the U.S. Wealth Distribution*). This file is the single reference a formalizer (human or matsya) should read first.

Full-form excerpts and paper-supported calibration tables live in `source/HKS_bellman_excerpt.md` (faithful mathematical excerpt, including the Table-8 portfolio schedules) and `source/HKS_bellman_stages.md` (long-form stage narrative). This file is the synthesis intended as input to the dolo-plus draft.

---

## 1. Purpose and scope

- **Scope of the YAML deliverable:** one household's within-period problem, partial equilibrium, steady state. Aggregate prices $(w, r, T, \tilde\tau)$ and policy schedules $(\tau(\cdot), r^X(\cdot), \sigma^X(\cdot), \psi(\cdot))$ are taken as given.
- **Out of scope for the YAML:** general-equilibrium capital-market clearing; transition experiments with time-varying $\sigma^P_t, \sigma^T_t, \kappa_t, \bar r_{c,t}, \tilde\tau_t, \tau_t(\cdot)$; four-asset-class portfolio construction (summarized by the reduced-form $r^X(a), \sigma^X(a)$).
- **Paper economics fully specified.** The open issues in Section 7 below are dolo-plus-spec representation gaps, not paper-understanding gaps; see `verification.md` for that distinction.

---

## 2. Symbol table

Every symbol that appears in the Bellman equation, transitions, or mover blocks below — or in the paper objects referenced by them.

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $x_t$ | state | $\mathbb{R}_+$ | Cash-on-hand at the consumption decision perch. |
| $a_{t+1}$ | control | $[\underline{a}, x_t]$ | End-of-period asset position; the only endogenous choice. |
| $c_t$ | derived | $\mathbb{R}_+$ | Consumption; $c_t = x_t - a_{t+1}$. |
| $p_t$ | state | $\mathbb{R}$ | Persistent earnings component; Gaussian AR(1). |
| $\beta_t$ | state | $(0,1)$ | Stochastic discount factor; Gaussian AR(1). |
| $\nu_t$ | shock | $\mathbb{R}$ | Transitory earnings shock; $N(0, (\sigma^T_t)^2)$, i.i.d. |
| $\eta_t$ | shock | $\mathbb{R}$ | Idiosyncratic return shock; $N(0,1)$, i.i.d. |
| $\epsilon^p_t, \epsilon^\beta_t$ | shock | $\mathbb{R}$ | Standard-normal innovations driving the $p$ and $\beta$ AR(1)s. |
| $y_t$ | derived | $\mathbb{R}$ | Ordinary gross income; taxed by $\tau_t(\cdot)$. |
| $\tilde y_t$ | derived | $\mathbb{R}$ | Mean-zero stochastic capital-income component; taxed flat at $\tilde\tau_t$. |
| $l_t(p, \nu)$ | derived | $\mathbb{R}_+$ | Labour supply in efficiency units; $l_t = \psi_t(p)\exp(\nu)$. |
| $V_t$ | value | $\mathbb{R}$ | Value function at the period decision perch. |
| $\underline{a}$ | parameter | $\mathbb{R}$ | Exogenous borrowing limit (benchmark $-0.22$). |
| $\gamma$ | parameter | $\mathbb{R}_+$ | CRRA coefficient (benchmark $1.5$). |
| $\chi$ | parameter | $[0,1]$ | Probability of the zero-earnings state (benchmark $0.075$). |
| $\rho_P, \mu_P, \sigma^P_t$ | parameter | $(0,1), \mathbb{R}, \mathbb{R}_+$ | $p_t$ AR(1) coefficients; $\sigma^P_t$ time-varying. |
| $\rho_\beta, \mu_\beta, \sigma_\beta$ | parameter | $(0,1), (0,1), \mathbb{R}_+$ | $\beta_t$ AR(1) coefficients (benchmark $0.992, 0.944, 0.0006$). |
| $\kappa_t$ | parameter | $\mathbb{R}_+$ | Pareto tail shape for top earnings; time-varying. |
| $w_t$ | aggregate | $\mathbb{R}_+$ | Wage per efficiency unit; from firm FOCs. |
| $r_t$ | aggregate | $\mathbb{R}$ | Aggregate return component; from firm FOCs net of depreciation. |
| $T_t$ | aggregate | $\mathbb{R}$ | Uniform lump-sum transfer; $\lambda \times$ aggregate tax revenue, $\lambda = 0.6$. |
| $\tau_t(\cdot)$ | aggregate | $\mathbb{R} \to \mathbb{R}$ | Nonlinear progressive income tax; 11-bracket step function (PS 2007). |
| $\tilde\tau_t$ | aggregate | $[0,1]$ | Flat tax on $\tilde y$; average effective capital gains rate. |
| $r^X_t(\cdot)$ | aggregate | $\mathbb{R} \to \mathbb{R}$ | Mean excess return as a function of wealth; 4-class portfolio sum (Bach 2015). |
| $\sigma^X(\cdot)$ | aggregate | $\mathbb{R} \to \mathbb{R}_+$ | Idiosyncratic return std dev as a function of wealth. |
| $\psi_t(\cdot)$ | aggregate | $\mathbb{R} \to \mathbb{R}_+$ | Persistent-component-to-efficiency-units map; log-normal below P90, Pareto($\kappa_t$) above. |

---

## 3. Timing convention (within one period)

Fix a period $t$ at the household's decision perch.

1. Household enters with $x_t$ (from the previous period's transition), and knows $(p_t, \beta_t)$.
2. Household chooses $a_{t+1} \in [\underline{a}, x_t]$, implying $c_t = x_t - a_{t+1}$.
3. Persistent states transition: $p_{t+1} \sim \Gamma_p(\cdot \mid p_t)$, $\beta_{t+1} \sim \Gamma_\beta(\cdot \mid \beta_t)$.
4. Transitory shocks realize: $\nu_{t+1} \sim N(0, (\sigma^T_{t+1})^2)$; $\eta_{t+1} \sim N(0,1)$; zero-earnings state with probability $\chi$ independently of $(p_{t+1}, \nu_{t+1})$.
5. Income components and $x_{t+1}$ form per the transition equations in Section 5.

All randomness is between the period's decision and next period's decision; there are no within-stage shocks at the consumption perch itself.

---

## 4. Two-stage decomposition

Each period is decomposed into two stages composed in sequence. The consumption stage contains the only decision; the shock-resolution stage contains all four shocks.

$$
\text{Period}_t = \underbrace{\text{Consumption stage}}_{\text{decision: choose } a_{t+1}} \circ \underbrace{\text{Shock-resolution stage}}_{\text{no decision; draw shocks; form } x'}.
$$

**Backward solution** runs right-to-left; **forward simulation** runs left-to-right. Full derivation is in `source/HKS_bellman_stages.md` §§3–5.

### 4.1 Consumption stage

| Perch | State vector | Value function |
|---|---|---|
| Arrival $[\prec]$ | $(x, p, \beta)$ | $v^{\text{cons}}_\prec(x, p, \beta)$ |
| Decision | $(x, p, \beta)$ | $v^{\text{cons}}(x, p, \beta)$ |
| Continuation $[\succ]$ | $(a, p, \beta)$ | $v^{\text{cons}}_\succ(a, p, \beta)$ |

- **Arrival → decision transition $g_{\prec\circ}$:** identity map on states, $(x, p, \beta) \mapsto (x, p, \beta)$ (no within-stage shocks); hence on values $v^{\text{cons}}_\prec = v^{\text{cons}}$, and the arrival mover is degenerate (explicitly labelled, not elided).
- **Decision backward mover $\mathbb{B}^{\text{cons}}$:** $v^{\text{cons}}(x,p,\beta) = \max_{a \in [\underline{a}, x]} \bigl\{ (x-a)^{1-\gamma}/(1-\gamma) + \beta \cdot v^{\text{cons}}_\succ(a, p, \beta) \bigr\}$.
- **Decision → continuation transition $g_{\circ\succ}$:** deterministic savings identity $(x, p, \beta, a) \mapsto (a, p, \beta)$.
- **Inter-stage wiring:** $v^{\text{cons}}_\succ(a, p, \beta) = v^{\text{shock}}_\prec(a, p, \beta)$.

### 4.2 Shock-resolution stage

| Perch | State vector | Value function |
|---|---|---|
| Arrival $[\prec]$ | $(a, p, \beta)$ | $v^{\text{shock}}_\prec(a, p, \beta)$ |
| Decision | $(a, p', \beta', \nu', \eta')$ | $v^{\text{shock}}(a, p', \beta', \nu', \eta')$ |
| Continuation $[\succ]$ | $(x', p', \beta')$ | $v^{\text{shock}}_\succ(x', p', \beta')$ |

- **Arrival → decision transition $g_{\prec\circ}$:** stochastic, $(a, p, \beta) \mapsto (a, p', \beta', \nu', \eta')$, with the four shocks drawn conditionally on $(p, \beta)$ per Section 3.
- **Arrival backward mover $\mathbb{B}^{\text{shock}}$ (on values):** pure expectation, $v^{\text{shock}}_\prec(a, p, \beta) = \mathbb{E}[v^{\text{shock}}(a, p', \beta', \nu', \eta') \mid p, \beta]$.
- **Decision perch:** no optimisation; evaluates the deterministic transition to the continuation perch.
- **Decision → continuation transition $g_{\circ\succ}$:** deterministic, $(a, p', \beta', \nu', \eta') \mapsto (x', p', \beta')$ with $x' = a + y' - \tau'(y') + (1 - \tilde\tau')\tilde y' + T'$ and $y', \tilde y'$ as in Section 5.
- **Inter-period wiring:** $v^{\text{shock}}_\succ(x', p', \beta') = V_{t+1}(x', p', \beta')$.

### 4.3 Period operator

$$
\mathbb{T}_t = \mathbb{B}^{\text{cons}} \circ \mathbb{B}^{\text{shock}},
$$

where each $\mathbb{B}$ is the stage backward mover above. Composing recovers the original HKS recursion:

$$
V_t(x, p, \beta) = \max_{a \in [\underline{a}, x]} \Bigl\{ u(x-a) + \beta \cdot \mathbb{E}[V_{t+1}(x', p', \beta') \mid p, \beta] \Bigr\}.
$$

---

## 5. Income and cash-on-hand transitions

$$
y' = \bigl(r' + r^X(a)\bigr) a + w' \, \psi(p') \exp(\nu'),
\qquad
\tilde y' = \sigma^X(a)\,\eta'\,a,
$$

$$
x' = a + y' - \tau'(y') + (1 - \tilde\tau')\tilde y' + T'.
$$

The zero-earnings state ($\psi(p') \exp(\nu') \to 0$ with probability $\chi$) is applied independently of the earnings draws. In a steady-state (benchmark) YAML the primed aggregate objects $(w', r', T', \tau', \tilde\tau', r^X, \sigma^X, \psi)$ are taken fixed.

---

## 6. Paper-supported calibration (pointer)

Full calibration tables and numerical-implementation details (EGM grids, Gauss–Hermite quadrature orders, Table-8 portfolio-schedule data across 13 wealth-percentile bins) are in `source/HKS_bellman_excerpt.md` (sections "Calibration," "Numerical implementation," and "Excess return schedule data"). Only the scalars needed to parse the YAML appear in the symbol table above.

---

## 7. Open issues for dolo-plus representation

Every item below is a **representation (dolo-plus-spec) gap**, not a paper gap. The paper fully specifies the economic content; see `verification.md` for the explicit distinction.

1. **Stochastic $\beta_t$ as a Markov state.** Canonical dolo-plus treats $\beta$ as a scalar parameter in the mover. Here it is a state that multiplies the continuation value. Proposed YAML idiom: encode as state `b` and write the Bellman as $u(c) + b \cdot V_\succ$. Flag: `# workaround:`.
2. **Function-valued objects $\tau(\cdot), r^X(\cdot), \sigma^X(\cdot), \psi(\cdot)$.** The paper uses piecewise and tabulated schedules (11-bracket tax, 13-bin portfolio schedule, Pareto-tail labour-efficiency map), not parametric closed forms. The DDSL spec provides `@mapsto … @via` for closed-form functions and *deliberately defers* tabulated/piecewise/external-data objects to a later semantic layer (dev-spec: "how these objects are constructed/evaluated is method-dependent and will be made explicit in DDSL-CORE / semantic directives"). Flag: `# unresolved:` — needs that semantic layer or an explicit parametric approximation.
3. **Aggregate-price treatment.** Partial equilibrium (the YAML's assumption): $(w, r, T, \tilde\tau)$ are `parameters`. Full equilibrium would time-index them as `exogenous` paths; transition experiments would do the same for $\sigma^P_t, \sigma^T_t, \kappa_t, \bar r_{c,t}$. Flag: `# workaround: partial-equilibrium`.
4. **EGM under wealth-dependent returns.** The Euler inversion itself is well-posed at fixed $a$ on the exogenous continuation grid (the canonical Carroll two-step $\hat c(a) = (v'_\succ(a))^{-1/\rho}$, $\hat m(a) = a + \hat c(a)$ still executes). The open item is whether the endogenous grid $\hat m(a)$ remains monotone as $r^X(a)$ increases in $a$; increasing returns to wealth can cause grid crossings and break value-function concavity. Non-monotone cases are addressed at the **solver** level by an upper-envelope correction (FUES / DC-EGM, Iskhakov et al. 2017), not at the problem-description level. Flag: `# unresolved:` — first-pass YAML may still omit `InvEuler` / `MarginalBellman` in favour of direct Bellman iteration, but that is an implementation choice, not a well-posedness failure.
5. **Period-level composition (canonical) and residual wiring items.** Period-level composition is canonical in dolo-plus per `docs/dolo-plus-spec/syntax-semantic-rules/05-periods-models.md`: a period file has `name`, `stages`, and optional `connectors` (the last needed only when adjacent stage interface names do not match). `dolo-plus-draft.yaml` now uses those keys. Two residual items remain flagged `# unresolved:` — (a) the intra-period rename between `hks_consumption` poststates `(a_cntn, p_cntn, b_cntn)` and `hks_shock_resolution` prestates `(a, p, b)`, pending the stage-file retag listed in `AGENTS.md` → "Common next tasks"; (b) the inter-period twister wiring shock-resolution.continuation → next-period consumption.arrival, which belongs at the **nest** level and is deliberately out of scope for this PR.

---

## Sources

- **Primary:** Hubmer, Krusell, and Smith (2018). Published as *NBER Macroeconomics Annual* 35 (2021), DOI [10.1086/712332](https://doi.org/10.1086/712332).
- **Faithful mathematical excerpt:** `source/HKS_bellman_excerpt.md`.
- **Long-form stage narrative:** `source/HKS_bellman_stages.md`.
- **Stage template:** SolvingMicroDSOPs §§12–13.
- **Matsya session:** see `matsya-session.txt`.
