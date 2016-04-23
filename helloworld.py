#!/usr/bin/env python

#	Example of MPI Hello
#	last edit: April 23
#	to run: mpirun -np 2 python ./hello_mpi.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

if rank ==0:
   print "Hello World from rank %d from size %d running on %s ..." % (rank, size, name)
else:
   print "Goodbye World from rank %d from size %d running on %s ..." % (rank, size, name)

comm.Barrier()
