# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Guvenen, Kambourov, Kuruscu, Ocampo, and Chen

# %% [markdown]
# # "[Use it or lose it: efficiency gains from wealth taxation](https://fguvenendotcom.files.wordpress.com/2019/09/gkkoc-2019_v208_nber_wp_submit.pdf)" (Draft)
#
# - Notebook created by Mateo Velásquez-Giraldo
#

# %% [markdown]
# ### Summary
#
# This paper uses a two-sector OLG model with heterogeneous entrepreneurial agents to explore how wealth and capital income taxation differ in their welfare implications when there is rate-of-return heterogeneity.
#
# The main findings are as follows:
# * With rate-of-return heterogeneity, wealth taxation (as opposed to capital income taxation) shifts the tax burden towards unproductive entrepreneurs, and gives the productive ones better incentives to save. This generates a reallocation of capital towards productive entrepreneurs, raising output and allowing the government to lower labor income taxes.
# * In a model aimed at matching the U.S., the authors simulation exercises display an average welfare gain of 7.5% in consumption terms to newborns from switching from capital income to wealth taxation.
# * In the same model, the authors estimate that the optimal wealth tax rate is 2%-3%. In contrast, if only captial income and labor income taxes were available, it would be optimal to subsidize capital income.
#

# %% [markdown]
# ### Overview 
#
#
# #### Rate-of-return heterogeneity
#
# The recent empirical literature (e.g. Fagereng, Guiso, Malacrino and Pistaferri (2016a)) has found evidence that there is persistent heterogeneity on the risk-adjusted rates of return that households face on their assets. This is important because:
# * A theoretical result implying that wealth and capital-income taxation are equivalent relies on the assumption that returns on investment are homogeneous.
# * The empirical distribution of wealth has a thick tail that is not easily matched by models without rate-of-return heterogeneity.
#
# #### Non-technical methodological overview
#
# To assess the effects of wealth and capital income taxation, the authors construct a model in which agents have different entrepreneurial ability which also varies over time and generations. Therefore, unproductive agents can end up with large wealth from their predecesors or their youth. There are financial constraints that prevent wealth from perfectly reallocating to efficient entrepreneurs.
#
# The authors use simulations of the model under different tax policies to find their welfare implications.
#
# #### The two main effect of wealth taxation
#
# Switching from capital income taxes to wealth taxes has two main effects that help in understanding the results of the paper:
# 1. __"Use it or lose it" effect__: under capital income taxes, more productive entrepreneurs pay a higher taxes on their investments. Switching to wealth taxes reduces this phenomenon, redistributing the tax burden towards less productive entrepreneurs and allowing more productive ones to keep more of their capital than before.
#
# 2. __"Behavioral response"__: taxes compress the distribution of after-tax returns, but this phenomenon is much larger under capital income taxation. Thus, switching to wealth taxation spreads the distribution of the effective returns to investment and elicits a saving response that shifts capital towards more productive agents.

# %% [markdown]
# ### The model
#
# #### Households/entrepreneurs
#
# * Households face mortality risk each period and can live up to $H$ years. When they die, they are replaced by an offspring with their wealth. 
# * They supply their labor and use their wealth to produce differentiated intermediate products.
#
# On each period they choose:
# 1. How much labor to supply.
# 2. How much of their income to consume and save.
# 3. How much of their wealth to invest in their own firm versus a riskless bond.
# 4. How much of their intermediate good to produce.
#
# They maximize $$\mathbb{E}_0\left\{ \sum_{h=1}^H \beta^{h-1}\phi_h u(c_h, 1-l_h) \right\}$$ where $\phi_h$ is the unconditional probability of survival up to age $h$.
#
# #### Producers
#
# ##### Intermediate goods
#
# Each household $i$ produces an intermediate good $x_i$ through the linear production function
#
# $$x_{i,h} = z_{i,h}\times k_{i,h}$$
#
# where $z_{i,h}$ is the household's entrepreneurial productivity at age $h$ and $k_{i,h}$ is the ammount of final good used in production.
#
# ##### Final good
#
# A profit-maximizing, price-taking firm uses labor and intermediate goods to produce the final good according to $$Y = Q^\alpha L^{1-\alpha}$$ where $\left( \int x_{i,h}^\mu di dh \right)^{1/\mu}$.
#
# Notice that Q serves as a quality-adjusted index of capital stock.
#
# #### Labor and entrepreneurial productivity
#
# Entrepreneurial productivity is imprefectly inherited according to
#
# $$log(\bar{z}_i^{child}) = \rho_z log(\bar{z}_i^{parent}) + \varepsilon_{\bar{z}_i}$$
#
# and is altered through a three-state Markov chain $\mathbb{I}_{i,h}\in \{H,L,0\}$ that represents a "fast lane" (in which entrepreneurs with above-median ability are born), a normal state, and entrepreneurial retirement with transition matrix
#
# \begin{equation}
#     \Pi_{\mathbb{I}}\begin{bmatrix}
#     1-p_1-p_2 & p_1 & p_2\\
#     0 & 1-p_2 & p_2 \\
#     0 & 0 & 1
#     \end{bmatrix}.
# \end{equation}
#
# Actual productivity is then defined as
#
# \begin{equation}
# z_{i,h} = \begin{cases}
# \bar{z}_i^\lambda, & \text{if} \quad \mathbb{I}_{i,h} = H\\
# \bar{z}_i, & if \quad \mathbb{I}_{i,h} = L\\
# 0, & if \quad \mathbb{I}_{i,h} = 0\\
# \end{cases}
# \end{equation}
#
# with $\lambda > 1$.
#
# Labor productivity has a permanent imperfectly inherited component, a life cycle component, and a random AR(1) component.
#
# #### The individuals' decision problems
#
# ##### Static production/allocation problem
#
# Given his assets an productivity an entrepreneur decides how much capital to use in his firm
#
# \begin{equation}
#     \pi (a,z) = \max_{k \leq \vartheta(z)a} \{ p(z k)\times zk - (r+\delta)k \}
# \end{equation}
#
# where $p(\cdot)$ gives the price of the intermediate good. Notice that there is a collateral constraint, where $\vartheta(z)\geq 1$ and non-decreasing.
#
# ##### Dynamic problem
#
# The problem and value function of a household of age $h$ is given by
#
# \begin{align}
#     V_h(a;\mathbf{S}) = &\max_{c,l,a'} u(c,1-l) + \beta\frac{\phi_{h+1}}{\phi_{h}} \mathbb{E}[V_{h+1}(a',\mathbf{S}')|S]\\
#     \text{s.t.} \quad & a' = \mathcal{Y}(a,l;z,e,\kappa;\mathcal{T}) - c(1+\tau_c)\\
#     & a'\geq 0
# \end{align}
#
# where $\mathcal{Y}$ denotes the total disposable income of the individual after production and taxation, $\mathbf{S}$ is the vector of individual exogenous states, and $\mathcal{T}$ represents the tax system.
#
# #### Government
#
# The government can tax consumption, labor income, capital income, and wealth. It uses its funds to fund pension payments to retirees and a fixed level of exogenous expenditure. It is assumed to always run a balanced budget.

# %% [markdown]
# ### Results

# %% [markdown]
# ### Conclusion
