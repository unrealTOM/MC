import numpy as np
import matplotlib.pyplot as plt

def p(x):
 #standard normal
    mu=0
    sigma=1
    return 1/(math.pi*2)**0.5/sigma*np.exp(-(x-mu)**2/2/sigma**2)

#uniform proposal distribution on [-4,4]
def q(x): #uniform
    return np.array([0.125 for i in range(len(x))])

#draw N samples that conform to q(x), and then draw M from then that approximately conform to p(x)
N=100000
M=1000
x = (np.random.rand(N)-0.5)*8
w_x = p(x)/q(x)
w_x = w_x/sum(w_x)
w_xc = np.cumsum(w_x) #used for uniform quantile inverse
# resample from x with replacement with probability of w_x
X=np.array([])
for i in range(M):
    u = np.random.rand()
    X = np.hstack((X,x[w_xc>u][0]))

x = np.linspace(-4,4,500)
plt.plot(x,p(x))
plt.hist(X,bins=100,normed=True)
plt.title('Sampling Importance Resampling')
