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

# Algan and Ragot (2009)

#  [Monetary policy with heterogeneous agents and borrowing constraints](https://spire.sciencespo.fr/hdl:/2441/3ao9avev669hj9hvol1l0lr6im/resources/2010-algan-ragot-monetary-policy.pdf)
- Notebook is created by Sinem Yagmur Toraman, edited by Asiye Irem Desdemir
- October 6, 2020 - February 9, 2026

## Summary
- **The paper studies how monetary policy operates in an economy with heterogeneous agents and borrowing constraints, and shows that inflation is no longer neutral for long-run capital accumulation once incomplete markets are taken seriously. Rather than operating through a representative-agent channel, inflation affects the economy through asymmetric portfolio adjustment across constrained and unconstrained households, generating a hump-shaped relationship between inflation and aggregate capital that is consistent with empirical evidence.**

The contribution of the paper to the literature is twofold:
- **Theoretical: the paper identifies a novel monetary transmission mechanism specific to heterogeneous-agent economies with binding borrowing constraints, whereby inflation induces differential portfolio responses across households and alters precautionary saving incentives.**
- **Quantitative: by embedding money into an Aiyagari (1994) incomplete-markets production economy, the model delivers a hump-shaped relationship between inflation and aggregate capital, highlighting the interaction between redistribution, self-insurance, and borrowing constraints.**

## Relation to the literature and subsequent developments

**The paper builds on the monetary growth and incomplete-markets literature by relaxing the representative-agent assumption and introducing binding borrowing constraints into the analysis of monetary policy. While earlier models emphasized either portfolio substitution effects (e.g. Tobin effects) or fiscal distortions, this framework shows that heterogeneity and market incompleteness fundamentally alter how inflation affects saving behavior and welfare. Subsequent research has built on these insights to study monetary policy transmission and redistribution in heterogeneous-agent economies, shifting the focus away from long-run capital accumulation per se toward distributional effects and balance-sheet channels. In this sense, the paper can be viewed as an early contribution to the heterogeneous-agent monetary policy literature that later culminates in modern HA macro frameworks.**

## Overview

### Heterogeneity in terms of borrowing constraints
**The paper highlights four channels through which inflation affects aggregate outcomes in a heterogeneous-agent economy, emphasizing that the relative strength of these channels depends on whether households face binding borrowing constraints.**
- Tobin effect (1965): This is the conventional portfolio substitution effect that arises when individuals switch from holding money to capital when there is no borrowing constraint.
- Phelps effect (1973): The negative impact of inflation tax on other distorting taxes, namely capital and labor tax.
- **Revenue effect: Under binding borrowing constraints, inflation-induced transfers raise disposable income for constrained households, increasing their demand for liquid assets and affecting aggregate saving behavior.**
- **Insurance effect: In incomplete markets, inflation tax revenues redistributed to households provide additional insurance against idiosyncratic risk. This reduces precautionary saving incentives and typically works in the opposite direction of the portfolio substitution (Tobin) effect.**

## The Model

The authors provide a simple and a general model, I will only report the general one:

Standard heterogenous agent model a la Aiyagari(1994) by embedding  money into the utility function

### Agents
#### Households
* Unit mass of ex-ante identical and infinitely lived households
* CES utility function following Charitys et al.(2000) given by



$u(c_i,m_i,l_i)=\dfrac{1}{1-\sigma}[({\omega}c_i^{\dfrac{\eta-1}{\eta}} +(1-{\omega})m_i^{\dfrac{\eta-1}{\eta}})^{\dfrac{\eta}{\eta-1}}(1-l_i)^{\psi}]^{1-\sigma}$

where

- $\omega$ : share parameter
- $\eta$ : interest elasticity of demand for real balances
- $\psi$ : weight of leisure
- $\sigma$ : risk aversion


* Idiosyncratic shocks on labor productivity, which follow a three state Markov process: $e_t\in E = ${$e_h, e_m, e_l$}$ $
* Households can insure themselves against employment risk in two ways:
 * Real money assets 
 * Risky asset which yields a return r
* There is linear tax on private income
* Distinguishing between 2 states: Binding and non-binding borrowing constraints

##### Dynamic Program

$v(q_t^{i}, e_t^{i})= max_{c_t^{i},m_t^{i},l_t,a_{t+1}^{i}} u(c_t^{i},m_t^{i},l_t^{i}) + {\beta}E[v(q_{t+1}^{i}, e_{t+1}^{i})]$

s.t.  $c_t^{i}+m_t^{i}+a_{t+1}^{i}=q_t^{i}+w_te_tl_t^{i}+{\mu}_t^{i}$

#### Firms

- Competitive firms
- Cobb-Douglas technology
- Single good with 2 inputs: $K_t$ and $L_t$

$Y_t = F(K_t,L_t) = K_t^{\alpha}L_t^{1-\alpha}$  $0<\alpha<1$

- Depreciation rate of $\delta$ which is installed one priod ahead
- There is no uncertainty
- Prices are set competitively

#### Government

Budget constraint of the government is given by:

$\int_0^1\mu_t^{i}di + G = \chi_t\tilde{r}_t K_t + \chi_t(L_t^{h}e_t^{h} + L_t^{l}e_t^{l}+L_t^{m}e_t^{m})\tilde{w}_t+\tau_t^{tot}$

where 
- $\tau_t^{tot}$: revenue from new money created at time t
- $\chi_t$: coefficients for the proportional taxes to the revenue of capital and labor

#### Monetary policy

- Monetary policy follows a simple rule
- Real quantity of money in circulation at time t is given by:

$\Omega_t = \dfrac{\Omega_{t-1}}{\Pi} + \pi\dfrac{\Omega_{t-1}}{\Pi_t}$

- Inflation tax in real terms is given by:

$ \tau_{t}^{tot} = \pi\dfrac{\Omega_{t-1}}{\Pi_t} $

where
- $\Omega$: aggregate real money

##### Market equilibria
- Final good market equilibrium:
$ C_t+K_{t+1} + G_t = Y_t+(1-\delta)K_t$
- Labor market equilibrium:
$ L_t=L_t^{s}$
- Financial market equilibrium:
$ K_{t+1}= A_{t+1}$
- Money market equilibrium:
$ \dfrac{M_t}{P_t}=\Omega_t$

where

$\Omega_t$: real quantity of money in circulation in period t

## Results

Authors conducted several experiments. Their results are based on the parameters that are calibrated to match the characteristics of U.S. economy. Here, I will provide a summary of their results.

### Individual Policy Responses
With an inflation rate of 0.75% in the benchmark economy, authors report that:
- low and medium productivity workers are net-dissavers
- high productivity workers are net-savers

Due to the borrowing constraint, concavity is observed at low levels of wealth. This portion corresponds to the workers with low or medium levels of productivity, indicating that they are net-dissavers (Figure 1). On the other hand, the high productivity workers are net-savers reflecting their motivation for consumption smoothing for less favorable states.

**This heterogeneity in saving behavior illustrates the core mechanism of the model: constrained households primarily use money as a self-insurance device, while unconstrained households adjust their portfolios intertemporally, generating differential responses to inflation.**

### Aggregate Policy Responses
#### Proportional lump-sum transfers and exogenous labor
When the increase in quarterly inflation from 0% to 10% is considered, the authors report that (Figure 3):
- demand for real money balances decreases continuously
- capital stock is increasing with a decreasing rate

#### Redistributive effects of inflation tax
This experiment can be described as a helicopter drop with symmetric transfers. The main observations can be listed as the following (Figure 4): 
- The incentive for self-insurance is dampened by monetary transfers 
- Hump-shaped pattern for aggregate capital stock
- **At relatively higher levels of inflation, the insurance and redistribution effects dominate precautionary saving incentives, while at lower inflation rates the portfolio substitution and precautionary-saving channels dominate, producing a hump-shaped response of aggregate capital.**

#### Endogenous labor, distorting taxes and redistribution of inflation taxes
##### Symmetric lump-sum redistribution of the inflation tax 
Table 4 reports the main quantitative results of the experiment along with the results that would have been observed under complete markets. It has been shown that the increase in monetary transfers dampens the incentive to work as it provides additional insurance. 
They further report the results under complete markets to highlight the impact of the borrowing constraints on the non-neutrality of inflation.

##### Change in distorting taxes
In this experiment, inflation tax is used by the government to decrease the distorting taxes on capital and labor. The results are reported in Table 4. The observations regarding the channels can be summarized as the following:
- Insurance effect is no longer relevant
- Substitution effect is still at work, reflecting a positive impact on the capital accumulation
- Phelps effect intensifies the positive impact of inflation on the capital stock 

### Sensitivity analysis
Authors conducted sensitivity analysis on 3 key parameters:  
- Elasticity of money demand
- Risk aversion
- Borrowing constraint
Results are reported in figures 6-7-8. 


## Conclusion

**By introducing heterogeneity and borrowing constraints into a monetary production economy, the paper shows that inflation affects the economy through channels that are absent in representative-agent models. Inflation induces asymmetric portfolio adjustments across households, alters precautionary saving incentives, and generates redistribution through inflation-tax transfers. These forces interact to produce a hump-shaped relationship between inflation and aggregate capital, with precautionary saving dominating at low inflation rates and insurance effects dominating at higher inflation rates.**

**Beyond its implications for capital accumulation, the paper highlights how borrowing constraints and incomplete markets fundamentally reshape the transmission and distributional consequences of monetary policy. In this sense, the model anticipates later heterogeneous-agent approaches to monetary policy, in which aggregate outcomes are driven not only by intertemporal substitution but also by balance-sheet effects and redistribution across agents.**

**These insights help rationalize why later work increasingly focuses on heterogeneous-agent monetary transmission and distributional effects rather than long-run growth alone.**


```{code-cell} ipython3

```
