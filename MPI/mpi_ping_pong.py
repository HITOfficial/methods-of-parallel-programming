from mpi4py import MPI


def standard_ping_pong(comm, rank, byte_array):
    comm.Barrier()
    start = MPI.Wtime()

    if rank == 0:
        comm.send(byte_array, dest=1)
        comm.recv(source=1)
    elif rank == 1:
        data = comm.recv(source=0)
        comm.send(data, dest=0)

    return MPI.Wtime() - start


def sync_ping_pong(comm, rank, byte_array):
    comm.Barrier()
    start = MPI.Wtime()
    dummy_buffer = bytearray(len(byte_array))
    if rank == 0:
        comm.Send(byte_array, dest=1)
        comm.Recv(dummy_buffer, source=1)
    elif rank == 1:
        comm.Recv(dummy_buffer, source=0)
        comm.Send(byte_array, dest=0)

    return MPI.Wtime() - start
