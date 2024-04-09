#!/bin/bash
rm -f output.csv
touch output.csv

echo "threads,n,generating_random_numbers,bucket_distribution_private_sort,shared_bucket_sort,initial_table_merge_bucket,total_runtime," > "output.csv"

gcc -Wall rand.c -o rand -fopenmp -DPADDING=0

for threads in {1..8}; do
  for n in {1000000..10000000..1000000}; do
    for repetition in {1..10}; do
      echo "Run number $repetition for $threads threads and $n numbers"
      ./rand $threads $n >> "output.csv";
    done
  done
done
