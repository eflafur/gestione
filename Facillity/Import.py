import re
import sys
import io
import CreateTable


class getTable:
    def readTable(self,num): 
        line=" "
        lista=[]
        res=[]
#        x=importTableDb.actionDb()
#        y=open("/home/jafu/regione","w+")   
        f=open("/home/jafu/siti","r")
        obj=CreateTable.Siti()
        while(1==1): 
            line=f.readline()
            if(line!=""):
                res=re.sub('[\t]',";",line)
                res1=re.sub('[\n]',"",res)
                res2=res1.split(';')
                obj.put(res2) 
               # y.write(res)
                #lista.append(res)
                #x.writeOfferta(res)
            else:
                break
        return lista    