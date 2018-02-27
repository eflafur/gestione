from gestione.models import Cliente,sp,ce,ivacliente,ivaforn,libro,saldocliente,saldoprod,contoce,contosp,Produttore,contocln,contofrn
from decimal import Decimal
from django.db.models import Q,F
import openpyxl,time,os,subprocess,datetime
from datetime import datetime,timedelta,date

class Commercio:
    def __init__(self,conto,tot,imp,erario,cod,pg,cl,fatt,codce="",data=date.today(),idfrn=0):
        self.tot=Decimal(tot)
        if(self.tot>0):
            self.pg=0
        else:
            self.pg=pg
        self.conto=conto
        self.tot=Decimal(tot)
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.codce=codce
        self.clnt=cl
        self.idfrn=idfrn
        self.fatt=fatt
        self.data=data
      #  self.s=sp.objects.all()
     #   self.cln=self.s.get(cod=cod)
      #  self.iva=self.s.get(cod="20.20")
      #  prt=libro.objects.latest("id")
      #  self.p=prt.id

    def Venditams(self,chc=0,):
        sl=saldocliente.objects.get(cliente=self.clnt)
        if(chc==0):
            sl.attivo+=self.imp+self.erario
            sl.save()
            ls=self.cod.split(".")
            lsce=self.codce.split(".")
            res=contocln(cod=ls[0],sub=ls[1],ssub=ls[2],dare=self.imp+self.erario,cliente=self.clnt,regis="VENDITA")#CLIENTE
            res.save()
            res=contosp(cod="35",sub="01",ssub="03",avere=self.erario,regis="IVA VENDITA") #ERARIO
            res.save()
            res=contoce(cod=lsce[0],sub=lsce[1],ssub=lsce[2],avere=self.imp,regis="VENDITA MERCI")#RICAVI
            res.save()
        if(self.pg==0):
            ls=self.conto.split(".")
            sl.passivo+=self.tot
            sl.save()
            res=contocln(cod="11",sub="03",ssub="01",avere=self.tot,cliente=self.clnt,regis="PAGAMENTO")#CLIENTE
            res.save()
            res=contosp(cod=ls[0],sub=ls[1],ssub=ls[2],dare=self.tot,regis="PAGAMENTO")#CLIENTE
            res.save()
            l=libro(doc=self.fatt,desc="Cassa/Banca per vendita a " +self.clnt.azienda,conto=self.conto,
                        dare=self.tot)#self.erario+self.imp)
            l1=libro(doc=self.fatt,desc="fattura acquisto da " +self.clnt.azienda,conto=self.cod,
                            avere=self.tot)#self.erario+self.imp)
            l.save()
            l1.save()
        
    def Acquistoms(self):
#        prd=Produttore.objects.get(id=self.idfrn)
        sprd=saldoprod.objects.get(prod=self.clnt)
        sprd.passivo+=self.imp+self.erario
        sprd.save()

        ls=self.cod.split(".")
        res=contofrn(cod=ls[0],sub=ls[1],ssub=ls[2],avere=self.imp+self.erario,forn=self.clnt,regis="ACQUISTO")#fornitore
        res.save()
        res=contosp(cod="35",sub="01",ssub="01",dare=self.erario,regis="IVA ACQUISTI") #ERARIO
        res.save()
        res=contoce(cod="55",sub="01",ssub="07",dare=self.imp,regis="ACQUISTO MERCI")#COSTI
        res.save()
        if(self.pg==1):
            sprd.attivo+=self.tot
            sprd.save()
            
            res=contosp(cod="19",sub="03",ssub="03",avere=self.imp+self.erario,regis="PAGAMENTO")#fornitore
            res.save()
            
    def SetErarioCliente(self,r=0):
#        rec=ivacliente.objects.latest("id")
        res=ivacliente(fatt=self.fatt,nome=self.clnt.azienda,tot=self.imp+self.erario,imp=self.imp,
            erario=self.erario,saldo=self.imp+self.erario-self.tot)
        res.save()
        if(r==0):
            l=libro(doc=self.fatt,desc="fattura vendita a " +self.clnt.azienda,conto=self.cod,
                        dare=self.erario+self.imp)
            l1=libro(doc=self.fatt,desc="fattura IVA " +self.clnt.azienda,conto="35.01.03",
                         avere=self.erario)
            l2=libro(doc=self.fatt,desc="fattura ricavi " +self.clnt.azienda,conto="47.01.03",
                         avere=self.imp)
        else:
            l=libro(doc=self.fatt,desc="reso vendita a " +self.clnt.azienda,conto=self.cod,
                            dare=self.erario+self.imp)
            l1=libro(doc=self.fatt,desc="storno IVA " +self.clnt.azienda,conto="35.01.03",
                             avere=self.erario)
            l2=libro(doc=self.fatt,desc="reso vendite" +self.clnt.azienda,conto="47.05.07",
                             avere=self.imp)
        l.save()
        l1.save()
        l2.save()
    def SetErarioForn(self):
#        rec=ivaforn.objects.latest("id")
  
        res=ivaforn(saldo=self.imp+self.erario-self.tot,fatt=self.fatt,nome=self.idfrn,tot=self.imp+self.erario,imp=self.imp,erario=self.erario)
        res.save()
        #prt=libro.objects.latest("id")
        #p=prt.id
        l=libro(doc=self.fatt,dtdoc=self.data,desc="fattura vendite a " +self.clnt.azienda,conto=self.cod,
                    avere=self.erario+self.imp)
        l1=libro(doc=self.fatt,dtdoc=self.data,desc="fattura IVA " +self.clnt.azienda,conto="35.01.01",
                     dare=self.erario)
        l2=libro(doc=self.fatt,dtdoc=self.data,desc="fattura costi " +self.clnt.azienda,conto="55.01.07",
                     dare=self.imp)
        l.save()
        l1.save()
        l2.save()
        
 
class ComVen(Commercio):
    pass


class Banca:
    def __init__(self,conto,tot,imp,erario,cod,sgn,doc,data,f,idfrn=0):
        self.conto=conto
        self.tot=Decimal(tot)
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.sgn=sgn
        self.doc=doc
        self.data=data
        self.frn=f
        self.idfrn=idfrn
        prt=libro.objects.latest("id")
        self.p=prt.id
        
    def putms(self):
        if(self.sgn==0):
            res=contosp(cod="19",sub="01",ssub="01",dare=self.tot,regis="PAG BANCA") #PAGAMENTO  BANCA
            resf=contofrn(cod="33",sub="03",ssub="01",avere=self.tot,forn=self.clnt,regis="ACQUISTO")#fornitore
            resf.save()
            l=libro(doc=self.doc,dtdoc=self.data,desc="Banca per vendita a " +self.clnt.azienda,conto="19.01.01",
                            dare=self.tot)#self.erario+self.imp)
            l1=libro(doc=self.doc,dtdoc=self.data,desc=" Storno cliente vendita a " +self.clnt.azienda,conto="3.1",
                             avere=self.tot)#self.erario+self.imp)
            l.save()
            l1.save()
        else:
            res=contosp(cod="19",sub="01",ssub="01",avere=self.imp,regis="PAG BANCA") #PAGAMENTO  BANCA
        res.save()
        
 
    def putfrnms(self):
        ls=self.conto.split(".")
        sprd=saldoprod.objects.get(prod=self.frn)
        sprd.attivo+=self.tot
        sprd.save()

        ss=ivaforn.objects.get(Q(fatt=self.doc),Q(nome=self.idfrn))
        ss.saldo-=self.tot
        ss.save()

        if(self.sgn==0):
            res=contosp(cod=ls[0],sub=ls[1],ssub=ls[2],avere=self.tot,regis="PAG BANCA") #PAGAMENTO  BANCA
            resf=contofrn(cod="33",sub="03",ssub="01",dare=self.tot,forn=self.frn,regis="ACQUISTO")#fornitore
            l=libro(doc=self.doc,dtdoc=self.data,desc="Banca per vendita a " +self.frn.azienda,conto=self.conto,
                            avere=self.tot)#self.erario+self.imp)
            l1=libro(doc=self.doc,dtdoc=self.data,desc="Storno fornitore acquisto da " +self.frn.azienda,conto="55.01.07",
                             dare=self.tot)#self.erario+self.imp)
            l.save()
            l1.save()
        else:
            res=contosp(cod=ls[0],sub=ls[1],ssub=ls[2],avere=self.imp,regis="PAG BANCA") #PAGAMENTO  BANCA
        res.save()
        resf.save()        
        
class ComVenBnc(Banca):
    pass
