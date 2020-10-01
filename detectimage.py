import cv2
import numpy as np

NumPlate = cv2.CascadeClassifier('haarcascades\haarcascade_russian_plate_number.xml')

img = cv2.imread('car.jpg')
Vehicle= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Num = NumPlate.detectMultiScale(Vehicle,scaleFactor=1.2,
    minNeighbors = 5, minSize=(5,5))

for (x,y,w,h) in Num:
    cv2.rectangle(Vehicle,(x,y),(x+w,y+h),(0,0,191),10)
    Blurr = Vehicle[y:y+h, x:x+w]
    # apply a gaussian blur on this new recangle image
    Blurr = cv2.GaussianBlur(Blurr,(23, 23), 30)
    # merge this blurry rectangle to our final image
    Vehicle[y:y+Blurr.shape[0], x:x+Blurr.shape[1]] = Blurr



cv2.imshow('Car',Vehicle)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
