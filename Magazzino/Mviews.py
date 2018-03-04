from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from decimal import Decimal
import CreateTable,Modifica,GetProduct,validazione,Fviews,MCreateTable,MGetTable,MModifica
import testdb,Import
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
            bolla1=message["bolla1"]
            facc=message["facc"]
            tras=message["tras"]
            vari=message["vari"]
            dt=message["dt"]
            cl=message["cl"]
            obj1=MCreateTable.CreateData()
            res=obj1.EntrataBolla(lst,bolla,bolla1,dt,facc,tras,vari,cl)
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
        res=objm.GetIdCod(message);
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        message=request.GET
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
            res=obj.GetBollaCv1(v)
        elif(message["azione"]=="b1"):
            obj=MGetTable.GetData()
            res=obj.GetBollabyPrd(message)
        elif(message["azione"]=="p"):
            ret=jsonpickle.decode(message["data"])
            mrg=message["mrg"]
            frn=message["frn"]
            obj=MGetTable.GetData()
            res=obj.PushBollaCv(ret,frn,mrg)
        elif(message["azione"]=="p1"):
            ret=jsonpickle.decode(message["data"])
            frn=message["frn"]
            obj=MGetTable.GetData()
            res=obj.GetBolla1(ret,frn)            
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
            obj=MGetTable.GetData()
            res=obj.GetCvFatt(message)
        elif(message["azione"]=="p"):
            ret=jsonpickle.decode(message["data"])
            fatt=message["fatt"]
            frn=message["frn"]
            idfrn=message["idfrn"]
            mrg=message["mrg"]
            dt=message["date"]
            obj=MGetTable.GetData()
            res=obj.SaveCvFatt(ret,fatt,frn,mrg,dt,idfrn)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        obj=Modifica.ModProd()
        res=obj.GetProduttori()
        context={"prod":res}
        return render(request,"Magazzino/Bilancio/fattfrn.html",context)
    
def RegFattFrn(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="t"):
            objf=MGetTable.GetData()
            res=objf.GetFattFrn(message);
        if(message["azione"]=="ftr"):
            p=message["fatt"]
            objf=MGetTable.GetData()
            res=objf.GetFatt(p);
        if(message["azione"]=="p"):
            objf=MGetTable.GetData()
            res=objf.Pagato(message);
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":""}
        return render(request,"Magazzino/Consultazione/RegFattFrn.html",context)        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#test----------------------------------------------

#def Gioco(request):
    #res=""
    #res1=""
        
    #global H1
    #context={}
    #if(request.method=="POST"):
        #message=request.POST
        #if(message["azione"]=="db"):
            #res=testdb.Clienti(333,222,"3.1",0,"brero","001")
            #res.Vendita()
            #res.SetErarioCliente()
        ##if(message["a2"]=="insert"):
            ##H1=1
            ##el=CreateTable.GetProd()
            ##a=message["vary"]
            ##res=el.GetCitta(a)            
            ##return JsonResponse(res,safe=False)
        ##elif(message['a2']!=""):
            ##if(H1!=1):
                ##context={}
                ##return render(request,"gestione/safe1.html",context)                 
            ##el=CreateTable.Produt()
            ##res=el.put(message)
            ##H1=0
            ##if(res==2):
                ##H1=0
                ##context={}
                ##return render(request,"gestione/safe.html",context)            
        #el=CreateTable.GetProd()
        #res1=el.GetArea()
        #prod=el.GetProduttori()
        #context={"items":res,"items1":res1,"items3":prod}
        #return render(request,"Magazzino/gioco.html",context)            
    #if(request.method=="GET"):
        #el=CreateTable.GetProd()
        #res1=el.GetArea()
        #prod=el.GetProduttori()
        #context={"items1":res1,"items3":prod}
    #return render(request,"Magazzino/gioco.html",context)


def Gioco(request):

    #obj=Import.getTable()
    #obj.readTable()
    #if(request.method=="POST"):
        #message=request.POST
    #res=testdb.Pdf("floppolo.pdf")
    #res.Do()
    context={res:""}
    return render(request,"Magazzino/gioco.html",context)        
    