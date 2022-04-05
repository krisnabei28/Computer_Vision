import cv2
 
image1 = cv2.imread('/home/krisnabei/Documents/Dokumen_Krisna/DeepLearning/Code/ImageDataSet/Picture04.jpg')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)

status = cv2.imwrite('/home/krisnabei/Documents/Dokumen_Krisna/DeepLearning/Code/ImageDataSet/Output.jpg',thresh1)


cv2.imshow('Original', image1)
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
print("Image written to file-system :",status)
   
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()