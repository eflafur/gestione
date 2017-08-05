from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import CreateTable,Modifica,GetProduct,validazione,Fviews,MCreateTable,MGetTable,MModifica
import re
#import wingdbstub
#nuova relaease salvata
#runserver --noreload 8000 

artic11=""
MPaz=" "
login=1
H1=0
H2=0
H3=0
H4=0

def CaricoMerci(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    global H1
    context={}
    if(request.method=="POST"):
        message=request.POST
        if((message["a1"]!="") & (message["a2"]!="")  & (message["a3"]!="")):
            obj1=MCreateTable.CreateData()
            res=obj1.Entrata(message)
            return JsonResponse(res,safe=False)
        #if(res==2):
            #var= message["a1"].split("-")
            #context={"avviso":"bolla esistente per il fornitore: "+ var[0],"azione":"entrata"}
            #return render(request,"gestione/safe1.html",context) 
        obj=GetProduct.LKPData()
        res=obj.GetIDcod("ciao")
        context={"items":res}
        return render(request,"Magazzino/Creazione/entrata.html",context)  
    if(request.method=="GET"):
        obj=GetProduct.LKPData()
        res=obj.GetIDcod("ciao")
        context={"items":res}
        return render(request,"Magazzino/Creazione/entrata.html",context)
    
def LKCaricoFornitore(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        if(message["res"]!=""):
            mgt=MGetTable.GetData()
            res=mgt.GetIdCod(message)
            return JsonResponse(res,safe=False)
        mod=Modifica.ModProd()
        prod=mod.GetProduttori()
        context={"items":prod}
        return render(request,"Magazzino/Consultazione/LKcaricofornitore.html",context)    
    if(request.method=="GET"):
        mod=Modifica.ModProd()
        prod=mod.GetProduttori()
        context={"items":prod}
    return render(request,"Magazzino/Consultazione/LKcaricofornitore.html",context)      

def EliminaBolla(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    global H1
    context={}
    if(request.method=="POST"):
        message=request.POST
        res=re.sub('[" "]',"",message["a1"])
        var=res.split("-")
        if((message["a2"]=="js")):
            obj1=MGetTable.GetData()
            res=obj1.GetBolla(var)
            return JsonResponse(res,safe=False)
        elif ((message["a2"]!="js")):
            obj5=MModifica.ModProd()
            res=obj5.DelBolla(var)
        obj3=MGetTable.GetData()
        res=obj3.GetCarico()
        context={"items":res}
        return render(request,"Magazzino/Modifica/eliminabolla.html",context)
    if(request.method=="GET"):
        obj3=MGetTable.GetData()
        res=obj3.GetCarico()
        context={"items":res}
        return render(request,"Magazzino/Modifica/eliminabolla.html",context)
