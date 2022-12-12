import numpy as np
import cv2
from mss import mss
from PIL import Image
import pyautogui as p

mon = {
     'top': 200, 
     'left': 160,
     'width': 800,
     'height': 200
}
mss = mss()                                          
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (50,50) 
fontScale = 1
fontColor = (255,0,0)
lineType = 2
xcnts = []
count = 0
last_count = 0

while True:
     mss.get_pixels(mon)
     img = Image.frombytes('RGB', (mss.width, mss.height), mss.image)
     img_arr = np.array(img)
     obj = img_arr[125:155 , 110:155]
     gray = cv2.cvtColor(obj, cv2.COLOR_BGR2GRAY)  
     th, threshed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) 
     cnts = cv2.findContours(threshed, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2] 
     count = len(cnts)
     if count >= 1:
          print("Прыжок")
          p.press('space')
          p.press('space')
     cv2.putText(img_arr,str(count), bottomLeftCornerOfText, font, fontScale,fontColor, lineType)
     cv2.imshow('test1', np.array(img_arr))
     if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          break