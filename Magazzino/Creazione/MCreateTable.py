#import django
#django.setup()
from gestione.models import IDcod,Carico,Genere,Saldo
from django.db.models import Q
from decimal import Decimal
import re
import sys
import io

class CreateData:
    #def EntrataBolla(self,ls,bl,dt):
        #before=" "
        #tot=0
        #totcss=0
        #line= sorted(ls, key=lambda k: k['cod']) 
        #seg=line[0]["cod"].split('-')
        #p=Carico.objects.filter(Q(bolla=bl),Q(idcod__produttore__azienda=seg[0]))
        #if(p):
            #p1=p.filter().values("q","cassa","idcod__id","data")
            #dt=p1[0]["data"]
            #for itm in p1:
                #rec1=Saldo.objects.get(idcod__id=itm["idcod__id"])
                #rec1.q=rec1.q-itm["cassa"]
                #rec1.save()
            #p.delete()

        #for item in line:
            #csx=0
            #for item1 in p:
                #if (item["id"]==item.id):
                    #csx=item1.cassaexit   
            #if(str(before)!=item["id"]):
                #if(before==" "):
                    #tot=0
                    #tot=tot+Decimal(item["ps"])
                    #totcss=0
                    #totcss=totcss+int(item["css"])
                #else:
                    #codid=IDcod.objects.get(id=before)
                    #rec=Carico(q=tot,cassa=totcss,bolla=bl,idcod=codid,data=dt,cassaexit=csx)
                    #rec.save()
                    #rec1=Saldo.objects.get(idcod__cod=codid)
                    #rec1.q=rec1.q+totcss
                    #rec1.save()
                    #tot=0
                    #tot=tot+Decimal(item["ps"])
                    #totcss=0
                    #totcss=totcss+int(item["css"])
            #elif(str(before)==item["id"]):
                #tot=tot+Decimal(item["ps"])
                #totcss=totcss+int(item["css"])
            #before=item["id"]
        #codid=IDcod.objects.get(id=before)
        #rec=Carico(q=tot,cassa=totcss,bolla=bl,idcod=codid,data=dt,cassaexit=csx)
        #rec.save()
        #rec1=Saldo.objects.get(idcod=codid)
        #rec1.q=rec1.q+totcss
        #rec1.save()
        #return 2
 
 
    #def EntrataBolla(self,ls,bl,dt):
        #before=" "
        #tot=0
        #totcss=0
        #line= sorted(ls, key=lambda k: k['cod']) 
        #seg=line[0]["cod"].split('-')
        #pc=Carico.objects.filter(Q(bolla=bl),Q(idcod__produttore__azienda=seg[0]))
        #if(pc):
            #p=pc.filter().values("q","cassa","cassaexit","idcod__id","data")
            #dt=p[0]["data"]
        #s=Saldo.objects.all()
        #cod=IDcod.objects.all()
  
        #for item in line:
            #csx=0
            #if(pc):
                #for itemp in p:
                    #if (int(item["id"])==int(itemp["idcod__id"])):
                        #csx=int(itemp["cassaexit"])
                        #diff=int(item["css"])-int(itemp["cassa"])
                        #s1=s.get(idcod_id=itemp["idcod__id"])
                        #qs=s1.q
                        #s1.q=qs+diff
                        #s1.save()
            #if(str(before)!=item["id"]):
                #if(before==" "):
                    #tot=0
                    #tot=tot+Decimal(item["ps"])
                    #totcss=0
                    #totcss=totcss+int(item["css"])
                #else:
                    #codid=cod.get(id=before)
                    #rec=Carico(q=tot,cassa=totcss,bolla=bl,idcod=codid,data=dt,cassaexit=csx)
                    #rec.save()
                    #tot=0
                    #tot=tot+Decimal(item["ps"])
                    #totcss=0
                    #totcss=totcss+int(item["css"])
            #elif(str(before)==item["id"]):
                #tot=tot+Decimal(item["ps"])
                #totcss=totcss+int(item["css"])
            #before=item["id"]
        #codid=cod.get(id=before)
        #pc.delete()
        #rec=Carico(q=tot,cassa=totcss,bolla=bl,idcod=codid,data=dt,cassaexit=csx)
        #rec.save()
        #return 2    
    
    def EntrataBolla(self,ls,bl,dt):
        i=0
        before=" "
        tot=0
        totcss=0
        line= sorted(ls, key=lambda k: k['cod']) 
        seg=line[0]["cod"].split('-')
        pc=Carico.objects.filter(Q(bolla=bl),Q(idcod__produttore__azienda=seg[0]))
        if(pc):
            p=pc.filter().values("q","cassa","cassaexit","idcod__id","data")
            data=list(p)
            pc.delete()
            dt=data[0]["data"]
        s=Saldo.objects.all()
        cod=IDcod.objects.all()
  
        for item in line:
            diff=int(item["css"])
            csx=0
            if(data):
                for itemp in data:
                    if (int(item["id"])==int(itemp["idcod__id"])):
                        csx=int(itemp["cassaexit"])
                        diff=int(item["css"])-int(itemp["cassa"])
            s1=s.get(idcod_id=item["id"])
            qs=s1.q
            s1.q=qs+diff
            s1.save()
            codid=cod.get(id=item["id"])
            rec=Carico(q=item["ps"],cassa=item["css"],bolla=bl,idcod=codid,data=dt,cassaexit=csx)
            rec.save()
        return 2        
    
 