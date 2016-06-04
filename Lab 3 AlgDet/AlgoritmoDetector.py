## Algoritmo Detector!! 

from SimpleCV import*
import numpy as np
import cv2
import time
from Calculo_Rho import rhoCalc

h = 320
w = 240
c = Camera()
img = c.live()
time.sleep(3)


d = img.size()
matImg = img.getNumpy().astype(dtype = 'float64')

imgBd = np.zeros((d[0] , d[1], 3))
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

imgBd = imgBd.reshape(d[0],d[1],3)
plt.figure(2)                     
plt.imshow(imgBd)
plt.show()
plt.axis("off")

time.sleep(100)
