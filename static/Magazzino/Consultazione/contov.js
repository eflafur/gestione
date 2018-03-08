var res1="";
var xx=0;
$(document).ready(function(){
//    $.ajaxSetup({cache:false});
    $("#brand").text("Clienti CV");
    Evidance();
    $("#azienda").click(function(){
        $("#tbf2").hide();
        $("#btddt").hide();
        $("#btmrg").show();
        $("#btslz").show();
//        $("#btcrc").show();
        $("#cldt2").show();
        $("#cldt3").show();
        $("#cldt4").show();
        $("#cldt5").show();
        $("#cldt6").show();
        $("#cldt7").show();
        $("#btcrc").hide();
        GetBolle();
    });
    
    $("#btmrg").click(function(){
            Write($("#dt2").val());
            return;
    });
    $("#btcrc").click(function(){
        ret=ReadChange(0);
        if(ret.length==0)
            return false;
        WriteChecked(ret);
    });
    
    $("#btsel").click(function(){
        $("#btcrc").show();
        $("#btmrg").hide();
        $("#btslz").hide();
        ret=GetCheched1();
        PostChecked(ret);
    });
});

    $("#btddt").click(function(){
        ret=ReadChange(1);
        if(ret.length==0)
            return false;

        PushDdt(ret);
        $("#tbf1").hide();
        $("#tbf2").hide();
        $("#tbf3").hide();
        $("#cldt2").hide();
        $("#cldt3").hide();
        $("#cldt4").hide();
        $("#cldt5").hide();
        $("#cldt6").hide();
        $("#cldt7").hide();
        $("#cl").hide();
    });
    
    $("#tbf1").on('click','a',function(){
        var bl=$(this).text();
        GetBolla(bl);
    });
    
function Evidance(){
    $("#btcrc").hide();
    $("#tbf1").hide();
    $("#tbf2").hide();
    $("#tbf3").hide();
    $("#btslz").toggle();
    $("#cldt2").toggle();
    $("#cldt3").toggle();
    $("#cldt4").toggle();
    $("#cldt5").toggle();
    $("#cldt6").toggle();
    $("#cldt7").toggle();
};


function GetBolle(){
    var label="";
    $("#tbf3").hide();  
    $.post(
        "cvc",
        {cln:$("#azienda option:selected").val(),azione:"b"},
        function(res){
        var x=0;
            for (i=0;i<res.length;i++){
                x=parseFloat(res[i].cassa)-parseFloat(res[i].cassaexit)
                label=label + '<tr>';
                label=label + '<td><input type="checkbox" value='+res[i].bolla+'></td>';
                label=label + '<td><a href="#">' + res[i].bolla+ '</a></td>';
                label=label + '<td>' + res[i].data+ '</td>';
                label=label + '<td>' + res[i].cassa+ '</td>';
                label=label + '<td>' + res[i].cassaexit+ '</td>';
                label=label + '<td>' + res[i].facc+ '</td>';
                label=label + '<td>' + res[i].trasporto+ '</td>';
                label=label + '<td>' + res[i].vari+ '</td>';
                label=label + '<td>' + res[i].produttore__margine+ '</td>';
                label=label + '<td>' + x+ '</td>';
                if(res[i].cassa>res[i].cassaexit)
                    label=label + '<td><button class="btn-danger btn-sm" value="'+ x +'"></button></td>';
                else
                    label=label + '<td><button class="btn-success btn-sm" value="'+ x +'"></button></td>';
                label=label + '</tr>';
            }
        $("#tbf1").show();  
        $("#tb61").html(label);          
    });
    return;
};



function GetBolla(bl){
    $.post(
        "cvc",
        {cln:$("#azienda option:selected").val(),bolla:bl,azione:"b1"},
        function(res){
            var label="";
            var x=0;
            for (i=0;i<res.length;i++){
                x=parseFloat(res[i].qn)/parseFloat(res[i].costo)
                label=label + '<tr>';
                label=label + '<td>' + res[i].bolla+ '</td>';
                label=label + '<td>' + res[i].idcod__cod+ '</td>';
                label=label + '<td>' + res[i].cassa+ '</td>';
                label=label + '<td>' + res[i].cassaexit+ '</td>';
                label=label + '<td>' + res[i].q+ '</td>';
                label=label + '<td>' + res[i].qn+ '</td>';
                label=label + '<td>' + res[i].tara+ '</td>';
                label=label + '<td>' +x.toFixed(2) + '</td>';
                label=label + '<td>' + res[i].costo+ '</td>';
                label=label + '</tr>';
            }
        $("#tbf1").hide();  
        $("#tbf3").show();  
        $("#tb63").html(label);          
        });
    }








function GetCheched1(){
    var ar=[];
    var lsck=[]
    var t=0;
    var x=0;
    var sum=0;
    var sumcst=0;
    var excs=0;
    var totexcsbl=0;
    $("#tbf1 :checked").each(function(index){
        xx=index+1;
        ar[index]=$(this).val();
    });

    if(xx>0){
        $("#tb61 tr").each(function(){
             r=$(this).find("td:eq(2)").text();
        }); 
    }
    else {
        $("input:checkbox:not(:checked)").each(function(index){
            x=index
            ar[x]=$(this).val();
        });
    }
    return ar;
};

function PostChecked(ret){
    var x=[]
    ar=JSON.stringify(ret);
    $.post(
        "cvc",
        {data:ar,azione:"p1",frn:$("#azienda option:selected").val()},
        function(res1){
            var before="";
            var label="";
            var sum=0;
            var sumcst=0;
            var excs=0;
            var totexcsbl=0;
            var mrg=res1[res1.length-1]["mrg"]
            for (i=0;i<res1.length-1;i++){
                excs=parseFloat(res1[i].excsbl__trasporto)+parseFloat(res1[i].excsbl__facc)+parseFloat(res1[i].excsbl__vari)
                nt1=(res1[i].costo/res1[i].q)*(1-mrg/100);
                nt=nt1*res1[i].q;
                iva=nt*(1+parseFloat(res1[i].idcod__genere__iva))
                sum=sum+nt;
                sumcst=sumcst+parseFloat(res1[i].costo);
                label=label + '<tr>';
                if(res1[i].bolla!=before){
                    label=label + '<td>' + res1[i].bolla+ '</td>';
                }
                else
                    label=label+'<td></td>'
                label=label + '<td style="display: none">' + res1[i].bolla+ '</td>';
                label=label+'<td>Carico</td>'
                label=label + '<td>' + res1[i].data+ '</td>';
                label=label + '<td>' + res1[i].qn+ '</td>';
                label=label + '<td>' + res1[i].cassa+ '</td>';
                label=label + '<td>' + res1[i].idcod__cod+ '</td>';
                label=label + '<td>' + res1[i].costo+ '</td>';
                label=label + '<td>'+nt1.toFixed(2)+'</td>';
                label=label + '<td>'+nt.toFixed(2)+'</td>';
                label=label + '<td>' + iva.toFixed(2)+ '</td>';
                label=label + '<td style="display: none">' + res1[i].idcod__genere__iva+ '</td>';
                label=label + '<td style="display: none">' + res1[i].id+ '</td>';
                label=label + '</tr>';

                
                label=label + '<tr style="color: #0000FF" >';
                label=label+'<td></td>'
                label=label + '<td style="display: none">' + res1[i].bolla+ '</td>';
                label=label+'<td>Scarico</td>'
                label=label + '<td>' + res1[i].data+ '</td>';
                label=label + '<td>' + res1[i].q+ '</td>';
                label=label + '<td>' + res1[i].cassaexit+ '</td>';
                label=label + '<td>' + res1[i].idcod__cod+ '</td>';
                label=label + '<td>' + res1[i].costo+ '</td>';
                label=label + '<td>'+nt1.toFixed(2)+'</td>';
                label=label + '<td>'+nt.toFixed(2)+'</td>';
                label=label + '<td>' + iva.toFixed(2)+ '</td>';
                label=label + '<td style="display: none">' + res1[i].idcod__genere__iva+ '</td>';
                label=label + '<td style="display: none">' + res1[i].id+ '</td>';
                label=label + '</tr>';
                
//                label=label + '<tr bgcolor="#CCEEFF>';
                label=label + '<tr style="color: #008000" >'
                label=label + '<td></td>'
                label=label + '<td style="display: none">' + res1[i].bolla+ '</td>';
                label=label+'<td>Ricavo</td>'
                label=label + '<td>' + res1[i].data+ '</td>';
                label=label + '<td><input class="psr" type=text maxlength="6" size="6" value=0></input></td>';
                label=label + '<td><input class="clr" type=text maxlength="6" size="6" value=0></input></td>';
                label=label + '<td> ' + res1[i].idcod__cod+ ' </td>';
                label=label + '<td>0</td>';
                label=label + '<td><input class="przr" type=text style=width:40% value=0></input></td>';
                label=label + '<td>0</td>';
                label=label + '<td>0</td>';
                label=label + '<td style="display: none">' + res1[i].idcod__genere__iva+ '</td>';
                label=label + '<td style="display: none">' + res1[i].id+ '</td>';
                label=label + '<td>0</td>';
                label=label + '<td style="display: none">'+nt1.toFixed(2)+'</td>';
                label=label + '<td style="display: none">'+res1[i].cassa+'</td>';
                label=label + '</tr>';
                label=label + '<tr><td></td></tr>';
                
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
            
            $("#tbf1").hide();  
            $("#tbf2").show();  
            $("#tb62").html(label);  
            $("#dt6").val(sum);
            $("#dt7").val(sumcst-sum-totexcsbl);
            });
};

function ReadChange(n){
    var ls=[];
    var rcv="";
    $("#tb62 tr").each(function(){
        rcv=$(this).find("td:eq(2)").text();
        if(rcv=="Ricavo" ){
            colli=parseFloat($(this).find("td:eq(15)").text());
            collir=parseFloat($(this).find("input.clr").val());
            if(collir!=colli){
                alert("Num. Colli ricavi inferiore al carico della bolla")
                $("#btddt").hide();
                ls.length=0;
                return false;
            }
            if(n==0)
                ls.push($(this));
            else if(n==1){
                var dc={}
                    dc["id"]=$(this).find("td:eq(12)").text();
                     dc["przr"]=$(this).find("input.przr").val();
                     dc["psr"]=$(this).find("input.psr").val();
                     dc["fatt"]=$(this).find("td:eq(10)").text();
                     ls.push(dc);
            }
        }
     });
     //if(xx==0)
         //ls.splice(0,1)
     return ls;
};

function WriteChecked(ret){
    var summrg=0;
    var sumfatt=0;
    var sumvnd=0;
    var label="";
    var totexcsbl=0;
    var przcr=0;
    label='<tr>'
    for (i=0;i<ret.length;i++){
        prz=parseFloat(ret[i].find("input.przr").val());
        p=parseFloat(ret[i].find("input.psr").val());
        iva=1+parseFloat(ret[i].find("td:eq(11)").text());
        przcr=parseFloat(ret[i].find("td:eq(14)").text());
        colli=parseFloat(ret[i].find("td:eq(15)").text());
        collir=parseFloat(ret[i].find("input.clr").val());
        ret[i].find("td:eq(9)").text((prz*p).toFixed(2));
        ret[i].find("td:eq(10)").text((prz*p*iva).toFixed(2));
        if(prz==0){
            przcr=1;
            prz=1;
        }
        if(collir!=colli){
            alert("Num. Colli ricavi inferiore al carico della bolla")
            $("#btddt").hide();
            return 1;
        }
            
        ret[i].find("td:eq(13)").text((przcr/prz-1).toFixed(2));
        summrg=summrg+(przcr/prz-1);
        label=label+ret[i];
        sumfatt+=prz*p;    
        sumvnd+=parseFloat(ret[i].find("td:eq(7)").text());
    }
    label=label+'</tr>'
    $("tb62").html(label);
    $("#dt6").val(sumfatt);
    $("#dt2").val(summrg/i);
    $("#dt7").val(sumvnd-sumfatt-totexcsbl);
    $("#btddt").show();

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
