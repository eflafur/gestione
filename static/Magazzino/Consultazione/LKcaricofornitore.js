$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#lkfrn").click(function(){
        //var a=$("#lkfrn option:selected").text();
        $("#cldt2").show();
        $("#dt2").val("");
        $("#idLKP").hide();
    });
    
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01",//autoSize:true,appendText: "(yyyy-mm-dd)",// 
        onSelect: function (date) {
            var a=$("#lkfrn option:selected").text();
            $("#idLKP").show();
            Put(a,date);
        }
    });
});

function Put(item,date) {
    $.post(
        "lkfornitore",
        { res: item,res1:date},
        function (result) {
        var sum=0;
            label="";
            for (i = 0; i < result.length; i++) {
                sum=sum+parseFloat(result[i].q);
                label = label + '<tr>';
                label = label + '<td>' + result[i].idcod__cod+ '</td>';
                label = label + '<td>' + result[i].q+ '</td>';
                label = label + '<td>' + result[i].bolla+ '</td>';
                label = label + '<td>' + result[i].data+ '</td>';
                label = label + '</tr>';
            }
            label=label + '<tr><td>TOT</td><td>'+sum+ '</td></tr>';
            $("#tb3").html(label);  
             var $a=$("#tb3 tr:last-child");
            var $b= $a.find("td:last");  //.css("font-size","30px");
            $b.css("color", "blue");
        });
    return;
};
