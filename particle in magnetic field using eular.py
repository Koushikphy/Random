from math import exp
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as ani


h=.1

t,x,x1,y,y1,z,z1=[0],[100],[.5],[100],[.5],[100],[.01]



while x[-1]<150:
    a = t[-1]+h
    b = y[-1] + y1[-1]*h
    c = y1[-1] + z1[-1]*h
    d = z[-1] +z1[-1]*h
    e = z1[-1] - y1[-1]*h
    f = x[-1]+ +x1[-1]*h
    g = x1[-1]
    x.append(f)
    x1.append(g)
    y.append(b)
    y1.append(c)
    z.append(d)
    z1.append(e)
    t.append(a)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z)
plt.show()