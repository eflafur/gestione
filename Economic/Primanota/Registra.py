from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo,Carico,trasporto,sp,ce
from decimal import Decimal
from django.db.models import Q,F
import openpyxl,time,os,subprocess,datetime
from datetime import datetime,timedelta,date

class Model:
    def __init__(self,ddt,cod,q,prezzo,data,lotto,cassa,iva):
        self.ddt=ddt
        self.cod=cod
        self.q=q
        self.prezzo=prezzo
        self.data=data
        self.lotto=lotto
        self.cassa=cassa
        self.iva=iva
        
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
