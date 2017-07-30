import django
django.setup()
from gestione.models import Cliente, Area,Sito
from django.db.models import Q

class Produt:
    def put(self,line):
        self.row=line
        p=Cliente.objects.filter(Q(azienda=self.row["a1"])) 
        if (p):
            return (2)
        p=Cliente.objects.create(
            azienda=self.row["a1"],
            citta=self.row["a4"],
            regione=self.row["a3"],
            pi=self.row["a2"],
            indirizzo=self.row["a7"],
            acquisizione=self.row["a5"],
            email=self.row["a6"],
            trpag=self.row["a9"],
            tel=self.row["a8"],
        )
        return (1)
