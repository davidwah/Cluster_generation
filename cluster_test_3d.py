from pylab import *
from numpy import *
from mpl_toolkits.mplot3d import axes3d

fig = figure()
ax = fig.gca(projection='3d')

clt1 = 1.0 * random.standard_normal((200,3))
ax.plot(clt1[:,0],clt1[:,1],clt1[:,2],'.')

clt2 = 0.7 * random.standard_normal((200,3)) + array([5,4,0])
ax.plot(clt2[:,0],clt2[:,1],clt2[:,2],'.')

clt3 = 0.4 * random.standard_normal((200,3)) + array([0,3,2])
ax.plot(clt3[:,0],clt3[:,1],clt3[:,2],'.')

unity=concatenate([clt1,clt2,clt3],axis=0)
indeces=random.permutation(unity.shape[0])
unity=unity.take(indeces,0)

savetxt('cluster_test_3d.txt', unity)

show()
