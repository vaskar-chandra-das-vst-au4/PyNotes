import os
from pypdf import PdfWriter

files = [file for file in os.listdir() if file.endswith(".pdf")]
merger = PdfWriter()
for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
# print("append" in dir(merger))
