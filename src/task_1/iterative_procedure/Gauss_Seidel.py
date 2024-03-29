﻿import math
import numpy as np
from utils.matrix import converge, is_positive_definite, is_symmetric


def solve_gauss_seidel(matrixA, vectorB, tol, maxIter=1000):

    vectorX = np.ones(vectorB.shape[0])

    residue = math.inf
    residueHistoric = []
    useErrors = []
    steps = 0

    if(matrixA.shape[0] != matrixA.shape[1]):
        msgError = "Erro! Essa matriz não é quadrada. Tente com outros parâmetros!"
        useErrors.append(msgError)
        return([], residueHistoric, useErrors, steps)
    
    if(vectorB.shape[0] != matrixA.shape[1]):
        msgError= "A matriz A precisa ter o mesmo número de colunas que a quantidade de linhas do vetor B"
        useErrors.append(msgError)
        return([], residueHistoric, useErrors, steps)
    
    if(not is_symmetric(matrixA) or not is_positive_definite(matrixA)):
        if(not converge(matrixA)):
            msgError = "Erro! Essa matriz não converge. Tente com outros parâmetros!"
            useErrors.append(msgError)
            return([], residueHistoric, useErrors, steps)

    while(residue>=tol):
        if(steps>maxIter):
            msgError = "Jacobi: max iterations reached"
            useErrors.append(msgError)
            return([], residueHistoric, useErrors, steps)

        vectorXold = vectorX.copy()

        for i in range(vectorB.shape[0]):
            vectorX[i] = (vectorB[i]-np.sum(matrixA[i, 0:i]*vectorX[0:i])-np.sum(matrixA[i, i+1:]*vectorXold[i+1:]))/matrixA[i, i]

        residue = np.linalg.norm(vectorX-vectorXold)/np.linalg.norm(vectorX)
        residueHistoric.append(residue)

        steps+=1

    return [vectorX, residueHistoric, useErrors, steps]