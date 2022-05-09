import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

f_0 = 48_135

f = np.array([
    100,
    200,
    500,
    1_000,
    2_000,
    5_000,
    10_000,
    20_000,
    50_000,
    100_000,
    200_000,
    500_000,
    1_000_000,
])

phi = np.array([
    176.7,
    178.2,
    179.8,
    176.7,
    175.8,
    177.8,
    174.2,
    162.6,
    133.7,
    114.1,
    97.6,
    91.7,
    75.7,
])

u_in = np.array([
    0.959,
    0.957,
    0.953,
    0.954,
    0.950,
    0.952,
    0.966,
    0.958,
    0.985,
    0.982,
    0.989,
    0.985,
    0.981,
])

u_out = np.array([
    9.32,
    9.38,
    9.27,
    9.25,
    9.30,
    9.23,
    9.24,
    9.02,
    6.70,
    3.28,
    1.67,
    0.70,
    0.33,
])

# =----------------------------------------------------------------------------

a_x = f
a_y = 20 * np.log10(u_out / u_in)

fig = plt.figure(figsize=(6, 3.75), dpi=600)
ax = fig.gca()
ax.plot(a_x, a_y, marker="o")

plt.ylabel("$T\\;$dB")
plt.xlabel("$f\;$[Hz]")
plt.xscale("log")
plt.xlim((100, 10**6))
plt.ylim((-10, 25))
plt.yticks([-10, -5, -0, 5, 10, 15, 20, 25])
plt.grid()

fig.savefig("./include/2/chart_t.pgf")

# =----------------------------------------------------------------------------

a_x = f
a_y = phi

fig = plt.figure(figsize=(6, 3.75), dpi=600)
ax = fig.gca()
ax.plot(a_x, a_y, marker="o")

plt.ylabel("$\\phi\;$[deg]")
plt.xlabel("$f\;$[Hz]")
plt.xscale("log")
plt.xlim((100, 10**6))
plt.ylim((0, 180))
plt.yticks([0, 45, 90, 135, 180])
plt.grid()
fig.savefig("./include/2/chart_phi.pgf")
