//var UserTable=$("#mytable");
//var TempUserTable=null;
var res1="";
$(document).ready(function(){
//    $.ajaxSetup({cache:false});
    $("#azienda").hide();
    Evidance();
    $("#numfatt").keypress(function(){
        $("#azienda").show();
    });
    $("#azienda").click(function(){
        $("#btddt").hide();
        $("#btmrg").hide();
        $("#btcrc").hide();
        $("#tbf2").hide();  
        $("#tbf1").hide();
        $("#cldt2").toggle();
        $("#cldt3").toggle();
        $("#cldt4").toggle();
        $("#cldt5").toggle();
        $("#cldt6").hide();
        $("#cldt7").hide();
        GetCv();
    });

    $("#tbf1").on('click','a',function(){
        a=$(this).text();
        $("#tbf1").hide();
        $("#btddt").show();
        $("#btmrg").show();
        $("#btcrc").show();
        $("#cldt6").show();
        $("#cldt7").show();
        PushCv(a)
    });
    
    $("#btmrg").click(function(){
        WriteCv($("#dt2").val());
    });
    $("#btcrc").click(function(){
        var sum=0,sumcst=0;
        ret=ReadChange();
        for (i=0;i<ret.length;i++){
            sum=sum+parseFloat(ret[i].cst);
            sumcst=sumcst+parseFloat(ret[i].vnd)
        }
        $("#dt6").val(sum);
        $("#dt7").val(sumcst-sum);
    });
    $("#btddt").click(function(){
        ret=ReadChange();
        PushDdt(ret);
        $("#tbf1").hide();
        $("#cldt2").hide();
        $("#cldt3").hide();
        $("#cldt4").hide();
        $("#cldt5").hide();
        $("#cldt6").hide();
        $("#cldt7").hide();
        $("#cl").hide();
    });
});

function Evidance(){
   $("#cldt2").toggle();
    $("#cldt3").toggle();
    $("#cldt4").toggle();
    $("#cldt5").toggle();
    $("#cldt6").toggle();
    $("#cldt7").toggle();
};

function GetCv(){
    $.post(
        "fattfrn",
        {cln:$("#azienda option:selected").text(),azione:"g"},
        function(res){
            Write(res);
            return;
        });
};

function Write(res) {
    var before="";
    var label="";
    var sum=0;
    for (i=0;i<res.length-1;i++){
        label=label + '<tr>';
        if(res[i].cv!=before)
            label=label+'<td><a href="#">' + res[i].cv+ '</a></td>';
        else
            label=label + '<td></td>';
        label=label + '<td>' + res[i].bolla+ '</td>';
        label=label + '<td>' + res[i].data+ '</td>';
        label=label + '</tr>';
        before=res[i].cv
    }
    $("#tbf1").show();  
    $("#tb6").html(label);  
    $("#tb6 tr:first").css("color","blue");//.find("td:last").css("color","blue");

    $("#dt2").val(res[i].mrg);
    $("#cldt2").show();
    $("#dt3").val(res[i].ct);
    $("#dt4").val(res[i].rg);
    $("#dt5").val(res[i].pi);
    $("#dt6").val(sum);
    $("#cldt2").show();
    $("#cldt3").show();
    $("#cldt4").show();
    $("#cldt5").show();
    return
};

function PushCv(cv){
    $.post(
        "fattfrn",
        {cvd:cv,azione:"v"},
        function(ret){
            res1=ret;
            WriteCv(0);
        });
};


function WriteCv(mrgg){
    var label="";
    var sum=0;
    var sumcst=0;
    for (i=0;i<res1.length;i++){
            nt=res1[i].fattimp*(1-mrgg/100);
        sum=sum+nt;
        sumcst=sumcst+parseFloat(res1[i].costo);
        label=label + '<tr>';
        label=label + '<td >' + res1[i].id+ '</td>';
        label=label + '<td>' + res1[i].bolla+ '</td>';
        label=label + '<td>' + res1[i].data+ '</td>';
        label=label + '<td>' + res1[i].q+ '</td>';
        label=label + '<td>' + res1[i].cassa+ '</td>';
        label=label + '<td>' + res1[i].idcod__cod+ '</td>';
        label=label + '<td>' + res1[i].costo+ '</td>';
        label=label + '<td><input class="tst" type=number value='+nt+'></input></td>';
        label=label + '</tr>';
    }
    $("#tbf2").show();  
    $("#tb62").html(label);  
    $("#dt6").val(sum);
    $("#dt7").val(sumcst-sum);
};


function ReadChange(){
    var ls=[];
   $("#tb62 tr").each(function(){
        var dc={}
        dc["id"]=$(this).find("td:first").text();
        dc["cst"]=$(this).find("input.tst").val();
        dc["vnd"]=$(this).find("td:eq(6)").text();
        ls.push(dc);
    });
//    ls.splice(0,1)
    return ls;
};

function PushDdt(ret){
    var ar=[];
    ar=JSON.stringify(ret);
    $.post(
        "fattfrn",
        {data:ar,fatt:$("#numfatt").val(),azione:"p",frn:$("#azienda option:selected").val()},
        function(ret){
            if(ret==1)
                alert("Fattura: "+$("#numfatt").val()+" già esistente")
            window.location.replace("fattfrn");
    });
};
