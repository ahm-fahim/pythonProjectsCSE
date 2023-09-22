import qrcode
import tkinter as tk
from tkinter import Entry, Button, Label, Canvas
from PIL import ImageTk

def generate_qr_code():
    data = data_entry.get()
    color = color_entry.get()
    file_name = file_name_entry.get()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill_color=color, back_color="white")

    # Save the QR code image to a file
    img.save(file_name + ".png")

    # Display the QR code image on the GUI
    qr_image = ImageTk.PhotoImage(file=file_name + ".png")
    qr_canvas.create_image(10, 10, anchor=tk.NW, image=qr_image)
    qr_canvas.image = qr_image

# Create the main application window
app = tk.Tk()
app.title("QR Code Generator")

# Create input fields and labels
data_label = Label(app, text="Input for QR code:")
data_label.pack()
data_entry = Entry(app)
data_entry.pack()

color_label = Label(app, text="Color:")
color_label.pack()
color_entry = Entry(app)
color_entry.pack()

file_name_label = Label(app, text="File name:")
file_name_label.pack()
file_name_entry = Entry(app)
file_name_entry.pack()

# Create a button to generate the QR code
generate_button = Button(app,bg="#21ad67",padx=10, pady=5,bd=5,relief=tk.RAISED, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create a canvas to display the QR code image
qr_canvas = Canvas(app, width=300, height=300)
qr_canvas.pack()

# Start the GUI main loop
app.mainloop()
