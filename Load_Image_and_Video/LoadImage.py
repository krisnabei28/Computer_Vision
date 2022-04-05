import cv2 as cv

loadImage = cv.imread('/home/krisnabei/Documents/Dokumen_Krisna/DeepLearning/Code/Image/openCV.png')
loadImage = cv.resize(loadImage, (720, 620))

cv.imshow('OpencCV Python - Image', loadImage)
cv.waitKey(0)

# Tutup semua jendela yang terbuka
cv.destroyAllWindows()