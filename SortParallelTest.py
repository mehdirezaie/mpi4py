from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def mergeSort(x):
    if len(x) <= 1:
	return x

    m = len(x) / 2
    L = mergeSort(x[:m])
    R = mergeSort(x[m:])
	
    result = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
	if L[i] < R[j]:
	    result.append(L[i])
	    i += 1
	else:
	    result.append(R[j])
	    j += 1
    result += L[i:]
    result += R[j:]
    return result


x = [3, 12, 1, 6, 23, 13, 4, 5, 2, 17, 82, 92, 37, 36, 100, 10]

if rank == 0:
    if len(x) <= 1:
	print x

    m = len(x) / 2

    comm.send(x[:m], dest=1, tag=10)
    comm.send(x[m:], dest=2, tag=11)

    L = comm.recv(source=1, tag=10)
    R = comm.recv(source=2, tag=11)
    
    result = []

    a=0
    b=0    
    for i in range(len(x)):
        
        if(L[a]<=R[b]):
            result.append(L[a])
            a += 1
            if(a>len(L)-1):
                result.append(R[b:])
                break
        else:
            result.append(R[b])
            b += 1
            if(b>len(R)-1):
                result.append(R[a:])
                break

    print result
    
    
else:
    data = comm.recv(source = 0, tag=9+rank)
    comm.send(mergeSort(data), dest=0, tag=9+rank)

    





