import django
django.setup()
from gestione.models import Cliente,Scarico,IDcod,Sospese
from django.db.models import Q

class Produt:
    def put(self,line):
        self.row=line
        p=Cliente.objects.filter(Q(azienda=self.row["a1"])) 
        if (p):
            return (2)
        p=Cliente.objects.create(
            azienda=self.row["a1"],
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
    
    def ScriviFattura(self,line):
        s=Scarico.objects.latest("id")
        f=(s.fattura).split("-")
        r=int(f[1])+1
        fatt=f[0]+"-"+str(r)
        for item in line:
            c=Cliente.objects.get(azienda=item["cln"])
            cod=IDcod.objects.get(cod=item["cod"])
            rec=Scarico(idcod=cod,cliente=c,prezzo=item["prz"],q=item["ps"],fattura=fatt)
            rec.save()
        return

    def ScriviSospesa(self,line):
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
    def GetSospesa(self,message):
        recls=Sospese.objects.filter(Q(data__gte=message["data"])).values("idcod__cod","q","fatturas","data","prezzo","cliente")
        data=list(recls)
        return data
