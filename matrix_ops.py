import sympy as sp
phi, pi = sp.symbols('phi pi')
s = sp.sqrt(2)/pi - 2/(pi**2 * phi**2)
d2 = phi**3 - 2/(pi**2 * phi**2)
d3 = phi**4 - 2/(pi**2 * phi**2) - s**2/d2
t = s * (1 - s/d2)
d4 = phi**5 - 2/(pi**2 * phi**2) - s**2/d2 - t**2/d3
A = sp.Matrix([[phi**2, sp.sqrt(2)/pi, sp.sqrt(2)/pi, sp.sqrt(2)/pi],
               [sp.sqrt(2)/pi, phi**3, sp.sqrt(2)/pi, sp.sqrt(2)/pi],
               [sp.sqrt(2)/pi, sp.sqrt(2)/pi, phi**4, sp.sqrt(2)/pi],
               [sp.sqrt(2)/pi, sp.sqrt(2)/pi, sp.sqrt(2)/pi, phi**5]])
L = sp.Matrix([[1, 0, 0, 0],
               [sp.sqrt(2)/(pi*phi**2), 1, 0, 0],
               [sp.sqrt(2)/(pi*phi**2), s/d2, 1, 0],
               [sp.sqrt(2)/(pi*phi**2), s/d2, t/d3, 1]])
D = sp.Matrix([[phi**2, 0, 0, 0],
               [0, d2, 0, 0],
               [0, 0, d3, 0],
               [0, 0, 0, d4]])
U = sp.Matrix([[1, sp.sqrt(2)/(pi*phi**2), sp.sqrt(2)/(pi*phi**2), sp.sqrt(2)/(pi*phi**2)],
               [0, 1, s/d2, s/d2],
               [0, 0, 1, t/d3],
               [0, 0, 0, 1]])
assert A == L * D * U  # Verify factorization