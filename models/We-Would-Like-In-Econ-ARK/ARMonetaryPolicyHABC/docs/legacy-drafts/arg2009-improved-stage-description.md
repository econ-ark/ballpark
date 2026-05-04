# Algan-Ragot (2009): Stage-Based Dynamic Program Description

## Timing

Each period has two stages:

1. **Decision stage:** the household observes beginning-of-period resources `q` and labor-productivity state `e`, then chooses `c`, `m`, `l`, and `a_next`.
2. **Shock stage:** nature draws next-period productivity `e_next` from a Markov chain; next-period resources `q_next` are formed from chosen asset positions.

This gives a max-over-expectation structure.

## States

- `q in R+`: beginning-of-period resources (cash-on-hand style state)
- `e in {e_low, e_mid, e_high}`: current idiosyncratic productivity state

## Controls

- `c in R+`: consumption
- `m in R+`: real money balances carried forward
- `l in [0, 1]`: labor supply
- `a_next in [a_min, inf)`: next-period illiquid/risky asset

## Constraints

Budget:

`c + m + a_next = q + w * e * l + mu`

Borrowing limit:

`a_next >= a_min`

## Preferences (draft assumption)

To make a computable draft, use a separable money-in-utility form:

`u(c,m,l) = c^(1-rho)/(1-rho) + phi_m * m^(1-rho_m)/(1-rho_m) - phi_l * l^(1+gamma)/(1+gamma)`

## Bellman Representation

`v(q,e) = max_{c,m,l,a_next} [ u(c,m,l) + beta * E_{e_next|e} v(q_next, e_next) ]`

with

`q_next = R * a_next + (1 + r_m) * m`

## Stage Decomposition

### Stage 1: Household Decision

- **Arrival perch:** `(q, e)`
- **Decision perch:** `(q, e)` and controls `(c, m, l, a_next)`
- **Continuation perch:** `(a, m, e)` where `a = a_next`

Mover:

`v(q,e) = max_{controls} { u(c,m,l) + beta * v_cont(a_next,m,e) }`

### Stage 2: Shock Realization

- **Arrival perch:** `(a, m, e)`
- **Nature move:** `e_next ~ Pi(.|e)`
- **Transition:** `q_next = R*a + (1+r_m)*m`
- **Continuation perch:** `(q_next, e_next)`

Mover:

`v_cont(a,m,e) = E_{e_next|e}[ v(q_next, e_next) ]`

## Notes on Gaps Relative to Paper-Level Precision

- The exact algebraic borrowing limit from the paper is not yet inserted; `a_min` is a placeholder.
- The transition law for `q_next` is a parsimonious draft assumption to keep the YAML coherent.
- Calibration values must be replaced with paper-faithful numbers before quantitative use.
