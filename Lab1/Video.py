from SimpleCV import Camera , Display , Image

c = Camera()

while True:
    img = c.getImage()
    img.show()
