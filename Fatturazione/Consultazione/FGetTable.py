from gestione.models import Cliente, Area,Sito,Sospese,Scarico,trasporto
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
        if(nome[:2]=="sc"):
            rec=Sospese.objects.filter(fatturas=nome).values("cliente__azienda","data","fatturas","q","cassa","prezzo","idcod__cod","idcod__genere__iva","lotto")
        elif(nome[:2]=="fc"):
            rec=Scarico.objects.filter(fattura=nome).values("cliente__azienda","data","fattura","q","cassa","prezzo","idcod__cod","idcod__genere__iva","lotto")
        else:
            rec=trasporto.objects.filter(ddt=nome).values("cliente__azienda","data","ddt","q","cassa","prezzo","idcod__cod","idcod__genere__iva","lotto")
        data=list(rec)
        return data   
