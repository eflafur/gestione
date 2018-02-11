from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import CreateTable,Modifica,GetProduct,validazione
import FCreateTable,FGetTable,FModifica,GetRGraph,ReportBilancio,MGetTable
import RModifica
import jsonpickle

login=1
def LKRGraph(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        if(message["act"]=="tree"):
            obj=GetRGraph.Design()
            res=obj.GetRGraph(message["flag"])  
            ret=jsonpickle.encode(res)
        elif(message["act"]=="set"):
            n=message["node"]
            p=message["peso"]
            objr=RModifica.MRim()
            ret=objr.ModPeso(n,p)
        elif(message["act"]=="lotto"):
            node=message["idnode"]
            objr=RModifica.MRim()
            ret=objr.GetLotto(node)
        elif(message["act"]=="push"):
            objr=RModifica.MRim()
            ret=objr.PushLotto(message)            
        return JsonResponse(ret,safe=False)             
    if(request.method=="GET"):
        if(request.GET.get("opr")):    
            message=request.GET
            flag=message["opr"]
            context={"el":flag}
        else:
            context={"items":" "}
        return render(request,"Rimanenza/Consultazione/RGraph.html",context)           

def RTot(request):
    res=""
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="cod"):
            obj=ReportBilancio.Estrazionecn()
            res=obj.Saldi(message)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":" "}
        return render(request,"Rimanenza/Report/Saldofn.html",context)    
    
def RArt(request):
    res=""
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="rart"):
            obj=ReportBilancio.GetReport()
            res=obj.BArt(message)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        obj=MGetTable.GetData()
        res=obj.GetIdCodAll()
        context={"items":res}
        return render(request,"Rimanenza/Report/Rart.html",context)    
 
def RTotArt(request):
    res=""
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="tart"):
            obj=ReportBilancio.GetReport()
            res=obj.BTotArt(message)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":" "}
        return render(request,"Rimanenza/Report/Rtotart.html",context)  

def RFrn(request):
    res=""
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        if(message["azione"]=="cod"):
            obj=ReportBilancio.Estrazionecn()
            res=obj.Giornale(message)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":" "}
        return render(request,"Rimanenza/Report/Giornale.html",context)  

def RScln(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        res=ReportBilancio.Estrazionecn.SaldoClienti()
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":" "}
        return render(request,"Rimanenza/Report/SaldoCliente.html",context)          

def RSfrn(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        res=ReportBilancio.Estrazionecn.SaldoFrn()
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":" "}
        return render(request,"Rimanenza/Report/SaldoFrn.html",context)   

def FattMese(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        res=ReportBilancio.Estrazionecn.Fatturato()
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":" "}
        return render(request,"Rimanenza/Report/FattMese.html",context)          



#metodi per report mastrini

def ContiMs(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)         
    if(request.method=="POST"):
        message=request.POST
        res=ReportBilancio.Reportms.Contims(message)
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        context={"items":" "}
        return render(request,"Rimanenza/Report/Contims.html",context)          




#metodi per report mastrini


def RBase(request):
    context={}
    return render(request,"Rimanenza/RBase.html",context)