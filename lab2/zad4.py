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

f_0 = 12_778

f = np.array([
    10_000,
    11_000,
    12_000,
    13_000,
    13_500,
    14_000,
    14_200,
    14_385,
    14_600,
    14_800,
    15_000,
    15_500,
    16_000,
    17_000,
    18_000,
    19_000,
    20_000,
])

phi = np.array([
    -94.0,
    -89.8,
    -85.3,
    -80.8,
    -77.7,
    -53.0,
    -30.1,
    -0.9,
    20.1,
    42.7,
    67.3,
    77.4,
    80.5,
    83.1,
    86.0,
    86.1,
    90.8,
])

u_in = np.array([
    9.79,
    9.80,
    9.79,
    9.79,
    9.70,
    9.41,
    8.81,
    8.33,
    8.52,
    8.91,
    9.44,
    9.67,
    9.67,
    9.80,
    9.80,
    9.79,
    9.79,
])

u_out = np.array([
    0.062,
    0.082,
    0.124,
    0.210,
    0.296,
    0.578,
    0.971,
    1.600,
    0.992,
    0.803,
    0.596,
    0.391,
    0.302,
    0.163,
    0.116,
    0.092,
    0.076,
])

# =----------------------------------------------------------------------------

a_x = f
a_y = 20 * np.log10(u_out / u_in)
# b_x = np.logspace(3, 6, base=10)
# b_y = 20 * np.log10(np.sqrt(((b_x / f_0)**2) / (1 + (b_x / f_0)**2)))

fig = plt.figure(figsize=(6, 3.75), dpi=600)
ax = fig.gca()

plt.axvline(x=f_0,
            label="$f_0=12.778$kHz teoretyczne",
            linestyle="dashed",
            color="orange")
plt.axvline(
    x=14_385,
    linestyle="dashed",
    label="$f_0=14.385$kHz zmierzone",
)

# ax.plot(b_x, b_y, color="orange")
ax.plot(a_x, a_y, marker="o")

secax = ax.secondary_xaxis('top',
                           functions=(lambda x: x / f_0, lambda x: x * f_0))
secax.set_xlabel('$\\frac{f}{f_0}$')

plt.ylabel("$T\\;$dB")
plt.xlabel("$f\;$[Hz]")
plt.xscale("log")
plt.xlim((10_000, 20_000))
plt.ylim((-45, -10))
# plt.yticks([-40, -30, -20, -10, -3, 0])
plt.legend()
plt.grid()

fig.savefig("./include/4/chart_t.pgf")

# =----------------------------------------------------------------------------

a_x = f
a_y = phi
# b_x = np.logspace(3, 6, base=10)
# b_y = np.arctan(f_0 / b_x) / np.pi * 180

fig = plt.figure(figsize=(6, 3.75), dpi=600)
ax = fig.gca()

plt.axvline(x=f_0,
            label="$f_0=12.778$kHz teoretyczne",
            linestyle="dashed",
            color="orange")
plt.axvline(
    x=14_385,
    linestyle="dashed",
    label="$f_0=14.385$kHz zmierzone",
)

# ax.plot(b_x, b_y, color="orange")
ax.plot(a_x, a_y, marker="o")

secax = ax.secondary_xaxis('top',
                           functions=(lambda x: x / f_0, lambda x: x * f_0))
secax.set_xlabel('$\\frac{f}{f_0}$')

plt.ylabel("$\\phi\;$[deg]")
plt.xlabel("$f\;$[Hz]")
plt.xscale("log")
plt.xlim((10_000, 20_000))
plt.ylim((-90, 90))
plt.yticks([-90, 0, 90])
plt.legend()
plt.grid()
fig.savefig("./include/4/chart_phi.pgf")
