# Bellman Excerpt: Algan and Ragot (2009)

This note extracts the core dynamic program from the model summary in `ToramanSY_AlganRagot2009_Summary.ipynb`.

## Household problem (as summarized)

The representative household type is infinitely lived, with idiosyncratic labor productivity shock `e_t` evolving on a three-state Markov chain.

Value function:

`v(q_t^i, e_t^i) = max_{c_t^i, m_t^i, l_t^i, a_{t+1}^i} u(c_t^i, m_t^i, l_t^i) + beta * E[v(q_{t+1}^i, e_{t+1}^i)]`

Budget constraint:

`c_t^i + m_t^i + a_{t+1}^i = q_t^i + w_t e_t^i l_t^i + mu_t^i`

where:

- `q_t^i` is beginning-of-period financial resources/cash-on-hand
- controls are consumption `c_t^i`, real money balances `m_t^i`, labor `l_t^i`, and next-period risky assets `a_{t+1}^i`
- `mu_t^i` is transfer income linked to monetary policy / inflation-tax redistribution

Utility (CES in consumption-money composite and leisure):

`u(c_i,m_i,l_i) = (1/(1-sigma)) * [ (omega*c_i^((eta-1)/eta) + (1-omega)*m_i^((eta-1)/eta))^(eta/(eta-1)) * (1-l_i)^psi ]^(1-sigma)`

## Economic environment details relevant for stage structure

- Idiosyncratic shock process: `e_t in {e_h, e_m, e_l}` (Markov)
- Incomplete markets and borrowing constraints (binding vs non-binding cases)
- Two savings technologies in the summary text: money and risky capital asset
- Transfers `mu_t^i` are tied to inflation tax and government redistribution rules

## Aggregate side (for consistency checks)

- Production: `Y_t = K_t^alpha L_t^(1-alpha)`
- Resource constraint: `C_t + K_{t+1} + G_t = Y_t + (1-delta)K_t`
- Asset-market clearing: `K_{t+1} = A_{t+1}`
- Money evolution and inflation tax are policy objects in the summary:
  - `Omega_t = Omega_{t-1}/Pi_t + pi * Omega_{t-1}/Pi_t`
  - `tau_t^{tot} = pi * Omega_{t-1}/Pi_t`

## Known ambiguity to resolve in Dolo-style formalization

The summary states borrowing constraints are central but does not provide one explicit algebraic inequality (for example, an explicit lower bound on `a_{t+1}^i`). A Dolo-style YAML draft therefore needs either:

1. an explicit placeholder borrowing-limit rule, or
2. a clearly labeled assumption that the exact limit is to be filled from the paper text.
