# -*- coding: utf-8 -*-
from SimpleCV import*                   # Importamos las librerias necesarias
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2

c = Camera()                            # Iniciamos la camara
time.sleep(2)                           # Asignamos un tiempo de enfoque antes de sacar la foto
img=c.getImage()                        # Sacamos la foto
print "Guardando foto normal..."        
img.save('Fotos/FotoNormal.png')        # Se guarda
imgGris =img.grayscale()                # Se le aplica escala de grises
print "Guardando foto gris..."
imgGris.save('Fotos/FotoGrayscale.png') # Se guarda foto con escala de gris aplicada

print "Opciones de papel:"              # Menú de selección de tipo de papel.
print "1 Blanco"
print "2 Cuadriculado"
print "3 Color"
print "4 Salir"

while True:
    opcion=raw_input("Ingrese opcion: ")
    if opcion=="1":
        ## Segmentacion manual
        histogram = imgGris.histogram(255)          #Se obtiene el histograma
        plt.figure(1)
        plt.plot(histogram)
        plt.title('Histograma Escala Grises')
        print "Guardando histograma escala gris..."
        plt.savefig('Fotos/Blanco/HistGray.png')
        print "Guardando foto binarizada..."
        imgBin = imgGris.binarize(50,255,0,5)       # Se binariza la imagen
        imgBin.save('Fotos/Blanco/Foto binarizada.png')
        imgBininv = imgBin.invert()                 # Se invierte la foto binarazada, para mostrar los resultados
        imgBininv.save('Fotos/Blanco/Foto binarizadaInvertida.png')
        print "Desea continuar y usar k-means?"
        sn = raw_input("s/n")

        if sn=="s":
            ##Segmentacion Kmeans
            image = cv2.imread("Fotos/FotoNormal.png")  # Se carga la imagen a trabajar
            (largo,ancho)=image.shape[:2]               # Se guardan las dimensiones de la imagen
            image = image.reshape((image.shape[0] * image.shape[1], 3)) # Se arregla la imagen para poder aplicarle el kmenas
            clt = KMeans(n_clusters = 2)                # aplicamos kmeans con 2 clusters
            limites= clt.fit_predict(image)             # guardamos limites de segmentacion
            quant=clt.cluster_centers_.astype("uint8")[limites]     # cuantizamos la imagen
            quant=quant.reshape(largo,ancho,3)          # volvemos al tamaño de la imagen original
            plt.figure(2)                                # ploteamos la figura resultante
            plt.imshow(quant)
            plt.show()
            plt.axis("off")
            plt.imsave("Fotos/Blanco/Kmeans.png")
            break
        if sn=="n":
            break
                                                    # El proceso para los siguientes tipos de papel, sigue la misma linea sin 
                                                    #presentar grandes diferencias
    if opcion=="2":
        ## Segmentacion manual
        histogram = imgGris.histogram(255)
        plt.figure(1)
        plt.plot(histogram)
        plt.title('Histograma Escala Grises')
        print "Guardando histograma escala gris..."
        plt.savefig('Fotos/Cuadriculado/HistGray.png')
        
        print "Guardando foto binarizada..."
        imgBin = imgGris.binarize(60,255,0,5)
        imgBin.save('Fotos/Cuadriculado/Foto binarizada con cuadriculas.png')
        imgccuad = imgGris.binarize(120,255,0,5)
        imgcuadinv=imgccuad.invert()
        imgBininv = imgBin.invert()
        imgBininv.save('Fotos/Cuadriculado/Foto binarizadaInvertida.png')
        imgcuad=imgBininv-imgcuadinv
        imgcuad.save('Fotos/Cuadriculado/cuadriculas.png')
        imgcuadn=imgcuad.invert()
        imgcuadn.save('Fotos/Cuadriculado/lineas.png')

        print "Desea continuar y usar k-means?"
        sn = raw_input("s/n")

        if sn=='s':
            ##Segmentacion Kmeans
            image = cv2.imread("Fotos/FotoNormal.png")
            (largo,ancho)=image.shape[:2]
            image = image.reshape((image.shape[0] * image.shape[1], 3))
            clt = KMeans(n_clusters = 2)
            limites= clt.fit_predict(image)
            quant=clt.cluster_centers_.astype("uint8")[limites]
            quant=quant.reshape(largo,ancho,3)
            plt.figure()
            plt.axis("off")
            plt.imshow(quant)
            plt.show()
            #plt.save("Fotos/Cuadriculado/Kmeans.png")
            break
        if sn=="n":
            break

    if opcion=="3":
        ## Segmentacion manual
        histogram = imgGris.histogram(255)
        plt.figure(1)
        plt.plot(histogram)
        plt.title('Histograma Escala Grises')
        print "Guardando histograma escala gris..."
        plt.savefig('Fotos/Color/HistGray.png')
        print "Guardando foto binarizada..."
        imgBin = imgGris.binarize(50,255,0,5)
        imgBin.save('Fotos/Color/Foto binarizada.png')
        imgBininv = imgBin.invert()
        imgBininv.save('Fotos/Color/Foto binarizadaInvertida.png')
        print "Desea continuar y usar k-means?"
        sn = raw_input("s/n")

        if sn=="s":
            ##Segmentacion Kmeans
            image = cv2.imread("Fotos/FotoNormal.png")
            (largo,ancho)=image.shape[:2]
            image = image.reshape((image.shape[0] * image.shape[1], 3))
            clt = KMeans(n_clusters = 2)
            limites= clt.fit_predict(image)
            quant=clt.cluster_centers_.astype("uint8")[limites]
            quant=quant.reshape(largo,ancho,3)
            plt.figure(2)
            plt.show(quant)
            plt.axis("off")
            plt.show()
            plt.imsave("Fotos/Color/Kmeans.png")
            break
        if sn=="n":
            break
    if opcion=="4":
        break
