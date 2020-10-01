import cv2
import numpy as np

plateNum = cv2.CascadeClassifier('haarcascades\haarcascade_russian_plate_number.xml')

cap = cv2.VideoCapture('videoplayback.mp4')

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 80)


if (cap.isOpened()==False):
    print('Error Reading video')



    if ret == True:
        cv2.imshow('Assignment',frame)
    
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()
