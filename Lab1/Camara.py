from SimpleCV import Camera , Display , Image, time

c = Camera(0,{"width":320,"height":240})

img = c.live()
print 'Permanezca quieto por favor...'
time.sleep(3)
img = c.getImage()
print 'Imagen capturada !'
img.save('Foto.jpg')

