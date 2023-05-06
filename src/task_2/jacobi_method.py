import math
import numpy as np
from utils.matrix import is_symmetric, largest_absolute_off_diagonal_value, calculate_matrix_p_jacobiano


def solve_jacobi_method(matrixA, tol, maxIter=1000):

    useErrors = []
    residue = math.inf
    steps = 0


    if(not is_symmetric(matrixA)):
        msgError = "Erro! Essa matriz não é simétrica. Tente com outros parâmetros!"
        useErrors.append(msgError)
        return([], useErrors, steps)

    matrixX =  np.identity(matrixA.shape[0])
    residue = math.inf
    position_biggest_absolute_off_diagonal_value = largest_absolute_off_diagonal_value(matrixA)


    while(residue>=tol):
    
        if(steps>maxIter):
            msgError = "Jacobi Method: max iterations reached"
            useErrors.append(msgError)
            return([], [], None, steps, useErrors)

        matrixP = calculate_matrix_p_jacobiano(matrixA, position_biggest_absolute_off_diagonal_value)

        matrixA = np.dot(np.dot(matrixP.T, matrixA), matrixP)
        matrixX = np.dot(matrixX, matrixP)

        position_biggest_absolute_off_diagonal_value = largest_absolute_off_diagonal_value(matrixA)
        residue = math.fabs(matrixA[position_biggest_absolute_off_diagonal_value])

        steps+=1

    matrixA = np.diag(matrixA)

    determinate = np.prod(matrixA)

    return([matrixA, matrixX, determinate, useErrors, steps])