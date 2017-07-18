from dittemng.models  import azienda,general,offerta,level
from django.db.models import Q

class dataModel():
    ruolo=""
    tipo=""
    qualifica=""
    aziendale__azienda=""
    lista=[]

lista=[]

class DataTbl:
    def GetOfferta(self,what):
        #res=Offerta.objects.filter(Q(azienda__general__settore="medico")
        #|Q(azienda__general__settore="turismo")).values("ruolo",
        #"tipo","qualifica","azienda__azienda","azienda__general__settore","level__qualifica")
        
        res=general.objects.filter(Q(azienda__offerta__level__qualifica="tecnico")
        & Q(azienda__capitale__lte=4555000)).values("azienda__offerta__ruolo",
        "azienda__offerta__level__qualifica","azienda__azienda")

        data=list(res) #usata per le 2 query sopra 
        
        #res=general.objects.filter(Q(azienda__offerta__level__qualifica="tecnico")
        #& Q(azienda__capitale__lte=4555000))        
        
        #data=list(res.values("azienda__offerta__ruolo",
        #"azienda__offerta__level__qualifica","aziendale__azienda"))      #usata per la query sopra   

        #lista=[]
        #data=[]
       
        #for item in res:
            #m=dataModel()
            #m.ruolo=item.ruolo
            #m.tipo=item.tipo
            #m.qualifica=item.qualifica
            #lista.append(m)
        #for item in lista:
                #data.append(
                    #{'ruolo': item.ruolo,
                    #'tipo': item.tipo,
                    #"qualifica":item.qualifica,
                    #}
                #)
                
            #usata per la query sopra 

        return data

class DataTablePage:
    def GetData(self,what):
        self.sett=what
        res=azienda.objects.filter(Q(general__areageografica=2))
        res=general.objects.filter(Q(azienda__offerta__level__qualifica="tecnico"))
        data=[]
        for item in res:
            m=dataModel()
            m.ruolo=item.settore
            m.tipo=item.areageografica
            m.qualifica=item.numofferte
            data.append(m)
        return data            

