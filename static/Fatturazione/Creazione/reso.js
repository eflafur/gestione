var ar1= [];
var sum;
var i=0;
var cliente;
var pvl=$("#psps").text();
var tipo=pvl.substr(0,2)
var lotto=[];    
var sos=[];    
var lt="";
var f;
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    
    $("#css").hide();
    $("#cod").hide();
    $("#lt").val();
    else if(tipo=="fc" ){
        $("#cliente").attr('disabled',true);
        $("#codice").attr('disabled',true);
        $("#cod").hide();
        $("#dsc").hide();
        $("#tr").hide();
        $("#lt").hide();
        $("#btsps").hide();
        $("#ddtft").hide();
        GetSospesa();
    } 
     $("#codice").click(function(){
        $("#btltsos").hide();    
        var cod=$("#codice option:selected").text();
        SelLotto(cod);
        $("#dsc").show();
        $("#desc").focus();
        $("#lt").show();
    });
    
    $("#peso").keypress(function(){
        $("#css").show();
    });
    $("#cassa").keypress(function(){
        $("#prz").show();
    });
    $("#cassa").on("blur", function(){
        if(parseInt($("#cassa").val())>sum){
            alert("superato il lotto massimo di magazzino")
            $("#cassa").val(sum);
            $("#prezzo").focus();
        }
    });
    
    $("#prezzo").keypress(function(){
            $("#pgm").show();
            $("#btadd").show();
    });
    
    
    $("#btems").click(function(){
        Invia('I');
        ar1.length=0
        Eval();
    });
    
    
    $("#btanl").click(function(){
        ar1.length=0
        if(pvl!="")
            window.location.replace("sospesa");
         Eval();

    });
    
    $("#btadd").click(function(){
        a=$("#peso").val();
        b=$("#prezzo").val();
        c=$("#cassa").val();
        if(a==""){
            alert ("inserire peso")
            $("#peso").focus()
        }
        else if(b==""){
            alert ("inserire prezzo")
            $("#prezzo").focus()   
        }
        else if(c==""){
            alert ("inserire Num Casse")
            $("#cassa").focus()
        }
        else {
            var obj={}
            obj['diff']=0;
            obj['cln'] =$("#cliente").val();
            obj['cod'] =$("#codice option:selected").text();
            obj['ps'] =$("#peso").val();
            obj['css'] =$("#cassa").val();
            obj['prz'] =$("#prezzo").val();
            obj["iva"]=$("#codice option:selected").val();
            obj['tara']=$("#tara option:selected").val();
            obj['lotto']=lt;
            ar1.push(obj);
            lt="";
            Fill();
            if((tipo!="dd") & (tipo!="fc"))
                $("#codice").attr('disabled',false);
            $("#tbf").show("");
            $("#peso").val("");
            $("#cassa").val("");
            $("#prezzo").val("");
            $("#ps").hide();
            $("#css").hide();
            $("#prz").hide();
            $("#btadd").hide();
            $("#pgm").hide();
            $("#pagam").attr('disabled',true);
            $("#tr").hide();
            $("#dsc").hide();
            $("#cod").focus();
            $("#cliente").attr('disabled',true);
            $("#lt").hide();
            $("#btltsos").hide();    
        }
        return;
    });

    $("#lotto").on('click',function(){
        lt=$(this).val();
    });

   $('#tbfb').on('click','a',function(){
        var arr= [];
        arr=$(this).text().split('-');   
        if(arr[1]=='E')
            DeleteRow(arr[0]);
        else if(arr[1]=='A')
            AddRow(arr[0]);
    });
});


function Eval(){
    $("#tbf").hide("");
    $("#cliente").attr('disabled',false);
    $("#cliente").focus();
    $("#cod").hide("");
    $("#ps").hide();
    $("#css").hide();
    $("#prz").hide();  
    $("#btadd").hide();
    $("#dsc").hide();
    $("#pgm").hide();
    $("#lt").hide();
};

function Fill(){
    var label="";
    var k=0;
    var sumf=0;
    for (i = 0; i < ar1.length; i++) {
        k=k+1
        imp=ar1[i].prz*ar1[i].ps*(parseFloat(ar1[i].iva)+1)
        sumf=sumf+ar1[i].prz*ar1[i].ps*(parseFloat(ar1[i].iva)+1);
        label = label + '<tr>';
        label = label + '<td>' + ar1[i].cod+ '</td>';
        label = label + '<td>' + ar1[i].ps+ '</td>';
        label = label + '<td>' + ar1[i].css+ '</td>';
        label = label + '<td>' + ar1[i].iva+ '</td>';
        label = label + '<td>' + ar1[i].prz+ '</td>';
        label = label + '<td>' + imp+ '</td>';
//        label = label + '<td>' + ar1[i].lotto+ '</td>';
        if(pvl=="" || tipo=="sc"){
            label = label + '<td> <a href="#" ><p>'+k+'-E'+'</p></a></td>';
            label = label + '<td> <a href="#" ><p>'+k+'-A'+'</p></a></td>';
        }
        else
            label = label + '<td> <a href="#" ><p>'+k+'-A'+'</p></a></td>';
        label = label + '<td>' + ar1[i].diff+ '</td>';
        label = label + '</tr>';
    }
    label=label + '<tr><td>TOT</td><td></td><td></td><td></td><td></td><td>'+sumf.toFixed(2)+ '</td></tr>';
    $("#tbfb").html(label);
    $("#tbfb tr:last").find("td:last").css("color","blue");
    return;
};

function Invia(act){
    $.post(
        "fattura",
      {res:JSON.stringify(ar1),azione:act,item:pvl,pgm:$("#pagam").val()},
    function (result){
    });
    return;  
    $("#dsc").hide();

};
function AddRow(row){
    t=ar1[row-1].cod;
    lt=ar1[row-1].lotto;
    DeleteRow(row)
    $("#ps").show();
    $("#codice").attr('disabled',true);
    $("#codice option:contains("+t+")").prop('selected', true)
    if((tipo=="dd") | (tipo=="fc")){
       sum=ar1[row-1].css
        $("#pagam").attr('disabled',true);
    }
    else   
       SelLottoSos(t);
};

function GetSospesa(){
    $.post(
        "fattura",
        {item:pvl,azione:"reazione"},
        function(ret){
            var res=ret["doc"];
            for (i=0;i<res.length;i++){
                var obj1={}  
                obj1['diff']=0
                obj1['cln'] =$("#cliente").val();
                obj1['cod'] =res[i].idcod__cod;
                obj1['ps'] =res[i].q;
                obj1['prz'] =res[i].prezzo;
                obj1['css'] =res[i].cassa;
                obj1['lotto']=res[i].lotto;
                obj1['tara']=res[i].tara;
                obj1["iva"]=parseFloat(res[i].idcod__genere__iva)+1
                ar1.push(obj1);
            }
        Fill();
        $("#cod").show("");
        $("#tbf").show("");
        });
};


function GetSospesaSos(){
    $.post(
        "fattura",
        {item:pvl,azione:"reazione"},
        function(ret){
            var res=ret["doc"];
            lotto=ret["cr"];
            var t=0;
            var ctr=0;
            for (i=0;i<res.length;i++){
                var obj1={}  
                t=0
                obj1['diff']=0
                for (k=0;k<lotto.length;k++)
                    if(res[i].idcod__cod==lotto[k].idcod__cod){
                        t+=lotto[k].cassa-lotto[k].cassaexit;
                        ctr=1;
                    }
                if(ctr==1){
                    if(t>res[i].cassa)
                        obj1['css']=res[i].cassa;
                    else{
                        obj1['css']=t;
                        obj1['diff']=t-res[i].cassa
                    }
                }
                else
                    obj1['css'] =res[i].cassa;
                ctr=0
                obj1['lotto'] =lt;
                obj1['cln'] =$("#cliente").val();
                obj1['cod'] =res[i].idcod__cod;
                obj1['ps'] =res[i].q;
                obj1['prz'] =res[i].prezzo;
                obj1['tara']=res[i].tara;
                obj1["iva"]=res[i].idcod__genere__iva
                ar1.push(obj1);
            }
        Fill();
        $("#tbf").show("");
        });
};

function GetLotto(){
   $.post(
        "fattura",
        {azione:"l"},
        function(res1){
            sos=res1["sp"];
            lotto=res1["cr"];
        });
            return;
};

//function SelLotto(cod){
    //var option=" ";
    //var cassat=0,cassat1=0;
    //sum=0;
    //for (k=0;k<sos.length;k++)
        //if(sos[k].idcod__cod==cod){
            //cassat=sos[k].css_sum;
            //cassat1=cassat;
            //$("#btltsos").show();
            //f=1;
            //break;
        //}
    //for (var i=0;i<lotto.length;i++){
        //if(lotto[i].idcod__cod==cod){
            //cassa=lotto[i].cassa-lotto[i].cassaexit;
            //if(cassat>0){
                //if(cassat>=cassa){
                    //cassat=cassat-cassa;
                    //cassa=0;
                //}
                //else{
                    //cassa=cassa-cassat;
                    //cassat=0
                //}
            //}
            //sum=sum+lotto[i].cassa-lotto[i].cassaexit
            //option += '<option value='+ lotto[i].id+ '>' + lotto[i].bolla+ " : " +cassa + '</option>';
        //}
    //}
        //sum=sum-cassat1
    //$('#lotto').html(option);
    //};

//function SelLottoSos(cod){
    //var option=" ";
    //sum=0;
    //f=0;
    //for (var i=0;i<lotto.length;i++)
        //if(lotto[i].idcod__cod==cod){
            //cassa=lotto[i].cassa-lotto[i].cassaexit;
            //sum=sum+lotto[i].cassa-lotto[i].cassaexit
            //option += '<option value='+ lotto[i].id+ '>' + lotto[i].bolla+ " : " +cassa+ '</option>';
        //}
    //$('#lotto').html(option);
    //};
    
    
    