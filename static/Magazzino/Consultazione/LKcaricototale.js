//3920656735
var UserTable=$("#mytable");
var TempUserTable=null;

var option=""
var optionValues=[];
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#cldt2").show();
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01",//autoSize:true,appendText: "(yyyy-mm-dd)",// 
        onSelect: function (date) {
            GetTable(date);
        }
    });
});

function GetTable(date){
    $.post(
        "lktotale",
        {data:date},
        function(res){
            var arr=new Array();
            var label="";
            var sum=0
            for (i=0;i<res.length;i++){
                arr=""
                arr=(res[i].idcod__cod).split("-");
                sum=sum+parseFloat(res[i].q);
                label=label + '<tr>';
                label=label + '<td>' + arr[0] + '</td>';
                label=label + '<td>' + arr[2] + '</td>';
                label=label + '<td>' + res[i].q + '</td>';
                label=label + '<td>' + res[i].bolla + '</td>';
                label=label + '<td>' +res[i].data+ '</td>';
                label=label + '</tr>';
            }
            label=label + '<tr><td>TOT</td><td></td><td>'+sum+ '</td></tr>';
            $("#tb5").html(label);  
            $("#idLKP").show();
            var $a=$("#tb5 tr:last-child");
            var $b= $a.find("td:last");  //.css("font-size","30px");
            $b.css("color", "blue");
        });
        return
};

 function Get(date){
    $.post(
        "lktotale",
        {data:date},
        function(result){
            if (TempUserTable!=null)
                TempUserTable.destroy();
            TempUserTable=UserTable.DataTable({
            "ordering":false,
            data:eval(result),
            columns:[
            {data:"produttore__azienda"}
            ]
          });
      });
      return;
  };