# add watermark

with open('wtr.pdf', 'rb') as f:
    watermark = PyPDF2.PdfFileReader(f)
    with open('twopage.pdf', 'rb') as f2:
        file_to_watermark = PyPDF2.PdfFileReader(f2)
        output = PyPDF2.PdfFileWriter()
        for i in range(file_to_watermark.getNumPages()):
            page = file_to_watermark.getPage(i)
            page.mergePage(watermark.getPage(0))
            output.addPage(page)
            
            with open('output_watermarked.pdf', 'wb') as f3:
                output.write(f3)
