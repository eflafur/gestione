var UserTable=$("#mytable");
var TempUserTable=null;
var res="";

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#cldt2").hide();
    $("#cldt3").hide();
    $("#cldt4").hide();
    $("#cldt5").hide();
    $("#cldt6").hide();
    $("#cl").hide();
    $("#numfatt").keypress(function(){
        $("#cl").show();
    });
    $("#azienda").click(function(){
        $("#tbf1").hide();
        $("#cldt2").hide();
        $("#cldt3").hide();
        $("#cldt4").hide();
        $("#cldt5").hide();
        $("#cldt6").hide();
        $("#btddt").hide();
        $("#btmrg").hide();
        GetCv();
    });
    $("#btmrg").click(function(){
        Write($("#dt2").val());
    });
    $("#btddt").click(function(){
        PushDdt();
        $("#tbf1").hide();
           $("#cldt2").hide();
    $("#cldt3").hide();
    $("#cldt4").hide();
    $("#cldt5").hide();
    $("#cldt6").hide();
    $("#cl").hide();
    });
});

function GetCv(){
    $.post(
        "fattfrn",
        {cln:$("#azienda option:selected").text(),azione:"g"},
        function(ret){
            $("#tbf1").show();
            $("#cldt2").show();
            $("#btddt").show();
            $("#btmrg").show();        
            res=ret;    
            Write("");
            return;
        });
};

function Write(w) {
    var before="";
    var label="";
    var sum=0;
    var mrg1=res[0].mrg;
    if(w!="")
        mrg1=w
    for (i=0;i<res.length-1;i++){
        nt=res[i].costo*(1-mrg1/100);
        sum=sum+nt;
        label=label + '<tr>';
        if( res[i].cv!=before){
            label=label + '<td><input type="checkbox" value='+res[i].cv+'></td>';
            label=label + '<td>' +res[i].cv+ '</td>';
        }
        else
        label=label + '<td></td><td></td>';
        label=label + '<td>' +res[i].bolla+ '</td>';
        label=label + '<td>' + res[i].idcod__cod+ '</td>';
        label=label + '<td>' + res[i].q+ '</td>';
        label=label + '<td>' + res[i].cassa + '</td>';
        label=label + '<td>' + res[i].data+ '</td>';
        label=label + '<td>' +res[i].costo+ '</td>';
        label=label + '<td>' +nt.toFixed(2)+ '</td>';
        label=label + '</tr>';
        before=res[i].cv;
    }
    $("#tb6").html(label);  
    $("#dt2").val(mrg1);
    $("#cldt2").show();
    $("#dt3").val(res[i].ct);
    $("#dt4").val(res[i].rg);
    $("#dt5").val(res[i].pi);
    $("#dt6").val(sum);
    $("#cldt2").show();
    $("#cldt3").show();
    $("#cldt4").show();
    $("#cldt5").show();
    $("#cldt6").show();
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
        "fattfrn",
        {ft:$("#numfatt").val(),ddt:JSON.stringify(ar),azione:"P",costo:$("#dt6").val(),mrg:$("#dt2").val(),frn:$("#azienda option:selected").text()},
)};





