import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,500)
y1 = np.sin(2*np.pi*x)
y2 = 1.1*np.sin(3*np.pi*x)

fig,ax = plt.subplots(3,1,sharex='all')

# between y2 and 0

plt.fill(x,y,color="cornflowerblue",alpha=0.4)  # 填充颜色函数

plt.plot(x,y,color="cornflowerblue",alpha=0.4)
plt.plot([x[0],x[-1]],[y[0],y[-1]],color="cornflowerblue",alpha=0.8)

plt.xlim(0,2*np.pi)
plt.ylim(-1.1,1.1)

plt.show()  # 显示