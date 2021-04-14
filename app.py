from tkinter import *
from PIL import Image, ImageTk
import cv2

mainWindow = None
sourceImageCV2 = None
grayImageCV2 = None
greenBinaryImageCV2 = None
yellowBinaryImageCV2 = None

scaleLowerYellowSetting = None
scaleUpperYellowSetting = None

scaleLowerAllSetting = None
scaleUpperAllSetting = None

scaleLowerAreaSetting = None
scaleUpperAreaSetting = None

lblResultGreen = None
lblResultYellow = None
lblResultAll = None

def init():
    global mainWindow
    mainWindow = Tk();
    mainWindow.title('Mango Detection')
    mainWindow.resizable(0, 0)
    mainWindow.geometry('1800x966')

    #
    # Controls
    #

    #
    # Yellow setting
    #
    lbl = Label(mainWindow, text = "Yellow Setting")
    lbl.config(font = ("Courier", 18))
    lbl.place(x=1300, y=10)

    # Lower
    lbl = Label(mainWindow, text = "Lower")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=1300, y=50)

    global scaleLowerYellowSetting
    lowerYellowSettingValue = DoubleVar() 
    scaleLowerYellowSetting = Scale(mainWindow, variable = lowerYellowSettingValue, from_ = 0, to = 255, orient = HORIZONTAL, length=480)
    scaleLowerYellowSetting.place(x=1300, y=65)
    scaleLowerYellowSetting.set(200)

    # Upper
    lbl = Label(mainWindow, text = "Upper")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=1300, y=120)

    global scaleUpperYellowSetting
    upperYellowSettingValue = DoubleVar() 
    scaleUpperYellowSetting = Scale(mainWindow, variable = upperYellowSettingValue, from_ = 0, to = 255, orient = HORIZONTAL, length=480)
    scaleUpperYellowSetting.place(x=1300, y=140)
    scaleUpperYellowSetting.set(255)

    #
    # All setting
    #
    lbl = Label(mainWindow, text = "All Setting")
    lbl.config(font = ("Courier", 18))
    lbl.place(x=1300, y=200)

    # Lower
    lbl = Label(mainWindow, text = "Lower")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=1300, y=250)

    global scaleLowerAllSetting
    lowerAllSettingValue = DoubleVar() 
    scaleLowerAllSetting = Scale(mainWindow, variable = lowerAllSettingValue, from_ = 0, to = 255, orient = HORIZONTAL, length=480)
    scaleLowerAllSetting.place(x=1300, y=265)
    scaleLowerAllSetting.set(100)

    # Upper
    lbl = Label(mainWindow, text = "Upper")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=1300, y=320)

    global scaleUpperAllSetting
    upperAllSettingValue = DoubleVar() 
    scaleUpperAllSetting = Scale(mainWindow, variable = upperAllSettingValue, from_ = 0, to = 255, orient = HORIZONTAL, length=480)
    scaleUpperAllSetting.place(x=1300, y=340)
    scaleUpperAllSetting.set(255)

    #
    # Area setting
    #
    lbl = Label(mainWindow, text = "Area Setting")
    lbl.config(font = ("Courier", 18))
    lbl.place(x=1300, y=400)

    # Lower
    lbl = Label(mainWindow, text = "Lower")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=1300, y=450)

    global scaleLowerAreaSetting
    lowerAreaSettingValue = DoubleVar() 
    scaleLowerAreaSetting = Scale(mainWindow, variable = lowerAreaSettingValue, from_ = 0, to = 50000, orient = HORIZONTAL, length=480)
    scaleLowerAreaSetting.place(x=1300, y=470)
    scaleLowerAreaSetting.set(5000)

    # Upper
    lbl = Label(mainWindow, text = "Upper")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=1300, y=530)

    global scaleUpperAreaSetting
    upperAreaSettingValue = DoubleVar() 
    scaleUpperAreaSetting = Scale(mainWindow, variable = upperAreaSettingValue, from_ = 0, to = 50000, orient = HORIZONTAL, length=480)
    scaleUpperAreaSetting.place(x=1300, y=550)
    scaleUpperAreaSetting.set(30000)

    #
    # Result
    #
    lbl = Label(mainWindow, text = "Result")
    lbl.config(font = ("Courier", 18))
    lbl.place(x=1300, y=650)

    global lblResultGreen
    lblResultGreen = Label(mainWindow, text = "Green = ")
    lblResultGreen.config(font = ("Courier", 12))
    lblResultGreen.place(x=1300, y=690)

    global lblResultYellow
    lblResultYellow = Label(mainWindow, text = "Yellow = ")
    lblResultYellow.config(font = ("Courier", 12))
    lblResultYellow.place(x=1300, y=720)

    global lblResultAll
    lblResultAll = Label(mainWindow, text = "All = ")
    lblResultAll.config(font = ("Courier", 12))
    lblResultAll.place(x=1300, y=750)

    #
    # Button
    #

    button = None
    button = Button(mainWindow, text ="Process", command = process, width = 37, font = ("Courier", 16))
    button.place(x=1300, y=920)

def process():
    # Source
    global sourceImageCV2 
    #sourceImageCV2 = cv2.imread('640x480.png')
    video = cv2.VideoCapture(0)
    ret, sourceImageCV2 = video.read()

    sourceImageCV2 = cv2.blur(sourceImageCV2, (5,5))
    
    # Gray
    grayImageCV2 = cv2.cvtColor(sourceImageCV2, cv2.COLOR_BGR2GRAY)
    grayImageData = cv2.cvtColor(grayImageCV2, cv2.COLOR_GRAY2BGR)
    grayImageData = Image.fromarray(grayImageData)
    grayImageData = ImageTk.PhotoImage(grayImageData)
    grayImage = Label(mainWindow, image=grayImageData)
    grayImage.image = grayImageData
    grayImage.place(x=642, y=0)

    # All binary
    ret, allBinaryImageCV2 = cv2.threshold(grayImageCV2, scaleLowerAllSetting.get(), scaleUpperAllSetting.get(), cv2.THRESH_BINARY)
    # find contours in the image
    allContours = cv2.findContours(allBinaryImageCV2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # filter by area
    allCnts = []
    for cnt in allContours:
        # print(cv.contourArea(cnt))
        if scaleLowerAreaSetting.get() < cv2.contourArea(cnt) < scaleUpperAreaSetting.get():
            allCnts.append(cnt)
    countAll = len(allCnts)
    lblResultAll.configure(text = ("All = " + str(countAll)))
    print("All = ", countAll)
    #
    allBinaryImageData = cv2.cvtColor(allBinaryImageCV2, cv2.COLOR_GRAY2RGB)
    allBinaryImageData = Image.fromarray(allBinaryImageData)
    allBinaryImageData = ImageTk.PhotoImage(allBinaryImageData)
    allBinaryImage = Label(mainWindow, image=allBinaryImageData)
    allBinaryImage.image = allBinaryImageData
    allBinaryImage.place(x=642, y=482)

    # Yellow binary
    ret, yellowBinaryImageCV2 = cv2.threshold(grayImageCV2, scaleLowerYellowSetting.get(), scaleUpperYellowSetting.get(), cv2.THRESH_BINARY)
    # find contours in the image
    yellowContours = cv2.findContours(yellowBinaryImageCV2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # filter by area
    yellowCnts = []
    for cnt in yellowContours:
        # print(cv.contourArea(cnt))
        if scaleLowerAreaSetting.get() < cv2.contourArea(cnt) < scaleUpperAreaSetting.get():
            yellowCnts.append(cnt)
    countYellow = len(yellowCnts)
    lblResultYellow.configure(text = ("Yellow = " + str(countYellow) + ", % = " + str("{:.2f}".format((countYellow * 100) / countAll))))
    print("Yellow = ", countYellow)
    #
    yellowBinaryImageData = cv2.cvtColor(yellowBinaryImageCV2, cv2.COLOR_GRAY2RGB)
    yellowBinaryImageData = Image.fromarray(yellowBinaryImageData)
    yellowBinaryImageData = ImageTk.PhotoImage(yellowBinaryImageData)
    yellowBinaryImage = Label(mainWindow, image=yellowBinaryImageData)
    yellowBinaryImage.image = yellowBinaryImageData
    yellowBinaryImage.place(x=0, y=482)

    # Green
    lblResultGreen.configure(text = ("Green = " + str(countAll - countYellow) + ", % = " + str("{:.2f}".format(((countAll - countYellow) * 100) / countAll))))
    print("Green = ", countAll - countYellow)
    print("-------------------")

    # Highlight aread
    cv2.drawContours(sourceImageCV2, yellowCnts, -1, (255,255,0), 3)
    cv2.drawContours(sourceImageCV2, allCnts, -1, (255,0,0), 3)

    # Source
    sourceImageData = cv2.cvtColor(sourceImageCV2, cv2.COLOR_BGR2RGB)
    sourceImageData = Image.fromarray(sourceImageData)
    sourceImageData = ImageTk.PhotoImage(sourceImageData)
    sourceImage = Label(mainWindow, image=sourceImageData)
    sourceImage.image = sourceImageData
    sourceImage.place(x=0, y=0)

# Main entry point.
init()
process()
mainWindow.mainloop()