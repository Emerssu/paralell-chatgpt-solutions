import threading

def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        threads = []

        # Fase de classificação paralela para números pares
        for i in range(0, n - 1, 2):
            if i + 1 < n and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
            threads.append(threading.Thread(target=sort_even, args=(arr, i, i + 2, n)))

        # Fase de classificação paralela para números ímpares
        for i in range(1, n - 1, 2):
            if i + 1 < n and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
            threads.append(threading.Thread(target=sort_odd, args=(arr, i, i + 2, n))

        # Iniciar todas as threads
        for thread in threads:
            thread.start()

        # Aguardar todas as threads terminarem
        for thread in threads:
            thread.join()

def sort_even(arr, start, end, n):
    for i in range(start, end, 2):
        if i + 2 < n and arr[i] > arr[i + 2]:
            arr[i], arr[i + 2] = arr[i + 2], arr[i]

def sort_odd(arr, start, end, n):
    for i in range(start, end, 2):
        if i + 2 < n and arr[i] > arr[i + 2]:
            arr[i], arr[i + 2] = arr[i + 2], arr[i]

if __name__ == "__main__":
    arr = [3, 6, 1, 8, 4, 9, 2, 5, 7]
    print("Array não ordenado:", arr)

    odd_even_sort(arr)

    print("Array ordenado:", arr)
