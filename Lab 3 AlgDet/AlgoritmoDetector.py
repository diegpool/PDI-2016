## Algoritmo Detector!! 

from SimpleCV import*
##from matplotlib import pyplot as plt
import numpy as np
import cv2
import time
from scipy import ndimage
import pylab as pl
from Calculo_Rho import rhoCalc



img = Image('Fotos/1.jpg')

d = img.size()

A = img.getPixel(12,88)
B = img.getPixel(1,120)
rho = rhoCalc(A,B)

matImg = img.getNumpy()
print matImg[1][2]
print img.getPixel(1,2)

print rho
print img.height # 480
print img.width  # 640



