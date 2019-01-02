#Plot longitudinal modes of laser

import scipy.special as f
import numpy as np 
import matplotlib.pyplot as plt 


g=f.eval_hermite

E = lambda p,q,x,y: g(p,(2**.5)*x/w)*g(q,(2**.5)*y/w)*np.exp(-(x**2+y**2)/w**2)
w=10
x=np.linspace(-20,20,100)
y=np.linspace(-20,20,100)
x,y=np.meshgrid(x,y)

fig = plt.figure()
z=[[0,0],[1,0],[0,1],[1,1],[2,0],[0,2],[2,1],[1,2],[2,2]]
c=1
for i,j in z:
    ax=fig.add_subplot(330+c)
    c+=1
    z=E(i,j,x,y)
    z=z**2
    plt.imshow(z, vmin=z.min(), vmax=z.max(), origin='lower',
               extent=[x.min(), x.max(), y.min(), y.max()])

    # plt.scatter(x, y, c=z)
    ax.set_xticks([]) 
    ax.set_yticks([]) 
    ax.set_title("(%s,%s)"%(i,j))
    


plt.suptitle("Transverse modes of Laser")
plt.show()