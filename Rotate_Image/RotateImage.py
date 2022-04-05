import cv2 as cv

loadImage = cv.imread('/home/krisnabei/Documents/Dokumen_Krisna/DeepLearning/Code/ImageDataSet/Picture10.jpg')

def rotateImage(image, angle, rotatePoint=None):
    (heightImg, widthImg) = loadImage.shape[:2]
    
    if rotatePoint is None:
        rotatePoint = (widthImg//2, heightImg//2)
    
    rotateMat = cv.getRotationMatrix2D(rotatePoint, angle, 1.0)
    dimension = (widthImg, heightImg)
    
    return cv.warpAffine(image,rotateMat, dimension,borderValue=(255,255,255))

rotatedImg = rotateImage(loadImage,-45)
cv.imshow("Original Image", loadImage)
cv.imshow("Rotate Image", rotatedImg)

cv.waitKey(0)

# Tutup semua jendela yang terbuka
cv.destroyAllWindows()
