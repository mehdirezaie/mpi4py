#!/usr/bin/env python

#	example of point to point
#   last edit: April 23


import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 0:
   data = numpy.arange(10)
   comm.send(data[:5], dest=1, tag=13)
   comm.send(data[5:], dest=2, tag=14)
   print "Rank %d data is: "%rank, data
elif rank == 1:
   data = comm.recv(source=0, tag=13)
   print "Rank %d Message Received, data is: "%rank, data
elif rank == 2:
   data = comm.recv(source=0, tag=14)
   print "Rank %d Message Received, data is: "%rank, data
