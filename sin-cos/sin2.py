import numpy as np
import matplotlib.pyplot as plt
sep=0.1
x=np.arange(0,2*np.pi+sep,sep)
y1=np.sin(x)
y2=y1**2
plt.rcParams['text.usetex'] = True
plt.plot(x,y1,label=r"$\sin x$")
plt.plot(x,y2,label=r"$\sin^2 x$")
""" plt.set_xlabel("x")
plt.set_ylabel("y")
 """
plt.grid()
plt.legend()
plt.show()