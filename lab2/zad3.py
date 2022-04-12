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
    # 100,
    # 200,
    # 500,
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
    # -0.8,
    # -0.7,
    # -1.0,
    -0.9,
    -2.9,
    -5.4,
    -8.2,
    -14.7,
    -42.8,
    -58.0,
    -72.4,
    -81.7,
    -89.3,
])

u_in = np.array([
    # 9.83,
    # 9.84,
    # 9.81,
    9.80,
    9.80,
    9.80,
    9.80,
    9.80,
    9.68,
    9.52,
    9.41,
    9.44,
    9.33,
])

u_out = np.array([
    # 9.80,
    # 9.80,
    # 9.80,
    9.80,
    9.80,
    9.79,
    9.64,
    9.20,
    7.63,
    5.02,
    2.85,
    1.21,
    0.59,
])

# =----------------------------------------------------------------------------

a_x = f
a_y = 20 * np.log10(u_out / u_in)
b_x = np.logspace(3, 6, base=10)
b_y = 20 * np.log10(np.sqrt(1 / (1 + (b_x / f_0)**2)))

fig = plt.figure(figsize=(6, 3.75), dpi=600)
ax = fig.gca()

plt.axhline(y=-3, linestyle="dashed", color="gray")
plt.axvline(x=f_0,
            label="$f_0=48.135$kHz teoretyczne",
            linestyle="dashed",
            color="orange")
plt.axvline(
    x=59_440,
    linestyle="dashed",
    label="$f_0=59.440$kHz zmierzone",
)

ax.plot(b_x, b_y, color="orange")
ax.plot(a_x, a_y, marker="o")

secax = ax.secondary_xaxis('top',
                           functions=(lambda x: x / f_0, lambda x: x * f_0))
secax.set_xlabel('$\\frac{f}{f_0}$')

plt.ylabel("$T\\;$dB")
plt.xlabel("$f\;$[Hz]")
plt.xscale("log")
plt.xlim((10**3, 10**6))
plt.ylim((-30, 1))
plt.yticks([-30, -20, -10, -3, 0])
plt.legend()
plt.grid()

fig.savefig("./include/3/chart_t.pgf")

# =----------------------------------------------------------------------------

a_x = f
a_y = phi
b_x = np.logspace(3, 6, base=10)
b_y = -np.arctan(b_x / f_0) / np.pi * 180

fig = plt.figure(figsize=(6, 3.75), dpi=600)
ax = fig.gca()

plt.axhline(y=-45, linestyle="dashed", color="gray")
plt.axvline(x=f_0,
            label="$f_0=48.135$kHz teoretyczne",
            linestyle="dashed",
            color="orange")
plt.axvline(
    x=54_710,
    linestyle="dashed",
    label="$f_0=54.710$kHz zmierzone",
)

ax.plot(b_x, b_y, color="orange")
ax.plot(a_x, a_y, marker="o")

secax = ax.secondary_xaxis('top',
                           functions=(lambda x: x / f_0, lambda x: x * f_0))
secax.set_xlabel('$\\frac{f}{f_0}$')

plt.ylabel("$\\phi\;$[deg]")
plt.xlabel("$f\;$[Hz]")
plt.xscale("log")
plt.xlim((10**3, 10**6))
plt.ylim((-90, 0))
plt.yticks([-90, -45, 0])
plt.legend()
plt.grid()
fig.savefig("./include/3/chart_phi.pgf")
