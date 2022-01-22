import qrcode

def genarateQRCode(words):
    generateQR_Code = qrcode.make("words")
    generateQR_Code.save(words + ".jpg")


if __name__ == '__main__':
    words = input()
    generateQR_Code(words)

