from gestione.models import Produttore,IDcod,Carico
from django.db.models import Q,F


class GetData:
    def GetIdCod(self,message):
        rec=Carico.objects.filter(Q(idcod__produttore__azienda=message["res"]),Q(data__gte=message["res1"])).values("idcod__cod",
                                "q","cassa","bolla","data").order_by("bolla")
        data=list(rec)
        return data
    def GetCarico(self):
        rec=Carico.objects.all().values("bolla","idcod__produttore__azienda").order_by("bolla")
        data=list(rec)
        return data    
    def GetBolla(self,line):
        rec=Carico.objects.filter(Q(bolla=line[0]), Q(idcod__produttore__azienda=line[1])).values("idcod__id","idcod__cod","q","cassa","data","bolla")
        data=list(rec)
        return data 
    def GetIdCodbyProdotto(self,message):
        rec=Carico.objects.filter(Q(idcod__genere__nome=message["prd"]),Q(data__gte=message["data"])).values("idcod__cod",
                                "q","bolla","data").order_by("-idcod__cod")
        data=list(rec)
        return data
    def GetCaricoTotale(self,message):
        rec=Carico.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","q","cassa","bolla","data").order_by("bolla")
        data=list(rec)
        return data    
    def GetCaricobyIdcod(self):
        rec=Carico.objects.filter(cassa__gt=F("cassaexit")).values("bolla","id","idcod__cod","cassa","cassaexit").order_by("idcod_id","data")
        data=list(rec)
        return data    
    def GetBollaCv(self,nome):
        ls=[]
        ls1=[]
        c=Carico.objects.filter(Q(idcod__produttore__azienda=nome)).order_by("bolla")
        cm1=c.filter(Q(cassa__gt=F("cassaexit")))
        cm2=cm1.values("bolla").distinct()
        for  item in cm2:
            ls.append(item["bolla"])
        cM1=c.filter(Q(cassa=F("cassaexit"))).values("idcod__id",
                                   "idcod__cod","q","cassa","data","bolla","costo").order_by("bolla")
        data=list(cM1)
        m=Produttore.objects.get(azienda=nome)
        for item in cM1:
            if(item["bolla"] in ls):
                continue
            item["costo"]=item["costo"]
            ls1.append(item)
        return ls1 
    