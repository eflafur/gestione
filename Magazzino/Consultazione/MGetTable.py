from gestione.models import Produttore,IDcod,Carico
from django.db.models import Q,F
import os,time,openpyxl,subprocess

class GetData:
    def GetIdCod(self,message):
        rec=Carico.objects.filter(Q(idcod__produttore__azienda=message["res"]),Q(data__gte=message["res1"])).values("idcod__cod",
                                "q","cassa","bolla","data").order_by("bolla")
        data=list(rec)
        return data
    def GetCarico(self):
        rec=Carico.objects.all().values("bolla","idcod__produttore__azienda").order_by("bolla")
        data=list(rec)
        return data    
    def GetBolla(self,line):
        rec=Carico.objects.filter(Q(bolla=line[0]), Q(idcod__produttore__azienda=line[1])).values("idcod__id","idcod__cod","q","cassa","data","bolla")
        data=list(rec)
        return data 
    def GetIdCodbyProdotto(self,message):
        rec=Carico.objects.filter(Q(idcod__genere__nome=message["prd"]),Q(data__gte=message["data"])).values("idcod__cod",
                                "q","bolla","data").order_by("-idcod__cod")
        data=list(rec)
        return data
    def GetCaricoTotale(self,message):
        rec=Carico.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","q","cassa","bolla","data").order_by("bolla")
        data=list(rec)
        return data    
    def GetCaricobyIdcod(self):
        rec=Carico.objects.filter(cassa__gt=F("cassaexit")).values("bolla","id","idcod__cod","cassa","cassaexit").order_by("idcod_id","data")
        data=list(rec)
        return data
    def GetBollaCv(self,nome):
        ls=[]
        ls1=[]
        c=Carico.objects.filter(Q(idcod__produttore__azienda=nome)).order_by("bolla")
        cm1=c.filter(Q(cassa__gt=F("cassaexit")))
        cm2=cm1.values("bolla").distinct()
        for  item in cm2:
            ls.append(item["bolla"])
        cM1=c.filter(Q(cassa=F("cassaexit"))).values("idcod__id",
                                   "idcod__cod","q","cassa","data","bolla","costo","idcod__produttore__margine").order_by("bolla")
        m=Produttore.objects.get(azienda=nome)
        for item in cM1:
            if(item["bolla"] in ls):
                continue
#            item["netto"]=float(item["costo"])*(1-float(item["idcod__produttore__margine"])/100)
            ls1.append(item)
        return ls1 
    
    def PushBollaCv(self,line,cln,mrg):
        ls=[]
        cliente=Produttore.objects.get(azienda=cln)
        c=Carico.objects.filter(Q(idcod__produttore__azienda=cln)).values("idcod__id",
                                   "idcod__cod","q","cassa","data","bolla","costo","idcod__genere__iva").order_by("bolla")
        for item in line:
            c1=c.filter(bolla=item)
            data=list(c1)
            for item1 in c1:
                ddt={}
                costo=float(item1["costo"])*(1-float(mrg)/100)
                ddt["cod"]=item1["idcod__cod"]
                ddt["lotto"]=item1["bolla"]
                ddt["ps"]=item1["q"]
                ddt["css"]=item1["cassa"]
                ddt["iva"]=item1["idcod__genere__iva"]
                ddt["prz"]=costo
                ls.append(ddt)
        self.stampaFattura("vostra fattura",cliente,ls,mrg)
        return
                

    def stampaFattura(self,nFattura,cln, righeFattura,mrg):
        venditore={'venditore': 'Società ORTOFRUTTICOLA', 'P-IVA': "1234567890", 'indirizzo':'via dei Tigli, 8','città':'Milano','telefono':'02555555'}
        cliente={}
        cliente["azienda"]=cln.azienda         
        cliente["pi"]=cln.pi         
        cliente["indirizzo"]=cln.indirizzo         
        
        data=time.strftime("%d/%m/%Y")
        a=os.getcwd()
        try:
            fa=openpyxl.load_workbook('formFattura.xlsx')
        except:
            print("file formFattura.xls errato o mancante")
            return
    
        sheet=fa.get_sheet_by_name('Sheet1')
    
        sheet['F3'].value = "vostro numero"
        sheet['F4'].value = data
    
        sheet['B2'].value = venditore['venditore']
        sheet['B3'].value = venditore['P-IVA']
        sheet['B4'].value = venditore['indirizzo']
        sheet['B5'].value = venditore['città']
        sheet['B6'].value = venditore['telefono']
    
        sheet['B8'].value = cliente['azienda']
        sheet['B9'].value = cliente['pi']
        sheet['B10'].value = cliente['indirizzo']
        #sheet['B11'].value = cliente['città']
        #sheet['B12'].value = cliente['telefono']
    
        line=16												# riga primo articolo
        cntr=0
        total=0
        for riga in righeFattura:
            sheet["B"+str(line+cntr)].value = riga['cod']
            sheet["C"+str(line+cntr)].value = riga['lotto']
            sheet["D"+str(line+cntr)].value = riga['ps']
            sheet["E"+str(line+cntr)].value = riga['css']
            sheet["F"+str(line+cntr)].value = riga['prz']
            sheet["G"+str(line+cntr)].value = mrg
            subtotale=float(riga['prz'])*float(riga['ps'])
            sheet["H"+str(line+cntr)].value = subtotale
            total+=subtotale
            cntr+=1
    
        sheet["F25"].value = total							# riga totale per il momento hardcoded a cella F25
    
        fa.save('nuovaFattura.xlsx')
        subprocess.call(["/usr/lib/libreoffice/program/soffice.bin", "nuovaFattura.xlsx"])
                        