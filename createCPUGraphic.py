import cv2
import numpy as np
# create blank cv2 image with a clear background
img = np.zeros((512, 512, 3), np.uint8)

# draw a square on the image
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# show the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
