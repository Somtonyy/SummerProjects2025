import qrcode
text = input("Enter the text or URL: ").strip()
filename = input("Enter the file name: ").strip()
qr = qrcode.QRCode(
    box_size=10,
    border=4,
)
qr.add_data(text)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f'QR code saved as {filename}')
