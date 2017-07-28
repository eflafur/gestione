import django
django.setup()
from gestione.models import Produttore,Settore,Genere,Area,Sito
from django.db.models import Q

class LKPData:
    def getbyCompany(self,line):
        self.row=line
        p=Produttore.objects.filter(Q(azienda=line)).values("settore__articolo","tel")
        if (p==""):
            return (2)
        data=list(p)
        return data
    def getbyArticolo(self,line):
        self.row=line
        p=Settore.objects.filter(Q(articolo=line)).values("articolo","produttore__azienda")
        if (p==""):
            return (2)
        data=list(p)
        return data    
    def getbyMargin(self,line):
        self.row=line
        p=Produttore.objects.filter(Q(margine__gte=line)).order_by("margine").values("azienda","margine","regione","citta","tel")
        if (p==""):
            return (2)
        data=list(p)
        return data
    def ListAddArt(self,line,par):
        dd=[]
        vv=[]
        self.row=line
        allart=Settore.objects.all().values("articolo")
        prd=Produttore.objects.filter(Q(azienda=line)).values("settore__articolo")
        for item in allart:
            h=0
            for item1 in prd:
                if(item["articolo"]==item1["settore__articolo"]):
                    h=1
                    break
                else:
                    c="ciccio"
            if(h==0):
                dd.append(item["articolo"])
        if(par==1):
            return dd
            
        res=self.ListDelArt(line,0)
        t=dd,res
        return t
    
    def ListDelArt(self,line,par):
        cc=[]
        prd=Produttore.objects.filter(Q(azienda=line)).values("settore__articolo")
        for item in prd:
            cc.append(item["settore__articolo"])
        if (par==1):
            res=self.ListAddArt(line,par)
            t=cc,res            
            return t
        return cc

    def GetArticoloMargine(self,line):
        dd=[]
        prd=Produttore.objects.filter(Q(settore__articolo=line['a2']), Q(margine__gte=line['a3'])).values("azienda","settore__articolo")
        data=list(prd)
        return data
