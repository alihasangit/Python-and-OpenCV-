import cv2
import numpy as np

NumPlate = cv2.CascadeClassifier('haarcascades\haarcascade_russian_plate_number.xml')

img = cv2.imread('car.jpg')
Vehicle= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Num = NumPlate.detectMultiScale(Vehicle,scaleFactor=1.2,
    minNeighbors = 5, minSize=(5,5))



cv2.imshow('Car',Vehicle)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
