def test_matrix_vector_mult():
    A_small = np.array([
        [1, 2],
        [3, 4]
    ])
    v_small = np.array([2, 3])
    
    A_special = np.array([
        [0, 2, -3],
        [4, -5, 6],
        [-7, 8, 0]
    ])
    v_special = np.array([-1, 0, 1])
    
    A_empty = np.array([[]])
    v_empty = np.array([])
    
    A_one_row = np.array([[1, 2, 3]])
    v_one_row = np.array([4, 5, 6])
    
    A_one_column = np.array([
        [7],
        [8],
        [9]
    ])
    v_one_column = np.array([10])

    # Exemplo de Matriz e Vetor
    A_example = np.array([
        [2, 4, 6, 8, 10],
        [1, 3, 5, 7, 9],
        [10, 20, 30, 40, 50],
        [5, 10, 15, 20, 25],
        [2, 3, 4, 5, 6]
    ])

    v_example = np.array([1, 2, 3, 4, 5])


    assert np.array_equal(parallel_matrix_vector_mult(A_small, v_small), [8, 18])
    assert np.array_equal(parallel_matrix_vector_mult(A_special, v_special), [-3, 2, 7])
    assert np.array_equal(parallel_matrix_vector_mult(A_empty, v_empty), [])
    assert np.array_equal(parallel_matrix_vector_mult(A_one_row, v_one_row), [32])
    assert np.array_equal(parallel_matrix_vector_mult(A_one_column, v_one_column), [70, 80, 90])
    assert np.array_equal(parallel_matrix_vector_mult(A_example, v_example), [110, 95, 550, 275, 70])
    
    return True
