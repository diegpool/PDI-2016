import numpy as np

def rhoCalc(A,B):
	rhoImg = np.array([A[0]/B[0] , A[1]/B[0] ,A[2]/B[0] ,  A[0]/B[1] , A[1]/B[1] , A[2]/B[1] , A[0]/B[2] , A[1]/B[2] , A[2]/B[2] ])

	return rhoImg 