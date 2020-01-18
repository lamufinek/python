# nalezy zaintsalowac biblioteke OpenCV- w cmd nalezy wpisac "pip install opencv-python"
import cv2
import random
import time
import keyboard


klatka = cv2.VideoCapture(0)
klatka.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
klatka.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def losowanieSrodka():
    x=random.randint(200,1000)
    y=random.randint(100,500)
    srodek = x,y
    return srodek


srodek = 640,360
while(True):
    ret,ramka = klatka.read()

    szary = cv2.cvtColor(ramka, cv2.COLOR_BGR2GRAY)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(szary)

    if(abs(maxLoc[0]-srodek[0])<100 and abs(maxLoc[1]-srodek[1])<100):
        srodek = losowanieSrodka()
    
    cv2.circle(szary, srodek, 50, (255, 0, 255), 20)

    cv2.imshow('obrazek',szary)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

klatka.release()
cv2.destroyAllWindows()
