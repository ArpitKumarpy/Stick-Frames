import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)

detector = PoseDetector()
posList = []
while True:
    success, img = cap.read()
    img= detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)
   
    print(bboxInfo)
    if bboxInfo:
        lmString = ''
        for lm in lmList:
            lmString += f'{lm[0]},{img.shape[0]-lm[1]},{lm[2]},'

        posList.append(lmString)
    print(len(posList)) 
    cv2.imshow("image",img)
    key = cv2.waitKey(1)

    if key==ord('s'):
        with open("MotionCaptureUnity\Assets\AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList]) 
        break
