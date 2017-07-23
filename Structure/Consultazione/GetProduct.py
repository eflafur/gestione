import django
django.setup()
from gestione.models import Produttore,Settore,Genere,Area,Sito,Preferenza
from django.db.models import Q

class LKPData:
    def getbyCompany(self,line):
        self.row=line
        p=Produttore.objects.filter(Q(azienda=line)).values("settore__articolo","tel")
        if (p==""):
            return (2)
        data=list(p)
        return data
    def getbyArticolo(self,line):
        self.row=line
        p=Settore.objects.filter(Q(articolo=line)).values("articolo","produttore__azienda")
        if (p==""):
            return (2)
        data=list(p)
        return data    
    def getbyMargin(self,line):
        self.row=line
        p=Produttore.objects.filter(Q(margine__gte=line)).order_by("margine").values("azienda","margine","regione","citta","tel")
        if (p==""):
            return (2)
        data=list(p)
        return data
    def ListAddArt(self,line):
        dd=[]
        self.row=line
        allart=Settore.objects.all().values("articolo")
        prd=Produttore.objects.filter(Q(azienda=line)).values("settore__articolo")
        
        for item in allart:
            h=0
            for item1 in prd:
                if(item["articolo"]==item1["settore__articolo"]):
                    h=1
                    break
                else:
                    c="ciccio"
            if(h==0):
                dd.append(item["articolo"])
        data=list(dd)
        return dd 
    def ListDelArt(self,line):
        dd=[]
        self.row=line
        prd=Produttore.objects.filter(Q(azienda=line)).values("settore__articolo")
        data=list(prd)
        return data     
