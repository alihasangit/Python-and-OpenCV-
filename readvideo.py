import cv2
import numpy as np



PlateNum= cv2.CascadeClassifier('haarcascades\haarcascade_russian_plate_number.xml')

cap = cv2.VideoCapture('videoplayback.mp4')

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 80)


if (cap.isOpened()==False):
    print('Error Reading video')

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Num = PlateNum.detectMultiScale(gray,scaleFactor=1.2,
    minNeighbors = 5, minSize=(25,25))

    for (x,y,w,h) in Num:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        Blurr = frame[y:y+h, x:x+w]
    # apply a gaussian blur on this new recangle image
        Blurr = cv2.GaussianBlur(Blurr,(23, 23), 30)
    # merge this blurry rectangle to our final image
        frame[y:y+Blurr.shape[0], x:x+Blurr.shape[1]] = Blurr
        
    if ret == True:
        cv2.imshow('Assignment',frame)
    
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()
