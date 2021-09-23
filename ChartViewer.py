# -----------------------------------------> GUI FOR SHOWCASING CHARTS <----------------------------------------- #
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def check(*args):
    dropDownVar.set(dropDownVar.get().strip("\t").strip())

def check1(*args):
    dropDownVar1.set(dropDownVar1.get().strip("\t").strip())

def check2(*args):
    dropDownVar2.set(dropDownVar2.get().strip("\t").strip())

def check3(*args):
    dropDownVar3.set(dropDownVar3.get().strip("\t").strip())


window = tk.Tk()
window.geometry("1316x800")
window.configure(bg = "black")
window.title("Stock Market Prediction")
window.resizable(0,0)
window.rowconfigure([0,1,2,3], minsize = 1, weight = 0)
window.columnconfigure([0,1], minsize = 332, weight = 0)
window.columnconfigure([2,3], minsize = 274, weight = 0)
window.columnconfigure(4, minsize = 1, weight = 0)

s = ttk.Style()
s.configure("TMenubutton", font = ('Helvetica', 19), foreground = "black", background = "#02c2e8")

#---------------------------------------------- IMAGES ----------------------------------------------#
image_1 = Image.open("./image/code-appears-here.png")
image_1 = ImageTk.PhotoImage(image_1.resize((round(image_1.size[0]*0.5), round(image_1.size[1]*0.5))))
image0= Image.open("./image/image-appears-here.png")
image0= ImageTk.PhotoImage(image0.resize((round(image0.size[0]*0.5), round(image0.size[1]*0.5))))
image1 = Image.open("./image/GBP-USD.png")
print(image1.size)
image1 = ImageTk.PhotoImage(image1.resize((round(image1.size[0]*0.5), round(image1.size[1]*0.5))))
image2 = Image.open("./image/USD-INR.png")
image2 = ImageTk.PhotoImage(image2.resize((round(image2.size[0]*0.5), round(image2.size[1]*0.5))))
image3 = Image.open("./image/BTC.png")
image3 = ImageTk.PhotoImage(image3.resize((round(image3.size[0]*0.5), round(image3.size[1]*0.5))))
image4 = Image.open("./image/USD-CAD.png")
image4 = ImageTk.PhotoImage(image4.resize((round(image4.size[0]*0.5), round(image4.size[1]*0.5))))
titleImage = Image.open("./image/stocktitle-cropped.png")
titleImage = titleImage.resize((round(titleImage.size[0] * 0.5), round(titleImage.size[1] * 0.5)))
titleImage_photoImage = ImageTk.PhotoImage(image = titleImage)

BTC_B10_E100_D120= Image.open("./images/BTC_B10_E100_D120.jpg")
BTC_B10_E100_D120= ImageTk.PhotoImage(BTC_B10_E100_D120.resize((round(BTC_B10_E100_D120.size[0]*0.5), 
round(BTC_B10_E100_D120.size[1]*0.5))))


BTC_B10_E100_D30= Image.open("./images/BTC_B10_E100_D30.jpg")
BTC_B10_E100_D30= ImageTk.PhotoImage(BTC_B10_E100_D30.resize((round(BTC_B10_E100_D30.size[0]*0.5), round(BTC_B10_E100_D30.size[1]*0.5))))


BTC_B10_E100_D60= Image.open("./images/BTC_B10_E100_D60.jpg")
BTC_B10_E100_D60= ImageTk.PhotoImage(BTC_B10_E100_D60.resize((round(BTC_B10_E100_D60.size[0]*0.5), round(BTC_B10_E100_D60.size[1]*0.5))))


BTC_B10_E1_D120= Image.open("./images/BTC_B10_E1_D120.jpg")
BTC_B10_E1_D120= ImageTk.PhotoImage(BTC_B10_E1_D120.resize((round(BTC_B10_E1_D120.size[0]*0.5), round(BTC_B10_E1_D120.size[1]*0.5))))


BTC_B10_E1_D30= Image.open("./images/BTC_B10_E1_D30.jpg")
BTC_B10_E1_D30= ImageTk.PhotoImage(BTC_B10_E1_D30.resize((round(BTC_B10_E1_D30.size[0]*0.5), round(BTC_B10_E1_D30.size[1]*0.5))))


BTC_B10_E1_D60= Image.open("./images/BTC_B10_E1_D60.jpg")
BTC_B10_E1_D60= ImageTk.PhotoImage(BTC_B10_E1_D60.resize((round(BTC_B10_E1_D60.size[0]*0.5), round(BTC_B10_E1_D60.size[1]*0.5))))


BTC_B10_E20_D120= Image.open("./images/BTC_B10_E20_D120.jpg")
BTC_B10_E20_D120= ImageTk.PhotoImage(BTC_B10_E20_D120.resize((round(BTC_B10_E20_D120.size[0]*0.5), round(BTC_B10_E20_D120.size[1]*0.5))))


BTC_B10_E20_D30= Image.open("./images/BTC_B10_E20_D30.jpg")
BTC_B10_E20_D30= ImageTk.PhotoImage(BTC_B10_E20_D30.resize((round(BTC_B10_E20_D30.size[0]*0.5), round(BTC_B10_E20_D30.size[1]*0.5))))


BTC_B10_E20_D60= Image.open("./images/BTC_B10_E20_D60.jpg")
BTC_B10_E20_D60= ImageTk.PhotoImage(BTC_B10_E20_D60.resize((round(BTC_B10_E20_D60.size[0]*0.5), round(BTC_B10_E20_D60.size[1]*0.5))))


BTC_B10_E5_D120= Image.open("./images/BTC_B10_E5_D120.jpg")
BTC_B10_E5_D120= ImageTk.PhotoImage(BTC_B10_E5_D120.resize((round(BTC_B10_E5_D120.size[0]*0.5), round(BTC_B10_E5_D120.size[1]*0.5))))


BTC_B10_E5_D30= Image.open("./images/BTC_B10_E5_D30.jpg")
BTC_B10_E5_D30= ImageTk.PhotoImage(BTC_B10_E5_D30.resize((round(BTC_B10_E5_D30.size[0]*0.5), round(BTC_B10_E5_D30.size[1]*0.5))))


BTC_B10_E5_D60= Image.open("./images/BTC_B10_E5_D60.jpg")
BTC_B10_E5_D60= ImageTk.PhotoImage(BTC_B10_E5_D60.resize((round(BTC_B10_E5_D60.size[0]*0.5), round(BTC_B10_E5_D60.size[1]*0.5))))


BTC_B16_E100_D120= Image.open("./images/BTC_B16_E100_D120.jpg")
BTC_B16_E100_D120= ImageTk.PhotoImage(BTC_B16_E100_D120.resize((round(BTC_B16_E100_D120.size[0]*0.5), 
round(BTC_B16_E100_D120.size[1]*0.5))))


BTC_B16_E100_D30= Image.open("./images/BTC_B16_E100_D30.jpg")
BTC_B16_E100_D30= ImageTk.PhotoImage(BTC_B16_E100_D30.resize((round(BTC_B16_E100_D30.size[0]*0.5), round(BTC_B16_E100_D30.size[1]*0.5))))


BTC_B16_E100_D60= Image.open("./images/BTC_B16_E100_D60.jpg")
BTC_B16_E100_D60= ImageTk.PhotoImage(BTC_B16_E100_D60.resize((round(BTC_B16_E100_D60.size[0]*0.5), round(BTC_B16_E100_D60.size[1]*0.5))))


BTC_B16_E1_D120= Image.open("./images/BTC_B16_E1_D120.jpg")
BTC_B16_E1_D120= ImageTk.PhotoImage(BTC_B16_E1_D120.resize((round(BTC_B16_E1_D120.size[0]*0.5), round(BTC_B16_E1_D120.size[1]*0.5))))


BTC_B16_E1_D30= Image.open("./images/BTC_B16_E1_D30.jpg")
BTC_B16_E1_D30= ImageTk.PhotoImage(BTC_B16_E1_D30.resize((round(BTC_B16_E1_D30.size[0]*0.5), round(BTC_B16_E1_D30.size[1]*0.5))))


BTC_B16_E1_D60= Image.open("./images/BTC_B16_E1_D60.jpg")
BTC_B16_E1_D60= ImageTk.PhotoImage(BTC_B16_E1_D60.resize((round(BTC_B16_E1_D60.size[0]*0.5), round(BTC_B16_E1_D60.size[1]*0.5))))


BTC_B16_E20_D120= Image.open("./images/BTC_B16_E20_D120.jpg")
BTC_B16_E20_D120= ImageTk.PhotoImage(BTC_B16_E20_D120.resize((round(BTC_B16_E20_D120.size[0]*0.5), round(BTC_B16_E20_D120.size[1]*0.5))))


BTC_B16_E20_D30= Image.open("./images/BTC_B16_E20_D30.jpg")
BTC_B16_E20_D30= ImageTk.PhotoImage(BTC_B16_E20_D30.resize((round(BTC_B16_E20_D30.size[0]*0.5), round(BTC_B16_E20_D30.size[1]*0.5))))


BTC_B16_E20_D60= Image.open("./images/BTC_B16_E20_D60.jpg")
BTC_B16_E20_D60= ImageTk.PhotoImage(BTC_B16_E20_D60.resize((round(BTC_B16_E20_D60.size[0]*0.5), round(BTC_B16_E20_D60.size[1]*0.5))))


BTC_B16_E5_D120= Image.open("./images/BTC_B16_E5_D120.jpg")
BTC_B16_E5_D120= ImageTk.PhotoImage(BTC_B16_E5_D120.resize((round(BTC_B16_E5_D120.size[0]*0.5), round(BTC_B16_E5_D120.size[1]*0.5))))


BTC_B16_E5_D30= Image.open("./images/BTC_B16_E5_D30.jpg")
BTC_B16_E5_D30= ImageTk.PhotoImage(BTC_B16_E5_D30.resize((round(BTC_B16_E5_D30.size[0]*0.5), round(BTC_B16_E5_D30.size[1]*0.5))))


BTC_B16_E5_D60= Image.open("./images/BTC_B16_E5_D60.jpg")
BTC_B16_E5_D60= ImageTk.PhotoImage(BTC_B16_E5_D60.resize((round(BTC_B16_E5_D60.size[0]*0.5), round(BTC_B16_E5_D60.size[1]*0.5))))


BTC_B32_E100_D120= Image.open("./images/BTC_B32_E100_D120.jpg")
BTC_B32_E100_D120= ImageTk.PhotoImage(BTC_B32_E100_D120.resize((round(BTC_B32_E100_D120.size[0]*0.5), 
round(BTC_B32_E100_D120.size[1]*0.5))))


BTC_B32_E100_D30= Image.open("./images/BTC_B32_E100_D30.jpg")
BTC_B32_E100_D30= ImageTk.PhotoImage(BTC_B32_E100_D30.resize((round(BTC_B32_E100_D30.size[0]*0.5), round(BTC_B32_E100_D30.size[1]*0.5))))


BTC_B32_E100_D60= Image.open("./images/BTC_B32_E100_D60.jpg")
BTC_B32_E100_D60= ImageTk.PhotoImage(BTC_B32_E100_D60.resize((round(BTC_B32_E100_D60.size[0]*0.5), round(BTC_B32_E100_D60.size[1]*0.5))))


BTC_B32_E20_D120= Image.open("./images/BTC_B32_E20_D120.jpg")
BTC_B32_E20_D120= ImageTk.PhotoImage(BTC_B32_E20_D120.resize((round(BTC_B32_E20_D120.size[0]*0.5), round(BTC_B32_E20_D120.size[1]*0.5))))


BTC_B32_E20_D30= Image.open("./images/BTC_B32_E20_D30.jpg")
BTC_B32_E20_D30= ImageTk.PhotoImage(BTC_B32_E20_D30.resize((round(BTC_B32_E20_D30.size[0]*0.5), round(BTC_B32_E20_D30.size[1]*0.5))))


BTC_B32_E20_D60= Image.open("./images/BTC_B32_E20_D60.jpg")
BTC_B32_E20_D60= ImageTk.PhotoImage(BTC_B32_E20_D60.resize((round(BTC_B32_E20_D60.size[0]*0.5), round(BTC_B32_E20_D60.size[1]*0.5))))


BTC_B32_E1_D120= Image.open("./images/BTC_B32_E1_D120.jpg")
BTC_B32_E1_D120= ImageTk.PhotoImage(BTC_B32_E1_D120.resize((round(BTC_B32_E1_D120.size[0]*0.5), round(BTC_B32_E1_D120.size[1]*0.5))))


BTC_B32_E1_D30= Image.open("./images/BTC_B32_E1_D30.jpg")
BTC_B32_E1_D30= ImageTk.PhotoImage(BTC_B32_E1_D30.resize((round(BTC_B32_E1_D30.size[0]*0.5), round(BTC_B32_E1_D30.size[1]*0.5))))


BTC_B32_E1_D60= Image.open("./images/BTC_B32_E1_D60.jpg")
BTC_B32_E1_D60= ImageTk.PhotoImage(BTC_B32_E1_D60.resize((round(BTC_B32_E1_D60.size[0]*0.5), round(BTC_B32_E1_D60.size[1]*0.5))))


BTC_B32_E5_D120= Image.open("./images/BTC_B32_E5_D120.jpg")
BTC_B32_E5_D120= ImageTk.PhotoImage(BTC_B32_E5_D120.resize((round(BTC_B32_E5_D120.size[0]*0.5), round(BTC_B32_E5_D120.size[1]*0.5))))


BTC_B32_E5_D30= Image.open("./images/BTC_B32_E5_D30.jpg")
BTC_B32_E5_D30= ImageTk.PhotoImage(BTC_B32_E5_D30.resize((round(BTC_B32_E5_D30.size[0]*0.5), round(BTC_B32_E5_D30.size[1]*0.5))))


BTC_B32_E5_D60= Image.open("./images/BTC_B32_E5_D60.jpg")
BTC_B32_E5_D60= ImageTk.PhotoImage(BTC_B32_E5_D60.resize((round(BTC_B32_E5_D60.size[0]*0.5), round(BTC_B32_E5_D60.size[1]*0.5))))


BTC_B5_E100_D120= Image.open("./images/BTC_B5_E100_D120.jpg")
BTC_B5_E100_D120= ImageTk.PhotoImage(BTC_B5_E100_D120.resize((round(BTC_B5_E100_D120.size[0]*0.5), round(BTC_B5_E100_D120.size[1]*0.5))))


BTC_B5_E100_D30= Image.open("./images/BTC_B5_E100_D30.jpg")
BTC_B5_E100_D30= ImageTk.PhotoImage(BTC_B5_E100_D30.resize((round(BTC_B5_E100_D30.size[0]*0.5), round(BTC_B5_E100_D30.size[1]*0.5))))


BTC_B5_E100_D60= Image.open("./images/BTC_B5_E100_D60.jpg")
BTC_B5_E100_D60= ImageTk.PhotoImage(BTC_B5_E100_D60.resize((round(BTC_B5_E100_D60.size[0]*0.5), round(BTC_B5_E100_D60.size[1]*0.5))))


BTC_B5_E1_D120= Image.open("./images/BTC_B5_E1_D120.jpg")
BTC_B5_E1_D120= ImageTk.PhotoImage(BTC_B5_E1_D120.resize((round(BTC_B5_E1_D120.size[0]*0.5), round(BTC_B5_E1_D120.size[1]*0.5))))


BTC_B5_E1_D30= Image.open("./images/BTC_B5_E1_D30.jpg")
BTC_B5_E1_D30= ImageTk.PhotoImage(BTC_B5_E1_D30.resize((round(BTC_B5_E1_D30.size[0]*0.5), round(BTC_B5_E1_D30.size[1]*0.5))))


BTC_B5_E1_D60= Image.open("./images/BTC_B5_E1_D60.jpg")
BTC_B5_E1_D60= ImageTk.PhotoImage(BTC_B5_E1_D60.resize((round(BTC_B5_E1_D60.size[0]*0.5), round(BTC_B5_E1_D60.size[1]*0.5))))


BTC_B5_E20_D120= Image.open("./images/BTC_B5_E20_D120.jpg")
BTC_B5_E20_D120= ImageTk.PhotoImage(BTC_B5_E20_D120.resize((round(BTC_B5_E20_D120.size[0]*0.5), round(BTC_B5_E20_D120.size[1]*0.5))))


BTC_B5_E20_D30= Image.open("./images/BTC_B5_E20_D30.jpg")
BTC_B5_E20_D30= ImageTk.PhotoImage(BTC_B5_E20_D30.resize((round(BTC_B5_E20_D30.size[0]*0.5), round(BTC_B5_E20_D30.size[1]*0.5))))


BTC_B5_E20_D60= Image.open("./images/BTC_B5_E20_D60.jpg")
BTC_B5_E20_D60= ImageTk.PhotoImage(BTC_B5_E20_D60.resize((round(BTC_B5_E20_D60.size[0]*0.5), round(BTC_B5_E20_D60.size[1]*0.5))))


BTC_B5_E5_D120= Image.open("./images/BTC_B5_E5_D120.jpg")
BTC_B5_E5_D120= ImageTk.PhotoImage(BTC_B5_E5_D120.resize((round(BTC_B5_E5_D120.size[0]*0.5), round(BTC_B5_E5_D120.size[1]*0.5))))


BTC_B5_E5_D30= Image.open("./images/BTC_B5_E5_D30.jpg")
BTC_B5_E5_D30= ImageTk.PhotoImage(BTC_B5_E5_D30.resize((round(BTC_B5_E5_D30.size[0]*0.5), round(BTC_B5_E5_D30.size[1]*0.5))))


BTC_B5_E5_D60= Image.open("./images/BTC_B5_E5_D60.jpg")
BTC_B5_E5_D60= ImageTk.PhotoImage(BTC_B5_E5_D60.resize((round(BTC_B5_E5_D60.size[0]*0.5), round(BTC_B5_E5_D60.size[1]*0.5))))


USDCAD_B10_E100_D120= Image.open("./images/USDCAD_B10_E100_D120.jpg")
USDCAD_B10_E100_D120= ImageTk.PhotoImage(USDCAD_B10_E100_D120.resize((round(USDCAD_B10_E100_D120.size[0]*0.5), round(USDCAD_B10_E100_D120.size[1]*0.5))))


USDCAD_B10_E100_D30= Image.open("./images/USDCAD_B10_E100_D30.jpg")
USDCAD_B10_E100_D30= ImageTk.PhotoImage(USDCAD_B10_E100_D30.resize((round(USDCAD_B10_E100_D30.size[0]*0.5), round(USDCAD_B10_E100_D30.size[1]*0.5))))


USDCAD_B10_E100_D60= Image.open("./images/USDCAD_B10_E100_D60.jpg")
USDCAD_B10_E100_D60= ImageTk.PhotoImage(USDCAD_B10_E100_D60.resize((round(USDCAD_B10_E100_D60.size[0]*0.5), round(USDCAD_B10_E100_D60.size[1]*0.5))))


USDCAD_B10_E1_D120= Image.open("./images/USDCAD_B10_E1_D120.jpg")
USDCAD_B10_E1_D120= ImageTk.PhotoImage(USDCAD_B10_E1_D120.resize((round(USDCAD_B10_E1_D120.size[0]*0.5), round(USDCAD_B10_E1_D120.size[1]*0.5))))


USDCAD_B10_E1_D60= Image.open("./images/USDCAD_B10_E1_D60.jpg")
USDCAD_B10_E1_D60= ImageTk.PhotoImage(USDCAD_B10_E1_D60.resize((round(USDCAD_B10_E1_D60.size[0]*0.5), 
round(USDCAD_B10_E1_D60.size[1]*0.5))))


USDCAD_B10_E20_D120= Image.open("./images/USDCAD_B10_E20_D120.jpg")
USDCAD_B10_E20_D120= ImageTk.PhotoImage(USDCAD_B10_E20_D120.resize((round(USDCAD_B10_E20_D120.size[0]*0.5), round(USDCAD_B10_E20_D120.size[1]*0.5))))


USDCAD_B10_E20_D30= Image.open("./images/USDCAD_B10_E20_D30.jpg")
USDCAD_B10_E20_D30= ImageTk.PhotoImage(USDCAD_B10_E20_D30.resize((round(USDCAD_B10_E20_D30.size[0]*0.5), round(USDCAD_B10_E20_D30.size[1]*0.5))))


USDCAD_B10_E20_D60= Image.open("./images/USDCAD_B10_E20_D60.jpg")
USDCAD_B10_E20_D60= ImageTk.PhotoImage(USDCAD_B10_E20_D60.resize((round(USDCAD_B10_E20_D60.size[0]*0.5), round(USDCAD_B10_E20_D60.size[1]*0.5))))


USDCAD_B10_E5_D120= Image.open("./images/USDCAD_B10_E5_D120.jpg")
USDCAD_B10_E5_D120= ImageTk.PhotoImage(USDCAD_B10_E5_D120.resize((round(USDCAD_B10_E5_D120.size[0]*0.5), round(USDCAD_B10_E5_D120.size[1]*0.5))))


USDCAD_B10_E5_D30= Image.open("./images/USDCAD_B10_E5_D30.jpg")
USDCAD_B10_E5_D30= ImageTk.PhotoImage(USDCAD_B10_E5_D30.resize((round(USDCAD_B10_E5_D30.size[0]*0.5), 
round(USDCAD_B10_E5_D30.size[1]*0.5))))


USDCAD_B10_E5_D60= Image.open("./images/USDCAD_B10_E5_D60.jpg")
USDCAD_B10_E5_D60= ImageTk.PhotoImage(USDCAD_B10_E5_D60.resize((round(USDCAD_B10_E5_D60.size[0]*0.5), 
round(USDCAD_B10_E5_D60.size[1]*0.5))))


USDCAD_B16_E100_D120= Image.open("./images/USDCAD_B16_E100_D120.jpg")
USDCAD_B16_E100_D120= ImageTk.PhotoImage(USDCAD_B16_E100_D120.resize((round(USDCAD_B16_E100_D120.size[0]*0.5), round(USDCAD_B16_E100_D120.size[1]*0.5))))


USDCAD_B16_E100_D30 = Image.open("./images/USDCAD_B16_E100_D30.jpg")
USDCAD_B16_E100_D30 = ImageTk.PhotoImage(USDCAD_B16_E100_D30.resize((round(USDCAD_B16_E100_D30.size[0]*0.5), round(USDCAD_B16_E100_D30.size[1]*0.5))))


USDCAD_B16_E100_D60= Image.open("./images/USDCAD_B16_E100_D60.jpg")
USDCAD_B16_E100_D60= ImageTk.PhotoImage(USDCAD_B16_E100_D60.resize((round(USDCAD_B16_E100_D60.size[0]*0.5), round(USDCAD_B16_E100_D60.size[1]*0.5))))


USDCAD_B16_E1_D120= Image.open("./images/USDCAD_B16_E1_D120.jpg")
USDCAD_B16_E1_D120= ImageTk.PhotoImage(USDCAD_B16_E1_D120.resize((round(USDCAD_B16_E1_D120.size[0]*0.5), round(USDCAD_B16_E1_D120.size[1]*0.5))))


USDCAD_B16_E1_D30= Image.open("./images/USDCAD_B16_E1_D30.jpg")
USDCAD_B16_E1_D30= ImageTk.PhotoImage(USDCAD_B16_E1_D30.resize((round(USDCAD_B16_E1_D30.size[0]*0.5), 
round(USDCAD_B16_E1_D30.size[1]*0.5))))


USDCAD_B16_E1_D60= Image.open("./images/USDCAD_B16_E1_D60.jpg")
USDCAD_B16_E1_D60= ImageTk.PhotoImage(USDCAD_B16_E1_D60.resize((round(USDCAD_B16_E1_D60.size[0]*0.5), 
round(USDCAD_B16_E1_D60.size[1]*0.5))))


USDCAD_B16_E20_D120= Image.open("./images/USDCAD_B16_E20_D120.jpg")
USDCAD_B16_E20_D120= ImageTk.PhotoImage(USDCAD_B16_E20_D120.resize((round(USDCAD_B16_E20_D120.size[0]*0.5), round(USDCAD_B16_E20_D120.size[1]*0.5))))


USDCAD_B16_E20_D30= Image.open("./images/USDCAD_B16_E20_D30.jpg")
USDCAD_B16_E20_D30= ImageTk.PhotoImage(USDCAD_B16_E20_D30.resize((round(USDCAD_B16_E20_D30.size[0]*0.5), round(USDCAD_B16_E20_D30.size[1]*0.5))))


USDCAD_B16_E20_D60= Image.open("./images/USDCAD_B16_E20_D60.jpg")
USDCAD_B16_E20_D60= ImageTk.PhotoImage(USDCAD_B16_E20_D60.resize((round(USDCAD_B16_E20_D60.size[0]*0.5), round(USDCAD_B16_E20_D60.size[1]*0.5))))


USDCAD_B16_E5_D120= Image.open("./images/USDCAD_B16_E5_D120.jpg")
USDCAD_B16_E5_D120= ImageTk.PhotoImage(USDCAD_B16_E5_D120.resize((round(USDCAD_B16_E5_D120.size[0]*0.5), round(USDCAD_B16_E5_D120.size[1]*0.5))))


USDCAD_B16_E5_D30= Image.open("./images/USDCAD_B16_E5_D30.jpg")
USDCAD_B16_E5_D30= ImageTk.PhotoImage(USDCAD_B16_E5_D30.resize((round(USDCAD_B16_E5_D30.size[0]*0.5), 
round(USDCAD_B16_E5_D30.size[1]*0.5))))


USDCAD_B16_E5_D60= Image.open("./images/USDCAD_B16_E5_D60.jpg")
USDCAD_B16_E5_D60= ImageTk.PhotoImage(USDCAD_B16_E5_D60.resize((round(USDCAD_B16_E5_D60.size[0]*0.5), 
round(USDCAD_B16_E5_D60.size[1]*0.5))))


USDCAD_B32_E100_D120= Image.open("./images/USDCAD_B32_E100_D120.jpg")
USDCAD_B32_E100_D120= ImageTk.PhotoImage(USDCAD_B32_E100_D120.resize((round(USDCAD_B32_E100_D120.size[0]*0.5), round(USDCAD_B32_E100_D120.size[1]*0.5))))


USDCAD_B32_E100_D30= Image.open("./images/USDCAD_B32_E100_D30.jpg")
USDCAD_B32_E100_D30= ImageTk.PhotoImage(USDCAD_B32_E100_D30.resize((round(USDCAD_B32_E100_D30.size[0]*0.5), round(USDCAD_B32_E100_D30.size[1]*0.5))))


USDCAD_B32_E100_D60= Image.open("./images/USDCAD_B32_E100_D60.jpg")
USDCAD_B32_E100_D60= ImageTk.PhotoImage(USDCAD_B32_E100_D60.resize((round(USDCAD_B32_E100_D60.size[0]*0.5), round(USDCAD_B32_E100_D60.size[1]*0.5))))


USDCAD_B32_E20_D120 = Image.open("./images/USDCAD_B32_E20_D120.jpg")
USDCAD_B32_E20_D120 = ImageTk.PhotoImage(USDCAD_B32_E20_D120.resize((round(USDCAD_B32_E20_D120.size[0]*0.5), round(USDCAD_B32_E20_D120.size[1]*0.5))))


USDCAD_B32_E20_D30 = Image.open("./images/USDCAD_B32_E20_D30.jpg")
USDCAD_B32_E20_D30 = ImageTk.PhotoImage(USDCAD_B32_E20_D30.resize((round(USDCAD_B32_E20_D30.size[0]*0.5), round(USDCAD_B32_E20_D30.size[1]*0.5))))


USDCAD_B32_E20_D60 = Image.open("./images/USDCAD_B32_E20_D60.jpg")
USDCAD_B32_E20_D60 = ImageTk.PhotoImage(USDCAD_B32_E20_D60.resize((round(USDCAD_B32_E20_D60.size[0]*0.5), round(USDCAD_B32_E20_D60.size[1]*0.5))))

USDCAD_B32_E5_D30= Image.open("./images/USDCAD_B32_E5_D30.jpg")
USDCAD_B32_E5_D30= ImageTk.PhotoImage(USDCAD_B32_E5_D30.resize((round(USDCAD_B32_E5_D30.size[0]*0.5), round(USDCAD_B32_E5_D30.size[1]*0.5))))

USDCAD_B32_E5_D60= Image.open("./images/USDCAD_B32_E5_D60.jpg")
USDCAD_B32_E5_D60= ImageTk.PhotoImage(USDCAD_B32_E5_D60.resize((round(USDCAD_B32_E5_D60.size[0]*0.5), round(USDCAD_B32_E5_D60.size[1]*0.5))))

USDCAD_B32_E5_D120= Image.open("./images/USDCAD_B32_E5_D120.jpg")
USDCAD_B32_E5_D120= ImageTk.PhotoImage(USDCAD_B32_E5_D120.resize((round(USDCAD_B32_E5_D120.size[0]*0.5), round(USDCAD_B32_E5_D120.size[1]*0.5))))

USDCAD_B32_E1_D120 = Image.open("./images/USDCAD_B32_E1_D120.jpg")
USDCAD_B32_E1_D120 = ImageTk.PhotoImage(USDCAD_B32_E1_D120.resize((round(USDCAD_B32_E1_D120.size[0]*0.5), round(USDCAD_B32_E1_D120.size[1]*0.5))))


USDCAD_B32_E1_D30 = Image.open("./images/USDCAD_B32_E1_D30.jpg")
USDCAD_B32_E1_D30 = ImageTk.PhotoImage(USDCAD_B32_E1_D30.resize((round(USDCAD_B32_E1_D30.size[0]*0.5), round(USDCAD_B32_E1_D30.size[1]*0.5))))


USDCAD_B32_E1_D60= Image.open("./images/USDCAD_B32_E1_D60.jpg")
USDCAD_B32_E1_D60= ImageTk.PhotoImage(USDCAD_B32_E1_D60.resize((round(USDCAD_B32_E1_D60.size[0]*0.5), 
round(USDCAD_B32_E1_D60.size[1]*0.5))))


USDCAD_B32_E20_D120= Image.open("./images/USDCAD_B32_E20_D120.jpg")
USDCAD_B32_E20_D120= ImageTk.PhotoImage(USDCAD_B32_E20_D120.resize((round(USDCAD_B32_E20_D120.size[0]*0.5), round(USDCAD_B32_E20_D120.size[1]*0.5))))


USDCAD_B32_E20_D30 = Image.open("./images/USDCAD_B32_E20_D30.jpg")
USDCAD_B32_E20_D30 = ImageTk.PhotoImage(USDCAD_B32_E20_D30.resize((round(USDCAD_B32_E20_D30.size[0]*0.5), round(USDCAD_B32_E20_D30.size[1]*0.5))))


USDCAD_B32_E20_D60 = Image.open("./images/USDCAD_B32_E20_D60.jpg")
USDCAD_B32_E20_D60 = ImageTk.PhotoImage(USDCAD_B32_E20_D60.resize((round(USDCAD_B32_E20_D60.size[0]*0.5), round(USDCAD_B32_E20_D60.size[1]*0.5))))


USDCAD_B5_E100_D120= Image.open("./images/USDCAD_B5_E100_D120.jpg")
USDCAD_B5_E100_D120= ImageTk.PhotoImage(USDCAD_B5_E100_D120.resize((round(USDCAD_B5_E100_D120.size[0]*0.5), round(USDCAD_B5_E100_D120.size[1]*0.5))))


USDCAD_B5_E100_D30= Image.open("./images/USDCAD_B5_E100_D30.jpg")
USDCAD_B5_E100_D30= ImageTk.PhotoImage(USDCAD_B5_E100_D30.resize((round(USDCAD_B5_E100_D30.size[0]*0.5), round(USDCAD_B5_E100_D30.size[1]*0.5))))


USDCAD_B5_E100_D60= Image.open("./images/USDCAD_B5_E100_D60.jpg")
USDCAD_B5_E100_D60= ImageTk.PhotoImage(USDCAD_B5_E100_D60.resize((round(USDCAD_B5_E100_D60.size[0]*0.5), round(USDCAD_B5_E100_D60.size[1]*0.5))))


USDCAD_B5_E1_D120= Image.open("./images/USDCAD_B5_E1_D120.jpg")
USDCAD_B5_E1_D120= ImageTk.PhotoImage(USDCAD_B5_E1_D120.resize((round(USDCAD_B5_E1_D120.size[0]*0.5), 
round(USDCAD_B5_E1_D120.size[1]*0.5))))


USDCAD_B5_E1_D30= Image.open("./images/USDCAD_B5_E1_D30.jpg")
USDCAD_B5_E1_D30= ImageTk.PhotoImage(USDCAD_B5_E1_D30.resize((round(USDCAD_B5_E1_D30.size[0]*0.5), round(USDCAD_B5_E1_D30.size[1]*0.5))))


USDCAD_B5_E1_D60= Image.open("./images/USDCAD_B5_E1_D60.jpg")
USDCAD_B5_E1_D60= ImageTk.PhotoImage(USDCAD_B5_E1_D60.resize((round(USDCAD_B5_E1_D60.size[0]*0.5), round(USDCAD_B5_E1_D60.size[1]*0.5))))


USDCAD_B5_E20_D120= Image.open("./images/USDCAD_B5_E20_D120.jpg")
USDCAD_B5_E20_D120= ImageTk.PhotoImage(USDCAD_B5_E20_D120.resize((round(USDCAD_B5_E20_D120.size[0]*0.5), round(USDCAD_B5_E20_D120.size[1]*0.5))))


USDCAD_B5_E20_D30= Image.open("./images/USDCAD_B5_E20_D30.jpg")
USDCAD_B5_E20_D30= ImageTk.PhotoImage(USDCAD_B5_E20_D30.resize((round(USDCAD_B5_E20_D30.size[0]*0.5), 
round(USDCAD_B5_E20_D30.size[1]*0.5))))


USDCAD_B5_E20_D60= Image.open("./images/USDCAD_B5_E20_D60.jpg")
USDCAD_B5_E20_D60= ImageTk.PhotoImage(USDCAD_B5_E20_D60.resize((round(USDCAD_B5_E20_D60.size[0]*0.5), 
round(USDCAD_B5_E20_D60.size[1]*0.5))))


USDCAD_B5_E5_D120= Image.open("./images/USDCAD_B5_E5_D120.jpg")
USDCAD_B5_E5_D120= ImageTk.PhotoImage(USDCAD_B5_E5_D120.resize((round(USDCAD_B5_E5_D120.size[0]*0.5), 
round(USDCAD_B5_E5_D120.size[1]*0.5))))


USDCAD_B5_E5_D30= Image.open("./images/USDCAD_B5_E5_D30.jpg")
USDCAD_B5_E5_D30= ImageTk.PhotoImage(USDCAD_B5_E5_D30.resize((round(USDCAD_B5_E5_D30.size[0]*0.5), round(USDCAD_B5_E5_D30.size[1]*0.5))))


USDCAD_B5_E5_D60= Image.open("./images/USDCAD_B5_E5_D60.jpg")
USDCAD_B5_E5_D60= ImageTk.PhotoImage(USDCAD_B5_E5_D60.resize((round(USDCAD_B5_E5_D60.size[0]*0.5), round(USDCAD_B5_E5_D60.size[1]*0.5))))

imageDict = {"BTC_B10_E100_D120": BTC_B10_E100_D120, "BTC_B10_E100_D30": BTC_B10_E100_D30, "BTC_B10_E100_D60": BTC_B10_E100_D60, "BTC_B10_E1_D120": BTC_B10_E1_D120, "BTC_B10_E1_D30": BTC_B10_E1_D30, "BTC_B10_E1_D60": BTC_B10_E1_D60, "BTC_B10_E20_D120": BTC_B10_E20_D120, "BTC_B10_E20_D30": BTC_B10_E20_D30, "BTC_B10_E20_D60": BTC_B10_E20_D60, "BTC_B10_E5_D120": BTC_B10_E5_D120, "BTC_B10_E5_D30": BTC_B10_E5_D30, "BTC_B10_E5_D60": BTC_B10_E5_D60, "BTC_B16_E100_D120": BTC_B16_E100_D120, "BTC_B16_E100_D30": BTC_B16_E100_D30, "BTC_B16_E100_D60": BTC_B16_E100_D60, "BTC_B16_E1_D120": BTC_B16_E1_D120, "BTC_B16_E1_D30": BTC_B16_E1_D30, "BTC_B16_E1_D60": BTC_B16_E1_D60, "BTC_B16_E20_D120": BTC_B16_E20_D120, "BTC_B16_E20_D30": BTC_B16_E20_D30, "BTC_B16_E20_D60": BTC_B16_E20_D60, "BTC_B16_E5_D120": BTC_B16_E5_D120, "BTC_B16_E5_D30": BTC_B16_E5_D30, "BTC_B16_E5_D60": BTC_B16_E5_D60, "BTC_B32_E100_D120": BTC_B32_E100_D120, "BTC_B32_E100_D30": BTC_B32_E100_D30, "BTC_B32_E100_D60": BTC_B32_E100_D60, "BTC_B32_E20_D120": BTC_B32_E20_D120, "BTC_B32_E20_D30": BTC_B32_E20_D30, "BTC_B32_E20_D60": BTC_B32_E20_D60, "BTC_B32_E1_D120": BTC_B32_E1_D120, "BTC_B32_E1_D30": BTC_B32_E1_D30, "BTC_B32_E1_D60": BTC_B32_E1_D60, "BTC_B32_E5_D120": BTC_B32_E5_D120, "BTC_B32_E5_D30": BTC_B32_E5_D30, "BTC_B32_E5_D60": BTC_B32_E5_D60, "BTC_B5_E100_D120": BTC_B5_E100_D120, "BTC_B5_E100_D30": BTC_B5_E100_D30, "BTC_B5_E100_D60": BTC_B5_E100_D60, "BTC_B5_E1_D120": BTC_B5_E1_D120, "BTC_B5_E1_D30": BTC_B5_E1_D30, "BTC_B5_E1_D60": BTC_B5_E1_D60, "BTC_B5_E20_D120": BTC_B5_E20_D120, "BTC_B5_E20_D30": BTC_B5_E20_D30, "BTC_B5_E20_D60": BTC_B5_E20_D60, "BTC_B5_E5_D120": BTC_B5_E5_D120, 
"BTC_B5_E5_D30": BTC_B5_E5_D30, "BTC_B5_E5_D60": BTC_B5_E5_D60, "USDCAD_B10_E100_D120": USDCAD_B10_E100_D120, "USDCAD_B10_E100_D30": USDCAD_B10_E100_D30, "USDCAD_B10_E100_D60": USDCAD_B10_E100_D60, "USDCAD_B10_E1_D120": USDCAD_B10_E1_D120, "USDCAD_B10_E1_D60": USDCAD_B10_E1_D60, "USDCAD_B10_E20_D120": USDCAD_B10_E20_D120, "USDCAD_B10_E20_D30": USDCAD_B10_E20_D30, "USDCAD_B10_E20_D60": USDCAD_B10_E20_D60, "USDCAD_B10_E5_D120": USDCAD_B10_E5_D120, "USDCAD_B10_E5_D30": USDCAD_B10_E5_D30, "USDCAD_B10_E5_D60": USDCAD_B10_E5_D60, "USDCAD_B16_E100_D120": USDCAD_B16_E100_D120, "USDCAD_B16_E100_D30": USDCAD_B16_E100_D30, "USDCAD_B16_E100_D60": USDCAD_B16_E100_D60, "USDCAD_B16_E1_D120": USDCAD_B16_E1_D120, "USDCAD_B16_E1_D30": USDCAD_B16_E1_D30, "USDCAD_B16_E1_D60": USDCAD_B16_E1_D60, "USDCAD_B16_E20_D120": USDCAD_B16_E20_D120, "USDCAD_B16_E20_D30": USDCAD_B16_E20_D30, "USDCAD_B16_E20_D60": USDCAD_B16_E20_D60, "USDCAD_B16_E5_D120": USDCAD_B16_E5_D120, "USDCAD_B16_E5_D30": USDCAD_B16_E5_D30, "USDCAD_B16_E5_D60": USDCAD_B16_E5_D60, "USDCAD_B32_E100_D120": USDCAD_B32_E100_D120, "USDCAD_B32_E100_D30": USDCAD_B32_E100_D30, "USDCAD_B32_E100_D60": USDCAD_B32_E100_D60, "USDCAD_B32_E20_D120": USDCAD_B32_E20_D120, "USDCAD_B32_E20_D30": USDCAD_B32_E20_D30, "USDCAD_B32_E20_D60": USDCAD_B32_E20_D60, "USDCAD_B32_E1_D120": USDCAD_B32_E1_D120, "USDCAD_B32_E1_D30": USDCAD_B32_E1_D30, "USDCAD_B32_E1_D60": USDCAD_B32_E1_D60, "USDCAD_B32_E20_D120": USDCAD_B32_E20_D120, "USDCAD_B32_E20_D30": USDCAD_B32_E20_D30, "USDCAD_B32_E20_D60": USDCAD_B32_E20_D60, "USDCAD_B5_E100_D120": USDCAD_B5_E100_D120, "USDCAD_B5_E100_D30": USDCAD_B5_E100_D30, "USDCAD_B5_E100_D60": USDCAD_B5_E100_D60, "USDCAD_B5_E1_D120": USDCAD_B5_E1_D120, "USDCAD_B5_E1_D30": USDCAD_B5_E1_D30, "USDCAD_B5_E1_D60": USDCAD_B5_E1_D60, "USDCAD_B5_E20_D120": USDCAD_B5_E20_D120, "USDCAD_B5_E20_D30": USDCAD_B5_E20_D30, "USDCAD_B5_E20_D60": USDCAD_B5_E20_D60, "USDCAD_B5_E5_D120": USDCAD_B5_E5_D120, "USDCAD_B5_E5_D30": USDCAD_B5_E5_D30, "USDCAD_B5_E5_D60": USDCAD_B5_E5_D60, "USDCAD_B32_E5_D30": USDCAD_B32_E5_D30, "USDCAD_B32_E5_D60": USDCAD_B32_E5_D60, "USDCAD_B32_E5_D120": USDCAD_B32_E5_D120}
#---------------------------------------------- IMAGES ----------------------------------------------#


def imageselect():
    img_name = dropDownVar.get()
    batch_size = dropDownVar1.get().strip("\t").strip()
    epochs = dropDownVar2.get().strip("\t").strip()
    days = dropDownVar3.get().strip("\t").strip()


    if img_name == "BTC Prediction":
        if batch_size == "Five":
            B = str(5)
        elif batch_size == "Ten":
            B = str(10)
        elif batch_size == "Sixteen":
            B = str(16)
        elif batch_size == "Thirty two":
            B = str(32)
        else:
            return
        
        if epochs == "One":
            E = str(1)
        elif epochs == "Five":
            E = str(5)
        elif epochs == "Twenty":
            E = str(20)
        elif epochs == "Hundred":
            E = str(100)
        else:
            return

        if days == "Thirty":
            D = str(30)
        elif days == "Sixty":
            D = str(60)
        elif days == "One Hundred Twenty":
            D = str(120)
        else:
            return
        code_frm.destroy()
        imagename = imageDict[f"BTC_B{B}_E{E}_D{D}"]
        grph_lbl.config(image = imagename, bg = "black")
        with open("./ChartViewer-Data/BTCprediction.txt", "r") as f:
            text = f.read()
            text = text[:118] + f"\nBATCH_SIZE = {B}\nEPOCHS = {E}\nDAYS = {D}\n\n" + text[118: ]
        code_txt.delete("1.0", tk.END)
        code_txt.insert("1.0", text)
    elif img_name == "USD/CAD Prediction":
        if batch_size == "Five":
            B = str(5)
        elif batch_size == "Ten":
            B = str(10)
        elif batch_size == "Sixteen":
            B = str(16)
        elif batch_size == "Thirty two":
            B = str(32)
        else:
            return
        
        if epochs == "One":
            E = str(1)
        elif epochs == "Five":
            E = str(5)
        elif epochs == "Twenty":
            E = str(20)
        elif epochs == "Hundred":
            E = str(100)
        else:
            return

        if days == "Thirty":
            D = str(30)
        elif days == "Sixty":
            D = str(60)
        elif days == "One Hundred Twenty":
            D = str(120)
        else:
            return
        code_frm.destroy()
        imagename = imageDict[f"USDCAD_B{B}_E{E}_D{D}"]
        grph_lbl.config(image = imagename, bg = "black")
        with open("./ChartViewer-Data/USDCADprediction.txt", "r") as f:
            text = f.read()
            text = text[:118] + f"\nBATCH_SIZE = {B}\nEPOCHS = {E}\nDAYS = {D}\n\n" + text[118: ]
        code_txt.delete("1.0", tk.END)
        code_txt.insert("1.0", text)
    else:
        return

title_frm = tk.Label(master = window, image = titleImage_photoImage, bg = "black")
title_frm.grid(row = 0, column = 0, sticky = "new", columnspan = 5, pady = 20)

dropDownList = ["BTC Prediction", "USD/CAD Prediction\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  "]
dropDownVar = tk.StringVar()
dropDownVar.set("Choose a Prediction")
opMenu = ttk.OptionMenu(window, dropDownVar, "Choose a prediction", *dropDownList, command = check)
opMenu.grid(row = 1, column = 0, padx = (2, 2), pady = 20, sticky = "ew")

dropDownList1 = ["Five\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  ", "Ten", "Sixteen", "Thirty two"]
dropDownVar1 = tk.StringVar()
dropDownVar1.set("0")
opMenu1 = ttk.OptionMenu(window, dropDownVar1, "Batch Size", *dropDownList1, command = check1)
opMenu1.grid(row = 1, column = 1, padx = (2, 2), pady = 20, sticky = "ew")

dropDownList2 = ["One\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ", "Five", "Twenty", "Hundred"]
dropDownVar2 = tk.StringVar()
dropDownVar2.set("0")
opMenu2 = ttk.OptionMenu(window, dropDownVar2, "Number of Epochs", *dropDownList2, command = check2)
opMenu2.grid(row = 1, column = 2, padx = (2, 2), pady = 20, sticky = "ew")

dropDownList3 = ["Thirty\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   ", "Sixty", "One Hundred Twenty"]
dropDownVar3 = tk.StringVar()
dropDownVar3.set("0")
opMenu3 = ttk.OptionMenu(window, dropDownVar3, "Number of Days", *dropDownList3, command = check3)
opMenu3.grid(row = 1, column = 3, padx = (2, 2), pady = 20, sticky = "ew")


grph_lbl = tk.Label(window, image = image0, bg = "black")
grph_lbl.grid(row = 2, column = 0, sticky = "nsew", pady = 20, padx = (2, 2), columnspan = 2)


code_txt = tk.Text(window, height = 26)
code_txt.grid(row = 2, column = 2, sticky = "nsew", padx = (2, 2), pady = 20, columnspan = 3)
with open("./ChartViewer-Data/testcode0.txt", "r") as f:
    text = f.read()
code_txt.delete("1.0", tk.END)
code_txt.insert("1.0", text)

code_frm = tk.Label(window, bg = "black", image = image_1)
code_frm.grid(row = 2, column = 2, sticky = "nsew", columnspan = 3, padx = (2, 2), pady = 20)



btn = tk.Button(window, text = "Submit", command = imageselect, font=("Helvetica", 15), bg = "red", fg = "white", relief = tk.FLAT)
btn.grid(row = 1, column = 4, padx = (2, 2), sticky = "ew")

window.mainloop()
