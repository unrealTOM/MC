import numpy as np
import matplotlib.pyplot as plt
import math

def normal(mu,sigma,x): #normal distribution
    return 1/(math.pi*2)**0.5/sigma*np.exp(-(x-mu)**2/2/sigma**2)

def eval(x):
    return normal(0,1,x)

def ref(x): #uniform
    return np.array([1/8 * 4 for i in range(len(x))])

N=1000 #number of samples needed
i = 1
X = np.array([])
while i < N:
    u = np.random.rand(10) #evaluate 10 each loop
    x = (np.random.rand(10)-0.5)*8
    res = u < eval(x)/ref(x)
    if any(res):
        X = np.hstack((X,x[res]))
        i+=len(x[res])
X=X[:1000]

x = np.linspace(-4,4,500)
plt.plot(x,eval(x))
plt.plot(x,ref(x))
plt.hist(X,bins=100,density=True)
plt.title('Rejection Sampling')
plt.xlabel('$samples$')
plt.ylabel('$sample prob.$')
plt.savefig('RejSampling.png',dpi=70)
plt.show()
