$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#lkfrn").click(function(){
        //var a=$("#lkfrn option:selected").text();
        $("#cldt2").show();
        $("#dt2").val("");
        //Put(a);
//        $("#idLKP").show();
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
        label="";

        for (i = 0; i < result.length; i++) {
            label = label + '<tr>';
            label = label + '<td>' + result[i].idcod__cod+ '</td>';
            label = label + '<td>' + result[i].q+ '</td>';
            label = label + '<td>' + result[i].bolla+ '</td>';
            label = label + '<td>' + result[i].data+ '</td>';
            label = label + '</tr>';
        }
        $("#tb3").html(label);
    });
    return;
};
