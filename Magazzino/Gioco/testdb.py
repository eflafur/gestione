from gestione.models import sp, ce,ivacliente,libro

import reportlab
from reportlab.pdfgen import canvas


    

class Pdf:
    def __init__(self,filename,pagesize=(595.27,841.89),bottomup = 1,pageCompression=0,verbosity=0,encrypt=None):
        self.filename=filename
    def Do(self):
        c=canvas.Canvas(self.filename)
        #c.drawString(100,100,"ciao a tutti")
        invoice=c.beginText(612,792)
        num=0
        x=0
        y=0
        while (num<10):
            invoice.textLine("adesso scrivo" +str(num))
            y+=10
            num+=1
        c.drawText(invoice)
        c.showPage()
        c.save()
        



    