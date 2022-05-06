import sys
import cv2


# Code from https://morioh.com/p/29f7e4c5f900


def scan(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    return data


if __name__ == "__main__":
    print(scan(sys.argv[1]))

