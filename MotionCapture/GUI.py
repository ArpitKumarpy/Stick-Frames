from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
from cvzone.PoseModule import PoseDetector
from cvzone.HandTrackingModule import HandDetector

#webcam

from tkinter import PhotoImage

app = CTk()
app.geometry("1000x500")
bg_image = PhotoImage(file="MotionCapture/ff.png")
bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
posList = []
RHList = []
LHList =[]

def Live_Track():
    cap = cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)

    detector = PoseDetector() 
    Hdetector = HandDetector(maxHands=3, detectionCon=0.8)
    global posList
    global RHList 
    global LHList 
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

def Upload():
    file_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

    if file_path:
            # You can perform further actions with the selected file path (e.g., upload to a server, process the video, etc.)
        cap = cv2.VideoCapture(file_path)

    cap.set(3,1280)
    cap.set(4,720)

    detector = PoseDetector() 
    Hdetector = HandDetector(maxHands=3, detectionCon=0.8)
    global posList
    global RHList 
    global LHList 
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


def Stop_Track():
    global posList
    global RHList 
    global LHList 
    with open("MotionCaptureUnity/Assets/RightHandAnimationFile.txt", 'w') as f:
        f.writelines(["%s\n" % item for item in RHList])
    with open("MotionCaptureUnity/Assets/LeftHandAnimationFile.txt", 'w') as f:
        f.writelines(["%s\n" % item for item in LHList])
    with open("MotionCaptureUnity/Assets/AnimationFile.txt", 'w') as f:
        f.writelines(["%s\n" % item for item in posList])
        #print(type(lmList)) 




btn1 = CTkButton(app, text="Live", command= Live_Track)
btn1.place(relx=0, rely=0,  x=200,y=205,)
btn1.configure(width=150, height=35)
btn2 = CTkButton(app, text="Stop Tracking", command= Stop_Track)
btn2.place(relx=0, rely=0, x=200, y=250, )
btn2.configure(width=150, height=35)
btn3= CTkButton(app, text="Upload", command= Upload)
btn3.place(relx=0, rely=0, x=200, y=295)
btn3.configure(width=150, height=35)
app.title("Motion Tracking")
heading_label = CTkLabel(app, text="STICK FRAMES", bg_color="black",font=("Bodoni FLF", 34, "bold"))
heading_label.place(relx=0.5, rely=0.1, anchor="center")




app.mainloop()