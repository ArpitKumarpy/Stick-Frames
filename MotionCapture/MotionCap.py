import cv2
from cvzone.PoseModule import PoseDetector
from cvzone.HandTrackingModule import HandDetector

#webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = PoseDetector() 
Hdetector = HandDetector(maxHands=3, detectionCon=0.8)
posList = []
RHList = []
LHList =[]
while True:
    success, img = cap.read()
    #success, img1 = cap.read()
    img= detector.findPose(img)

    #body landmarks 33
    lmList, bboxInfo = detector.findPosition(img)

    #hand landmarks 21
    hands, handimg = Hdetector.findHands(img)

    #print(hands)
    if bboxInfo:
        lmString = ''
        #print(lmList)
        for lm in lmList:
            lmString += f'{lm[0]},{img.shape[0]-lm[1]},{lm[2]},'
        posList.append(lmString)

    if hands:
        Lstring = ''
        Rstring = ''
        HmList= hands[0]['lmList']
        if hands[0]['type'] == 'Right' :
            for hs in HmList:
                Rstring += f'{hs[0]}, {img.shape[0]-hs[1]},{lm[2]},'
            RHList.append(Rstring)
        if hands[0]['type'] == 'Left' :
            for hs in HmList:
                Lstring += f'{hs[0]}, {img.shape[0]-hs[1]},{lm[2]},'
            LHList.append(Lstring)
        #print(HmList)


        
    #print(len(posList))
    #print(hstring)
    cv2.imshow("image",img)
    key = cv2.waitKey(1)

    if key==ord('s'):
        with open("MotionCaptureUnity/Assets/RightHandAnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in RHList])
        with open("MotionCaptureUnity/Assets/LeftHandAnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in LHList])
        with open("MotionCaptureUnity/Assets/AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList])
        #print(type(lmList)) 
        break