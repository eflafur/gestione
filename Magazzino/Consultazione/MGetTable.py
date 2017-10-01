#import django
#django.setup()
from gestione.models import Produttore,IDcod,Carico
from django.db.models import Q,F
import os,time,openpyxl,subprocess,decimal

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
        rec=Carico.objects.filter(Q(bolla=line[0]), Q(idcod__produttore__azienda=line[1])).values("idcod__id","idcod__cod","q","cassa","data","bolla")
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
        rec=Carico.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","q","cassa","bolla","data").order_by("bolla")
        data=list(rec)
        return data    
    def GetCaricobyIdcod(self):
        rec=Carico.objects.filter(cassa__gt=F("cassaexit")).values("bolla","id","idcod__cod","cassa","cassaexit").order_by("bolla","data")
        data=list(rec)
        return data
    def GetBollaCv(self,nome):
        dic={}
        ls=[]
        ls1=[]
        c=Carico.objects.filter(Q(idcod__produttore__azienda=nome),Q(p=0)).order_by("bolla")
        cm1=c.filter(Q(cassa__gt=F("cassaexit")))
        cm2=cm1.values("bolla").distinct()
        for  item in cm2:
            ls.append(item["bolla"])
        cm1=c.filter(Q(cassa=F("cassaexit"))).values("id",
                                   "idcod__cod","q","cassa","data","bolla","costo","idcod__produttore__margine").order_by("bolla")
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
    #def GetBollaCvP(self):
        #ls=[]
        #ls1=[]
        #c=Carico.objects.filter(p=0).order_by("bolla")
        #cm1=c.filter(Q(cassa=F("cassaexit")))
        #cm2=cm1.values("bolla").distinct()
        #for  item in cm2:
            #ls.append(item["bolla"])
        #cM1=c.filter(Q(cassa__gt=F("cassaexit"))).values("idcod__id",
                                   #"idcod__cod","q","cassa","cassaexit","data","bolla","costo","idcod__produttore__margine").order_by("bolla")
        #for item in cM1:
            #if(item["bolla"] in ls):
                #continue
            #ls1.append(item)
        #return ls1     

    
    def PushBollaCv(self,line,cln,mrgn):
        ls=[]
        cliente=Produttore.objects.get(azienda=cln)
        ccv=Carico.objects.filter().values("cv").order_by("cv").last()
        c=Carico.objects.filter(Q(idcod__produttore__azienda=cln),Q(p=0)).values("id",
                                   "idcod__cod","q","cassa","data","bolla","costo","idcod__genere__iva").order_by("bolla")
        fatt=ccv["cv"]+1
        for item in line:
            ddt={}
            c1=c.filter(id=item["id"])
            ddt['costo']=float(item["cst"])
            ddt["cod"]=c1[0]["idcod__cod"]
            ddt["lotto"]=c1[0]["bolla"]
            ddt["ps"]=c1[0]["q"]
            ddt["css"]=c1[0]["cassa"]
            ddt["iva"]=c1[0]["idcod__genere__iva"]
            c1.update(fattimp=float(item["cst"]),mrg=mrgn,p=1,cv=fatt)
            ls.append(ddt)
        self.stampaFattura("vostra fattura",cliente,ls,mrgn)
        return
    
    def PushFattFrn(self,line,ft,frn,mrgn,cst):
        c=Carico.objects.filter(Q(idcod__produttore__azienda=frn),Q(p=1)).order_by("cv")
        for item in line:
            c1=c.filter(cv=item)
            c1.update(p=2,fatt=ft,mrg=mrgn,fattimp=cst)
        return
    
    def GetCvbyPrd(self,cln):
        dic={}
        rec=Carico.objects.filter(Q(idcod__produttore__azienda=cln),Q(p=1)).values("bolla","cv","mrg","data").order_by("cv").distinct()
        frn=Produttore.objects.get(azienda=cln)
        dic["ct"]=frn.citta
        dic["pi"]=frn.pi
        dic["mrg"]=frn.margine
        dic["rg"]=frn.regione
        data=list(rec)
        data.append(dic)
        return data 
    
    def GetCvFatt(self,cvd):
        rec=Carico.objects.filter(cv=cvd).values("id","idcod__cod","q","cassa","data","costo","bolla","fattimp").order_by("bolla")
        data=list(rec)
        return data
    def SaveCvFatt(self,cvls,ft,frn):
        cst=0
        res=Carico.objects.filter(Q(p__lte=1),Q(idcod__produttore__azienda=frn))
        #try:
            #r=res.get(fatt=ft)
        #except IndexError:
            #return 1
        r=res.filter(fatt=ft)
        if (r.exists()):
            for item in cvls:
                rec=res.get(id=item["id"])
                cst=float(item["cst"])
                rec.fattimp=cst
                rec.fatt=ft
                rec.p=2
                rec.save()
        else:
            return 1
        return 0

    def stampaFattura(self,nFattura, cln, righeFattura,mrg):
        """ produce fattura in excel """
        venditore={'venditore': 'Società ORTOFRUTTICOLA', 'P-IVA': "1234567890", 'indirizzo':'via dei Tigli, 8','città':'Milano','telefono':'02555555'}
    
        data=time.strftime("%d/%m/%Y")
        try:
            fa=openpyxl.load_workbook('formFattura.xlsx')
        except:
            print("file 'formFattura.xlsx' errato o mancante in "+os.getcwd())
            return
    
        sheet=fa.get_sheet_by_name('Sheet1')
    
        sheet['I3'].value = nFattura
        sheet['I4'].value = data
    
        sheet['B2'].value = venditore['venditore']
        sheet['B3'].value = venditore['P-IVA']
        sheet['B4'].value = venditore['indirizzo']
        sheet['B5'].value = venditore['città']
        sheet['B6'].value = venditore['telefono']
    
        sheet['B8'].value = cln.azienda
        sheet['B9'].value = cln.pi
        sheet['B10'].value = cln.indirizzo
    
        line=16												
        cntr=0
        total=0
        for riga in righeFattura:
            sheet["B"+str(line+cntr)].value = riga['cod']
            sheet["C"+str(line+cntr)].value = riga['lotto']
            sheet["D"+str(line+cntr)].value = riga['ps']
            sheet["E"+str(line+cntr)].value = riga['css']
            sheet["G"+str(line+cntr)].value = riga['iva']
            sheet["H"+str(line+cntr)].value = mrg
            subtotale =riga['costo']
            sheet["I"+str(line+cntr)].value = subtotale
            total+=subtotale
            cntr+=1
        cntr+=1
        sheet["H"+str(line+cntr)].value = "TOTALE"							
        sheet["I"+str(line+cntr)].value = total							
    
        try:
            fa.save('nuovaFattura.xlsx')
        except:
            print("file 'nuovaFattura.xls' errato o mancante in "+os.getcwd())
            return
    
        subprocess.call(["/usr/lib/libreoffice/program/soffice.bin", "nuovaFattura.xlsx"])
