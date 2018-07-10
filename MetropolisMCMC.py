import numpy as np
import matplotlib.pyplot as plt
import math

def q(x_star,x):
 #normal distribution
    mu=x
    sigma=10
    return 1/(math.pi*2)**0.5/sigma*np.exp(-(x_star-mu)**2/2/sigma**2) 

def p(x): #target distribution
    return 0.3*np.exp(-0.2*x**2)+0.7*np.exp(-0.2*(x-10)**2)
    
N = [100,500,1000,5000]
fig = plt.figure()
for i in range(4):
    X = np.array([])
    x = 0.1 #initialize x0 to be 0.1
    for j in range(N[i]):
        u = np.random.rand()
        x_star = np.random.normal(x,10)
        A = min(1,p(x_star)/p(x)) #*q(x,x_star)/p(x)/q(x_star,x))
        if u < A:
            x = x_star
        X=np.hstack((X,x))
    ax = fig.add_subplot(2,2,i+1)
    ax.hist(X,bins=100,density=True)
    x = np.linspace(-10,20,5000)
    ax.plot(x,p(x)/2.7) #2.7 is just a number that approximates the normalizing constant
    ax.set_ylim(0,0.35)
    ax.text(-9,0.25,'I=%d'%N[i])
fig.suptitle('Metropolis_Hastings for MCMC')
plt.show()
