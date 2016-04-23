#!/usr/bin/env python

#
#   example of brodcasting
#   last edit: April 23, 2016

#   to run on 3 nodes:
#   mpirun -np 3 python bcast.py

from numpy import array
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
data = {'key1' : [10,10.1,10+11j],
           'key2' : ( 'mpi4py', 'python'),
           'key3':array([1,2,3])}
else:
   data = None

data = comm.bcast(data, root=0)

if rank == 0:
    print "bcast finished"

print "data on rank %d is: "%comm.rank, data
