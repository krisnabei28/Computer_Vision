import cv2 as cv

loadImage = cv.imread('../flag.png')
loadImage = cv.resize(loadImage,(720, 450))
copyImage = loadImage.copy()
for i in range(0, copyImage.shape[0]):
    for j in range(0, copyImage.shape[1]):
        if copyImage[i,j][0] != 255 and copyImage[i,j][1] != 255 and copyImage[i,j][2] == 255:
            copyImage[i][j] = (255,255,255)
        elif copyImage[i,j][0] != 0 and copyImage[i,j][1] != 0 and copyImage[i,j][2] == 255:
            copyImage[i][j] = (0,0,255)

statuss = cv.imwrite('D:/Materi_Kuliah/Semester 6/DeepLearning/Code/ImageDataSet/flag02.png',copyImage)
cv.imshow("Original", loadImage)
cv.imshow("Modified Image", copyImage)
cv.waitKey(0)
cv.destroyAllWindows()