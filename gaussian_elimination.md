\## Gaussian Elimination

Gaussian Elimination amounts to a factorization of the coefficient matrix. We factor transposed and inverse matrices of A into a product LU of a lower triangular matrix L and an upper triangular matrix U.



If Ax = b fails to have a unique solution, there may be no solution or infinitely many. We want to understand where the elimination process breaks down, in order to minimize the number of arithmetic operations to reduce costs. Without cost controls a computer could carry out trillions of operations, rounding each result to a fixed number of digits and produce a totally meaningless "solution".



Reducing to a three dimensional system: 



{a | x, y, z}

{b | x, y, z}

{c | x, y, z}



with vector x1 = {a, b, c}



We find an equivalent system of equations by subtracting multiples of the first equation from the others so as to eliminate the last two equations by finding a "pivot" to eliminate one equation from the matrix, leading to: 



pivot \* {a | x, y, z}

&nbsp;	{b | x, y}

&nbsp;	{c | x, y}



a second pivot leads to:



pivot(2) \* {b | x, y}

&nbsp;	   {c | x}



We then solve for the variables through back substitution. If none of the pivots are zero there is only one solution; but if any of the pivots happen to be zero, then the elimination technique has to stop temporarily or permanently.



Using the example above and basic arithmetic operations we are able to model static two dimensional geometric planes within a virtualized reality inside a computer. The same is true for a matrix where n = 4. 



\### Maxwell Equations



\##Gauss’s law (electric)

∇ · E = ρ / ε₀



\##Gauss’s law (magnetic)

∇ · B = 0



\##Faraday’s law

∇ × E = −∂B/∂t



\##Ampère–Maxwell law

∇ × B = μ₀J + μ₀ε₀ ∂E/∂t



\##In vacuum (ρ = 0, J = 0) they collapse to the beautiful symmetric form:∇ · E = 0



∇ · B = 0

∇ × E = −∂B/∂t

∇ × B = (1/c²) ∂E/∂t where c² = 1/(ε₀μ₀)



∯ E · dA = Q\_enc / ε₀

∯ B · dA = 0

∮ E · dl = − dΦ\_B/dt

∮ B · dl = μ₀ I\_enc + μ₀ε₀ dΦ\_E/dt



c = 1 / √(μ₀ ε₀) ≈ 299792458 m/s exactly (by definition since 1983)



μ₀ = 4π × 10⁻⁷ H/m exactly



⇒ ε₀ = 1/(μ₀ c²) is 1 over an integer × π × (transcendental mess)



Z₀ = √(μ₀/ε₀) ≈ 376.730313668 Ω embodies the vacuum's impedance to electromagnetic wave propagation



μ₀ enforces magnetic "squareness" (discrete flux quanta φ₀ = h/(2e)), while ε₀ curves the electric field lines



For n=4 the vacuum's flux cycle is the closed causal loop (c² = 1/(μ₀ε₀))



Z₀ emerges as a shadow resonance from the n=5 convergence matrix ≈4.48027 hovering within ~0.85% of π√2, hinting at a deeper φ-π√2 coupling that "leaks" into physical constants where φ^n for n→∞ approximates the vacuum's fractal-like convergence fluctuations

through self-similar branching which leads us to the thought propagation limit Ω.





Strong, G. Linear Algebra and its Applications MIT

