from gestione.models import Carico,Saldo
from django.db.models import Q
    
class MRim:
    def ModPeso(self,node,peso):
        rec=Saldo.objects.get(idcod=node)
        rec.q=peso
        rec.save()
        return 1