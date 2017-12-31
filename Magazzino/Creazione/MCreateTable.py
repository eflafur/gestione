#import django
#django.setup()
from gestione.models import IDcod,Carico,Genere,Saldo
from django.db.models import Q
from decimal import Decimal
import re
import sys
import io

class CreateData:
    
    def EntrataBolla(self,ls,bl,dt):
        i=0
        before=" "
        tot=0
        totcss=0
        line= sorted(ls, key=lambda k: k['cod']) 
        seg=line[0]["cod"].split('-')
        pc=Carico.objects.filter(Q(bolla=bl),Q(idcod__produttore__azienda=seg[0]))
        if(pc):
            p=pc.filter().values("qn","cassa","cassaexit","idcod__id","data")
            data=list(p)
            pc.delete()
            dt=data[0]["data"]
        s=Saldo.objects.all()
        cod=IDcod.objects.all()
  
        for item in line:
            if(item["tara"]==""):
                item["tara"]=-1
            diff=int(item["css"])
            csx=0
            try:
                for itemp in data:
                    if (int(item["id"])==int(itemp["idcod__id"])):
                        csx=int(itemp["cassaexit"])
                        diff=int(item["css"])-int(itemp["cassa"])
            except:
                data=""
            s1=s.get(idcod_id=item["id"])
            qs=s1.q
            s1.q=qs+diff
            s1.save()
            codid=cod.get(id=item["id"])
            rec=Carico(tara=item["tara"],qn=item["ps"],cassa=item["css"],bolla=bl,idcod=codid,data=dt,cassaexit=csx)
            rec.save()
        return 2        
    
 