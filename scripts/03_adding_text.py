import cv2

image_path = r'resources/test-image.jpg'
image = cv2.imread(image_path)


# Add Text
watermark = "Hello World!"
coordinates = (50, 150)
font = cv2.QT_FONT_NORMAL
fontScale = 1
color = (255, 0, 0)
thickness = 2

img_watermarked = cv2.putText(image, watermark, coordinates, font, fontScale, color, thickness)
cv2.imshow('Zhu Jiang New Town, Guangzhou, Guangdong, China', img_watermarked)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# Add Line
start = (0, 0)
end = (715, 476)
color = (0, 0, 255)
thickness = 2

img_line = cv2.line(image, start, end, color, thickness)
cv2.imshow('Zhu Jiang New Town, Guangzhou, Guangdong, China', img_line)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# Draw Circle
center = (100, 100)
radius = 80
color = (255, 255, 255)
thickness = 2

img_line = cv2.circle(image, center, radius, color, thickness)
cv2.imshow('Zhu Jiang New Town, Guangzhou, Guangdong, China', img_line)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# Draw Rectangle
start = (280, 80)
end = (350, 350)
color = (0, 255, 0)
thickness = 2

img_line = cv2.rectangle(image, start, end, color, thickness)
cv2.imshow('Zhu Jiang New Town, Guangzhou, Guangdong, China', img_line)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# Draw Ellipse
center = (120, 100)
axesLength = (100, 50)
angle = 30
startAngle = 0
endAngle = 360
color = (0, 0, 255)
thickness = 2

img_line = cv2.ellipse(image, center, axesLength, angle, startAngle, endAngle, color, thickness)
cv2.imshow('Zhu Jiang New Town, Guangzhou, Guangdong, China', img_line)
cv2.waitKey(2000)
cv2.destroyAllWindows()