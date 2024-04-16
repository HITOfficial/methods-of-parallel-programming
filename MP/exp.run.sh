#!/bin/bash
rm -f output.csv
touch output.csv

echo "threads,n,buckets,generating_random_numbers,bucket_distribution_private_sort,shared_bucket_sort,initial_table_merge_bucket,total_runtime," > "csv/output.csv"

gcc -Wall bucket_sort_on_steroids.c -o bucket_sort_on_steroids -fopenmp -DPADDING=0

for threads in {1..8}; do
  for buckets in {100..1000..100}; do
    for n in {1000000..10000000..1000000}; do
      for repetition in {1..3}; do
        echo "Run number $repetition for $threads threads $buckets buckets and $n numbers"
        ./bucket_sort_on_steroids $threads $buckets $n >> "output.csv";
      done
    done
  done
done