from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo,Carico,trasporto,sp,ce,ivacliente
from decimal import Decimal
from django.db.models import Q,F
import openpyxl,time,os,subprocess,datetime
from datetime import datetime,timedelta,date
        

class Commercio:
    def __init__(self,imp,erario,cod,pg,cl,fatt):
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.pg=pg
        self.cl=cl
        self.fatt=fatt
        self.s=sp.objects.all()
        self.cl=self.s.get(cod=cod)
        self.iva=self.s.get(cod="20.20")
    def Vendita(self):
        self.cl.attivo+=self.imp+self.erario
        self.iva.passivo+=self.erario
        rc=ce.objects.get(cod="80.80")
        rc.ricavi+=self.imp
        self.cl.save()
        self.iva.save()
        rc.save()
        if(self.pg==0):
            cs=self.s.get(cod="1.1")
            cs.attivo+=self.imp+erario
            cs.save()
    def Acquisto(self):
        self.cl.passivo+=self.imp+self.erario
        self.iva.attivo+=self.erario
        rc=ce.objects.get(cod="72.72")
        rc.costi+=self.imp
        self.cl.save()
        self.iva.save()
        rc.save()
        if(self.pg==1):
            cs=self.s.get(cod="1.1")
            cs.passivo+=self.imp+self.erario
            cs.save()
        
    def SetErarioCliente(self):
        rec=ivacliente.objects.latest("id")
        res=ivacliente(prot=rec.prot+1,fatt=self.fatt,nome=self.cl,tot=self.imp+self.erario,imp=self.imp,erario=self.erario)
        res.save()   

class Clienti(Commercio):
    pass
class Fornitore(Commercio):
    pass





    
    
    
class Banca:
    def __init__(self,imp,erario,cod,sgn):
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.sgn=sgn
        self.put(self.imp,self.erario,self.cod,self.sgn)
        
    def put(self,imp,erario,cod,sgn):
        bc=sp.objects.get(cod="1.2")
        if(sgn==0):
            bc.attivo+=imp+erario
            rc=ce.objects.get(cod="80.80")
            rc.ricavi+=imp
            rc.save()
            cl=sp.objects.get(cod="3.1")
            cl.passivo+=imp+erario
            cl.save()
        else:
            bc.passivo+=imp
        bc.save()
        