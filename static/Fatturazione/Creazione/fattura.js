var ar1= [];
var ar2= [];
var ar3= [];
var i=0;
var cliente;

$(document).ready(function(){
    $.ajaxSetup({cache:false});
 //   cliente=$("#cliente option:selected").text();
      // ln=$("#cliente option").length;
      //$("p:contains('sos')").css("color", "blue");
    pvl=$("#psps").text();
    if(pvl!=" "){
        GetSospesa(pvl);
    }  
    
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
     //   $("#cliente option:selected").html(cliente);
        Invia('S');
        ar1.length=0
        $("#tbf").hide("");
        $("#cliente").attr('disabled',false);
        $("#cliente").focus();
        $("#cod").hide();
        $("#ps").hide();
        $("#prz").hide();
        $("#btadd").hide();

    });
    
    $("#btems").click(function(){
     //   $("#cliente option:selected").html(cliente);
        Invia('I');
        ar1.length=0
        $("#tbf").hide("");
        $("#cliente").attr('disabled',false);
        $("#cliente").focus();
        $("#cod").hide("");
        $("#ps").hide();
        $("#prz").hide();  
        $("#btadd").hide();
    });
    
    $("#btanl").click(function(){
        //$("#cliente option:selected").html(cliente);
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
            obj['cod'] =$("#codice option:selected").text();
            obj['ps'] =$("#peso").val();
            obj['prz'] =$("#prezzo").val();
            obj["iva"]=parseFloat($("#codice option:selected").val())+1;
            ar1.push(obj);
            Fill("f");
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


function Fill(crt){
    var label="";
    var k=0;
    var sum=0;
    for (i = 0; i < ar1.length; i++) {
        k=k+1
        sum=sum+ar1[i].prz*ar1[i].ps*ar1[i].iva;
        label = label + '<tr>';
        label = label + '<td>' + ar1[i].cod+ '</td>';
        label = label + '<td>' + ar1[i].ps+ '</td>';
        label = label + '<td>' + ar1[i].prz+ '</td>';
        label = label + '<td> <a href="#" ><p>'+k+'-A'+'</p></a></td>';
        label = label + '<td> <a href="#" ><p>'+k+'-E'+'</p></a></td>';
        label = label + '</tr>';
    }
    label=label + '<tr><td>TOT</td><td></td><td>'+sum+ '</td></tr>';
    $("#tbfb").html(label);
    $("#tbfb tr:last").find("td:last").css("color","blue");
    return;
};

function Invia(azione){
    if (azione=="I")
        act="invio";
    else if (azione=="S")
        act="sospesa";
    $.post(
        "fattura",
      {res:JSON.stringify(ar1),azione:act},
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
    $("#codice option:selected").text(t);
    //$("#codice option[value=t").prop("selected", true);
  //  $("#codice").html(t);
    $("#ps").show();
};

function GetSospesa(pvl){
    $.post(
        "fattura",
        {item:pvl,azione:"reazione"},
        function(res){

            for (i=0;i<res.length;i++){
                var obj1={}  
                obj1['cod'] =res[i].idcod__cod;
                obj1['ps'] =res[i].q;
                obj1['prz'] =res[i].prezzo;
                obj1["iva"]=parseFloat(res[i].idcod__genere__iva)+1
                ar1.push(obj1);
            }
        Fill("s");
        $("#cod").show("");
        $("#tbf").show("");
        });
};