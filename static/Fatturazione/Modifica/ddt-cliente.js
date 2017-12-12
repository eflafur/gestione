var x=0;
var sum=0;
var ar=[];
var choice="";
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#tt").hide();
    $("#tbf2").hide();
    $("#pgm").hide();
    $("#btsel").hide();
    $("#chc").hide();
    
    $("#clientes").click(function(){
        ar.length=0;
        $("#tt").hide();
        $("#btsel").hide();
        $("#btddt").hide();
        $("#tbf1").hide();
        $("#tbf2").hide();
        $("#pgm").show();
        GetTable($("#clientes option:selected").val());
    });
   $("#pagam").click(function(){
        $("#btsel").show();
    });
    
    $("#chc").click(function(){
        choice=$("#chc :checked").val();
        $("#btsel").show();
        $("#btddt").show();
    });
    
   $("#btsel").click(function(){
        if($("#pagam").val()==0)
            $("#chc").show();
        else
            $("#btddt").show();
        $("#tt").show();
        $("#tot").attr("readonly",false);
        GetDdt();
    });

   $("#btddt").click(function(){
        SendDdt()
        $("#pgm").hide();
        $("#tbddt").hide();
        $("#tbsel").hide();
    });
});

function GetTable(cl){
    $.post(
        "ddt",
        {cliente:cl,action:"tbl"},
        function(res){
        if(res.length==0)
            return;
        $("#tbf1").show();
        var label="";
        for (i=0;i<res.length;i++){
           label=label + '<tr>';
           label=label + '<td><input type="checkbox" class="chc" value='+res[i].ddt+'></td>';
           label=label + '<td>' + res[i].ddt + '</td>';
           label=label + '<td>' + res[i].cliente__azienda + '</td>';
           label=label + '<td>' + res[i].valore+ '</td>';
           label=label + '<td>' +res[i].data + '</td>';
           label=label + '</tr>';
           before=res[i].ddt;
       }
       $("#tb6").html(label);
    });
   return
};


function GetDdt(){
    var t=0;
    var xx=0;
    sum=0;
    $("#tbf1 :checked").each(function(index){
        xx=index+1;
        ar[index]=$(this).val();
    });
    if(xx>0){
        $("#tb6 tr").each(function(){
             r=$(this).find("td:eq(1)").text();
             for (i=0;i<ar.length;i++){
                 if(r==ar[i]){
                     sum+=parseFloat($(this).find("td:eq(3)").text());
                     t=1
                     break;
                 }
                 continue;
             }
            if(t==0)
                 $(this).remove();
             t=0;
         });
    } 
    else {
        $("#tb6 tr").each(function(){
            ar.push($(this).find("td:eq(1)").text());
            sum+=parseFloat($(this).find("td:eq(3)").text());
         });
    }
    $("#tot").val(sum);
    if($("#pagam").val()!=0)
        $("#tot").attr("readonly",true);
 };


function SendDdt(){
    var t=parseFloat($("#tot").val());
    var pg=$("#pagam").val();
    if(pg>0)
        t=0;
    else if(t.toFixed(2)>sum.toFixed(2) || t<0){
        alert ("valore inammissibile")
        return 1;
    }
    else if(t<sum.toFixed(2))
        pg=1
    $.post(
        "ddt",
        {ddt:JSON.stringify(ar),action:"ddt",cln:$("#clientes option:selected").val(),pgm:pg,tot:t,chc:choice},
        function(res){
            //var label="";
            //for (i=0;i<res.length;i++){
                //imp=parseFloat(res[i]["q"])*parseFloat(res[i]["prz"])*(parseFloat(res[i]["iva"])+1);
                //label=label + '<tr>';
                //label=label + '<td>'+res[i]["ddt"]+'</td>';
                //label=label + '<td>' + res[i]["cod"] + '</td>';
                //label=label + '<td>' + res[i]["q"] + '</td>';
                //label=label + '<td>' + res[i]["css"] + '</td>';
                //label=label + '<td>' + res[i]["prz"] + '</td>';
                //label=label + '<td>' + res[i]["iva"]+ '</td>';
                //label=label + '<td>' + imp + '</td>';
                //label=label + '<td>' + res[i]["data"] + '</td>';
                //label=label + '<td>' + res[i]["lotto"] + '</td>';
                //label=label + '</tr>';
            //}
            //$("#tb7").html(label);
            //$("#tbf2").show();
        });
};
