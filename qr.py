import qrcode

data = input("Input for create QR code: ")
color = input("color: ")
fileName = input("File name : ")

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
img.save(fileName+".png")
