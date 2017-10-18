from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo,Carico,trasporto,sp,ce
from decimal import Decimal
from django.db.models import Q,F
import openpyxl,time,os,subprocess,datetime
from datetime import datetime,timedelta,date

        
class Clienti:
    def __init__(self,imp,erario,cod):
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.put(self.imp,self.erario,self.cod)
        
    def put(self,imp,erario,cod):
        s=sp.objects.all()
        rc=ce.objects.get(cod="80.80")
        cl=s.get(cod=cod)
        cs=s.get(cod="1.1")
        iva=s.get(cod="20.20")
        cl.attivo+=imp+erario
        iva.passivo+=erario
        cs.attivo+=imp+erario
        rc.ricavi+=imp
        cl.passivo+=imp+erario
        cl.save()
        cs.save()
        iva.save()
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
        a=imp+erario
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
