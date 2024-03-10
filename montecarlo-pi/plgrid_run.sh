#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=12
#SBATCH --time=01:00:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr24-cpu

module add scipy-bundle/2021.10-foss-2021b

rm results_small.csv
rm results_medium.csv
rm results_high.csv

touch results_small.csv
touch results_medium.csv
touch results_high.csv

for proc in {1..12}
do
  for i in 1000000 2000000 3000000 4000000 5000000 6000000 7000000 8000000 9000000 10000000
  do
    i_medium=$((i*10))
    i_high=$((i*100))
    mpiexec -np $proc python montecarlo_pi.py $i >> results_small.csv
    mpiexec -np $proc python montecarlo_pi.py $i_medium >> results_medium.csv
    mpiexec -np $proc python montecarlo_pi.py $i_high >> results_high.csv
  done
done
