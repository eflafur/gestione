#import django
#django.setup()
from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo,Carico,trasporto,ivacliente
from decimal import Decimal
from django.db.models import Q,F
import time,os,subprocess,datetime
import Registra,Pdf,math,io,sys
from datetime import datetime,timedelta,date

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
#            indirizzo=self.row["a7"],
            acquisizione=self.row["a5"],
            email=self.row["a6"],
            trpag=self.row["a9"],
            tel=self.row["a8"],
        )
        return (1)
    
    def ScriviFattura(self,line,sps,pgm,tot,conto):
        ltstr=""
        i=0
        bl=[]
        bls=[]
        lsdc=[]
        imp=0
        erario=0
        pg=0
        c=""
        ltt1=0
        if (int(pgm)!=0):
            pg=1
        gg=date.today()+timedelta(int(pgm))
        lotto=Carico.objects.filter(cassa__gt=F("cassaexit")).order_by("id")
        fatt=""
        if(sps[:2]=="sc"):
            rec=Sospese.objects.filter(fatturas=sps)
            rec.delete()
        s=Scarico.objects.latest("id")
        f=(s.fattura).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        c=Cliente.objects.get(azienda=line[0]["cln"])
        for item in line:
            bls.clear()
            bl.clear()
            iva=Decimal(item["iva"])+1
            prz=Decimal(item["prz"])
            tara=Decimal(item["tara"])
            ps=Decimal(item["ps"])
            css=int(item["css"])
            qcss=ps/css-tara
            cod=IDcod.objects.get(id=item["id"])
            ltcod=lotto.filter(idcod__id=item["id"])
            
            if(item["lotto"]!=""):
                ltt=item["lotto"]
            else:
                try:
                    ltt=ltcod[0].id
                except:
                    f=open("/home/djangolog","w")
                    f.write("errore su assegnazione Lotto :+"+item + datetime.now())
                    f.close()
                    return 1
            ltt1=ltcod.get(id=ltt)
            bl.append(ltt)
            rim=ltt1.cassa-(ltt1.cassaexit+css)
            if(rim>=0):
                bls.append(str(ltt)+"-"+str(css))
                ltt1.cassaexit+=css
                ltt1.costo+=qcss*css*prz
                ltt1.q+=qcss*css
                ltt1.save()
                rim=0
            else:
                bls.append(str(ltt)+"-"+str(css+rim))
                ltt1.cassaexit=ltt1.cassa
                ltt1.costo+=prz*(css+rim)*qcss
                ltt1.q+=(css+rim)*qcss
                ltt1.save()
                ltt2=ltcod.exclude(id=ltt).order_by("id")
                data=list(ltt2)
                rim=self.DelLotto(ltt2,-rim,prz,qcss,0,bl,bls)
            rec1=Saldo.objects.get(idcod__id=item["id"])
            rec1.q=rec1.q-css+rim
            rec1.save()
            imp+=round(prz*qcss*(css-rim),2)
            erario+=round(Decimal(item["iva"])*prz*qcss*(css+rim),2)
            ltstr=' '.join(str(x) for x in bls)
            rec=Scarico(idcod=cod,cliente=c,prezzo=prz,q=ps,cassa=css-rim,fattura=fatt,lotto=ltstr,scadenza=gg,pagato=pg,tara=tara,iva=iva-1)
            rec.save()
            ls={}
            ls["cod"]=cod.cod
            ls["imp"]=round(prz*qcss*(css-rim),2)
            ls["iva"]=iva-1
            ls["tara"]=tara*css
            ls["lotto"]=bl.copy()    
            ls["prz"]=prz
            ls["css"]=css
            ls["ps"]=ps
            lsdc.append(ls)
    
#registrazione contabile
        res=Registra.ComVen(conto,tot,imp,erario,"3.1",pg,line[0]["cln"],fatt)
        res.SetErarioCliente()
        res.Vendita()
#registrazione contabile
        obj=Pdf.PrintTable("FATTURA",lsdc,imp+erario-Decimal(tot))
        obj.PrintArt()
        obj.PrintAna(fatt,c)
        return 0
    
    def ScriviDDT(self,line,sps):
        ltstr=""
        i=0
        bl=[]
        bls=[]
        lsdc=[]
        c=""
        ltt1=0
        lotto=Carico.objects.filter(cassa__gt=F("cassaexit")).order_by("id")
        fatt=""
        if(sps[:2]=="sc"):
            rec=Sospese.objects.filter(fatturas=sps)
            rec.delete()
        elif(sps[:2]=="dd"):    
            rec=trasporto.objects.filter(ddt=sps)
            rec.delete()
        s=trasporto.objects.latest("id")
        f=(s.ddt).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        c=Cliente.objects.get(azienda=line[0]["cln"])
        for item in line:
            bl.clear()
            bls.clear()
            iva=Decimal(item["iva"])+1
            prz=Decimal(item["prz"])
            tara=Decimal(item["tara"])
            ps=Decimal(item["ps"])
            css=int(item["css"])
            qcss=ps/css-tara
            cod=IDcod.objects.get(cod=item["id"])
            ltcod=lotto.filter(idcod__cod=item["id"])
            if(sps[:2]=="dd"):    
                fatt=sps                
                rec=trasporto(idcod=cod,cliente=c,prezzo=prz,q=ps,cassa=css,ddt=fatt,lotto=item["lotto"],tara=tara)
                bl.append(item["lotto"])
            if(item["lotto"]!=""):
                ltt=item["lotto"]
            else:
                try:
                    ltt=ltcod[0].id
                except:
                    f=open("/home/jafu/djangolog","w")
                    f.write("errore su assegnazione Lotto :+"+item["lotto"] + datetime.now())
                    f.close()
                    return 1
            bl.append(ltt)
            ltt1=ltcod.get(id=ltt)
            rim=ltt1.cassa-(ltt1.cassaexit+css)
            if(rim>=0):
                bls.append(str(ltt)+"-"+str(css))
                ltt1.cassaexit+=css
                ltt1.costo+=qcss*css*prz
                ltt1.q+=qcss*css
                ltt1.save()
                rim=0
            else:
                bls.append(str(ltt)+"-"+str(css+rim))
                ltt1.cassaexit=ltt1.cassa
                ltt1.costo+=prz*(css+rim)*qcss
                ltt1.q+=(css+rim)*qcss
                ltt1.save()
                ltt2=ltcod.exclude(id=ltt)
                data=list(ltt2)
                rim=self.DelLotto(ltt2,-rim,prz,qcss,0,bl,bls)
            rec1=Saldo.objects.get(idcod__cod=item["id"])
            rec1.q=rec1.q-css+rim
            rec1.save()
            ltstr=' '.join(str(x) for x in bls)
            rec=trasporto(idcod=cod,cliente=c,prezzo=prz,q=ps,cassa=css-rim,ddt=fatt,lotto=ltstr,tara=tara)
            rec.save()
            ls={}
            ls["cod"]=item["cod"]
            ls["imp"]=round(prz*qcss*(css-rim),2)
            ls["iva"]=iva-1
            ls["tara"]=tara*css
            ls["lotto"]=bl.copy()    
            ls["prz"]=prz
            ls["css"]=css
            ls["ps"]=ps
            lsdc.append(ls)
        obj=Pdf.PrintTable("DDT",lsdc,0)
        obj.PrintArt()
        obj.PrintAna(fatt,c)
        return 0
    
    def DelLotto(self,lotti,num,prz,qcss,i,lt,bls):
        try:
            cod=lotti[i].id
            rim=lotti[i].cassa-(lotti[i].cassaexit+num)
        except:
            return num
        if(rim<0):
            ltt=lotti.get(id=cod)
            ltt.cassaexit=ltt.cassa
            ltt.costo+=prz*(num+rim)*qcss
            ltt.q=(num+rim)*qcss
            bls.append(str(cod)+"-"+str(num+rim))
            ltt.save()
            lt.append(cod)
            return self.DelLotto(lotti,-rim,prz,qcss,i+1,lt,bls)
        else:
            ltt=lotti.get(id=cod)
            bls.append(str(cod)+"-"+str(num))
            ltt.cassaexit+=num
            ltt.costo+=prz*num*qcss
            ltt.q=num*qcss
            ltt.save()
            lt.append(cod)
            rim=0
        return rim          
    

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
        for item in line:
            c=Cliente.objects.get(azienda=item["cln"])
            cod=IDcod.objects.get(cod=item["cod"])
            rec=Sospese(idcod=cod,cliente=c,prezzo=item["prz"],q=item["ps"],cassa=item["css"],
                        fatturas=fatt,tara=Decimal(item["tara"]))
            rec.save()
        return
    
    def RecFatt(self,message):
        somma=0
        before=" "
        i=0
        ll=[]
        ss=[]
        if(message["cl"]!=" "):
            recls=Scarico.objects.filter(Q(cliente__azienda=message["cl"]),Q(rscassa__gte=0),Q(cassa__gt=F("rscassa"))).exclude(id=0).values("rscassa",
                                                    "tara","idcod__cod","idcod__genere__iva","q","cassa","fattura","data","prezzo","cliente__azienda")
        else:
            recls=Scarico.objects.filter(Q(rscassa__gte=0)).values("idcod__cod","idcod__genere__iva","q","cassa","fattura","data","prezzo","cliente__azienda","tara")
        
        for el in recls:
            iva=el["idcod__genere__iva"]+1
            if(el["fattura"]!=before):
                if(before!=" "):
                    ll.append(somma)
                somma=0
                somma=somma+el["prezzo"]*(el["q"]-el["cassa"]*el["tara"])*iva
            else:
                somma=somma+el["prezzo"]*(el["q"]-el["cassa"]*el["tara"])*iva
            before=el["fattura"]
        
        ll.append(somma)
        before=" "
        i=0
        
        for item in recls:
            if (item["fattura"]!=before):
                item["valore"]=round(ll[i],2)
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
            recls=trasporto.objects.filter(Q(data__gte=message["data"]),Q(cliente__azienda=message["cliente"]),Q(status=0)).exclude(id=1).values("tara","idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
        else:
            recls=trasporto.objects.filter(Q(data__gte=message["data"]),Q(status=0)).exclude(id=1).values("tara","idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
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
            recls=Sospese.objects.filter(Q(data__gte=message["data"]),Q(cliente__azienda=message["cliente"])).exclude(id=199).values("tara","idcod__cod","idcod__genere__iva","q","cassa","fatturas","data","prezzo","cliente__azienda").order_by("fatturas")
        else:
            recls=Sospese.objects.filter(Q(data__gte=message["data"])).exclude(id=1).values("tara","idcod__cod","idcod__genere__iva","q","cassa","fatturas","data","prezzo","cliente__azienda").order_by("fatturas")
        
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
        i=0
        somma=0
        before=" "
        i=0
        ll=[]
        rim=[]
        ss=[]
        if(message["cliente"]!= ""):
            recls=Scarico.objects.filter(Q(data__gte=message["data"]),Q(rscassa__gte=0),
            Q(cliente__azienda=message["cliente"]),Q(pagato=1)).values("tara","scadenza","pagato",
            "idcod__cod","idcod__genere__iva","q","cassa","fattura","data","prezzo","cliente__azienda","note")
        else:
            rec=Scarico.objects.filter(Q(data__gte=message["data"]),
            Q(rscassa__gte=0),Q(pagato=1)).exclude(id=1).values("tara","scadenza","pagato",
            "idcod__cod","idcod__genere__iva","q","cassa","fattura","data","prezzo","cliente__azienda","note")

        for item in rec:
            if(item["fattura"]==before):
                    continue
            res=ivacliente.objects.get(fatt=item["fattura"])
            item["valore"]=res.tot
            item["rim"]=res.saldo
            ss.append(item)
            before=item["fattura"]
        return ss
    
    def Pagato(self,line):
        imp=0
        erario=0
        cl=ivacliente.objects.get(fatt=line["pg"])
        cl.saldo-=Decimal(line["part"])
        cl.save()
        s=Scarico.objects.filter(fattura=line["pg"])
        s.update(pagato=line["ppg"],note=line["nt"])
        s1=s.values("q","prezzo","cassa","idcod__genere__iva","tara","data","cliente__azienda")
        for item in s1:
            imp+=(item["q"]-(item["cassa"]*item["tara"]))*item["prezzo"]
            erario+=(item["q"]-(item["cassa"]*item["tara"]))*item["prezzo"]*(item["idcod__genere__iva"])
        res=Registra.ComVen(line["chc"],line["part"],imp,erario,"3.1",0,s1[0]["cliente__azienda"],line["pg"])
        #res.put() 
        res.Vendita(1)
        
    def GetFatturabyNum(self,num):
        recls=Scarico.objects.filter(fattura=num).values("id","idcod__cod","idcod__genere__iva","q","cassa","fattura",
                                                    "data","prezzo","cliente__azienda","lotto","tara","rs","rscassa")
        data=list(recls)
        return data          
    
    def GetDdt(self,message):
        somma=0
        before=" "
        i=0
        ll=[]
        ss=[]
        if(message["cliente"]!=""):
            recls=trasporto.objects.filter(Q(cliente__azienda=message["cliente"]),Q(status=0)).exclude(id=1).values("tara","idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
        else:
            recls=trasporto.objects.filter(Q(status=0)).exclude(id=1).values("tara","idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
        
        for el in recls:
            iva=el["idcod__genere__iva"]+1
            if(el["ddt"]!=before):
                if(before!=" "):
                    ll.append(somma)
                somma=0
                somma=somma+el["prezzo"]*(el["q"]-el["cassa"]*el["tara"])*iva
            else:
                somma=somma+el["prezzo"]*(el["q"]-el["cassa"]*el["tara"])*iva
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

    def GetDdtbyNum(self,num):
        recls=trasporto.objects.filter(ddt=num).values("idcod__cod","idcod__genere__iva","q","cassa","ddt","data","prezzo","cliente__azienda")
        data=list(recls)
        return data          
    
    
    def DdtEmit(self,ls,cln,pgm,tot,conto):
        ddtls=[]
        ls1=[]
        lsddt=""
        trs=trasporto.objects.filter(status=0).values("tara","ddt","q","prezzo","data","lotto","cassa",
                                "idcod__cod","cliente__azienda","idcod__genere__iva","status","cliente__azienda")
        trstrs=trs.annotate(cod=F("idcod__cod"),ps=F("q"),css=F("cassa"),prz=F("prezzo"),iva=F("idcod__genere__iva")).values("cod",
                                   "q","css","prz","iva","data","lotto","ddt","cliente__azienda","tara")
        for item in ls:
            t=trstrs.filter(ddt=item).values()
            data=list(t)
            t.update(status=1)
            for el in data:
                ddtls.append(el)
        lsddt=" ".join(ls)
        self.Ddt2Fatt(ddtls,cln,pgm,lsddt,tot,conto)
        return ddtls
        
    def Ddt2Fatt(self,line,cliente,pgm,lsddt,tot,conto):
        erario=0
        imp=0
        pg=0
        ls=[]
        lsdc=[]
        s=Scarico.objects.latest("id")
        f=(s.fattura).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        cln=Cliente.objects.get(azienda=cliente)
        if (int(pgm)!=0):
            pg=1
        gg=datetime.now()+timedelta(int(pgm))
        for item in line:
            row=Decimal(item["prz"])*(Decimal(item["q"])-(int(item["cassa"])*Decimal(item["tara"])))
            cod=IDcod.objects.get(cod=item["cod"])
            rec=Scarico(idcod=cod,cliente=cln,prezzo=item["prz"],q=item["q"],cassa=item["css"],
                                    fattura=fatt,lotto=item["lotto"],iva=item["iva"],pagato=pg,scadenza=gg,tara=item["tara"])
            rec.save()
            cln=Cliente.objects.get(azienda=cliente)
            imp+=row
            erario+=Decimal(item["iva"])*row
            ls={}
            ls["cod"]=item["cod"]
            ls["imp"]=round(row,2)
            ls["iva"]=Decimal(item["iva"])
            ls["tara"]=item["tara"]
            ls["lotto"]=item["lotto"] #bl.copy()    
            ls["prz"]=item["prz"]
            ls["css"]=item["cassa"]
            ls["ps"]=item["q"]
            lsdc.append(ls)
        res=Registra.ComVen(conto,tot,imp,erario,"3.1",pg,cliente,fatt)
        res.Vendita()
        res.SetErarioCliente()
   
        obj=Pdf.PrintTable("FATTURA",lsdc,imp+erario-Decimal(tot))
        obj.PrintArt()
        obj.PrintAna(fatt,cln,lsddt)       
        return ls        
    
    def ScriviNotaC(self,line,fatt,cln,conto,tot=0):
        lslotti=[]
        lsdc=[]
        bl=[]
        imp=0
        erario=0
        nodi=Scarico.objects.filter(fattura=fatt)
        crc=Carico.objects.filter(pagato=0)
        s=Scarico.objects.latest("id")
        f=(s.fattura).split("-")
        r=int(f[1])+1
        prg=f[0]+"-"+str(r)
        c=Cliente.objects.get(azienda=cln)

        for item in line:
            d=0
            ar=[]
            bl.clear()
            nodo=nodi.get(id=item["id"])
            psrs=Decimal(item["rs"])
            css=int(item["rscss"])
            pscss=psrs/css-nodo.tara
            rec=Scarico(idcod=nodo.idcod,cliente=nodo.cliente,prezzo=-nodo.prezzo,
                        q=psrs,cassa=css,fattura=prg,lotto=nodo.lotto,tara=nodo.tara,iva=nodo.iva,note=fatt,rscassa=-1)
            rec.save()
            rec1=Saldo.objects.get(idcod__id=nodo.idcod_id)
            rec1.q+=css
            rec1.save()
            lslotti=(nodo.lotto).split(" ")
            rscss=nodo.rscassa
            for i in lslotti:
                ar=i.split("-")
                try:
                    lt=crc.get(id=ar[0])
                except:
                    continue
                bl.append(ar[0])
                d=int(ar[1])-rscss
                if(css<=d):
                    lt.costo-=nodo.prezzo*css*pscss
                    lt.cassaexit-=css
                    lt.q-=css*pscss
                    lt.save()
                    break
                elif(css>d & d>0):
                    lt.costo-=nodo.prezzo*d*pscss
                    lt.cassaexit-=d
                    lt.q-=d*pscss
                    lt.save()
                    rscss=0
                    css-=d
                else:
                    rscss=-d
                    continue
            css=int(item["rscss"])
            impfatt=nodo.prezzo*pscss*css
            imp+=nodo.prezzo*pscss*css
            erario+=nodo.iva*nodo.prezzo*(css)*pscss
            nodo.rs+=psrs
            nodo.rscassa+=css
            nodo.save()
            ls={}
            ls["cod"]=item["cod"]
            ls["imp"]=round(-impfatt,2)
            ls["iva"]=nodo.iva
            ls["tara"]=nodo.tara
            ls["lotto"]=bl.copy() 
            ls["prz"]=-nodo.prezzo
            ls["css"]=int(css)
            ls["ps"]=psrs
            lsdc.append(ls)
#registrazione contabile
        #if(int(tot)==-1):
            #tot=-imp-erario
        res=Registra.ComVen(conto,-imp-erario,-imp,-erario,"3.1",0,cln,prg)
        res.SetErarioCliente(1)
        res.Vendita()
#registrazione contabile  
#        self.stampaFattura(fatt,c,rg)
        obj=Pdf.PrintTable("Nota di Credito",lsdc,0)
        obj.PrintArt()
        obj.PrintAna(prg,c,fatt)       
        

        return 0        
    
  