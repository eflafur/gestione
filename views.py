from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
#import CreateTable,Modifica,GetProduct,validazione,Fviews,GetGraph
import jsonpickle
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

def Logout(request):
    global login
    login=0
    context={"items":"Fine sessione"}
    return render(request,"Validazione/Logout.html",context)    
    
def Login(request):
    global login
    if(request.method=="POST"):
        message=request.POST
        obj=validazione.Credentials()
        res=obj.GetCredentials(message)
        if(res==1):
            login=1
            context={}
            return render(request,"gestione/base.html",context)
        elif(res==0):
            context={"items":"autenticazione non riuscita"}
            return render(request,"Validazione/login.html",context)
    if(request.method=="GET"):
        context={}
    return render(request,"Validazione/login.html",context)    

def Produttore(request):
    res=""
    res1=""
    global H1
    context={}
    if(login==0):
        return render(request,"Validazione/login.html",context)         
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
            azn=message['a2'].strip()
            el=CreateTable.Produt()
            res=el.put(message,azn)
            H1=0
        el=CreateTable.GetProd()
        res1=el.GetArea()
        prod=el.GetProduttori()
        context={"items":res,"items1":res1,"items3":prod}
        return render(request,"gestione/insert.html",context)            
    if(request.method=="GET"):
        el=CreateTable.GetProd()
        res1=el.GetArea()
        prod=el.GetProduttori()
        context={"items1":res1,"items3":prod}
    return render(request,"gestione/insert.html",context)

def CreaArticolo(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    context={}
    if(request.method=="POST"):
        message=request.POST
        if(message["s1"]=="insert"):
            el=CreateTable.GetSett()
            a=message["var"]
            res=el.GetSettore(a)     
            return JsonResponse(res,safe=False)        
        if((message['s1']!="insert")& (message['s2']!="")):
            sett=message['s2'].strip()
            el=CreateTable.Sett()
            res=el.put(message,sett)
            if(res==2):
                context={}
                return render(request,"gestione/safe_settore.html",context)
            el=CreateTable.GetSett()
            res=el.GetGenere() 
            context={"items":res}
            return render(request,"gestione/settore.html",context)
        elif(message['s2']==""):
            request.method="GET"
    if(request.method=="GET"):
        el=CreateTable.GetSett()
        res=el.GetGenere() 
        context={"items":res}
    return render(request,"gestione/settore.html",context)

def ModProd(request):
    res=""
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    global H2
    global MPaz
    context={}
    if(request.method=="POST"):
        message=request.POST
        if(message["a2"]=="insert"):
            H2=1
            el=Modifica.ModProd()
            a=message["var"]
            res=el.GetAll(a)
            MPaz=res[0]['azienda']
            regioni=el.GetRegione() 
            res[0]['prova']=regioni
            citta=el.GetCitta(res[0]['regione']) 
            res[0]['ct']=citta
            a=res
            return JsonResponse(res,safe=False)
        elif(message["a2"]=="regione"):
            el=Modifica.ModProd()
            a=message["var"]
            res=el.GetAll(MPaz)
            citta=el.GetCitta(a) 
            res[0]['ct']=citta
            return JsonResponse(res,safe=False)            
        elif(message['a2']!="insert"):
            if(H2==1):
                el=Modifica.ModProd()
                res=el.Change(message)
            H2=0
            if(res==2):
                H2=0
                context={}
                return render(request,"gestione/modify/safe_modifica.html",context)            
            el=Modifica.ModProd()
            prod=el.GetProduttori()
            context={"items":prod}
        return render(request,"gestione/modify/Modifica.html",context)    
    if(request.method=="GET"):
        el=Modifica.ModProd()
        prod=el.GetProduttori()
        context={"items":prod}
        H2=0
    return render(request,"gestione/modify/Modifica.html",context)        
        
def AddCod(request):   
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        obj=GetProduct.LKPData()
        message=request.POST
        if (message["a2"]=="genere"):
            res=obj.GetGenere()
            return JsonResponse(res,safe=False)
        elif(message["a2"]=="settore"): 
            var=message["genere"]
            res=obj.GetByGenere(var)
            return JsonResponse(res,safe=False)
        elif(message["a2"]=="spec"): 
            var=message["articolo"]
            res=obj.GetSpec(var)
            return JsonResponse(res,safe=False)        
        elif(message["a1"]!=""):
            if ((message["a1"]!="") & (message["a2"]!="")  & (message["a3"]!="" )):
                cat=message["a4"].strip()
                obj=Modifica.ModProd()
                res=obj.ChangeSpec(message,cat)
                if(res==2):
                    context={}
                    return render(request,"gestione/modify/safe_modifica.html",context)
        obj=Modifica.ModProd()
        prod=obj.GetProduttori()
        context={"items":prod}
        return render(request,"gestione/modify/ModificaArt.html",context)
    if(request.method=="GET"):
        obj=Modifica.ModProd()
        prod=obj.GetProduttori()
        context={"items":prod}
        return render(request,"gestione/modify/ModificaArt.html",context)
        
def DelArt(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    global H4
    context={}
    if(request.method=="POST"):
        message=request.POST
        if(message["s1"]=="insert"):
            H4=1
            el=CreateTable.GetSett()
            a=message["var"]
            res=el.GetSettore(a)     
            return JsonResponse(res,safe=False)             
        else: 
            if(H4==1):
                el=CreateTable.Sett()
                res=el.Delete(message)
                H4=0
            el=CreateTable.GetSett()
            res=el.GetGenere() 
            context={"items":res}
            return render(request,"gestione/modify/Modifica_settore.html",context)
    if(request.method=="GET"):
        el=CreateTable.GetSett()
        res=el.GetGenere() 
        context={"items":res}
    return render(request,"gestione/modify/Modifica_settore.html",context)

def DelFornitore(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    global H3
#    context={}
    if(request.method=="POST"):
        message=request.POST
        if(message["a2"]=="insert"):
            H3=1
            el=Modifica.ModProd()
            a=message["var"]
            res=el.GetAll(a)
            return JsonResponse(res,safe=False)
        else:
            el=CreateTable.GetProd()
            if(H3==1):
                var=message["a2"]
                res=el.DelProduttori(var)
                H3=0
            prod=el.GetProduttori()
            context={"items":prod}
            return render(request,"gestione/modify/DelFornitore.html",context)    
    if(request.method=="GET"):
        el=Modifica.ModProd()
        prod=el.GetProduttori()
        context={"items":prod}
    return render(request,"gestione/modify/DelFornitore.html",context)    

def LKProduttore(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        var=message["data"]
        obj=GetProduct.LKPData()
        res=obj.getbyCompany(var)
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        el=Modifica.ModProd()
        prod=el.GetProduttori()
        context={"items":prod}
        return render(request,"Consultazione/GetProduct.html",context)          
    
def LKPArticolo(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        var=message["data"]
        obj=GetProduct.LKPData()
        res=obj.getbyArticolo(var)
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        el=GetProduct.LKPData()
        prod=el.GetGenere()
        context={"items":prod}
        return render(request,"Consultazione/GetArticolo.html",context)    
    
def LKPMargine(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        var=message["data"]
        if(var!=""):
            obj=GetProduct.LKPData()
            res=obj.getbyMargin(var)
            return JsonResponse(res,safe=False)
        context={"items":""}
        return render(request,"gestione/Consultazione/GetByMargin.html",context)        
    if(request.method=="GET"):
        context={"items":""}
        return render(request,"gestione/Consultazione/GetByMargin.html",context)
    

def Graffo(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        obj=GetGraph.Design()
        res=obj.GetGraph()  
        ret=jsonpickle.encode(res)
        return JsonResponse(ret,safe=False)             
    if(request.method=="GET"):
        context={"items":" "}
        return render(request,"gestione/Consultazione/GGraph.html",context)           
    
    

def Base(request):
    context={}
    return render(request,"gestione/base.html",context)

def Logo(request):
    context={}
    return render(request,"gestione/logo.html",context)






