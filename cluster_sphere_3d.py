from pylab import *
from numpy import *
from mpl_toolkits.mplot3d import axes3d

fig = figure()
ax = fig.gca(projection='3d')

n=500

clt1=clt1 = 1.0 * random.standard_normal((n,3))  ##cluster
ax.plot(clt1[:,0],clt1[:,1],clt1[:,2],'.')

u=random.uniform(0,2*pi,n) ##cluster sphere
v=random.uniform(0,pi,n)
r=10

clt2=empty_like(clt1)
clt2[:,0]=0+r*cos(u)*sin(v)
clt2[:,1]=0+r*sin(u)*sin(v)
clt2[:,2]=0+r*ones(size(u))*cos(v)
ax.plot(clt2[:,0],clt2[:,1],clt2[:,2],'.')

u2=random.uniform(0,2*pi,n) ##cluster sphere 2
v2=random.uniform(0,pi,n)
r2=25

clt3=empty_like(clt1)
clt3[:,0]=0+r2*cos(u2)*sin(v2)
clt3[:,1]=0+r2*sin(u2)*sin(v2)
clt3[:,2]=0+r2*ones(size(u2))*cos(v2)
ax.plot(clt3[:,0],clt3[:,1],clt3[:,2],'.')

unity=concatenate([clt1,clt2,clt3],axis=0)
indeces=random.permutation(unity.shape[0])
unity=unity.take(indeces,0)

savetxt('cluster_sphere_3d.txt',unity)

show()
