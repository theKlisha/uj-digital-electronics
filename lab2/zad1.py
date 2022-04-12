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
    # 119.5,
    # 103.0,
    # 90.1,
    88.4,
    87.2,
    84.2,
    81.0,
    70.9,
    48.9,
    30.3,
    13.1,
    6.8,
    2.7,
])

u_in = np.array([
    # 9.86,
    # 9.82,
    # 9.82,
    9.81,
    9.80,
    9.80,
    9.80,
    9.80,
    9.58,
    9.48,
    9.47,
    9.51,
    9.31,
])

u_out = np.array([
    # 0.012,
    # 0.026,
    # 0.066,
    0.144,
    0.292,
    0.722,
    1.42,
    2.72,
    5.52,
    7.48,
    8.37,
    8.26,
    8.39,
])

# =----------------------------------------------------------------------------

a_x = f
a_y = 20 * np.log10(u_out / u_in)
b_x = np.logspace(3, 6, base=10)
b_y = 20 * np.log10(np.sqrt(((b_x / f_0)**2) / (1 + (b_x / f_0)**2)))

fig = plt.figure(figsize=(6, 3.75), dpi=600)
ax = fig.gca()

plt.axhline(y=-3, linestyle="dashed", color="gray")
plt.axvline(x=f_0,
            label="$f_0=48.135$kHz teoretyczne",
            linestyle="dashed",
            color="orange")
plt.axvline(
    x=76_085,
    linestyle="dashed",
    label="$f_0=76.085$kHz zmierzone",
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
plt.ylim((-40, 1))
plt.yticks([-40, -30, -20, -10, -3, 0])
plt.legend()
plt.grid()

fig.savefig("./include/1/chart_t.pgf")

# =----------------------------------------------------------------------------

a_x = f
a_y = phi
b_x = np.logspace(3, 6, base=10)
b_y = np.arctan(f_0 / b_x) / np.pi * 180

fig = plt.figure(figsize=(6, 3.75), dpi=600)
ax = fig.gca()

plt.axhline(y=45, linestyle="dashed", color="gray")
plt.axvline(x=f_0,
            label="$f_0=48.135$kHz teoretyczne",
            linestyle="dashed",
            color="orange")
plt.axvline(
    x=57_640,
    linestyle="dashed",
    label="$f_0=57.640$kHz zmierzone",
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
plt.ylim((0, 90))
plt.yticks([0, 45, 90])
plt.legend()
plt.grid()
fig.savefig("./include/1/chart_phi.pgf")
