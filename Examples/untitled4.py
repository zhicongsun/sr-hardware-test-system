# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:56:43 2020

@author: SZC
"""
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib import colors
elements = []
styles = getSampleStyleSheet()
doc = SimpleDocTemplate('test_table.pdf')
elements.append(Paragraph("SZC tests Table",styles['Title']))
data = [['Caves','WUm'],
        ['Deep ditch',50],
        ['Caves','WUm'],
        ['Deep ditch',50],
        ['Caves','WUm'],
        ['Deep ditch',50]]
ts = [('ALIGN',(1,1),(-1,-1),'CENTER'),
      ('LINEABOVE',(0,0),(-1,0),1,colors.purple),
      ('LINEBELOW',(0,0),(-1,0),1,colors.purple),
      ('FONT',(0,0),(-1,0),'Times-Bold'),
      ('LINEABOVE',(0,-1),(-1,-1),1,colors.purple),
      ('LINEBELOW',(0,-1),(-1,-1),0.5,colors.purple,1,None,None,4,1),
      ('LINEABOVE',(0,-1),(-1,-1),1,colors.red),
      ('FONT',(0,-1),(-1,-1),'Times-Bold')]
table = Table(data,style=ts)
elements.append(table)
doc.build(elements)