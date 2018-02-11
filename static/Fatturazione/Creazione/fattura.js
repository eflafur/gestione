var ar1= [];
var sum;
var sumf;
var i=0;
var cliente;
var pvl=$("#psps").text();
var tipo=pvl.substr(0,2)
var lotto=[];    
var sos=[];    
var lt="";
var f;
var dtl="";
var choice="";
var n=0;
var codls=[]
var lt0;
var trl=[];
var fatres=[];

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    lotto.length=0;
    $("#brand").text("Nuova Fattura");
    Eval();
    if(tipo=="dd" ){
        $("#cliente").attr('disabled',true);
        $("#pagam").attr('disabled',false);
        $("#codice").attr('disabled',true);
        n=1
        GetSospesa();
    }  
    else if(tipo=="sc" ){
        $("#pgm").show();
        $("#cliente").attr('disabled',true);
        $("#cod").show();
        $("#codice").attr("disabled",true);
    } 
    $("#cliente").click(function(){
        ar1.length=0
        Eval();
        GetLotto();
        $("#pagam").attr('disabled',false);
        $("#cod").show();
    });

    $("#tara1").click(function(){
        $("#ps").show();
    });
    $("#desc").click(function(){
        $("#lt").show();
        $("#tr").show();
    });
    $(".pr").click(function(){
        $("#ps").show();
    });

    $("#pagam").click(function(){
        if (tipo=="sc"){
            if($(this).val()==0)
                $("#chc").show();
            n=1;
            GetSospesaSos();
            $("#btemit").show();
            $("#codice").attr("disabled",false);
            return false;
        }
        if($(this).val()==0){
//            $("#btadd").hide();
            $("#chc").show();
            $(".tot").attr("readonly",false);
        }
        else{
            $("#chc").hide();
            $(".tot").attr("readonly",true);
     //       $("#btadd").show();
        }
//        if($(this).val()==0 && ar1.length==0 && n==1)
       //     $("#btadd").hide();
        if(n==1)
            return false;
    });
    
    $("#chc").click(function(){
        choice=$("#chc :checked").val();
        if (tipo=="sc")
            return;
      //  $("#btadd").show();
    });

     $("#btltsos").click(function(){
        if(f==0)
            SelLotto(codls[1]);
        else
            SelLottoSos(codls[1]);
    });
    
     $("#codice").click(function(){
        var cod=$("#codice option:selected").text();
        codls.length=0;
        $("#tara1").val("");
        codls=$("#codice option:selected").val().split(" ");
        for(i=0;i<ar1.length;i++)
            if (codls[1]==ar1[i].id){
                alert(""+ar1[i].cod+ " già presente")
                $("#btadd").hide();
                return false;
            }
        Eval();
        ret=SelLotto(codls[1]);
        if(ret!=0){
            $("#dsc").show();
            $("#desc").focus();
//            $("#lt").show();
        }
    else{
        alert("LOTTI NON DISPONIBILI");
        //Eval();
        if(n>0){
            Fill();
            $("#btemit").show();
        }
    }
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
       // if(n==1)
            $("#btadd").show();
        $("#pgm").show();
    });
    
    $("#btsps").click(function(){
        Invia('S');
        if(pvl!="")
            window.location.replace("sospesa");
    });
    
    $("#btems").click(function(){
        Invia('I');
    });
    
    $("#ddtft").click(function(){
        if(tipo=="dd")
            Invia('R')
        else
            Invia('D');
    });
    
    $("#btanl").click(function(){
        ar1.length=0
        if(pvl!="")
            window.location.replace("sospesa");
         n=0   
         Eval();
    });
    
    $("#tara1").on("input",function(e){
      dtl=parseFloat($(this).val()).toFixed(2);  
    });
    
    $("#btadd").click(function(){
        var obj={}
        n=1;
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
            if((isNaN(dtl) || dtl=="") && (trl[3]=="na" || isNaN(trl[3]))){
                alert("Specificare la tara");
                $("#tara1").focus();
                return false;
            }
            if(trl[3]!="na" && (isNaN(dtl) || dtl=="" ))
                dtl=trl[3]
        
            if(parseFloat($("#cassa").val()) % 1 !=0){
                alert(" Valore Colli non valido")
                $("#btemit").hide();
                $("#cassa").focus();
                return false;
            }

            if(dtl>=1){
                alert(" Valore Tara non valido")
                $("#btemit").hide();
                $("#tara1").focus();
                return false;
            }
            obj['diff']=0;
            obj['cln'] =$("#cliente").val();
            obj['cod'] =$("#codice option:selected").text();
            obj['id'] =codls[1];
            obj['ps'] =$("#peso").val();
            obj['css'] =$("#cassa").val();
            obj['prz'] =parseFloat($("#prezzo").val()).toFixed(2);
            obj["iva"]=parseFloat(codls[0]).toFixed(2);
            obj['tara']=dtl;
            obj['lotto']=lt;
            ar1.push(obj);
            lt="";
            Fill();
//            if((tipo!="dd"))
                //$("#codice").attr('disabled',false);
            $("#btadd").hide();
        }
        dtl="";
        trl.length=0;
        //if(tipo=="dd"){
            //$("#ddtft").show();
            //$("#btanl").show();
            //return;
            //}
        $("#btemit").show();
        return;
    });

    $("#lotto").on('click',function(){
        trl=($("#lotto option:selected").text()).split(":");
        lt=$("#lotto option:selected").val();
        if(isNaN(lt))
            lt="";
        $("#ps").show();
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
    $("#btltsos").hide();
    $("#chc").hide();
    $("#tr").hide();
    $("#btemit").hide();
    $("#tbf").hide("");
    $("#cliente").attr('disabled',false);
    $("#cliente").focus();
    $("#ps").hide();
    $("#css").hide();
    $("#prz").hide();  
    $("#btadd").hide();
    $("#dsc").hide();
    $("#pgm").hide();
    $("#lt").hide();
    $("#peso").val("");
    $("#prezzo").val("");
    $("#cassa").val("");
    $("#tara1").val("");
    //if(ar1.length==0 && n==1)
        //$("#cod").hide();
};

function Fill(){
    var label="";
    var k=0;
    var imp=0;
    sumf=0;
    for (i = 0; i < ar1.length; i++) {
        k=k+1
        imp=ar1[i].prz*(ar1[i].ps-ar1[i].css*ar1[i].tara)*(parseFloat(ar1[i].iva)+1)
        sumf+=imp;
        label = label + '<tr>';
        label = label + '<td>' + ar1[i].cod+ '</td>';
        label = label + '<td>' + ar1[i].ps+ '</td>';
        label = label + '<td>' + ar1[i].tara+ '</td>';
        label = label + '<td>' + ar1[i].css+ '</td>';
        label = label + '<td>' + ar1[i].iva+ '</td>';
        label = label + '<td>' + ar1[i].prz+ '</td>';
        label = label + '<td>' + imp.toFixed(2)+ '</td>';
        if(pvl=="" || tipo=="sc"){
            label = label + '<td> <a href="#" ><p>'+k+'-E'+'</p></a></td>';
            label = label + '<td> <a href="#" ><p>'+k+'-A'+'</p></a></td>';
        }
        else
            label = label + '<td> <a href="#" ><p>'+k+'-A'+'</p></a></td>';
        label = label + '<td>' + ar1[i].diff+ '</td>';
        label = label + '</tr>';
    }
    pagam=$("#pagam option:selected").val();
    if(pagam==0)
        label=label + '<tr><td>TOT</td><td></td><td></td><td></td><td></td><td>  <input class="tot" type=number value='+sumf.toFixed(2)+'></input></td></tr>';
    else
        label=label + '<tr><td>TOT</td><td></td><td></td><td></td><td></td><td>  <input class="tot" type=number value='+sumf.toFixed(2)+' readonly></input></td></tr>';
    $("#tbf").show("");
    $("#tbfb").html(label);
    $("#tbfb tr:last").find("td:last").css("color","blue");
    return;
};

function Invia(act){
//$(".tot").trigger(function(e){
//});
    var t=parseFloat($(".tot").val());
    var pg=$("#pagam").val();
    if(pg>0)
        t=0;
    else if(sumf>t)
        pg=1
        
    $.post(
        "fattura",
      {res:JSON.stringify(ar1),azione:act,item:pvl,pgm:pg,tot:t,chc:choice,cln:$("#cliente").val()},
    function (result){
    });
    ar1.length=0
    lotto.length=0;
    $("#cod").hide();
    n=0;
    Eval();
    return;  
};

function DeleteRow(row){
    ar1.splice(row-1,1);
    Fill();
};
function AddRow(row){
    t=ar1[row-1].cod;
    lt=ar1[row-1].lotto;
    $("#ps").show();
    $("#codice").attr('disabled',true);
    $("#codice option:contains("+t+")").prop('selected', true)
    codls=$("#codice option:selected").val().split(" ");
    if((tipo=="dd")){
       sum=ar1[row-1].css
        $("#pagam").attr('disabled',true);
        $("#lt").show();
        SelLottoDDT(codls[1]);
    }
    else   
       SelLottoSos(t);
    DeleteRow(row)
};

function GetSospesa(){
    $.post(
        "fattura",
        {item:pvl,azione:"reazione"},
        function(ret){
        var option="";
            fatres=ret["doc"];
            for (i=0;i<fatres.length;i++){
                var obj1={}  
                obj1['diff']=0
                obj1['cln'] =$("#cliente").val();
                obj1['cod'] =fatres[i].idcod__cod;
                obj1['id'] =fatres[i].idcod__id;
                obj1['ps'] =fatres[i].q;
                obj1['prz'] =fatres[i].prezzo;
                obj1['css'] =fatres[i].cassa;
                obj1['lotto']=fatres[i].lotto;
                obj1['tara']=fatres[i].tara;
                obj1["iva"]=parseFloat(fatres[i].idcod__genere__iva)
                ar1.push(obj1);
            }
        //for (i=0;i<fatres.length;i++){
            //option += '<option value='+ fatres[i].lotto+ '> Lotto:'+ fatres[i].lotto+ " -Casse:" +fatres[i].cassa+" - Tara:"+fatres[i].tara+ '</option>';
        //}
        Fill();
//        $('#lotto').html(option);
        $("#cod").show("");
        $("#tbf").show("");
        });
};

function GetSospesaSos(){
    $.post(
        "fattura",
        {item:pvl,azione:"reazione"},
        function(ret){
            var psos=0;
            var res=ret["doc"];
            lotto=ret["cr"];
            var t=0;
            var ctr=0;
            $("#pagam").attr('disabled',true);
            for (i=0;i<res.length;i++){
                var obj1={}  
                t=0
                obj1['diff']=0
                for (k=0;k<lotto.length;k++)
                    if(res[i].idcod__id==lotto[k].idcod__id){
                        t+=lotto[k].cassa-lotto[k].cassaexit;
                        lt=lotto[k].id
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
                psos=parseFloat(obj1['css'])*res[i].q/res[i].cassa
                obj1['lotto'] =lt;
                obj1['cln'] =$("#cliente").val();
                obj1['cod'] =res[i].idcod__cod;
                obj1['id'] =res[i].idcod__id;
                obj1['ps'] =psos;;
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

function SelLotto(cod){
    var option=" ";
    var cassat=0,cassat1=0;
    var islotto=0;
    lt="";
    sum=0;
    for (k=0;k<sos.length;k++)
        if(sos[k].idcod__id==cod){
            cassat=sos[k].css_sum;
            cassat1=cassat;
            $("#btltsos").show();
            f=1;
        }
    for (var i=0;i<lotto.length;i++){
        if(lotto[i].idcod__id==cod){
            islotto=1;
            cassa=lotto[i].cassa-lotto[i].cassaexit;
            if(cassat>0){
                if(cassat>=cassa){
                    cassat=cassat-cassa;
                    cassa=0;
                }
                else{
                    cassa=cassa-cassat;
                    cassat=0
                }
            }
            sum=sum+lotto[i].cassa-lotto[i].cassaexit
            if(lt=="")
                lt=lotto[i].id
            if(parseFloat(lotto[i].tara)==-1)
                lotto[i].tara="na"
            option += '<option value='+ lotto[i].id+ '> Lotto:'+ lotto[i].bolla+ " -Casse:" +cassa +" - Tara:"+lotto[i].tara + '</option>';
        }
    }
    sum=sum-cassat1
    $('#lotto').html(option);
    return islotto;
    };
    
function SelLottoDDT(cod){
    var option;
    for (var i=0;i<fatres.length;i++)
        if(fatres[i].idcod__id==cod)
            option += '<option value='+ fatres[i].lotto+ '> Lotto:'+ fatres[i].lotto+ " -Casse:" +fatres[i].cassa+" - Tara:"+fatres[i].tara+ '</option>';
 //       break;
    $('#lotto').html(option);
};   

function SelLottoSos(cod){
    var option=" ";
    sum=0;
    f=0;
    for (var i=0;i<lotto.length;i++)
        if(lotto[i].idcod__id==cod){
            cassa=lotto[i].cassa-lotto[i].cassaexit;
            sum=sum+lotto[i].cassa-lotto[i].cassaexit
            option += '<option value='+ lotto[i].id+ '>' + lotto[i].bolla+ " : " +cassa+ '</option>';
        }
    $('#lotto').html(option);
    };
    