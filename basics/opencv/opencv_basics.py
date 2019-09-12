import cv2
import os

img = cv2.imread((os.path.dirname(os.path.abspath(__file__)) 
                    + "/" + "galaxy.jpg"), 0)

# print(img)
# print(img.shape)


resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
print(resized.shape)
# show image, title of window
cv2.imshow("Galaxy", resized)
cv2.imwrite(os.path.dirname(os.path.abspath(__file__)) 
                + "/" + "Galaxy_resized.jpg", resized)

# wait mseconds for window to close
cv2.waitKey(0)
cv2.destroyAllWindows()