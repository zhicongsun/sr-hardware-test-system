import barcode
from barcode.writer import ImageWriter


#生成一维码的类型的种类
"""
[u'code39', u'code128', u'ean', u'ean13', u'ean8', u'gs1', u'gtin',
 u'isbn', u'isbn10', u'isbn13', u'issn', u'jan', u'pzn', u'upc', u'upca']
"""

#生成一维码，参数:码类型、码内容、文件名(文件名后缀自动加.png)
def barcode_to_png(barcode_type,text_str,filename):
    EAN = barcode.get_barcode_class(barcode_type) #设置生成一维码的类型
    ean = EAN(text_str, writer=ImageWriter())
    ean.save(filename)
if __name__ == "__main__":
    code_type = "code128"
    barcode_to_png(code_type,"20200807T001","./sncode/ddd")