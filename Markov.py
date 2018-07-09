# https://zhuanlan.zhihu.com/p/25610149

import numpy as np
import matplotlib.pyplot as plt
import math

def p(x):
 #standard normal
    mu=0
    sigma=1
    return 1/(math.pi*2)**0.5/sigma*np.exp(-(x-mu)**2/2/sigma**2)

#uniform proposal distribution on [-4,4]
def q(x): #uniform
    return np.array([0.125 for i in range(len(x))])

x = np.linspace(-4,4,500)
M = 3.5

N=1000 #number of samples needed
i = 1
count = 0
X = np.array([])
while i < N:
    u = np.random.rand(10) #evaluate 10 each loop
    x = (np.random.rand(10)-0.5)*8
    res = u < p(x)/q(x)/M
    if any(res):
        X = np.hstack((X,x[res]))
        i+=len(x[res])
    count+=10
count -= len(X) - 1000
X=X[:1000]

x = np.linspace(-4,4,500)
plt.plot(x,p(x))
plt.hist(X,bins=100,density=True)
plt.title('Rejection Sampling')
plt.show()

plt.savefig('result.png', dpi=100)
print (N/count) #proportion of raw sample used
