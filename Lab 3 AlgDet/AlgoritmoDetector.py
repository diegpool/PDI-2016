## Algoritmo Detector!! 

from SimpleCV import*
##from matplotlib import pyplot as plt
import numpy as np
import cv2
import time
from scipy import ndimage
import pylab as pl
from Calculo_Rho import rhoCalc
import math
from distRhof import distRhot

img = Image('Fotos/1.jpg')

d = img.size()
img.resize(img.width +1, img.height+1)
A = img.getPixel(12,88)
B = img.getPixel(1,120)
rho = rhoCalc(A,B)

matImg = img.getNumpy()
print matImg[1][2]

print d 
print img.height # 480
print img.width  # 640

imgBd = np.zeros((d[0]+2 , d[1]+2))
tolBd = 1

for i in range(img.width-2):
	for j in range(img.height-2):
		At = matImg[i+1][j+1]
		Bt = matImg[i+1][j+2]
		rhot1 = rhoCalc(At,Bt)
		rhot2 = rhoCalc(Bt,At)
		if distRhot(rho,rhot1)<tolBd :
			imgBd[i+1][j+1] = 0
		elif distRhot(rho,rhot2)<tolBd :
			imgBd[i+1][j+1] = 0


        At = matImg[i][j+1]
        Bt = matImg[i+2][j+1]
        rhot1 = rhoCalc(At,Bt)
        rhot2=rhoCalc(Bt,At)
        if distRhot(rho,rhot1)<tolBd:
            imgBd[i+1][j+1]=[255 , 255 ,255]
        elif distRhot(rho,rhot2)<tolBd:
            imgBd[i+1][j+1]=[255 , 255 ,255]
        
        
        At = matImg[i][j]
        Bt = matImg[i+2][j+2]
        rhot1 = rhoCalc(At,Bt)
        rhot2 = rhoCalc(Bt,At)
        if distRhot(rho,rhot1)<tolBd :
            imgBd[i+1][j+1]=[255 , 255 ,255]
        elif distRhot(rho,rhot2)<tolBd :
            imgBd[i+1][j+1]=[255 , 255 ,255]
        
        
        At = matImg[i][j+2]
        Bt = matImg[i+2][j]
        rhot1 = rhoCalc(At,Bt)
        rhot2 = rhoCalc(Bt,At)
        if distRhot(rho,rhot1)<tolBd :
            imgBd[i+1][j+1]=[255 , 255 ,255]
        elif distRhot(rho,rhot2)<tolBd :
            imgBd[i+1][j+1]=[255 , 255 ,255]
        

img.show()
imgBd.show()

