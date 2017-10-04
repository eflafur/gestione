
var UserTable=$("#mytable");
var TempUserTable=null;

var option=""
var optionValues=[];

$(document).ready(function(){
    $.ajaxSetup({cache:false});

    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01",onSelect: function (date) {
            GetTable(date);
                $("#tbf1").show();
                return
        }
    });
    
    $("#tablef").on('click','a',function(){
        var ar=[]
        a=$(this).text();
        ar=a.split("-");
        window.location.replace("entrata?bolla="+ar[0]+"&cliente="+ar[1]+"&azione=sps");
       // return; 
    });
    
});

function GetTable(date){
    $.post(
        "lkfornitore",
        {res:$("#lkfrn option:selected").text(),res1:date},
        function(res){
            var below=" ";
            var label="";
            var ar=[];
            var bl=" ";
            for (i=0;i<res.length;i++){
                ar=res[i].idcod__cod.split("-");
                bl=res[i].bolla +'-'+ ar[0];
                if(bl!=below){
                    label=label + '<tr>';
                    label=label + '<td><a href="#">' + bl+ '</a></td>';
                }
                else
                label=label + '<tr><td></td>';
                label=label + '<td>' + res[i].idcod__cod+ '</td>';
                label=label + '<td>' + res[i].q+ '</td>';
                label=label + '<td>' + res[i].cassa+ '</td>';
                label=label + '<td>' +res[i].data + '</td>';
                label=label + '</tr>';
                below=bl
            }
            $("#tb6").html(label);  
            $("#tbf1").show();
        });
        return
};


