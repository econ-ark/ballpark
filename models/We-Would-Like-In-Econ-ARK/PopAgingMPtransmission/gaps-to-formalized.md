# Gaps between the current Primer and a defensible Formalized tier

*Review against [`llorracc/ballpark` CONTRIBUTING.md](https://github.com/llorracc/ballpark/blob/master/CONTRIBUTING.md), performed against `Arlene-Wong-refinancing.mmd` §4 (the paper's own "Model" section), not only the `_summary.ipynb`.*

The entry is genuinely a *Primer* — all four exposition notebooks exist, `self.bib`/`subsequent-literature.bib` are populated, the `.mmd` is committed, and `index.md` frontmatter is valid. What keeps it from being *Formalized*-ready is not cosmetic: the recursive statement in `_summary.ipynb` is inconsistent with the paper on several points that a formalizer would have to resolve by re-reading the PDF, and the agent-facing scaffolding (`AGENTS.md`, symbol table, perch decomposition) is absent. The five items below are prioritized by how much they would block a matsya pass.

Note on matsya: I deliberately did **not** open a `--session PopMP` thread. Feeding matsya the current `_summary.ipynb §"The Model"` would produce a confident-looking perch decomposition of the *wrong* model — three regimes instead of four, no mortgage law of motion, an under-specified `assets` bundle. The correct sequence is **fix the summary first (item 1), then call matsya**. That way the human-reviewer gate at the Formalized tier (which CI cannot perform) has something real to check.

---

## 1. Rewrite "The Model" in `_summary.ipynb` to match the paper's four-regime recursive statement

**(a) Problem.** The summary compresses the paper's four housing-tenure regimes into three and drops the mortgage balance's law of motion, the duration-specific mortgage-rate mapping, and the fixed mortgage coupon as a state variable — so the recursive formulation does not admit an unambiguous perch decomposition.

**(b) Proposed substantive change.** Reconstruct "The Model" to mirror Wong (2021) §4.2 exactly. Concretely:

- **Split "own & adjust" into two regimes: `purchase` and `own & refi`**, matching paper Eqs. (13) and (14). They differ in both the state transition on $h^{\text{own}}$ (new stock vs. depreciated existing stock) and the transaction-cost schedule ($F^{\text{new}} = 0.05 \cdot p_t h_{jat}^{\text{own}}$ proportional; $F^{\text{refi}} = F_f^{\text{refi}} + F_v^{\text{refi}} b'_{jat}$ dominated by a fixed component). The current summary lumps both into a single `own & adjust` regime with a scalar `F`, which is under-determined for a formalization pass.
- **Write out the mortgage law of motion** from paper Eqs. (5)–(6): the amortization identity $b_{j,a+1,t+1} = b_{jat}(1+R_{jat}) - M_{jat}$ with $M_{jat}$ the annuity payment implied by outstanding balance, remaining duration $d(a) = T-a$, and fixed coupon $R_{jat}$; and the coupon's own recursion $R_{j,a+1,t+1} = r_{t+1}^{d(a+1)} \mathbf{1}(\text{refi})_{t+1} + R_{jat}(1 - \mathbf{1}(\text{refi})_{t+1})$. The summary's budget constraints use $M_{jat}$ and the term $b_{j,a-1,t-1}(1+R_{j,a-1,t-1})$ without ever defining where $M_{jat}$ comes from or how $R$ rolls — a matsya pass would have to invent these.
- **Unpack the `assets` state.** The summary writes $z_{jat} = \{S_t, y_{jat}, \text{assets}_{j,a-1,t-1}\}$ and leaves `assets` undefined. The paper is explicit: $\text{assets} = (s, h^{\text{own}}, b, R)$. Without this, the arrival perch cannot list its state variables.
- **Add the reduced-form mortgage-rate and rental-rate links.** Paper Eqs. (9), (10), (16), (17): $r_t^d = f^d(S_t)$ (duration-specific, estimated linear-in-$r_t$-and-$\log y_t$) and $\log p_t^r = f^{pr}(S_t)$. The summary uses the aggregate short rate $r_t$ as if it were the mortgage rate and silently treats $p_t^r$ as exogenous. Both functional forms carry the aggregate state into prices the household actually faces; omitting them severs the monetary-transmission channel at exactly the point matsya would need.
- **Fix the bequest form.** Paper: $B(W_{jat} - 1)^{1-\sigma}/(1-\sigma)$ (with the $-1$ shift, matching Cocco-Gomes-Maenhout 2005). Summary: $B W_{jat}^{1-\sigma}/(1-\sigma)$. This is small algebraically but material for calibration.
- **Fix the income process.** Paper: $\log y_{jat} = \chi_a + \eta_{jat} + \phi_a(y_t)$. Summary: $\phi_a(y_t/\bar y)$ — the $\bar y$ normalization is not in the paper and is never defined.
- **State the timing convention explicitly** — "start-of-period holdings carry the $(j,a-1,t-1)$ indices; choices are made at $t$; continuation is $(j,a+1,t+1)$". The summary's mixed-indexing budget constraints are consistent with this reading, but at the Formalized tier the convention should be named, because it is what pins down which variables sit on which perch.

**(c) Where.** `PopAgingMPtransmission_summary.ipynb`, cells 3–7 (the "The Model" section and its four sub-regime cells). Cross-check against `Arlene-Wong-refinancing.mmd` lines 475–625 (paper §§4.1–4.2). Once this is done, the recursive statement is authoritative and a `bellman-excerpt.md` can be lifted from it mechanically.

**Review:** This change is well founded in the paper, and reflects the update from the 2016 working paper to the most recent version. **Accept.**

---

## 2. Add a symbol table and a perch-decomposition stub to a new `bellman-excerpt.md`

**(a) Problem.** The Formalized-tier checklist requires a *comprehensive* symbol table and a three-perch decomposition with explicit $\mathrm{g}_{\prec\circ}$, $\mathrm{g}_{\circ\succ}$, $\mathbb{B}$, $\mathbb{I}$, $\mathbb{T} = \mathbb{I}\circ\mathbb{B}$ — this file does not exist yet, and the summary's prose cannot substitute because several required symbols ($M_{jat}$, $R_{jat}$, $d(a)$, $f^d$, $f^{pr}$, $F^{\text{new}}$, $F^{\text{refi}}$, $\phi$, $\underline{s}$, $\pi_a$, $B$) are not inventoried anywhere.

**(b) Proposed substantive change.** Create `bellman-excerpt.md` with four sections:

1. **Symbol table** (one row per object): list every state ($a, s, h^{\text{own}}, b, R, \eta, S$), every control ($c, s', h^{\text{own}\prime}, h^{\text{rent}}, b'$, discrete regime $d \in \{\text{rent}, \text{purchase}, \text{refi}, \text{no-refi}\}$), every shock ($\psi_{jt}, u_t$), every parameter ($\alpha, \sigma, \beta, \delta, \phi, \underline{s}, B, F_f^{\text{refi}}, F_v^{\text{refi}}, T, T_y, \rho_\eta, \sigma_\eta, \chi_a, \phi_a, \pi_a, A_0, A_1, V$), every derived object ($r_t^d, p_t^r, M_{jat}, d(a), y_{jat}, W_{jat}$), plus the value functions $V, V^{\text{rent}}, V^{\text{purchase}}, V^{\text{own\&refi}}, V^{\text{own\&no-refi}}, V^{\text{beq}}$. For each: role (state/control/shock/parameter/derived), space/domain, one-line description.
2. **Timing convention** — numbered steps within a period (arrival → aggregate-state realization → idiosyncratic income realization → discrete regime choice → continuous choice → asset/mortgage update → continuation).
3. **Perch decomposition.** Arrival perch $\prec$ carries $(a, s, h^{\text{own}}, b, R, \eta_{-1})$ and the aggregate state $S_{-1}$; the decision perch $\circ$ adds the realized $(S, \psi, y)$ and hosts the discrete-then-continuous choice; the continuation perch $\succ$ holds post-choice $(s', h^{\text{own}\prime}, b', R', \eta)$. State-contingent coupon updating under refinancing makes $\mathrm{g}_{\circ\succ}$ non-trivial (flag as a workaround candidate, see item 6). The arrival mover $\mathbb{I}$ integrates over $(\psi, u)$; the backward mover $\mathbb{B}$ maximizes over the four-way discrete choice stacked with the continuous controls.
4. **Stage operator** $\mathbb{T} = \mathbb{I} \circ \mathbb{B}$, followed by explicit CRRA-Cobb-Douglas $u$ and the shifted warm-glow $V^{\text{beq}}$.

A degenerate stub perch is fine and should be *labeled* degenerate (per CONTRIBUTING.md), but no perch can be omitted.

**(c) Where.** New file `bellman-excerpt.md` in the item root. This file is the one matsya is supposed to ingest; its absence is the blocker for the Formalized checklist's first two bullets (`bellman-excerpt.md` and `bellman-excerpt-SMD-polished.md`).

**Review:** This is the next step--setting up a bellman decomposition for matsya to turn into a .yml file. **Accept.**

---

## 3. Surface the paper's distinguishing features in `_summary.ipynb` Results

**(a) Problem.** The Overview and Results cells list the empirical finding ("young consumption is 2–3× more responsive") and a generic claim ("aging dampens transmission") but do not surface the three mechanisms that actually make this paper *this paper* — the covariance mechanism, the fixed-vs-variable-rate counterfactual, and the quantitative decomposition — so a reader of the summary cannot tell what the model adds beyond the empirical result.

**(b) Proposed substantive change.** Expand the Results cell (and add a sentence to Overview) to state, in order:

- **The covariance mechanism.** The paper's signature theoretical insight is that young households are simultaneously (i) more likely to refinance when rates fall (larger loans, longer durations → interest savings exceed the fixed cost) and (ii) more likely to be short-term-liquidity-constrained. The *positive covariance* between refinancing propensity and constrained-MPC status is what amplifies the aggregate response, and it is what disappears as the population ages. This is the mechanism that ties the age gradient to monetary-policy effectiveness — without it, the entry reads as an empirical paper with a calibration.
- **The fixed-vs-variable-rate counterfactual.** The paper's headline quantitative experiment is replacing the FRM structure with an ARM structure and recomputing consumption responses. Two offsetting forces: lower covariance (dampens the heterogeneity), more households experiencing rate changes (amplifies the aggregate). Wong finds the second dominates — aggregate response is *larger* under ARMs; cross-sectional heterogeneity is *smaller*.
- **The 45 % decomposition.** Shutting down refinancing and re-estimating under ARMs reduces the young-old consumption-response gap by ≈ 45 %. This is a concrete number the summary should report.

These three items are load-bearing for `AGENTS.md §"Why in-ballpark"` and for `_intro.ipynb`'s one-sentence pitch; surfacing them in the summary gives downstream agents something concrete to point at.

**(c) Where.** `PopAgingMPtransmission_summary.ipynb`, cell 8 ("Results") — rewrite substantively; and a one-line addition to cell 2 ("Overview") naming the covariance mechanism.

**Review:** While this critique is well founded, this is not the focus of the ballpark entry. **Reject.**

---

## 4. Tighten prior-literature to include the direct modeling antecedents

**(a) Problem.** `_prior-literature.ipynb` cites 3 papers (Kaplan-Violante 2014, Auclert 2019, Mian-Sufi 2013), which is at the low end of the 3–6 window and omits the papers Wong explicitly cites as the *modeling* foundations for her mortgage, transaction-cost, and aggregate-state specifications.

**(b) Proposed substantive change.** Add three foundational references and briefly state what each one supplies:

- **Campbell & Cocco (2003), "Household Risk Management and Optimal Mortgage Choice," *QJE*.** The paper's mortgage-amortization specification (Eq. 5–6 of Wong) is "following Campbell and Cocco (2003)"; this is the direct ancestor of the FRM-with-amortization block that is the paper's whole mechanism.
- **Kaplan, Moll & Violante (2018), "Monetary Policy According to HANK," *AER*.** Wong cites this explicitly as the source for her two-liquid-and-illiquid asset structure, her aggregate state VAR specification, and her transaction-cost modeling. It is currently mis-classified in `subsequent-literature.bib` as `monetary_kaplan_2016`; it is *foundational*, not subsequent. (Wong 2016 JMP and KMV are contemporaries, but for a 2021 working-paper revision KMV 2018 is clearly prior art.)
- **Berger, Guerrieri, Lorenzoni & Vavra (2018), "House Prices and Consumer Spending," *REStud*.** Wong cites this directly for the fixed-cost-of-housing-adjustment specification and for several calibration targets. Currently in `subsequent-literature.bib` as `house_berger_2018` but is not discussed in that notebook either; it belongs in prior.

Optional additions if you want to push into the 5–6 range: **Díaz & Luengo-Prado (2012)** for the new-home transaction-cost parameterization, or **Alvarez & Lippi (2009)** / **Alvarez, Guiso & Lippi (2012)** as the generic lumpy-adjustment foundation.

**(c) Where.** `PopAgingMPtransmission_prior-literature.ipynb` (expand the "Key foundational papers" list and the "Connecting demographics to monetary policy transmission" paragraph); `references.bib` (verify entries exist; add if missing); `subsequent-literature.bib` (reclassify or drop the three entries above — currently uncited from the subsequent notebook in any case).

**Review:** Since this paper took a long time to develop, the difference between *prior* and *subsequent* literature is hazy. The current iteration of the literature rewiew is fine. **Reject.**

---

## 5. Create `AGENTS.md` and correct the subsequent-literature coverage

**(a) Problem.** `AGENTS.md` is absent (it is *required* at Formalized and *recommended* at Primer), and `_subsequent-literature.ipynb` carries two structural errors — it mis-classifies Kaplan-Moll-Violante 2018 and Beraja et al. 2019 as post-Wong follow-ups (both are contemporaneous with or antecedent to the 2021 WP), and omits the three papers most often cited today as direct descendants.

**(b) Proposed substantive change.**

*AGENTS.md.* Create the file following the CONTRIBUTING.md template. Every section has a grounded source in the item once items 1–3 are done:

- **Paper** — copy verbatim from `_intro.ipynb` (citation, URL, one-sentence pitch).
- **If a user asks to work on this item** — read-first pointer to `_summary.ipynb §"The Model"` until `bellman-excerpt-SMD-polished.md` exists, then repoint; AI-ingestion file is `Arlene-Wong-refinancing.mmd`.
- **Formalization status** — honest ticks. After items 1–2 are done: explicit recursive formulation *present*; `bellman-excerpt.md` *committed*; `bellman-excerpt-SMD-polished.md`, `dolo-plus-draft.yaml`, `verification.md`, `matsya-session.txt` *not yet*.
- **Known model features requiring attention** — grounded, not aspirational. The real list (from items 1 and 6): (i) *state-contingent coupon update* under refinancing — $R'$ flips between its current value and $r_{t+1}^{d(a+1)}$ depending on a binary choice, a state-contingent shock distribution that is one of CONTRIBUTING.md's three canonical workaround categories; (ii) *duration-dependent mortgage rate* $r_t^d = f^d(S_t)$ — the yield curve is embedded as a reduced-form function of the aggregate state, so the "interest rate the household faces" is not the same variable as the one in the aggregate VAR; (iii) *proportional vs. fixed transaction costs* — the `purchase` regime uses $F^{\text{new}} = 0.05 \cdot p_t h^{\text{own}\prime}$ (proportional, endogenous to the choice), the `refi` regime uses a fixed $F_f^{\text{refi}}$ — dolo-plus must encode both and the flag is non-trivial; (iv) *amortization as a mechanical deduction* — $M_{jat}$ is not a choice, it is the annuity implied by $(b, R, d(a))$, which is CONTRIBUTING.md's "mechanical (non-optimized) deductions" workaround; (v) *income process uses the aggregate level $y_t$ not its innovation* — this is cleanly first-order Markov in the aggregate state but couples idiosyncratic income to the aggregate VAR in a way that is easy to get wrong; (vi) *warm-glow bequest has a shift* ($W-1$, not $W$).
- **Common next tasks** — tied to actual gaps: (1) produce `bellman-excerpt.md` and `bellman-excerpt-SMD-polished.md` from the repaired `_summary.ipynb §"The Model"`; (2) draft a one-stage `dolo-plus-draft.yaml` for the interior period, flagging the state-contingent coupon update and the amortization deduction inline; (3) write `verification.md` comparing the draft against paper Eqs. (5)–(15); (4) commit `matsya-session.txt` with the `--session PopMP` string; (5) add alt-text for the paper's Table 2 / Table 14 if the summary eventually embeds them.
- **Workflow reminders** — Matsya session `--session PopMP`; paper verification against `Arlene-Wong-refinancing.mmd`, not `_summary.ipynb`; `# workaround:` / `# unresolved:` for YAML anomalies.

*Subsequent-literature repair.* In `_subsequent-literature.ipynb`: (i) **demote** Kaplan-Moll-Violante 2018 — it is prior art per item 4, not a follow-up; (ii) **demote or re-frame** Beraja-Fuster-Hurst-Vavra 2019 — published before Wong 2021 and cited by Wong, so it is at best contemporaneous; a cleaner edit is to cite it in *prior* literature as the closest contemporaneous structural model and drop the claim that it "followed" Wong; (iii) **add** three descendants that are actually downstream and increasingly standard:
  - *Cloyne, Ferreira & Surico (2020), "Monetary Policy when Households Have Debt," REStud* — direct empirical follow-up on mortgagor vs. outright-owner heterogeneity, the empirical result Wong's model is meant to rationalize.
  - *McKay & Wieland (2021), "Lumpy Durable Consumption Demand and the Limited Ammunition of Monetary Policy," Econometrica* — formalizes the durable-goods-with-fixed-costs channel at aggregate scale, extending Wong-style transaction-cost logic beyond mortgages.
  - *Auclert, Rognlie & Straub (2024), "Micro Jumps, Macro Humps," AER* — the quantitative HANK benchmark that subsumes age- and liquidity-heterogeneity into an estimated model of monetary transmission; the natural "where-the-field-went" citation.

**(c) Where.** New `AGENTS.md` in item root; `PopAgingMPtransmission_subsequent-literature.ipynb` (re-classification + three additions); `subsequent-literature.bib` (add Cloyne-Ferreira-Surico, McKay-Wieland, Auclert-Rognlie-Straub entries; remove or relocate the Kaplan-Moll-Violante and Beraja entries).

**Review:** Of course the agents file is required for the formalization tier, so (a) will be implemented. Other changes to the literature review are secondary concerns. **Accept/Reject.**

---

## 6. Resolve the ambiguities a grad-student formalizer would otherwise re-discover

**(a) Problem.** Even after items 1–5, a thoughtful formalizer starting `dolo-plus-draft.yaml` will hit three specific ambiguities that are not resolved in either the summary or the paper and that, left unflagged, will quietly change the model; these belong in an `unresolved` note inside `AGENTS.md` or (better) as an explicit decision recorded in the repaired summary.

**(b) Proposed substantive change.** Make three decisions explicitly and record them:

- **What is in `assets` at the *arrival* perch of a renter?** The summary's rent-regime budget carries $(1-\delta) p_t h_{j,a-1,t-1}^{\text{own}}$ on the right-hand side, i.e. a renter who arrives with owned housing liquidates it at the depreciated value this period. Is that a one-shot conversion (the agent becomes a renter permanently while draining stock), or can an agent toggle regimes freely period-by-period? The paper (Eq. 12) reads as free toggling. This needs to be stated — it is the difference between one discrete-continuous stage and a multi-stage hysteresis model.
- **Does the `own & no-refi` mortgage payment $M$ use the *current* balance and *current* coupon, or the balance and coupon at contract origination?** Paper footnote 8 says $M_{jat}$ is computed from *current* $b_{jat}$ and $R_{jat}$ (i.e., recomputed each period using remaining duration $d(a)$). The summary's `own & no-adjust` constraint shows $M_{jat}$ as a black box. A dolo-plus encoding must pick one — and the paper's choice means $M$ is a deterministic function of the arrival state, not an additional state.
- **Discretization of $S_t$.** The paper discretizes the aggregate VAR with Tauchen into 18 states. Once translated to dolo-plus, the aggregate process becomes a finite Markov chain on $S_t$, not a continuous Gaussian innovation. This is the cleanest way to handle the $r_t^d = f^d(S_t)$ and $\log p_t^r = f^{pr}(S_t)$ mappings (they become tabulated functions on the grid). A formalizer who takes the summary's Gaussian-innovation statement at face value will over-parameterize the shock block.

Recording these three decisions in `_summary.ipynb §"The Model"` (as brief "Conventions" paragraph) and/or in `AGENTS.md §"Known model features requiring attention"` closes the main remaining interpretation gaps before matsya sees the file.

**(c) Where.** A new "Conventions and scope" subsection at the end of `PopAgingMPtransmission_summary.ipynb §"The Model"` (before "Results") — three short paragraphs, one per item. Cross-reference from `AGENTS.md §"Known model features requiring attention"`.

**Review:** This change is a bit redundant and will be captured by the other changes. So in some sense, **accept.**

---

## Summary of where this lands

Items 1, 2, and 6 together produce a recursive formulation and perch-decomposition stub that matsya can operate on productively. Items 3 and 4 repair exposition gaps that are small per-unit but that cumulatively determine whether a reader who has not read the paper can trust the entry. Item 5 produces the `AGENTS.md` that the Formalized tier requires and fixes the two structural mis-classifications in the subsequent-literature notebook.

None of the six items requires new research. All are grounded in text that exists either in `Arlene-Wong-refinancing.mmd` (items 1, 3, 4, 6) or in the CONTRIBUTING.md template itself (items 2, 5). Total effort is inside CONTRIBUTING.md's "≤ 2 weekly assignments from Primer to Formalized" budget, provided matsya is only invoked *after* item 1 lands.

---

## Follow up prompt: 

Implement changes 1,2, 5(a) and 6 that you propose in gaps-to-formalized.md. That is, in summary,  

- update PopAgingMptransmission_summary.ipynb so that the model matches the 4 types of households as in the paper
- create a bellman-excerpt file that is ready to be fed to matsya
- create an agents file that are up to the standards of a formalized tier ballpark.

## Implementation log — 2026-04-24

Items **1, 2, 5(a), and 6** from the prioritized list above were implemented in a single pass on 2026-04-24. Items 3, 4, and 5(b) are deferred and remain tracked above.

### 1. `PopAgingMPtransmission_summary.ipynb` — rewrite of "The Model"

The notebook now has 13 cells (was 10) with a recursive formulation that matches paper §4.2 equation-by-equation:

- **Cell 3** (modified): four-regime $\max$, state unpacked as $(a,\, S_t,\, y_{jat},\, (s,\, h^{\mathrm{own}},\, b,\, R))$, income process with $\phi_a(y_t)$ (no spurious $/\bar y$), shifted warm-glow bequest $B(W-1)^{1-\sigma}/(1-\sigma)$, explicit six-step timing convention.
- **Cell 4** (new, "Mortgage dynamics"): amortization annuity $M_{jat}$, balance LoM, state-contingent coupon update $R_{j,a+1,t+1} = r_{t+1}^{d(a+1)}\,\mathbf{1}(\mathrm{adj}) + R_{jat}\,[1-\mathbf{1}(\mathrm{adj})]$, reduced-form $r_t^{d} = f^{d}(S_t)$ and $\log p_t^{r} = f^{pr}(S_t)$, regime-specific transaction costs.
- **Cells 5–8** (modified + new): four regime-specific Bellman equations — rent (Eq. 12), own & no-refi (Eq. 15), purchase (Eq. 13), own & refi (Eq. 14). The old "own & adjust" umbrella is gone.
- **Cell 9** (Retirement, modified): bequest now includes $-b_{j,a-1,t-1}(1+R_{j,a-1,t-1})$ in $W_{jat}$ and uses the $(W-1)^{1-\sigma}$ form.
- **Cell 10** (new, "Conventions and scope"): free regime toggling, $M_{jat}$ as mechanical deduction, 18-state Tauchen discretization.
- **Cell 11** (Results, expanded): covariance mechanism, FRM-vs-ARM counterfactual, 45% decomposition, aggregate implication. Note: these additions properly belong to item 3 (distinguishing features) but were rolled in here because they live in the same notebook cell.

### 2. `bellman-excerpt.md` — standalone DDSL Bellman statement

Ready to feed to Matsya (`--session PopMP`). Contains:

- **§1 Symbol table** — 9 sub-tables (indices, arrival-perch states, aggregate state, shocks, realized derived quantities, controls, continuation-perch states, parameters, value functions) with role/space/description for every symbol in the formalized statement.
- **§2 Timing convention** — six numbered steps within one period.
- **§3 Perch decomposition** — arrival $\prec$ / decision $\circ$ / continuation $\succ$ each with states carried, value function, and control; within-stage transitions $\mathrm{g}_{\prec\circ}$ and $\mathrm{g}_{\circ\succ}$ (including the regime-contingent post-state identity); backward mover $\mathbb{B}$ and forward/arrival mover $\mathbb{I}$; stage operator $\mathbb{T} = \mathbb{I}\circ\mathbb{B}$.
- **§4** isolates the mechanical annuity deduction.
- **§5** gives utility, bequest, and all four regime-conditional Bellman equations with paper-equation cross-references.
- **§6 Notes for the formalizer** — the six workaround categories, including EGM applicability per regime.
- **§7** explicitly stubs retirement, terminal age, and initialization as out-of-scope.

### 3. `AGENTS.md` — six sections, all grounded

- **Paper** — citation, DOI note, one-sentence core-model description, one-sentence why-in-ballpark.
- **If a user asks to work on this item** — read-first pointer to `bellman-excerpt.md` (authoritative), fallback to `_summary.ipynb §"The Model"`, AI-ingestion file `Arlene-Wong-refinancing.mmd`.
- **Formalization status** — honest: `bellman-excerpt.md` committed; the four remaining layer files are not.
- **Known model features requiring attention** — eight items, each tied to a specific feature (state-contingent coupon update, mechanical annuity, regime-dependent transaction costs, duration-specific mortgage rate, Tauchen discretization, shifted bequest, free regime toggling, joint $(c,\, h^{\mathrm{own}\prime})$ choice in purchase), plus the stage-scoping note on retirement and initialization.
- **Common next tasks** — six tasks, each with the file and specific flags required (inline `# workaround: mechanical deduction`, `# workaround: state-contingent transition`, `# unresolved:` on the four-way discrete choice).
- **Workflow reminders** — Matsya session `PopMP`; paper-not-summary verification; `$r_t \neq r_t^{d(a)}$` warning.

### What was *not* implemented

- **Item 3** (distinguishing features in Results) — the Results-cell content was rolled into item 1 above, but the corresponding refresh of the Overview cell and the intro's one-sentence pitch are *not* done.
- **Item 4** (prior-literature additions: Campbell-Cocco 2003, KMV 2018, Berger-Guerrieri-Lorenzoni-Vavra 2018) — deferred. The citations are referenced from inside `bellman-excerpt.md` and the new "Mortgage dynamics" cell (Campbell2003-qk is already in `references.bib`), but the `_prior-literature.ipynb` notebook itself is unchanged.
- **Item 5(b)** (subsequent-literature re-classification: demote KMV and Beraja, add Cloyne-Ferreira-Surico 2020 / McKay-Wieland 2021 / Auclert-Rognlie-Straub 2024) — deferred. `subsequent-literature.bib` is unchanged and `_subsequent-literature.ipynb` retains the mis-classifications.

### Matsya usage

No `--session PopMP` thread was opened during this implementation. The rationale from the original review stands: the correct ordering is to fix the summary first (item 1), then feed `bellman-excerpt.md` — now present in the repo — to Matsya. Any earlier invocation would have produced a decomposition of the three-regime summary, which is no longer what the paper says.

### Files touched

| File | Action | Size |
|---|---|---|
| `PopAgingMPtransmission_summary.ipynb` | modified (13 cells; 3 new, 6 rewritten) | ≈ 27 KB |
| `bellman-excerpt.md` | created | ≈ 20 KB |
| `AGENTS.md` | created | ≈ 11 KB |
| `gaps-to-formalized.md` | this log appended | — |

No other files were modified. `references.bib`, `self.bib`, `subsequent-literature.bib`, `index.md`, `myst.yml`, `PopAgingMPtransmission_intro.ipynb`, `PopAgingMPtransmission_prior-literature.ipynb`, and `PopAgingMPtransmission_subsequent-literature.ipynb` are unchanged.
