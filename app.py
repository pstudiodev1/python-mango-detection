from tkinter import *
from PIL import Image, ImageTk
import cv2

mainWindow = None
sourceImageCV2 = None
grayImageCV2 = None
greenBinaryImageCV2 = None
yellowBinaryImageCV2 = None

def init():
    global mainWindow
    mainWindow = Tk();
    mainWindow.title('Mango Detection')
    mainWindow.geometry('1800x966')

def process():
    # Source
    global sourceImageCV2 
    sourceImageCV2 = cv2.imread('640x480.png')
    sourceImageData = cv2.cvtColor(sourceImageCV2, cv2.COLOR_BGR2RGB)
    sourceImageData = Image.fromarray(sourceImageData)
    sourceImageData = ImageTk.PhotoImage(sourceImageData)
    sourceImage = Label(mainWindow, image=sourceImageData)
    sourceImage.image = sourceImageData
    sourceImage.place(x=0, y=0)
    # Gray
    grayImageCV2 = cv2.cvtColor(sourceImageCV2, cv2.COLOR_BGR2GRAY)
    grayImageData = cv2.cvtColor(grayImageCV2, cv2.COLOR_GRAY2BGR)
    grayImageData = Image.fromarray(grayImageData)
    grayImageData = ImageTk.PhotoImage(grayImageData)
    grayImage = Label(mainWindow, image=grayImageData)
    grayImage.image = grayImageData
    grayImage.place(x=642, y=0)
    # Yellow binary
    ret, yellowBinaryImage = cv2.threshold(grayImageCV2, 150, 255, cv2.THRESH_BINARY)
    yellowBinaryImageData = cv2.cvtColor(yellowBinaryImage, cv2.COLOR_GRAY2RGB)
    yellowBinaryImageData = Image.fromarray(yellowBinaryImageData)
    yellowBinaryImageData = ImageTk.PhotoImage(yellowBinaryImageData)
    yellowBinaryImage = Label(mainWindow, image=yellowBinaryImageData)
    yellowBinaryImage.image = yellowBinaryImageData
    yellowBinaryImage.place(x=0, y=482)
    # All binary
    ret, allBinaryImageCV2 = cv2.threshold(grayImageCV2, 100, 255, cv2.THRESH_BINARY)
    allBinaryImageData = cv2.cvtColor(allBinaryImageCV2, cv2.COLOR_GRAY2RGB)
    allBinaryImageData = Image.fromarray(allBinaryImageData)
    allBinaryImageData = ImageTk.PhotoImage(allBinaryImageData)
    allBinaryImage = Label(mainWindow, image=allBinaryImageData)
    allBinaryImage.image = allBinaryImageData
    allBinaryImage.place(x=642, y=482)

    # Scale
    v = DoubleVar() 
    scale = Scale(mainWindow, variable = v, from_ = 0, to = 255, orient = HORIZONTAL)
    scale.place(x=1600, y=0)

# Main entry point.
init()
process()
mainWindow.mainloop()