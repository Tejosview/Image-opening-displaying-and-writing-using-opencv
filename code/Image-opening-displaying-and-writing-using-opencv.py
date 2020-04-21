import cv2

## ImageOpen

original=cv2.imread("../image/logo.png")

## ImageDisplay
cv2.imshow("test-image",original)    
cv2.waitKey(0)

## ImageWriting
cv2.imwrite("../Generated/written-image.png",original)