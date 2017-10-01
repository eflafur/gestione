var UserTable=$("#mytable");
var TempUserTable=null;
var res="";

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#azienda").click(function(){
            $("#tbf1").hide();
            $("#cldt2").hide();
            $("#btddt").hide();
            $("#btmrg").hide();        
            GetBolla();
    });
    $("#btmrg").click(function(){
        Write();
//        alert("Reimposta la selezione") 
    });
    $("#btddt").click(function(){
        PushDdt();
        $("#tbf1").hide();
    });
});

function GetBolla(){
    $.post(
        "cvc",
        {cln:$("#azienda option:selected").text(),azione:"B"},
        function(ret){
            if(ret.length==0)
                return
            $("#tbf1").show();
            $("#cldt2").show();
            $("#btddt").show();
            $("#btmrg").show();        
            res=ret;    
            $("#dt2").val(res[0].idcod__produttore__margine);
            Write();
            return;
        });
};

function Write() {
    var before="";
    var label="";
    mrg=$("#dt2").val();
    for (i=0;i<res.length;i++){
        nt=res[i].costo*(1-mrg/100);
        label=label + '<tr>';
        if( res[i].bolla!=before){
            label=label + '<td><input type="checkbox" value='+res[i].bolla+'></td>';
            label=label + '<td>' +res[i].bolla+ '</td>';
        }
        else
        label=label + '<td></td><td></td>';
        label=label + '<td>' + res[i].idcod__cod+ '</td>';
        label=label + '<td>' + res[i].q+ '</td>';
        label=label + '<td>' + res[i].cassa + '</td>';
        label=label + '<td>' + res[i].data+ '</td>';
        label=label + '<td>' +res[i].costo+ '</td>';
        label=label + '<td>' +nt.toFixed(2)+ '</td>';
        label=label + '</tr>';
        before=res[i].bolla;
    }
    $("#tb6").html(label);  
    return
};

function PushDdt(){
    var ar=[];
    var st=[]
    var x=0;
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
    $.post(
        "cvc",
        {ddt:JSON.stringify(ar),mrg:$("#dt2").val(),frn:$("#azienda option:selected").text(),azione:"P"},
)};




