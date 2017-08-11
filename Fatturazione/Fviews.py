from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import CreateTable,Modifica,GetProduct,validazione,FCreateTable,FGetTable,FModifica
import json

artic11=""
MPaz=" "

login=1
H1=0
H2=0
H3=0
H4=0

def CreaAnagrafica(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    global H1
    context={}
    if(request.method=="POST"):
        message=request.POST
        if(message["a1"]=="insert"):
            H1=1
            obj=CreateTable.GetProd()
            a=message["vary"]
            res=obj.GetCitta(a)            
            return JsonResponse(res,safe=False)
        elif(message['a1']!=""):
            if(H1!=1):
                context={}
                return render(request,"fatturazione/FSafe1.html",context)                 
            obj=FCreateTable.Produt()
            res=obj.put(message)
            H1=0
            if(res==2):
                context={}
                return render(request,"fatturazione/FSafe.html",context)     
        obj=FGetTable.GetData()
        var=""
        res=obj.GetAnagrafica(var)            
        obj=CreateTable.GetProd()
        res1=obj.GetArea()
        context={"items":res,"items1":res1}
        return render(request,"fatturazione/Creazione/FInsert.html",context)            
    if(request.method=="GET"):
        obj=FGetTable.GetData()
        var=""
        res=obj.GetAnagrafica(var)
        obj=CreateTable.GetProd()
        res1=obj.GetArea()        
        context={"items":res,"items1":res1}
        return render(request,"fatturazione/Creazione/FInsert.html",context)

def ModificaAnagrafica(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    global H2
    global MPaz
    context={}
    if(request.method=="POST"):
        message=request.POST
        if(message["a1"]=="insert"):
            H2=1
            obj=FGetTable.GetData()
            a=message["var"]
            res=obj.GetAnagrafica(a)
            MPaz=res[0]['azienda']
            obj=Modifica.ModProd()
            regioni=obj.GetRegione() 
            res[0]['prova']=regioni
            citta=obj.GetCitta(res[0]['regione']) 
            res[0]['ct']=citta
            a=res
            return JsonResponse(res,safe=False)
        elif(message["a1"]=="regione"):
            a=message["var"]
            obj=FModifica.ModProd()
            res=obj.GetCliente(MPaz)
            obj=Modifica.ModProd()
            citta=obj.GetCitta(a) 
            res[0]['ct']=citta
            return JsonResponse(res,safe=False)            
        elif(message['a1']!="insert"):
            if(H2!=1):
                context={}
                return render(request,"fatturazione/Modifica/Fsafe_modifica.html",context)              
            obj=FModifica.ModProd()
            res=obj.Change(message)
            H2=0
            if(res==2):
                H2=0
                context={}
                return render(request,"fatturazione/Modifica/Fsafe_modifica.html",context)            
            obj=FGetTable.GetData()
            var=""
            res=obj.GetAnagrafica(var)
            context={"items":res}
        return render(request,"fatturazione/Modifica/FModificaAnagrafica.html",context)    
    if(request.method=="GET"):
        obj=FGetTable.GetData()
        var=""
        res=obj.GetAnagrafica(var)
        context={"items":res}
        H2=0
    return render(request,"fatturazione/Modifica/FModificaAnagrafica.html",context)    

def DelCliente(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    global H3
    context={}
    if(request.method=="POST"):
        message=request.POST
        if(message["a1"]=="insert"):
            H3=1
            obj=FGetTable.GetData()
            a=message["var"]
            res=obj.GetAnagrafica(a)
            return JsonResponse(res,safe=False)
        else:
            if(H3==1):
                var=message["a1"]
                obj=FModifica.ModProd()
                res=obj.DelCliente(var)
                H3=0
            obj=FGetTable.GetData()
            var=""
            res=obj.GetAnagrafica(var)
            context={"items":res}
            return render(request,"fatturazione/Modifica/FDelFornitore.html",context)    
    if(request.method=="GET"):
        obj=FGetTable.GetData()
        var=""
        res=obj.GetAnagrafica(var)
        context={"items":res}
    return render(request,"fatturazione/Modifica/FDelFornitore.html",context)  


def Fattura(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    context={}
    if(request.method=="POST"):
        message=request.POST
        lst = json.loads(message['res'])
        objf=FCreateTable.Produt()        
        if((message["azione"]=="invio")):
            objf.ScriviFattura(lst)
        elif ((message["azione"]=="sospesa")):
            objf.ScriviSospesa(lst)
        res=""
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        obj=GetProduct.LKPData()
        res=obj.GetIDcod("ciao")
        objf=FGetTable.GetData()
        res1=objf.GetCliente()
        context={"items":res,"itemsf":res1}
        return render(request,"fatturazione/Creazione/fattura.html",context)    





def FBase(request):
    context={}
    return render(request,"fatturazione/FBase.html",context)