import numpy as np
import matplotlib.pyplot as plt
from alisuretool.Tools import Tools
from matplotlib.backends.backend_pdf import PdfPages

name = "./result/Abl_SUM"
pdf = PdfPages(Tools.new_dir('{}.pdf'.format(name)))

plt.figure(figsize=(9, 4))

# 11111111111111111111111111111111111111111
ax = plt.subplot(121)
x = [1, 2, 3, 4, 5, 6]
label = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
r1 = [0.74, 0.75, 0.77, 0.78, 0.78, 0.75]
r2 = [0.72, 0.74, 0.76, 0.78, 0.77, 0.74]
r3 = [0.73, 0.75, 0.78, 0.76, 0.775, 0.735]
r4 = [0.73, 0.78, 0.751, 0.762, 0.767, 0.748]
r5 = [0.736, 0.784, 0.741, 0.760, 0.777, 0.758]
r6 = [0.72, 0.789, 0.741, 0.768, 0.760, 0.742]

# {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
plt.plot(x, r1, label="$β=0.0$", color="r", linewidth=1)
plt.plot(x, r2, "b--", label="$β=0.2$", color="g", linewidth=1)
plt.plot(x, r3, "b-.", label="$β=0.4$", color="b", linewidth=1)
plt.plot(x, r4, "b:", label="$β=0.6$", color="c", linewidth=2)
plt.plot(x, r5, "b-.", label="$β=0.8$", color="m", linewidth=1)
plt.plot(x, r6, "b:", label="$β=1.0$", color="y", linewidth=2)

plt.xlabel("$α$")
plt.ylabel("$\max F_β$")
plt.xticks(x, label)  # 坐标的设置
plt.grid(linestyle='--')
plt.legend()

# 2222222222222222222222222222222222222222
ax = plt.subplot(122)
x = [1, 2, 3, 4, 5, 6]
label = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
r1 = [0.084, 0.075, 0.077, 0.078, 0.078, 0.075]
r2 = [0.062, 0.074, 0.086, 0.078, 0.067, 0.074]
r3 = [0.073, 0.0875, 0.078, 0.076, 0.0875, 0.0635]
r4 = [0.073, 0.0678, 0.0851, 0.0762, 0.0667, 0.0648]
r5 = [0.0636, 0.0784, 0.0741, 0.0760, 0.0877, 0.0758]
r6 = [0.0772, 0.06789, 0.0841, 0.0768, 0.0860, 0.0642]

# {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
plt.plot(x, r1, label="$β=0.0$", color="r", linewidth=1)
plt.plot(x, r2, "b--", label="$β=0.2$", color="g", linewidth=1)
plt.plot(x, r3, "b-.", label="$β=0.4$", color="b", linewidth=1)
plt.plot(x, r4, "b:", label="$β=0.6$", color="c", linewidth=2)
plt.plot(x, r5, "b-.", label="$β=0.8$", color="m", linewidth=1)
plt.plot(x, r6, "b:", label="$β=1.0$", color="y", linewidth=2)

plt.xlabel("$α$")
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

