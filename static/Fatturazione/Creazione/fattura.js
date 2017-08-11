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
        Invia(ar1);
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
            obj['cln'] =$("#cliente").val();
            obj['cod'] =$("#codice").val();
            obj['ps'] =$("#peso").val();
            obj['prz'] =$("#prezzo").val();
            ar1.push(obj);
            //i=1+i;
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
        return;
    });

    $('#tbfb').on('click','a',function(){
        var arr= [];
        arr=$(this).text().split('-');   
        if(arr[1]=='E')
            DeleteRow(arr[0]);
        else if(arr[1]=='A')
            AddRow(arr[0]);
    });
    return;
});

function Fill(res){
    var label="";
    var k=0;
    for (i = 0; i < res.length; i++) {
        k=i+1;
        label = label + '<tr>';
        label = label + '<td>' + res[i].cod+ '</td>';
        label = label + '<td>' + res[i].ps+ '</td>';
        label = label + '<td>' + res[i].prz+ '</td>';
        label = label + '<td> <a href="#" value="ded" ><p>'+k+'-A'+'</p></a></td>';
        label = label + '<td> <a href="#" value="ded" ><p>'+k+'-E'+'</p></a></td>';
        label = label + '</tr>';
    }
    $("#tbfb").html(label);  
    return;
};



function Invia(ar){
    $.post(
        "fattura",
      {res:JSON.stringify(ar1),azione:"invio"},
        //{
            //json_data: JSON.stringify(ar1),
            //"type": 'clone',
    //  "csrfmiddlewaretoken": $csrf_token
        //},  
    function (result){

    });
    return;
};


function DeleteRow(row){
    ar1.splice(row-1,1);
    Fill(ar1);
};

function AddRow(row){
    t=ar1[row-1].cod;
//    $("#codice option[value=t").prop("selected", true);
    $("#codice").val(t);
    $("#ps").show();
};