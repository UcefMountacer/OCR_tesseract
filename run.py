import cv2 
import pytesseract

img = cv2.imread('data/page.png')

# Adding custom options
# custom_config = r'--oem 3 --psm 6'
# text = pytesseract.image_to_string(img, config=custom_config)

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)


cv2.imwrite('output.png', img)
print('done')