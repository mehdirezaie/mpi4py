#!/usr/bin/env python

#	example of point to point
#
import sys
import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 0:
   data = numpy.arange(10000)
   comm.send(data, dest=1, tag=13)
   print "Message sent, data is: ", data
elif rank == 1:
   data = comm.recv(source=0, tag=13)
   print "Message Received, data is: ", data
