from gestione.models import IDcod,Saldo
from django.db.models import Q


class Model:
  def __init__(self,el,dic):
    self.name=el
    self.id=dic
    self.children=[]

  
  

class Design:
  def GetRGraph(self):
    i=0
    ls=[]
    befsg=" "
    befsp=" "
    befss=" "
    befsc=" "
    cod=IDcod.objects.all()
    s=Saldo.objects.all()
    sg=s.filter(q__gte=1).values("q","idcod__cod","idcod","idcod__genere","idcod__genere__nome").order_by("idcod__genere__nome")

    for itemsg in sg:
      if(befsg==itemsg["idcod__genere__nome"]):
        continue
      i=i+1
      msg=Model(itemsg["idcod__genere__nome"],i)
      ss=sg.filter(idcod__genere__nome=itemsg["idcod__genere__nome"]).values("idcod__settore__articolo","idcod__settore").order_by("idcod__settore__articolo")
      befsg=itemsg["idcod__genere__nome"]
      
      for itemss in ss:
        if(befss==itemss["idcod__settore__articolo"]):
          continue
        i=i+1
        mss=Model(itemss["idcod__settore__articolo"],i)
        sp=ss.filter(idcod__settore__articolo=itemss["idcod__settore__articolo"]).values("idcod__produttore__azienda","idcod__produttore").order_by("idcod__produttore__azienda")        
        befss=itemss["idcod__settore__articolo"]      
      
        for itemp in sp:
          if(befsp==itemp["idcod__produttore__azienda"]):
            continue
          i=i+1
          msp=Model(itemp["idcod__produttore__azienda"],i)
          sc=sp.filter(idcod__produttore__azienda=itemp["idcod__produttore__azienda"]).values("q","idcod","idcod__cod","idcod__specifica__nome","idcod__specifica").order_by("idcod__specifica__nome")
          befsp=itemp["idcod__produttore__azienda"]
          
          for itemsc in sc:
            if(befsc==itemsc["idcod__specifica__nome"]):
              continue
            i=i+1
            msc=Model(itemsc["idcod__specifica__nome"],i)
            i=i+1
            msid=Model(itemsc["idcod__cod"]+" : "+ str(itemsc["q"]),itemsc["idcod"])
            msc.children.append(msid)
            msp.children.append(msc)               
          mss.children.append(msp)
        msg.children.append(mss)
      ls.append(msg)
    return ls  
  
  

  #for itemsg in sg:
    #if(befsg==itemsg["idcod__genere__nome"]):
      #continue
    #i=i+1
    #msg=Model(itemsg["idcod__genere__nome"],i)
    #ss=sg.filter(idcod__genere__nome=itemsg["idcod__genere__nome"]).values("idcod__settore__articolo","idcod__settore").order_by("idcod__settore__articolo")
    #befsg=itemsg["idcod__genere__nome"]
    
    #for itemss in ss:
      #if(befss==itemss["idcod__settore__articolo"]):
        #continue
      #i=i+1
      #mss=Model(itemss["idcod__settore__articolo"],i)
      #sp=ss.filter(idcod__settore__articolo=itemss["idcod__settore__articolo"]).values("idcod__produttore__azienda","idcod__produttore").order_by("idcod__produttore__azienda")        
      #befss=itemss["idcod__settore__articolo"]      
    
      #for itemp in sp:
        #if(befsp==itemp["idcod__produttore__azienda"]):
          #continue
        #i=i+1
        #msp=Model(itemp["idcod__produttore__azienda"],i)
        #sc=sp.filter(idcod__produttore__azienda=itemp["idcod__produttore__azienda"]).values("q","idcod","idcod__cod","idcod__specifica__nome","idcod__specifica").order_by("idcod__specifica__nome")
        #befsp=itemp["idcod__produttore__azienda"]
        
        #for itemsc in sc:
          #if(befsc==itemsc["idcod__specifica__nome"]):
            #continue
          #i=i+1
          #msc=Model(itemsc["idcod__specifica__nome"],i)
          #i=i+1
          #msid=Model(itemsc["idcod__cod"]+" : "+ str(itemsc["q"]),itemsc["idcod"])
          #msc.children.append(msid)
          #msp.children.append(msc)               
        #mss.children.append(msp)
      #msg.children.append(mss)
    #ls.append(msg)
  #return ls    