import cv2 as cv
import numpy as np

# Load image
sourceImage = cv.imread('mix.png')

def findObjectByColorRange(source, lower, upper, isDrawAll):
    grayImage = cv.cvtColor(sourceImage, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', grayImage) 
    ret, binaryImage = cv.threshold(grayImage, lower, upper, cv.THRESH_BINARY_INV)
    cv.imshow('filter', binaryImage) 
    # find contours in the image
    contours = cv.findContours(binaryImage, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[-2]
    # filter by area
    s1 = 5000
    s2 = 30000
    xcnts = []
    for cnt in contours:
        # print(cv.contourArea(cnt))
        if s1 < cv.contourArea(cnt) < s2:
            xcnts.append(cnt)
    if isDrawAll:
        cv.drawContours(sourceImage, xcnts, -1, (0,255,0), 3)
        cv.imshow('source', sourceImage) 
    return len(xcnts)


amountAll = findObjectByColorRange(
    sourceImage, 
    100,
    255,
    False
)

amountOfYellow = findObjectByColorRange(
    sourceImage, 
    200,
    255,
    True
)

print("All = ", amountAll)
print("Yellow = ", amountOfYellow)
print("Green = ", amountAll - amountOfYellow)

#
cv.waitKey(0)
cv.destroyAllWindows()
