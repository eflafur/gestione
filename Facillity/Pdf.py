import reportlab,webbrowser
from reportlab.pdfgen import canvas

class PrintTable:
    def __init__(self,filename,line,pagesize=(595.27,841.89),bottomup = 1,pageCompression=0,verbosity=0,encrypt=None):
        self.filename=filename
        self.line=line
        self.c=canvas.Canvas(self.filename)
    def PrintArt(self):
        tot=0
        totp=0
        self.c.translate(0,500)
        self.c.setFont("Helvetica",10)
        x=0
        y=0
        self.c.drawString(10,20,"Codice")
        self.c.drawString(170,20,"Lotto")
        self.c.drawString(260,20,"Casse")
        self.c.drawString(310,20,"Peso")
        self.c.drawString(340,20,"Tara")
        self.c.drawString(380,20,"Prezzo")
        self.c.drawString(430,20,"Imponibile")
        self.c.drawString(490,20,"Iva")
        self.c.drawString(550,20,"Tot")
        for item in self.line:
            #for key in  item:
                #a=item[key]
            totp=round((item["iva"]+1)*(item["imp"]),2)
            self.c.drawString(10,y,str(item["cod"]))
            self.c.drawString(170,y,str(item["lotto"]))
            self.c.drawAlignedString(290,y,str(item["css"]),pivotChar=" ")
            self.c.drawAlignedString(330,y,str(item["ps"]),pivotChar=".")
            self.c.drawAlignedString(350,y,str(item["tara"]),pivotChar=".")
            self.c.drawAlignedString(400,y,str(item["prz"]),pivotChar=".")
            self.c.drawAlignedString(460,y,str(item["imp"]),pivotChar=".")
            self.c.drawAlignedString(500,y,str(item["iva"]),pivotChar=".")
            self.c.drawAlignedString(570,y,str(totp),pivotChar=".")
            tot+=item["imp"]*(item["iva"]+1)
            y-=20
        self.c.drawAlignedString(570,-400,"Tot   "+str(round(tot,2)),pivotChar=".")
        
    def PrintAna(self, nFattura=0, cln=None,lsddt=None):
        """ produce fattura in pdf """
        
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.colors import blue, black
        import time
    
        data=time.strftime("%d/%m/%Y")
        self.c.translate(0,-500)
    # scrive intestazione fattura
        self.c.setFont("Times-Roman",22)
        self.c.setFillColor(blue)
        self.c.drawString(400,800,self.filename)
        self.c.setFont("Times-Roman",10)
        self.c.setFillColor(black)
        self.c.drawString(400,770,self.filename+" N.")
        self.c.drawString(500,770,nFattura)
        self.c.drawString(400,755,"DATA")
        self.c.drawString(500,755,data)
    
    # scrive dati venditore'
        self.c.setFont("Times-Roman",14)
        self.c.setFillColor(blue)
        self.c.drawString(30,770,"Ortofrutta  F.V.")
        self.c.setFont("Times-Roman",10)
        self.c.setFillColor(black)
        self.c.drawString(30,750,'Posteggio 166 Padiglione C')
        self.c.drawString(30,735,'Milano')
        self.c.drawString(30,720,'0254019236')
        self.c.drawString(30,705,"P.I.")
        self.c.drawString(60,705,'06520750966')
        self.c.setFont("Times-Roman",12)
        self.c.setFillColor(black)
        self.c.drawString(30,660,"FATTURARE A")
    
    # scrive dati cliente'
        self.c.setFont("Times-Roman",14)
        self.c.setFillColor(blue)
        self.c.drawString(30,630,cln.azienda)
        self.c.setFont("Times-Roman",10)
        self.c.setFillColor(black)
        self.c.drawString(30,610,cln.indirizzo)
        self.c.drawString(30,595,"P.I.")
        self.c.drawString(60,595,cln.pi)
        if(lsddt is not None):
            self.c.drawString(10,560,"Rif.  "+lsddt)

        self.c.showPage()
        self.c.save()
        webbrowser.open_new(self.filename)
