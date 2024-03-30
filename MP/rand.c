#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: %s <number of threads> <schedule type> <chunk size>\n", argv[0]);
        return 1;
    }
    int n = 1000000000;
    int max = 1000000001;

    int schedule_type = atoi(argv[1]);
    int chunk_size = atoi(argv[2]);
    int nthreads = atoi(argv[3]);

    omp_set_num_threads(nthreads);

    int *tab = calloc(n, sizeof(int)); // Corrected allocation size

    double start = omp_get_wtime();

#pragma omp parallel default(none) shared(tab, n, chunk_size, schedule_type, max)
    {
        switch (schedule_type) {
            case 1:
#pragma omp for schedule(guided, chunk_size)
                for (int i = 0; i < n; i++) {
                    unsigned int seed = time(NULL) + omp_get_thread_num();
                    tab[i] = rand_r(&seed) % max;
                }
                break;
            case 2:
#pragma omp for schedule(dynamic, chunk_size)
                for (int i = 0; i < n; i++) {
                    unsigned int seed = time(NULL) + omp_get_thread_num();
                    tab[i] = rand_r(&seed) % max;
                }
                break;
            default:
#pragma omp for schedule(static, chunk_size)
                for (int i = 0; i < n; i++) {
                    unsigned int seed = time(NULL) + omp_get_thread_num();
                    tab[i] = rand_r(&seed) % max;
                }
                break;
        }
    }


    double end = omp_get_wtime();

    printf("%d,%d,%d,%f\n", schedule_type, nthreads, chunk_size, end - start);

    free(tab);
    return 0;
}
