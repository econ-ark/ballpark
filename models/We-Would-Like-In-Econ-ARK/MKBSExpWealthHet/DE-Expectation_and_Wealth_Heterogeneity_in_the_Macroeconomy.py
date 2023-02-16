# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] tags=[]
# # Mitman, Kohlhas, Broer, and Schlafmann (2022)
#
# # [Expectation and Wealth Heterogeneity in the Macroeconomy](http://perseus.iies.su.se/~akohl/EWHM_web.pdf)
#
# * Notebook is created Decory Edwards
# * Created on February 14, 2022
# -

# ## Introduction
#
# As the expectations of agents in the economy has become an important feature of macroeconomic modelling, recent work by Mitman, Kohlhas, Broer, and Schlafmann (2022) adds to this literature by developing a model of expectation formation for households that is consistent with the data. That is, recent empirical work suggests that households not only have significantly different expectations but that these differences are systematically correlated with some economics characteristics of the household (ex. *wealth*). 
#
# The model in this paper develops a theory incorporates households' decisions to acquire information into the standard framework of macroeconomic models of heterogeneous agents with a precautionary savings motive, who face aggregate risk, and have the choice to invest in a single, riskless asset.  
#

# + [markdown] tags=[]
# ## Empirical Findings
#
# The key empirical insight of the paper consolidates data from the Survey of Consumer Expectations (SCE) regarding (i) a panel of point and density forecasts for relevant macroeconomic and financial variables and (ii) survey data on the composition of household wealth to provide evidence of a systematic relationship between a household's wealth holdings and the accuracy of their expectations regarding uncertain economic events. 
#
# Namely, the article finds a **non-monotone relationship between wealth and expectations**. Wealthier households tend to have more accurate forecasts, but this pattern from the data only holds for those households above the 20th percentile of the wealth distribution. In fact, households below this 20th percentile threshold have expectations that are closer to those of the most wealthy households.

# + [markdown] tags=[]
# ![ ](MKBS_fig1.pdf)
# -

# This analysis of the SCE data gives motivation for the authors' proposed model of heterogeneity in expectations, embedded in the standard heterogeneouos agent model framework. This is done by allowing for households at a given level of wealth to choose the optimal level of information to acquire. 

# ## Quantitative Results
#
# ### Information acquisition and savings behavior 
#
# In these types of macroeconomic models, agents have two main reasons to save across periods: to smooth consumption over their lifetime due to potential loss in income (precautionary savings) and to reap the benefits of movements in the rate of return to assets (intertemporal substitution).
#
# With this in mind, the first result of the paper describes how endogenous information choice affects households' savings decisions by analyzing the two cases: 
#
# 1. The *static cost* of not being informed: This is done by keeping a household's prior over the capital stock fixed, which in turn fixes their expectation regarding the rate of return to assets. So, this is an attempt to isolate the effect of the precautionary savings motive on savings behavior given the household's choice of acquiring information.
#
# The paper finds that **informed households save more than uninformed in recessions** (captured by $z_l$) since they can accurately assess that the probability of becoming unemployed is higher. This strengthens the effect of the precautionary savings motives for *all* households; thus, uninformed housholds make a mistake in their optimal savings decision given the state of the economy.
#
# Since the precautionary savings motive is stronger at lower levels of wealth, the difference in savings behavior at lower levels of wealth is more pronounced given the choice to acquire information. This can be seen in figure 3.
#
# ![](MKBS_fig3.pdf)
#
# 2. The *dynamic cost* of not being informed: The choice to not acquire information will lead to mean-biased expectations for some households. The differences in household savings behavior in this case is compounded by the desire to substitute intertemporally. However, information choices will lead to some households making worse savings decisions as their expectations on the dynamic capital stock will determine their expectation on the rate of return.  
#
# Further, the paper finds that uninformed households additionally save less in recessions than informed households. As the **aggregate capital stock falls during recessions, households who choose not to acquire information believe that the capital stock is larger** than it is. This in turn leads to an **expectation on the rate of return to their savings that is lower** than what it is, **given the fall in the capital stock**. 
#
# The effect of underpredicting the rate of return during recessions (or overpredicting during booms) given the choice to not acquire information can be significant even at higher levels of wealth. This is captured in figure 4.
#
# ![ ](MKBS_fig4.pdf)
#
# ### Individual state-variables and information acquisition
#
# After describing the savings behavior of households given their decisions to acquire information, the paper discusses how this behavior is sensitive to the realization of the relevant state-variables for a given household. Notably, information choices will be described by the probability to acquire information.
#
# 1. *Prior over productivity*
#
# Nonsurprisingly, households with less informative prior expectations regarding productivity levels are more likely to acquire information at all wealth levels.
#
# From here, to understand the rest of this argument, it is best to consider the result conditional on a household's employment status, since this implies markedly different savings behavior.
#
# $\hspace{1mm}$ 2A. *Employed households (main savers in the economy)*
#
# **As wealth levels increase, employed households are more likely acquire information**. Since the precautionary savings motive is not as strong for these households who are far from the borrowing constraint, they are making the comparison between the cost of acquiring information and the benefit of accurately predicting the rate of return to financial assets. 
#
# $\hspace{1mm}$ 2B. *Unemployed households (dissavers in the economy)*
#
# When **sufficiently far enough from the borrowing constraint, unemployed households are very likely to acquire information**. This is due to the incentive against making a savings mistake close to the borrowing constraint. As wealth increases, the value of information acqusition falls in this regard, so the probability of acquiring information does as well. However, at higher levels of wealth, the same comparison between costs and benefits for employed households will cause unemployed households to also become more likely to acquire information.  
#
# These effects can be seen in figure 5. 
#
# ![ ](MKBS_fig5.pdf)
#
# ### Matching the forecast accuracy data
#
# The previous results describe how wealth and employment status affect a household's decision to acquire information, as well as how a household's optimal savings behavior is affected by their relevant state-variables.
#
# The next finding shows that the interaction between information and savings choices allows the model to match the SCE data on household expectations.
#
# Recall that the SCE data featured a non-montone relationship between wealth and expectations. The model presented in MKBS (2022) adds some economic intuition to this relationship. Consider the following graphic (figure 6) from the paper.
#
# ![ ](MKBS_fig6.pdf)
#
# Households with lower levels of wealth are, on average, more likely to be unemployed. Figure 5 showed that the model predicts that these households acquire information with high probability. This corresponds to these same households having more accurate forecasts, as reflected in the SCE data. 
#
# Furthermore, as wealth levels increase, the probability of acquiring information eventually becomes monotonic in wealth, as did the forecast accuracy in the SCE data. This can be seen in figure 6 as well.
#
# ### Aggregate implications
#
# Following the discussion of the role of savings and information for individual households, the paper then describes the aggregate implications of the previous findings. From here on out, it will be useful to keep in mind three different "variations of the economy":
#
# 1. Full-information economy: all households acquire information every period.
#
# 2. Exogenous-information economy: households probability of acquiring information is exogenously given.
#
# 3. (Benchmark) Endogenous-information economy: this is the model presented in the paper, where agents choose in every period whether or not to acquire information.
#
# When the benchmark model is compared to the full-information economy, it is clear that uninformed households systematically underpredict the capital stock in booms (and overpredict it in recessions). These uninformed households, not present in the full-information economy, will relatively overpredict the returns to savings in booms. 
#
# Thus, **in equilibrium the benchmark economy "overaccumulates" capital in booms and "underaccumulates" in recessions**. This corresponds to **larger fluctuations in output, consumption, and investment.**
#
# The exogenous-information economy also features this increase in volatility for relevant aggregate variables, but it is **less pronounced than in the benchmark model**. This is because it is the middle-to-rich households, who combine to hold the bulk of the capital stock, that choose not to acquire information.  
#

# ### Implications for the Distribution of Wealth
#
# After discussing the implications for the aggregate capital stock, the paper does a further analysis on the wealth distribution to discuss inequality.
#
# First, when comparing the benchmark model to the full-information economy, there is more mass placed at the bottom and near the top of the wealth distribution. Consequently, the model implies fewer middle-income and extremely wealthy households. This can be seen in figure 7.
#
# ![ ](MKBS_fig7.pdf)
#
# When comparing the benchmark model to the exogenous-information economy, these effects on the distribution of wealth are less pronounced than when information is endogenously determined. 
#
# To see this, we first describe the decomposition of the interaction between information and the distribution of wealth in the following three cases:
#
# 1. *General equilibrium effects*
#
# This experiment is done by having the law of motion for capital be the one from the benchmark, endogenous information choice setting. Agents have full information about $z_t$, and make optimal decisions given this surprise in the aggregate capital stock they face (as opposed to the benchmark where some agents would be surprised AND not have information about $z_t$).
#
# 2. *The effect of exogenous, incomplete information*
#
# Now, a given household's optimal behavior is the same as the case where there is exogenous, incomplete information (infrequent updating of beliefs, as opposed to full information about $z_t$). They believe that the law-of-motion for capital is the one from the benchmark model. The resulting distribution, when compared to the one resulting from the previous case, isolates the effect of incomplete information on households.
#
# 3. *The effect of incomplete information from endogenous information choice*
#
# The last experiment is to compare the distribution that arises from the previous case with infrequent updating of beliefs given the law of motion from the benchmark case, with the distribution from the benchmark case. This should isolate the additional effects of heterogeneous information choices on the wealth distribution, since now the infrequent, updated beliefs are a result of optimal household behavior.
#
# This can be seen in figure 8 and in table 3.
#
# ![ ](MKBS_fig8.pdf)
#
# ![ ](MKBS_tab3.pdf)
#
# The key insight regarding the effect of incomplete information on the distribution of wealth is that the increase in volatility and fluctuations in the capital stock leads to random savings behavior, which becomes more important for households with larger wealth holdings.

# + [markdown] tags=[]
# ## Aggregate effects of Wealth Tax Policy
#
# The final analysis of the paper considers the aggregate effects of a wealth tax on households in this setting of endogenous information choice.
#
# Specifically, consider the following linear wealth tax $\tau_k > 0$, which modifies the expression for a given household's cash-at-hand $m_i$:
#
# $$ m_i = r k_i + (1 - \tau) \epsilon_i w \bar{l} + \mu (1 - \epsilon) w + (1 - \delta - \tau_k)k_i . $$
#
# There is a direct effect of the wealth tax: a reduction in the size of the aggregate capital stock. However, recall the established relationship between wealth and information acquisition in this model. This causes a **reduction in the average level of information in the evonomy since lower-wealth level households acquire information less frequently**. Furthermore, with less information in the economy on average, there is **more volatility in the aggregate capital stock**. 
#
# As for the distribution of wealth, the implementation of the wealth tax $\tau_k$ actually increases the number of super-rich households (i.e. those with more than \\$3.5 million in wealth) in the model. The number of households below \\$600,000 in wealth also increases, while those in the \\$600,000 to \\$3.5 million range falls. 
#
# Notably, if one measuring inequality in the distribution of wealth by using a measure such as the Gini coefficient (which is typically done for these types of HA models), then the **wealth tax actually increases wealth inequality**. This is opposite of the intended effect of the policy implementation! This can be seen in figure 9.
#
# ![ ](MKBS_fig9.pdf)
#
# Lastly, the paper cites three forces as an explanation for why the wealth tax policy could have such an unintended effect on the level of inequality in the wealth distribution.
#
# 1. The model of endogenous information choice has a considerable share of high-wealth households (i.e. those with at least \\$500,000 in wealth) who are disproportionately effected by the tax, as these households are less likely to acquire information. Thus, their wealth share decreases.
#
# 2. Households with less wealth holdings are more likely to be uninformed, as they are closer to the borrowing contraint. These households make worse savings decisions with the introduction of the wealth tax, which decreases their share of wealth as well.
#
# 3. Recalling that the wealth tax decreases the average level of information in the economy, the aggregate capital stock becomes more volatile. For the super-wealthy households, they now face "random savings rates". But, these households with more than \\$3.5 million in wealth are significantly more likely to acquire information and make correct savings decisions. Thus, their share of the wealth increases.
# -


