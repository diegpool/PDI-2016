
from SimpleCV import*
import matplotlib.pyplot as plt

c = Camera()

img=c.getImage()

print "Guardando foto normal..."
img.save('Fotos/FotoNormal.png')
imgGris =img.grayscale()
print "Guardando foto gris..."
imgGris.save('Fotos/FotoGrayscale.png')

histogram = imgGris.histogram(255)
plt.figure(1)
plt.plot(histogram)
plt.title('Histograma Escala Grises')
print "Guardando histograma escala gris..."
plt.savefig('Hist/HistGray.png')

(red,green,blue) = img.splitChannels(False)
print "Guardando foto red..."
red.save('Fotos/FotoRed.png')
print "Guardando foto blue..."
blue.save('Fotos/FotoBlue.png')
print "Guardando foto green..."
green.save('Fotos/FotoGreen.png')
red_histogram = red.histogram(255)
blue_histogram = blue.histogram(255)
green_histogram = green.histogram(255)
plt.figure(2)
plt.plot(red_histogram)
plt.title('Histograma Escala red')
plt.savefig('Hist/HistRed.png')
print "Guardando histograma escala red..."
plt.figure(3)
plt.plot(green_histogram)
plt.title('Histograma Escala green')
print "Guardando histograma escala green..."
plt.savefig('Hist/HistGreen.png')
plt.figure(4)
plt.plot(blue_histogram)
plt.title('Histograma Escala blue')
print "Guardando histograma escala blue..."
plt.savefig('Hist/HistBlue.png')

print "Guardando foto binarizada..."
imgBin = img.binarize(170)
imgBin.save('Fotos/Foto binarizada.png')
