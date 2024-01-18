import  cv2

Im=cv2.imread("rose.jpg")
black=cv2.cvtColor(Im,cv2.COLOR_BGR2GRAY)

cv2.imshow("color",Im)
cv2.imshow("bw",black)

cv2.waitKey(0)