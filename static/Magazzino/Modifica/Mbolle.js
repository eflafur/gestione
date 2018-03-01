
var UserTable=$("#tablef");
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
        var ar1=[]
        a=$(this).text();
        ar1=a.split("-");
        window.location.replace("entrata?bolla="+ar1[0]+"&cliente="+ar1[1]+"&azione=sps");
       // return; 
    });
    
});

function GetTable(date){
    $.post(
        "lktotale",
        {data:date},
        function(res){
            var below=" ";
            var label="";
            var ar=[];
            var bl=" ";
            for (i=0;i<res.length;i++){
                ar=res[i].carico__idcod__cod.split("-");
                bl=res[i].carico__bolla +'-'+ ar[0];
                if(bl!=below){
                    label=label + '<tr>';
                    label=label + '<td><a href="#">' + bl+ '</a></td>';
                }
                else
                label=label + '<tr><td></td>';
                label=label + '<td>' + res[i].carico__idcod__cod+ '</td>';
                label=label + '<td>' + res[i].q+ '</td>';
                label=label + '<td>' + res[i].cassa+ '</td>';
                label=label + '<td>' +res[i].carico__data + '</td>';
                label=label + '</tr>';
                below=bl
            }
            $("#tb6").html(label);  
            $("#idLKP").show();
        });
        return
};


function GetTableDT(date){
     $.post(
        "lktotale",
        {data:date},
        function(res){
            var below=" ";
            var label="";
            var ar=[];
            var bl=" ";
            if(res.length==0)
                return;

        if (TempUserTable!=null)
          TempUserTable.destroy();
          TempUserTable=UserTable.DataTable({
    //        "searching": false,
            "ordering":true,
            data:eval(res),
            columns:[
              {data:"bolla"},
              {data:"idcod__cod"},
              {data:"idcod__cod"},
              {data:"idcod__cod"},
              {data:"idcod__produttore__azienda"},
              {data:"cassa"},
              {data:"fatt"}
              //{ render: function(data, type,row){
              //return row["valore"];}
              //}
            ]
        });
        //var table = $('#tablef').DataTable();
        //t=table.column( 2 ).data().sum();
        //$("#totale").val(t.toFixed(2));
        //$("#pgm").hide();
        //$("#tbf3").show();
        //$("#tott").show()
//      return;
  });
              $("#idLKP").show();
  x=1;
  };
