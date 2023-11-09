
'''
import numpy as np
import time
from multiprocessing import Pool, cpu_count

def worker(args):
    row, v = args
    return np.dot(row, v)

def matrix_vector_mult_multiprocessing(A, v):
    with Pool(processes=cpu_count()) as pool:
        w = pool.map(worker, [(row, v) for row in A])
    return np.array(w)

M = 10000
N = 10000

A = np.random.rand(M, N)
v = np.random.rand(N)

start_time = time.time()
w = matrix_vector_mult_multiprocessing(A, v)
end_time = time.time()

print(f"Tempo de execução com multiprocessing: {end_time - start_time:.4f} segundos")
'''
import numpy as np
import time
import threading

def worker(start, end, A, v, result):
    for i in range(start, end):
        result[i] = np.dot(A[i], v)

def matrix_vector_mult_threading(A, v):
    num_threads = 1
    threads = []
    results = [0] * A.shape[0]
    chunk_size = A.shape[0] // num_threads
    
    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_threads - 1 else A.shape[0]
        t = threading.Thread(target=worker, args=(start_index, end_index, A, v, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return np.array(results)

M = 10000
N = 10000

A = np.random.rand(M, N)
v = np.random.rand(N)

start_time = time.time()
w = matrix_vector_mult_threading(A, v)
end_time = time.time()

print(f"Tempo de execução com threading: {end_time - start_time:.4f} segundos")