## Algoritmo Detector!! 

from SimpleCV import*
import numpy as np
import cv2
import time
import ast
from Calculo_Rho import rhoCalc
import os

h = 240
w = 320

c = Camera(0,{"width":w,"height":h})
Captura = 's'
while Captura == 's':
	img = c.live()
	print 'Permanezca quieto por favor...'
	time.sleep(3)
	img = c.getImage()
	print 'Imagen capturada !'
	Sample = img.show()
	print 'Desea tomar otra foto?'
	Captura = raw_input('[s]i o [n]o-> ')


Sample.quit()
img.save('Fotos/CapturaInicial.png')

matImg = img.getNumpy().astype(dtype='float64')
d = matImg.shape
matBd = np.zeros_like(matImg)
colorBd = np.array([255,0,0],dtype='float64')

A=np.array([86,53,36],dtype='float64')
B=np.array([133,119,63],dtype='float64')
rho = rhoCalc(A,B);

print 'Para seleccionar el valor de la tolerancia considere que a mayor exposicion a la luz mas tolerancia, e inverso entre menos luz menos tolerancia'
print 'Valor medio recomendado tol = 1'
porcentaje = 0
Probar = 's'
while Probar == 's':
	matBd = np.zeros_like(matImg)
	tolBd = raw_input('Ingrese el valor de la tolerancia->')
	tolBd = float(tolBd)

	print 'Detectando pixeles de borde con tol = '
	print tolBd
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


			At = matImg[i+1][j]
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
	Probar = raw_input('Desea probar con otro valor de tolerancia?: [s]i o [n]o ->')
	Show.quit()


ImgFinal.save('Fotos/FotoFinal.png')
print 'Adios !'
