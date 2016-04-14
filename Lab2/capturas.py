from SimpleCV import Camera , Display , Image

c = Camera()

img=c.getImage()
img.save('Foto1.png')
imgGris =img.toGray()
imgGris.save('Foto2.png')
hist = imgGris.histogram(255)
ploteo=plot(hist)
ploteo.save('Histograma1.png')
