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
    if (argc != 4) {
        printf("Usage: %s <number of threads> <schedule type> <chunk size>\n", argv[0]);
        return 1;
    }

    int n = 17; // array size
    int max = 10;
    int schedule_type = atoi(argv[1]);
    int chunk_size = atoi(argv[2]);
    int nthreads = atoi(argv[3]);

    omp_set_num_threads(nthreads);

    int *tab = calloc(n, sizeof(int)); // Allocate memory for the array
//    fill tab with random numbers,not 0

    srand(10);

    // Fill the array with random numbers between 1 and 9
    for (int i = 0; i < n; i++) {
        tab[i] = (rand() % max) + 1; // random number between 1 and 9
    }


    double start = omp_get_wtime();


    double end = omp_get_wtime();
    double first_part = end - start;
    for (int i = 0; i < n; i++) {
        printf("%d\t", tab[i]);
    }
    printf("first part ended \n");

    // Find min and max values in the array
    int max_value_in_tab = 0;
    int min_value_in_tab = 0;
    for (int i = 0; i < n; i++) {
        if (tab[i] > max_value_in_tab) max_value_in_tab = tab[i];
        if (tab[i] < min_value_in_tab) min_value_in_tab = tab[i];
    }
    printf("min: %d, max: %d\n", min_value_in_tab, max_value_in_tab);

    // Allocate memory for shared buckets and their lengths
    int *shared_bucket_length = calloc(nthreads, sizeof(int));
    int **shared_buckets = calloc(nthreads, sizeof(int *));
    for (int i = 0; i < nthreads; i++) {
        shared_buckets[i] = calloc(n, sizeof(int));
    }

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

        for (int i = 0; i < nthreads; i++) {
            qsort(buckets[i], bucket_length[i], sizeof(int), cmpfunc);
            // check if the buckets are sorted
            if (bucket_length[i] == 0) {
                continue;
            }
            printf("qsort 1\n");
            for (int j = 0; j < bucket_length[i]; j++) {
                printf(" %d\t", buckets[i][j]);
                printf("\n");
            }
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




// Sort shared buckets
#pragma omp parallel
    {
        int i = omp_get_thread_num();
        qsort(shared_buckets[i], shared_bucket_length[i], sizeof(int), cmpfunc);
        if (shared_bucket_length[i] > 0) {
            printf("qsort 2\n");
            for (int j = 0; j < shared_bucket_length[i]; j++) {
                printf(" %d\t", shared_buckets[i][j]);
                printf("\n");
            }
        }
    }

//
//
//#pragma omp barrier
//// Merge sorted buckets back into the original array
#pragma omp parallel
    {
        int i = omp_get_thread_num();
        int previous_buckets_length = 0;
        for (int j = 0; j < i; j++) {
            previous_buckets_length += shared_bucket_length[j];
        }
        for(int j = 0; j < shared_bucket_length[i]; j++) {
            int index = j + previous_buckets_length;
            tab[index] = shared_buckets[i][j];
        }
    }

//
//printf("ONOMATOPEJA\n");
//
printf("\n");
for (int i = 0; i < n; i++) {
    printf("%d\t", tab[i]);
}
//printf("first part:  %f\n", first_part);
//printf("schedule type: %d\n", schedule_type);
//
//#pragma omp barrier
//
//// Cleanup
    for (int i = 0; i < nthreads; i++) {
        free(shared_buckets[i]);
    }
    free(shared_buckets);
    free(shared_bucket_length);
    free(tab);

    return 0;
}