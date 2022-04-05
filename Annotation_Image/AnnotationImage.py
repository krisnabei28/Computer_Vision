import cv2 as cv

loadImage = cv.imread('/home/krisnabei/Documents/Dokumen_Krisna/DeepLearning/Code/ImageDataSet/sample.jpg')

#Copy Image
lineImage = loadImage.copy()
circleImage = loadImage.copy()
rectangleImage = loadImage.copy()
imageText = loadImage.copy()

#Draw line in image
pointA = (200,80)
pointB = (500,80)
cv.line(lineImage, pointA, pointB, (0, 0, 255), thickness=3)

#Draw circle in image
circleCenter = (415,190)
radius = 150
cv.circle(circleImage, circleCenter, radius, (0, 0, 255), thickness=3, lineType=cv.LINE_AA)

#Draw retangle in image
startA = (250,80)
endA = (550,280)
cv.rectangle(rectangleImage, startA, endA, (0, 0, 255), thickness= 3, lineType=cv.LINE_8)

#Input text in image
text = "I am a dog !!"
org = (25,50) #Position text in image
cv.putText(imageText, text, org, fontFace = cv.FONT_HERSHEY_SIMPLEX, fontScale = 1.5, color = (0,0,255), thickness=2)

#Show image
cv.imshow("Original image", loadImage)
cv.imshow("Line image", lineImage)
cv.imshow("Circle image", circleImage)
cv.imshow("Rectangle Image", rectangleImage)
cv.imshow("Text in Image", imageText)
cv.waitKey()
cv.destroyAllWindows()