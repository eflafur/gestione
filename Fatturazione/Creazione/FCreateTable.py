import django
django.setup()
from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo,Carico,trasporto
from decimal import Decimal
from django.db.models import Q,F

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
            if("lotto" in item):
                ltt=int(item["lotto"])
            else:
                ltt=ltcod[0].id
            ltid=ltcod.get(id=ltt)
            num=ltid.cassa-(int(item["css"])+ltid.cassaexit)
            if(num>=0):
                ltid.cassaexit=int(item["css"])+ltid.cassaexit
                ltid.save()
            else:
                ltid.cassaexit=ltid.cassa
                ltid.save()
                self.Rec(ltcod,num*(-1),0,ltt)
            rec=Scarico(idcod=cod,cliente=c,prezzo=item["prz"],q=item["ps"],cassa=item["css"],
                                    fattura=fatt,lotto=ltt,iva=iva1)
            rec.save()
        return ls
    
    def ScriviDDT(self,line,sps):
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
            num=ltid.cassa-(int(item["css"])+ltid.cassaexit)
            if(num>=0):
                ltid.cassaexit=int(item["css"])+ltid.cassaexit
                ltid.save()
            else:
                ltid.cassaexit=ltid.cassa
                ltid.save()
                self.Rec(ltcod,num*(-1),0,ltt)
            rec=trasporto(idcod=cod,cliente=c,prezzo=item["prz"],q=item["ps"],cassa=item["css"],
                        ddt=fatt,lotto=ltt)
            rec.save()
        return ls    
    
    
    
    def Rec(self,lotti,casse,i,lotto):
        if(i<lotti.count()):
            data=list(lotti)
            a=lotti[i].id
            num=lotti[i].cassa-(lotti[i].cassaexit+casse)
            if(num>=0 and lotti[i].id!=lotto):
#                lt1=lotti.get(id=lotti[i].id)
                lotti[i].cassaexit=lotti[i].cassaexit+casse
                lotti[i].save()
                #lt1.cassaexit=lotti[i].cassaexit+casse    
                #lt1.save()
                return 
            else:
                if(lotti[i].id!=lotto):
                    #lt1=lotti.get(id=lotti[i].id)
                    #lt1.cassaexit=lotti[i].cassa
                    #lt1.save()
                    lotti[i].cassaexit=lotti[i].cassa
                    lotti[i].save()
                else:
                    num=casse*(-1)
                i=i+1
                self.Rec(lotti,num*(-1),i,lotto)
                return
            return 
            

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
        if(message["cliente"]!=" "):
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
    
    def DdtEmit(self,ls):
        ddtls=[]
        ls1=[]
        for item in ls:
            i=0
            t=trasporto.objects.filter(ddt=item).values("ddt","q","prezzo","data","lotto","cassa",
                                             "idcod__cod","cliente__azienda","idcod__genere__iva","status")
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