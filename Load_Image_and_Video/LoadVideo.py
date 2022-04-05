import cv2 as cv

loadVideo = cv.VideoCapture('/home/krisnabei/Documents/Dokumen_Krisna/DeepLearning/Code/ImageDataSet/cat.mp4')

while True:
    isTrue, vid = loadVideo.read()
    cv.imshow("Video", vid)
    if cv.waitKey(10) & 0xFF ==ord('q'):
        break