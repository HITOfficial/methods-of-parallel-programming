#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=12
#SBATCH --time=01:00:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr24-cpu

module add scipy-bundle/2021.10-foss-2021b



ITER_BIG=20000002000 # 2 * 10^9
ITER_SMALL=1000000 # 10^5
ITER_MEDIUM=14142135 # geometric mean of small and big

ITERATIONS=$(seq 1 30)
PROC=$(seq 1 12)


ARES_RESULTS_BIG_CSV="ares_results_big.csv"
ARES_RESULTS_MEDIUM_CSV="ares_results_medium.csv"
ARES_RESULTS_SMALL_CSV="ares_results_small.csv"

rm $ARES_RESULTS_BIG_CSV
rm $ARES_RESULTS_MEDIUM_CSVsp
rm $ARES_RESULTS_SMALL_CSV

touch $ARES_RESULTS_CSV
chmod 777 *


for proc in $PROC
do
  for iteration in $ITERATIONS
  do
      echo "Running iteration $iteration for $proc processes"
      mpiexec -np $proc python montecarlo_pi.py $ITER_SMALL >> $ARES_RESULTS_SMALL_CSV
      mpiexec -np $proc python montecarlo_pi.py $ITER_MEDIUM >> $ARES_RESULTS_MEDIUM_CSV
      mpiexec -np $proc python montecarlo_pi.py $ITER_BIG >> $ARES_RESULTS_BIG_CSV
  done
done