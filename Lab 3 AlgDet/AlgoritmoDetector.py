## Algoritmo Detector!! 

from SimpleCV import*
import numpy as np
import cv2
import time
from Calculo_Rho import rhoCalc



c = Camera()
img = c.live()
print 'Permanezca quieto por favor...'
time.sleep(3)
img = c.getImage()
print 'Imagen capturada !'

matImg = img.getNumpy()
d = matImg.shape
matBd = np.zeros_like(matImg)
colorBd = np.array((255,255,255))

A=np.array([86,53,36])
B=np.array([133,119,63])
rho = rhoCalc(A,B);

tolBd = 1
print 'Detectando pixeles de borde...'
pt = '.'
for i in range(img.width-2):
	for j in range(img.height-2):

		At = matImg[i][j+1]
		Bt = matImg[i+2][j+1]
		rhot1 = rhoCalc(At,Bt)
		rhot2 = rhoCalc(Bt,At)
		if np.linalg.norm(rho - rhot1)<tolBd :
			matBd[i+1][j+1] = colorBd
		elif np.linalg.norm(rho - rhot2)<tolBd :
			matBd[i+1][j+1] = colorBd


        At = matImg[i][j]
        Bt = matImg[i+1][j+2]
        rhot1 = rhoCalc(At,Bt)
        rhot2=rhoCalc(Bt,At)
        if np.linalg.norm(rho - rhot1)<tolBd:
            matBd[i+1][j+1]=colorBd
        elif np.linalg.norm(rho - rhot2)<tolBd:
            matBd[i+1][j+1]=colorBd
        
        
        At = matImg[i][j]
        Bt = matImg[i+2][j+2]
        rhot1 = rhoCalc(At,Bt)
        rhot2 = rhoCalc(Bt,At)
        if np.linalg.norm(rho - rhot1)<tolBd :
            matBd[i+1][j+1]=colorBd
        elif np.linalg.norm(rho - rhot2)<tolBd :
            matBd[i+1][j+1]=colorBd
        
        At = matImg[i][j+2]
        Bt = matImg[i+2][j]
        rhot1 = rhoCalc(At,Bt)
        rhot2 = rhoCalc(Bt,At)
        if np.linalg.norm(rho - rhot1)<tolBd :
            matBd[i+1][j+1]=colorBd
        elif np.linalg.norm(rho - rhot2)<tolBd :
            matBd[i+1][j+1]=colorBd
        



print 'Escaneo completado!'
imgBd = Image(matBd)
ImgFinal = img+imgBd
Show = ImgFinal.show()
time.sleep(100)