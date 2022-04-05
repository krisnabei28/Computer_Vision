import cv2 as cv
import numpy as np
from skimage.exposure import rescale_intensity

kernelImage = np.array([[0, -1,  0],
                   		[-1,  5, -1],
                    	[0, -1,  0]])
						
def convolution(image, kernel):
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]
	pad = (kW - 1) // 2
	image = cv.copyMakeBorder(image, pad, pad, pad, pad,cv.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi * kernel).sum()
			output[y - pad, x - pad] = k
	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")
	return output

smallBlur = np.ones((11, 11), dtype="float") * (1.0 / (11 * 11))

image = cv.imread('../micky.jpg')
image = cv.resize(image,(420,420))
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
convoleOutput = convolution(gray, smallBlur)
opencvOutput = cv.filter2D(gray, -1, smallBlur)
sharp_img = cv.filter2D(src=gray, ddepth=-1, kernel=kernelImage)
grayCanny = cv.Canny(image,100,100)
bicubic_img = cv.resize(gray,None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC)
bicubic_img = cv.resize(bicubic_img,(420,420))

cv.imshow("Original", gray)
cv.imshow("Blur - Image", convoleOutput)
cv.imshow('Sharpen - Image', sharp_img)
cv.imshow('Edge Detection - Image', grayCanny)
cv.imshow('Interpolation - Image', bicubic_img)
cv.waitKey(0)
cv.destroyAllWindows()