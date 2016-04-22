from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
 data = numpy.arange(1000, dtype='i')
 comm.Send([data, MPI.INT], dest=1, tag=77)
 print('from rank 0: ')
 print(data)

elif rank == 1:
 data = numpy.empty(1000, dtype='i')
 comm.Recv([data, MPI.INT], source=0, tag=77)
 print('from '+str(rank))
 print(data)
