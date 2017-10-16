from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo,Carico,trasporto
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
        
class CLienti:
    def __init__(self,imp,erario,cod):
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.put(self.imp,self.erario.self.cod)
        
    def put(self,imp,erario,cod):
        a=imp
        b=erario
        c=cod
        return (1)
