#!/usr/bin/env python

#	Example of MPI Hello
#	last edit: Jul 28 2017
#	to run: mpirun -np 2 python ./helloworld.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()


if rank ==0:
   print("Hello World from rank {} from size {} running on {} ...".format(rank, size, name))
else:
   print("Goodbye World from rank {} from size {} running on {} ...".format(rank, size, name))

comm.Barrier()
