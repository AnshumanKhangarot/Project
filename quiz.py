import math
from decimal import *
import random
import matplotlib.pyplot as plt

n = int(raw_input("N:"));
t = int(raw_input("t:"));
disp=[]
xaxis=[]
yaxis=[]
rx = 0
ry = 0
rz = 0
freq=[0 for x in range(10000)]
maxi = 0
for i in range(n):
    rx = 0
    ry = 0
    rz = 0
    for j in range(t):
        x = random.random()
        y = random.random()
        z = random.random()
        l = random.random()
        r = math.sqrt(x*x+y*y+z*z)
        x = Decimal(Decimal(x)/Decimal(r))
        x = Decimal(x*Decimal(l))
        y = Decimal(Decimal(x)/Decimal(r))
        x = Decimal(y*Decimal(l))
        z = Decimal(Decimal(x)/Decimal(r))
        x = Decimal(z*Decimal(l))
        r = r*l
        rx += x
        ry += y
        rz += z
    dist = math.sqrt(rx*rx + ry*ry + rz*rz)
    disp.append(dist);
for i in range(len(disp)):
    if (disp[i] - int(disp[i])) > 0.5: disp[i] = int(disp[i]) + 1
    else: disp[i] = int(disp[i])
    freq[disp[i]]+= 1;
    if maxi < disp[i] : maxi = disp[i]
for i in range(0,maxi+1):
    xaxis.append(i)
    yaxis.append(freq[i])
plt.plot(xaxis,yaxis);
plt.show()


        




