var res=[];
var d = new Date();
var strDate = d.getFullYear() + "-" + (d.getMonth()+1) + "-" + d.getDate();
$(document).ready(function(){
    $.ajaxSetup({cache:false});

   
    
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01", 
        onSelect: function (date) {
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
        p=$(this).val();
        $(this).css('background-color','green');
        Pagato(p);
    });
    
});

function Pagato(pgm){
    var txt="";
   $("#tb6 tr").each(function(index){
        ft=$(this).find("td:eq(0)").text();
        if(ft==pgm){
            txt=$(this).find("input").val();//.find("td:eq(6)").text()
            return false;
        }
    });
    $.post(
    "lkftr",
    {pg:ft,nt:txt,azione:"p"},
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
                label=label + '<td><input type="text" value="'+res[i].note+'"></input></td>';
                if(res[i].pagato==1 && strDate>res[i].scadenza)
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
                sum=sum+parseFloat(res[i].prezzo)*parseFloat(res[i].q)*(parseFloat(res[i].idcod__genere__iva)+1);
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

