#import django
#django.setup()
from gestione.models import Produttore,IDcod,Carico,libro,sp,ce,saldocliente,ivacliente,ivaforn,saldoprod
from gestione.models import contocln,contofrn,contoce,contosp

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


class Estrazionecn:
    def Saldi(self,line):
        s1=0
        s2=0
        s3=0
        s4=0
        sca=""
        scd=""
        sba=""
        sbd=""
        sea=""
        sed=""
        scla=""
        scld=""
        sfra=""
        sfrd=""
        ls=[]
        rec=libro.objects.filter(dtreg__gte=line["datacn"]).values("conto","dare","avere","desc","dtreg")
        if(line["codcn"]=="1"):
            r1=rec.filter(conto="80.80")
            s1= r1.aggregate(Sum("avere"))
            r2=rec.filter(conto="72.72")
            s2= r2.aggregate(Sum("dare"))

            r3=rec.filter(conto="3.1")
            scla= r3.aggregate(Sum("avere"))
            scld= r3.aggregate(Sum("dare"))
            r4=rec.filter(conto="53.1")
            sfra= r4.aggregate(Sum("avere"))
            sfrd= r4.aggregate(Sum("dare"))
        
            ls.append(s1["avere__sum"])
            ls.append(s2["dare__sum"])
            ls.append(scla["avere__sum"])
            ls.append(scld["dare__sum"])
            ls.append(sfra["avere__sum"])
            ls.append(sfrd["dare__sum"])
            
        elif (line["codcn"]=="2"):
            r1=rec.filter(conto="1.1")
            sca= r1.aggregate(Sum("avere"))
            scd= r1.aggregate(Sum("dare"))

            r2=rec.filter(conto="1.2")
            sba= r2.aggregate(Sum("avere"))
            sbd= r2.aggregate(Sum("dare"))

            r3=rec.filter(conto="20.20")
            sea= r3.aggregate(Sum("avere"))
            sed= r3.aggregate(Sum("dare"))
        
            ls.append(sca["avere__sum"])
            ls.append(scd["dare__sum"])
            ls.append(sba["avere__sum"])
            ls.append(sbd["dare__sum"])
            ls.append(sea["avere__sum"])
            ls.append(sed["dare__sum"])
        return ls
    
    def Giornale(self,line):
        if(line["codcn"]=="0"):
            rec=libro.objects.filter(dtreg__gte=line["datacn"]).values("doc","prot","conto","dare","avere","desc","dtreg")
        else:                                 
            rec=libro.objects.filter(Q(dtreg__gte=line["datacn"]),Q(conto=line["codcn"])).values("doc","prot","conto","dare","avere","desc","dtreg")
        data=list(rec)
        return data
    
    @staticmethod
    def SaldoClienti():
        res=saldocliente.objects.values("attivo","passivo","cliente__azienda")
        data=list(res)
        return data

    @staticmethod
    def SaldoFrn():
        res=saldoprod.objects.values("attivo","passivo","prod__azienda")
        data=list(res)
        return data
    
    @staticmethod
    def Fatturato():
        res=ivacliente.objects.values("dtreg","nome","tot","imp","erario","saldo").order_by("dtreg")
        data=list(res)
        return data    
        
        

class Reportms:

    @staticmethod
    def Contims(cod):
        dic={}
        lsms=[]
        ls=[]
        lsms=cod["ms"].split(".")
        res=contocln.objects.filter(cod=lsms[0],sub=lsms[1])
        sumdare=res.aggregate(Sum("dare"))
        sumavere=res.aggregate(Sum("avere"))
        dic["dare"]=sumdare["dare__sum"]
        dic["avere"]=sumavere["avere__sum"]
        ls.append(dic)
        return ls