# Ballpark entry: Gornemann, Kuester, and Nakajima (2012)

> Structured brief for coding agents (Claude Code, Cursor, etc.). Human-facing content lives in [`GKNMonetaryPolicyHA.ipynb`](GKNMonetaryPolicyHA.ipynb).

## Paper

- **Citation:** Gornemann, Nils, Keith Kuester, and Makoto Nakajima (2012), "Monetary Policy with Heterogeneous Agents," Philadelphia Fed Working Paper 12-21.
- **DOI:** [10.21799/frbp.wp.2012.21](https://doi.org/10.21799/frbp.wp.2012.21)
- **Core model:** New Keynesian DSGE with heterogeneous households (employment status × skill × mutual-fund shares), search-and-matching labor market frictions, incomplete asset markets, and nominal rigidities. Households choose consumption and mutual-fund shares; aggregate state includes capital, employment, TFP, monetary-policy shock, and the cross-sectional distribution. Closed by a Krusell-Smith forecasting rule.
- **Why in-ballpark:** The paper is among the first to rigorously analyze the distributional consequences of monetary policy in a heterogeneous-agent New Keynesian framework with frictional labor markets — a natural candidate for HARK's Markov-chain exogenous-state and search-and-matching machinery.

## If a user asks to work on this item

1. **Read first:** `docs/gkn-bellman-improved.md` — SMD-polished stage decomposition with perch table, EGM channel, and all employment transitions. This is the authoritative formalized statement.
2. **Then read:** `docs/gkn-bellman-excerpt.md` — comprehensive symbol table, Bellman equations faithful to the paper, perch decomposition, and full calibration. This is the Matsya input document.
3. **Paper source for AI ingestion:** `Gornemann_2012.pdf`. No `.mmd` (Pandoc-converted) version is available yet.

## Formalization status

- Explicit recursive formulation: present in `GKNMonetaryPolicyHA.ipynb` → "The Model" section (legacy slideware format).
- `bellman-excerpt.md`: committed (`docs/gkn-bellman-excerpt.md`) — includes comprehensive symbol table and perch decomposition.
- `bellman-excerpt-SMD-polished.md`: committed as `docs/gkn-bellman-improved.md`.
- `dolo-plus-draft.yaml`: committed (`docs/gkn-dolo.yaml`).
- `verification.md`: committed (`docs/gkn-verification.md`).
- `matsya-session.txt`: committed (`docs/matsya-session.txt`); session name: `topics2026-mon-policy`.

## Known model features requiring attention in a formalization pass

- **Pre-transition vs. post-transition aggregate state.** The paper distinguishes \(\tilde{X}\) (pre-transition, before separations/matching) from \(X\) (post-transition). The employment transition probability \(f\) is evaluated at \(\tilde{X}'\), not \(X'\). The YAML now includes `X_tilde_prime = G_tilde(X)` but dolo-plus has no canonical idiom for this distinction. See `# workaround:` comment in `gkn-dolo.yaml`.
- **Krusell-Smith aggregate law of motion.** `H(X, Z', D')` is a black-box forecasting rule — the paper does not give a closed form (Appendix B). The YAML uses `H` as a placeholder. See `# unresolved:` comment in `gkn-dolo.yaml`.
- **State-contingent employment transitions.** Employment transition probabilities depend on the aggregate state through the job-finding rate \(f(\tilde{X}')\), which itself depends on endogenous vacancies satisfying a free-entry condition. This is not a simple Markov chain — it is state-dependent.
- **Skill transition matrix retrieval.** Matsya could not retrieve the skill transition matrix from piped input; the \(4 \times 4\) matrix was filled in by hand from Table 2. Verified against the paper.
- **Grid settings are placeholders.** `n_a = 200`, `a_max = 500.0`, `n_X = 3` are reasonable defaults but not from the paper.

## Common next tasks (grounded)

1. **Produce `.mmd` from PDF.** Run `pandoc Gornemann_2012.pdf -o Gornemann_2012.mmd` to create an AI-ingestible version of the paper. Currently only the PDF is committed.
2. **Refactor legacy notebook into four-notebook exposition layer.** The current `GKNMonetaryPolicyHA.ipynb` is a monolithic slideware notebook. CONTRIBUTING.md requires `_intro.ipynb`, `_prior-literature.ipynb`, `_summary.ipynb`, `_subsequent-literature.ipynb`, plus `index.md`. See the Benhabib entry for reference structure.
3. **Add `references.bib` and `self.bib`.** No bib files exist yet. At minimum, the paper's own entry (`self.bib`) and the prior-literature references (Mortensen-Pissarides, Rotemberg, Krusell-Smith, Nakajima 2012, etc.) need bib entries.
4. **Resolve the KS forecasting-rule placeholder in the YAML.** If Appendix B provides enough detail, the `H` function could be specified as a log-linear rule with estimated coefficients.
5. **Add `index.md` with required frontmatter.** Needs `tier:`, `econ_ark_topic:`, `jel:`, `difficulty:`, `has_formalization_layer:`, etc.

## Workflow reminders

- **Matsya session:** use `--session topics2026-mon-policy` for all matsya calls on this item.
- **Paper verification:** Matsya output must be checked against the paper PDF, not only against the ballpark notebook. See `docs/gkn-verification.md` for the accept/edit/reject record.
- **When flagging workarounds in YAML:** use inline `# workaround:` or `# unresolved:` comments rather than silently fudging non-canonical syntax.
