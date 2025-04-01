import cv2
import pickle
try:
    with open('/Users/apple/Downloads/Azoca/CarParkingManagement/CarParkProject/CarParkPos.pkl', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


# img = cv2.imread('/Users/apple/Downloads/Azoca/untitled folder/CarParkProject/carParkImg.png')
# cv2.rectangle(img, (50, 90), (157, 138 ), (0,255,0), 2)
width, height = 107, 48


def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    with open('/Users/apple/Downloads/Azoca/CarParkingManagement/CarParkProject/CarParkPos.pkl', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('/Users/apple/Downloads/Azoca/CarParkingManagement/CarParkProject/carParkImg.png')

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width,pos[1]+height), (0,255,0), 2)

    cv2.imshow('img', img)
    cv2.setMouseCallback("img",mouseClick)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
