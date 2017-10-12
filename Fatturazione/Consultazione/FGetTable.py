from gestione.models import Cliente, Area,Sito,Sospese,Scarico,trasporto,Carico
from django.db.models import Q,F


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
        dic={}
        if(nome[:2]=="sc"):
            rec=Sospese.objects.filter(fatturas=nome).values("cliente__azienda","data","fatturas","q","cassa","prezzo","idcod__cod","idcod__genere__iva","lotto")
            c=Carico.objects.filter(cassa__gt=F("cassaexit")).values("idcod__id","bolla","id","idcod__cod","cassa","cassaexit").order_by("bolla","data")
            d2=list(c)
            dic["cr"]=d2
        elif(nome[:2]=="fc"):
            rec=Scarico.objects.filter(fattura=nome).values("cliente__azienda","data","fattura","q","cassa","prezzo","idcod__cod","idcod__genere__iva","lotto")
        else:
            rec=trasporto.objects.filter(ddt=nome).values("cliente__azienda","data","ddt","q","cassa","prezzo","idcod__cod","idcod__genere__iva","lotto")
        d1=list(rec)
        dic["doc"]=d1
        return dic
