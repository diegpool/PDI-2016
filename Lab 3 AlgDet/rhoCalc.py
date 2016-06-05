import numpy as np

def rhoCalc(A,B):

Ar = A[1]
Ag = A[2]
Ab = A[3]
Br = B[1]
Bg = B[2]
Bb = B[3]
rhoImg = [Ar/Br Ag/Br Ab/Br Ar/Bg Ag/Bg Ab/Bg Ar/Bb Ag/Bb Ab/Bb];
return rhoImg
