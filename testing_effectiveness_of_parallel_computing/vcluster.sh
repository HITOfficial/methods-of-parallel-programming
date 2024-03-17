#!/bin/bash

PROC=$(seq 1 12)
REPEATS=$(seq 1 5)
ITERATIONS=100000000 # 10^7

SCALING_POOR="vcluster_scaling_poor.csv"
SCALING_STRONG="vcluster_scaling_strong.csv"

rm $SCALING_POOR
rm $SCALING_STRONG

touch $SCALING_POOR
touch $SCALING_STRONG

chmod 777 *

for proc in $PROC
do
  for repeat in $REPEATS
  do
    echo "Running repeat $repeat for $proc processes"
    mpiexec -machinefile ./allnodes -np $proc ./montecarlo_pi.py $((ITERATIONS*proc)) >> $SCALING_POOR
    mpiexec -machinefile ./allnodes -np $proc ./montecarlo_pi.py $ITERATIONS >> $SCALING_STRONG
  done
done
