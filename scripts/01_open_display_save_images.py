import time
import cv2

# Read image
import_path = r'../resources/test-image.jpg'
image = cv2.imread(import_path)

# Display image for 2s
cv2.imshow('Zhu Jiang New Town, Guangzhou, Guangdong, China', image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# Save image to output folder + use timestamp for filename
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)

export_path = ('./processed/processed_image-' + timestamp + '.jpg')

cv2.imwrite(export_path, image)
print('Image was saved!')