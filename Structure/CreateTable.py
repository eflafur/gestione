import django
django.setup()
from gestione.models import Produttore,Settore,Genere,Area,Sito
from django.db.models import Q

#nuova release salvata

class Produt:
    def put(self,line):
        self.row=line
        p=Produttore.objects.filter(Q(azienda=self.row["a2"])) 
        contatto1=self.row["a3"]
        if (self.row["a3"]==""):
            contatto1=self.row["a2"]
        if (p):
            return (2)
        item=Settore.objects.get(articolo=self.row["a1"])
        p=Produttore.objects.create(
            azienda=self.row["a2"],
            contatto=contatto1,
            citta=self.row["a4"],
            regione=self.row["a5"],
            acquisizione=self.row["a6"],
            capacita=self.row["a7"],
            email=self.row["a8"],
            trpag=self.row["a10"],
            margine=self.row["a11"],
            fatturato=self.row["a12"],
        )
        p.settore.add(item)
        return (1)


class Siti:
    def put(self,line):
        self.row=line
        p=Area.objects.get(regione=self.row[0])
        if (p==""):
            return 
        s=Sito.objects.create(
            area=p,
            citta=self.row[1],
            sigla=self.row[2],
        )
        return   
    
class GetProd:
    def GetArticolo(self):
        res=Settore.objects.all()
        return res
    def GetArea(self):
        res=Area.objects.all()
        return res
    def GetCitta(self,var):
        res=Sito.objects.filter(Q(area__regione=var)).values("citta")
        data=list(res)
        return data
    def GetProduttori(self):
        res=Produttore.objects.all()
        data=list(res)
        return data
    def GetCapacita(self):
        res=Produttore.objects.all()
        data=list(res)
        return data    
    def DelProduttori(self,var):
        p=Produttore.objects.filter(Q(azienda=var))
        p.delete()
        return 1


class GetSett:
    def GetGenere(self):
        res=Genere.objects.all()
        return res        
    def GetSettore(self,var):
        res=Settore.objects.filter(Q(genere__nome=var)).values("articolo")
        data=list(res)
        return data
    
class Sett:
    def put(self,line):
        self.row=line
        s=Settore.objects.filter(Q(articolo=self.row["s2"]))
        if (s):
            return (2)
        item=Genere.objects.get(nome=self.row["s1"])        
        Settore.objects.create(
            articolo=self.row["s2"],
            genere=item,
        )
        return 
    def Delete(self,line):
        self.row=line
        s=Settore.objects.filter(Q(articolo=self.row["s2"]))
        if (s==""):
            return (2)
        s.delete()
        return 
    