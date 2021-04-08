import cv2 as cv
import numpy as np

#
sourceImage = cv.imread('demo.png')
grayImage = cv.cvtColor(sourceImage, cv.COLOR_BGR2GRAY)
ret, binaryImage = cv.threshold(grayImage, 100, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

#
contours = cv.findContours(binaryImage, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[-2]
# print(contours)

# filter by area
s1 = 5000
s2 = 30000
xcnts = []
for cnt in contours:
    # print(cv.contourArea(cnt))
    if s1 < cv.contourArea(cnt) < s2:
        xcnts.append(cnt)

# for cnt in xcnts:
#     print(cv.contourArea(cnt))

print("Amount of mongo: {}" . format(len(xcnts)))

# draw
cv.drawContours(sourceImage, xcnts, -1, (0,255,0), 3)

#
cv.imshow('source', sourceImage) 
# cv.imshow('gray', grayImage) 
cv.imshow('binary', binaryImage) 

# #
# def mouseRGB(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN: #checks mouse left button down condition
#         value = grayImage[y, x]
#         print("GValue: ", value)
#         print("X: ", x, "Y: ", y)
#         print("-------------------------")

# # cv.namedWindow('gray')
# cv.setMouseCallback('gray',mouseRGB)

#
cv.waitKey(0)
cv.destroyAllWindows()
