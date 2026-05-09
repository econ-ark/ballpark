# Dynasty-layer excerpt — Benhabib, Bisin, and Luo (2019)

> **Paper:** Jess Benhabib, Alberto Bisin, and Mi Luo, "Wealth Distribution and Social Mobility in the US: A Quantitative Approach," *American Economic Review*, 109(5), 1623–1647, 2019. [DOI: 10.1257/aer.20151684](https://doi.org/10.1257/aer.20151684)

## Purpose and scope

This document is the modular-DDSL statement of the **dynasty-level / cross-generational** composition layer in the paper, intended as input to a Matsya iteration that will produce a [`dolo-plus-dynasty.yaml`](dolo-plus-dynasty.yaml). It is the sibling of [`bellman-excerpt.md`](bellman-excerpt.md), which formalizes the within-lifetime stage problem.

It covers:

- The **lifetime map** $g(\cdot;\tau,r)$: a black-box reference to the solution of the within-lifetime problem, $a^n_T = g(a^n_0;\tau^n,r^n)$.
- The **stochastic difference equation** for dynasty wealth: $a^{n+1}_0 = a^n_T = g(a^n_0;\tau^n,r^n)$.
- The **independent intergenerational Markov chains**: $\tau^n \mid \tau^{n-1} \sim \Pi_\tau$ and $r^n \mid r^{n-1} \sim \Pi_r$, with the two chains independent (paper §I).
- The **stationary-distribution / Pareto-tail Proposition** (paper §I): linearity of $g$ when $\mu = \sigma$, convexity when $\mu < \sigma$, and the resulting tail behavior of $\{a^n\}_n$.

It **does not** cover:

- The **within-lifetime stage problem** itself — see [`bellman-excerpt.md`](bellman-excerpt.md) and [`dolo-plus-draft.yaml`](dolo-plus-draft.yaml). The dynasty layer treats the 50 within-life value/policy functions as black-box outputs.
- The **Section IIID wealth-dependent $r$ extension** — flagged in "Out-of-scope" below; would belong in a separate dynasty variant document.
- **Numerical solution / replication.** Out of scope for this repo per `AGENTS.md`; the formalization layer describes the model rather than computing it.

---

## Symbol table (dynasty-layer additions)

Symbols inherited from the within-life excerpt (`bellman-excerpt.md`) — $\tau$, $r$, $a$, $T$, $\sigma$, $\mu$, $A$, $\beta$, $w_t(\tau)$, $V^{\tau,r}_t$, $\mathbb{B}_t$, $\mathbb{I}_t$, $\mathbb{T}_t$ — keep their meanings. New or extended symbols at the dynasty layer:

| Symbol | Role | Space / domain | Description |
|---|---|---|---|
| $n$ | index | $\{0, 1, 2, \ldots\}$ | Generation index along a dynasty |
| $\tau^n$ | type (decorated) | $\{1, \ldots, 10\}$ | Earnings-decile type for generation $n$ |
| $r^n$ | type (decorated) | $\{r_1, \ldots, r_5\}$ | Rate-of-return type for generation $n$ |
| $a^n_t$ | state (decorated) | $\mathbb{R}_{\ge 0}$ | Wealth at age $t$ within generation $n$'s lifetime |
| $a^n_0$ (= $a^n_1$) | initial wealth of $n$ | $\mathbb{R}_{\ge 0}$ | Newborn wealth; equals terminal wealth $a^{n-1}_T$ of parent |
| $a^n_T$ | terminal wealth of $n$ | $\mathbb{R}_{\ge 0}$ | Bequest of generation $n$ |
| $g(\cdot;\tau,r)$ | lifetime map | $\mathbb{R}_{\ge 0} \to \mathbb{R}_{\ge 0}$ | $a_T = g(a_0;\tau,r)$: terminal wealth as a function of initial wealth, given fixed-within-life types $(\tau,r)$ |
| $\Pi_\tau$ | transition matrix | $10 \times 10$, row-stochastic | Intergenerational transition for $\tau$, from Chetty et al. (2014) reduced (paper §IIB; full matrix in online Appendix B.2 — not tabulated there) |
| $\Pi_r$ | transition matrix | $5 \times 5$, row-stochastic | Intergenerational transition for $r$ (paper Table 4 + online Appendix C.1) |
| $\alpha(\tau,r)$ | savings rate | $\mathbb{R}_{>0}$ | Slope of $g$ in the linear regime $\mu = \sigma$: $g(a_0;\tau,r) = \alpha(\tau,r) a_0 + \beta_g(\tau,r)$ |
| $\beta_g(\tau,r)$ | shift constant | $\mathbb{R}$ | Intercept of $g$ in the linear regime; subscripted to disambiguate from the discount factor $\beta$ |
| $\gamma$ | tail index | $\mathbb{R}_{>0}$ | Pareto tail exponent of the stationary distribution: $\Pr(a > \underline a) \sim Q\,\underline a^{-\gamma}$ |
| $Q$ | tail constant | $\ge 1$ | Pareto-tail prefactor |

**Notation convention.** Superscripted $n$ denotes generation index; subscripted $t$ denotes age within a generation. Where unambiguous, we write $a^n$ for $a^n_0$ (the initial wealth of generation $n$, which is also the terminal wealth of generation $n-1$).

---

## Timing convention (across generations)

The within-period timing is documented in [`bellman-excerpt.md`](bellman-excerpt.md) (under the appendix-A.1 model, Open Issue #10 there). The cross-generational timing is:

1. **Generation $n$ is born** with initial wealth $a^n_0 = a^{n-1}_T$ (= terminal wealth of the parent).
2. **Type draws happen at birth.** $\tau^n \mid \tau^{n-1} \sim \Pi_\tau[\tau^{n-1},\,\cdot]$ and $r^n \mid r^{n-1} \sim \Pi_r[r^{n-1},\,\cdot]$, with the two chains **independent** (paper §I).
3. **Generation $n$ lives one lifetime**: $T = 36$ ages, types $(\tau^n, r^n)$ fixed throughout, no within-life shocks. The within-lifetime stage problem (`bellman-excerpt.md`) is solved once per type pair, producing $a^n_T = g(a^n_0;\tau^n,r^n)$.
4. **Generation $n+1$ is born** with $a^{n+1}_0 = a^n_T$, and the cycle repeats.

The dynasty layer treats step 3 as a black box; the **lifetime map** $g$ is the only piece of within-life output that crosses the boundary into the dynasty layer.

---

## Stochastic structure: $(\tau^n, r^n)$ as independent Markov chains

The intergenerational stochastic process $\{(\tau^n, r^n)\}_n$ is a finite irreducible Markov chain on $\{1, \ldots, 10\} \times \{r_1, \ldots, r_5\}$. Paper §I assumes **independence** of the two type dimensions:

$$
\Pi\bigl[(\tau^n, r^n) \mid (\tau^{n-1}, r^{n-1})\bigr] \;=\; \Pi_\tau[\tau^n \mid \tau^{n-1}] \cdot \Pi_r[r^n \mid r^{n-1}].
$$

Each component chain has its own state structure:

- **$\Pi_\tau$** (10 × 10): from Chetty et al. (2014) reduced to a 10-state chain (paper §IIB). Full matrix not tabulated in online Appendix B.2; would need reconstruction from Chetty et al.'s `online_data_tables.xls` or the BBL replication package at `https://doi.org/10.3886/E113112V1`. Status: matrix entries **UNRESOLVED** in the YAML pending separate fetch (mirroring the same flag in `dolo-plus-draft.yaml`).
- **$\Pi_r$** (5 × 5): paper Table 4 reports the diagonal; full matrix in online Appendix C.1. **Transcribed** in `dolo-plus-draft.yaml::calibration_family.population.Pi_r.matrix` (and reproduced for self-containment in `dolo-plus-dynasty.yaml`).

The initial distribution $\pi_0$ over $(\tau^0, r^0, a^0)$ is left unspecified at the formalization layer; the paper analyzes the stationary distribution under the chain's irreducibility (see "Stationary distribution" below).

---

## The lifetime map $g(\cdot;\tau,r)$

The lifetime map is **defined** as the composition of the within-life backward induction (which yields the optimal policy $c^*_t(\cdot;\tau,r)$ at each age) with the deterministic forward simulation under that policy:

$$
g(a_0;\tau,r) \;\equiv\; a_T \quad\text{where}\quad a_{t+1} \;=\; (1+r)\bigl(a_t - c^*_t(a_t;\tau,r)\bigr) + w_t(\tau), \quad t = 1, \ldots, T,
$$

with $a_1 = a_0$ and $c^*_t$ obtained from the Bellman equation in [`bellman-excerpt.md`](bellman-excerpt.md) (under the online-appendix-A.1 model, with $m_t = a_t$ identity).

The map is well-defined for every $(a_0, \tau, r)$ in the domain (because the within-life problem has a unique solution under the paper's assumptions) and is the **single object the dynasty layer composes**.

### Properties (paper Proposition, §I)

The paper characterizes $g$'s curvature in $a_0$ as follows:

- **If $\mu = \sigma$:** $g$ is **affine in $a_0$**:
$$
g(a_0;\tau,r) \;=\; \alpha(\tau,r)\,a_0 \;+\; \beta_g(\tau,r),
$$
where the **savings rate** $\alpha(\tau,r)$ is independent of $a_0$. There is no differential savings.

- **If $\mu < \sigma$:** $g$ is **strictly convex in $a_0$**:
$$
\frac{\partial^2 g}{\partial a_0^2}(a_0;\tau,r) \;>\; 0 \qquad\text{for all }(\tau,r) \text{ and all } a_0 > 0.
$$
Savings out of wealth are increasing in wealth — the **rich save proportionally more**. This is the analytical foundation of the paper's differential-savings story (paper Table 6, §IIIC).

The paper estimates $\mu = 0.5993 < \sigma = 2$ (Table 4); the empirically relevant regime is the convex one.

The within-life excerpt ([`bellman-excerpt.md`](bellman-excerpt.md), "Differential-savings result") gives an analytical sketch at the terminal age $T$; the full curvature claim follows by backward induction over the lifetime.

---

## Dynasty composition: the stochastic difference equation

The dynasty wealth process is the composition

$$
a^{n+1} \;=\; g\bigl(a^n;\,\tau^{n+1},\, r^{n+1}\bigr),
$$

(using $a^n$ as shorthand for $a^n_0 = a^{n-1}_T$). Combined with the type chains $\Pi_\tau$ and $\Pi_r$, this defines a Markov process on the joint state space

$$
\mathbb{R}_{\ge 0} \;\times\; \{1, \ldots, 10\} \;\times\; \{r_1, \ldots, r_5\}.
$$

The dynasty operator (in modular-DDSL terms) takes the within-life stage operators $\{\mathbb{T}^{(\tau,r)}\}$ — one per type pair — and composes them into a single intergenerational kernel via $g$ and $\Pi_\tau \otimes \Pi_r$.

---

## Stationary distribution and Pareto tail

Paper §I, characterization of the stationary distribution of $\{a^n\}_n$:

### Linear regime ($\mu = \sigma$)

The wealth process is a **linear stochastic recurrence equation**. Under standard conditions on the joint distribution of $(\alpha,\beta_g)$ (paper footnote 9; see Grey 1994, Hay-Rastegar-Roitershtein 2011, Benhabib-Bisin-Zhu 2011), the stationary distribution exists and has a **Pareto right tail**:

$$
\Pr(a > \underline a) \;\sim\; Q\,\underline a^{-\gamma}, \qquad Q \ge 1,
$$

with the tail index $\gamma$ defined implicitly by

$$
\lim_{N \to \infty}\;\mathbb{E}\!\left[\,\prod_{n=0}^{N-1} \alpha\bigl(\tau^{-n}, r^{-n}\bigr)^{\gamma}\,\right]^{1/N} \;=\; 1.
$$

**Independence of the earnings tail:** the constant term $\beta_g$ does not affect the asymptotic Pareto exponent $\gamma$ — only the multiplicative term $\alpha$ does. This is the paper's mechanism for generating a thick wealth tail despite the relatively thin earnings distribution.

### Convex regime ($\mu < \sigma$, the empirical case)

A stationary distribution may or may not exist (depends on the joint parameter values); when it exists, the right tail is **at least as thick as Pareto**:

$$
\Pr(a > \underline a) \;\ge\; Q\,\underline a^{-\gamma}.
$$

The paper's quantitative analysis (paper §III, Table 5) confirms the existence of a stationary distribution at the estimated parameter values and matches it to the empirical wealth shares.

---

## Deliverable for the YAML

The minimum adequate `dolo-plus-dynasty.yaml` formalization consists of:

1. A **reference to the within-life YAML** (`dolo-plus-draft.yaml`), naming the 50-instance family $\{(\tau, r_\mathrm{type})\}$ that parameterizes $g$.
2. A **dynasty-state block** declaring the cross-generational state $(a^n, \tau^n, r^n)$ and its inter-generational dynamics.
3. **The two intergenerational Markov chains** $\Pi_\tau$ and $\Pi_r$, with the independence assumption explicit. ($\Pi_r$ is also in the within-life YAML; reproduced here for self-containment.)
4. The **transition equation** $a^{n+1} = g(a^n;\tau^{n+1},r^{n+1})$ — symbolic reference to the lifetime map (the dynasty YAML does not compute $g$).
5. A **stationary-distribution annotation** noting the Pareto-tail Proposition and the linear-vs-convex dichotomy.

The paper provides all the formal structure needed; the gap is at the **dolo-plus syntax layer** (no canonical idiom for cross-generational composition), not the paper.

---

## Open issues / flagged gaps

### Resolved / addressed

(none yet — first iteration of this excerpt)

### Still open

1. **Cross-generational composition syntax.** Dolo-plus has no canonical keyword for composing solved within-life value functions across an outer Markov chain. The closest documented concepts (period templates, `stages:` block per matsya Turn 6) only address within-period composition. The dynasty YAML's outer block is SPECULATIVE; status UNRESOLVED at the dolo-plus spec level. (Inheriting matsya Turn 6's verdict on related items: terminal blocks, calibration-override families, per-age overrides — all UNRESOLVED in the indexed corpus.)

2. **Lifetime-map invocation syntax.** How does dolo-plus reference "the policy function from solving stage X with parameter overrides Y"? Not documented in matsya's corpus. The dynasty YAML treats $g(\cdot;\tau,r)$ as a symbolic reference; an actual solver would need to wire the within-life solution to the dynasty composition explicitly.

3. **Independence-of-chains specification.** Encoding "$\Pi$ is the product $\Pi_\tau \otimes \Pi_r$" cleanly in the YAML's exogenous block — likely via two separate `Markov(...)` declarations in the `exogenous:` block — is straightforward in principle but uses speculative syntax for the multi-chain case.

4. **$\Pi_\tau$ matrix not yet inlined.** Same flag as in the within-life YAML's `calibration_family.population.Pi_tau`: online Appendix B.2 only documents the construction procedure (collapse Chetty et al.'s 100 × 100 matrix into 10 × 10) and does not tabulate the result. Reconstruction would require Chetty et al.'s data tables or the BBL replication package.

5. **Initial-distribution choice.** Paper analyzes the stationary distribution; a runnable simulation would require an initial $a^0$ distribution (the paper uses a degenerate point at zero wealth in some exercises and the SCF 1962–63 distribution in the transitional-dynamics exercise of paper §V). Not part of the formalization, but relevant for downstream simulation.

---

## Out-of-scope, for reference only

- **Section IIID wealth-dependent $r$ extension.** In this paper extension, the Markov state of $r^n$ becomes wealth-conditioned ($r^n \mid r^{n-1}, a^n$), changing the dynasty layer's stochastic structure: the `r_chain` exogenous would become state-conditioned on $a$. The within-life stage structure is unchanged (the budget transition uses whatever $r$ value is drawn, which is now $a$-dependent). A formalization of this variant would belong in a separate dynasty excerpt + YAML pair.

- **Section V transitional-dynamics exercise.** The paper §V analyzes nonstationary dynamics starting from the SCF 1962–63 distribution. Same dynasty operator as the baseline but with a non-stationary initial distribution. Out of scope for this excerpt (which describes the operator), in scope for any future replication exercise (which would specify the initial distribution and iterate).

- **Numerical computation of the lifetime map $g$.** Out of scope per `AGENTS.md` "Common next tasks" — this repo describes models, does not solve them. The map $g(\cdot;\tau,r)$ is defined here but not computed; computation would happen in a downstream solver (econ-ARK or otherwise) that ingests this YAML pair.
