import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.title('Clock')

label = tk.Label(root, font=('arial', 100, 'bold'), background='orange', foreground='white')
label.pack(anchor='center')

time()
root.mainloop()
