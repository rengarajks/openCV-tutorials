import cv2

img=cv2.imread('assets/image.jpg',-1)
img=cv2.resize(img,(0,0),fx=0.25,fy=0.25)
img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)


#save
cv2.imwrite('new_image.jpg',img)

cv2.imshow('image 1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()