
$(document).ready(function(){
    $.ajaxSetup({cache:false});

    $("#clientes").click(function(){
        $("#dt2").val(" ");
        $("#dtf").show();
        $("#tbf1").hide();
        $("#tbf2").hide();
        $("#pf").hide();
    });
    
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01",//autoSize:true,appendText: "(yyyy-mm-dd)",// 
        onSelect: function (date) {
            var cl=$("#clientes").val()
            $("#tb62").html(" ");
            $("#tbf2").hide();
            GetTable(date,cl);
            $("#pf").hide();
 
        }
    });
    
    $("#tablef").on('click','a',function(){
        a=$(this).text();
        GetFatt(a)
        $("#pfatt").val(a);
        $("#pf").show();
        $("#tbf1").hide();
        $("#tbf2").show();
    });
});

function GetTable(date,cl){
    $.post(
        "lkftrcln",
        {data:date,cliente:cl,azione:"table"},
        function(res){
            if(res.length==0)
                return;
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                label=label + '<td><a href="#">' + res[i].fattura + '</a></td>';
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

