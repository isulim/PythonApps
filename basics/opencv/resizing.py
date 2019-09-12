import cv2
import os

samplePath = (os.path.dirname(os.path.abspath(__file__))) + "/sample-images/"

for image in os.listdir(samplePath):

    source = cv2.imread((samplePath + str(image)), 1)
    
    resized = cv2.resize(source, (100, 100))

    cv2.imwrite((samplePath + "resized_" + str(image)), resized)
