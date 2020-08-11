# -*- coding: utf-8 -*-
# """
# Created on Mon Jul 27 09:30:13 2020

# @author: SZC
# """
# import win32print
# import win32ui
# from PIL import Image, ImageWin,ImageDraw,ImageFont
# import qrcode
# import os
# # SN码使用
# import barcode
# from barcode.writer import ImageWriter

# def print_barcode(imgname,pcb_type):
#     """打印二维码函数
    
#     从官方的print库修改过来，可支持大部分打印机机型，功能是生成二维码图片并保存在barcode文件夹，接着调用打印机打印该二维码图片
#     """
#     global pcb_data
#     # 如果控制板测试通过，打印SN码
#     if pcb_type == "True":
#         EAN = barcode.get_barcode_class("code128") #设置生成一维码的类型
#         ean = EAN(imgname, writer=ImageWriter())
#         img_path = os.getcwd() + "/sncode/" + imgname # 这里的路径不用自己加.png，因为EAN的save函数的特性决定的
#         ean.save(img_path,
#         {'dpi':600,'text_distance':1.0,'font_size':20}) 
#         # 向SN码的顶部加入信息
#         ttfont = ImageFont.truetype("msyh.ttf",20) 
#         img_path = img_path + ".png"
#         im = Image.open(img_path)
#         draw = ImageDraw.Draw(im)
#         draw.text((300,0),"EU200测试", fill="#000000",font=ttfont)
#         im.save(img_path)
#     # 控制板测试不通过，打印二维码
#     else:
#         # 生成二维码并保存在barcode文件夹，以imgname.png命名
#         img = qrcode.make(imgname)
#         img_path = os.getcwd() + "/barcode/" + imgname + ".png"
#         img.save(img_path)
#         #向二维码图片的底端中加入imgname的文字，再次保存覆盖原文件
#         ttfont = ImageFont.truetype("msyh.ttf",20) 
#         im = Image.open(img_path)
#         draw = ImageDraw.Draw(im)
#         draw.text((35,250),imgname, fill="#000000",font=ttfont)
#         draw.text((85,0),pcb_data[0]['task_name'], fill="#000000",font=ttfont)
#         im.save(img_path)
    
#     # HORZRES / VERTRES 代表可打印的区域，给GetDeviceCaps用
#     HORZRES = 8
#     VERTRES = 8#10
#     # 每英寸点数，即精度
#     LOGPIXELSX = 200 #88
#     LOGPIXELSY = 200 #90
#     # 物理宽度和高度
#     PHYSICALWIDTH = 110
#     PHYSICALHEIGHT = 110#111
#     # 左边距和顶端边距
#     PHYSICALOFFSETX = 112
#     PHYSICALOFFSETY = 112#113
    
#     printer_name = win32print.GetDefaultPrinter () # 获取已连接的打印机的名字
#     if pcb_type == "True":
#         file_name = img_path
#     else:
#         file_name = img_path
#         pass
    
#     # 可以将不依赖于设备的位图bitmap直接写入设备，因此需要使用Imaging库来生成image
#     # 从已连接的打印机获取设备信息，得到可以打印的标签的大小
#     hDC = win32ui.CreateDC ()
#     hDC.CreatePrinterDC (printer_name)
#     printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES) # 获取可打印的区域
#     print(printable_area)
#     printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT) # 获取打印的大小
#     print(printer_size) 
#     printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY) # 获取打印的位置
#     print(printer_margins)
#     # 打开图像，如果宽度大于高度，则乘以一个比例，尽量不失真
#     bmp = Image.open (file_name)
#     # 按比例放大图像
#     ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
#     scale = min (ratios)

#     #开始打印工作，将图片按照刚才的scaled size去打印
#     hDC.StartDoc (file_name)
#     hDC.StartPage ()
    
#     dib = ImageWin.Dib (bmp)
#     scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
#     scaled_width = int(scaled_width/6)
#     scaled_height = int(scaled_height/6)
#     x1 = int ((printer_size[0] - scaled_width) / 2)
#     y1 = int ((printer_size[1] - scaled_height) / 2)+100 # 100为后续调整的数据，测试值 
#     x2 = x1 + scaled_width
#     y2 = y1 + scaled_height
#     dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))
#     hDC.EndPage ()
#     hDC.EndDoc ()
#     hDC.DeleteDC ()


# if __name__ == "__main__":
#     imgname = "20200811T004"
#     print_barcode(imgname,"True")

# import win32print
# import win32ui
# from PIL import Image, ImageWin

# #
# # Constants for GetDeviceCaps
# #
# #
# # HORZRES / VERTRES = printable area
# #
# HORZRES = 10#234#8
# VERTRES = 10#10
# #
# # LOGPIXELS = dots per inch
# #
# LOGPIXELSX = 100
# LOGPIXELSY = 100
# #
# # PHYSICALWIDTH/HEIGHT = total area
# #
# PHYSICALWIDTH = 234#110
# PHYSICALHEIGHT = 39#111
# #
# # PHYSICALOFFSETX/Y = left / top margin
# #
# PHYSICALOFFSETX = 112
# PHYSICALOFFSETY = 113

# printer_name = win32print.GetDefaultPrinter ()
# file_name = "test.png"

# #
# # You can only write a Device-independent bitmap
# #  directly to a Windows device context; therefore
# #  we need (for ease) to use the Python Imaging
# #  Library to manipulate the image.
# #
# # Create a device context from a named printer
# #  and assess the printable size of the paper.
# #
# hDC = win32ui.CreateDC ()
# hDC.CreatePrinterDC (printer_name)
# printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
# print(printable_area)
# printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
# print(printer_size)
# printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)
# print(printer_margins)
# #
# # Open the image, rotate it if it's wider than
# #  it is high, and work out how much to multiply
# #  each pixel by to get it as big as possible on
# #  the page without distorting.
# #
# bmp = Image.open (file_name)
# # if bmp.size[0] > bmp.size[1]:
# #   bmp = bmp.rotate (90)
# print(bmp.size[0])
# print(bmp.size[1])
# print(printer_size[0])
# print(printer_size[1])
# ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
# ratios = [1.0 * 1200 / bmp.size[0], 1.0 * 200 / bmp.size[1]]
# scale = min (ratios)

# #
# # Start the print job, and draw the bitmap to
# #  the printer device at the scaled size.
# #
# hDC.StartDoc (file_name)
# hDC.StartPage ()

# dib = ImageWin.Dib (bmp)
# scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
# # x1 = int ((printer_size[0] - scaled_width) / 2)
# # y1 = int ((printer_size[1] - scaled_height) / 2)
# scaled_width =  int (scaled_width/2)
# scaled_height = int (scaled_height/2)
# # x1 = int ((1200 - scaled_width) / 2)
# # y1 = int ((200 - scaled_height) / 2)+100
# x1 =0
# y1=0
# x2 = x1 + scaled_width*2
# y2 = y1 + scaled_height
# dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))

# hDC.EndPage ()
# hDC.EndDoc ()
# hDC.DeleteDC ()

# import win32print
# import win32ui
# from PIL import Image, ImageWin

# #
# # Constants for GetDeviceCaps
# #
# #
# # HORZRES / VERTRES = printable area
# #
# HORZRES = 8
# VERTRES = 10
# #
# # LOGPIXELS = dots per inch
# #
# LOGPIXELSX = 88
# LOGPIXELSY = 90
# #
# # PHYSICALWIDTH/HEIGHT = total area
# #
# PHYSICALWIDTH = 110
# PHYSICALHEIGHT = 111
# #
# # PHYSICALOFFSETX/Y = left / top margin
# #
# PHYSICALOFFSETX = 112
# PHYSICALOFFSETY = 113

# printer_name = win32print.GetDefaultPrinter ()
# file_name = "test.png"

# #
# # You can only write a Device-independent bitmap
# #  directly to a Windows device context; therefore
# #  we need (for ease) to use the Python Imaging
# #  Library to manipulate the image.
# #
# # Create a device context from a named printer
# #  and assess the printable size of the paper.
# #
# hDC = win32ui.CreateDC ()
# hDC.CreatePrinterDC (printer_name)
# printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
# printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
# printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)
# print(printable_area)
# print(printer_size)
# print(printer_margins)
# #
# # Open the image, rotate it if it's wider than
# #  it is high, and work out how much to multiply
# #  each pixel by to get it as big as possible on
# #  the page without distorting.
# #
# bmp = Image.open (file_name)
# # if bmp.size[0] > bmp.size[1]:
# #   bmp = bmp.rotate (90)

# ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
# scale = min (ratios)

# #
# # Start the print job, and draw the bitmap to
# #  the printer device at the scaled size.
# #
# hDC.StartDoc (file_name)
# hDC.StartPage ()

# dib = ImageWin.Dib (bmp)
# scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
# x1 = int ((printer_size[0] - scaled_width) / 2)
# y1 = int ((printer_size[1] - scaled_height) / 2)
# x2 = x1 + scaled_width
# y2 = y1 + scaled_height
# print(x1,x2,y1,y2)
# dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))

# hDC.EndPage ()
# hDC.EndDoc ()
# hDC.DeleteDC ()

import win32print
import win32ui
from PIL import Image, ImageWin,ImageDraw,ImageFont
import qrcode
import os
# SN码使用
import barcode
from barcode.writer import ImageWriter

def print_barcode(imgname,pcb_type):
    """打印二维码函数
    
    从官方的print库修改过来，可支持大部分打印机机型，功能是生成二维码图片并保存在barcode文件夹，接着调用打印机打印该二维码图片
    """
    global pcb_data
    # 如果控制板测试通过，打印SN码
    if pcb_type == "True":
        EAN = barcode.get_barcode_class("code128") #设置生成一维码的类型
        ean = EAN(imgname, writer=ImageWriter())
        img_path = os.getcwd() + "/sncode/" + imgname # 这里的路径不用自己加.png，因为EAN的save函数的特性决定的
        ean.save(img_path,
        {'dpi':1000,'text_distance':1.0,'font_size':20}) 
        # 向SN码的顶部加入信息
        ttfont = ImageFont.truetype("msyh.ttf",120) 
        img_path = img_path + ".png"
        im = Image.open(img_path)
        width = im.size[0]
        hight = im.size[1]
         # 创建空白图片
        target = Image.new('RGBA', (width+504, hight), (255, 255, 255))

        # 创建header Image对象，paste拼接到空白图片指定位置target.paste(img_h, (0, 0))
        # img_h = img_header(os.path.join(img_path, imgname))
        # 图片合成paste 参数中img_h表示Image对象，(0, 0)表示x,y轴位置 单位像素 target的左上角为原点 y轴向下 
        target.paste(im, (0, 0))
        # target.show()
        draw = ImageDraw.Draw(target)
        draw.text((width+20,20),"EU200", fill="#000000",font=ttfont)
        draw.text((width+20,hight/3),"合格", fill="#000000",font=ttfont)
        draw.text((width+20,hight/3*2),imgname, fill="#000000",font=ttfont)
        target.save(img_path)
        # draw = ImageDraw.Draw(im)
        # draw.text((300,0),"EU200", fill="#000000",font=ttfont)
        # im.save(img_path)
    # 控制板测试不通过，打印二维码
    else:
        # 生成二维码并保存在barcode文件夹，以imgname.png命名
        img = qrcode.make(imgname)
        img_path = os.getcwd() + "/barcode/" + imgname + ".png"
        img.save(img_path)
        #向二维码图片的底端中加入imgname的文字，再次保存覆盖原文件
        ttfont = ImageFont.truetype("msyh.ttf",20) 
        im = Image.open(img_path)
        draw = ImageDraw.Draw(im)
        draw.text((35,250),imgname, fill="#000000",font=ttfont)
        draw.text((85,0),pcb_data[0]['task_name'], fill="#000000",font=ttfont)
        im.save(img_path)
    
    # HORZRES / VERTRES 代表可打印的区域，给GetDeviceCaps用
    HORZRES = 8
    VERTRES = 10
    # 每英寸点数，即精度
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    # 物理宽度和高度
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 111
    # 左边距和顶端边距
    PHYSICALOFFSETX = 112
    PHYSICALOFFSETY = 113
    
    printer_name = win32print.GetDefaultPrinter () # 获取已连接的打印机的名字
    if pcb_type == "True":
        file_name = img_path
    else:
        file_name = img_path
        pass
    
    # 可以将不依赖于设备的位图bitmap直接写入设备，因此需要使用Imaging库来生成image
    # 从已连接的打印机获取设备信息，得到可以打印的标签的大小
    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES) # 获取可打印的区域
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT) # 获取打印的大小 
    printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY) # 获取打印的位置

    # 打开图像，如果宽度大于高度，则乘以一个比例，尽量不失真
    bmp = Image.open (file_name)
    # 按比例放大图像
    ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
    scale = min (ratios)

    # 开始打印工作，将图片按照刚才的scaled size去打印
    hDC.StartDoc (file_name)
    hDC.StartPage ()
    
    dib = ImageWin.Dib (bmp)
    scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
    scaled_width = scaled_width*3
    # x1 = int ((printer_size[0] - scaled_width) / 2)
    x1 = 0
    y1 = int ((printer_size[1] - scaled_height) / 2) # 100为后续调整的数据，测试值 
    x2 = x1 + scaled_width
    y2 = y1 + scaled_height
    dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))
    hDC.EndPage ()
    hDC.EndDoc ()
    hDC.DeleteDC ()

if __name__ == "__main__":
    imgname = "20200811T0005"
    print_barcode(imgname,"True")