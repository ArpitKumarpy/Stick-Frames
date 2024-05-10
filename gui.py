from customtkinter import *
import tkinter as tk

app = CTk()
app.geometry("700x600")


btn1 = CTkButton(app, text="Live")

btn1.place(relx=0, rely=0,  x=105,y=185,)

btn2 = CTkButton(app, text="Stop Tracking")
btn2.place(relx=.5, rely=.25, x=80, y=50)

btn3= CTkButton(app, text="UPload")
btn3.place(relx=0, rely=0, x=105, y=220)
app.title("Motion Tracking")
heading_label = CTkLabel(app, text="Stick Frames", font=("Helvetica", 34, "bold"))
heading_label.place(relx=0.5, rely=0.1, anchor="center")




app.mainloop()
