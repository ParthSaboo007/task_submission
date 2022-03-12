import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img1 = cv2.imread('test_img.png')

capture1 = cv2.VideoCapture(0)
capture1.set(3,1080) # capture id for width is 3
capture1.set(4,640) # capture id for height

while True:
    success,img1 = capture1.read()
    for barcode in decode(img1):
        #print(barcode.data)
        data_saved = barcode.data.decode('utf-8')
        print(data_saved)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img1,[pts],True,(255,1,255),5) # pline thikness=5
# till here qrcode code is detected but no bounding boxes visible

        # displaying text on barcode
        pts1 = barcode.rect
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(img1, data_saved,(pts1[0] + 6, pts1[1] - 6), font, 2.0, (0,0,255), 4)

        #saving the ddecoded data into file
        with open("barcode_results.txt",mode='a') as file:
            file.write("Decoded data:" + data_saved+"\n")

    cv2.imshow('Result',img1)
    cv2.waitKey(1)

#code1 = decode(img1)
#print(code1)  # provides decoded link, rectangle dimesions, polygon(tilted rectangle) coordinates

# function for detecting multiple barcodes



