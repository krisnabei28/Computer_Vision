import cv2 as cv

image = cv.imread('../Image02.jpg')
image= cv.resize(image,(1080,720))
img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
img_gray= cv.resize(img_gray,(1080,720))
ret, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)

image_copy = image.copy()
image_copy= cv.resize(image_copy,(1080,720))
cv.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv.LINE_AA)

cv.imshow('Original', image)
cv.imshow('Result', image_copy)
cv.waitKey(0)
cv.destroyAllWindows()