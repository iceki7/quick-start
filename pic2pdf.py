import os
import img2pdf
# from pdf2image import convert_from_path
import sys
# from PyPDF2 import PdfReader


predir=r"D:\ustb78\【Sync】\pro\教材\教改编译结题相关\教改编译结题相关\参考资料\\"

aa = [predir+r"962bd40735fae6cd7b89dbc98afe182442a7d933a14c.jpg"]
aa = [predir+r"img9.jpg"]
aa = [predir+r"scale.jpg"]


imagelist = aa[:]

with open(predir+"scale-目录.pdf",'wb') as f:
    img2pdf.rotation=img2pdf.Rotation.ifvalid
    f.write(img2pdf.convert(imagelist))






