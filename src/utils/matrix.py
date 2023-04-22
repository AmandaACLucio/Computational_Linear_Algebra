import numpy as np

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