import numpy as np
import matplotlib.pyplot as plt
import sympy
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams['text.usetex'] = True
#x=np.arange(0,100,1)

fig = plt.figure()
txf = fig.add_subplot(1, 2, 1)
txg = fig.add_subplot(1, 2, 2)
#text
tx,ty=0.5,0.5
txf.text(tx,ty,r'$ f(x)=x^{\frac{a}{100}} \times 100^{\frac{100-a}{100}} $',horizontalalignment='center',fontsize=18)
txg.text(tx,ty,r'$ g(x)=f(x)-x $',horizontalalignment='center',fontsize=18)
fig.savefig("tex.png",dpi=600)

pp = PdfPages('数式.pdf')

# figureをセーブする
pp.savefig()

# pdfファイルをクローズする。
pp.close()
plt.show()