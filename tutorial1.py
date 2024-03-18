import cv2

img=cv2.imread('assets/image.jpg',0)
img=cv2.resize(img,(0,0),fx=0.25,fy=0.25)

cv2.imshow('image 1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()