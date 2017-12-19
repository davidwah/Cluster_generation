from numpy import *
from matplotlib.pyplot import *

N=500

mean1=[0,0]
cov1=[[1,0],[0,1]]

c1=random.multivariate_normal(mean1,cov1,N)

p1=random.uniform(10,12,N)
fi1=random.uniform(0,2*pi,N)
c2=empty_like(c1)
c2[:,0]=p1*cos(fi1)
c2[:,1]=p1*sin(fi1)

p2=random.uniform(14,15,N)
fi2=random.uniform(0,2*pi,N)
c3=empty_like(c1)
c3[:,0]=p2*cos(fi2)
c3[:,1]=p2*sin(fi2)

unity=concatenate([c1,c2,c3],axis=0)
indeces=random.permutation(unity.shape[0])
unity=unity.take(indeces,0)

savetxt('cluster_circle.txt',unity)

plot(c1[:,0], c1[:,1], '.', c2[:,0], c2[:,1], '.', c3[:,0], c3[:,1], '.')
grid()
show()
