from gestione.models import Cliente,sp,ce,ivacliente,ivaforn,libro,saldocliente,saldoprod,Produttore
from decimal import Decimal
from django.db.models import Q,F
import openpyxl,time,os,subprocess,datetime
from datetime import datetime,timedelta,date

class Commercio:
    def __init__(self,conto,tot,imp,erario,cod,pg,cl,fatt,data=date.today(),idfrn=0):
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
        self.cl=cl
        self.idfrn=idfrn
        self.fatt=fatt
        self.data=data
        self.s=sp.objects.all()
        self.cln=self.s.get(cod=cod)
        self.iva=self.s.get(cod="20.20")
        prt=libro.objects.latest("id")
        self.p=prt.id
        

    def Vendita(self,chc=0):
        cl=Cliente.objects.get(azienda=self.cl)
        sl=saldocliente.objects.get(cliente=cl)
        if(chc==0):
            sl.attivo+=self.imp+self.erario
            sl.save()
            
            self.cln.attivo+=self.imp+self.erario
            self.iva.passivo+=self.erario
            rc=ce.objects.get(cod="80.80")
            rc.ricavi+=self.imp
            self.iva.save()
            rc.save()
        if(self.pg==0):
            sl.passivo+=self.tot
            sl.save()            
            
            self.cln.passivo+=self.tot#self.imp+self.erario
            cs=self.s.get(cod=self.conto)
            cs.attivo+=self.tot#self.imp+self.erario
            cs.save()
            l=libro(id=self.p+4,prot=self.p+4,doc=self.fatt,desc="Cassa/Banca per vendita a " +self.cl,conto=self.conto,
                        dare=self.tot)#self.erario+self.imp)
            l1=libro(id=self.p+5,prot=self.p+4,doc=self.fatt,desc="fattura acquisto da " +self.cl,conto=self.cod,
                            avere=self.tot)#self.erario+self.imp)
            l.save()
            l1.save()
        self.cln.save()
    def Acquisto(self):
        prd=Produttore.objects.get(id=self.idfrn)
        sprd=saldoprod.objects.get(prod=prd)
        sprd.passivo+=self.imp+self.erario
        sprd.save()

        self.cln.passivo+=self.imp+self.erario
        self.iva.attivo+=self.erario
        rc=ce.objects.get(cod="72.72")
        rc.costi+=self.imp
        self.cln.save()
        self.iva.save()
        rc.save()
        if(self.pg==1):
            sprd.attivo+=self.tot
            sprd.save()
            
            sprd.save()
            cs=self.s.get(cod="1.1")
            cs.passivo+=self.imp+self.erario
            cs.save()
    def SetErarioCliente(self,r=0):
        rec=ivacliente.objects.latest("id")
        res=ivacliente(prot=rec.prot+1,fatt=self.fatt,nome=self.cl,tot=self.imp+self.erario,imp=self.imp,
            erario=self.erario,saldo=self.imp+self.erario-self.tot)
        res.save()
        if(r==0):
            l=libro(id=self.p+1,prot=self.p+1,doc=self.fatt,desc="fattura vendita a " +self.cl,conto=self.cod,
                        dare=self.erario+self.imp)
            l1=libro(id=self.p+2,prot=self.p+2,doc=self.fatt,desc="fattura IVA " +self.cl,conto="20.20",
                         avere=self.erario)
            l2=libro(id=self.p+3,prot=self.p+3,doc=self.fatt,desc="fattura ricavi " +self.cl,conto="80.80",
                         avere=self.imp)
        else:
            l=libro(id=self.p+1,prot=self.p+1,doc=self.fatt,desc="reso vendita a" +self.cl,conto=self.cod,
                            dare=self.erario+self.imp)
            l1=libro(id=self.p+2,prot=self.p+2,doc=self.fatt,desc="storno IVA " +self.cl,conto="20.20",
                             avere=self.erario)
            l2=libro(id=self.p+3,prot=self.p+3,doc=self.fatt,desc="reso su vendite" +self.cl,conto="80.80",
                             avere=self.imp)
        l.save()
        l1.save()
        l2.save()
    def SetErarioForn(self):
        rec=ivaforn.objects.latest("id")
  
        res=ivaforn(saldo=self.imp+self.erario-self.tot,prot=rec.prot+1,fatt=self.fatt,nome=self.idfrn,tot=self.imp+self.erario,imp=self.imp,erario=self.erario)
        res.save()
        prt=libro.objects.latest("id")
        p=prt.id
        l=libro(id=self.p+1,prot=self.p+1,doc=self.fatt,dtdoc=self.data,desc="fattura acquisto da " +self.cl,conto=self.cod,
                    avere=self.erario+self.imp)
        l1=libro(id=self.p+2,prot=self.p+2,doc=self.fatt,dtdoc=self.data,desc="fattura IVA " +self.cl,conto="20.20",
                     dare=self.erario)
        l2=libro(id=self.p+3,prot=self.p+3,doc=self.fatt,dtdoc=self.data,desc="fattura costi " +self.cl,conto="72.72",
                     dare=self.imp)
        l.save()
        l1.save()
        l2.save()
        
 
class ComVen(Commercio):
    pass

    
class Banca:
    def __init__(self,conto,tot,imp,erario,cod,sgn,doc,data,cl,idfrn=0):
        self.conto=conto
        self.tot=Decimal(tot)
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.sgn=sgn
        self.doc=doc
        self.data=data
        self.cl=cl
        self.idfrn=idfrn
        prt=libro.objects.latest("id")
        self.p=prt.id
    def put(self):
        bc=sp.objects.get(cod="1.2")
        if(self.sgn==0):
            bc.attivo+=self.tot#self.imp+self.erario
            cln=sp.objects.get(cod="3.1")
            cln.passivo+=self.tot#self.imp+self.erario
            l=libro(id=self.p+1,prot=self.p+1,doc=self.doc,dtdoc=self.data,desc="Banca per vendita a " +self.cl,conto="1.2",
                            dare=self.tot)#self.erario+self.imp)
            l1=libro(id=self.p+2,prot=self.p+2,doc=self.doc,dtdoc=self.data,desc=" Storno cliente vendita a " +self.cl,conto="3.1",
                             avere=self.tot)#self.erario+self.imp)
            l.save()
            l1.save()
        else:
            bc.passivo+=self.imp
        bc.save()
        cln.save()
 
    def putfrn(self):
        prd=Produttore.objects.get(id=self.idfrn)
        sprd=saldoprod.objects.get(prod=prd)
        sprd.attivo+=self.tot
        sprd.save()

        ss=ivaforn.objects.get(Q(fatt=self.doc),Q(nome=self.idfrn))
        ss.saldo-=self.tot
        ss.save()
        bc=sp.objects.get(cod=self.conto)#"1.2")
        if(self.sgn==0):
            bc.passivo+=self.tot#self.imp+self.erario
            cln=sp.objects.get(cod="53.1")
            cln.attivo+=self.tot#self.imp+self.erario
            l=libro(id=self.p+1,prot=self.p+1,doc=self.doc,dtdoc=self.data,desc="Banca per vendita a " +self.cl,conto=self.conto,
                            avere=self.tot)#self.erario+self.imp)
            l1=libro(id=self.p+2,prot=self.p+2,doc=self.doc,dtdoc=self.data,desc="Storno fornitore acquisto da " +self.cl,conto="53.1",
                             dare=self.tot)#self.erario+self.imp)
            l.save()
            l1.save()
        else:
            bc.passivo+=self.imp
        bc.save()
        cln.save()        
        
class ComVenBnc(Banca):
    pass
