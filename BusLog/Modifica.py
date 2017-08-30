import django
django.setup()
from gestione.models import Produttore,Settore,Genere,Area,Sito,Preferenza,Specifica,IDcod,Saldo
from django.db.models import Q

class Produt:
    def put(self,line):
        self.row=line
        p=Produttore.objects.filter(Q(azienda=self.row["a2"]) & Q(settore__articolo=self.row["a1"]))
        if (p):
            return (2)
        item=Settore.objects.get(articolo=self.row["a1"])
        p=Produttore.objects.create(
            azienda=self.row["a2"],
            contatto=self.row["a3"],
            citta=self.row["a4"],
            regione=self.row["a5"],
            acquisizione=self.row["a6"],
            capacita=int(self.row["a7"]),
            email=self.row["a8"],
            tel=self.row["a9"],
        )
        p.settore.add(item)
        return (1)

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
    
class ModProd:
    def GetProduttori(self):
        res=Produttore.objects.all()
        data=list(res)
        return data
    def GetAll(self,line):
        self.row=line
        res=Produttore.objects.filter(Q(azienda=line)).values("azienda","settore__articolo",
            "contatto","regione","citta","acquisizione","capacita","email","tel","trpag","margine","fatturato","pi")
        ret=list(res)    
        return ret
    def GetRegione(self):
        res=Area.objects.all().values("regione")
        ret=list(res)
        return ret     
    def GetArticolo(self):
        res=Settore.objects.all().values("articolo")
        ret=list(res)
        return ret     
    def GetCitta(self,var):
        res=Area.objects.filter(Q(regione=var)).values("sito__citta")
        ret=list(res)
        return ret         
    def Change(self,line):
        self.row=line
        val=0
        val1=0
        p=Produttore.objects.get(azienda=self.row["a2"])
        pt=Produttore.objects.filter(Q(azienda=self.row["a2"])).values("settore__articolo","contatto","regione",
                                    "citta","acquisizione","capacita","email","tel","trpag","margine","fatturato","pi")
        if(pt[0]["contatto"]!=self.row["a3"]):
            val=1
        elif(pt[0]["regione"]!=self.row["a4"]):
            val=1            
        elif(pt[0]["citta"]!=self.row["a5"]):
            val=1
        elif(pt[0]["capacita"]!=self.row["a7"]):
            val=1            
        elif(pt[0]["tel"]!=self.row["a9"]):
            val=1
        elif(pt[0]["email"]!=self.row["a8"]):
            val=1
        elif(pt[0]["trpag"]!=int(self.row["a10"])):
            val=1
        elif(pt[0]["margine"]!=int(self.row["a11"])):
            val=1
        elif(pt[0]["fatturato"]!=int(self.row["a12"])):
            val=1            
        elif(pt[0]["pi"]!=self.row["a13"]):
            val=1
        if (val==0):
            return 2
        if (val==1):
            p.contatto=self.row["a3"]
            p.regione=self.row["a4"]
            p.citta=self.row["a5"]
            p.capacita=self.row["a7"]
            p.acquisizione=self.row["a6"]
            p.tel=self.row["a9"]
            p.email=self.row["a8"]
            p.trpag=self.row["a10"]
            p.margine=self.row["a11"]
            p.fatturato=self.row["a12"]
            p.pi=self.row["a13"]
            p.save()
        return "okey"
    def AddArticolo(self,azd,art):
        p=Produttore.objects.get(azienda=azd)
        s=Settore.objects.get(articolo=art)
        p.settore.add(s)
        return
    def DelArticolo(self,azd,art):
        p=Produttore.objects.get(azienda=azd)
        s=Settore.objects.get(articolo=art)
        p.settore.remove(s)
        return
    
    def ChangeSpec(self,message,cat):
        sp=Specifica.objects.filter(nome=cat)
        st=Settore.objects.filter(Q(articolo=message["a3"]),  Q(specifica__nome=message["a4"]))
        if((not sp) & (cat!="")):
            sp=Specifica(nome=cat)
            sp.save()
            st=Settore.objects.get(articolo=message["a3"])
            sp.settore.add(st)
        elif ((sp is not None) & (cat!="") & (not st)):
                st=Settore.objects.get(articolo=message["a3"])
                sp=Specifica.objects.get(nome=cat)
                sp.settore.add(st)
        codifica=message["a1"] + "-" + message["a2"] + "-"  + message["a3"] + "-"  + cat 
        c=IDcod.objects.filter(Q(cod=codifica))
        if (c):
            return 2
        p=Produttore.objects.get(azienda=message["a1"])
        g=Genere.objects.get(nome=message["a2"])
        st=Settore.objects.get(articolo=message["a3"])
        if(cat==""):
            c=IDcod(cod=codifica,genere=g,settore=st,produttore=p)
        else:
            sp=Specifica.objects.get(nome=cat)
            c=IDcod(cod=codifica,genere=g,settore=st,specifica=sp,produttore=p)
        c.save()
        c=IDcod.objects.get(cod=codifica)
        s=Saldo(idcod=c)
        s.save()
        return 1

        
    
        