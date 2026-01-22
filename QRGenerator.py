def generate_qr_code():
    import qrcode
    import os

    url = input("Enter the URL: ").strip()
    file_name = "qrcode.png"

    i = 1
    while os.path.exists(file_name):
        file_name = "qrcode(" + str(i) + ").png"
        i += 1

    qr = qrcode.QRCode()
    qr.add_data(url)

    img = qr.make_image()
    img.save(file_name)
    print("QR Code was generated!")
while True:
    generate_qr_code()
