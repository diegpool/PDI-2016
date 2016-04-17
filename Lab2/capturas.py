from SimpleCV import*
import matplotlib.pyplot as plt

c = Camera()

img=c.getImage()
img.save('FotoNormal.png')
imgGris =img.grayscale()
imgGris.save('FotoGrayscale.png')

histogram = imgGris.histogram(255)
plt.figure(1)
plt.plot(histogram)
plt.title('Histograma Escala Grises')
plt.savefig('HistGray.png')

(red,green,blue) = img.splitChannels(False)
red.save('FotoRed.png')
blue.save('FotoBlue.png')
green.save('FotoGreen.png')
red_histogram = red.histogram(255)
blue_histogram = blue.histogram(255)
green_histogram = green.histogram(255)
plt.figure(2)
plt.plot(red_histogram)
plt.title('Histograma Escala red')
plt.savefig('HistRed.png')
plt.figure(3)
plt.plot(green_histogram)
plt.title('Histograma Escala green')
plt.savefig('HistGreen.png')
plt.figure(4)
plt.plot(blue_histogram)
plt.title('Histograma Escala blue')
plt.savefig('HistBlue.png')






