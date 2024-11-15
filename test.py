import cv2
import numpy as np
img=np.zeros((512,512,3))
# Rectangle
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),cv2.LINE_AA,2)
cv2.imshow("window name",img)
cv2.waitKey(0)
