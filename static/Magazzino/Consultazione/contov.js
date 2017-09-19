var UserTable=$("#mytable");
var TempUserTable=null;
var x=0;

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#azienda").click(function(){
        $("#tbf1").show();
        GetBolla();
    });
});

function GetBolla(){
    $.post(
        "cvc",
        {cln:$("#azienda option:selected").text(),azione:"B"},
        function(res){
            //res=[]
            //res=JSON.parse(rec);
            var before="";
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                if( res[i].bolla!=before)
                    label=label + '<td><input type="checkbox" value='+res[i].bolla+'></td>';
                else
                    label=label + '<td></td>';
                label=label + '<td>' +res[i].bolla+ '</td>';
                label=label + '<td>' + res[i].idcod__cod+ '</td>';
                label=label + '<td>' + res[i].q+ '</td>';
                label=label + '<td>' + res[i].cassa + '</td>';
                label=label + '<td>' + res[i].data+ '</td>';
                label=label + '<td>' +res[i].costo+ '</td>';
                label=label + '</tr>';
                before=res[i].bolla;
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




