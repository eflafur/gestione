from gestione.models import sp, ce,ivacliente,libro

class Commercio:
    def __init__(self,imp,erario,cod,pg,cl,fatt):
        self.imp=imp
        self.erario=erario
        self.cod=cod
        self.pg=pg
        self.cl=cl
        self.fatt=fatt
        self.s=sp.objects.all()
        self.cln=self.s.get(cod=cod)
        self.iva=self.s.get(cod="20.20")
    def Vendita(self):
        self.cln.attivo+=self.imp+self.erario
        self.iva.passivo+=self.erario
        rc=ce.objects.get(cod="80.80")
        rc.ricavi+=self.imp
        self.cln.save()
        self.iva.save()
        rc.save()
        if(self.pg==0):
            cs=self.s.get(cod="1.1")
            cs.attivo+=self.imp+self.erario
            cs.save()
    def SetErarioCliente(self):
        prt=libro.objects.latest("id")
        p=prt.id
        ds="fattura vendita a " +self.cl
        l=libro(id=p+1,prot=p+1,doc=self.fatt,desc="fattura vendita a " +self.cl,conto=self.cod,
                dare=self.erario+self.imp)
        l1=libro(id=p+2,prot=p+2,doc=self.fatt,desc="fattura IVA " +self.cl,conto="20.20",
                avere=self.erario)
        l2=libro(id=p+3,prot=p+3,doc=self.fatt,desc="fattura ricavi" +self.cl,conto="80.80",
                    avere=self.imp)
        l.save()
        l1.save()
        l2.save()
class Clienti(Commercio):
    #def __init__(self,imp,erario,cod,pg,cl,fatt):
        #super().__init__(imp,erario,cod,pg,cl,fatt)
    pass


#class test():
##    fr=""
    #def __init__(self,imp,erario,cod):
        #self.imp=imp
        #self.erario=erario
        #self.cod=cod
        #s=sp.objects.all()
        #fr=s.get(cod=self.cod)
        #fr.passivo+=self.imp+self.erario
        #fr.save()
    #def put(self):
        #a=0
        #s=sp.objects.all()
        #fr=s.get(cod="3.1")
        #fr.passivo+=49
        ##cs=s.get(cod="1.1")
        ##iva=s.get(cod="20.20")
        ##fr.save()
        ##cs.save()
        ##iva.save()
        ##rc.save()
        ##return (1)
        #fr.save()
#class Clienti(test):
    #def __init__(self,imp,erario,cod):
        #pass
    #def put(self):
        #super().put()
        #s=sp.objects.all()
        #fr=s.get(cod="3.1")
        #fr.passivo+=951        
        #fr.save()
        ##self.imp=imp
        ##self.erario=erario
        ##self.cod=cod
        ##s=sp.objects.all()
        ##fr=s.get(cod=self.cod)
        ##fr.passivo+=self.imp+self.erario
        ##fr.save()    
        ##rc=ce.objects.get(cod="80.80")
        ##rc.costi+=self.imp

        ##iva.attivo+=self.erario
        ##cs.passivo+=self.imp+self.erario
        ##fr.attivo+=self.imp+self.erario
    
