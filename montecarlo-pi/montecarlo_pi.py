# if main
import sys
from random import random

from mpi4py import MPI


def calc_pi(iterations):
    k = 0
    for _ in range(iterations):
        x, y = random(), random()
        k += int(x ** 2 + y ** 2 < 1)
    return k


def main(total_points):
    comm = MPI.COMM_WORLD
    comm.Barrier()
    rank = comm.Get_rank()
    size = comm.Get_size()
    iterations_per_process = total_points // size
    start_time = MPI.Wtime()
    k = calc_pi(iterations_per_process)
    result = comm.reduce(k, op=MPI.SUM, root=0)
    if rank == 0:
        stop_time = MPI.Wtime()
        output = "{size};{time};{pi}".format(size=size, time=stop_time - start_time, pi=4 * result / total_points)
        print(output)


if __name__ == "__main__":
    main(int(sys.argv[1]))
