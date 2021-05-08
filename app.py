from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import threading

mainWindow = None

tabResult = None
tabControl = None
tabOriginal = None
tabGray = None
tabBinary = None
tabYellow = None

tabSettingYellow = None
tabSettingAll = None
tabSettingArea = None

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
    # mainWindow.resizable(0, 0)
    mainWindow.geometry('600x400')

    #
    # Controls
    #
    global tabControl
    global tabOriginal
    global tabGray
    global tabBinary
    global tabYellow
    global tabSettingYellow

    tabControl = ttk.Notebook(mainWindow)
    tabResult = ttk.Frame(tabControl)
    tabOriginal = ttk.Frame(tabControl)
    tabGray = ttk.Frame(tabControl)
    tabBinary = ttk.Frame(tabControl)
    tabYellow = ttk.Frame(tabControl)
    tabSettingYellow = ttk.Frame(tabControl)
    tabSettingAll = ttk.Frame(tabControl)
    tabSettingArea = ttk.Frame(tabControl)

    tabControl.add(tabResult, text ='Result')

    tabControl.add(tabOriginal, text ='Original')
    tabControl.add(tabGray, text ='Gray')
    tabControl.add(tabBinary, text ='Binary')
    tabControl.add(tabYellow, text ='Yellow')

    tabControl.add(tabSettingYellow, text ='Setting 1')
    tabControl.add(tabSettingAll, text ='Setting 2')
    tabControl.add(tabSettingArea, text ='Setting 3')

    tabControl.pack(expand = 1, fill ="both")

    #
    # Yellow setting
    #
    lbl = Label(tabSettingYellow, text = "Yellow Setting")
    lbl.config(font = ("Courier", 18))
    lbl.place(x=10, y=10)

    # # Lower
    lbl = Label(tabSettingYellow, text = "Lower")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=10, y=50)

    global scaleLowerYellowSetting
    lowerYellowSettingValue = DoubleVar() 
    scaleLowerYellowSetting = Scale(tabSettingYellow, variable = lowerYellowSettingValue, from_ = 0, to = 255, orient = HORIZONTAL, length=520)
    scaleLowerYellowSetting.place(x=10, y=65)
    scaleLowerYellowSetting.set(200)

    # Upper
    lbl = Label(tabSettingYellow, text = "Upper")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=10, y=120)

    global scaleUpperYellowSetting
    upperYellowSettingValue = DoubleVar() 
    scaleUpperYellowSetting = Scale(tabSettingYellow, variable = upperYellowSettingValue, from_ = 0, to = 255, orient = HORIZONTAL, length=520)
    scaleUpperYellowSetting.place(x=10, y=140)
    scaleUpperYellowSetting.set(255)

    #
    # Button
    #
    # buttonSaveYellowSetting = None
    # buttonSaveYellowSetting = Button(tabSettingYellow, text ="Save", command = process, font = ("Courier", 16))
    # buttonSaveYellowSetting.place(x=460, y=300)

    #
    # All setting
    #
    lbl = Label(tabSettingAll, text = "All Setting")
    lbl.config(font = ("Courier", 18))
    lbl.place(x=10, y=10)

    # Lower
    lbl = Label(tabSettingAll, text = "Lower")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=10, y=50)

    global scaleLowerAllSetting
    lowerAllSettingValue = DoubleVar() 
    scaleLowerAllSetting = Scale(tabSettingAll, variable = lowerAllSettingValue, from_ = 0, to = 255, orient = HORIZONTAL, length=520)
    scaleLowerAllSetting.place(x=10, y=65)
    scaleLowerAllSetting.set(100)

    # Upper
    lbl = Label(tabSettingAll, text = "Upper")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=10, y=120)

    global scaleUpperAllSetting
    upperAllSettingValue = DoubleVar() 
    scaleUpperAllSetting = Scale(tabSettingAll, variable = upperAllSettingValue, from_ = 0, to = 255, orient = HORIZONTAL, length=520)
    scaleUpperAllSetting.place(x=10, y=140)
    scaleUpperAllSetting.set(255)

    #
    # Button
    #
    # buttonAllSetting = None
    # buttonAllSetting = Button(tabSettingAll, text ="Save", command = process, font = ("Courier", 16))
    # buttonAllSetting.place(x=460, y=300)

    #
    # Area setting
    #
    lbl = Label(tabSettingArea, text = "Area Setting")
    lbl.config(font = ("Courier", 18))
    lbl.place(x=10, y=10)

    # Lower
    lbl = Label(tabSettingArea, text = "Lower")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=10, y=50)

    global scaleLowerAreaSetting
    lowerAreaSettingValue = DoubleVar() 
    scaleLowerAreaSetting = Scale(tabSettingArea, variable = lowerAreaSettingValue, from_ = 0, to = 50000, orient = HORIZONTAL, length=520)
    scaleLowerAreaSetting.place(x=10, y=65)
    scaleLowerAreaSetting.set(5000)

    # Upper
    lbl = Label(tabSettingArea, text = "Upper")
    lbl.config(font = ("Courier", 10))
    lbl.place(x=10, y=120)

    global scaleUpperAreaSetting
    upperAreaSettingValue = DoubleVar() 
    scaleUpperAreaSetting = Scale(tabSettingArea, variable = upperAreaSettingValue, from_ = 0, to = 50000, orient = HORIZONTAL, length=520)
    scaleUpperAreaSetting.place(x=10, y=140)
    scaleUpperAreaSetting.set(30000)

    #
    # Button
    #
    # buttonAreaSetting = None
    # buttonAreaSetting = Button(tabSettingArea, text ="Save", command = process, font = ("Courier", 16))
    # buttonAreaSetting.place(x=460, y=300)

    #
    # Result
    #
    lbl = Label(tabResult, text = "Result")
    lbl.config(font = ("Courier", 18))
    lbl.place(x=10, y=10)

    global lblResultGreen
    lblResultGreen = Label(tabResult, text = "Green = ")
    lblResultGreen.config(font = ("Courier", 12))
    lblResultGreen.place(x=10, y=50)

    global lblResultYellow
    lblResultYellow = Label(tabResult, text = "Yellow = ")
    lblResultYellow.config(font = ("Courier", 12))
    lblResultYellow.place(x=10, y=90)

    global lblResultAll
    lblResultAll = Label(tabResult, text = "All = ")
    lblResultAll.config(font = ("Courier", 12))
    lblResultAll.place(x=10, y=130)

    #
    # Button
    #
    # buttonProcess = None
    # buttonProcess = Button(tabResult, text ="Process", command = process, font = ("Courier", 16))
    # buttonProcess.place(x=430, y=300)

def process():
    # Source
    global sourceImageCV2

    # Source from demo image 
    sourceImageCV2 = cv2.imread('640x480.png')

    # Source from USB cam
    #video = cv2.VideoCapture(0)
    #ret, sourceImageCV2 = video.read()

    sourceImageCV2 = cv2.blur(sourceImageCV2, (5,5))
    
    # Gray
    global tabGray
    grayImageCV2 = cv2.cvtColor(sourceImageCV2, cv2.COLOR_BGR2GRAY)
    grayImageData = cv2.cvtColor(grayImageCV2, cv2.COLOR_GRAY2BGR)
    grayImageData = Image.fromarray(grayImageData)
    grayImageData = ImageTk.PhotoImage(grayImageData.resize((520,320)))
    grayImage = Label(tabGray, image=grayImageData)
    grayImage.image = grayImageData
    grayImage.place(x=10, y=10)

    # All binary
    global tabBinary
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
    allBinaryImageData = ImageTk.PhotoImage(allBinaryImageData.resize((520,320)))
    allBinaryImage = Label(tabBinary, image=allBinaryImageData)
    allBinaryImage.image = allBinaryImageData
    allBinaryImage.place(x=10, y=10)

    # Yellow binary
    global tabYellow
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
    yellowBinaryImageData = ImageTk.PhotoImage(yellowBinaryImageData.resize((520,320)))
    yellowBinaryImage = Label(tabYellow, image=yellowBinaryImageData)
    yellowBinaryImage.image = yellowBinaryImageData
    yellowBinaryImage.place(x=10, y=10)

    # Green
    if countAll != 0:
        lblResultGreen.configure(text = ("Green = 0, % = 0"))
        print("Green = 0")
        print("-------------------")
    else:
        lblResultGreen.configure(text = ("Green = " + str(countAll - countYellow) + ", % = " + str("{:.2f}".format(((countAll - countYellow) * 100) / countAll))))
        print("Green = ", countAll - countYellow)
        print("-------------------")

    # Highlight aread
    cv2.drawContours(sourceImageCV2, yellowCnts, -1, (255,255,0), 3)
    cv2.drawContours(sourceImageCV2, allCnts, -1, (255,0,0), 3)

    # Source
    global tabResult
    sourceImageData = cv2.cvtColor(sourceImageCV2, cv2.COLOR_BGR2RGB)
    sourceImageData = Image.fromarray(sourceImageData)
    sourceImageData = ImageTk.PhotoImage(sourceImageData.resize((520,320)))
    sourceImage = Label(tabOriginal, image=sourceImageData)
    sourceImage.image = sourceImageData
    sourceImage.place(x=10, y=10)

    # Next calling
    threading.Timer(5.0, process).start()

# Main entry point.
init()
process()
mainWindow.mainloop()