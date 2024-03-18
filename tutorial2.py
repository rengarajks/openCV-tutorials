import cv2
import random

img=cv2.imread('assets/image.jpg',1)
img=cv2.resize(img,(800,500))


tag=img[100:200, 200:500]
img[0:100,0:300]=tag

# for i in range(0,len(img)-100):
#     for j in range(img.shape[1]):
#         img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()