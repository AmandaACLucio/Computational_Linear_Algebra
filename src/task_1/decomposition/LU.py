import numpy as np
import copy as c
from src.utils.matrix import forward_substituiton, backward_substituiton

def decomposition_LU(matrixLU):
    
    n = matrixLU.shape[0]
    #matrixLU = np.copy(matrixA).astype(float)
    useErrors = []

    if(matrixLU.shape[0] != matrixLU.shape[1]):
        msgError = "Erro! Essa matriz não é quadrada. Tente com outros parâmetros!"
        useErrors.append(msgError)
        return [matrixLU, useErrors]

    for k in range(n-1):
        matrixLU[k+1:n, k] = matrixLU[k+1:n, k] / matrixLU[k, k]
        matrixLU[k+1:n, k+1:n] -= np.outer(matrixLU[k+1:n, k], matrixLU[k, k+1:n])

    
    return [matrixLU, useErrors]

def solve_decomposition_LU(matrix, vector_b):
    
    "Solve LUx=b, first we have Ly=b, so we solve Ly=b and then Ux=y"

    [matrixLU, useErrors] = decomposition_LU(matrix)

    
    if(len(useErrors)>0):
        return [matrixLU, useErrors]
    
    [SolveLyB, useErrors] = forward_substituiton(matrixLU, vector_b)
    
    if(len(useErrors)>0):
        return [[], useErrors]

    [SolveUxY, useErrors]=backward_substituiton(matrixLU, SolveLyB)

    return [SolveUxY, useErrors]

