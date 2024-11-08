import cv2
import pyf_esp as pyf
from cvzone.HandTrackingModule import HandDetector


detector=HandDetector(detectionCon=0.8,maxHands=1)

video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
   
    hands,img=detector.findHands(frame)
    if hands:
        lmList=hands[0]
        finger_up=detector.fingersUp(lmList)
        print(finger_up)
        pyf.relay_trigger(finger_up)
        if finger_up==[0,1,0,0,0]:
            cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif finger_up==[0,1,1,0,0]:
            cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==ord("k"):
        break
    
pyf.board_exit()
video.release()
cv2.destroyAllWindows()