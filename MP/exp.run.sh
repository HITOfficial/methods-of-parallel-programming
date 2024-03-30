#!/bin/bash
rm -f output.csv
touch output.csv

echo "experiment_type,threads,chunk_size,padding_time" > "output.csv"


for schedule_type in 0 1 2; do
    for chunk_size in 1 64 1024 2048; do
        gcc -Wall rand.c -o rand -fopenmp -DCHUNKSIZE=$chunk_size -DPADDING=0
        for threads in 1 2 4 8; do
            case $schedule_type in
                            0) schedule_name="static" ;;
                            1) schedule_name="guided" ;;
                            2) schedule_name="dynamic" ;;
                        esac
                        echo "run for" $schedule_name "schedule type, chunk size" $chunk_size "and" $threads "threads"
            OMP_NUM_THREADS=$threads OMP_DYNAMIC=false; ./rand $schedule_type $chunk_size $threads >> "output.csv";
        done
    done
done