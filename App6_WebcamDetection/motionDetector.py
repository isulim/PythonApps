import cv2.cv2 as cv2
from pandas import DataFrame, read_csv
from datetime import datetime
from App6_WebcamDetection.plotting import PlotGraph

firstFrame = None
status_list = [0]
times = []
df = DataFrame(columns=["Start", "End"])
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
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
    (contours, _) = cv2.findContours(threshFrame.copy(), cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangle in current color frame for contours at least
    # 1000 pixels area
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    status_list.append(status)

    status_list = status_list[-2:]

    if status_list[-1] != status_list[-2]:
        times.append(datetime.now())

    cv2.imshow("Gray Frame", frame)
    cv2.imshow("Delta Frame", threshFrame)

    key = cv2.waitKey(100)

    if key == ord('q'):
        # Append time on exiting
        if status == 1:
            times.append(datetime.now())
        break

video.release()
cv2.destroyAllWindows()

# Iterate through recorded times with jump of 2
for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)
df.to_csv("Times.csv")

print(df.to_string())

# Plot graph with Bokeh
graph1 = PlotGraph(df, "graph1")
graph1.show()
