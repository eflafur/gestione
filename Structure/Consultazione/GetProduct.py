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
    