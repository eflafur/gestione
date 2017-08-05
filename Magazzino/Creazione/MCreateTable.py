from gestione.models import IDcod,Carico
from django.db.models import Q
import re
import sys
import io

class CreateData:
    def Entrata(self,line):
        seg=line["a1"].split('-')
        p=Carico.objects.filter(Q(bolla=line["a3"]),Q(idcod__produttore__azienda= seg[0]))
        if(p):
            return 2
        cod=IDcod.objects.get(cod=line["a1"])
        rec=Carico(q=line["a2"],bolla=line["a3"],idcod=cod)
        rec.save()