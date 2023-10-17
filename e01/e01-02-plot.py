# Script para generar las líneas de campo del segundo
# problema del primer parcial

import numpy as np
import matplotlib.pyplot as plt

# Malla
X, Y = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))

# Campo Eléctrico
Ex = Y**2
Ey = 2 * X * Y

# Líneas de campo
x = np.linspace(-10, 10, 100)
fl = [np.sqrt(2 * x**2 + C) for C in np.linspace(0.0, 100.0, 16)]

for fli in fl:
    plt.plot(x, fli, color="green")
    plt.plot(x, -fli, color="green")
plt.quiver(X, Y, Ex, Ey, color="black", pivot="middle")
plt.title("Líneas de Campo")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-11, 11)
plt.ylim(-11, 11)
plt.savefig("e01-02-plot.png")
