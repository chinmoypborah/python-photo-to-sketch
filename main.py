import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
if img_path.endswith(('.jpg', '.jpeg')): #Checks if the file is a valid jpg or jpeg file or not
    image = cv2.imread(img_path)
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (21,21),0)
    inverted = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, inverted, scale=256.0)
    cv2.imwrite("ifinal.png", sketch)
else:
    print("Not a valid image")
