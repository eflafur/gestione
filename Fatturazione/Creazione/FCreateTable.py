import django
django.setup()
from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo,Carico,trasporto
from decimal import Decimal
from django.db.models import Q,F
import openpyxl,time,os,subprocess

class Modelddt:
    def __init__(self,ddt,q,prezzo,data,lotto,cassa,iva):
        self.ddt=ddt
        self.q=q
        self.prezzo=prezzo
        self.data=data
        self.lotto=lotto
        self.cassa=cassa
        self.iva=iva
        
class Produt:
    def put(self,line,azn):
        self.row=line
        p=Cliente.objects.filter(azienda=azn) 
        if (p):
            return (2)
        p=Cliente.objects.create(
            azienda=azn,
            citta=self.row["a4"],
            regione=self.row["a3"],
            pi=self.row["a2"],
            indirizzo=self.row["a7"],
            acquisizione=self.row["a5"],
            email=self.row["a6"],
            trpag=self.row["a9"],
            tel=self.row["a8"],
        )
        return (1)
    
    def ScriviFattura(self,line,sps):
        res=0
        i=0
        vnd={}
        bl=[]
        ls=[]
        lotto=Carico.objects.filter(cassa__gt=F("cassaexit")).order_by("id")
        if(sps!=""):
            rec=Sospese.objects.filter(fatturas=sps)
            rec.delete()
        s=Scarico.objects.latest("id")
        f=(s.fattura).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        for item in line:
            c=Cliente.objects.get(azienda=item["cln"])
            cod=IDcod.objects.get(cod=item["cod"])
            iva1=float(item["iva"])-1
            rec1=Saldo.objects.get(idcod__cod=item["cod"])
            rec1.q=rec1.q-(int(item["css"]))
            if(rec1.q<0):
                ls.append(item["cod"])
            rec1.save()
            ltcod=lotto.filter(idcod__cod=item["cod"])
            data=list(ltcod)
            if("lotto" in item):
                ltt=int(item["lotto"])
            else:
                ltt=ltcod[0].id
            ltid=ltcod.get(id=ltt)
            bl.append(ltt)
            num=ltid.cassa-(int(item["css"])+ltid.cassaexit)
            prz=Decimal(item["prz"])
            ps=Decimal(item["ps"])
            css=int(item["css"])
            if(num>=0):
                ltid.cassaexit=css+ltid.cassaexit
                ltid.costo=ltid.costo+ps*prz
                ltid.save()
            else:
                qc=ps/css
                cst=ltid.costo+prz*qc*(num+css)
                ltid.costo=cst
                ltid.cassaexit=ltid.cassa
                ltid.save()
                res=self.Rec(ltcod,num*(-1),0,ltt,bl,qc,prz)
                if(res==0):
                    return
            rec=Scarico(idcod=cod,cliente=c,prezzo=prz,q=ps,cassa=css,
                                    fattura=fatt,lotto=ltt,iva=iva1)
            rec.save()
            line[i]["lotto"]=str(ltt)
            i=i+1
        rg=list(line)
        venditore={'venditore': 'Società ORTOFRUTTICOLA', 'P-IVA': "1234567890", 'indirizzo':'via dei Tigli, 8','città':'Milano','telefono':'02555555'}
        cln=Cliente.objects.get(azienda=item["cln"])
        self.stampaFattura(fatt,venditore,cln,rg)
        return res
    
    
    
    def ScriviDDT(self,line,sps):
        i=0
        res=0
        bl=[]
        ls=[]
        lotto=Carico.objects.filter(cassa__gt=F("cassaexit")).order_by("id")
        s=trasporto.objects.latest("id")
        f=(s.ddt).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        for item in line:
            c=Cliente.objects.get(azienda=item["cln"])
            cod=IDcod.objects.get(cod=item["cod"])
            rec1=Saldo.objects.get(idcod__cod=item["cod"])
            rec1.q=rec1.q-(int(item["css"]))
            if(rec1.q<0):
                ls.append(item["cod"])
            rec1.save()
            ltcod=lotto.filter(idcod__cod=item["cod"])
            if("lotto" in item):
                ltt=int(item["lotto"])
            else:
                ltt=ltcod[0].id
            ltid=ltcod.get(id=ltt)
            bl.append(ltt)
            num=ltid.cassa-(int(item["css"])+ltid.cassaexit)
            prz=Decimal(item["prz"])
            ps=Decimal(item["ps"])
            css=int(item["css"])
            if(num>=0):
                ltid.cassaexit=css+ltid.cassaexit
                ltid.costo=ltid.costo+ps*prz
                ltid.save()
            else:
                qc=ps/css
                cst=ltid.costo+prz*qc*(num+css)
                ltid.costo=cst
                ltid.cassaexit=ltid.cassa
                ltid.save()
                res=self.Rec(ltcod,num*(-1),0,ltt,bl,qc,prz)
            rec=trasporto(idcod=cod,cliente=c,prezzo=prz,q=ps,cassa=css,
                        ddt=fatt,lotto=ltt)
            rec.save()
            line[i]["lotto"]=str(ltt)
            i=i+1
        rg=list(line)
        venditore={'venditore': 'Società ORTOFRUTTICOLA', 'P-IVA': "1234567890", 'indirizzo':'via dei Tigli, 8','città':'Milano','telefono':'02555555'}
        cln=Cliente.objects.get(azienda=item["cln"])
        self.stampaFattura(fatt,venditore,cln,rg)            
        return res
    
    def Rec(self,lotti,casse,i,lotto,bl,qc,prz):
        data=list(lotti)
        try:
            num=lotti[i].cassa-(lotti[i].cassaexit+casse)
        except IndexError:
            return 0
        if(num>=0 and lotti[i].id!=lotto):
            bl.append(lotti[i].id)
#            lt1=lotti.get(id=lotti[i].id)
            lotti[i].cassaexit=lotti[i].cassaexit+casse
            lotti[i].costo=lotti[i].costo+prz*qc*casse
            lotti[i].save()
            #lt1.cassaexit=lotti[i].cassaexit+casse
            #lt1.save()
            return bl
        else:
            if(lotti[i].id!=lotto):
                bl.append(lotti[i].id)
                #lt1=lotti.get(id=lotti[i].id)
                #lt1.cassaexit=lotti[i].cassa
                #lt1.save()
                lotti[i].costo=lotti[i].costo+prz*qc*(num+casse)
                lotti[i].cassaexit=lotti[i].cassa
                lotti[i].save()
            else:
                num=casse*(-1)
            i=i+1
            res=self.Rec(lotti,num*(-1),i,lotto,bl,qc,prz)
        return res

    def stampaFattura(self,nFattura, venditore, cln, righeFattura):
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
    
        sheet['F3'].value = nFattura
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
            sheet["G"+str(line+cntr)].value = riga['iva']
            subtotale=float(riga['prz'])*float(riga['ps'])
            sheet["H"+str(line+cntr)].value = subtotale
            total+=subtotale
            cntr+=1
    
        sheet["F25"].value = total							# riga totale per il momento hardcoded a cella F25
    
        fa.save('nuovaFattura.xlsx')
        subprocess.call(["/usr/lib/libreoffice/program/soffice.bin", "nuovaFattura.xlsx"])
        

    def ScriviSospesa(self,line,sps):
        if(sps!=" "):
            rec=Sospese.objects.filter(fatturas=sps)
            rec.delete()        
        s=Sospese.objects.latest("id")
        f=(s.fatturas).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        for item in line:
            c=Cliente.objects.get(azienda=item["cln"])
            cod=IDcod.objects.get(cod=item["cod"])
            rec=Sospese(idcod=cod,cliente=c,prezzo=item["prz"],q=item["ps"],cassa=item["css"],
                        fatturas=fatt,lotto=item["lotto"])
            rec.save()
        return
    
#evidenzia tutte le righe della sopsesa *1    
    #def GetSospesa(self,message):
        #recls=Sospese.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","q","fatturas","data","prezzo","cliente__azienda")
        #data=list(recls)
        #return data
    
    def GetSospesa(self,message):
        somma=0
        before=" "
        i=0
        ll=[]
        ss=[]
        if(message["cliente"]!=" "):
            recls=Sospese.objects.filter(Q(data__gte=message["data"]) , Q(cliente__azienda=message["cliente"])).values("idcod__cod","idcod__genere__iva","q","cassa","fatturas","data","prezzo","cliente__azienda")
        else:
            recls=Sospese.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","idcod__genere__iva","q","cassa","fatturas","data","prezzo","cliente__azienda")
        
        for el in recls:
            if(el["fatturas"]=="sc2018-0"):
                continue
            iva=el["idcod__genere__iva"]+1
            if(el["fatturas"]!=before):
                if(before!=" "):
                    ll.append(somma)
                somma=0
                somma=somma+el["prezzo"]*el["q"]*iva
            else:
                somma=somma+el["prezzo"]*el["q"]*iva
            before=el["fatturas"]
        
        ll.append(somma)
        before=" "
        i=0
        
        for item in recls:
            if(item["fatturas"]=="sc2018-0"):
                continue
            if (item["fatturas"]!=before):
                item["valore"]=ll[i]
                ss.append(item)
                i=i+1
            before=item["fatturas"]
        return ss    
    
    
    def GetFattura(self,message):
        somma=0
        before=" "
        i=0
        ll=[]
        ss=[]
        if(message["cliente"]!= ""):
            recls=Scarico.objects.filter(Q(data__gte=message["data"]) , Q(cliente__azienda=message["cliente"])).values("idcod__cod","idcod__genere__iva","q","cassa","fattura","data","prezzo","cliente__azienda")
        else:
            recls=Scarico.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","idcod__genere__iva","q","cassa","fattura","data","prezzo","cliente__azienda")
        
        for el in recls:
            if(el["fattura"]=="fc2018-0"):
                continue
            iva=el["idcod__genere__iva"]+1
            if(el["fattura"]!=before):
                if(before!=" "):
                    ll.append(somma)
                somma=0
                somma=somma+el["prezzo"]*el["q"]*iva
            else:
                somma=somma+el["prezzo"]*el["q"]*iva
            before=el["fattura"]
        
        ll.append(somma)
        before=" "
        i=0
        
        for item in recls:
            if(item["fattura"]=="fc2018-0"):
                continue     
            if (item["fattura"]!=before):
                item["valore"]=ll[i]
                ss.append(item)
                i=i+1
            before=item["fattura"]
        return ss        
    
    def GetFatturabyNum(self,num):
        recls=Scarico.objects.filter(fattura=num).values("idcod__cod","idcod__genere__iva","q","cassa","fattura","data","prezzo","cliente__azienda")
        data=list(recls)
        return data          
    
    
    def GetDdt(self,message):
        somma=0
        before=" "
        i=0
        ll=[]
        ss=[]
        if(message["cliente"]!=""):
            recls=trasporto.objects.filter(Q(cliente__azienda=message["cliente"]),Q(status=0)).values("idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
        else:
            recls=trasporto.objects.filter(Q(status=0)).values("idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
        
        for el in recls:
            if(el["ddt"]=="ddt2018-01"):
                continue
            iva=el["idcod__genere__iva"]+1
            if(el["ddt"]!=before):
                if(before!=" "):
                    ll.append(somma)
                somma=0
                somma=somma+el["prezzo"]*el["q"]*iva
            else:
                somma=somma+el["prezzo"]*el["q"]*iva
            before=el["ddt"]
        ll.append(somma)
        before=" "
        i=0
        
        for item in recls:
            if(item["ddt"]=="ddt2018-01"):
                continue
            if (item["ddt"]!=before):
                item["valore"]=ll[i]
                ss.append(item)
                i=i+1
            before=item["ddt"]
        return ss

    def GetDdtbyNum(self,num):
        recls=trasporto.objects.filter(ddt=num).values("idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
        data=list(recls)
        return data          
    
    
    def DdtEmit(self,ls):
        ddtls=[]
        ls1=[]
        trs=trasporto.objects.filter().values("ddt","q","prezzo","data","lotto","cassa",
                                "idcod__cod","cliente__azienda","idcod__genere__iva","status")
        for item in ls:
            i=0
            t=trs.filter(ddt=item)
            t.update(status=1)
            for el in t:
                prz=float(el["prezzo"])
                q=float(el["q"])
                iva=float(el["idcod__genere__iva"])
                dt=str(el["data"])
                if(i==1):
                    el["ddt"]=""
                m=Modelddt(el["ddt"],q,prz,dt,el["lotto"],el["cassa"],iva)
                ddtls.append(m)
                ls1.append(el)
                i=1
        self.Ddt2Fatt(ls1)
        return ddtls
            
        
    def Ddt2Fatt(self,line):
        ls=[]
        s=Scarico.objects.latest("id")
        f=(s.fattura).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        for item in line:
            c=Cliente.objects.get(azienda=item["cliente__azienda"])
            cod=IDcod.objects.get(cod=item["idcod__cod"])
            rec=Scarico(idcod=cod,cliente=c,prezzo=item["prezzo"],q=item["q"],cassa=item["cassa"],
                                    fattura=fatt,lotto=item["lotto"],iva=item["idcod__genere__iva"])
            rec.save()
        return ls        