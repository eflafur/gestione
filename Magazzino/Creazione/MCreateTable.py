from gestione.models import IDcod,Carico,Genere
from django.db.models import Q
import re
import sys
import io

class CreateData:
    def Entrata(self,line):
        seg=line["a1"].split('-')
        p=Carico.objects.filter(Q(bolla=line["a3"]),Q(idcod__cod=line["a1"])).values("q")
        p1=Carico.objects.filter(Q(bolla=line["a3"]),Q(idcod__produttore__azienda= seg[0])).values("data")
        if(p):
            tot=p[0]["q"]+int(line["a2"])
            p.update(q=tot)
            return 2
        elif(p1):
            dt=p1[0]["data"]
            cod=IDcod.objects.get(cod=line["a1"])
            rec=Carico(q=line["a2"],bolla=line["a3"],idcod=cod,data=dt)            
            rec.save()
            return 2
        else:
            cod=IDcod.objects.get(cod=line["a1"])
            rec=Carico(q=line["a2"],bolla=line["a3"],idcod=cod)
            rec.save()
        return
    
#inserimento IVA causa shell non funziona
    def Genere(self):
        g=Genere.objects.get(id=16)
        g.iva=0.12
        g.save()