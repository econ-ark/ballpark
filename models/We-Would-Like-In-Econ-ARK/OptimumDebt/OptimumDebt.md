---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"slideshow": {"slide_type": "slide"}}

<font size="10"><b><center>The Optimum Quantity of Debt</center></b></font>
<br><br>
<font size="6"><b><center>Author: S. Rao Aiyagari and Ellen R. McGrattan</center></b></font>
<font size="6"><b><center>Journal of Monetary Economics 42 (1998)</center></b></font>
<br><br>
<font size="6"><b><center>Slides by: Syareza Tobing (Ray)</center></font>
     <font size="6"><b><center>February 2021</center></b></font><br>
<font size="6"><b><center>Edits by: Yiran Ma (Emma) (Feb 2026)</center></font>

+++ {"slideshow": {"slide_type": "slide"}}

# I. Summary

* The paper undertakes a normative exercise to calculate optimum quantity of risk-free public debt and the welfare cost of being outside the optimum using US data.


+++ {"slideshow": {"slide_type": "fragment"}}

* It studies economies with a large number of infinitely lived households whose saving behaviour is influenced by precautionary saving motives and borrowing constraints

+++ {"slideshow": {"slide_type": "fragment"}}

* It employs two models; 
    * Inelastic labor supply and lump-sum taxes
    * Elastic labor supply and proportional taxes (benchmark)

+++ {"slideshow": {"slide_type": "subslide"}}

Effects of government debt on welfare:
* An increase in debt increases the return on assets increasing welfare (+)
* Taxes have distributional effects which lowers welfare (-)
* Crowding out of capital which reduces percapita consumption (-)

+++ {"slideshow": {"slide_type": "subslide"}}

* It finds that the welfare gains to being at the optimum rather than the US level is trivially small


<center><img src="P1Figure1.png" style="height:500px"></center>  

+++

# Prior Literature (what this paper builds on)

Aiyagari & McGrattan (1998) builds on the Bewley–Aiyagari incomplete-markets tradition, where households face **uninsurable idiosyncratic risk** and **borrowing constraints**, generating **precautionary saving** and a non-degenerate wealth distribution (Bewley 1983; Aiyagari 1994). Within this framework, the paper studies government debt not just as a financing device, but as a **liquid safe asset** that can relax household liquidity constraints—an idea closely related to the “public debt as private liquidity” perspective (Woodford 1990).

The key gap the paper addresses is quantitative and normative: earlier work established the mechanisms (liquidity benefits vs. tax/distortion and crowding-out costs), but did not pin down **how much** risk-free public debt is optimal in a calibrated heterogeneous-agent general equilibrium model with taxes.

**Key foundational papers (3–5):**
- Bewley (1983), *A difficulty with the optimum quantity of money*: canonical incomplete-markets/liquidity-constraint framework.
- Aiyagari (1994), *Uninsured idiosyncratic risk and aggregate saving*: quantitative GE version with capital and wealth distribution.
- Woodford (1990), *Public debt as private liquidity*: debt as liquidity and a reason Ricardian equivalence can fail.
- Chamley (1986), *Optimal taxation of capital income*: benchmark for thinking about distortionary tax costs in GE.
- Barro (1979), *On the determination of the public debt*: Ricardian benchmark the constrained-agent setting departs from.

+++ {"slideshow": {"slide_type": "slide"}}

# II. The Model

### A growth model with uninsured idiosyncratic shocks

+++ {"slideshow": {"slide_type": "subslide"}}

* The model employed is an augmented version of the model in Aiyagari (1994)
    * Augmented to permit growth and to include government debt, lump-sum taxes and government consumption.
* The consumer's problem is:

+++ {"slideshow": {"slide_type": "fragment"}}

$\max _{\left\{\tilde{c}_{t}, \tilde{a}_{t+1}\right\}} \quad E\left[Y_{0}^{1-v} \sum_{t=0}^{\infty}\left[\beta(1+g)^{1-v}\right]^{t} \tilde{c}_{t}^{1-v} /(1-v) \mid \tilde{a}_{0}, e_{0}\right]$

subject to

$\begin{array}{l}
\tilde{c}_{t}+(1+g) \tilde{a}_{t+1} \leq(1+r) \tilde{a}_{t}+\tilde{w} e_{t}-\tau \\
\tilde{c}_{t} \geq 0, \tilde{a}_{t} \geq 0, t \geq 0
\end{array}$

$
\\
$

$
\begin{align}
 Y &: per \ capita \ output \\
 \beta &: discount \ factor \\ 
 g &: rate \ of \ technical \ progress \\
 v &: relative \ risk \ aversion \ coefficient \\
 \tilde{c} &: output \ normalized \ per \ capita \ consumption \\
 \tilde{a} &: output \ normalized \ per \ capita \ asset \ held \ by \ consumers \\
 \tilde{w} &: output \ normalized \ per \ capita \ wage \\
 e &: individual \ labor \ productivity
\end{align}
$

+++ {"slideshow": {"slide_type": "subslide"}}

* The effect of an increase of the quantity of debt on welfare is captured by the following welfare criterion

$\Omega=\iint V(a, e) \mathrm{d} H(a, e)$

where:

$
\begin{align}
 V(a, e) &: optimal \ value \ function \\
 H &: steady-state \ joint \ distribution \ of \ assets \ and \ productivity
\end{align}
$

+++ {"slideshow": {"slide_type": "fragment"}}

The optimality criterion is utilitzed for three reasons:
* Can be thought of as a utilitarian social welfare function
* Can be though of as a steady-state ex ante welfare
* Computationally tractable

+++ {"slideshow": {"slide_type": "slide"}}

# III Computational Method

$
\begin{array}{l}
\max _{\left\{\tilde{c}_{t}, l_{t}, \tilde{a}_{t+1}\right\}} \quad E\left[\sum_{t=0}^{\infty} \tilde{\beta}^{t}\left\{\frac{\left(\tilde{c}_{t}^{\eta} l_{t}^{1-\eta}\right)^{1-\mu}}{1-\mu}+\frac{1}{3} \zeta\left(\min \left(\tilde{a}_{t}, 0\right)^{3}+\min \left(1-l_{t}, 0\right)^{3}\right)\right\} \mid \tilde{a}_{0}, e_{0}\right] \\
\text { subject to } \tilde{c}_{t}+(1+g) \tilde{a}_{t+1} \leq(1+\bar{r}) \tilde{a}_{t}+\bar{w} e_{t}\left(1-l_{t}\right)+\chi
\end{array}
$

+++ {"slideshow": {"slide_type": "subslide"}}

$
\begin{array}{l}
R(x, i ; \alpha)=\eta(1+g) c\left(l^{*}(x, i ; \alpha)\right)^{\eta(1-\mu)-1} l^{*}(x, i ; \alpha)^{(1-\eta)(1-\mu)} \\
-\tilde{\beta}\left\{\sum_{j} \pi_{i, j} \eta(1+\vec{r}) c\left(l^{*}(\alpha(x, i), j ; \alpha)\right)^{\eta(1-\mu)-1} \cdot l^{*}(\alpha(x, i), j ; \alpha)^{(1-\eta)(1-\mu)}\right. \\
\left.+\zeta \min (\alpha(x, i), 0)^{2}\right\}
\end{array}
$

The computational task done by the author is to find an approximation for $\alpha(x, i)$-say, $\alpha^h(x, i)$-which implies that $R(x, i ; \alpha^h)$ is approximately equal to zero for all $x$ and $i$, which they do by applying a finite element method.

+++

# Subsequent Literature (what came next)

I found **20** papers in LitMaps that cite *The Optimum Quantity of Debt*.

The subsequent literature pushes the “debt as liquidity” mechanism into richer heterogeneous-agent policy environments. One frontier is **joint fiscal–monetary design**: debt/tax policy is analyzed alongside monetary policy and liquidity when households are constrained and markets are incomplete (e.g., Bilbiie & Ragot 2020; Grand et al. 2021). Another frontier is **methods and implementation**: improved computational techniques make optimal-policy HA models—especially transition dynamics—more tractable, enabling more realistic experiments and distributional analysis (Le Grand & Ragot 2023).

Open questions that repeatedly emerge include characterizing **optimal debt paths** (not just steady-state levels), integrating **financial-sector frictions/crises**, and strengthening **empirical validation** of the mechanism and welfare tradeoffs.

**Most important subsequent papers (where the field is heading):**
1. Le Grand & Ragot (2023), *Optimal Policies with Heterogeneous Agents: Truncation and Transitions*: computational advances for HA optimal policy (esp. transitions).
2. Bilbiie & Ragot (2020), *Optimal monetary policy and liquidity with heterogeneous households*: HA liquidity constraints in optimal monetary policy.
3. Grand et al. (2021), *Optimal fiscal and monetary policy with heterogeneous agents*: integrated multi-instrument policy design.
4. Chakrabarti et al. (2021), *Targeted interventions: Consumption dynamics and distributional effects*: targeted policy + explicit distributional outcomes.
5. Carroll, Dolmas & Young (2021), *The politics of flat taxes*: political feasibility constraints on normative prescriptions.

(See `subsequent-literature-analysis.md` and `subsequent-literature.bib` in the repo root for the full write-up and BibTeX.)

+++ {"slideshow": {"slide_type": "slide"}}



Link to original paper and replication code
* [Aiyagari-McGrattan](http://aefweb.net/AefArticles/aef040111.pdf)
* [Replication](http://users.cla.umn.edu/~erm/data/sr203/)
