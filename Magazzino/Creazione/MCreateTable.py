#import django
#django.setup()
from gestione.models import IDcod,Carico,Genere,Saldo,ExCsBl,Produttore
from django.db.models import Q
from decimal import Decimal
import re
import sys
import io

class CreateData:
    
    def EntrataBolla(self,ls,bl,bl1,dt,facc,tras,vari,cl):
        rec=0
        cnt=0
        i=0
        before=" "
        tot=0
        totcss=0
        pssum=0
        csssum=0
        cssexitsum=0
        line= sorted(ls, key=lambda k: k['cod']) 
        seg=line[0]["cod"].split('-')
        pc=Carico.objects.filter(Q(bolla=bl),Q(idcod__produttore__id=cl))
        pc1=Carico.objects.filter(Q(bolla=bl1),Q(idcod__produttore__id=cl))
        if (pc1):
            if(bl!=bl1):
                return 3
        for item in line:
            pssum+=Decimal(item["ps"])
            csssum+=int(item["css"])
        
        if(pc):
            p=pc.filter().values("qn","cassa","cassaexit","idcod__id","data","excsbl__id")
            o=p[0]["qn"]
            o1=p[0]["excsbl__id"]
            rec=ExCsBl.objects.get(id=o1)
            rec.facc=Decimal(facc)
            rec.trasporto=Decimal(tras)
            rec.vari=Decimal(vari)
            rec.qn=pssum
            rec.cassa=csssum
            rec.bolla=bl1
            rec.data=dt
            rec.save()
            data=list(p)
            pc.delete()
            dt=data[0]["data"]
            cnt=1
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
            prd=Produttore.objects.get(id=cl)
            if(cnt==0):
                rec=ExCsBl(produttore=prd,data=dt,bolla=bl1,facc=Decimal(facc),trasporto=Decimal(tras),vari=Decimal(vari),qn=pssum,cassa=csssum)
                rec.save() 
            rec1=Carico(excsbl=rec,tara=item["tara"],qn=item["ps"],cassa=item["css"],bolla=bl1,idcod=codid,data=dt,cassaexit=csx)
            rec1.save()
            cnt=1
        return 2        
    
 