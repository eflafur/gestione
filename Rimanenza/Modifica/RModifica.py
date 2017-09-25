from gestione.models import Carico,Saldo
from django.db.models import Q,F
    
class MRim:
    def ModPeso(self,node,colli):
        cll=int(colli)
        rec=Saldo.objects.get(idcod=node)
        saldo=rec.q-cll
        rec.q=saldo
        rec.save()
        self.PushCarico(node,cll)        
        return 1
    
    def PushCarico(self,cod,cassa):
        lotto=Carico.objects.filter(Q(idcod__id=cod),cassa__gt=F("cassaexit")).order_by("id")
        ltid=lotto.first()
        num=ltid.cassa-(cassa+ltid.cassaexit)
        if(num>=0):
            ltid.cassaexit=cassa+ltid.cassaexit
            ltid.save()
        else:
            ltid.cassaexit=ltid.cassa
            ltid.save()
            res=self.Rec(lotto,ltid.id,num*(-1),0)
        return 
    
    def Rec(self,lotti,lotto,casse,i):
        num=0
        try:
            num=lotti[i].cassa-(lotti[i].cassaexit+casse)
        except IndexError:
            return num
        if(num>=0 and lotti[i].id!=lotto):
            lt1=lotti.get(id=lotti[i].id)
            #lotti[i].cassaexit=lotti[i].cassaexit+casse
            #lotti[i].save()
            lt1.cassaexit=lotti[i].cassaexit+casse
            lt1.save()
#            return bl
            return 0
        else:
            if(lotti[i].id!=lotto):
                lt1=lotti.get(id=lotti[i].id)
                lt1.cassaexit=lotti[i].cassa
                lt1.save()
                #lotti[i].cassaexit=lotti[i].cassa
                #lotti[i].save()
            else:
                num=casse*(-1) 
            i=i+1
            res=self.Rec(lotti,lotto,num*(-1),i)
        return 0    