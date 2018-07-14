import numpy as np
import matplotlib.pyplot as plt
import math

def normal(mu,sigma,x): #normal distribution
    return 1/(math.pi*2)**0.5/sigma*np.exp(-(x-mu)**2/2/sigma**2)

def eval(x):
    return normal(-4,1,x) + normal(4,1,x)
    #return 0.3*np.exp(-0.2*x**2)+0.7*np.exp(-0.2*(x-10)**2)

def ref(x_star,x):  #normal distribution
    return normal(x,10,x_star)

N = [100,500,1000,5000]
fig = plt.figure()
for i in range(4):
    X = np.array([])
    x = 0.1 #initialize x0 to be 0.1
    for j in range(N[i]):
        u = np.random.rand()
        x_star = np.random.normal(x,10)
        A = min(1,eval(x_star)/eval(x)) #*q(x,x_star)/p(x)/q(x_star,x))
        if u < A:
            x = x_star
        X=np.hstack((X,x))

    ax = fig.add_subplot(2,2,i+1)
    ax.hist(X,bins=100,density=True)
    x = np.linspace(-10,20,5000)
    #ax.plot(x,eval(x)/2.7) #2.7 approximates the normalizing constant
    ax.plot(x,eval(x)/2) #2 approximates the normalizing constant
    ax.set_ylim(0,0.35)
    ax.text(-9,0.25,'I=%d'%N[i])

fig.suptitle('Metropolis_Hastings for MCMC(Normal)')
#fig.suptitle('Metropolis_Hastings for MCMC(Exp.)')
plt.savefig('MetropolisNormal.png',dpi=100)
#plt.savefig('MetropolisExp.png',dpi=100)
plt.show()
