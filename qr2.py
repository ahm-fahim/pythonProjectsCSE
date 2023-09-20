import qrcode
import tkinter as tk
from tkinter import simpledialog, filedialog

# Create a tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Get input from the user using tkinter's simpledialog
data = simpledialog.askstring("Input", "Input for creating QR code:")

# Get the color input
color = simpledialog.askstring("Input", "Color for QR code:")

# Get the file name using tkinter's filedialog
file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

if data and color and file_name:
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

    # Save the QR code image to the selected file
    img.save(file_name)
