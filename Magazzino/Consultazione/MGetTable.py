from gestione.models import Produttore,IDcod,Carico
from django.db.models import Q


class GetData:
    def GetIdCod(self,message):
        rec=Carico.objects.filter(Q(idcod__produttore__azienda=message["res"]),Q(data__gte=message["res1"])).values("idcod__cod","q","bolla","data")
        data=list(rec)
        return data
    def GetCarico(self):
        rec=Carico.objects.all().values("bolla","idcod__produttore__azienda").order_by("bolla")
        data=list(rec)
        return data    
    def GetBolla(self,line):
        rec=Carico.objects.filter(Q(bolla=line[0]), Q(idcod__produttore__azienda=line[1])).values("idcod__cod","q","data")
        data=list(rec)
        return data    