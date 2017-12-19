from numpy import *
from matplotlib.pyplot import *

N=300

mean1=[0,0]
cov1=[[1,0],[0,1]]

mean2=[4,10]
cov2=[[1,0],[0,1]]

mean3=[15,2]
cov3=[[1,0],[0,1]]

clt1=random.multivariate_normal(mean1,cov1,N)
clt2=random.multivariate_normal(mean2,cov2,N)
clt3=random.multivariate_normal(mean3,cov3,N)

unity=concatenate([clt1,clt2,clt3],axis=0)
indeces=random.permutation(unity.shape[0])
unity=unity.take(indeces,0)

savetxt('cluster_test.txt',unity)

plot(clt1[:, 0], clt1[:, 1],'.', clt2[:,0], clt2[:,1], '.', clt3[:, 0], clt3[:, 1],'.')
grid()
show()
