import numpy as np
import scipy as sp
import scipy.optimize
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

u_in = [
    0.993,
    1.981,
    2.940,
    3.920,
    4.881,
    5.846,
    6.908,
    7.920,
    8.880,
    9.840,
]

u_out = [
    0.844,
    1.680,
    2.504,
    3.320,
    4.149,
    4.960,
    5.823,
    6.642,
    7.520,
    8.400,
]

[a], _ = sp.optimize.curve_fit(lambda x, a: a * x, u_in, u_out)
fn_fit = lambda x: a * x
print(a)

fig = plt.figure(figsize=(6, 3.75), dpi=600)
ax = fig.gca()

x = np.linspace(0, 10)
line_b, = ax.plot(x, fn_fit(x))
line_b.set_label("Dopasowana prosta, $a=" + a.astype(str) + "$")

line_a, = ax.plot(u_in, u_out, marker="o", linewidth=0)
line_a.set_label('Zmierzone wartości')

ax.legend()
plt.xlabel("$U_{we}$")
plt.ylabel("$U_{wy}$")
plt.grid()

fig.savefig("./include/4/chart.png")
fig.savefig("./include/4/chart.pgf")