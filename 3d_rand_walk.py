import numpy as np
# import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


n=100

x,y,z=[],[],[]
xx,yy,zz=0.0,0.0,0.0
a,b,c=n,n,n         #Boundery

while (abs(xx)<a and abs(yy)<b and abs(yy)<c):
    n=np.random.randint(6)
    if n is 0:xx+=1
    elif n is 1: xx-=1
    elif n is 2: yy+=1
    elif n is 3: yy-=1
    elif n is 4: zz+=1
    else:zz-=1 
    x.append(xx)
    y.append(yy)
    z.append(zz)

def update_lines(i):
    lines.set_data(x[:i],y[:i])
    lines.set_3d_properties(z[:i])
    ax.set_xlim3d([min(x[:i+1]),max(x[:i+1])])         
    ax.set_ylim3d([min(y[:i+1]),max(y[:i+1])])          
    ax.set_zlim3d([min(z[:i+1]),max(z[:i+1])])
    return lines




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

lines = ax.plot([],[],[])[0]                #initialize a line
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Random_Walk')

line_ani = animation.FuncAnimation(fig, update_lines, interval=100, blit=False,repeat=False)
plt.show()
