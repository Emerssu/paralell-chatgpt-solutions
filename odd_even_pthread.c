#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 4  // Ajuste o número de threads conforme necessário

int arr[] = {3, 5, 2, 4, 1};
int n = 5;

void compare_and_swap(int start, int step) {
    for (int i = start; i < n - 1; i += step) {
        if (arr[i] > arr[i + 1]) {
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }
}

void* parallel_sort(void* arg) {
    int thread_id = *((int*)arg);
    for (int phase = 0; phase < n; phase++) {
        if (phase % 2 == 0) {
            for (int i = 1; i < n; i += 2) {
                compare_and_swap(i - 1, 2);
            }
        } else {
            for (int i = 1; i < n - 1; i += 2) {
                compare_and_swap(i, 2);
            }
        }
    }
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];
    int thread_ids[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS; i++) {
        thread_ids[i] = i;
        if (pthread_create(&threads[i], NULL, parallel_sort, &thread_ids[i]) != 0) {
            perror("Error creating thread");
            exit(1);
        }
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        if (pthread_join(threads[i], NULL) != 0) {
            perror("Error joining thread");
            exit(1);
        }
    }

    printf("Lista ordenada: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
