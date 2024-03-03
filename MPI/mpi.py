#!/usr/bin/env python
from mpi4py import MPI
import sys
import mpi_ping_pong



if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    test_count = 100
    if len(sys.argv) != 3:
        print("Usage: mpi.py <bytes_to_send> <sync/async>")
        sys.exit(1)

    bytes_to_send = int(sys.argv[1])
    is_synchronous = sys.argv[2] == "sync"

    byte_array = bytearray(bytes_to_send)

    total_time = 0
    for i in range(test_count):
        if is_synchronous:
            time = mpi_ping_pong.sync_ping_pong(comm, rank, byte_array)
        else:
            time = mpi_ping_pong.standard_ping_pong(comm, rank, byte_array)
        total_time += time

    if rank == 0:
        result = total_time / test_count
        speed_mbs = (bytes_to_send / result) / 1_000_000  # MB/s
        latency = result * 1_000  # ms

        output = "{bytes};{speed};{latency}".format(bytes=bytes_to_send, speed=speed_mbs, latency=latency)
        print(output)
