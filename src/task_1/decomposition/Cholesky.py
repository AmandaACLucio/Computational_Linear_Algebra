import numpy as np
import copy as c
from utils.matrix import forward_substituiton, backward_substituiton, is_positive_definite, is_symmetric

def decomposition_Cholesky(matrixA):

    n = matrixA.shape[0]
    matrix_L = np.zeros((n,n)).astype(float)
    useErrors = []

    if(matrixA.shape[0] != matrixA.shape[1]):
        str_error = "Erro! Essa matriz não é quadrada. Tente com outros parâmetros!"
        useErrors.append(str_error)
        return [matrix_L, useErrors]

    if(not is_symmetric(matrixA) or not is_positive_definite(matrixA)):
        str_error = "Erro! A matriz precisa ser simétrica e definida positiva. Tente com outros parâmetros!"
        useErrors.append(str_error)
        return [matrix_L, useErrors]
    
    for i in range(n):

        matrix_L[i, i] = np.sqrt(matrixA[i, i] - np.sum(matrix_L[i, 0:i]**2))

        for j in range(i+1, n):
            matrix_L[j, i] = (matrixA[j, i] - np.sum(matrix_L[i, 0:i]*matrix_L[j, 0:i]))/float(matrix_L[i, i])
    

    return [np.around(matrix_L, 2), useErrors]

def solve_decomposition_Cholesky(matrix, vector_b):
    
    "Solve LUx=b, first we have Ly=b, so we solve Ly=b and then Ux=y"

    [matrixL, useErrors] = decomposition_Cholesky(matrix)
    
    if(len(useErrors)>0):
        return [matrixL, useErrors]
    
    [SolveLyB, useErrors] = forward_substituiton(matrixL, vector_b, isLU=False)
    
    if(len(useErrors)>0):
        return [[], useErrors]

    [SolveLtxY, useErrors]=backward_substituiton(matrixL.T, SolveLyB)

    return [SolveLtxY, useErrors]