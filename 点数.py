import numpy as np
import matplotlib.pyplot as plt
f=lambda z,a:(z**(a/100))*(100**((100-a)/100))
g=lambda z,a:(z**(a/100))*(100**((100-a)/100))-z
x=np.arange(0,100,1)
fig, ax = plt.subplots()
for i,j in zip(range(11),range(0,101,10)):
    exec(f"yf{i}=f(x,{j})")
    exec(f"yg{i}=g(x,{j})")
    exec(f"l{i}={j}")
    exec(f"ax.plot(x, yf{i},label=l{i})")

ax.set_xlabel('Score')  # x軸ラベル
ax.set_ylabel('After')  # y軸ラベル
ax.grid()            # 罫線
ax.legend() 
plt.show()