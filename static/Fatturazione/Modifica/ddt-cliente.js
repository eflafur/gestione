var x=0;

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#tbf2").hide();

    $("#clientes").click(function(){
        $("#tbf2").hide();
        GetTable($("#clientes").val());
                $("#tbf1").show();
    });
    
   $("#btddt").click(function(){
        $("#tbf1").hide();
        $("#tbf2").show();
//        $("#tb7").show();
        GetDdt()
    });
});

function GetTable(cl){
    $.post(
        "ddt",
        {cliente:cl,action:"tbl"},
        function(res){
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
        x=index;
        ar[x]=$(this).val();
    });

    if(x==0){
        $("input:checkbox:not(:checked)").each(function(index){
            x=index
            ar[x]=$(this).val();
        });
    }
    $.post(
        "ddt",
        {ddt:JSON.stringify(ar),action:"ddt"},
        function(ret){
            var label="";
            var res=[]
            res=JSON.parse(ret);
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                label=label + '<td>'+res[i].ddt+'</td>';
                label=label + '<td>' + res[i].q + '</td>';
                label=label + '<td>' + res[i].cassa + '</td>';
                label=label + '<td>' + res[i].prezzo + '</td>';
                label=label + '<td>' + res[i].iva+ '</td>';
                label=label + '<td>' + res[i].data + '</td>';
                label=label + '<td>' + res[i].lotto + '</td>';
                label=label + '</tr>';
            }
            $("#tb7").html(label);  
        });
};

