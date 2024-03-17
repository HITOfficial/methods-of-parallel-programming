#!/usr/bin/env python3
import sys
from random import random, seed

from mpi4py import MPI


def calc_pi(iterations):
    k = 0
    for _ in range(iterations):
        x, y = random(), random()
        k += int(x ** 2 + y ** 2 < 1)
    return k


def main(total_points):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    seed(rank)
    iterations_per_process = total_points // size
    comm.Barrier()
    start_time = MPI.Wtime()
    k = calc_pi(iterations_per_process)
    result = comm.reduce(k, op=MPI.SUM, root=0)
    if rank == 0:
        stop_time = MPI.Wtime()
        output = "{proc};{total_points};{time};{pi}".format(proc=size, total_points=total_points,
                                                            time=stop_time - start_time,
                                                            pi=4 * result / total_points)
        print(output)


if __name__ == "__main__":
    main(int(sys.argv[1]))
