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
        ret=ReadChange(0);
        WriteChecked(ret);    
    });
    $("#btddt").click(function(){
        ret=ReadChange(1);
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
        {cln:$("#azienda option:selected").text(),fatt:$("#numfatt").val(),azione:"g"},
        function(res){
            if(res==1){
                alert("Fattura: "+$("#numfatt").val()+" già esistente")
                window.location.replace("fattfrn");
            }
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
            label=label+'<td color="#FF0000"><a href="#">' + res[i].cv+ '</a></td>';
        else
            label=label + '<td></td>';
        label=label + '<td>' + res[i].bolla+ '</td>';
        label=label + '<td>' + res[i].data+ '</td>';
        label=label + '</tr>';
        before=res[i].cv
    }
    $("#tbf1").show();  
    $("#tb6").html(label);  
//    $("#tb6 tr:first").css("color","blue");//.find("td:last").css("color","blue");

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
    var sumcosto=0;
    for (i=0;i<res1.length;i++){
        nt1=res1[i].fattimp/res1[i].q*(1-mrgg/100);
        nt=nt1*res1[i].q;
        sum=sum+nt;
//        sumcosto=sumcosto+res1[i].costo;
        label=label + '<tr>';
        label=label + '<td style="display: none">' + res1[i].id+ '</td>';
        label=label + '<td>' + res1[i].bolla+ '</td>';
        label=label + '<td>' + res1[i].data+ '</td>';
        label=label + '<td>' + res1[i].q+ '</td>';
        label=label + '<td>' + res1[i].cassa+ '</td>';
        label=label + '<td>' + res1[i].idcod__cod+ '</td>';
        label=label + '<td><input class="prz" type=number value='+nt1.toFixed(2)+'></input></td>';
        label=label + '<td>'+nt.toFixed(2)+'</td>';
        label=label + '</tr>';
    }
    $("#tbf2").show();  
    $("#tb62").html(label);  
    $("#dt6").val(sum);
 //   $("#dt7").val(sumcosto-sum);
};


function ReadChange(n){
    var ls=[];
    $("#tb62 tr").each(function(){
    if(n==0)
        ls.push($(this));
    else if(n==1){
        var dc={}
        dc["id"]=$(this).find("td:first").text();
//        dc["prz"]=$(this).find("input.prz").val();
        dc["vnd"]=$(this).find("td:eq(7)").text();
        ls.push(dc);
    }
    });
//    ls.splice(0,1)
    return ls;
};

function WriteChecked(ret){
    var sumfatt=0;
    var sumvnd=0;
    var label="";
    label='<tr>'
    for (i=0;i<ret.length;i++){
        ft=parseFloat(ret[i].find("input.prz").val())*parseFloat(ret[i].find("td:eq(3)").text());
        r=ret[i].find("td:eq(7)").text(ft);
        label=label+r.html();
        sumfatt=sumfatt+ft;    
        sumvnd=sumvnd+parseFloat(ret[i].find("td:eq(7)").text())
    }
    label=label+'</tr>'
    $("tb62").html(label);
    $("#dt6").val(sumfatt);
    $("#dt7").val(sumvnd-sumfatt);
};

function PushDdt(ret){
    var ar=[];
    ar=JSON.stringify(ret);
    $.post(
        "fattfrn",
        {data:ar,fatt:$("#numfatt").val(),azione:"p",frn:$("#azienda option:selected").val(),mrg:$("#dt2").val()},
        function(ret){
            if(ret==1)
                alert("Fattura: "+$("#numfatt").val()+" già esistente")
            window.location.replace("fattfrn");
    });
};
