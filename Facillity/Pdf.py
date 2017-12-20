import reportlab,webbrowser
from reportlab.pdfgen import canvas
from decimal import Decimal
import webbrowser
#stampa OO

#class hdlPdf (object):
    #""" superclasse gestione documenti pdf """

    #def buildPdf(self):
        #from reportlab.pdfgen import canvas

        #docu=canvas.Canvas(self.nomePdf,self.pagesize)

        #for el in self.pdfbody:
            #if el[0]=="txt":
                #docu.setFont(el[4],el[3])
                #docu.setFillColor(el[5])
                #docu.drawString(el[1],el[2],str(el[6]))
                #docu.drawAlignedString(el[1],el[2],str(el[6]),pivotChar=".")  #drawString(el[1],el[2],str(el[6]))
            #elif el[0]=="lin":
                #docu.setStrokeColor(el[5])
                #docu.line(el[1],el[2],el[3],el[4])
            #elif el[0]=="ret":
                #docu.setFillColorCMYK(el[5][0],el[5][1],el[5][2],el[6])
                #docu.rect(el[1],el[2],el[3],el[4],0,1)

        #docu.showPage()
        #docu.save()
        #webbrowser.open_new(self.nomePdf)

    #def savePdf(self,nFattura):
        #""" archivia documento pdf in folder """

    #def stampaPdf(self,nFattura):
        #""" invia documento pdf a stampante """


#class fattura (hdlPdf):
    #""" classe gestione documenti di fatturazione """

    #def __init__ (self,venditore={}, nFattura=0, cln=None, righeFattura={}):
        #from reportlab.lib.colors import blue, black
        #from reportlab.lib.pagesizes import A4
        #import time

        #self.nomePdf="Fattura-"+str(nFattura)+str(time.strftime("%Y"))+"-"+cln.azienda+".pdf"
        #self.pagesize=A4
        #sizemedium=6

        #self.pdfbody=[]
## write title in pdf body
        #self.pdfbody.append(["txt",400,800,22,"Times-Roman",blue,"FATTURA"])
        #self.pdfbody.append(["txt",400,770,sizemedium,"Times-Roman",black,"FATTURA N."])
        #self.pdfbody.append(["txt",500,770,sizemedium,"Times-Roman",black,nFattura])
        #self.pdfbody.append(["txt",400,755,sizemedium,"Times-Roman",black,"DATA"])
        #self.pdfbody.append(["txt",500,755,sizemedium,"Times-Roman",black,time.strftime("%d/%m/%Y")])

## append vendor data in pdf body
        #self.pdfbody.append(["txt",30,770,sizemedium,"Times-Roman",blue,venditore['venditore']])
        #self.pdfbody.append(["txt",30,750,sizemedium,"Times-Roman",black,venditore['indirizzo']])
        #self.pdfbody.append(["txt",30,735,sizemedium,"Times-Roman",black,venditore['città']])
        #self.pdfbody.append(["txt",30,720,sizemedium,"Times-Roman",black,venditore['telefono']])
        #self.pdfbody.append(["txt",30,705,sizemedium,"Times-Roman",black,"P.I."])
        #self.pdfbody.append(["txt",60,705,sizemedium,"Times-Roman",black,venditore['P-IVA']])

## append client data in pdf body
        #self.pdfbody.append(["txt",30,660,12,"Times-Roman",black,"FATTURARE A"])
        #self.pdfbody.append(["txt",30,630,14,"Times-Roman",blue,cln.azienda])
        #self.pdfbody.append(["txt",30,610,10,"Times-Roman",black,cln.indirizzo])
        #self.pdfbody.append(["txt",30,595,10,"Times-Roman",black,"P.I."])
        #self.pdfbody.append(["txt",60,595,10,"Times-Roman",black,cln.pi])

## append list of articles in pdf body

## titles
        #self.pdfbody.append(["lin",10,470,580,470,black])

        #xcoord=10
        #ycoord=450
        #self.pdfbody.append(["txt",10,ycoord,12,"Times-Roman",black,"CODICE"])
        #self.pdfbody.append(["txt",160,ycoord,12,"Times-Roman",black,"LOTTO"])
        #self.pdfbody.append(["txt",210,ycoord,12,"Times-Roman",black,"CASSE"])
        #self.pdfbody.append(["txt",260,ycoord,12,"Times-Roman",black,"PESO"])
        #self.pdfbody.append(["txt",310,ycoord,12,"Times-Roman",black,"TARA"])
        #self.pdfbody.append(["txt",360,ycoord,12,"Times-Roman",black,"PREZZO"])
        #self.pdfbody.append(["txt",410,ycoord,12,"Times-Roman",black,"IMP"])
        #self.pdfbody.append(["txt",470,ycoord,12,"Times-Roman",black,"IVA"])
        #self.pdfbody.append(["txt",520,ycoord,12,"Times-Roman",black,"TOTALE"])

        #self.pdfbody.append(["lin",10,440,580,440,black])
## data
        #rowGap=30                   # gap between rows
        #ycoord-=rowGap
        #total=0
        #color=[0.1, 0.0, 0.0]         # colore blu chiaro in formato Cyan, Magenta, Yellow
        #fill=0.1                    # opacita'
        #for el in righeFattura:
            #if fill==0.1:           # campitura righe alternate
                #self.pdfbody.append(["ret",10,ycoord-12,580,rowGap,color,fill])
                #fill=0.0
            #else:
                #fill=0.1
            #self.pdfbody.append(["txt",10,ycoord,sizemedium,"Times-Roman",black,el["cod"]])
            #self.pdfbody.append(["txt",160,ycoord,sizemedium,"Times-Roman",black,el["lotto"]])
            #self.pdfbody.append(["txt",210,ycoord,sizemedium,"Times-Roman",black,el["css"]])
            #self.pdfbody.append(["txt",260,ycoord,sizemedium,"Times-Roman",black,el["ps"]])
            #self.pdfbody.append(["txt",310,ycoord,sizemedium,"Times-Roman",black,el["tara"]])
            #self.pdfbody.append(["txt",360,ycoord,sizemedium,"Times-Roman",black,el["prz"]])
            #self.pdfbody.append(["txt",410,ycoord,sizemedium,"Times-Roman",black,el["imp"]])
            #self.pdfbody.append(["txt",470,ycoord,sizemedium,"Times-Roman",black,el["iva"]])
            #self.pdfbody.append(["txt",520,ycoord,sizemedium,"Times-Roman",black,el["ps"]*el["prz"]])
            #total+=el["ps"]*el["prz"]
            #ycoord-=rowGap

        #ycoord-=rowGap
        #self.pdfbody.append(["txt",430,ycoord,12,"Times-Roman",black,"TOTALE"])
        #self.pdfbody.append(["txt",520,ycoord,12,"Times-Roman",black,total])


#stampa procedurale

class PrintTable:
    def __init__(self,filename,line,tot,pagesize=(595.27,841.89),bottomup = 1,pageCompression=0,verbosity=0,encrypt=None):
        self.filename=filename
        self.line=line
        self.c=canvas.Canvas(self.filename)
        self.tot=str(tot)
    def PrintArt(self):
        tot=0
        totp=0
        self.c.translate(0,500)
        self.c.setFont("Helvetica",8)
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
        self.c.drawString(30,610,cln.indirizzo+" "+cln.citta)
        self.c.drawString(30,595,"P.I.")
        self.c.drawString(60,595,cln.pi)
        self.c.drawString(30,570,"Da pagare: "+self.tot)
        if(lsddt is not None):
            self.c.drawString(30,550,"Rif.  "+lsddt)
        self.c.showPage()
        self.c.save()
        webbrowser.open_new(self.filename)


    def PrintCV(self):
        tot=0
        totp=0
        self.c.translate(0,500)
        self.c.setFont("Helvetica",10)
        x=0
        y=0
        self.c.drawString(10,20,"Lotto")
        self.c.drawString(170,20,"Codice")
        self.c.drawString(260,20,"Casse")
        self.c.drawString(310,20,"Peso")
        if(self.filename!="CV"):
            self.c.drawString(340,20,"Tara")
        self.c.drawString(380,20,"Prezzo")
        self.c.drawString(430,20,"Imponibile")
        self.c.drawString(490,20,"Iva")
        self.c.drawString(550,20,"Tot")
        for item in self.line:
            imp=item["prz"]*item["ps"]
            self.c.drawString(10,y,str(item["lotto"]))
            self.c.drawString(100,y,str(item["cod"]))
            self.c.drawAlignedString(290,y,str(item["css"]),pivotChar=" ")
            self.c.drawAlignedString(330,y,str(item["ps"]),pivotChar=".")
#            self.c.drawAlignedString(350,y,str(item["tara"]),pivotChar=".")
            self.c.drawAlignedString(400,y,str(item["prz"]),pivotChar=".")
            self.c.drawAlignedString(460,y,str(item["costo"]),pivotChar=".")
            self.c.drawAlignedString(500,y,str(item["iva"]),pivotChar=".")
            self.c.drawAlignedString(570,y,str(Decimal(item["costo"])*(item["iva"]+1)),pivotChar=".")
            tot+=Decimal(item["costo"])*(item["iva"]+1)
            y-=20
        self.c.drawAlignedString(570,-400,"Tot   "+str(round(tot,2)),pivotChar=".")