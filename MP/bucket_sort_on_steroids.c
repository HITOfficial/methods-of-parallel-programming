#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <time.h>

#define BUCKET_INDEX(number, min_value, max_value, number_of_buckets) \
    ((number - min_value) * (number_of_buckets - 1) / (max_value - min_value))

int cmpfunc(const void *a, const void *b) {
    return (*(int *) a - *(int *) b);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <number of threads> <n> \n", argv[0]);
        return 1;
    }
    double initial_time = omp_get_wtime();

    int max = 10000000;

    int nthreads = atoi(argv[1]);
    int n = atoi(argv[2]);

    omp_set_num_threads(nthreads);

    int *tab = calloc(n, sizeof(int)); // Allocate memory for the array

    double start = omp_get_wtime();
    // Generate random numbers in parallel
#pragma omp parallel
    {
        unsigned int seed = time(0) + omp_get_thread_num();
#pragma omp for
        for (int i = 0; i < n; i++) {
            tab[i] = rand_r(&seed) % max;
        }
    }

    double end = omp_get_wtime();

    double generating_random_numbers = end - start;

    // Find min and max values in the array
    int max_value_in_tab = 0;
    int min_value_in_tab = 0;
    for (int i = 0; i < n; i++) {
        if (tab[i] > max_value_in_tab) max_value_in_tab = tab[i];
        if (tab[i] < min_value_in_tab) min_value_in_tab = tab[i];
    }

    // Allocate memory for shared buckets and their lengths
    int *shared_bucket_length = calloc(nthreads, sizeof(int));
    int **shared_buckets = calloc(nthreads, sizeof(int *));
    for (int i = 0; i < nthreads; i++) {
        shared_buckets[i] = calloc(n, sizeof(int));
    }

    start = omp_get_wtime();
// Distribute elements into buckets
#pragma omp parallel
    {
        int thread_id = omp_get_thread_num();
        int *bucket_length = calloc(nthreads, sizeof(int));
        int **buckets = calloc(nthreads, sizeof(int *));
        for (int i = 0; i < nthreads; i++) {
            buckets[i] = calloc(n, sizeof(int));
        }

        int start_index = n / nthreads * thread_id;
        int end_index = (thread_id == nthreads - 1) ? n : n / nthreads * (thread_id + 1);

        for (int index = start_index; index < end_index; index++) {
            int bucket_index = BUCKET_INDEX(tab[index], min_value_in_tab, max_value_in_tab, nthreads);
            buckets[bucket_index][bucket_length[bucket_index]] = tab[index];
            bucket_length[bucket_index]++;
        }

        // Sort each private bucket
        for (int i = 0; i < nthreads; i++) {
            qsort(buckets[i], bucket_length[i], sizeof(int), cmpfunc);
        }

        // Merge buckets into shared_buckets
        for (int i = 0; i < nthreads; i++) {
            for (int j = 0; j < bucket_length[i]; j++) {
                int bucket_index = BUCKET_INDEX(buckets[i][j], min_value_in_tab, max_value_in_tab, nthreads);
#pragma omp critical
                {
                    shared_bucket_length[bucket_index]++;
                    shared_buckets[bucket_index][shared_bucket_length[bucket_index] - 1] = buckets[i][j];
                }
            }
        }

        // Cleanup
        for (int i = 0; i < nthreads; i++) {
            free(buckets[i]);
        }
        free(buckets);
        free(bucket_length);
    }
    end = omp_get_wtime();
    double bucket_distribution_private_sort = end - start;


    start = omp_get_wtime();
// Sort shared buckets
#pragma omp parallel
    {
        int i = omp_get_thread_num();
        qsort(shared_buckets[i], shared_bucket_length[i], sizeof(int), cmpfunc);
    }

    end = omp_get_wtime();
    double shared_bucket_sort = end - start;


    start = omp_get_wtime();
//  Merge sorted buckets back into the original array
#pragma omp parallel
    {
        int i = omp_get_thread_num();
        int previous_buckets_length = 0;
        for (int j = 0; j < i; j++) {
            previous_buckets_length += shared_bucket_length[j];
        }
        for (int j = 0; j < shared_bucket_length[i]; j++) {
            int index = j + previous_buckets_length;
            tab[index] = shared_buckets[i][j];
        }
    }
    end = omp_get_wtime();
    double initial_table_merge_bucket = end - start;

    double total_runtime = end - initial_time;
    printf("%d %d %f %f %f %f %f\n", nthreads, n, generating_random_numbers, bucket_distribution_private_sort,
           shared_bucket_sort, initial_table_merge_bucket, total_runtime);

    for (int i = 0; i < nthreads; i++) {
        free(shared_buckets[i]);
    }
    free(shared_buckets);
    free(shared_bucket_length);
    free(tab);

    return 0;
}