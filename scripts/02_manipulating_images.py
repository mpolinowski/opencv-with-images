import time
import cv2

image_path = r'../resources/test-image.jpg'
image = cv2.imread(image_path)

t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)

# Display image resolution
print(image.shape)

# Convert image to different colour space
## RGB -> Monochrome
image_monochrome = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
export_path_monochrome = ('./processed/monochrome-' + timestamp + '.jpg')
cv2.imwrite(export_path_monochrome, image_monochrome)
print(image_monochrome.shape)
## RGB -> HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
export_path_colour = ('./processed/colour-' + timestamp + '.jpg')
cv2.imwrite(export_path_colour, image_hsv)
print(image_hsv.shape)

# Resize an image
img_resized = cv2.resize(image, (450, 450))
cv2.imshow('Zhu Jiang New Town, Guangzhou, Guangdong, China', img_resized)
cv2.waitKey(2000)
cv2.destroyAllWindows()