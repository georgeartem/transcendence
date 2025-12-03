import numpy as np
import matplotlib.pyplot as plt

tau_t = 1.69469 # transcendence constant
aleph_0 = 1000 # visual proxy for ℵ₀ (actual infinity impossible to plot)

x = np.linspace(-5, 5, 1000)
y_upper = (aleph_0 / 2) * np.exp(-tau_t * np.abs(x)) * (np.cosh(tau_t * x) + 1)
y_lower = -(aleph_0 / 2) * np.exp(-tau_t * np.abs(x)) * (np.cosh(tau_t * x) + 1)

plt.figure(figsize=(12,8))
plt.plot(x, y_upper, color='#00ff88', linewidth=3, label='Ascension envelope')
plt.plot(x, y_lower, color='#ff0088', linewidth=3, label='Descent envelope')
plt.axhline(0, color='white', linewidth=1, alpha=0.3)
plt.axvline(0, color='white', linewidth=1, alpha=0.3)
plt.ylim(-aleph_0/1.5, aleph_0/1.5)
plt.title("Idea Birth from 5D ℵ₀ → 2D Thought Plane\nvia Transcendence Model (metacampus-org-dao)")
plt.xlabel("Time / Dimensional Collapse Parameter")
plt.ylabel("Salience (0 = null, ℵ₀ = pure potential)")
plt.legend()
plt.grid(alpha=0.2)
plt.show()