import django
django.setup()
from gestione.models import IDcod,Carico,Genere,Saldo
from django.db.models import Q
from decimal import Decimal
import re
import sys
import io

class CreateData:
    def EntrataBolla(self,ls,bl):
        before=" "
        tot=0
        totcss=0
        line= sorted(ls, key=lambda k: k['cod']) 
        seg=line[0]["cod"].split('-')
        p=Carico.objects.filter(Q(bolla=bl),Q(idcod__produttore__azienda=seg[0]))
        if(p):
            p1=p.filter().values("q","cassa","idcod__id")
            for itm in p1:
                rec1=Saldo.objects.get(idcod__id=itm["idcod__id"])
                rec1.q=rec1.q-itm["cassa"]
                rec1.save()      
            p.delete()
        for item in line:
            if(str(before)!=item["id"]):
                if(before==" "):
                    tot=0
                    tot=tot+Decimal(item["ps"])
                    totcss=0
                    totcss=totcss+int(item["css"])
                else:
                    codid=IDcod.objects.get(id=before)
                    rec=Carico(q=tot,cassa=totcss,bolla=bl,idcod=codid)
                    rec.save()
                    rec1=Saldo.objects.get(idcod__cod=codid)
                    rec1.q=rec1.q+totcss
                    rec1.save()
                    tot=0
                    tot=tot+Decimal(item["ps"])
                    totcss=0
                    totcss=totcss+int(item["css"])
            elif(str(before)==item["id"]):
                tot=tot+Decimal(item["ps"])
                totcss=totcss+int(item["css"])
            before=item["id"]
        codid=IDcod.objects.get(id=before)
        rec=Carico(q=tot,cassa=totcss,bolla=bl,idcod=codid)
        rec.save()
        rec1=Saldo.objects.get(idcod=codid)
        rec1.q=rec1.q+totcss
        rec1.save()
        return 2
    