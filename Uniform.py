import numpy as np
import matplotlib.pyplot as plt
import math

def eval(x):
    if x > 0.21111 and x < 0.3232:
        return True
    if x > 0.4957 and x < 0.9191:
        return True
    return False

N=[100,500,1000]
fig = plt.figure(figsize=(20,5))
for i in range(3):
    x = np.array([])
    d = np.random.rand(N[i])
    for j in range(N[i]):
        if eval(d[j]):
            x=np.hstack((x,d[j]))

    y = np.array([1/N[i] for k in range(len(x))])
    e = np.array([1/N[i] for k in range(len(d))])
    print(len(x)/len(d))

    ax = fig.add_subplot(1,3,i+1)
    ax.scatter(x=d,y=e,marker='o',c='r')
    ax.scatter(x=x,y=y,marker='d',c='g')
    ax.set_title('Scatter: N=%i' %N[i])
    ax.set_xlabel('$x$')
    ax.set_ylabel('$Prob.$=%f' %(1/N[i]))

plt.show()
fig.savefig('Naive.png',bbox_inches='tight')
