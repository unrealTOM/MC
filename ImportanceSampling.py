import numpy as np
import matplotlib.pyplot as plt
import math

def normal(mu,sigma,x): #normal distribution
    return 1/(math.pi*2)**0.5/sigma*np.exp(-(x-mu)**2/2/sigma**2)

def eval(x):
    return normal(-4,1,x) + normal(4,1,x)

def ref(x): 
    return normal(0,2,x)  #normal
    #return np.array([0.2 for i in range(len(x))])  #uniform

N=100000
M=5000
#x = (np.random.rand(N)-0.5)*16
x = np.random.normal(0,2,N)
w_x = eval(x)/ref(x)
w_x = w_x/sum(w_x)
w_xc = np.cumsum(w_x) #accumulate

X=np.array([])
for i in range(M):
    u = np.random.rand()
    X = np.hstack((X,x[w_xc>u][0]))

x = np.linspace(-8,8,500)
plt.plot(x,eval(x)/2)
plt.plot(x,ref(x))
plt.hist(X,bins=100,density=True)
#plt.title('Importance Sampling(Uniform)')
plt.title('Importance Sampling(Normal)')
plt.xlabel('$samples$')
plt.ylabel('$sample prob.$')
#plt.savefig('ImpSampling1.png',dpi=70)
plt.savefig('ImpSampling2.png',dpi=70)
plt.show()
