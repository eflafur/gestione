var dt1;
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#bt4").hide()
    $("#btt").hide()
    $("#pf1").hide();
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01", 
        onSelect: function (date) {
            dt1=date;
            $("#pf").hide();
            $("#pf1").hide();
            $("#btt").show();
         }
    });
    $("#btsps").click(function(){
            GetBT(0);
    });
    $("#btems").click(function(){
            GetBT(1);
    });
});

function GetBT(ctr){
    $.post(
        "rtotale",
        {data:dt1,tipo:ctr,azione:"r"},
        function(ret){
            $("#pf").show();
            $("#pf1").show();
            $("#btot").val(ret[0].diffcst);  
            $("#btotcl").val(ret[1].diffcs);  
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

