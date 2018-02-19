from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import CreateTable,Modifica,GetProduct,validazione,FCreateTable,FGetTable,FModifica,MGetTable
import json,jsonpickle

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
            azn=message['a1'].strip()
            obj=FCreateTable.Produt()
            res=obj.put(message,azn)
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
    res=""
    res1=""
    itm=" "
    context={}
    if(request.method=="POST"):
        message=request.POST
        objf=FCreateTable.Produt()
        if(message["azione"]=='l'):
            obj=MGetTable.GetData()
            res=obj.GetCaricobyIdcod()
        if(message["azione"]=="I"):
            itm=message["item"]
            tot=message["tot"]
            pgm=message["pgm"]
            chc=message["chc"]
            cln=message["cln"]
            lst = jsonpickle.decode(message['res'])
            res=objf.ScriviFattura(lst,itm,pgm,tot,chc,cln)
        elif (message["azione"]=="S"):
            itm=message["item"]
            lst = json.loads(message['res'])
            res=objf.ScriviSospesa(lst,itm)
        elif (message["azione"]=="D"):
            itm=message["item"]
            lst = jsonpickle.decode(message['res'])
            res=objf.ScriviDDT(lst,itm)
        elif (message["azione"]=="R"):
            itm=message["item"]
            lst = jsonpickle.decode(message['res'])
            res=objf.ResoDDT(lst,message["item"],message["cln"])
        elif (message["azione"]=="reazione"):
            itm=message["item"]
            objf=FGetTable.GetData()
            res=objf.GetClienteByNumSospese(itm)
        elif (message["azione"]=="p"):
            itm=message["item"]
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        message=request.GET
        obj=GetProduct.LKPData()
        res=obj.GetIDcod()
        res2=obj.GetProdotto()
        res3=obj.GetTerminiPag()
        res4=obj.GetTara();
        objf=FGetTable.GetData()
        if(request.GET.get("azione")):
            dc={} 
            ls=[]
            res1=objf.GetClienteByNumSospese(message["nome"])
            dc["azienda"]=res1["doc"][0]["cliente__azienda"]
            dc["id"]=res1["doc"][0]["cliente__id"]
            ls.append(dc)
            context={"items":res,"itemsd":res2,"itemsp":res3,"itemsf":ls,"el":message["nome"],"itemtr":res4}
        else:
            res1=objf.GetCliente()
            context={"items":res,"itemsf":res1,"itemsd":res2,"itemsp":res3,"itemtr":res4}
        return render(request,"fatturazione/Creazione/fattura.html",context)
    
    
def RecFatt(request):
    res=""
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)
    if(request.method=="POST"):
        message=request.POST
        if(message["action"]=="ga"):
            objf=FCreateTable.Produt()
            res=objf.RecFatt(message);
        elif(message["action"]=="gf"):
            fatt=message["ft"]
            obj=FCreateTable.Produt()
            res=obj.GetFatturabyNum(fatt)
        elif(message["action"]=="rs"):
            ret=jsonpickle.decode(message["rsls"])
            fatt=message["ft"]
            cln=message["cln"]
            conto=message["chc"]
#            tot=message["tot"]
            obj=FCreateTable.Produt()
            res=obj.ScriviNotaC(ret,fatt,cln,conto)
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        objf=FGetTable.GetData()
        res=objf.GetCliente()
        context={"items":res}
        return render(request,"fatturazione/Modifica/Frecfatt.html",context)

def RecDdt(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)
    if(request.method=="POST"):
        message=request.POST
        objf=FCreateTable.Produt()
        res=objf.RecDdt(message);
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        context={"items":""}
        return render(request,"fatturazione/Modifica/Frecddt.html",context)    

def Sospesa(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)
    if(request.method=="POST"):
        message=request.POST
        objf=FCreateTable.Produt()
        res=objf.GetSospesa(message);
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        context={"items":""}
        return render(request,"fatturazione/Modifica/Fsospese.html",context)

def SospesabyCliente(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)
    if(request.method=="POST"):
        message=request.POST
        objf=FCreateTable.Produt()
        res=objf.GetSospesa(message);
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        objf=FGetTable.GetData()
        res=objf.GetCliente()
        context={"items":res}
        return render(request,"fatturazione/Modifica/Fsospese-cliente.html",context)

def DDT(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)
    if(request.method=="POST"):
        message=request.POST
        if(message["action"]=="tbl"):
            objf=FCreateTable.Produt()
            res=objf.GetDdt(message);
        elif(message["action"]=="ddt"):
            objf=FCreateTable.Produt()
            ddtls=jsonpickle.decode(message["ddt"])
            cln=message["cln"]
            pgm=message["pgm"]
            tot=message["tot"]
            conto=message["chc"]
            res=objf.DdtEmit(ddtls,cln,pgm,tot,conto)
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        obj=GetProduct.LKPData()
        res3=obj.GetTerminiPag()        
        objf=FGetTable.GetData()
        res=objf.GetCliente()
        context={"items":res,"itemtp":res3}
        return render(request,"fatturazione/Modifica/ddt-cliente.html",context)

def LKFatturabyCliente(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)
    if(request.method=="POST"):
        message=request.POST
        objf=FCreateTable.Produt()
        if(message["azione"]=="table"):
            res=objf.GetFattura(message);
        if(message["azione"]=="ftr"):
            p=message["fatt"]
            res=objf.GetFatturabyNum(p);
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        objf=FGetTable.GetData()
        res=objf.GetCliente()
        context={"items":res}
        return render(request,"fatturazione/Consultazione/Ffatture-cliente.html",context)

def LKFattura(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="t"):
            objf=FCreateTable.Produt()
            res=objf.GetFattura(message);
        if(message["azione"]=="p"):
            objf=FCreateTable.Produt()
            res=objf.Pagato(message);
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":""}
        return render(request,"fatturazione/Consultazione/Ffatture.html",context)
    
def LKDdt(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="table"):
            objf=FCreateTable.Produt()
            res=objf.GetDdt(message);
        elif(message["azione"]=="ftr"):
            p=message["fatt"]
            objf=FCreateTable.Produt()
            res=objf.GetDdtbyNum(p)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":""}
        return render(request,"fatturazione/Consultazione/Fddt.html",context)    
    
def LKFGraph(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        
        obj=GetGraph.Design()
        res=obj.GetFGraph()  
        ret=jsonpickle.encode(res)
        return JsonResponse(ret,safe=False)             
    if(request.method=="GET"):
        context={"items":" "}
        return render(request,"fatturazione/Consultazione/FGraph.html",context)          



def FBase(request):
    context={}
    return render(request,"fatturazione/FBase.html",context)