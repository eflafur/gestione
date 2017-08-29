from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import CreateTable,Modifica,GetProduct,validazione,Fviews,MCreateTable,MGetTable,MModifica
import re,json
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
bl=[]

def CreaBolla(request):
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)        
    global bl
    ls1=[]
    if(request.method=="POST"):
        ls1.clear()
        message=request.POST
        if(message["azione"]=="gid"):
            
            ls1.append(re.sub(" ","",(message["bolla"])))
            ls1.append(message["cliente"])
            objf=MGetTable.GetData()
            res1=objf.GetBolla(ls1)         
            if(res1 and message["dod"]==" "):
                res="full"
            elif (message["dod"]!=" "):
                obj1=GetProduct.LKPData()
                res2=obj1.GetIDcodbyProvider(message)            
                objf=MGetTable.GetData()
                res3=objf.GetBolla(bl)
                res={}
                res["a"]=res2
                res["b"]=res3
            else:
                obj1=GetProduct.LKPData()
                res=obj1.GetIDcodbyProvider(message)            
        elif(message["azione"]=="I"):
            lst = json.loads(message['res'])
            bolla=message["bolla"]
            obj1=MCreateTable.CreateData()
            res=obj1.EntrataBolla(lst,bolla)
        return JsonResponse(res,safe=False)
    if(request.method=="GET"):
        message=request.GET
        if(request.GET.get("azione")):
            bl.clear()
            dc={} 
            ls=[]
            bl.append(message["bolla"])
            bl.append(message["cliente"])
            dc["azienda"]=message["cliente"]
            ls.append(dc)
            context={"prod":ls,"el":bl[0]}
        else:
            obj=Modifica.ModProd()
            prod=obj.GetProduttori()
            context={"prod":prod}
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
    if(login==0):
        context={}
        return render(request,"Validazione/login.html",context)     
    if(request.method=="POST"):
        message=request.POST
        objm=MGetTable.GetData()
        if(message["prs"]!=" "):
            res=objm.GetBolla(bl)
        else:
            res=objm.GetIdCod(message);
        return JsonResponse(res,safe=False)        
    if(request.method=="GET"):
        message=request.GET
        if(request.GET.get("azione")):
            bl.clear()
            dc={} 
            ls=[]
            bl.append(message["bolla"])
            bl.append(message["cliente"])
            dc["azienda"]=message["cliente"]
            ls.append(dc)
            context={"prod":ls,"el":bl[0]}
        else:        
            mod=Modifica.ModProd()
            prod=mod.GetProduttori()
            context={"prod":prod,"el":" "}
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
        res=re.sub('[" "]',"",message["a1"])
        var=res.split(":")
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
    
   


# per la selezione anche dell'articolo*****
#def LKCaricoProdotto(request):
    #if(login==0):
        #context={}
        #return render(request,"Validazione/login.html",context)     
    #global H4
    #context={}
    #if(request.method=="POST"):
        #message=request.POST
        #if(message["s1"]=="insert"):
            #H4=1
            #obj6=CreateTable.GetSett()
            #a=message["var"]
            #res=obj6.GetSettore(a)     
            #return JsonResponse(res,safe=False)  
        #elif(message["s1"]=="table"):
            #obj7=MGetTable.GetData()
            #res=obj7.GetIdCodbyProdotto(message)     
            #return JsonResponse(res,safe=False)        
        #else: 
            #if(H4==1):
                #el=CreateTable.Sett()
                #res=el.Delete(message)
                #H4=0
            #el=CreateTable.GetSett()
            #res=el.GetGenere() 
            #context={"items":res}
            #return render(request,"Magazzino/Consultazione/LKcaricoprodotto.html",context)
    #if(request.method=="GET"):
        #el=CreateTable.GetSett()
        #res=el.GetGenere() 
        #context={"items":res}
    #return render(request,"Magazzino/Consultazione/LKcaricoprodotto.html",context)






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