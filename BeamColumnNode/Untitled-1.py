import numpy as np 
import matplotlib.pyplot as plt
x=np.loadtxt('XYdisp.txt')
plt.plot(x[10:,1],x[10:,2])
plt.show()
