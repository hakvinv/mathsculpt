"""
torus_knot.py
-------------
A (p, q) torus knot is a curve that wraps p times around a torus
longitudinally and q times meridionally before closing.
Change p and q to get completely different knot geometries.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Parameters -----------------------------------------------------------

P         = 3       # longitudinal wraps  — try 2, 3, 5, 7
Q         = 7       # meridional wraps    — try 3, 4, 5, 8
R         = 2.0     # torus major radius
r         = 0.5     # torus minor radius
N_POINTS  = 4000
COLOR_MAP = "coolwarm"   # try: plasma, inferno, twilight, hsv

# --------------------------------------------------------------------------

t = np.linspace(0, 2 * np.pi, N_POINTS)

phi = t * P
theta = t * Q

x = (R + r * np.cos(theta)) * np.cos(phi)
y = (R + r * np.cos(theta)) * np.sin(phi)
z = r * np.sin(theta)

colors = plt.get_cmap(COLOR_MAP)(np.linspace(0, 1, N_POINTS))

fig = plt.figure(figsize=(10, 8), facecolor="black")
ax  = fig.add_subplot(111, projection="3d", facecolor="black")

for i in range(N_POINTS - 1):
      ax.plot(x[i:i+2], y[i:i+2], z[i:i+2],
                          color=colors[i], linewidth=1.2)

ax.set_axis_off()
ax.set_title(f"Torus Knot ({P}, {Q})", color="white", fontsize=14, pad=20)

plt.tight_layout()
plt.savefig(f"torus_knot_{P}_{Q}.png", dpi=200,
                        bbox_inches="tight", facecolor="black")
plt.show()
print(f"Saved torus_knot_{P}_{Q}.png")
