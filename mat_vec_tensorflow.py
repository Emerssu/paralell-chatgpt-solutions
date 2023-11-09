import numpy as np
import concurrent.futures
import tensorflow as tf
    
M = 1000  # Número de linhas da matriz
N = 1000  # Número de colunas da matriz
NUM_THREADS = 6  # Número de threads a serem usadas
    
def matrix_vector_mult(A, v):
    # Utilize TensorFlow para fazer a multiplicação da matriz por vetor
    w = tf.linalg.matvec(A, v)
    return w
    
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
            futures.append(executor.submit(matrix_vector_mult, A[start:end], v))
            
        concurrent.futures.wait(futures)
    
        for i, future in enumerate(futures):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < NUM_THREADS - 1 else M
            w[start:end] = future.result()
        
    return w
    
# Exemplo de uso
A = np.random.rand(M, N)
v = np.random.rand(N)
A = tf.constant(A, dtype=tf.float32)
v = tf.constant(v, dtype=tf.float32)
    
    result = parallel_matrix_vector_mult(A, v)
