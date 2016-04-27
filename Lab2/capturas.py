from SimpleCV import*
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2

c = Camera()
time.sleep(2)
img=c.getImage()
print "Guardando foto normal..."
img.save('Fotos/FotoNormal.png')
imgGris =img.grayscale()
print "Guardando foto gris..."
imgGris.save('Fotos/FotoGrayscale.png')

print "Opciones de papel:"
print "1 Blanco"
print "2 Cuadriculado"
print "3 Color"

while True:
    opcion=raw_input("Ingrese opcion: ")
    if opcion=="1":
        ## Segmentacion manual
        histogram = imgGris.histogram(255)
        plt.figure(1)
        plt.plot(histogram)
        plt.title('Histograma Escala Grises')
        print "Guardando histograma escala gris..."
        plt.savefig('Fotos/Blanco/HistGray.png')
        print "Guardando foto binarizada..."
        imgBin = imgGris.binarize(50,255,0,5)
        imgBin.save('Fotos/Blanco/Foto binarizada.png')
        imgBininv = imgBin.invert() 
        imgBininv.save('Fotos/Blanco/Foto binarizadaInvertida.png')

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
        break 

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
        imgccuad = imgGris.binarize(90,255,0,5)
        imgcuadinv=imgccuad.invert()
        imgBininv = imgBin.invert()
        imgBininv.save('Fotos/Cuadriculado/Foto binarizadaInvertida.png')
        imgcuad=imgBininv-imgcuadinv
        imgcuad.save('Fotos/Cuadriculado/cuadriculas.png')
        imgcuadn=imgcuad.invert()
        imgcuadn.save('Fotos/Cuadriculado/lineas.png')
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
        break





##(red,green,blue) = img.splitChannels(False)
##print "Guardando foto red..."
##red.save('Fotos/FotoRed.png')
##print "Guardando foto blue..."
##blue.save('Fotos/FotoBlue.png')
##print "Guardando foto green..."
##green.save('Fotos/FotoGreen.png')
##red_histogram = red.histogram(255)
##blue_histogram = blue.histogram(255)
##green_histogram = green.histogram(255)
##plt.figure(2)
##plt.plot(red_histogram)
##plt.title('Histograma Escala red')
##plt.savefig('Hist/HistRed.png')
##print "Guardando histograma escala red..."
##plt.figure(3)
##plt.plot(green_histogram)
##plt.title('Histograma Escala green')
##print "Guardando histograma escala green..."
##plt.savefig('Hist/HistGreen.png')
##plt.figure(4)
##plt.plot(blue_histogram)
##plt.title('Histograma Escala blue')
##print "Guardando histograma escala blue..."
##plt.savefig('Hist/HistBlue.png')
