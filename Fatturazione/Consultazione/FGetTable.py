from gestione.models import Cliente, Area,Sito
from django.db.models import Q


class GetData:
    def GetAnagrafica(self,var):
        if(var!=""):
            c=Cliente.objects.filter(Q(azienda=var)).values("azienda","pi","regione","citta","indirizzo"
                                                            ,"tel","email","trpag","acquisizione")
        else:
            c=Cliente.objects.all()
        data=list(c)
        return data
    def GetCliente(self):
        recs=Cliente.objects.all();
        data=list(recs)
        return data