import os
from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1= PdfFileReader(open("1.pdf", "rb"))

#output.addPage(input1.getPage(0))
#output.addPage(input1.getPage(1))


for i in xrange(0,2):
	output.addPage(input1.getPage(i)) 

"""
for x in xrange(7,28):
	output.addPage(input1.getPage(x))
"""

#3
#or y in xrange(13,input1.getNumPages()):
#output.addPage(input1.getPage(y))


outputStream = file("2.pdf", "wb")
output.write(outputStream)