import cv2.cv2 as cv2

firstFrame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Assign the first frame as reference
    if firstFrame is None:
        firstFrame = gray
        continue

    # Compare first frame to current
    deltaFrame = cv2.absdiff(firstFrame, gray)

    # Create threshold image with over 30 colored as white
    threshFrame = cv2.threshold(deltaFrame, 30, 255, cv2.THRESH_BINARY)[1]

    # Smooth out areas
    threshFrame = cv2.dilate(threshFrame, None, iterations=2)

    # Find external contours in threshold frame
    (contours, _) = cv2.findContours(threshFrame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangle in current color frame for contours at least
    # 100 pixels area
    for contour in contours:
        if cv2.contourArea(contour) < 200:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Gray Frame", frame)
    cv2.imshow("Delta Frame", threshFrame)

    key = cv2.waitKey(50)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
