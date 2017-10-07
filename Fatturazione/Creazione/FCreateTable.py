#import django
#django.setup()
from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo,Carico,trasporto
from decimal import Decimal
from django.db.models import Q,F
import openpyxl,time,os,subprocess

class Modelddt:
    def __init__(self,ddt,cod,q,prezzo,data,lotto,cassa,iva):
        self.ddt=ddt
        self.cod=cod
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
        lsecc=[]
        res=0
        i=0
        bl=[]
        ls=[]
        lotto=Carico.objects.filter(cassa__gt=F("cassaexit")).order_by("id")
        if(sps[:2]=="sp"):
            rec=Sospese.objects.filter(fatturas=sps)
            rec.delete()
        elif(sps[:2]=="fc"):
            rec=Scarico.objects.filter(fattura=sps)
            rec.delete()
            fatt=sps
        else:
            s=Scarico.objects.latest("id")
            f=(s.fattura).split("-")
            r=int(f[1])+1
            fatt=f[0]+"-"+str(r)
        for item in line:
            bl.clear()
            prz=Decimal(item["prz"])
            ps=Decimal(item["ps"])
            css=int(item["css"])
            iva1=float(item["iva"])-1
            c=Cliente.objects.get(azienda=item["cln"])
            cod=IDcod.objects.get(cod=item["cod"])
            ltcod=lotto.filter(idcod__cod=item["cod"])
            if(sps[:2]=="fc"):    
                rec=Scarico(idcod=cod,cliente=c,prezzo=prz,q=ps,cassa=css,
                                        fattura=fatt,lotto=item["lotto"],iva=iva1)
                csssps=css
                qc=ps/css
                bl.append(item["lotto"])
            else:                
                if(item["lotto"]!="" and sps==""):
                    ltt=int(item["lotto"])
                else:
                    try:
                        ltt=ltcod[0].id
                    except:
                        ecc={}
                        ecc["num"]=item["css"]
                        ecc["cod"]=item["cod"]
                        lsecc.append(ecc)
                        return lsecc
                ltid=ltcod[0]
                bl.append(ltt)
                num=ltid.cassa-(int(item["css"])+ltid.cassaexit)
                csssps=css
                qc=ps/css
                if(num>=0):
                    ltid.cassaexit=css+ltid.cassaexit
                    ltid.costo=ltid.costo+ps*prz
                    ltid.save()
                else:
                    cst=ltid.costo+prz*qc*(num+css)
                    ltid.costo=cst
                    ltid.cassaexit=ltid.cassa
                    ltid.save()
                    res=self.Rec(ltcod,num*(-1),0,ltt,bl,qc,prz)
                    if(res!=0 and sps!=""):
                        ecc={}
                        ecc["num"]=res
                        ecc["cod"]=item["cod"]
                        csssps=css-res
                        lsecc.append(ecc)
                qsps=qc*csssps
                rec1=Saldo.objects.get(idcod__cod=item["cod"])
                rec1.q=rec1.q-csssps
                rec1.save()
                rec=Scarico(idcod=cod,cliente=c,prezzo=prz,q=qsps,cassa=csssps,
                                        fattura=fatt,lotto=ltt,iva=iva1)
            rec.save()
            line[i]["lotto"]=bl.copy()
            line[i]["css"]=csssps
            line[i]["ps"]=qc*csssps
            i=i+1
        rg=list(line)
        self.stampaFattura(fatt,c,rg)
#        os.system("
        return lsecc
    
    def ScriviDDT(self,line,sps):
        c=""
        lsecc=[]
        i=0
        res=0
        bl=[]
        ls=[]
        lotto=Carico.objects.filter(cassa__gt=F("cassaexit")).order_by("id")
        if(sps[:2]=="sp"):
            rec=Sospese.objects.filter(fatturas=sps)
            rec.delete()
        elif(sps[:2]=="dd"):
            rec=trasporto.objects.filter(ddt=sps)
            rec.delete()
            fatt=sps
        else:
            s=trasporto.objects.latest("id")
            f=(s.ddt).split("-")
            r=int(f[1])+1
            fatt=f[0]+"-"+str(r)
        for item in line:
            bl.clear()
            prz=Decimal(item["prz"])
            ps=Decimal(item["ps"])
            css=int(item["css"])
            csssps=0
            c=Cliente.objects.get(azienda=item["cln"])
            cod=IDcod.objects.get(cod=item["cod"])
            ltcod=lotto.filter(idcod__cod=item["cod"])
            if(sps[:2]=="dd"):    
                rec=trasporto(idcod=cod,cliente=c,prezzo=prz,q=ps,cassa=css,
                      ddt=fatt,lotto=item["lotto"])
                csssps=css
                qc=ps/css
                bl.append(item["lotto"])
            else:                            
                if(item["lotto"]!="" and sps==""):
                    ltt=int(item["lotto"])
                else:
                    try:
                        ltt=ltcod[0].id
                    except:
                      #  lsecc.clear()
                        ecc={}
                        ecc["num"]=css
                        ecc["cod"]=item["cod"]
                        lsecc.append(ecc)
                        return lsecc
                ltid=ltcod.get(id=ltt)
#                ltid=ltcod[0]
                bl.append(ltt)
                num=ltid.cassa-(css+ltid.cassaexit)
                csssps=css
                qc=ps/css
                if(num>=0):
                    ltid.cassaexit=css+ltid.cassaexit
                    ltid.costo=ltid.costo+ps*prz
                    ltid.save()
                else:
                    cst=ltid.costo+prz*qc*(num+css)
                    ltid.costo=cst
                    ltid.cassaexit=ltid.cassa
                    ltid.save()
           #         vv1=list(ltcod)
                    res=self.Rec(ltcod,num*(-1),0,ltt,bl,qc,prz)
                    if(res!=0 and sps!=""):
                        ecc={}
                        ecc["num"]=res
                        ecc["cod"]=item["cod"]
                        csssps=css-res
                        lsecc.append(ecc)
                qsps=qc*csssps
                rec1=Saldo.objects.get(idcod__cod=item["cod"])
                rec1.q=rec1.q-csssps
                rec1.save()
                rec=trasporto(idcod=cod,cliente=c,prezzo=prz,q=qsps,cassa=csssps,
                            ddt=fatt,lotto=ltt)
            rec.save()
            line[i]["lotto"]=bl.copy()
            line[i]["css"]=csssps
            line[i]["ps"]=qc*csssps
            i=i+1
        rg=list(line)
        self.stampaFattura(fatt,c,rg)            
        return lsecc
    
    def Rec(self,lotti,casse,i,lotto,bl,qc,prz):
        num=0
 #       data=list(lotti)
        try:
            dd=lotti[i].id
        except IndexError:
            return casse
        num=lotti[i].cassa-(lotti[i].cassaexit+casse)
        if(num>=0 and lotti[i].id!=lotto):
            bl.append(lotti[i].id)
#            lt1=lotti.get(id=dd)
            lotti[i].cassaexit=lotti[i].cassaexit+casse
            lotti[i].costo=lotti[i].costo+prz*qc*casse
            lotti[i].save()
            #lt1.costo=lotti[i].costo+prz*qc*casse
            #lt1.cassaexit=lotti[i].cassaexit+casse
            #lt1.save()
#            return bl
            return 0
        else:
            if(lotti[i].id!=lotto):
                bl.append(lotti[i].id)
                #lt1=lotti.get(id=dd)
                #lt1.costo=lotti[i].costo+prz*qc*(num+casse)
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

    
    def stampaFattura(self,nFattura, cln, righeFattura):
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
            try:
                sheet["C"+str(line+cntr)].value = riga['ddt']
            except:
                a=10
            sheet["D"+str(line+cntr)].value=""
            for item in riga['lotto']:
                sheet["D"+str(line+cntr)].value = sheet["D"+str(line+cntr)].value+" "+str(item)

            sheet["E"+str(line+cntr)].value = riga['ps']
            sheet["F"+str(line+cntr)].value = riga['css']
            sheet["G"+str(line+cntr)].value = riga['prz']
            sheet["H"+str(line+cntr)].value = riga['iva']
            subtotale=float(riga['prz'])*float(riga['ps'])
            sheet["I"+str(line+cntr)].value = float(subtotale)
            total+=subtotale
            cntr+=1
    
        sheet["H"+str(line+cntr)].value = "TOTALE"							
        sheet["I"+str(line+cntr)].value = total							
    
        try:
            fa.save('nuovaFattura.xlsx')
        except:
            print("file 'nuovaFattura.xls' errato o mancante in "+os.getcwd())
            return
    
        subprocess.call(["/usr/lib/libreoffice/program/soffice.bin", "nuovaFattura.xlsx"])

    def ScriviSospesa(self,line,sps):
        if(sps!=""):
            rec=Sospese.objects.filter(fatturas=sps)
            rec.delete()        
            fatt=sps
        else:
            s=Sospese.objects.latest("id")
            f=(s.fatturas).split("-")
            r=int(f[1])+1
            fatt=f[0]+"-"+str(r)
#        lotto=Carico.objects.filter(cassa__gt=F("cassaexit")).order_by("id")
        for item in line:
            c=Cliente.objects.get(azienda=item["cln"])
            cod=IDcod.objects.get(cod=item["cod"])
#            ltcod=lotto.filter(idcod__cod=item["cod"])
 #           ltt=ltcod[0].id
            rec=Sospese(idcod=cod,cliente=c,prezzo=item["prz"],q=item["ps"],cassa=item["css"],
                        fatturas=fatt)
            rec.save()
        return
    
    
    
#evidenzia tutte le righe della sopsesa *1    
    #def GetSospesa(self,message):
        #recls=Sospese.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","q","fatturas","data","prezzo","cliente__azienda")
        #data=list(recls)
        #return data

    def RecFatt(self,message):
        somma=0
        before=" "
        i=0
        ll=[]
        ss=[]
        if(message["cliente"]!=" "):
            recls=Scarico.objects.filter(cliente__azienda=message["cliente"]).values("idcod__cod","idcod__genere__iva","q","cassa","fattura","data","prezzo","cliente__azienda")
        else:
            recls=Scarico.objects.filter().values("idcod__cod","idcod__genere__iva","q","cassa","fattura","data","prezzo","cliente__azienda")
        
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
    def RecDdt(self,message):
        somma=0
        before=" "
        i=0
        ll=[]
        ss=[]
        if(message["cliente"]!=" "):
            recls=trasporto.objects.filter(Q(data__gte=message["data"]),Q(cliente__azienda=message["cliente"]),Q(status=0)).exclude(id=1).values("idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
        else:
            recls=trasporto.objects.filter(Q(data__gte=message["data"]),Q(status=0)).exclude(id=1).values("idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
        for el in recls:
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
            if (item["ddt"]!=before):
                item["valore"]=ll[i]
                ss.append(item)
                i=i+1
            before=item["ddt"]
        return ss           
    
    def GetSospesa(self,message):
        somma=0
        before=" "
        i=0
        ll=[]
        ss=[]
        if(message["cliente"]!=" "):
            recls=Sospese.objects.filter(Q(data__gte=message["data"]),Q(cliente__azienda=message["cliente"])).exclude(id=158).values("idcod__cod","idcod__genere__iva","q","cassa","fatturas","data","prezzo","cliente__azienda").order_by("fatturas")
        else:
            recls=Sospese.objects.filter(Q(data__gte=message["data"])).exclude(id=158).values("idcod__cod","idcod__genere__iva","q","cassa","fatturas","data","prezzo","cliente__azienda").order_by("fatturas")
        
        for el in recls:
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
    
    
    def DdtEmit(self,ls,cln):
        ddtls=[]
        ls1=[]
        trs=trasporto.objects.filter(status=0).values("ddt","q","prezzo","data","lotto","cassa",
                                "idcod__cod","cliente__azienda","idcod__genere__iva","status","cliente__azienda")
#        data1=list(trs)
        trstrs=trs.annotate(cod=F("idcod__cod"),ps=F("q"),css=F("cassa"),prz=F("prezzo"),iva=F("idcod__genere__iva")).values("cod",
                                   "ps","css","prz","iva","data","lotto","ddt","cliente__azienda")
        for item in ls:
#            i=0
            t=trstrs.filter(ddt=item).values()
            data=list(t)
            t.update(status=1)
            for el in data:
                #if(i==1):
                    #el["ddt"]=""
                ddtls.append(el)
                i=1
        self.Ddt2Fatt(ddtls,cln)
        return ddtls
            
        
    def Ddt2Fatt(self,line,cliente):
        ls=[]
        s=Scarico.objects.latest("id")
        f=(s.fattura).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        cln=Cliente.objects.get(azienda=cliente)
        for item in line:
            cod=IDcod.objects.get(cod=item["cod"])
            rec=Scarico(idcod=cod,cliente=cln,prezzo=item["prz"],q=item["ps"],cassa=item["css"],
                                    fattura=fatt,lotto=item["lotto"],iva=item["iva"])
            rec.save()
            cln=Cliente.objects.get(azienda=cliente)
        self.stampaFattura(fatt,cln,line)
        return ls        
    
    
    
    
    
    
    #def ScriviDDT(self,line,sps):
        #c=""
        #lsecc=[]
        #i=0
        #res=0
        #bl=[]
        #ls=[]
        #lotto=Carico.objects.filter(cassa__gt=F("cassaexit")).order_by("id")
        #if(sps[:2]=="sp"):
            #rec=Sospese.objects.filter(fatturas=sps)
            #rec.delete()
        #elif(sps[:2]=="dd"):
            #rec=trasporto.objects.filter(ddt=sps)
            #rec.delete()
            #fatt=sps
        #else:
            #s=trasporto.objects.latest("id")
            #f=(s.ddt).split("-")
            #r=int(f[1])+1
            #fatt=f[0]+"-"+str(r)
        #for item in line:
            #bl.clear()
            #prz=Decimal(item["prz"])
            #ps=Decimal(item["ps"])
            #css=int(item["css"])
            #csssps=0
            #c=Cliente.objects.get(azienda=item["cln"])
            #cod=IDcod.objects.get(cod=item["cod"])
            #ltcod=lotto.filter(idcod__cod=item["cod"])
            #if(sps[:2]=="dd"):    
                #rec=trasporto(idcod=cod,cliente=c,prezzo=prz,q=ps,cassa=css,
                      #ddt=fatt,lotto=item["lotto"])
                #csssps=css
                #qc=ps/css
                #bl.append(item["lotto"])
            #else:                            
                #if(item["lotto"]!="" and sps==""):
                    #ltt=int(item["lotto"])
                #else:
                    #try:
                        #ltt=ltcod[0].id
                    #except:
                      ##  lsecc.clear()
                        #ecc={}
                        #ecc["num"]=item["css"]
                        #ecc["cod"]=item["cod"]
                        #lsecc.append(ecc)
                        #return lsecc
##                ltid=ltcod.get(id=ltt)
                #ltid=ltcod[0]
                #bl.append(ltt)
                #num=ltid.cassa-(int(item["css"])+ltid.cassaexit)
                #csssps=css
                #qc=ps/css
                #if(num>=0):
                    #ltid.cassaexit=css+ltid.cassaexit
                    #ltid.costo=ltid.costo+ps*prz
                    #ltid.save()
                #else:
                    #cst=ltid.costo+prz*qc*(num+css)
                    #ltid.costo=cst
                    #ltid.cassaexit=ltid.cassa
                    #ltid.save()
           ##         vv1=list(ltcod)
                    
                    #res=self.Rec(ltcod,num*(-1),0,ltt,bl,qc,prz)
                    #if(res!=0 and sps!=""):
                        #ecc={}
                        #ecc["num"]=res
                        #ecc["cod"]=item["cod"]
                        #csssps=css-res
                        #lsecc.append(ecc)
                #qsps=qc*csssps
                #rec1=Saldo.objects.get(idcod__cod=item["cod"])
                #rec1.q=rec1.q-csssps
                #rec1.save()
                #rec=trasporto(idcod=cod,cliente=c,prezzo=prz,q=qsps,cassa=csssps,
                            #ddt=fatt,lotto=ltt)
            #rec.save()
            #line[i]["lotto"]=bl.copy()
            #line[i]["css"]=csssps
            #line[i]["ps"]=qc*csssps
            #i=i+1
        #rg=list(line)
        #self.stampaFattura(fatt,c,rg)            
        #return lsecc    