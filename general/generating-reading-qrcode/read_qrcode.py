import cv2
import sys

filename = sys.argv[1]

# read the QRCODE image
#in case if QR code is not black/white it is better to convert it into grayscale
img = cv2.imread(filename, 0)# Zero means grayscale
img_origin = cv2.imread(filename)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox[0])#Cause bbox = [[[float, float]]], we need to convert fload into int and loop over the first element of array
    bbox1 = bbox.astype(int) #Float to Int conversion
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox1[0, [i][0]])
        point2 = tuple(bbox1[0, [(i+1) % n_lines][0]])
        cv2.line(img_origin, point1, point2, color=(255, 0, 0), thickness=2)


    # display the result
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("QR code not detected")
