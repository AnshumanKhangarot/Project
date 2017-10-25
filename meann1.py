import random

"""
Program to find the mean n1,n2-steps to left and right and compare it to the theoritical value.
Theoritical Values:
<n1> = N*p
<n2> = N*q
<m> = <n1 -n2> = <n1> - <n2> = N*(p-q)
"""
ns = input("Please enter the number of steps:")
n = int(ns)
nts = input("Please enter the number of Testcases:")
nt = int(nts)

for f in xrange(n):
    n1sum=0;n2sum=0;dsum=0
    for j in xrange(nt):
        n1t=0;n2t=0;dt=0
        for k in xrange(int(f)):
            p = random.random()
            if p>=0.5:#Right step
                dt = dt+1
                n1t = n1t+1
            else:
                dt = dt -1
                n2t= n2t+1
        n1sum= n1sum+n1t;n2sum=n2sum+n2t;dsum=dsum+dt
    n1mt = n1sum/nt;n2mt=n1sum/nt;dmt=dsum/nt
    print f , " " ,n1mt
