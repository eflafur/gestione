var res=[];
var d = new Date();
var strDate = d.getFullYear() + "-" + (d.getMonth()+1) + "-" + d.getDate();
var choice="";
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#chc").hide();
    
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01", 
        onSelect: function (date) {
            $("#chc").show();
            $("#tb62").html(" ");
            $("#tbf2").hide();
            GetTable(date);
            $("#pf").hide();
        }
    });
    
    $("#tb6").on('click','a',function(){
        a=$(this).text();
        GetFatt(a)
        $("#pcln").val(res[0].cliente__azienda);
        $("#pfatt").val(a);
        $("#pf").show();
        $("#tbf1").hide();
        $("#tbf2").show();
    });
    
    $("#tb6").on('click','button',function(){
        if(choice==""){
            alert("Inserire Banca/Cassa")
            return 1;
        }
        p=$(this).val();
        Pagato(p,$(this));
    });
    
    $("#chc").click(function(){
        choice=$("#chc :checked").val();
    });
});

function Pagato(fts,btc){
    var txt="";
    var pgm=0;
   $("#tb6 tr").each(function(index){
        ft=$(this).find("td:eq(0)").text();
        if(ft==fts){
            txt=$(this).find("input.note").val();//.find("td:eq(6)").text()
            p=parseFloat($(this).find("input.part").val());
            rim=parseFloat($(this).find("td:eq(8)").text());
            return false;
        }
    });
    if(p>=0 && p<rim){
        pgm=1
    }
    else if (p<0 || p>rim){
        alert("Valore inammissibile")
        return 1;
    }
    else if(isNaN(p) || p==rim){
        p=rim;
        btc.css('background-color','green');
    }
    $.post(
    "lkftr",
    {pg:ft,nt:txt,azione:"p",part:p,ppg:pgm,chc:choice},
    function(){
    });
}
    
function GetTable(date){
    res.length=0;
    $.post(
        "lkftr",
        {data:date,azione:"t",cliente:""},
        function(ret){
            res=ret;
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                label=label + '<td><a href="#">' + res[i].fattura + '</a></td>';
                label=label + '<td>' + res[i].cliente__azienda + '</td>';
                label=label + '<td>' + res[i].valore+ '</td>';
                label=label + '<td>' +res[i].data + '</td>';
                label=label + '<td>' +res[i].scadenza+ '</td>';
                label=label + '<td>' +res[i].pagato+ '</td>';
                label=label + '<td><input type="text" class="note"  value="'+res[i].note+'"></input></td>';
                label=label + '<td><input type="integer" class="part"></input></td>';
                label=label + '<td>' +res[i].rim+ '</td>';
                if(res[i].pagato==1)// && strDate>res[i].scadenza)
                    label=label + '<td><button class="btn-danger btn-sm" value="'+res[i].fattura +'"></button></td>';
                else
                    label=label + '<td><button class="btn-success btn-sm" value="'+res[i].fattura +'"></button></td>';
                label=label + '</tr>';
            }
            $("#tbf1").show();
            $("#tb6").html(label);  
        });
        return
};


function GetFatt(num){
    $.post(
        "lkftrcln",
        {fatt:num,azione:"ftr"},
        function(res){
            var label="";
            var sum=0
            var prd=0;
            for (i=0;i<res.length;i++){
                label=label+'<tr>'
                sum=sum+parseFloat(res[i].prezzo)*(parseFloat(res[i].q)-parseFloat(res[i].cassa)*parseFloat(res[i].tara))*(parseFloat(res[i].idcod__genere__iva)+1);
                label=label + '<td>'+ res[i].idcod__cod + '</td>';
                label=label + '<td>' + res[i].cassa+ '</td>';
                label=label + '<td>' + res[i].q + '</td>';
                label=label + '<td>' + res[i].prezzo + '</td>';
                label=label + '<td>' + res[i].idcod__genere__iva + '</td>';
                label=label + '<td>' + res[i].data + '</td>';
                label=label+'</tr>'
            }
            label=label + '<td>ToT</td><td></td><td></td><td>' + sum + '</td>';
            label=label+'</tr>'
            $("#tb62").html(label);  
            $("#tb62 tr:last").find("td:last").css("color","blue");
        });
        return
};

