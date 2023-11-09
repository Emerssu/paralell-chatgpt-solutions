import numpy as np
import multiprocessing

M = 1000  # Número de linhas da matriz
N = 1000  # Número de colunas da matriz

def matrix_vector_mult_row(i, A, v, result):
    M, N = A.shape
    result[i] = np.dot(A[i], v)

#Explica o que faz o codigo abaixo:
# 1. Cria uma pool de processos
# 2. Cria uma lista de tuplas com os argumentos para a funcao matrix_vector_mult_row
# 3. Executa a funcao matrix_vector_mult_row para cada tupla da lista de tuplas
# 4. Fecha a pool de processos
# 5. Espera todos os processos terminarem
# 6. Retorna o vetor w
def parallel_matrix_vector_mult(A, v):
    M, N = A.shape
    w = np.zeros(M)
    
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_cores)
    
    result = pool.starmap(matrix_vector_mult_row, [(i, A, v, w) for i in range(M)])
    pool.close()
    pool.join()
    
    return w

# Exemplo de uso
A = np.random.rand(M, N)
v = np.random.rand(N)
result = parallel_matrix_vector_mult(A, v)