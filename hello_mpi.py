#!/usr/bin/env python

#	Example of MPI Hello 
#	to run: mpirun -np 2 python ./hello_mpi.py

from mpi4py import MPI


size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

if rank ==0:
   print "Hello World from rank %d from size %d running on %s..." % (rank, size, name)
else:
   print "Goodbye World from rank %d from size %d running on %s..." % (rank, size, name)

MPI.COMM_WORLD.Barrier()
