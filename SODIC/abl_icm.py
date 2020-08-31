import numpy as np
import matplotlib.pyplot as plt
from alisuretool.Tools import Tools
from matplotlib.backends.backend_pdf import PdfPages

name = "./result/Abl_ICM"
pdf = PdfPages(Tools.new_dir('{}.pdf'.format(name)))

plt.figure(figsize=(9, 4))

# 11111111111111111111111111111111111111111
ax = plt.subplot(121)
x = [1, 2, 3, 4, 5]
label = [64, 128, 256, 512, 1024]
r1 = [0.74, 0.75, 0.77, 0.78, 0.75]
r2 = [0.72, 0.74, 0.76, 0.77, 0.74]
r3 = [0.73, 0.75, 0.76, 0.775, 0.735]
r4 = [0.73, 0.751, 0.762, 0.767, 0.748]

# {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
plt.plot(x, r1, label="$r=1$", color="r", linewidth=1)
plt.plot(x, r2, "b--", label="$r=2$", color="g", linewidth=1)
plt.plot(x, r3, "b-.", label="$r=3$", color="b", linewidth=1)
plt.plot(x, r4, "b:", label="$r=4$", color="c", linewidth=2)

plt.xlabel("$d$")
plt.ylabel("$\max F_β$")
plt.xticks(x, label)  # 坐标的设置
plt.grid(linestyle='--')
plt.legend()

# 2222222222222222222222222222222222222222
ax = plt.subplot(122)
x = [1, 2, 3, 4, 5]
label = [64, 128, 256, 512, 1024]
r1 = [0.74, 0.75, 0.77, 0.78, 0.75]
r2 = [0.72, 0.74, 0.76, 0.77, 0.74]
r3 = [0.73, 0.75, 0.76, 0.775, 0.735]
r4 = [0.73, 0.751, 0.762, 0.767, 0.748]

# {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
plt.plot(x, r1, label="$r=1$", color="r", linewidth=1)
plt.plot(x, r2, "b--", label="$r=2$", color="g", linewidth=1)
plt.plot(x, r3, "b-.", label="$r=3$", color="b", linewidth=1)
plt.plot(x, r4, "b:", label="$r=4$", color="c", linewidth=2)

plt.xlabel("$d$")
plt.ylabel("MAE")
plt.xticks(x, label)  # 坐标的设置
plt.grid(linestyle='--')
plt.legend()


plt.subplots_adjust(left=0.08, right=0.98, top=0.98, bottom=0.12, wspace=0.3)

# 显示图示
plt.savefig(Tools.new_dir('{}.png'.format(name)))
pdf.savefig()
pdf.close()

plt.show()

