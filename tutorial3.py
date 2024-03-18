import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:

    ret,frame=cap.read()

    frame=cv2.resize(frame,(300,200))
    frame=np.zeros(frame.shape)


    cv2.imshow('Frame',frame)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()