import concurrent.futures

def parallel_sort(arr):
    # Divide o array em elementos pares e ímpares
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 != 0]

    # Função para classificar uma lista
    def sort_list(lst):
        return sorted(lst)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Classifique a lista de elementos pares em uma thread
        even_sorted = executor.submit(sort_list, even)

        # Classifique a lista de elementos ímpares em outra thread
        odd_sorted = executor.submit(sort_list, odd)

        # Espere a conclusão das duas tarefas
        even_sorted = even_sorted.result()
        odd_sorted = odd_sorted.result()

    # Combine as listas ordenadas de elementos pares e ímpares
    sorted_arr = []

    i, j = 0, 0

    while i < len(even_sorted) and j < len(odd_sorted):
        if even_sorted[i] < odd_sorted[j]:
            sorted_arr.append(even_sorted[i])
            i += 1
        else:
            sorted_arr.append(odd_sorted[j])
            j += 1

    sorted_arr.extend(even_sorted[i:])
    sorted_arr.extend(odd_sorted[j:])

    return sorted_arr

# Exemplo de uso
if __name__ == "__main__":
    unsorted_array = [9, 7, 6, 5, 1, 3, 8, 2, 4]
    sorted_array = parallel_sort(unsorted_array)
    print("Array ordenado:", sorted_array)
