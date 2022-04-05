
import cv2 as cv
import numpy as np
  
image = cv.imread('../Image12.jpg')

height, width = image.shape[:2]
  
quarter_height, quarter_width = height / 4, width / 4
  
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

img_translation = cv.warpAffine(image, T, (width, height))
  
cv.imshow("Original image", image)
cv.imshow('Translation image', img_translation)
cv.waitKey()
  
cv.destroyAllWindows()