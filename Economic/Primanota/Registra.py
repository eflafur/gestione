from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo,Carico,trasporto,sp,ce
from decimal import Decimal
from django.db.models import Q,F
import openpyxl,time,os,subprocess,datetime
from datetime import datetime,timedelta,date
        
        
      
class Clienti:
    def __init__(self,imp,erario,cod,pg):
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.pg=pg
        self.put(self.imp,self.erario,self.cod,self.pg)
        
    def put(self,imp,erario,cod,pg):
        s=sp.objects.all()
        cl=s.get(cod=cod)
        iva=s.get(cod="20.20")
        cl.attivo+=imp+erario
        iva.passivo+=erario
        cl.save()
        iva.save()
        if(pg==0):
            cs=s.get(cod="1.1")
            cs.attivo+=imp+erario
            cs.save()
            cl.passivo+=imp+erario
            cl.save()
            rc=ce.objects.get(cod="80.80")
            rc.ricavi+=imp
            rc.save()
        return (1)

class Fornitori:
    def __init__(self,imp,erario,cod):
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.put(self.imp,self.erario,self.cod)
        
    def put(self,imp,erario,cod):
        s=sp.objects.all()
        rc=ce.objects.get(cod="72.72")
        fr=s.get(cod=cod)
        cs=s.get(cod="1.1")
        iva=s.get(cod="20.20")
        fr.passivo+=imp+erario
        iva.attivo+=erario
        cs.passivo+=imp+erario
        rc.costi+=imp
        fr.attivo+=imp+erario
        fr.save()
        cs.save()
        iva.save()
        rc.save()
        return (1)

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
        