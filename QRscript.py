import qrcode
from cv2 import imread, QRCodeDetector
from IPython.display import Image


def qrgeneretor(text, filename="temp.png", color="white"):
    qrObject = qrcode.QRCode()
    qrObject.add_data(text)
    qrObject.make()
    image = qrObject.make_image(back_color=color)
    name = filename if filename == "temp.png" else f"{filename}.png"
    image.save(filename if filename == "temp.png" else f"{filename}.png")
    return name


def decoder(filepath):
    qr = imread(filepath)
    return QRCodeDetector().detectAndDecode(qr)[0]
