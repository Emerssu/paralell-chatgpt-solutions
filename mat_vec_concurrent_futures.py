import numpy as np
import concurrent.futures
    
M = 1000  # Número de linhas da matriz
N = 1000  # Número de colunas da matriz
NUM_THREADS = 6  # Número de threads a serem usadas
    
def matrix_vector_mult_row(start, end, A, v, result):
    M, N = A.shape
    for i in range(start, end):
        result[i] = np.dot(A[i], v)
    
def parallel_matrix_vector_mult(A, v):
    M, N = A.shape
    w = np.zeros(M)
    thread_list = []
    chunk_size = M // NUM_THREADS
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = []
        for i in range(NUM_THREADS):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < NUM_THREADS - 1 else M
            futures.append(executor.submit(matrix_vector_mult_row, start, end, A, v, w))
            
        concurrent.futures.wait(futures)
    
    return w
    
# Exemplo de uso
A = np.random.rand(M, N)
v = np.random.rand(N)
result = parallel_matrix_vector_mult(A, v)