import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

f=lambda z,a:x*a/100+100-100*a/100
g=lambda z,a:f(z,a)-z
x=np.arange(0,100,1)
fig = plt.figure(figsize=(20.0, 10.0))

axf = fig.add_subplot(1, 2, 1)
axg = fig.add_subplot(1, 2, 2)

for i,j in zip(range(11),range(0,101,10)):
    exec(f"yf{i}=f(x,{j})")
    exec(f"yg{i}=g(x,{j})")
    exec(f"l{i}={j}")
    for d in "fg":
        exec(f"ax{d}.plot(x, y{d}{i},label=l{i})")

for d in "fg":
    exec(f"ax{d}.set_xlabel(r'Score')")  # x軸ラベル
    exec(f"ax{d}.set_ylabel('After')")
    exec(f"ax{d}.grid()")            # 罫線
    exec(f"ax{d}.legend()")


plt.tight_layout()
fig.savefig("お友達.png",dpi=100)

pp = PdfPages('お友達.pdf')

# figureをセーブする
pp.savefig()

# pdfファイルをクローズする。
pp.close()

plt.show()