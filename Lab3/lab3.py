from SimpleCV import*                   # Importamos las librerias necesarias
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
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

##keypoints=detector.detect(img3)
##wk=cv2.drawKeypoints(img3, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
##cv2.imshow("Keypoints", wk)
##cv2.waitKey(0)
