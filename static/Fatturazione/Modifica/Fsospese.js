
var UserTable=$("#mytable");
var TempUserTable=null;

var option=""
var optionValues=[];
$(document).ready(function(){
    $.ajaxSetup({cache:false});

    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01",//autoSize:true,appendText: "(yyyy-mm-dd)",// 
        onSelect: function (date) {
            GetTable(date);
                $("#tbf").show();
        }
    });
    
    $("#tablef").on('click','a',function(){
        a=$(this).text();
        GetSospese(a);
    });
    
});

function GetTable(date){
    $.post(
        "sospesa",
        {data:date,azione:"tabella"},
        function(res){
            var arr=new Array();
            var label="";
            var sum=0
            for (i=0;i<res.length;i++){
                arr=""
                arr=(res[i].idcod__cod).split("-");
                sum=sum+parseInt(res[i].prezzo);
                label=label + '<tr>';
                label=label + '<td><a href="#">' + res[i].fatturas + '</a></td>';
                label=label + '<td>' + arr[0] + '</td>';
                label=label + '<td>' + res[i].idcod__cod + '</td>';
                label=label + '<td>' + res[i].q + '</td>';
                label=label + '<td>' +res[i].prezzo + '</td>';
                label=label + '<td>' +res[i].data + '</td>';
                label=label + '</tr>';
            }
            label=label + '<tr><td>TOT</td><td></td><td></td><td></td><td>'+sum+ '</td></tr>';
            $("#tb6").html(label);  
            $("#idLKP").show();
            var $a=$("#tb6 tr:last-child");
            var $b= $a.find("td:last");  //.css("font-size","30px");
            $b.css("color", "blue");
        });
        return
};


function GetSospese(num){
    $.post(
    "sospesa",
        {item:num,azione:"reopen"},
        function(res){
            window.location.replace("fattura");
       
        });
    
};