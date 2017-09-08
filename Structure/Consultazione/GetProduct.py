import django
django.setup()
from gestione.models import Produttore,Settore,Genere,Area,Sito,Specifica,IDcod,Prodotto,Pagamento
from django.db.models import Q

class LKPData:
    def getbyCompany(self,line):
        self.row=line
        p=IDcod.objects.filter(Q(produttore__azienda=line)).values("settore__articolo","genere__nome","produttore__margine").order_by("genere__nome","settore__articolo")
        if (p==""):
            return (2)
        data=list(p)
        return data
    def getbyArticolo(self,line):
        self.row=line
        p=IDcod.objects.filter(Q(genere__nome=line)).values("genere__nome","settore__articolo",
                                            "produttore__azienda","produttore__margine").order_by("-produttore__margine","produttore__azienda","settore__articolo")
        if (p==""):
            return (2)
        data=list(p)
        return data    
    def getbyMargin(self,line):
        self.row=line
        p=Produttore.objects.filter(Q(margine__gte=line)).order_by("-margine").values("azienda","margine","regione","citta","tel")
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
    
    def GetGenere(self):
        res=Genere.objects.all().values("nome")
        data=list(res)
        return data
    
    def GetByGenere(self,art):
        res=Settore.objects.filter(Q(genere__nome=art)).values("genere__nome","articolo")
        data=list(res)
        return data
    
    def GetSpec(self,art):
        s=Specifica.objects.filter(settore__articolo=art).values("nome")
        data=list(s)
        return data
    def GetIDcod(self):
        s=IDcod.objects.all().values("id","cod","genere__iva").order_by("produttore__azienda")
        data=list(s)
        return data
    def GetIDcodbyProvider(self,message):
        s=IDcod.objects.filter(produttore__azienda=message["cliente"]).values("id","cod","genere__iva").order_by("produttore__azienda")
        data=list(s)
        return data    
    def GetTerminiPag(self):
        s=Pagamento.objects.filter().values("tipo")
        data=list(s)
        return data
    def GetProdotto(self):
        s=Prodotto.objects.filter().values("tipo")
        data=list(s)
        return data
    