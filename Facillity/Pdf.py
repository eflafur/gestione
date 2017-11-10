import reportlab
from reportlab.pdfgen import canvas

class PrintTable:
    def __init__(self,filename,line,pagesize=(595.27,841.89),bottomup = 1,pageCompression=0,verbosity=0,encrypt=None):
        self.filename=filename
        self.line=line
    def Do(self):
        c=canvas.Canvas(self.filename)
        #c.drawString(100,100,"ciao a tutti")
        invoice=c.beginText(600,800)
        x=0
        y=0
        for item in self.line:
            for key in  item:
                a=item[key]
                invoice.textLine(a)
        c.drawText(invoice)
        c.showPage()
        c.save()