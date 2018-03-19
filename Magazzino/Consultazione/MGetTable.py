#import django
#django.setup()
from gestione.models import Produttore,IDcod,Carico,Sospese,ivaforn,ExCsBl
from django.db.models import Q,F,Sum
import os,time,openpyxl,subprocess,Registra,datetime,Pdf
from decimal import Decimal
from datetime import date

class GetData:
    def GetIdCodAll(self):
        rec=IDcod.objects.all().values("id","cod").order_by("cod")
        data=list(rec)
        return data
    def GetIdCod(self,message):
        rec=Carico.objects.filter(Q(idcod__produttore__azienda=message["res"]),Q(data__gte=message["res1"])).values("idcod__cod",
                                "q","cassa","bolla","data").order_by("bolla")
        data=list(rec)
        return data
    def GetCarico(self):
        rec=Carico.objects.all().values("bolla","idcod__produttore__azienda").order_by("bolla").distinct()
        data=list(rec)
        return data    
    def GetBolla(self,line):
        rec=Carico.objects.filter(Q(bolla=line["bolla"]), Q(idcod__produttore__id=line["cliente"])).values("idcod__id","idcod__cod","qn","cassa",
                                                                    "data","bolla","tara","excsbl__facc","excsbl__trasporto","excsbl__vari")
        data=list(rec)
        return data 
    def GetFatt(self,line):
        rec=Carico.objects.filter(fatt=line).values("idcod__produttore__azienda","idcod__genere__iva","costo","fattimp","bolla","idcod__cod","q","cassa","data")
        data=list(rec)
        return data 
    def GetIdCodbyProdotto(self,message):
        rec=Carico.objects.filter(Q(idcod__genere__nome=message["prd"]),Q(data__gte=message["data"])).values("idcod__cod",
                                "q","cassa","bolla","data").order_by("-idcod__cod")
        data=list(rec)
        return data
    def GetCaricoTotaleCv(self,x):
        rec="";
        if(x=='p'):
            rec=Carico.objects.filter(Q(p=0),Q(cassa__gt=F("cassaexit"))).values("idcod__cod","q","cassa","cassaexit","bolla","data").order_by("data","bolla")
        elif(x=="f"):
            rec=Carico.objects.filter(p=2).values("idcod__cod","q","cassa","cassaexit","bolla","data").order_by("data","bolla")
        elif(x=="c"):
            rec=self.GetBollaCvT()
        data=list(rec)
        return data    
    def GetCaricoTotale(self,message):
        beforefatt=""
        beforefrn=""
        #rec=Carico.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","q","cassa","bolla","data","cassa","cassaexit",
                                    #"fatt","pagato","fattimp","excsbl","idcod__produttore__azienda").order_by("bolla","idcod__produttore__azienda")
        rec=ExCsBl.objects.all().values("carico__bolla","carico__idcod__cod","q","cassa","carico__data","cassa","cassaexit",
                        "fatt","pagato","fattimp","id","carico__idcod__produttore__azienda").order_by("carico__bolla","carico__idcod__produttore__azienda").distinct()
        data=list(rec)

        return data    
    def GetCaricobyIdcod(self):
        dic={}
        s=Sospese.objects.values("idcod__id").annotate(css_sum=Sum("cassa")).exclude(id=1)
        c=Carico.objects.filter(cassa__gt=F("cassaexit")).values("tara","idcod__id","bolla","id","idcod__cod","cassa","cassaexit").order_by("bolla","data")
        d1=list(s)
        dic["sp"]=d1
        d2=list(c)
        dic["cr"]=d2
        return dic
    
    def GetBollaCv(self,nome):
        dic={}
        ls=[]
        ls1=[]
        c=Carico.objects.filter(Q(idcod__produttore__azienda=nome),Q(p=0)).order_by("bolla")
        cm1=c.filter(Q(cassa__gt=F("cassaexit")))
        data=list(cm1)
        cm2=cm1.values("bolla").distinct()
        for  item in cm2:
            ls.append(item["bolla"])
        cm1=c.filter(Q(cassa=F("cassaexit"))).values("excsbl__facc","excsbl__trasporto","excsbl__vari","id","idcod__genere__iva",
                                                         "idcod__cod","q","cassa","data","bolla","costo").order_by("bolla")
        for item in cm1:
            if(item["bolla"] in ls):
                continue
            ls1.append(item)
    
        frn=Produttore.objects.get(azienda=nome)
        dic["ct"]=frn.citta
        dic["pi"]=frn.pi
        dic["mrg"]=frn.margine
        dic["rg"]=frn.regione            
        ls1.append(dic)
        return ls1 

    def GetBolla1(self,ls,frn):
        ls1=[]
        dic={}
        for item in ls: 
            c=Carico.objects.filter(Q(bolla=item),Q(idcod__produttore__id=frn)).values("excsbl__facc","excsbl__trasporto","excsbl__vari","id","idcod__genere__iva",
                                   "qn","cassaexit","idcod__cod","q","cassa","data","bolla","costo","id").order_by("bolla")
            for item in c:
                ls1.append(item)            
            #ls1.append(list(c))    
            
            
        frn=Produttore.objects.get(id=frn)
        dic["ct"]=frn.citta
        dic["pi"]=frn.pi
        dic["mrg"]=frn.margine
        dic["rg"]=frn.regione            
        ls1.append(dic)
        return ls1 

    def GetBollaCv1(self,nome):
        rec=ExCsBl.objects.filter(Q(produttore=nome),Q(p=0)).values("bolla","data","facc","trasporto","vari",
                                    "cassa","cassaexit","produttore__margine")
        data=list(rec)
        return data
        
    def GetBollabyPrd(self,ls):
        rec=Carico.objects.filter(Q(bolla=ls["bolla"]),Q(idcod__produttore__id=ls["cln"])).values("idcod__cod","q","qn","cassa",
                                "cassaexit","bolla","tara","costo")
        data=list(rec)
        return data        


    def GetBollaCvT(self):
        ls=[]
        ls1=[]
        c=Carico.objects.filter(p__lte=1).order_by("bolla")
        cm1=c.filter(Q(cassa__gt=F("cassaexit")))
        cm2=cm1.values("bolla").distinct()
        for  item in cm2:
            ls.append(item["bolla"])
        cm11=c.filter(Q(cassa=F("cassaexit"))).values("idcod__id",
                                   "idcod__cod","q","cassa","cassaexit","data","bolla","costo","idcod__produttore__margine").order_by("bolla")
        for item in cm11:
            if(item["bolla"] in ls):
                continue
            ls1.append(item)
        return ls1     
    
    def PushBollaCv(self,line,cln,mrgn):
        bolla=""
        imp=0
        erario=0
        ls=[]
        lsbl=[]
        cliente=Produttore.objects.get(id=cln)
        ccv=Carico.objects.filter().values("cv").order_by("cv").last()
        c=Carico.objects.filter(Q(idcod__produttore__id=cln),Q(p=0)).values("id",
                                   "idcod__cod","q","cassa","data","bolla","costo","idcod__genere__iva","excsbl").order_by("bolla")
        fatt=ccv["cv"]+1
        for item in line:
            c1=c.filter(id=item["id"])
            ddt={}
            ddt['costo']=item["fatt"]
            ddt["cod"]=c1[0]["idcod__cod"]
            ddt["lotto"]=c1[0]["id"]
            ddt["ps"]=Decimal(item["psr"])
            ddt["css"]=c1[0]["cassa"]
            ddt["iva"]=c1[0]["idcod__genere__iva"]
            ddt["prz"]=Decimal(item["przr"])
           # ddt["prz"]=round(Decimal(item["fatt"])/Decimal(item["psr"]),2)
#            ddt["tara"]="0.2"
#            x=60
            #f = lambda x: ['small', 'big'][x>100]
            #lambda x: 'big' if x > 100 else 'small'
            if(c1[0]["bolla"]!=bolla):
                lsbl.append(c1[0]["bolla"])
            bolla=c1[0]["bolla"]
            x=ExCsBl.objects.get(id=c1[0]["excsbl"])
            x.fattimp+=Decimal(item["fatt"])
            x.p=1
            x.cv=fatt
            x.save()
            c1.update(fattcv=Decimal(item["fatt"]),p=1,cv=fatt,qcv=item["psr"])
            ls.append(ddt)
            lsblt="Bolle: "+" ".join(lsbl)
        obj=Pdf.PrintTable("CV",ls,0)
        obj.PrintCV()
        obj.PrintAna(str(fatt),cliente,lsblt)         
        return
    
    def PushFattFrn(self,line,ft,frn,mrgn,cst):
        c=Carico.objects.filter(Q(idcod__produttore__azienda=frn),Q(p=1)).order_by("cv")
        for item in line:
            c1=c.filter(cv=item)
            c1.update(p=2,fatt=ft,mrg=mrgn,fattimp=cst)
        return
    
    def GetCvbyPrd(self,line):
        dic={}
        if(line["chc"]=="bl"):
            chc=0
            rec=ExCsBl.objects.filter(Q(cv=0),Q(produttore__id=line["cln"]))
        else:
            chc=1
            rec=ExCsBl.objects.filter(Q(p__lte=2),Q(cv__gt=0),Q(produttore__id=line["cln"]))
        r2=rec.values("carico__bolla","carico__cv","carico__mrg","carico__data").order_by("carico__cv").distinct()
        frn=Produttore.objects.get(id=line["cln"])
        dic["ct"]=frn.citta
        dic["pi"]=frn.pi
        dic["mrg"]=frn.margine
        dic["rg"]=frn.regione
        data=list(r2)
        data.append(dic)
        return data 
    
    def GetCvFatt(self,line):
        if(line["ch"]=="cv"):
            rec=Carico.objects.filter(cv=line["cvd"]).values("qn","idcod__genere__iva","id","idcod__cod","q","cassa","data","costo","bolla","fattimp").order_by("bolla")
        else:
            rec=Carico.objects.filter(Q(bolla=line["cvd"]),Q(idcod__produttore__id=line["frn"])).values("qn","idcod__genere__iva","id","idcod__cod","q","cassa","data","costo","bolla","fattimp").order_by("bolla")
        data=list(rec)
        return data
    def SaveCvFatt(self,cvls,ft,frn,mrgg,data=date.today(),idfrn=0):
        imp=0
        erario=0
        cst=0
        fattimp=0
        res=Carico.objects.filter(Q(p__lte=1),Q(idcod__produttore__id=idfrn))# azienda->id
        for item in cvls:
            rec=res.get(id=item["id"])
            rec.fattimp=Decimal(item["vnd"])
            rec.fatt=ft
            rec.mrg=mrgg
            rec.datafatt=data
            rec.p=2
            rec.save()
            x=ExCsBl.objects.get(id=rec.excsbl_id)
            fattimp+=Decimal(item["vnd"])
            x.fatt=ft
            x.p=2
            x.datafatt=data
            imp+=Decimal(item["vnd"])
            erario+=Decimal(item["vnd"])*(Decimal(item["iva"]))
        x.fattimp=fattimp
        x.save()
        f=Produttore.objects.get(id=idfrn)
        res=Registra.ComVen(0,0,imp,erario,"33.03.01",0,f,ft,"55.01.07",data,idfrn)
 #       res.Acquisto()
        res.Acquistoms()
        res.SetErarioForn()   
        return 0
    
    def GetFattFrn(self,message):
        erario=0
        imp=0
        dt=""
        frn=""
        somma=0
        beforefatt=" "
        beforefrn=" "
        i=0
        ll=[]
        recls=Carico.objects.filter(Q(data__gte=message["data"]),Q(p=2),Q(pagato=0)).values("pagato","idcod__produttore__azienda","fattimp"
                                ,"fatt","data","idcod__genere__iva","note","idcod__produttore__id").order_by("fatt")
        if(len(recls)==0):
            return 1
        for el in recls:
            if((el["fatt"]!=beforefatt)  or (el["idcod__produttore__id"]!=beforefrn)):
                if(beforefatt!=" "):
                    dic={}
                    dic["fatt"]=beforefatt
                    dic["imp"]=imp
                    dic["erario"]=erario
                    dic["frn"]=frn
                    dic["idfrn"]=idfrn
                    dic["dt"]=dt
                    dic["dtadd"]=dt+datetime.timedelta(days=15)
                    dic["note"]=note
                    dic["pg"]=pg
                    dic["saldo"]=ss.saldo
                    ll.append(dic)
                erario=0
                imp=0
                imp+=el["fattimp"]
                erario+=el["fattimp"]*el["idcod__genere__iva"]
                frn=el["idcod__produttore__azienda"]
                idfrn=el["idcod__produttore__id"]
                dt=el["data"]
                note=el["note"]
                pg=el["pagato"]
                ss=ivaforn.objects.get(Q(fatt=el["fatt"]),Q(nome=el["idcod__produttore__id"]))
            else:
                imp+=el["fattimp"]
                erario+=el["fattimp"]*el["idcod__genere__iva"]
            beforefatt=el["fatt"]
            beforefrn=el["idcod__produttore__id"]
        dic={}
        dic["fatt"]=beforefatt
        dic["imp"]=imp
        dic["erario"]=erario
        dic["frn"]=frn
        dic["idfrn"]=idfrn
        dic["dt"]=dt
        dic["dtadd"]=dt+datetime.timedelta(days=15)
        dic["note"]=note
        dic["pg"]=pg
        dic["saldo"]=ss.saldo
        ll.append(dic)
        return ll
    
    def Pagato(self,line):
        imp=0
        erario=0
        s=Carico.objects.filter(Q(fatt=line["pg"]),Q(idcod__produttore__id=line["idfrn"]))
        s.update(pagato=line["pgm"],note=line["nt"])
        s1=s.values("fattimp","idcod__genere__iva","idcod__produttore__azienda","datafatt","excsbl_id")
        x=ExCsBl.objects.get(id=s1[0]["excsbl_id"])
        x.pagato=line["pgm"]
        x.save()
        for item in s1:
            imp+=item["fattimp"]
            erario+=item["fattimp"]*(item["idcod__genere__iva"])
        f=Produttore.objects.get(id=line["idfrn"])
        res=Registra.ComVenBnc(line["chc"],line["part"],imp,erario,"33.03.01",0,line["pg"],s1[0]["datafatt"],f,line["idfrn"])
   #     res.putfrn()
        res.putfrnms()
