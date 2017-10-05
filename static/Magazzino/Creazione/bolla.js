var ar1= [];
var i=0;
var pvl=$("#psps").text();
var dt1="";   
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    if(pvl!=""){
        $("#cln").show();
        $("#cliente").attr('disabled',true);
        $("#bolla").attr('disabled',true);
        $("#bolla").val(pvl);
        GetCod();
    }
    else
        $("#dtft").hide();
        $("#cln").hide();
        $("#css").hide();
        $("#bl").keypress(function(){
            $("#cln").show();
        });
    
    $("#cliente").click(function(){
        $("#cliente").attr("disabled",false);
        GetCod();
        $("#dtft").show();
        $("#peso").val("");
        $("#ps").hide();
        $("#css").hide();
        $("#prz").hide();
    });
    
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01", 
     onSelect: function (date) {
         dt1=date;
         $("#cod").show();
         $("#codice").focus();
         $("#btt").show(); 
         $("#pf").hide();
      }
    });
    
     $("#codice").click(function(){
        $("#ps").show();
        $("#peso").focus();
    });
    
    $("#peso").keypress(function(){
        $("#css").show();
    });
    
    $("#cassa").keypress(function(){
        $("#btadd").show();
    });
    
 
    
    $("#btems").click(function(){
        Invia('I');
        if(pvl!="")
            window.location.replace("lktotale");
        ar1.length=0
        $("#tbf").hide("");
        $("#cliente").attr('disabled',false);
        $("#bolla").attr('disabled',false);
        $("#bolla").focus();
        $("#bolla").val(" ");
        $("#cod").hide("");
        $("#cln").hide("");
        $("#ps").hide();
        ("#css").hide();
        $("#btadd").hide();
        $("#dtft").hide();
        $("#dtft").hide();
        if(pvl)
            window.location.replace("lktotale");
    });
    
    $("#btanl").click(function(){
        ar1.length=0
        if(pvl)
            window.location.replace("base");
        $("#tbf").hide("");
        $("#cliente").attr('disabled',false);
        $("#cliente").focus();
        $("#cod").hide("");
        $("#ps").hide();
        ("#css").hide();
        $("#btadd").hide();
        $("#dtft").show();
    });
    
    $("#btadd").click(function(){
        a=$("#peso").val();
        b=$("#cassa").val();
        if(a==""){
            alert ("inserire peso")
            $("#peso").focus()
        }
        if(b==""){
            alert ("inserire Num. casse")
            $("#cassa").focus()
        }
        else {
            var obj={}
            obj['cod'] =$("#codice option:selected").text();
            obj['ps'] =$("#peso").val();
            obj['css'] =$("#cassa").val();
            obj["id"]=$("#codice option:selected").val();
            ar1.push(obj);
            Fill();
            $("#tbf").show("");
            $("#peso").val("");
            $("#ps").hide();
            $("#cassa").val("");
            $("#css").hide();
            $("#btadd").hide();
            $("#cod").focus();
            $("#cliente").attr('disabled',true);
            $("#bolla").attr('disabled',true);
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

function GetCod(){
    var cl=$("#cliente option:selected").val();
    var str = ($("#bolla").val()).replace(/\s/g, '');
    $.post(
        "entrata",
        {cliente:cl,bolla:str,azione:"gid",dod:pvl},
        function(res){
          if(typeof res.a!='undefined')
            GetCodId(res);
        else
            GetCodT(res);
    });
};

function GetCodId(res){
    label=" ";
    for (i=0;i<res.a.length;i++){
        label=label +'<option value='+res.a[i].id+'>'+res.a[i].cod+'</option>';
    }
    $("#dtft").hide();
    $("#codice").html(label);
    label=" "
    for (i=0;i<res.b.length;i++){
        var obj1={}  
        obj1["id"]=res.b[i].idcod__id
        obj1['cod'] =res.b[i].idcod__cod;
        obj1['ps'] =res.b[i].q;
        obj1['css'] =res.b[i].cassa;
        ar1.push(obj1);
    }
    Fill();
    $("#cod").show("");
    $("#tbf").show("");
    return;
 };


function GetCodT(res){
    label=" ";
    for (i=0;i<res.length;i++){
        label=label +'<option value='+res[i].id+' >'+res[i].cod+'</option>';
    }
    $("#codice").html(label);
    return;
};

function Fill(){
    var label="";
    var k=0;
    for (i = 0; i < ar1.length; i++) {
        k=k+1
        label = label + '<tr>';
        label = label + '<td>' + ar1[i].cod+ '</td>';
        label = label + '<td>' + ar1[i].ps+ '</td>';
        label = label + '<td>' + ar1[i].css+ '</td>';
        label = label + '<td> <a href="#" ><p>'+k+'-A'+'</p></a></td>';
        label = label + '<td> <a href="#" ><p>'+k+'-E'+'</p></a></td>';
        label = label + '</tr>';
    }
    $("#tbfb").html(label);
    return;
};

function Invia(act){
    str = ($("#bolla").val()).replace(/\s/g, '');
    $.post(
        "entrata",
        {res:JSON.stringify(ar1),bolla:str,azione:act,dt:dt1},
        function(res){
        });
    return;
};

function DeleteRow(row){
    ar1.splice(row-1,1);
    Fill();
    return
};

function AddRow(row){
    t=ar1[row-1].cod;
    DeleteRow(row)
     $("#codice option:contains("+t+")").prop('selected', true)
//    $("#codice option:selected").text(t);
    $("#ps").show();
};


