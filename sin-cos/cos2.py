import numpy as np
import matplotlib.pyplot as plt
sep = 1/16
x = np.arange(0, 2 * np.pi + sep, sep)
y1 = np.cos(x)
y2 = y1**2
#plt.rcParams['text.usetex'] = True
plt.plot(x, y1, label=r"$\cos x$")
plt.plot(x, y2, label=r"$\cos^2 x$")
""" plt.set_xlabel("x")
plt.set_ylabel("y")
 """
plt.grid()
plt.legend()
plt.show()
