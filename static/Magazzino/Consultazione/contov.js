//var UserTable=$("#mytable");
//var TempUserTable=null;
var res1="";
var xx=0;
var cntrl=0;
$(document).ready(function(){
//    $.ajaxSetup({cache:false});
    Evidance();
    $("#azienda").click(function(){
        $("#btddt").show();
        $("#btmrg").show();
        $("#btslz").show();
        $("#btcrc").show();
        $("#tbf2").show();  
        $("#tbf1").show();
        $("#cldt2").show();
        $("#cldt3").show();
        $("#cldt4").show();
        $("#cldt5").show();
        $("#cldt6").show();
        $("#cldt7").show();
        if(cntrl==0){
            GetCv();
            return;
        }
        Write($("#dt2").val());
    });
    
    $("#btmrg").click(function(){
 //       if(xx==0)
            Write($("#dt2").val());
   //     else
            return;
    });
    $("#btcrc").click(function(){
        var sum=0;
        var sumcst=0;
        ret=ReadChange();
        for (i=0;i<ret.length;i++){
            sum=sum+parseFloat(ret[i].cst);
            sumcst=sumcst+parseFloat(ret[i].vnd)
        }
            $("#dt6").val(sum);
            $("#dt7").val(sumcst-sum);
    });
    
    $("#btsel").click(function(){
        $("#btslz").hide();
        ret=GetCheched();
        WriteChecked(ret);
    });
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
    
function Evidance(){
    $("#btslz").toggle();
    $("#cldt2").toggle();
    $("#cldt3").toggle();
    $("#cldt4").toggle();
    $("#cldt5").toggle();
    $("#cldt6").toggle();
    $("#cldt7").toggle();
};

function GetCv(){
    cntrl=1;
    $.post(
        "cvc",
        {cln:$("#azienda option:selected").text(),azione:"b"},
        function(res){
            var k=res.length;
            var mrg=0;
            res1=res;
            $("#dt2").val(res1[k-1].mrg);
            $("#tbf2").show();
            Write($("#dt2").val());
            return;
        });
};

function Write(mrg){
    var before="";
    var label="";
    var sum=0;
    var sumcst=0;
    for (i=0;i<res1.length-1;i++){
        nt=res1[i].costo*(1-mrg/100);
        sum=sum+nt;
        sumcst=sumcst+parseFloat(res1[i].costo);
        label=label + '<tr>';
        if( res1[i].bolla!=before){
            label=label + '<td><input type="checkbox" value='+res1[i].bolla+'></td>';
            label=label + '<td>' + res1[i].bolla+ '</td>';
        }
        else
        label=label+'<td></td><td></td>'
        label=label + '<td style="display: none">' + res1[i].bolla+ '</td>';
        label=label + '<td>' + res1[i].data+ '</td>';
        label=label + '<td>' + res1[i].q+ '</td>';
        label=label + '<td>' + res1[i].cassa+ '</td>';
        label=label + '<td>' + res1[i].idcod__cod+ '</td>';
        label=label + '<td>' + res1[i].costo+ '</td>';
        label=label + '<td><input class="tst" type=number value='+nt.toFixed(2)+'></input></td>';
        label=label + '<td style="display: none">' + res1[i].id+ '</td>';
        label=label + '</tr>';
        before=res1[i].bolla;
    }
    $("#cldt2").show();
    $("#dt3").val(res1[i].ct);
    $("#dt4").val(res1[i].rg);
    $("#dt5").val(res1[i].pi);
    $("#dt6").val(sum);
    $("#cldt2").show();
    $("#cldt3").show();
    $("#cldt4").show();
    $("#cldt5").show();
    
    $("#tbf2").show();  
    $("#tb62").html(label);  
    $("#dt6").val(sum);
    $("#dt7").val(sumcst-sum);
};

function WriteChecked(ret){
    var label="";
    label='<tr>'
    for (i=0;i<ret.length;i++)
        label=label+ret[i];
    label=label+'</tr>'
    $("tb62").html(label);
};

function ReadChange(){
    var ls=[];
    $("#tb62 tr").each(function(){
         var dc={}
         dc["id"]=$(this).find("td:last").text();
         dc["cst"]=$(this).find("input.tst").val();
         dc["vnd"]=$(this).find("td:eq(7)").text();
         ls.push(dc);
     });
     //if(xx==0)
         //ls.splice(0,1)
     return ls;
};

function PushDdt(ret){
    var ar=[];
    ar=JSON.stringify(ret);
    $.post(
        "cvc",
        {data:ar,azione:"p",mrg:$("#dt2").val(),frn:$("#azienda option:selected").val()},
        function(){
            window.location.replace("cvc");
    });
};

function GetCheched(){
    var ar=[];
    var lsck=[]
    var t=0;
    var x=0;
    $("#tbf2 :checked").each(function(index){
        xx=index+1;
        ar[index]=$(this).val();
    });

    if(xx>0){
        $("#tb62 tr").each(function(){
             r=$(this).find("td:eq(2)").text();
             for (i=0;i<ar.length;i++){
                 if(r==ar[i]){
                     lsck.push($(this).html());
                     t=1;
                     break;
                 }
                 continue;
             }
             if(t==0)
                 $(this).remove()
             t=0;
         });
        return lsck;
    } 
    else {
        $("input:checkbox:not(:checked)").each(function(index){
            x=index
            ar[x]=$(this).val();
        });
    }
    //$.post(
        //"cvc",
        //{ddt:JSON.stringify(ar),mrg:$("#dt2").val(),frn:$("#azienda option:selected").text(),azione:"P"},
    return ;
};