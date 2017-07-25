from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
#import sys, jsonpickle
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
#import CreateTable,Modifica,GetProduct,validazione
#import wingdbstub
#nuova relaease salvata
#runserver --noreload 8000 


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
        return render(request,"gestione/insert.html",context)            
        
    if(request.method=="GET"):
        el=CreateTable.GetProd()
        res=el.GetArticolo() 
        res1=el.GetArea()
        prod=el.GetProduttori()
        context={"items":res,"items1":res1,"items3":prod}
    return render(request,"gestione/insert.html",context)

def Articolo(request):
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
            el=CreateTable.Sett()
            res=el.put(message)
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

def MP(request):
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
            #articolo=el.GetArticolo() 
            #res[0]['art']=articolo   
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
            if(H2!=1):
                context={}
                return render(request,"gestione/modify/safe_modifica.html",context)              
            #if (message['a1']==" "):
                #context={}
                #return render(request,"gestione/modify/safe_modifica.html",context)                    
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
        
def AddArt(request):   
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        if (message["insert"]=="prdc"):
            var=message["data"]
            obj=GetProduct.LKPData()
            res=obj.ListAddArt(var)
            return JsonResponse(res,safe=False)
        elif(message["insert"]=="add"): 
            art=message["articolo"]
            azd=message["azienda"]
            if(art!=""):
                obj=Modifica.ModProd()
                res=obj.AddArticolo(azd,art) 
            obj=GetProduct.LKPData()
            res=obj.ListAddArt(azd)            
            return JsonResponse(res,safe=False)            
    if(request.method=="GET"):
        el=Modifica.ModProd()
        prod=el.GetProduttori()
        context={"items":prod}
        return render(request,"gestione/modify/ModificaArt.html",context) 
        
def DelArt(request):      
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        if (message["insert"]=="dlrt"):
            var=message["data"]
            obj=GetProduct.LKPData()
            res=obj.ListDelArt(var)
            return JsonResponse(res,safe=False)
        elif((message["insert"]=="del") & (message["articolo"]!="")): 
            azd=message["azienda"]
            art=message["articolo"]
            if(art!=""):
                obj=Modifica.ModProd()
                res=obj.DelArticolo(azd,art) 
            obj=GetProduct.LKPData()
            res=obj.ListDelArt(azd)            
            return JsonResponse(res,safe=False)            
    if(request.method=="GET"):
        el=Modifica.ModProd()
        prod=el.GetProduttori()
        context={"items":prod}
        return render(request,"gestione/modify/DelArt.html",context)
        
def MA(request):
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
    context={}
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
        el=Modifica.ModProd()
        prod=el.GetArticolo()
        context={"items":prod}
        return render(request,"Consultazione/GetArticolo.html",context)    
def LKPMargine(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        var=message["data"]
        obj=GetProduct.LKPData()
        res=obj.getbyMargin(var)
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        context={"items":""}
        return render(request,"Consultazione/GetByMargin.html",context)        


#def LKArticolo(request):
    #if(request.method=="POST"):

    #if(request.method=="GET"):
    

def Logo(request):
    context={}
    return render(request,"gestione/logo.html",context)

def ImportTable(request):
    obj=Import.getTable()
    res=obj.readTable("go")
    context={}
    return render(request,"gestione/logo.html",context)



#--- per usi futuri---


#def Offerta(request):
    #if(request.method=="GET"):
        #context={}
    #return render(request,"dittemng/temp1.html",context)


#def Manage(request):
    #if(request.method=="POST"):
        #message=request.POST
        #x=Load.GetTable()
        #res=x.Load()
        #result=jsonpickle.encode(res)
        #result=json.dumps(res)
       ##result=({"settore":"a","area":"nord"},{"settore":"b","area":"est"},{"settore":"c","area":"ovest"})
        #return JsonResponse(result,safe=False)
    #if(request.method=="GET"):
        #x=Load.GetTable()
        #res=x.Load();
        #context={"vari":res}
    #return render(request,"dittemng/temp1.html",context)

#def DataTable(request):
    #if(request.method=='POST'):
        #message=request.POST
        #x=Table.Tbl()
        #var=x.Offerta("ciccio")
        ##result=jsonpickle.encode(var)
        #tt=JsonResponse(var, encoder=DjangoJSONEncoder, safe=False)
        #return tt
    #if(request.method=="GET"):
        #context={}	
    #return render(request,"dittemng/DataTable.html",context)



