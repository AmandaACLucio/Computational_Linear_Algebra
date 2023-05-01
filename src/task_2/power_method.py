import math
import numpy as np


def solve_power_method(matrixA, tol, maxIter=1000):

    useErrors = []

    residue = math.inf
    steps = 0

    while(residue>=tol):

        if(steps>maxIter):
            msgError = "Power Method: max iterations reached"
            useErrors.append(msgError)
            return([], [], steps, useErrors)
        
        if(steps==0):
            eigenVector = np.ones(matrixA.shape[1])
            eigenValue = 1

        vectorY = np.dot(matrixA, eigenVector)
        eigenValueNext = np.max(vectorY)
        eigenVector = vectorY/eigenValueNext

        residue = math.fabs(eigenValueNext-eigenValue)/math.fabs(eigenValueNext)

        eigenValue = eigenValueNext
        steps+=1

    return [eigenValue, eigenVector, steps, useErrors]