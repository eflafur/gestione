
var UserTable=$("#mytable");
var TempUserTable=null;

var option=""
var optionValues=[];
$(document).ready(function(){
    $.ajaxSetup({cache:false});

    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01",//autoSize:true,appendText: "(yyyy-mm-dd)",// 
        onSelect: function (date) {
            GetTable(date);
                $("#tbf1").show();
        }
    });
    
    $("#tablef").on('click','a',function(){
        a=$(this).text();
        window.location.replace("fattura?nome="+a+"&azione=sps");
    });
    
});

function GetTable(date){
    $.post(
        "sospesa",
        {data:date,cliente:" "},
        function(res){
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                label=label + '<td><a href="#">' + res[i].fatturas + '</a></td>';
                label=label + '<td>' + res[i].cliente__azienda + '</td>';
                label=label + '<td>' + res[i].valore+ '</td>';
                label=label + '<td>' +res[i].data + '</td>';
                label=label + '</tr>';
            }
            $("#tb6").html(label);  
            $("#idLKP").show();
        });
        return
};


