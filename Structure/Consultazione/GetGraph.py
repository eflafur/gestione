from gestione.models import Produttore,Settore,Genere,Area,Sito,Specifica,IDcod
from django.db.models import Q


class Model:
  def __init__(self,genere):
    self.name=genere
    self.children=[]

class Design:
  def GetGraph(self):
    ls=[]
    gen=Genere.objects.all()
    sett=Settore.objects.all()
    res1=Specifica.objects.all()
    
    for item in gen:
      m=Model(item.nome)
      res=sett.filter(genere__nome=item.nome)
      for item1 in res:
        m1=Model(item1.articolo)
        res2=res1.filter(settore__articolo=item1.articolo)
        for item2 in res2:
          m2=Model(item2.nome)
          m1.children.append(m2)
        m.children.append(m1)
      ls.append(m)
    return ls
 
 
