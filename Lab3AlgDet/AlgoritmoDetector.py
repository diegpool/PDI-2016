## Algoritmo Detector!! 

from SimpleCV import*
import numpy as np
import cv2
import time
import ast
from Calculo_Rho import rhoCalc

h = 240   # Se asignan las dimensiones de la imagen
w = 320

c = Camera(0,{"width":w,"height":h}) # Con esto se inicializa la camara con las dimensiones entregadas
Captura = 's' # Es la opcion para capturar hasta que salga la foto bien
while Captura == 's': 	#Ciclo de captura
	img = c.live()  #Desplegamos la camara hasta que queramos capturar
	print 'Permanezca quieto por favor...'
	time.sleep(3) # Le damos un tiempo muerto para que la camara enfoque
	img = c.getImage() # Capturamos la imagen
	print 'Imagen capturada !' 
	Sample = img.show() # Mostramos la imagen capturada
	print 'Desea tomar otra foto?'
	Captura = raw_input('[s]i o [n]o-> ') # Ingremos la opcion si la foto quedo mal sacada


Sample.quit() # Cerramos la imagen mostrada
img.save('Fotos/CapturaInicial.png') # Guardamos la imagen capturada

matImg = img.getNumpy().astype(dtype='float64') # Transformamos la imagen en array numpy con tipo float64 de datos para evitar perdidas por redondeo
d = matImg.shape # obtenemos las dimensiones de la array
colorBd = np.array([255,0,0],dtype='float64') # Definimos como color de borde el rojo como convencion para que se note al sumar ambas imagenes

A=np.array([86,53,36],dtype='float64') # Valores de material A y B obtenidos por entrenamiento
B=np.array([133,119,63],dtype='float64')
rho = rhoCalc(A,B); # Se calcula el rho entre el material A y B obtenido por el entrenamiento

print 'Para seleccionar el valor de la tolerancia considere que a mayor exposicion a la luz mas tolerancia, e inverso entre menos luz menos tolerancia'
print 'Valor medio recomendado tol = 1' # nos da la opcion de elegir el valor de rho , sin embargo , nos entrega una media bastante funcional

Probar = 's'
while Probar == 's': # Ingremos al ciclo para detectar los bordes 
	matBd = np.zeros_like(matImg) # creamos una matriz de ceros para ir almacenando los bordes detectados 
	tolBd = raw_input('Ingrese el valor de la tolerancia->') # ingresamos el valor de Tolerancia
	tolBd = float(tolBd) # lo manejamos como valor float

	print 'Detectando pixeles de borde con tol = ' # Comienza a detectar los pixeles de borde
	print tolBd
	for i in range(img.width-2): # Empieza a recorrer la imagen para detectar los bordes
		for j in range(img.height-2):

			At = matImg[i][j+1] # Detector horizontal 
			Bt = matImg[i+2][j+1]
			rhot1 = rhoCalc(At,Bt) # Calculamos los rho temporales y el rho inverso
			rhot2 = rhoCalc(Bt,At)
			if np.linalg.norm(rho - rhot1)<tolBd : #Comparamos los rho temporal con el base
				matBd[i+1][j+1] = colorBd
			elif np.linalg.norm(rho - rhot2)<tolBd :
				matBd[i+1][j+1] = colorBd


			At = matImg[i+1][j]  # Detector vertical
			Bt = matImg[i+1][j+2]
			rhot1 = rhoCalc(At,Bt) # Calculamos los rho temporales y el rho inverso
			rhot2 = rhoCalc(Bt,At)
			if np.linalg.norm(rho - rhot1)<tolBd: #Comparamos los rho temporal con el base
			    	matBd[i+1][j+1]=colorBd
			elif np.linalg.norm(rho - rhot2)<tolBd:
			    	matBd[i+1][j+1]=colorBd
			
		
			At = matImg[i][j]	#Detector Diagonal
			Bt = matImg[i+2][j+2]
			rhot1 = rhoCalc(At,Bt)	# Calculamos los rho temporales y el rho inverso
			rhot2 = rhoCalc(Bt,At)
			if np.linalg.norm(rho - rhot1)<tolBd : #Comparamos los rho temporal con el base
			    	matBd[i+1][j+1]=colorBd
			elif np.linalg.norm(rho - rhot2)<tolBd :
			    	matBd[i+1][j+1]=colorBd
			
			At = matImg[i][j+2]	#Detector Diagonal
			Bt = matImg[i+2][j]
			rhot1 = rhoCalc(At,Bt)	# Calculamos los rho temporales y el rho inverso
			rhot2 = rhoCalc(Bt,At)
			if np.linalg.norm(rho - rhot1)<tolBd : #Comparamos los rho temporal con el base
			    	matBd[i+1][j+1]=colorBd
			elif np.linalg.norm(rho - rhot2)<tolBd :
				matBd[i+1][j+1]=colorBd
	
	print 'Escaneo completado!'
	imgBd = Image(matBd) # Se convierte la matriz de pixeles de borde en imagen 
	ImgFinal = img+imgBd # Se suma la imagen de borde a la original para que se vea 
	Show = ImgFinal.show() # Se muestra la imagen
	Probar = raw_input('Desea probar con otro valor de tolerancia?: [s]i o [n]o ->')
	#Nos da la opcion de detectar los pixeles de borde con otra tolerancia.
	Show.quit()# Cerramos la imagen mostrada


ImgFinal.save('Fotos/FotoFinal.png') #Guardamos la imagen final.
print 'Adios !'
