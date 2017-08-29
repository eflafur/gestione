import django
django.setup()
from gestione.models import IDcod,Carico,Genere,Saldo
from django.db.models import Q
from decimal import Decimal
import re
import sys
import io

class CreateData:
    def Entrata(self,line):
        seg=line["a1"].split('-')
        p=Carico.objects.filter(Q(bolla=line["a3"]),Q(idcod__cod=line["a1"])).values("q")
        p1=Carico.objects.filter(Q(bolla=line["a3"]),Q(idcod__produttore__azienda= seg[0])).values("data")
        if(p):
            tot=p[0]["q"]+Decimal(line["a2"])
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


    def EntrataBolla(self,ls,bl):
        before=" "
        tot=0
        line= sorted(ls, key=lambda k: k['cod']) 
        bolla=re.sub(" ","",bl)
        seg=line[0]["cod"].split('-')
        p=Carico.objects.filter(Q(bolla=bolla),Q(idcod__produttore__azienda=seg[0]))
        if(p):
            p1=p.filter().values("q","idcod__id")
            for itm in p1:
                rec1=Saldo.objects.get(idcod__id=itm["idcod__id"])
                rec1.q=rec1.q-itm["q"]
                rec1.save()      
            p.delete()
        for item in line:
            if(str(before)!=item["id"]):
                if(before==" "):
                    tot=0
                    tot=tot+Decimal(item["ps"])
                else:
                    codid=IDcod.objects.get(id=before)
                    rec=Carico(q=tot,bolla=bolla,idcod=codid)
                    rec.save()
                    rec1=Saldo.objects.get(idcod__cod=codid)
                    rec1.q=rec1.q+tot
                    rec1.save()
                    tot=0
                    tot=tot+Decimal(item["ps"])
            elif(str(before)==item["id"]):
                tot=tot+Decimal(item["ps"])
            before=item["id"]
        codid=IDcod.objects.get(id=before)
        rec=Carico(q=tot,bolla=bolla,idcod=codid)
        rec.save()
        rec1=Saldo.objects.get(idcod__cod=codid)
        rec1.q=rec1.q+tot
        rec1.save()
        return 2
    