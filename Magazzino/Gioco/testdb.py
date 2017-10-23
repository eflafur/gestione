from gestione.models import sp, ce

class test():
    v=400
    def __init__(self,cod, imp,iva):
        self.cod=500
        self.imp=imp
        self.iva=iva
    def ScriviAttivo(self):
        c=self.v
        a=self.imp*100
        b="ciao"
        #s=sp.objects.all()
        #cl=s.get(cod=cod)
        #iva=s.get(cod="20.20")
        #cl.attivo+=imp+erario
        #iva.passivo+=erario
        #cl.save()
        #iva.save()
        return self
class test1(test):
    f=100
