from SimpleCV import*

c = Camera()

img=c.getImage()
img.save('FotoNormal.png')
imgGris =img.grayscale()
imgGris.save('FotoGrayscale.png')

histogram = imgGris.histogram(255)
b = range(256)
plt.plot(b,histogram)

(red,green,blue) = img.splitChannels(False)
red.save('FotoRed.png')
blue.save('FotoBlue.png')
green.save('FotoGreen.png')
red_histogram = red.histogram(255)
blue_histogram = blue.histogram(255)
green_histogram = green.histogram(255)





