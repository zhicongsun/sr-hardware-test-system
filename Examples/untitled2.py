# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:31:40 2020

@author: Wenfei
"""


from reportlab.pdfgen import canvas
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def hello(c):
    pdfmetrics.registerFont(TTFont('micro', 'msyh.ttf'))
    c.setFont('micro', 32)
    somestring = "你是猪"
    somestring += "哈哈哈"
    c.drawString(50,50,somestring)
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()