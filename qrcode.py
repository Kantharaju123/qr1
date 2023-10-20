import qrcode


url = input("Enter the URL to convert to a QR code: ")


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  
    border=4 


qr.add_data(url)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.save("qr_code.png")


img.show()