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
        plt.savefig('Fotos/HistGray.png')
        print "Guardando foto binarizada..."
        imgBin = imgGris.binarize(50,255,0,5)
        imgBin.save('Fotos/Foto binarizada.png')
        imgBininv = imgBin.invert()
        imgBininv.save('Fotos/Foto binarizadaInvertida.png')
        ##Segmentacion Kmeans

        break 

    if opcion=="2":
        ## Segmentacion manual
        histogram = imgGris.histogram(255)
        plt.figure(1)
        plt.plot(histogram)
        plt.title('Histograma Escala Grises')
        print "Guardando histograma escala gris..."
        plt.savefig('Fotos/HistGray.png')
        print "Guardando foto binarizada..."
        imgBin = imgGris.binarize(75,255,0,5)
        imgBin.save('Fotos/Foto binarizada.png')
        imgBininv = imgBin.invert()
        imgBininv.save('Fotos/Foto binarizadaInvertida.png')
        ##Segmentacion Kmeans

        break


    if opcion=="3":

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
