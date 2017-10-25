import random,math
from decimal import *
import matplotlib.pyplot as plt

d = input("D:")
d = int(d)
t = input("time:")
t= int(t)
x=-100
for f in xrange(t):
        while x<100:
                k=-1*(float(x*x)/float(4*d*t))
                n=float(math.exp(k))
                l=float(math.sqrt(4*math.pi*d*t))
                yaxis=n/l
                plt.plot(x,yaxis,'bo')
                x=x+0.1;

plt.show()
