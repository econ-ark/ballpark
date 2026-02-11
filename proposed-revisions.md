# Proposed Revisions: The Optimum Quantity of Debt (Aiyagari & McGrattan, 1998)

## Prior Literature section to add

**Placement**: Insert after the “I. Summary” section and before “II. The Model”.

Aiyagari & McGrattan (1998) builds on the Bewley–Aiyagari incomplete-markets tradition, where households face **uninsurable idiosyncratic risk** and **borrowing constraints**, generating **precautionary saving** and a non-degenerate wealth distribution (Bewley 1983; Aiyagari 1994). Within this framework, the paper studies government debt not just as a financing device, but as a **liquid safe asset** that can relax household liquidity constraints—an idea closely related to the “public debt as private liquidity” perspective (Woodford 1990).

The key gap the paper addresses is quantitative and normative: earlier work established the mechanisms (liquidity benefits vs. tax/distortion and crowding-out costs), but did not pin down **how much** risk-free public debt is optimal in a calibrated heterogeneous-agent general equilibrium model with taxes.

Key foundational papers (3–5):
- Bewley (1983), *A difficulty with the optimum quantity of money*
- Aiyagari (1994), *Uninsured idiosyncratic risk and aggregate saving*
- Woodford (1990), *Public debt as private liquidity*
- Chamley (1986), *Optimal taxation of capital income in general equilibrium*
- Barro (1979), *On the determination of the public debt*

## Subsequent Literature section to add

**Placement**: Insert after “III. Computational Method” and before the final “Link to original paper and replication code” slide/cell.

I found **18** papers in LitMaps that cite *The Optimum Quantity of Debt*.

The subsequent literature pushes the “debt as liquidity” mechanism into richer heterogeneous-agent policy environments. One frontier is **joint fiscal–monetary design**: debt/tax policy is analyzed alongside monetary policy and liquidity when households are constrained and markets are incomplete (e.g., Bilbiie & Ragot 2020; Grand et al. 2021). Another frontier is **methods and implementation**: improved computational techniques make optimal-policy HA models—especially transition dynamics—more tractable, enabling more realistic experiments and distributional analysis (Le Grand & Ragot 2023).

Open questions that repeatedly emerge include characterizing **optimal debt paths** (not just steady-state levels), integrating **financial-sector frictions/crises**, and strengthening **empirical validation** of the mechanism and welfare tradeoffs.

Most important subsequent papers:
1. Le Grand & Ragot (2023), *Optimal Policies with Heterogeneous Agents: Truncation and Transitions*: computational advances for HA optimal policy (esp. transitions).
2. Bilbiie & Ragot (2020), *Optimal monetary policy and liquidity with heterogeneous households*: HA liquidity constraints in optimal monetary policy.
3. Grand et al. (2021), *Optimal fiscal and monetary policy with heterogeneous agents*: integrated multi-instrument policy design.
4. Chakrabarti et al. (2021), *Targeted interventions: Consumption dynamics and distributional effects*: targeted policy + explicit distributional outcomes.
5. Carroll, Dolmas & Young (2021), *The politics of flat taxes*: political feasibility constraints on normative prescriptions.

(See `subsequent-literature-analysis.md` and `subsequent-literature.bib` for the full write-up and BibTeX.)

## Other improvements

- Add a short **“Replication roadmap”** cell near the top (after the title slide): what to reproduce (key figures/tables), required inputs, and stretch extensions (e.g., transition dynamics, alternative calibrations).
- Replace `models/We-Would-Like-In-Econ-ARK/OptimumDebt/README.md` (currently boilerplate) with a paper-specific README that lists: paper citation + links, what’s in the folder, how to run the notebook, and pointers to `prior-literature.md`, `subsequent-literature-analysis.md`, and the `.bib` files.
- Ensure the notebook has a clear **“References / Further reading”** block (could be a short bullet list at the end) pointing to the foundational + most important subsequent papers.
