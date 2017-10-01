var res=[];
var dt1;
$(document).ready(function(){
    $.ajaxSetup({cache:false});
//    $("#dt2").hide();
    $("#dtft").hide();
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01", 
        onSelect: function (date) {
            dt1=date;
            $("#tb62").html(" ");
            $("#tbf2").hide();
            GetBT(date,$("#bcodice option:selected").val());
            $("#pf").hide();
         }
    });
    
    $("#bcodice").click(function(){
       $("#pf").hide();
       $("#dt2").val("");
       $("#dtft").show();
    });
    
    $("#tablef").on('click','a',function(){
        y=$(this).text();
        GetFatt(y)
        $("#pcln").val(res[0].cliente__azienda);
        $("#pfatt").val(y);
        $("#pf").show();
        $("#tbf1").hide();
        $("#tbf2").show();
        $("#bt4").show();
       // window.location.replace("fattura?nome="+a+"&azione=ftr");
    });
    $("#btddt2").click(function(){
        $("#bt4").hide()
        $("#tb62").html(" ");
        $("#tbf2").hide();
        GetTable(dt1);
        $("#pf").hide();
    });
    
});

function GetTable(date){
    res.length=0;
    $.post(
        "rart",
        {data:date,azione:"r"},
        function(ret){
            res=ret;
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                label=label + '<td><a href="#">' + res[i].ddt + '</a></td>';
                label=label + '<td>' + res[i].cliente__azienda + '</td>';
                label=label + '<td>' + res[i].valore+ '</td>';
                label=label + '<td>' +res[i].data + '</td>';
                label=label + '</tr>';
            }
            $("#tbf1").show();
            $("#tb6").html(label);  
        });
        return
};
function GetBT(date,cod){
    res.length=0;
    $.post(
        "rart",
        {artid:cod,data:date,azione:"rart"},
        function(ret){
            $("#pf").show();
            $("#btot").val(ret);  
        });
        return
};


function GetFatt(num){
    $.post(
        "gino",
        {fatt:num,azione:"ftr"},
        function(res){
            var label="";
            var sum=0
            var prd=0;
            for (i=0;i<res.length;i++){
                label=label+'<tr>'
                sum=sum+parseFloat(res[i].prezzo)*parseFloat(res[i].q)*(parseFloat(res[i].idcod__genere__iva)+1);
                label=label + '<td>'+ res[i].idcod__cod + '</td>';
               // label=label + '<td>' + res[i].cliente__azienda + '</td>';
                label=label + '<td>' + res[i].cassa+ '</td>';
                label=label + '<td>' + res[i].q + '</td>';
                label=label + '<td>' + res[i].prezzo + '</td>';
                label=label + '<td>' + res[i].idcod__genere__iva + '</td>';
                label=label + '<td>' + res[i].data + '</td>';
                label=label+'</tr>'
            }
            label=label + '<td>ToT</td><td></td><td>' + sum + '</td>';
            label=label+'</tr>'
            $("#tb62").html(label);  
            $("#tb62 tr:last").find("td:last").css("color","blue");
        });
        return
};

