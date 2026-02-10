# Proposed Revisions: Monetary Policy with Heterogeneous Agents (Görnemann, Kuester, Nakajima, 2012)

## 1. Where to insert each section

- **Prior Literature**  
  **Insert after the "Overview" block** (after the cell that says *"The goal of the paper is to establish the extent to which monetary policy in the US might have distributional effects..."*).  
  In the current notebook that is **after cell index 6**. Add two new markdown cells: one with the heading `## Prior Literature`, the next with the draft text below.

- **Subsequent Literature**  
  **Insert after the "Results" section and before "Conclusion"** — i.e. after the welfare subsection (after the cell that contains the Table7 image and the sentence about the top 5% gaining 0.02% consumption-equivalent).  
  In the current notebook that is **after cell index 54**. Add two new markdown cells: one with the heading `## Subsequent Literature`, the next with the draft text below.

---

## 2. Prior Literature — draft text (ballpark-style)

**Heading (new cell):** `## Prior Literature`

**Body (new cell):**

The paper combines two strands of macroeconomics. The first is **New Keynesian monetary policy**: nominal rigidities and interest-rate rules as the main transmission mechanism. Woodford (1998) showed that inflation can be analyzed in a “cashless” setup where the central bank sets interest rates rather than the money supply, which is the standard basis for modern DSGE policy analysis. Much of that work used a representative agent and ignored distribution.

The second strand is **heterogeneous-agent macroeconomics** with incomplete markets and labor market frictions. Aiyagari (1994) showed that uninsurable idiosyncratic risk and borrowing limits generate precautionary saving and realistic wealth inequality. Later work (e.g. Heathcote, Storesletten, and Violante 2009) clarified how heterogeneity matters for aggregates and welfare. Search and matching were brought into general equilibrium models of unemployment (e.g. Mortensen and Pissarides 1994; Merz 1995), and combined with nominal rigidities (e.g. Walsh 2005; Krause and Lubik 2007; Blanchard and Galí 2010). The distributional effects of inflation and monetary policy were studied in incomplete-markets settings (e.g. Erosa and Ventura 2002; Doepke and Schneider 2006; Meh and Terajima 2011). GKN’s contribution is to integrate heterogeneous households, incomplete markets, and search frictions into a single New Keynesian model, so that the redistributive and welfare effects of monetary policy can be quantified.

---

## 3. Subsequent Literature — draft text (ballpark-style)

**Heading (new cell):** `## Subsequent Literature`

**Body (new cell):**

Later work has extended the analysis of **monetary policy in heterogeneous-agent New Keynesian (HANK) models**. One line of research focuses on transmission mechanisms: how marginal propensities to consume, wealth distributions, and labor income risk change aggregate and distributional responses to monetary shocks (e.g. Herkenhoff 2015; Chen 2018; Alves 2019). Another line deepens the role of **labor market frictions** in HANK models—unemployment risk, job-finding rates, and wage rigidity—and shows that they amplify distributional effects and matter for optimal policy (e.g. Hagedorn 2018; Bertsch 2017; Jones 2017). The frontier combines rich household heterogeneity with empirically grounded labor market dynamics and policy rules; open questions include identification of redistribution channels in the data and the interaction of monetary and fiscal policy in HANK environments.

---

## 4. Other small improvements

- **Typos and wording (search-and-replace):**  
  - "aggegate" → "aggregate"  
  - "attibutes" → "attributes"  
  - "responces" → "responses" (all instances)  
  - "exogeneous" → "exogenous"  
  - "intermedaite" → "intermediate"  
  - "procuers" → "producers"  
  - "autogregressive" → "autoregressive"  
  - "compenents" → "components"  
  - "constraines" → "constrained"  
  - "gaint" → "gains" (welfare gains)  
  - "wealthies" → "wealthiest"  
  - "loses" → "losses"  
  - "fof" → "of" (in "type distribution fof households")

- **Citation:**  
  - "Mortensen and Pissaridis" → **Mortensen and Pissarides** (correct spelling) in the "Incomplete Markets and heterogeneity" cell.  
  - "Krusell et al., 2010" in the same cell is ambiguous; consider replacing with a specific reference (e.g. **Krusell and Smith (1998)** for heterogeneity, or the actual 2010 paper if different).

- **Structure:**  
  - The link to the working paper is already in the title; no change needed.  
  - Optionally add a one-sentence “Key result” under the title (e.g. *Contractionary monetary policy raises welfare for the wealthiest 5% and lowers it for the rest.*) to help scanners.

- **Consistency:**  
  - Use **GKN** or **Görnemann, Kuester, and Nakajima (2012)** consistently in the new Prior/Subsequent sections and in the Conclusion.

- **Citations:**  
  - If the notebook supports citations (e.g. jupyterlab-citation-manager), add keys for the Prior and Subsequent literature so they appear in the bibliography; otherwise keep the inline “Author (year)” form as in the draft text above.
