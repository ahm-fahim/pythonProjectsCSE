from tkinter import *
from time import strftime

def time():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    day_string = strftime("%A")
    day_label.config(text=day_string)
    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    window.after(1000, time)

window = Tk()
window.title("Clock")

time_label = Label(window, font=("arial", 50), fg="green", )
time_label.pack(anchor="center")
day_label = Label(window, font=("arial", 30), fg="orange", )
day_label.pack(anchor="center")
date_label = Label(window, font=("arial", 30), fg="black", )
date_label.pack(anchor="center")

time()
window.mainloop()
