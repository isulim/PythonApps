import cv2.cv2 as cv2

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(10)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
