# Ballpark entry: Wong (2021)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing content lives in [`index.md`](index.md).

## Paper

- **Citation:** Wong, Arlene (2021), "Refinancing and the Transmission of Monetary Policy to Consumption," Working Paper, Department of Economics, Princeton University, March 2021. Latest public revision of Wong's 2016 Northwestern job-market paper originally circulated as "Population Aging and the Transmission of Monetary Policy to Consumption."
- **DOI:** No DOI — unpublished working paper. Paper PDF: [`Arlene-Wong-refinancing.pdf`](Arlene-Wong-refinancing.pdf); math-preserving Pandoc conversion: [`Arlene-Wong-refinancing.mmd`](Arlene-Wong-refinancing.mmd).
- **Core model:** Partial-equilibrium life-cycle overlapping-generations with uninsurable idiosyncratic income risk, an aggregate VAR in $(\log y_t,\, \log p_t,\, r_t)$, and a four-regime discrete-continuous choice (rent / own-&-no-refi / own-&-refi / purchase). Household states at arrival are $(s,\, h^{\mathrm{own}},\, b,\, R,\, \eta)$ plus age; fixed-rate mortgages are amortized over remaining life, with refinancing and new-purchase transaction costs.
- **Why in-ballpark:** Canonical heterogeneous-agent life-cycle model with discrete-continuous choice, explicit CRRA-Cobb-Douglas utility, shifted warm-glow bequest, state-contingent mortgage-coupon updating, and both idiosyncratic and aggregate shocks — exactly the modular-DP problem class Econ-ARK targets for formalization. The paper's headline economic result — that a positive covariance between refinancing propensity and liquidity-constrained status amplifies monetary-policy transmission, and that population aging erodes this covariance — is reproducible only in a formalized life-cycle framework.

## If a user asks to work on this item

1. **Read first:** [`bellman-excerpt.md`](bellman-excerpt.md). This is the modular-DDSL Bellman statement with a comprehensive symbol table, timing convention, perch decomposition, and regime-conditional Bellman equations. It is the authoritative starting point for any formalization work; do not re-derive from the paper PDF.
2. **If additional context is needed,** read [`PopAgingMPtransmission_summary.ipynb §"The Model"`](PopAgingMPtransmission_summary.ipynb) — verbose companion to the excerpt, aligned equation-by-equation.
3. **Paper source for AI ingestion:** [`Arlene-Wong-refinancing.mmd`](Arlene-Wong-refinancing.mmd) (Pandoc-converted). Prefer this over `Arlene-Wong-refinancing.pdf`. The Bellman section is §4.2, Eqs. (11)–(15); mortgage amortization is §4.1, Eqs. (5)–(6); reduced-form aggregate mappings are Eqs. (9)–(10), (16)–(17).

## Formalization status

- Explicit recursive formulation: **present** in `PopAgingMPtransmission_summary.ipynb §"The Model"` (aligned to paper §4.2).
- `bellman-excerpt.md`: **committed**.
- `bellman-excerpt-SMD-polished.md`: **not committed**. Post-Matsya SMD-aligned revision is the next deliverable.
- `dolo-plus-draft.yaml`: **not committed**.
- `verification.md`: **not committed**.
- `matsya-session.txt`: **not committed**. Intended session name: `PopMP` (per the contributor's convention in the gap-analysis). Switch to the course convention `topics2026-PopMP` if this item is used for coursework.

## Known model features requiring attention in a formalization pass

Pulled from `bellman-excerpt.md §6`, the regime-conditional structure in §5, and the CONTRIBUTING.md workaround taxonomy.

- **State-contingent coupon update.** $R_{j, a+1, t+1} = r_{t+1}^{d(a+1)}\, \mathbf{1}(\mathrm{adj}) + R_{jat}\,[1 - \mathbf{1}(\mathrm{adj})]$, where $\mathbf{1}(\mathrm{adj})$ is 1 in the `refi` or `purchase` regime and 0 under `rent` or `no-refi`. This is a state-contingent transition (CONTRIBUTING.md workaround category 3) and must be flagged inline in `dolo-plus-draft.yaml`. It cannot be silently encoded as a constant coupon or as an unconditional market-rate reset.

- **Mechanical (non-optimized) annuity payment.** $M_{jat}$ is the level annuity implied by $(b_{j, a-1, t-1},\, R_{j, a-1, t-1},\, d(a))$ in the `no-refi` regime, not a control. The balance recursion $b_{j, a+1, t+1} = b_{jat}(1 + R_{jat}) - M_{jat}$ is a deterministic identity. Flag as `# workaround: mechanical deduction` when writing the balance-and-payment block.

- **Regime-dependent transaction costs.** `purchase` carries $F^{\mathrm{new}} = \kappa^{\mathrm{new}}\, p_t\, h^{\mathrm{own}\prime}$ (proportional to the chosen new stock — endogenous to the choice). `refi` carries $F^{\mathrm{refi}} = F_f^{\mathrm{refi}} + F_v^{\mathrm{refi}}\, b'$ (dominantly fixed). The two regimes cannot share a single transaction-cost term in the YAML.

- **Duration-dependent mortgage rate as a reduced-form function of the aggregate state.** $r_t^{d} = f^d(S_t) = a_0^d + a_1^d\, r_t + a_2^d\, \log y_t$, estimated for $d \in \{1, 15, 30\}$ and interpolated. $r_t^d$ is **not** the short rate $r_t$ in the aggregate VAR — conflating the two severs the monetary-transmission channel at exactly the point the paper's mechanism depends on. The rental rate $p_t^r = \exp f^{pr}(S_t)$ has an analogous reduced-form specification.

- **Aggregate state is a finite Markov chain in practice.** The paper discretizes $S_t$ with Tauchen onto 18 states; a formalizer who keeps $S_t$ as a continuous Gaussian VAR in the YAML will over-parameterize the shock structure relative to what the paper actually computes. The intended dolo-plus representation is the discretized Markov chain.

- **Shifted warm-glow bequest.** $V^{\mathrm{beq}}(W) = B\,(W-1)^{1-\sigma}/(1-\sigma)$ — the $-1$ shift is from Cocco-Gomes-Maenhout (2005) and is material for calibration. A common earlier draft of the summary omitted the shift; any YAML derived from pre-April-2026 versions of the summary should be checked.

- **Free regime toggling, no hysteresis.** The four regimes form a flat discrete-choice menu every period. In particular a renter arriving with $h^{\mathrm{own}} = b = 0$ can enter `purchase` next period, and an owner can unconditionally switch to `rent` by liquidating. A formalization that introduces tenure persistence or a "once-a-renter-always-a-renter" constraint is incorrect.

- **Joint choice of $(c,\, h^{\mathrm{own}\prime})$ in the `purchase` regime.** In three of the four regimes housing services are fixed once the regime is chosen, so the continuous inner problem is standard CRRA in $c$ and straightforwardly EGM-compatible. The `purchase` regime is different: $h^{\mathrm{own}\prime}$ is a simultaneous choice with $c$ (and with $b',\, s'$), so a full EGM pass requires a nested inner problem. Discuss this in `bellman-excerpt-SMD-polished.md`.

- **Initialization and retirement as separate stages.** The working-age stage specified in `bellman-excerpt.md` is interior-only. The initialization at $a=1$ (distribution matched to 2004 SCF 20–29 age bracket), the retirement transition at $a = T_y + 1$ (stochastic labor income replaced by a deterministic Social Security transfer that is a function of terminal-working-age income, as in Guvenen and Smith 2014), and the terminal age $a = T$ (continuation collapses to $V^{\mathrm{beq}}$) are all out of scope for the current excerpt and will each need their own stage in a complete YAML.

## Common next tasks (grounded)

Each cites the file or section a next-task should touch.

1. **Draft `bellman-excerpt-SMD-polished.md`** by running `bellman-excerpt.md` through Matsya (`--session PopMP`), aligning the output to SolvingMicroDSOPs §§12–13, adding the perch table with a *Key transition or Bellman step* column, and writing the EGM-channel discussion (distinguishing the `rent` / `no-refi` / `refi` regimes, where EGM applies straightforwardly, from the `purchase` regime, where $h^{\mathrm{own}\prime}$ is a simultaneous continuous choice).

2. **Draft `dolo-plus-draft.yaml`** for the interior working-age stage (single stage is acceptable per CONTRIBUTING.md). Inline flags required:
   - `# workaround: mechanical deduction` on the $M_{jat}$ annuity line and balance recursion.
   - `# workaround: state-contingent transition` on the $R_{j, a+1, t+1}$ coupon-update line.
   - `# unresolved:` on any behavior that does not map cleanly — specifically, whether the four-regime discrete choice can be encoded natively in dolo-plus or must be split into four parallel stages stitched by a max operator.

3. **Write `verification.md`** one-paragraph note, comparing the YAML draft to **paper Eqs. (5)–(17)**, not to `_summary.ipynb`. State explicitly which items were accepted / edited / rejected from the Matsya output. The `_summary.ipynb` is the summary's own authoritative statement and is aligned to the paper, but the final verification must reach through to the paper per CONTRIBUTING.md §"Review policy".

4. **Commit `matsya-session.txt`** with the single line `PopMP` (or `topics2026-PopMP` for coursework use). Staff can inspect the server-side conversation by session name.

5. **Add terminal-age and retirement stages** to the YAML once the interior stage is stable. The retirement block reuses the four-regime structure with $y_{jat}$ replaced by a deterministic transfer; the terminal block collapses to $V^{\mathrm{beq}}$.

6. **Decide on the discretization contract.** The YAML should use the 18-state Tauchen-discretized Markov chain for $S_t$, not the continuous Gaussian VAR; the reduced-form functions $r_t^d = f^d(S_t)$ and $\log p_t^r = f^{pr}(S_t)$ should be tabulated on that grid. Confirm this choice in `verification.md`.

## Workflow reminders

- **Matsya session:** use `--session PopMP` for all calls on this item. For coursework, switch to `--session topics2026-PopMP` per the CONTRIBUTING.md convention.
- **Paper verification:** Matsya output must be checked against `Arlene-Wong-refinancing.mmd` (or the PDF), not only against `PopAgingMPtransmission_summary.ipynb`. The summary is aligned to the paper as of April 2026, but is a summary, not the source of truth.
- **When flagging workarounds in YAML:** use inline `# workaround:` or `# unresolved:` comments rather than silently fudging non-canonical syntax. The three categories most likely to hit in this item are (i) mechanical deductions (the $M_{jat}$ annuity), (ii) state-contingent transitions (the $R$ coupon update), and (iii) state-contingent shock distributions (if retirement is encoded as a stochastic transition from the stochastic-income stage rather than as a separate stage).
- **Do not conflate $r_t$ and $r_t^{d(a)}$.** The short rate drives the aggregate VAR and the return on short-term savings; the duration-specific mortgage rate is a reduced-form function of the whole aggregate state. The paper's mechanism turns on this distinction.
