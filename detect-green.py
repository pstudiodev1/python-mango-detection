import cv2 as cv
import numpy as np

# Load image
sourceImage = cv.imread('mix.png')

def findObjectByColorRange(source, lowerColor, upperColor):
    binaryImage = cv.inRange(sourceImage, lowerColor, upperColor)
    cv.imshow('filter', binaryImage) 
    # find contours in the image
    contours = cv.findContours(binaryImage, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[-2]
    # filter by area
    s1 = 500
    s2 = 30000
    xcnts = []
    for cnt in contours:
        print(cv.contourArea(cnt))
        if s1 < cv.contourArea(cnt) < s2:
            xcnts.append(cnt)
    cv.drawContours(sourceImage, xcnts, -1, (0,255,0), 3)
    cv.imshow('source', sourceImage) 
    return len(xcnts)

amount = findObjectByColorRange(
    sourceImage, 
    np.array([70, 90, 70]),
    np.array([120, 160, 100]),
)

print("Count = ", amount)

#
cv.waitKey(0)
cv.destroyAllWindows()
