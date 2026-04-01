"""
strange_attractor.py
--------------------
Lorenz and Rossler attractors rendered as 3D trajectories.
Tweak the parameters at the top — the geometry changes completely.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Parameters -----------------------------------------------------------

ATTRACTOR = "lorenz"   # "lorenz" or "rossler"
N_STEPS   = 100_000
DT        = 0.005
COLOR_MAP = "plasma"   # try: inferno, viridis, magma, coolwarm

# Lorenz parameters
SIGMA = 10.0
RHO   = 28.0
BETA  = 8.0 / 3.0

# Rossler parameters
A = 0.2
B = 0.2
C = 5.7

# --------------------------------------------------------------------------


def lorenz(x, y, z):
      dx = SIGMA * (y - x)
      dy = x * (RHO - z) - y
      dz = x * y - BETA * z
      return dx, dy, dz


def rossler(x, y, z):
      dx = -y - z
      dy = x + A * y
      dz = B + z * (x - C)
      return dx, dy, dz


def integrate(fn, x0=0.1, y0=0.0, z0=0.0):
      xs, ys, zs = [x0], [y0], [z0]
      x, y, z = x0, y0, z0
      for _ in range(N_STEPS):
                dx, dy, dz = fn(x, y, z)
                x += dx * DT
                y += dy * DT
                z += dz * DT
                xs.append(x)
                ys.append(y)
                zs.append(z)
            return np.array(xs), np.array(ys), np.array(zs)


fn = lorenz if ATTRACTOR == "lorenz" else rossler
xs, ys, zs = integrate(fn)

# color by trajectory progress
colors = plt.get_cmap(COLOR_MAP)(np.linspace(0, 1, N_STEPS + 1))

fig = plt.figure(figsize=(10, 8), facecolor="black")
ax  = fig.add_subplot(111, projection="3d", facecolor="black")

for i in range(0, N_STEPS, 10):
      ax.plot(xs[i:i+11], ys[i:i+11], zs[i:i+11],
                          color=colors[i], linewidth=0.4, alpha=0.8)

ax.set_axis_off()
ax.set_title(f"{ATTRACTOR.capitalize()} Attractor", color="white",
                          fontsize=14, pad=20)

plt.tight_layout()
plt.savefig(f"{ATTRACTOR}_attractor.png", dpi=200,
                        bbox_inches="tight", facecolor="black")
plt.show()
print(f"Saved {ATTRACTOR}_attractor.png")
