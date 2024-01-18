import cv2

facedetect = cv2.CascadeClassifier('defult.xml')
img=cv2.imread('imgg.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=facedetect.detectMultiScale(gray,1.2,4)

for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
cv2.imshow('r',img)
