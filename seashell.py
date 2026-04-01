"""
seashell.py
-----------
Logarithmic spiral shell surface. The same mathematics that governs
nautilus growth, galaxy arms, and hurricane spirals.
Tweak the parameters — small changes produce radically different shells.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Parameters -----------------------------------------------------------

N      = 5.0    # number of turns          — try 3, 7, 10
H      = 1.0    # height scaling           — try 0.5, 2.0
P      = 2.0    # power (shell flare)      — try 1, 3, 4
W      = 0.3    # width of opening         — try 0.1, 0.6
COLOR_MAP = "viridis"   # try: plasma, magma, copper, ocean

# --------------------------------------------------------------------------

u = np.linspace(0, 2 * np.pi * N, 500)
v = np.linspace(0, 2 * np.pi, 200)
U, V = np.meshgrid(u, v)

r = W * np.exp(U / (2 * np.pi))

X = r * (1 - V / (2 * np.pi)) ** P * np.cos(V) * np.cos(U)
Y = r * (1 - V / (2 * np.pi)) ** P * np.sin(V) * np.cos(U)
Z = H * r * (1 - V / (2 * np.pi)) ** P * np.sin(V) + r * np.sin(U)

fig = plt.figure(figsize=(10, 8), facecolor="black")
ax  = fig.add_subplot(111, projection="3d", facecolor="black")

surf = ax.plot_surface(X, Y, Z, cmap=COLOR_MAP,
                                              linewidth=0, antialiased=True, alpha=0.9)

ax.set_axis_off()
ax.set_title("Seashell Surface", color="white", fontsize=14, pad=20)

plt.tight_layout()
plt.savefig("seashell.png", dpi=200, bbox_inches="tight", facecolor="black")
plt.show()
print("Saved seashell.png")
