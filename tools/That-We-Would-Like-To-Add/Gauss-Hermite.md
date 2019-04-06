# Gauss-Hermite Quadrature

The default method for discretizing the lognormal distributon in HARK is to construct and equiprobable set of bins. This has two advantages over other methods:

1. It is very easy to understand so is useful for teaching
1. Simulation of a population of agents whose shocks are equiprobable is easy
   * Because the population mass of each simulated agent does not change 
   
However, for numerical efficiency, other methods of discretization are better.

The most common such method is Gauss-Hermite Quadrature. 

An extension to the existing `approxMeanOneLognormal` that allowed the user to specify the method of approximation (Equiprobable, GaussHermite, or something else) would be most welcome.
