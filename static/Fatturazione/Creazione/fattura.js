var ar1= [];
var sum;
var i=0;
var cliente;
var pvl=$("#psps").text();
var lotto=[];    
var lt="";
$(document).ready(function(){
    $.ajaxSetup({cache:false});
 //   cliente=$("#cliente option:selected").text();
      // ln=$("#cliente option").length;
      //$("p:contains('sos')").css("color", "blue");
    $("#css").hide();
    $("#dsc").hide();
    $("#pgm").hide();
    $("#cod").hide();
    $("#lt").hide();

    if(pvl!=""){
        $("#cliente").attr('disabled',true);
        $("#cod").hide();
        $("#dsc").show();
        $("#desc").focus();
        GetLotto();
        GetSospesa();
    }  

    $("#cliente").click(function(){
        GetLotto();
        $("#dsc").show();
        $("#desc").focus();
        $("#peso").val("");
        $("#prezzo").val("");
        $("#ps").hide();
        $("#css").hide();
        $("#prz").hide();
    });

    $("#dsc").click(function(){
        $("#pgm").show();
    });

    $("#pagam").click(function(){
        $("#cod").show();
    });
    
     $("#codice").click(function(){
        var cod=$("#codice option:selected").text();
        SelLotto(cod);
        $("#ps").show();
        $("#peso").focus();
        $("#peso").val("");
        $("#prezzo").val("");
        $("#css").hide();
        $("#cassa").val("");
        $("#prz").hide();
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
            $("#btadd").show();
    });
    
    $("#btsps").click(function(){
        Invia('S');
        ar1.length=0
        if(pvl!="")
            window.location.replace("sospesa");
        $("#tbf").hide("");
        $("#cliente").attr('disabled',false);
        $("#cliente").focus();
        $("#cod").hide();
        $("#css").hide();
        $("#ps").hide();
        $("#prz").hide();
        $("#btadd").hide();
        $("#dsc").hide();
        $("#pgm").hide();
        $("#lt").hide();
    });
    
    $("#btems").click(function(){
        Invia('I');
        ar1.length=0
        //if(pvl!="")
            //window.location.replace("sospesa");
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
    });
    
      $("#ddtft").click(function(){
        Invia('D');
        ar1.length=0
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
    });
    
    $("#btanl").click(function(){
        ar1.length=0
        if(pvl!="")
            window.location.replace("sospesa");
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
            obj['cln'] =$("#cliente").val();
            obj['cod'] =$("#codice option:selected").text();
            obj['ps'] =$("#peso").val();
            obj['css'] =$("#cassa").val();
            obj['prz'] =$("#prezzo").val();
            obj["iva"]=$("#codice option:selected").val();
            obj['lotto']=lt;
            ar1.push(obj);
            lt=""
            Fill();
            $("#tbf").show("");
            $("#peso").val("");
            $("#cassa").val("");
            $("#prezzo").val("");
            $("#ps").hide();
            $("#css").hide();
            $("#prz").hide();
            $("#btadd").hide();
            $("#cod").focus();
            $("#cliente").attr('disabled',true);
            $("#lt").hide();
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
    });
    return;
});


function Fill(){
    var label="";
    var k=0;
    var sum=0;
    for (i = 0; i < ar1.length; i++) {
        k=k+1
        imp=ar1[i].prz*ar1[i].ps*(parseFloat(ar1[i].iva)+1)
        sum=sum+ar1[i].prz*ar1[i].ps*(parseFloat(ar1[i].iva)+1);
        label = label + '<tr>';
        label = label + '<td>' + ar1[i].cod+ '</td>';
        label = label + '<td>' + ar1[i].ps+ '</td>';
        label = label + '<td>' + ar1[i].css+ '</td>';
        label = label + '<td>' + ar1[i].iva+ '</td>';
        label = label + '<td>' + ar1[i].prz+ '</td>';
        label = label + '<td>' + imp+ '</td>';
        label = label + '<td> <a href="#" ><p>'+k+'-E'+'</p></a></td>';
        label = label + '</tr>';
    }
    label=label + '<tr><td>TOT</td><td></td><td></td><td></td><td></td><td>'+sum.toFixed(2)+ '</td></tr>';
    $("#tbfb").html(label);
    $("#tbfb tr:last").find("td:last").css("color","blue");
    return;
};

function Invia(act){
    $.post(
        "fattura",
      {res:JSON.stringify(ar1),azione:act,item:pvl},
    function (result){
        var label=""
        if(result.length!=0){ 
            for(i=0;i<result.length;i++)
                label=label+result[i].num+" eccedenze per articolo: "+ result[i].cod+'\n'
            alert(label)
        }
    });
    return;
};

function DeleteRow(row){
    ar1.splice(row-1,1);
    Fill();
};

function GetSospesa(){
    $.post(
        "fattura",
        {item:pvl,azione:"reazione"},
        function(res){
            for (i=0;i<res.length;i++){
                var obj1={}  
                obj1['cln'] =$("#cliente").val();
                obj1['cod'] =res[i].idcod__cod;
                obj1['ps'] =res[i].q;
                obj1['css'] =res[i].cassa;
                obj1['prz'] =res[i].prezzo;
                obj1['lotto'] =res[i].lotto;
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
        {azione:"L"},
        function(res){
            lotto=res;
        });
};

function SelLotto(cod){
    var option=" ";
    sum=0;
    for (var i=0;i<lotto.length;i++)
        if(lotto[i].idcod__cod==cod){
            sum=sum+lotto[i].cassa-lotto[i].cassaexit
            option += '<option value='+ lotto[i].id+ '>' + lotto[i].bolla+ " : " +lotto[i].cassa+ ":"+lotto[i].cassaexit + '</option>';
        }
    $('#lotto').html(option);
    };

