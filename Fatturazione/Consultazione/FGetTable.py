from gestione.models import Cliente, Area,Sito,Sospese,Scarico
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
    def GetClienteByNumSospese(self,nome):
        rec=""
        rec=Sospese.objects.filter(fatturas=nome).values("cliente__azienda","data","fatturas","q","cassa","prezzo","idcod__cod","idcod__genere__iva","lotto")
        data=list(rec)
        return data   
    def GetClienteByNumFatture(self,nome):
        rec=""
        rec=Scarico.objects.filter(fattura=nome).values("cliente__azienda","data","fattura","q","prezzo","idcod__cod","idcod__genere__iva")
        data=list(rec)
        return data       