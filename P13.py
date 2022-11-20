import matplotlib.pyplot as plt
import numpy as np
import math
'''time=np.arange(0,10,0.1)
amp=np.cos(time)
plt.plot(time,amp)
plt.grid(True, which='both')
plt.axhline(y=0)
plt.show()
x=np.array([11,23,31,43,51])
y=np.array([2,4,6,8,10])
y_log=np.log(y)
curve=np.polyfit(x,y_log,1)
y1=np.exp(0.69)*np.exp(0.085*x)
plt.plot(x,y)
plt.plot(x,y1)
plt.show()'''
plt.subplot(2,1,1)
deg=range(0,360+1)
sine=[math.sin(math.radians(i))for i in deg]
plt.plot(sine)
plt.grid()
plt.axhline(y=0, color='k')
plt.show()
plt.subplot(2,1,2)
deg=range(0,360+1)
cos=[math.cos(math.radians(i))for i in deg]
plt.plot(cos)
plt.grid()
plt.axhline(y=0, color='k')
plt.show()
x=np.array([11,23,31,43,51])
y=np.array([2,4,6,8,10])
y_log=np.log(y)
curve=np.polyfit(x,y_log,1)
y1=np.exp(0.69)*np.exp(0.085*x)
plt.plot(x,y)
plt.plot(x,y1)
plt.show()