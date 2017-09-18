from gestione.models import IDcod,Saldo
from django.db.models import Q


class Model:
  def __init__(self,el,dic):
    self.name=el
    self.id=dic
    self.children=[]

  
  

class Design:
  def GetRGraph(self,flag):
    i=1000
    ls=[]
    befsg=" "
    befsp=" "
    befss=" "
    befsc=" "
    cod=IDcod.objects.all()
    s=Saldo.objects.all()
    if(flag=='t'):
      sg=s.filter().values("q","idcod__cod","idcod","idcod__genere","idcod__genere__nome").order_by("idcod__genere__nome")
    else:
      sg=s.filter(q__gte=1).values("q","idcod__cod","idcod","idcod__genere","idcod__genere__nome").order_by("idcod__genere__nome")
  
    tree=Model("SALDO",900)
    for itemsg in sg:
      if(befsg==itemsg["idcod__genere__nome"]):
        continue
      i=i+1
      msg=Model(itemsg["idcod__genere__nome"],i)
      ss=sg.filter(idcod__genere__nome=itemsg["idcod__genere__nome"]).values("idcod__settore__articolo","idcod__settore").order_by("idcod__settore__articolo")
      befsg=itemsg["idcod__genere__nome"]
      befss=" "      
      for itemss in ss:
        if(befss==itemss["idcod__settore__articolo"]):
          continue
        i=i+1
        mss=Model(itemss["idcod__settore__articolo"],i)
        sp=ss.filter(idcod__settore__articolo=itemss["idcod__settore__articolo"]).values("idcod__produttore__azienda","idcod__produttore").order_by("idcod__produttore__azienda")        
        befss=itemss["idcod__settore__articolo"]      
        befsp=" "
      
        for itemp in sp:
          if(befsp==itemp["idcod__produttore__azienda"]):
            continue
          i=i+1
          msp=Model(itemp["idcod__produttore__azienda"],i)
          sc=sp.filter(idcod__produttore__azienda=itemp["idcod__produttore__azienda"]).values("q","idcod","idcod__cod","idcod__specifica__nome","idcod__specifica").order_by("idcod__specifica__nome")
          befsp=itemp["idcod__produttore__azienda"]
          befsc=" "
          
          for itemsc in sc:
            if(befsc==itemsc["idcod__specifica__nome"]):
              continue
            i=i+1
            msid=Model(itemsc["idcod__cod"]+" : "+ str(itemsc["q"]),str(itemsc["idcod"]))
            if(itemsc["idcod__specifica"]!=None):
              i=i+1
              msc=Model(itemsc["idcod__specifica__nome"],i)
              msc.children.append(msid)
              msp.children.append(msc)               
            else:
              msp.children.append(msid)               
          mss.children.append(msp)
        msg.children.append(mss)
        tree.children.append(msg)
      ls.append(tree)
    return ls  
    
                