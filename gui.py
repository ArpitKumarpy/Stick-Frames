from customtkinter import *
import tkinter as tk
from tkinter import PhotoImage

app = CTk()
app.geometry("1000x500")
bg_image = PhotoImage(file="ff.png")
bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)



btn1 = CTkButton(app, text="Live")

btn1.place(relx=0, rely=0,  x=200,y=205,)
btn1.configure(width=150, height=35)
btn2 = CTkButton(app, text="Stop Tracking")
btn2.place(relx=0, rely=0, x=200, y=250, )
btn2.configure(width=150, height=35)
btn3= CTkButton(app, text="Upload")
btn3.place(relx=0, rely=0, x=200, y=295)
btn3.configure(width=150, height=35)
app.title("Motion Tracking")
heading_label = CTkLabel(app, text="STICK FRAMES", bg_color="black",font=("Bodoni FLF", 34, "bold"))
heading_label.place(relx=0.5, rely=0.1, anchor="center")




app.mainloop()
