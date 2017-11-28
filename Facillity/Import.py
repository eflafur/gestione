import re
import sys
import io
import CreateTable


class getTable:
    def readTable(self): 
        line=" "
        lista=[]
        res=""
        res1=[]
#        x=importTableDb.actionDb()
#        y=open("/home/jafu/regione","w+")   
        f=open("/home/jafu/antonio","r")
        obj=CreateTable.Siti()
        while(1==1): 
            line=f.readline()
            if(line!=""):
                res=re.sub('[\n]',"",line)
                res1=res.split(';')
                obj.put(res1) 
               # y.write(res)
                #lista.append(res)
                #x.writeOfferta(res)
            else:
                break
        return lista    
    


class Color:
    def __init__(self, color):
        self.color = color
    def getcolor(self):
        return self.color    