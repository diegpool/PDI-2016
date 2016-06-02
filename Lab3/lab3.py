from SimpleCV import*                   # Importamos las librerias necesarias
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import numpy as np
import cv2

##c = Camera()                            # Iniciamos la camara
##time.sleep(2)                           # Asignamos un tiempo de enfoque antes de sacar la foto
##img=c.getImage()                        # Sacamos la foto      
##img.save('Foto.png')                    # Se guarda

img=Image("Foto.png")
mascara=Image("mascara.png")
(red, green, blue)=img.splitChannels(False)
red.save("fotored.png")
blue.save("fotoblue.png")
green.save("fotogreen.png")
imgGris=img.grayscale()
imgGris.save("fotogris.png")

img2=green.edges(30,80)                 # algoritmo canny
img22=img2*mascara+img
img22.save("FotoEdgeG.png")
img2=red.edges(30,80)                  
img22=img2*mascara+img
img22.save("FotoEdgeR.png")
img2=blue.edges(30,80)                  
img22=img2*mascara+img
img22.save("FotoEdgeB.png")
img2=imgGris.edges(30,80)
img22=img2*mascara+img
img22.save("FotoEdgeGris.png")

img3=green.findBlobs()                  # algoritmo blob
img3.draw((200,0,0),width=3)
img.addDrawingLayer(green.dl())
img.save("FotoBlobG.png")
img3=red.findBlobs()                  
img3.draw((200,0,0),width=3)
img.addDrawingLayer(red.dl())
img.save("FotoBlobR.png")
img3=blue.findBlobs()                  
img3.draw((200,0,0),width=3)
img.addDrawingLayer(blue.dl())
img.save("FotoBlobB.png")
img3=imgGris.findBlobs()                  
img3.draw((200,0,0),width=3)
img.addDrawingLayer(imgGris.dl())
img.save("FotoBlobGris.png")

dist=green.colorDistance(60,30,30)   # Distancia de color    
bin=dist.binarize(70).morphClose()
lines=bin.findLines(threshold=10,minlinelength=15)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("FotoDistG.png")
dist=red.colorDistance()
bin=dist.binarize(70).morphClose()
lines=bin.findLines(threshold=10,minlinelength=15)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("FotoDistR.png")
dist=blue.colorDistance()
bin=dist.binarize(70).morphClose()
lines=bin.findLines(threshold=10,minlinelength=15)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("FotoDistB.png")
dist=imgGris.colorDistance()
bin=dist.binarize(70).morphClose()
lines=bin.findLines(threshold=10,minlinelength=15)
lines.draw(width=3)
img.addDrawingLayer(bin.dl())
img.save("FotoDistGris.png")

img4 = cv2.imread('Foto.png',0)     # laplaciano         
laplacian = cv2.Laplacian(img4,cv2.CV_64F)
sobelx = cv2.Sobel(img4,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img4,cv2.CV_64F,0,1,ksize=5)
plt.imshow(sobelx,cmap = 'gray')
plt.savefig("FotoLaplaciana.png")

