import django
django.setup()
from gestione.models import Cliente,Scarico,IDcod,Sospese,Saldo
from decimal import Decimal
from django.db.models import Q

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
        if(sps!=" "):
            rec=Sospese.objects.filter(fatturas=sps)
            rec.delete()
        s=Scarico.objects.latest("id")
        f=(s.fattura).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        for item in line:
            c=Cliente.objects.get(azienda=item["cln"])
            cod=IDcod.objects.get(cod=item["cod"])
            rec=Scarico(idcod=cod,cliente=c,prezzo=item["prz"],q=item["ps"],fattura=fatt)
            rec.save()
            rec1=Saldo.objects.get(idcod__cod=item["cod"])
            rec1.q=rec1.q-(Decimal(item["ps"]))
            if(rec1.q<0):
                ls.append(item["cod"])
            rec1.save()              
        return ls

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
            rec=Sospese(idcod=cod,cliente=c,prezzo=item["prz"],q=item["ps"],fatturas=fatt)
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
            recls=Sospese.objects.filter(Q(data__gte=message["data"]) , Q(cliente__azienda=message["cliente"])).values("idcod__cod","idcod__genere__iva","q","fatturas","data","prezzo","cliente__azienda")
        else:
            recls=Sospese.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","idcod__genere__iva","q","fatturas","data","prezzo","cliente__azienda")
        
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
            recls=Scarico.objects.filter(Q(data__gte=message["data"]) , Q(cliente__azienda=message["cliente"])).values("idcod__cod","idcod__genere__iva","q","fattura","data","prezzo","cliente__azienda")
        else:
            recls=Scarico.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","idcod__genere__iva","q","fattura","data","prezzo","cliente__azienda")
        data=list(recls)
        
        for el in data:
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
            if (item["fattura"]!=before):
                item["valore"]=ll[i]
                ss.append(item)
                i=i+1
            before=item["fattura"]
        return ss        
    
    def GetFatturabyNum(self,num):
        recls=Scarico.objects.filter(fattura=num).values("idcod__cod","idcod__genere__iva","q","fattura","data","prezzo","cliente__azienda")
        data=list(recls)
        return data          