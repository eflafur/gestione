from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import CreateTable,Modifica,GetProduct,validazione,Fviews,MCreateTable,MGetTable,MModifica
import re,json,jsonpickle
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


def CreaBolla(request):
    dc={} 
    ls=[]
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)        
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="gid"):
            objf=MGetTable.GetData()
            res1=objf.GetBolla(message)         
            if(res1):
                obj1=GetProduct.LKPData()
                res2=obj1.GetIDcodbyProvider(message)            
                res={}
                res["a"]=res2
                res["b"]=res1
            else:
                obj1=GetProduct.LKPData()
                res=obj1.GetIDcodbyProvider(message)            
        elif(message["azione"]=="I"):
            lst = jsonpickle.decode(message['res'])
            bolla=message["bolla"]
            dt=message["dt"]
            obj1=MCreateTable.CreateData()
            res=obj1.EntrataBolla(lst,bolla,dt)
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        message=request.GET
        if(request.GET.get("azione")):
            dc["azienda"]=message["cliente"]
            ls.append(dc)
            context={"prod":ls,"el":message["bolla"]}
        else:
            obj=Modifica.ModProd()
            prod=obj.GetProduttori()
            context={"prod":prod,"el":""}
        return render(request,"Magazzino/Creazione/bolla.html",context)   

def LKCaricoTotale(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        objm=MGetTable.GetData()
        res=objm.GetCaricoTotale(message);
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":""}
        return render(request,"Magazzino/Modifica/Mbolle.html",context)
    
def LKCaricoFornitore(request):
    ls1=[]
    dc={} 
    ls=[]
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     

    if(request.method=="POST"):
        message=request.POST
        objm=MGetTable.GetData()
        #if(message["prs"]!=""):
            #ls1.append(message["prs"])
            #ls1.append(message["res"])
            #res=objm.GetBolla(ls1)
        #else:
        res=objm.GetIdCod(message);
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        message=request.GET
        #if(request.GET.get("azione")):
            #dc["azienda"]=message["cliente"]
            #ls.append(dc)
            #context={"prod":ls,"el":message["bolla"]}
        #else:        
        mod=Modifica.ModProd()
        prod=mod.GetProduttori()
        context={"prod":prod,"el":""}
        return render(request,"Magazzino/Modifica/Mfbolle.html",context) 

def LKCaricoProdotto(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        obj7=MGetTable.GetData()
        res=obj7.GetIdCodbyProdotto(message)     
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
# inserimento IVA causa shell non funziona
        el=CreateTable.GetSett()
        res=el.GetGenere() 
        context={"items":res}
        return render(request,"Magazzino/Consultazione/LKcaricoprodotto.html",context)

def EliminaBolla(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    global H1
    context={}
    if(request.method=="POST"):
        message=request.POST
        res=message["a1"]
#        res=re.sub('[" "]',"",message["a1"])
        var=res.split(":")
        obj5=MModifica.ModProd()
        res=obj5.DelBolla(var)
        obj5=MGetTable.GetData()
        res=obj5.GetCarico()
        context={"items":res}
        return render(request,"Magazzino/Modifica/eliminabolla.html",context)
    if(request.method=="GET"):
        obj3=MGetTable.GetData()
        res=obj3.GetCarico()
        context={"items":res}
        return render(request,"Magazzino/Modifica/eliminabolla.html",context)
    
def Contov(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="b"):
            obj=MGetTable.GetData()
            v=message["cln"]
            res=obj.GetBollaCv(v)
        if(message["azione"]=="p"):
            ret=jsonpickle.decode(message["data"])
            #if(ret[0]==None):
                #ret.pop(0);
            mrg=message["mrg"]
            frn=message["frn"]
            obj=MGetTable.GetData()
            res=obj.PushBollaCv(ret,frn,mrg)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        obj=Modifica.ModProd()
        res=obj.GetProduttori()
        context={"items":res}
        return render(request,"Magazzino/Consultazione/contov.html",context)

def ContovT(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        x=message["item"]
        obj3=MGetTable.GetData()
        res=obj3.GetCaricoTotaleCv(x)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":""}
        return render(request,"Magazzino/Consultazione/contovt.html",context)


def FattFrn(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="g"):
            obj=MGetTable.GetData()
            res=obj.GetCvbyPrd(message)
        elif(message["azione"]=="v"):
            v=message["cvd"]
            obj=MGetTable.GetData()
            res=obj.GetCvFatt(v)
        elif(message["azione"]=="p"):
            ret=jsonpickle.decode(message["data"])
            fatt=message["fatt"]
            frn=message["frn"]
            mrg=message["mrg"]
            obj=MGetTable.GetData()
            res=obj.SaveCvFatt(ret,fatt,frn,mrg)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        obj=Modifica.ModProd()
        res=obj.GetProduttori()
        context={"prod":res}
        return render(request,"Magazzino/Bilancio/fattfrn.html",context)
    
#test----------------------------------------------























def Gioco(request):
    res=""
    res1=""
        
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
        res1=el.GetArea()
        prod=el.GetProduttori()
        context={"items":res,"items1":res1,"items3":prod}
        return render(request,"Magazzino/gioco.html",context)            
    if(request.method=="GET"):
        el=CreateTable.GetProd()
        res1=el.GetArea()
        prod=el.GetProduttori()
        context={"items1":res1,"items3":prod}
    return render(request,"Magazzino/gioco.html",context)