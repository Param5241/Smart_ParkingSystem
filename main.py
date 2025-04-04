import cv2
import pickle
import cvzone
import numpy as np

#video feed 
cap = cv2.VideoCapture('/Users/apple/Downloads/Azoca/CarParkingManagement/CarParkProject/carPark.mp4')

with open('/Users/apple/Downloads/Azoca/CarParkingManagement/CarParkProject/CarParkPos.pkl', 'rb') as f:
        posList = pickle.load(f)
width, height = 107, 48

def checkParkingSpace(imgPro):
    spaceCounter = 0
    for pos in posList:
        x,y = pos

        imgCrop = imgPro[y:y+height, x:x+width]
        # cv2.imshow(str(x*y), imgCrop)
        count = cv2.countNonZero(imgCrop)
        

        if count < 900:
            color = (0,255,0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0,0,255)
            thickness = 2
        # for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width,pos[1]+height),color, thickness)
        cvzone.putTextRect(img,str(count),(x,y+height-3),scale=1,thickness=1,offset=0,colorR=color)

    cvzone.putTextRect(img,f'Free :{spaceCounter}/{len(posList)}',(50,50),scale=3,thickness=5,offset=20,colorR=(0,200,0))
        
    

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) 
    ret, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)

    kernal = np.ones((3,3),np.uint8)
    imgDialate = cv2.dilate(imgMedian, kernal, iterations=1)


    checkParkingSpace(imgDialate )
    


    cv2.imshow('Parking', img)
    # cv2.imshow('Blur', imgBlur)
    # cv2.imshow('Threshold', imgThreshold)
    # cv2.imshow('Median', imgMedian)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
