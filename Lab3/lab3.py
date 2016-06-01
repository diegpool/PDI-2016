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
(red, green, blue)=img.splitChannels(False)
red.save("fotored.png")
blue.save("fotoblue.png")
green.save("fotogreen.png")
imgGris=img.grayscale()
imgGris.save("fotogris.png")

img2=green.edges(30,80)                  # algoritmo canny
img2.save("FotoEdgeG.png")
img2=red.edges(30,80)                  
img2.save("FotoEdgeR.png")
img2=blue.edges(30,80)                  
img2.save("FotoEdgeB.png")
img2=imgGris.edges(30,80)
img2.save("FotoEdgeGris.png")

img3=cv2.imread("Foto.png")            # algoritmo blob
detector=cv2.SimpleBlobDetector()
keypoints=detector.detect(img3)
wk=cv2.drawKeypoints(img3, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", wk)
cv2.waitKey(0)
