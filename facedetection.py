import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img = cv2.imread('crowd.jpg')
faces = face_cascade.detectMultiScale(img, 1.1, 6)

for (a,b,c,d) in faces:
    img = cv2.rectangle(img,(a,b),(a+c,b+d),(255,255,0),3)
    roi_color = img[b:b+d, a:a+c]
    

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
