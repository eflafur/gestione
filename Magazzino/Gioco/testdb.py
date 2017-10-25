from gestione.models import sp, ce,ivacliente

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
            cs.attivo+=self.imp+self.erario
            cs.save()
    def SetErarioCliente(self):
        rec=ivacliente.objects.latest("id")
        res=ivacliente(prot=rec.prot+1,fatt=self.fatt,nome=self.cl,tot=self.imp+self.erario,imp=self.imp,erario=self.erario)
        res.save()            

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
    
