from gestione.models import sp, ce,ivacliente,libro
import reportlab,webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4,inch
from reportlab.lib.colors import pink, black, red, blue, green
    

class Pdf:
    def __init__(self,filename,pagesize=A4,bottomup = 1,pageCompression=0,verbosity=0,encrypt=None):
        self.filename=filename
        self.size=pagesize
    def Do(self):
        
        c=canvas.Canvas(self.filename,pagesize=A4)
        c.translate(0,800)
        c.setFont("Helvetica",10)
   
        c.drawString(0,0,"flaviotrr")
        c.drawAlignedString(150,0,"1254543.44456",pivotChar=".")
        c.drawString(250,0,"33 801 1234 ")
        c.drawAlignedString(350,0,"1234.4566",pivotChar=".")
#        c.drawAlignedString(150,0,"12343.45654",pivotChar=".")

        c.drawString(0,-20,"piuu")
        c.drawAlignedString(150,-20,"123.45",pivotChar=".")
        c.drawString(250,-20,"801 134 ")
        c.drawAlignedString(350,-20,"123.45",pivotChar=".")
        #c.drawAlignedString(100,-20,"1.4",pivotChar=".")
        #c.drawAlignedString(1500,-20,"12.45",pivotChar=".")


        #c.line(120,700,580,700)
        #c.drawString(595, 842, "H")
        #while (num<30):
            #c.setFont("Helvetica", size)
            #c.drawString(x,y, "adesso scrivo "+str(num))
            #y-=10
            #num+=1
            #size+=1

            

        x=0
        y=0
        size=10
        invoice=c.beginText(x,y)
        invoice.setFont("Helvetica",size)
        num=0


        while (num<3):
            #invoice.setCharSpace(num)
            #invoice.setWordSpace(num)
            #invoice.setLeading(num+4)
            #invoice.textLine("adesso scrivo" +str(num))
            invoice.textOut("adesso scrivo" +str(num))
            invoice.moveCursor(100,0)
            num+=1
        #c.setFont("Courier", 60)
        c.setFillColorRGB(1, 0, 0)
        #c.drawCentredString(letter[0] / 2, inch * 6, "CLASSIFIED")
#        c.drawText(invoice)
        c.showPage()
        c.save()
        webbrowser.open_new("floppolo.pdf")

        



    