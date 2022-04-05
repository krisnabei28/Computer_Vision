import cv2 as cv

loadImage = cv.imread('../Image08.png')

imageResize = cv.resize(loadImage,(250,200))
imageCrop = loadImage[100:300,200:500]

print(loadImage.shape)
print(imageResize.shape)

cv.imshow("Orginal", loadImage)
cv.imshow("Resize", imageResize)
cv.imshow("Crop", imageCrop)

cv.waitKey(0)

# Tutup semua jendela yang terbuka
cv.destroyAllWindows()