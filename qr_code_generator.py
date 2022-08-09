import qrcode

input_data = input("Insert your url: ")
file_name = input("Name your image: ")+ ".png"

qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=3)
qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save(file_name)

