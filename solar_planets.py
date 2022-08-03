from msilib.schema import Font
import cv2
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np

img=cv2.imread("solar_system.jpg")
cv2.putText(img,"sun",(20,300),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255) )

cv2.imshow("output",img)
cv2.waitKey(0)