import numpy as np
import copy as c
#from src.utils.matrix import forward_substituiton, backward_substituiton, is_positive_definite, is_symmetric
def forward_substituiton(matrixA, vectorB, isLU=True, useErrors=[]):
    n = vectorB.shape[0]
    vectorX = np.zeros(n).astype(float)

    if(n != matrixA.shape[1]):
        msgError= "A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas do vetor"
        useErrors.append(msgError)
        return [[], useErrors]

    if(isLU):
        vectorX[0] = vectorB[0]
    else:
        vectorX[0] = vectorB[0]/matrixA[0][0]

    for i in range(n):
        vectorX[i] = vectorB[i] -np.dot(matrixA[i,0:i], vectorX[0:i])

        if not isLU:
            vectorX[i] /= matrixA[i, i]

    return [vectorX, useErrors]

def backward_substituiton(matrixA, vectorB, isLU=True, useErrors=[]):
    n = vectorB.shape[0]
    vectorX = np.zeros(n).astype(float)

    if(n != matrixA.shape[1]):
        msgError= "A matriz 1 precisa ter o mesmo número de colunas que a quantidade de linhas do vetor"
        useErrors.append(msgError)
        return [[], useErrors]


    vectorX[n-1] = vectorB[n-1]/matrixA[n-1][n-1]

    for i in range(n-1, -1, -1):
        vectorX[i] = (vectorB[i]-np.dot(matrixA[i, i+1:n], vectorX[i+1:n]))/float(matrixA[i, i])

    return [vectorX, useErrors]

def is_positive_definite(matrixA):
    return np.all(np.linalg.eigvals(matrixA) > 0)

def is_symmetric(matrixA):
    return np.allclose(matrixA, matrixA.T)

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
    print(matrixL)

    
    if(len(useErrors)>0):
        return [matrixL, useErrors]
    
    [SolveLyB, useErrors] = forward_substituiton(matrixL, vector_b)
    
    if(len(useErrors)>0):
        return [[], useErrors]

    [SolveLtxY, useErrors]=backward_substituiton(matrixL.T, SolveLyB)

    return [SolveLtxY, useErrors]