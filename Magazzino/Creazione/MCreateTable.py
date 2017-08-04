from gestione.models import IDcod,Carico
from django.db.models import Q

class CreateData:
    def Entrata(self,line):
        cod=IDcod.objects.get(cod=line["a1"])
        rec=Carico(q=line["a2"],bolla=line["a3"],idcod=cod)
        rec.save()