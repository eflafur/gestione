var res=[];
var d = new Date();
var strDate = d.getFullYear() + "-" + (d.getMonth()+1) + "-" + d.getDate();
var choice="";
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#brand").text("Salda Fattura");
    $("#chc").hide();
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01",
        onSelect: function (date) {
            $("#tb62").html(" ");
            $("#tbf2").hide();
            GetTable(date);
            $("#pf").hide();
            $("#chc").show();
        }
    });
    
    $("#tb6").on('click','a',function(){
        a=$(this).text();
        frn=$(this).val();
        GetFatt(a,frn)
        $("#pcln").val(res[0].cliente__azienda);
        $("#pfatt").val(a);
        $("#pf").show();
        $("#tbf1").hide();
        $("#tbf2").show();
    });
    
    $("#chc").click(function(){
        choice=$("#chc :checked").val();
    });
    
    $("#tb6").on('click','button',function(){
        if(choice==""){
            alert("Inserire Banca/Cassa")
            return 1;
        }
        p=$(this).val();
        Pagato(p);
    });
});

function Pagato(pgm){
    var txt="";
    var pg=0;
    var line;
    var th;
   $("#tb6 tr").each(function(index){
        line=$(this).find("button");
        if(index==pgm){
            th=$(this).find("td:eq(9)");
            p=parseFloat($(this).find("input.part").val());
            f=$(this).find("td:eq(1)").text();
            tot=parseFloat($(this).find("td:eq(9)").text());
            ft=$(this).find("td:eq(0)").text();
            id=$(this).find("td:eq(11)").text();
            return false;
        }
    });
    if(p>tot || p<0){
        alert("valore nammissibile") 
        return 1;
    }
    else if(isNaN(p) || p==tot){
        p=tot;
        pg=1
        line.css('background-color','green');
    }
    th.text(tot-p);
    $.post(
        "regfattfrn",
        {pg:ft,nt:txt,azione:"p",part:p,frn:f,idfrn:id,pgm:pg,chc:choice},
        function(){
    });
}
    
function GetTable(date){
    res.length=0;
    $.post(
        "regfattfrn",
        {data:date,azione:"t",cliente:""},
        function(ret){
            res=ret;
            var x=0
            var label="";
            if(res==1)
                window.location.replace("regfattfrn");
            for (i=0;i<res.length;i++){
                tot=parseFloat(res[i].erario)+parseFloat(res[i].imp);
                label=label + '<tr>';
                label=label + '<td><a href="#" value="tipo">' + res[i].fatt + '</a></td>';
                label=label + '<td>' + res[i].frn + '</td>';
                label=label + '<td>' +res[i].dt+ '</td>';
                label=label + '<td>' +res[i].dtadd+ '</td>';
                label=label + '<td>' + res[i].imp+ '</td>';
                label=label + '<td>' +res[i].erario+ '</td>';
                label=label + '<td>' +tot+ '</td>';
                label=label + '<td><input type="text" value="'+res[i].note+'"></input></td>';
                label=label + '<td><input type="integer" class="part"></input></td>';
                label=label + '<td>'+res[i].saldo+'</td>';
                if(res[i].pg==0 && strDate>res[i].dtadd)
                    label=label + '<td><button class="btn-danger btn-sm" value="'+ x++ +'"></button></td>';
                else
                    label=label + '<td><button class="btn-success btn-sm" value="'+ x++ +'"></button></td>';
                label=label + '<td style=display:none>'+res[i].idfrn+'</td>';
                label=label + '</tr>';
            }
            $("#tbf1").show();
            $("#tb6").html(label);  
        });
        return
};


function GetFatt(num,f){
    $.post(
        "regfattfrn",
        {fatt:num,azione:"ftr"},
        function(res){
            var label="";
            var prd=0;
            for (i=0;i<res.length;i++){
                totfatt=parseFloat(res[i].fattimp)*(1+parseFloat(res[i].idcod__genere__iva));
                totcosto=parseFloat(res[i].costo)*(1+parseFloat(res[i].idcod__genere__iva));
                label=label+'<tr>'
                label=label + '<td>' + res[i].bolla + '</td>';
                label=label + '<td>' + res[i].data + '</td>';
                label=label + '<td>'+ res[i].idcod__cod + '</td>';
                label=label + '<td>' + res[i].q + '</td>';
                label=label + '<td>' + res[i].cassa+ '</td>';
                label=label + '<td>' + totcosto+ '</td>';
                label=label + '<td>' + totfatt+ '</td>';
                label=label+'</tr>'
            }
            label=label+'</tr>'
            $("#tb62").html(label);  
            $("#pcln").val(res[0].idcod__produttore__azienda);  
        });
        return
};

