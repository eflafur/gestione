#import django
#django.setup()
from gestione.models import Produttore,IDcod,Carico
from django.db.models import Q,F,Sum
import os,time,openpyxl,subprocess,decimal

    

class GetReport:
    def BTot(self,line):
        dic={}
        dic1={}
        ls=[]
        rec=Carico.objects.filter(Q(data__gte=line["data"]),Q(p__gte=line["tipo"])).values("costo","fattimp","data").order_by("data")
        rcst = rec.aggregate(Sum("costo"))
        rcft = rec.aggregate(Sum("fattimp"))
        cscst= rec.aggregate(Sum("cassa"))
        csft= rec.aggregate(Sum("cassaexit"))
        dic["diffcst"]=rcst["costo__sum"]-rcft["fattimp__sum"]
        dic1["diffcs"]=cscst["cassa__sum"]-csft["cassaexit__sum"]
        ls.append(dic)
        ls.append(dic1)
        return ls    
    def BArt(self,line):
        rec=Carico.objects.filter(Q(data__gte=line["data"]),Q(idcod__id=line["artid"])).values("costo","fattimp","idcod__cod","q","cassa","cassaexit","bolla","data")
        try:
            rcst = rec.aggregate(Sum("costo"))
            rcft = rec.aggregate(Sum("fattimp"))
            diff=rcst["costo__sum"]-rcft["fattimp__sum"]
        except :
            diff=0
        return diff
    
    def BTotArt(self,line):
        ls=[]
        before=""
        sumft=0
        sumcs=0
        sumcasse=0
        sumcassex=0
        frn=""
        cod="" 
        rec=Carico.objects.filter(Q(data__gte=line["data"]),Q(p__gte=line["tipo"])).values("cassa","cassaexit","idcod__produttore__azienda","costo","fattimp","idcod__cod","idcod__id").order_by("idcod__id")#,"q","cassa","cassaexit","bolla","data")
        for item in rec:
            dic={}
            if(before==item["idcod__id"] or before==""):
                sumcs=sumcs+item["costo"]
                sumft=sumft+item["fattimp"]
                sumcasse=sumcasse+item["cassa"]
                sumcassex=sumcassex+item["cassaexit"]
            else:
                dic["diff"]=sumcs-sumft
                dic["diffcasse"]=sumcasse-sumcassex
                dic["cod"]=cod
                dic["frn"]=item["idcod__produttore__azienda"]
                ls.append(dic)
                sumcs=item["costo"]
                sumft=item["fattimp"]
                sumcasse=sumcasse+item["cassa"]
                sumcassex=sumcassex+item["cassaexit"]
            before=item["idcod__id"]
            cod=item["idcod__cod"]
        return ls

    def BFrn(self,line):
        ls=[]
        before=""
        sumft=0
        sumcs=0
        sumcasse=0
        sumcassex=0
        frn=""
        cod="" 
        rec=Carico.objects.filter(Q(data__gte=line["data"]),Q(p__gte=line["tipo"])).values("cassa","cassaexit","idcod__produttore__azienda","costo","fattimp","idcod__cod","idcod__produttore__id").order_by("idcod__produttore__id")#,"q","cassa","cassaexit","bolla","data")
        for item in rec:
            dic={}
            if(before==item["idcod__produttore__id"] or before==""):
                sumcs=sumcs+item["costo"]
                sumft=sumft+item["fattimp"]
                sumcasse=sumcasse+item["cassa"]
                sumcassex=sumcassex+item["cassaexit"]
            else:
                dic["diff"]=sumcs-sumft
                dic["diffcasse"]=sumcasse-sumcassex
                dic["frn"]=item["idcod__produttore__azienda"]
                ls.append(dic)
                sumcs=item["costo"]
                sumft=item["fattimp"]
                sumcasse=sumcasse+item["cassa"]
                sumcassex=sumcassex+item["cassaexit"]
            before=item["idcod__produttore__id"]
        return ls
