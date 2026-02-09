# Proposed Revisions: Taxing Women: A Macroeconomic Analysis (2012)

## Prior Literature section to add

**Where to put it**: Insert a new section **right after** `# I. Summary` (or as `# I. Motivation & Prior Literature`, then renumber the rest). This keeps the reader oriented before the Bellman equations.

**Text to add (copy/paste)**:

The paper builds on two strands of work. First is **optimal income taxation** (Mirrlees 1971) and its application to family taxation: classic results (Boskin and Sheshinski 1983) and the policy debate over **joint filing / income splitting** (Rosen 1977; Kesselman 2008; McCaffery 2007) emphasize that efficiency depends on *whose* labor supply is most elastic. A central implication is that if the **secondary earner** (often the wife) has the more elastic participation response, then optimal policy tends to **shift lower marginal tax rates toward secondary earners** rather than taxing spouses symmetrically. Related theory on taxing couples and intra-household allocation (Apps and Rees 1988, 2007; “optimal income taxation of couples”) clarifies why participation choices and within-household interactions matter for incidence and welfare.

Second is the empirical/quantitative literature on **female labor supply**, especially the extensive margin. Surveys and evidence (Blundell and MaCurdy 1998; Keane 2010; Heim 2007; Blau and Kahn 2007) motivate modeling married women’s participation as highly responsive to taxes and family circumstances. Quantitative life-cycle and macro family-labor frameworks (Cho and Rogerson 1988; Attanasio, Low, and Sánchez‑Marcos 2008) make it feasible to evaluate gender-targeted or spouse-specific tax wedges in general equilibrium, which is what this paper does.

## Subsequent Literature section to add

**Where to put it**: Add near the end, **after** `# III Method of Computation`, as a short coda section like `# IV. Subsequent Literature / Where the field went next`. This avoids breaking the technical flow of the model while still giving the reader context and “so what?”.

**Text to add (copy/paste)**:

Later work takes the paper’s core quantitative insight—**secondary-earner participation is a first-order margin for tax design**—and pushes it in three directions. (i) **Cross-country measurement and comparison**: studies quantify how differences in tax-transfer systems map into married couples’ labor supply and participation across countries and over time (Bick and Fuchs‑Schündeln 2018; Bick et al. 2018). (ii) **Integrated family policy packages**: research increasingly evaluates taxes jointly with child-related transfers, childcare subsidies, and Social Security rules because these policies interact strongly with the extensive margin for married women (Kaygusuz 2015; Nishiyama 2019; Guner, Kaygusuz, and Ventura 2020; related measurement in Guner, Kaygusuz, and Ventura 2014). (iii) **Richer household mechanisms**: models add home production and time allocation, bargaining, and gender gaps in wages and childcare constraints to explain why elasticities differ by gender and family type (Duernecker and Herrendorf 2018; Olivetti and Petrongolo 2016).

Open questions remain about how best to discipline these mechanisms with micro evidence (reform-based identification, effective marginal tax rates for couples, time-use/childcare constraints) and how to separate policy effects from norms and institutions in cross-country work. A good path for new contributions is to combine a life-cycle heterogeneous-household model with careful institutional measurement of couple-level tax wedges and credible empirical moments on participation and time allocation.

## Other improvements

- **Fix a few factual/wording issues**
  - The “Journal” line should match the paper (your header says *Journal of Monetary Economics 59 (2012)*; keep it consistent everywhere).
  - “US tax system is replace by” → “is **replaced** by”; “gender netural” → “gender **neutral**”; “households that periodically makes” → “households that periodically **make**”.
- **Add a 5–7 bullet “Mechanism + Experiments” panel in the Summary**
  - What wedge changes (female vs male marginal tax rates / filing rules)
  - Why effects are large (extensive margin + human-capital/efficiency loss when out of work)
  - Which groups move most (married women by skill/children)
  - What is held revenue-neutral and how welfare is computed (transition vs steady state)
- **Clarify model objects early**
  - Add a short “State variables” bullet list right before the Bellman equations (what are \(a,h,x,z,q,b,j\)?).
  - In the married problem, add one bullet explaining how taxes differ under \(T^M(\cdot)\) vs \(T^S(\cdot)\) and how children enter (\(\chi(l_f)\), \(d(\cdot)\)).
- **Make the computation section more concrete**
  - One slide/bullet on “How transitions are computed” (solve policy functions, simulate/iterate distribution, compute welfare by cohort).
  - One bullet on “Welfare metric” (CEV or equivalent variation; winners/losers across cohorts).
- **Improve reproducibility**
  - Add a second link to the replication repository (if available) and state what is needed to run it (software/version, data sources).
- **Tighten visuals**
  - Label images with what they show (“Figure 1: …”, “Table 1: …”) and add 1–2 interpretation bullets under each.
  - Standardize image heights so the page doesn’t jump (e.g., 450–500px consistently).
