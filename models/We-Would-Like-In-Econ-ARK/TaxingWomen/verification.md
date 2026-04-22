# Verification (short)

Matsya / formalization-layer claims checked against Guner, Kaygusuz, and Ventura (2012), "Taxing Women: A Macroeconomic Analysis," *Journal of Monetary Economics* 59(1), 111–128.

**Accepted (paper-verified).** The recursive structure of the three household problems (single male, single female, married) as in GKV 2012 §2.2 eqs. (1)–(3); additively separable log utility per eq. (3); permanent-types structure for $(z, x, q, b)$ with no within-period shocks per §2.1; wife's human-capital law of motion $h' = \exp[\ln h + a_j^x\chi(l_f) - \delta(1-\chi(l_f))]$ with participation-indicator driver $\chi(l) = \mathbf{1}\{l>0\}$ per §2.1 and Table 3; child-care cost schedule with $d(1) = 0.064$, $d(2) = d(3) = 0.049$ per Table 3; log-progressive income tax $\tau(\tilde y) = \zeta_1 + \zeta_2 \ln \tilde y$ with $(\zeta_1, \zeta_2)$ indexed by filing status × young-children indicator per §2.3 and Table 2; terminal condition $V_{J+1} \equiv 0$ per §2.2; revenue-neutral stationary-OLG equilibrium close per §2.4.

**Edited.** The initial excerpt used placeholder utility kernels $U_m^S, U_f^S, U^M$ with no functional-form content; corrected to the additively separable log forms of GKV 2012 eq. (3) with the married-household kernel written as a **single** $\ln c$ (unitary objective), not $u_f + u_m$ with two copies of $\ln c$. The initial excerpt also lacked the tax function (now per Table 2), the calibration (now per Table 3), $\chi(l) = \mathbf{1}\{l>0\}$, and the child-care schedule — all needed by Matsya to produce a correct YAML. See `TaxingWomen_Summary.ipynb` §II.0 for the committed primitives and `bellman-excerpt.md` for the symbol table.

**Rejected.** Matsya's initial `ShockRealization` stage. GKV 2012 §2.1 draws $(z, x, q, b)$ once at birth/marriage; there is no Markov process on $z$ and no i.i.d. period draw on $q$. A within-period shock stage is fictitious and was removed; the arrival-to-decision mover is the identity on every stage and $\mathbb{T} = \mathbb{I} \circ \mathbb{B}$ with degenerate $\mathbb{I}$.

**Edited (decomposition).** An earlier draft proposed a two-stage branching decomposition (labor-branch → cons-savings) with separate work/home continuation legs. Superseded in `bellman-excerpt-SMD-polished.md` by a four-stage non-branching decomposition $\text{female\_labor} \to \text{male\_labor} \to \text{consumption\_savings} \to \text{disc}$ adapted from `TaxingWomen_bellman-stages.ipynb`; the extensive margin at $l_f = 0$ is handled as a corner of the continuous optimization rather than a discrete branch. The two are mathematically equivalent when the tax function is smooth within each filing-status × young-children cell; the non-branching form keeps the stage interface continuous and isolates the only EGM-amenable step (`consumption_savings`) on its own.

**Unverified (DDSL-side claims).** The following are framework conventions adopted in `bellman-excerpt.md`, `bellman-excerpt-SMD-polished.md`, and `dolo-plus-draft.yaml`; GKV 2012 does not make and cannot verify them:

- the arrival / decision / continuation perch tripartition itself;
- the four-stage ordering (placing `consumption_savings` after both labor stages, in particular, to isolate the Euler-inversion step on log utility);
- treating the discount factor as a separate stub stage `disc` rather than absorbing $\beta$ into the continuation value of `consumption_savings`;
- handling the extensive margin at $l_f = 0$ as a corner of the continuous control rather than as a branching stage on wife's $d \in \{\text{work}, \text{home}\}$;
- the connector-as-pure-rename convention $(a', h') \leftrightarrow (a, h)$ between periods;
- the workaround `I_guard = \max(I_\text{total}, \varepsilon)` for the $\ln(I/\bar I)$ singularity as $I \to 0$;
- the stage-instantiation workaround for $(\zeta_1, \zeta_2)$ parameter switching on (filing status × young children).

**Paper-verify pending.** Two functional-form specifics are flagged with $\dagger$ in `TaxingWomen_Summary.ipynb` §II.0 and in the symbol table of `bellman-excerpt.md`: (i) the additive channel $(l_f + k_y\kappa)$ through which the wife's young-child time cost enters her disutility; (ii) the additive form $q\,\chi(l_f)$ of the wife's participation utility cost in the married-household objective. Both are consistent with the calibration in GKV 2012 Table 3 but should be cross-checked against GKV 2012 eq. (3) and the surrounding text before the formalization layer is treated as paper-verified.

**Matsya session:** `topics2026-TaxingWomen`.
