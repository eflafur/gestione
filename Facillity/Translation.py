import re
import sys
import io
import CreateTable


class ChangeFormat:
    def ChangeDate(self,date): 
        if(date!=""):
            res=re.sub('[/]',"-",date)
            res1=res.split('-')
            obj=25 
           # y.write(res)
            #lista.append(res)
            #x.writeOfferta(res)
        else:
            return
        return date    