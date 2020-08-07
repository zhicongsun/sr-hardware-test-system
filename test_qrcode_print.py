# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:30:13 2020

@author: SZC
"""

import win32print
import win32ui
from PIL import Image, ImageWin,ImageDraw,ImageFont
import qrcode
import os

def print_barcode(imgname):
    img = qrcode.make(imgname)
    img_path = os.getcwd() + "/barcode/" + imgname + ".png"
    img.save(img_path)

    ttfont = ImageFont.truetype("msyh.ttf",20) 
    im = Image.open(img_path)
    draw = ImageDraw.Draw(im)
    draw.text((35,250),imgname, fill="#000000",font=ttfont)
    im.save(img_path)

    #
    # Constants for GetDeviceCaps
    #
    #
    # HORZRES / VERTRES = printable area
    #
    HORZRES = 10
    VERTRES = 10#10
    #
    # LOGPIXELS = dots per inch
    #
    LOGPIXELSX = 100
    LOGPIXELSY = 100
    #
    # PHYSICALWIDTH/HEIGHT = total area
    #
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 110#111
    #
    # PHYSICALOFFSETX/Y = left / top margin
    #
    PHYSICALOFFSETX = 112
    PHYSICALOFFSETY = 112#113
    
    printer_name = win32print.GetDefaultPrinter ()
    file_name = img_path
    
    #
    # You can only write a Device-independent bitmap
    #  directly to a Windows device context; therefore
    #  we need (for ease) to use the Python Imaging
    #  Library to manipulate the image.
    #
    # Create a device context from a named printer
    #  and assess the printable size of the paper.
    #
    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
    print(printable_area)
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
    print(printer_size)
    printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)
    print(printer_margins)
    #
    # Open the image, rotate it if it's wider than
    #  it is high, and work out how much to multiply
    #  each pixel by to get it as big as possible on
    #  the page without distorting.
    #
    bmp = Image.open (file_name)
    if bmp.size[0] > bmp.size[1]:
      bmp = bmp.rotate (90)
    
    print(bmp.size[0])
    print(bmp.size[1])
    ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
    scale = min (ratios)
    
    #
    # Start the print job, and draw the bitmap to
    #  the printer device at the scaled size.
    #
    hDC.StartDoc (file_name)
    hDC.StartPage ()
    
    dib = ImageWin.Dib (bmp)
    scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
    print(scaled_width)
    print(scaled_height)
    scaled_width = int(scaled_width/3)
    scaled_height = int(scaled_height/3)
    # x1 = int ((printer_size[0] - scaled_width) / 3)+100
    # y1 = int ((printer_size[1] - scaled_height) / 3)
    x1 = int ((printer_size[0] - scaled_width) / 2)
    y1 = int ((printer_size[1] - scaled_height) / 2)
    x2 = x1 + scaled_width
    y2 = y1 + scaled_height
    print(x1)
    print(y1)
    dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))

    hDC.EndPage ()
    hDC.EndDoc ()
    hDC.DeleteDC ()
    

if __name__ == "__main__":
    imgname = "20200803001"
    print_barcode(imgname)

