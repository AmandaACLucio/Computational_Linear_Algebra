import math
import numpy as np
from utils.matrix import is_symmetric, largest_absolute_off_diagonal_value, calculate_matrix_p_jacobiano, largest_value_off_diagonal_value


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

    while(residue>=tol):
    
        if(steps>maxIter):
            msgError = "Jacobi Method: max iterations reached"
            useErrors.append(msgError)
            return([], [], None, steps, useErrors)
        

        print("-----------------")

        print("step: ", steps)

        position_biggest_absolute_off_diagonal_value = largest_absolute_off_diagonal_value(matrixA)

        matrixP = calculate_matrix_p_jacobiano(matrixA, position_biggest_absolute_off_diagonal_value)

        matrixA = np.dot(np.dot(matrixP.T, matrixA), matrixP)
        matrixX = np.dot(matrixX, matrixP)

        print("P: ", matrixP)
        print("A: ", matrixA)
        print("X: ", matrixX)

        position_residue = largest_absolute_off_diagonal_value(matrixA)
        residue = math.fabs(matrixA[position_residue])
        print("residue: ", residue)

        print("-----------------")


        steps+=1

    matrixA = np.diag(matrixA)

    determinate = np.prod(matrixA)

    return([matrixA, matrixX, determinate, useErrors, steps])