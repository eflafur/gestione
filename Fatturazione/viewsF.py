from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
#import sys, jsonpickle
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import CreateTable,Modifica,GetProduct,validazione
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



def Creaprd(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    global H1
    context={}
    if(request.method=="POST"):
        message=request.POST
        if(message["a2"]=="insert"):
            H1=1
            el=CreateTable.GetProd()
            a=message["vary"]
            res=el.GetCitta(a)            
            return JsonResponse(res,safe=False)
        elif(message['a2']!=""):
            if(H1!=1):
                context={}
                return render(request,"gestione/safe1.html",context)                 
            el=CreateTable.Produt()
            res=el.put(message)
            H1=0
            if(res==2):
                H1=0
                context={}
                return render(request,"gestione/safe.html",context)            
        el=CreateTable.GetProd()
        res=el.GetArticolo() 
        res1=el.GetArea()
        prod=el.GetProduttori()
        context={"items":res,"items1":res1,"items3":prod}
        return render(request,"fatturazione/insertF.html",context)            
        
    if(request.method=="GET"):
        el=CreateTable.GetProd()
        res=el.GetArticolo() 
        res1=el.GetArea()
        prod=el.GetProduttori()
        context={"items":res,"items1":res1,"items3":prod}
    return render(request,"fatturazione/InsertF.html",context)