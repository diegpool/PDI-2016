from SimpleCV import Camera , Display , Image

time.sleep(3)
c = Camera()

img = c.getImage()
img.save('Foto.png')

