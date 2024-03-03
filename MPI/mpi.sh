rm standard_case1.csv
rm standard_case2.csv
rm synchronous_case1.csv
rm synchronous_case2.csv

# standard
touch standard_case1.csv
touch standard_case2.csv

## synchronous
touch synchronous_case1.csv
touch synchronous_case2.csv

for i in 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576
do
    mpiexec -machinefile ./case1 -np 2 ./mpi.py $i standard >> standard_case1.csv
    mpiexec -machinefile ./case2 -np 2 ./mpi.py $i standard >> standard_case2.csv
    mpiexec -machinefile ./case1 -np 2 ./mpi.py $i sync >> synchronous_case1.csv
    mpiexec -machinefile ./case2 -np 2 ./mpi.py $i sync >> synchronous_case2.csv
done