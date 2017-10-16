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
def EReg(request):
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
