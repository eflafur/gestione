var x=0;

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#tbf2").hide();

    $("#clientes").click(function(){
        $("#btddt").hide();
        $("#tbf1").hide();
        $("#tbf2").hide();
        GetTable($("#clientes option:selected").val());
    });
    
   $("#btddt").click(function(){
        $("#tbf1").hide();
        GetDdt()
        $("#btddt").hide();
//        $("#tbf2").hide();
    });
});

function GetTable(cl){
    $.post(
        "ddt",
        {cliente:cl,action:"tbl"},
        function(res){
        if(res.length==0)
            return;
        $("#btddt").show();
        $("#tbf1").show();
        var label="";
        for (i=0;i<res.length;i++){
           label=label + '<tr>';
           label=label + '<td><input type="checkbox" value='+res[i].ddt+'></td>';
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
    var ar=[];
    $("#tbf1 :checked").each(function(index){
        x=index+1;
        ar[x]=$(this).val();
    });

    if(x==0){
        $("input:checkbox:not(:checked)").each(function(index){
            x=index
            ar[x]=$(this).val();
        });
    }
    var t=JSON.stringify(ar);
    x=0;
    $.post(
        "ddt",
        {ddt:JSON.stringify(ar),action:"ddt",cln:$("#clientes option:selected").val()},
        function(res){
//            imp=res[i]["ps"]*res[i]["prz"]*(parseFloat(res[i]["iva"])+1);
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                label=label + '<td>'+res[i]["ddt"]+'</td>';
                label=label + '<td>' + res[i]["cod"] + '</td>';
                label=label + '<td>' + res[i]["ps"] + '</td>';
                label=label + '<td>' + res[i]["css"] + '</td>';
                label=label + '<td>' + res[i]["prz"] + '</td>';
                label=label + '<td>' + res[i]["iva"]+ '</td>';
//                label=label + '<td>' + imp + '</td>';
                label=label + '<td>' + res[i]["data"] + '</td>';
                label=label + '<td>' + res[i]["lotto"] + '</td>';
                label=label + '</tr>';
            }
            $("#tb7").html(label);
            $("#tbf2").show();
        });
};


