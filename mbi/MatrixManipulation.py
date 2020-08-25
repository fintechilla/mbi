import numpy as np
from numpy.core._multiarray_umath import ndarray


class MM:
    A = None
    B = None

    def __init__(self):
        print("MM created")

    def setMatrices(self, dimA, dimB):
        Ar = dimA[0]
        Ac = dimA[1]
        Br = dimB[0]
        Bc = dimB[1]
        self.A = np.arange(1, Ar * Ac + 1).reshape(Ar, Ac)
        self.B = np.arange(Ar * Ac + 1, Ar * Ac + 1 + Br * Bc).reshape(Br, Bc)
        print("MM initialized")
        print("Matrix A:")
        print(self.A)
        print("Matrix B:")
        print(self.B)

    def quickDotMult(self):
        C: ndarray = np.dot(self.A, self.B)
        # self.D = self.A @ self.B

        return C

    def statMin(self, mat, axis):
        if axis == -1:
            result = np.amin(mat)
            return result
        else:
            result = np.amin(mat, axis)
            return result

    def statMax(self, mat, axis):

        if axis == -1:
            result = np.amax(mat)
            return result
        else:
            result = np.amax(mat, axis)
            return result

    def statMean(self, mat, axis):

        if axis == -1:
            result = np.mean(mat)
            return result
        else:
            result = np.mean(mat, axis)
            return result

    def cummulativeProd(self, mat, axis):

        if axis == -1:
            result = np.cumprod(mat)
            return result
        else:
            result = np.cumprod(mat, axis)
            return result
