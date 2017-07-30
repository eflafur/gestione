import django
django.setup()
from gestione.models import Cliente,Area,Sito,Preferenza
from django.db.models import Q

    
class ModProd:
    def GetCliente(self,line):
        self.row=line
        res=Cliente.objects.filter(Q(azienda=line)).values("azienda",
                                "regione","citta","email","tel","trpag","pi","indirizzo")
        ret=list(res)    
        return ret
    def Change(self,line):
        self.row=line
        val=0
        val1=0
        p=Cliente.objects.get(azienda=self.row["a1"])
        pt=Cliente.objects.filter(Q(azienda=self.row["a1"])).values("regione",
                                    "citta","email","tel","trpag","pi","indirizzo")
        if(pt[0]["regione"]!=self.row["a3"]):
            val=1            
        elif(pt[0]["citta"]!=self.row["a4"]):
            val=1
        elif(pt[0]["tel"]!=self.row["a8"]):
            val=1
        elif(pt[0]["email"]!=self.row["a6"]):
            val=1
        elif(pt[0]["trpag"]!=int(self.row["a9"])):
            val=1
        elif(pt[0]["indirizzo"]!=self.row["a7"]):
            val=1
        elif(pt[0]["pi"]!=self.row["a2"]):
            val=1
        if (val==0):
            return 2
        if (val==1):
            p.regione=self.row["a3"]
            p.citta=self.row["a4"]
            p.indirizzo=self.row["a7"]
            p.tel=self.row["a8"]
            p.email=self.row["a6"]
            p.trpag=self.row["a9"]
            p.pi=self.row["a2"]
            p.save()
        return "okey"
    
    def DelCliente(self,var):
        rec=Cliente.objects.get(azienda=var)
        rec.delete()
        return 1