import math
import numpy as np
#from src.utils.matrix import is_symmetric, largest_off_diagonal_value, calculate_matrix_p_jacobiano

def largest_off_diagonal_value(matrixA):
    
    mask = np.ones(matrixA.shape, dtype=bool)
    np.fill_diagonal(mask, 0)
    row, col = np.nonzero(mask)  # encontra as coordenadas dos elementos fora da diagonal
    max_value_index = np.argmax(matrixA[row, col])
    max_value_coords = (row[max_value_index], col[max_value_index])
    return max_value_coords

def calculate_value_phi(matrixA, position):
    (i, j) = position

    if(matrixA[i,i] == matrixA[j,j]):
        return math.pi/4
    return 0.5*math.atan(2*matrixA[i,j]/(matrixA[i,i]-matrixA[j,j]))

def calculate_matrix_p_jacobiano(matrixA, position):
    
    value_phi = calculate_value_phi(matrixA, position)
    matrix_p = np.identity(matrixA.shape[0]).astype(float)
    (i, j) = position

    matrix_p[i, i] = math.cos(value_phi)
    matrix_p[j, j] = math.cos(value_phi)
    matrix_p[i, j] = -math.sin(value_phi)
    matrix_p[j, i] = math.sin(value_phi)

    return matrix_p

def is_symmetric(matrixA):
    return np.allclose(matrixA, matrixA.T)

def solve_jacobi_method(matrixA, tol, maxIter=1000):

    useErrors = []
    residue = math.inf
    steps = 0


    if(not is_symmetric(matrixA)):
        msgError = "Erro! Essa matriz não é simétrica. Tente com outros parâmetros!"
        useErrors.append(msgError)
        return([], useErrors, steps)

    while(residue>=tol):
    
        if(steps>maxIter):
            msgError = "Jacobi Method: max iterations reached"
            useErrors.append(msgError)
            return([], [], None, steps, useErrors)
        

        if(steps==0):
            matrixX =  np.identity(matrixA.shape[0])
            position_biggest_off_diagonal_value = largest_off_diagonal_value(matrixA)

        matrixP = calculate_matrix_p_jacobiano(matrixA, position_biggest_off_diagonal_value)

        matrixA = np.dot(np.dot(matrixP.T, matrixA), matrixP)
        matrixX = np.dot(matrixX, matrixP)


        position_biggest_off_diagonal_value = largest_off_diagonal_value(matrixA)
        residue = matrixA[position_biggest_off_diagonal_value]

        steps+=1

    matrixA = np.diag(matrixA)

    determinate = np.prod(matrixA)

    return([matrixA, matrixX, determinate, useErrors, steps])


print(solve_jacobi_method(np.array([[1, 0.2, 0], [0.2, 1, 0.5], [0, 0.5, 1]]), 0.01))