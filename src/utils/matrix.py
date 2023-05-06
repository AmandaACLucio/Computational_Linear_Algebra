import math
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

def backward_substituiton(matrixA, vectorB, useErrors=[]):
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

def converge(matrixA):
    
    if(matrixA.shape[0] != matrixA.shape[1]):
        print("A matriz precisa ser quadrada para realizar essa operação")
        return -1

    n = matrixA.shape[0]
    for i in range(n):

        sum_line = np.sum(np.abs(matrixA[i, 0:i]))+np.sum(np.abs(matrixA[i, i+1:]))
        sum_column = np.sum(np.abs(matrixA[0:i,i]))+np.sum(np.abs(matrixA[i+1:, i]))

        if(sum_column > matrixA[i,i] or sum_line > matrixA[i,i]):
            return False

    return True

def largest_absolute_off_diagonal_value(matrixA):

    mask = np.ones(matrixA.shape, dtype=bool)
    np.fill_diagonal(mask, 0)
    row, col = np.nonzero(mask)  # encontra as coordenadas dos elementos fora da diagonal
    maxValueIndex = np.argmax(np.absolute((matrixA[row, col])))
    maxValueCoords = (row[maxValueIndex], col[maxValueIndex])
    return maxValueCoords

def calculate_value_phi(matrixA, position):
    (i, j) = position

    if(matrixA[i,i] == matrixA[j,j]):
        return math.pi/4
    return 0.5*math.atan(2*matrixA[i,j]/(matrixA[i,i]-matrixA[j,j]))

def calculate_matrix_p_jacobiano(matrixA, position):
    
    valuePhi = calculate_value_phi(matrixA, position)
    matrixP = np.identity(matrixA.shape[0])
    (i, j) = position

    matrixP[i, i] = math.cos(valuePhi)
    matrixP[j, j] = math.cos(valuePhi)
    matrixP[i, j] = -math.sin(valuePhi)
    matrixP[j, i] = math.sin(valuePhi)

    return matrixP