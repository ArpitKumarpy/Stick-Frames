import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
from cvzone.PoseModule import PoseDetector

class VideoUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Uploader")

        # Create and pack widgets
        self.label1 = tk.Label(root, text="Select a video file:")
        self.label1.pack(pady=10)

        self.upload_button = tk.Button(root, text="Upload Video", command=self.upload_video)
        self.upload_button.pack(pady=10)
        
        self.label2 = tk.Label(root, text="Live track from camera")
        self.label2.pack(pady=10)

        self.camera_button = tk.Button(root, text="Live Track", command=self.camera_track)
        self.camera_button.pack(pady=10)


    def upload_video(self):
        file_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

        if file_path:
            # You can perform further actions with the selected file path (e.g., upload to a server, process the video, etc.)
            cap = cv2.VideoCapture(file_path)

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
                print(posList) 
                cv2.imshow("image",img)
                key = cv2.waitKey(1)

                if key==ord('s'):
                    with open("AnimationFile.txt", 'w') as f:
                        f.writelines(["%s\n" % item for item in posList]) 
                if cv2.waitKey(1) == ord('q'):
                               break
        
    def camera_track(self):
            # You can perform further actions with the selected file path (e.g., upload to a server, process the video, etc.)
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
                print(posList) 
                cv2.imshow("image",img)
                key = cv2.waitKey(1)

                if key==ord('s'):
                    with open("AnimationFile.txt", 'w') as f:
                        f.writelines(["%s\n" % item for item in posList]) 
                if cv2.waitKey(1) == ord('q'):
                               break              

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    app = VideoUploaderApp(root)
    root.mainloop()

'''def convert(text="type", src="en", dest="fr"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text


def word(text_get=None):
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    text_get = convert(text=msg, src=s, dest=d)
    dest_text.delete(1.0, END)
    dest_text.insert(END, text_get)


root = Tk()
root.title("Translator")
root.geometry("500x800")
root.overrideredirect(1)
root.wm_attributes("-transparentcolor", "grey") 

def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

#photo side bar

frame_photo= PhotoImage(file='background.png')
frame_label= Label(root, border=0,bg="grey", image=frame_photo)
frame_label.pack(fill =BOTH, expand= True)

frame_label.bind("<B1-Motion>", move_app)

exit_photo= PhotoImage(file="x.png")
exit_label= Label(root, border=0, bg='grey')
exit_label.place(x=186,y=-386)


lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"), bg="white")
lab_txt.place(x=100, y=120, height=100, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"))
lab_txt.place(x=100, y=210, height=30, width=300)

Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=240, height=150, width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, values=list_text)
comb_sor.place(x=10, y=390, height=50, width=150)
comb_sor.set("FROM")

button = Button(frame, text="Translate", relief=RAISED, command=word)
button.place(x=180, y=390, height=50, width=150)

comb_dest = ttk.Combobox(frame, values=list_text)
comb_dest.place(x=330, y=390, height=50, width=150)
comb_dest.set("TO")

lab_txt = Label(root, text="Trans Text", font=("Time New Roman", 30, "bold"))
lab_txt.place(x=100, y=450, height=50, width=300)

dest_text = Text(frame, font=("Time New Roman", 20, "bold"))
dest_text.place(x=10, y=460, height=150, width=480)


 
root.mainloop()'''