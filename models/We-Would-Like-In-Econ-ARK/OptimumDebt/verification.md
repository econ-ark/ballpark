# Verification: Matsya Output vs. Published Paper

I compared Matsya's stage decomposition, dolo-plus YAML draft, and improved
markdown against the published Aiyagari & McGrattan (1998) paper and my
notebook summary.

**Accepted:** The perch structure (arrival with assets and productivity,
decision with cash-on-hand, continuation with end-of-period assets) correctly
captures the paper's timing. The EGM inversion recipe, envelope condition, and
the Markov conditional expectation in the forward mover all match the
paper's recursive formulation. The treatment of prices and taxes as
stage-external parameters faithfully reflects the paper's partial-equilibrium
household block.

**Edited:** Matsya's first YAML draft omitted the $(1+g)$ growth factor in
the decision-to-continuation transition. The paper's budget constraint (Sec.
II, equation (1)) has $(1+g)\tilde{a}_{t+1}$ on the left-hand side. The
resolution adopted here is to restore the factor explicitly in the
dcsn-to-cntn transition ($\tilde{a}' = (\tilde{m} - \tilde{c})/(1+g)$) and
to propagate it through the EGM reverse transition
($\tilde{m}_{[\succ]} = (1+g)\tilde{a}' + \tilde{c}_{[\succ]}$) and the
Inverse Euler ($\tilde{c}_{[\succ]} = (\tilde{\beta}\cdot\mathrm{v}'_\succ/(1+g))^{-1/\nu}$).
Keeping the factor visible rather than absorbing it into the effective
discount factor preserves a 1-to-1 correspondence between the YAML and
the paper's equation numbers. I also added an explicit parameter
restriction $\tilde{\beta} < 1$ that was absent from the notebook summary
but required for the contraction mapping.

**Rejected:** Nothing was rejected outright. Matsya's treatment of the
elastic-labor Model B as "same stage template, expanded control space" is
consistent with the paper. The penalty-function formulation in the
notebook was correctly identified as a solver-level device rather than part
of the formal DP.
