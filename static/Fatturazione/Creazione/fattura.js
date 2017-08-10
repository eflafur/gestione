var ar1= [];
var ar2= [];
var ar3= [];
var i=0;

$(document).ready(function(){
    $.ajaxSetup({cache:false});
   
    $("#cln").focus();
    
    $("#cliente").click(function(){
        $("#cod").show();
        $("#codice").focus();
        $("#peso").val("");
        $("#prezzo").val("");
    });
    
     $("#codice").click(function(){
        $("#ps").show();
        $("#peso").focus();
    });
    
    $("#peso").keypress(function(){
        $("#prz").show();
    });
    
    $("#prezzo").keypress(function(){
        $("#btadd").show();
    });
    
    $("#btsps").click(function(){
        Invia(ar1);
        $("#tbf").hide("");
        $("#cliente").attr('disabled',false);
        $("#cliente").focus();
        $("#cod").hide();
        $("#ps").hide();
        $("#prz").hide();
        $("#btadd").hide();
    });
    
    $("#btems").click(function(){
        $("#tbf").hide("");
        $("#cliente").attr('disabled',false);
        $("#cliente").focus();
        $("#cod").hide("");
        $("#ps").hide();
        $("#prz").hide();  
        $("#btadd").hide();
    });
    
       $("#btanl").click(function(){
        ar1.length=0
        Invia(ar1);
        $("#tbf").hide("");
        $("#cliente").attr('disabled',false);
        $("#cliente").focus();
        $("#cod").hide("");
        $("#ps").hide();
        $("#prz").hide();  
        $("#btadd").hide();
    });
    
     $("#btadd").click(function(){
        a=$("#peso").val();
        b=$("#prezzo").val();
        if(a==""){
            alert ("inserire peso")
            $("#peso").focus()
        }
        else if(b==""){
            alert ("inserire prezzo")
            $("#prezzo").focus()
        }
        

        else {
        //versione con array
            //ar1[i]=$("#codice").val();
            //ar2[i]=$("#peso").val();
            //ar3[i]=$("#prezzo").val();
            //i++;
            //Fill(ar1,ar2,ar3);
            var obj={}
            obj['cod'] =$("#codice").val();
            obj['ps'] =$("#peso").val();
            obj['prz'] =$("#prezzo").val();
            ar1[i]=obj;
            i=1+i;
            Fill(ar1);
            $("#tbf").show("");
            $("#peso").val("");
            $("#prezzo").val("");
            $("#ps").hide();
            $("#prz").hide();
            $("#btadd").hide();
            $("#cod").focus();
            $("#cliente").attr('disabled',true);
        }
        return
     });
});

function Fill(res){
    var label="";
    for (i = 0; i < res.length; i++) {
        label = label + '<tr>';
        label = label + '<td>' + res[i].cod+ '</td>';
        label = label + '<td>' + res[i].ps+ '</td>';
        label = label + '<td>' + res[i].prz+ '</td>';
        label = label + '</tr>';
    }
    $("#tb3").html(label);  
    return;
};

function Invia(ar){
    $.post(
        "fattura",
        {a2:ar},
    function (result){

    });
    return;
};
