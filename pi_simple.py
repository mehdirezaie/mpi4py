#!/usr/bin/env python

# python pi_mpi.py
# mpirun -np 5 python pi_mpi.py

import time

def f(x):
    return 4.0/(1.0+x*x)
    
def trap(local_a,local_b,local_n,h):
    estimate = (f(local_a)+f(local_b))/2.0
    for i in xrange(1,local_n):
        x = local_a+float(i)*h
        estimate += f(x)
    #
    estimate *= h
    return estimate


start = time.time()

b = 1.0
a = 0.0
n = 100000000
h = (b-a)/float(n)
total_int = trap(a,b,n,h)
end = time.time()
print "Pi with %d steps is %f in %f secs" %(n, total_int, end-start)
