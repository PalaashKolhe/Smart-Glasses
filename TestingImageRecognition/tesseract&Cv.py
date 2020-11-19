# ********************************************************************************************************
# IMPORTS
import cv2    # pip install opencv-python
import pytesseract

# Tutorial by https://www.youtube.com/watch?v=6DjFscX4I_c

# ********************************************************************************************************
# WORKING CODE
# creating connection with pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/.local/lib/python3.8/site-packages'

# settings regarding the image
img = cv2.imread('img/image4.jpeg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# printing out the text found within the image
text = pytesseract.image_to_string(img)
print(text)
# print(boxes)   # char x y width height

### CHARACTER RECOGNITION
# displaying the boxes
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# print(boxes)
#
# for box in boxes.splitlines():
#     # print(box)
#     box = box.split(" ")
#     # print(box)
#     x, y, width, height = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(img, (x, hImg-y), (width, hImg - height), (0, 0, 255), 1)
#     cv2.putText(img, box[0], (x, hImg-y+15), cv2.FONT_ITALIC, 0.5, (50, 50, 255), 1)

### WORD RECOGNITION
# displaying the boxes
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)
print(boxes)

for i, box in enumerate(boxes.splitlines()):
    if i != 0:
        box = box.split()
        if len(box) == 12:
            x, y, width, height = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (width + x, height + y), (0, 0, 255), 1)
            cv2.putText(img, box[11], (x, y-5), cv2.FONT_ITALIC, 0.5, (50, 50, 255), 1)

### CHARACTER RECOGNITION 2 FOR DIGITS - EDITING CONFIG (i don't like this)
# displaying the boxes
# hImg, wImg, _ = img.shape
# config = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img, config=config)
# print(boxes)
#
# for box in boxes.splitlines():
#     # print(box)
#     box = box.split(" ")
#     # print(box)
#     x, y, width, height = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(img, (x, hImg-y), (width, hImg - height), (0, 0, 255), 1)
#     cv2.putText(img, box[0], (x, hImg-y+25), cv2.FONT_ITALIC, 0.5, (50, 50, 255), 1)

# displays the image
cv2.imshow('Result', img)
cv2.waitKey(0)


