var UserTable=$("#tablef2");
var TempUserTable=null;

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#dtft").hide();
    $("#tbf1").hide();
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01", 
        onSelect: function (date) {
            dt1=date;
            GetBT(date,$("#bcodice option:selected").val());
         }
    });
    
    $("#bcodice").click(function(){
        $("#dt2").val(" ");
        $("#tbf1").hide();
        $("#dtft").show();
    });
});

function GetBT(data,cod){
    $.post(
        "rsfrn",
        {},
        function(ret){
            WriteDt(ret,cod);            
        });
        return
};

function Write(res,cod){
    var label="";
    var subtot=0;
    var cliente="";
    for (i=0;i<res.length;i++){
        subtot+=res[i].attivo
        if(res[i].cliente__azienda!=cliente && cliente!=""){
            label=label + '<tr>';
            label=label + '<td>' + res[i].cliente+ '</td>';
            label=label + '<td>' + res[i].passivo+ '</td>';
            label=label + '<td>' +res[i].prod__azienda+ '</td>';
            label=label + '</tr>';
        
        }
        else{
            label=label + '<tr>';
            label=label + '<td>' + res[i].attivo+ '</td>';
            label=label + '<td>' + res[i].passivo+ '</td>';
            label=label + '<td>' +res[i].prod__azienda+ '</td>';
            label=label + '</tr>';
        }
        cliente=res[i].prod__azienda
    }
    $("#tbf1").show();
    $("#tb6").html(label);  
    return
};

 function WriteDt(result,cod){
     $("#tbf1").show();
        if (TempUserTable!=null)
          TempUserTable.destroy();
          TempUserTable=UserTable.DataTable({
            "ordering":true,
            data:eval(result),
            columns:[
              {data:"prod__azienda"},
              {data:"attivo"},
              {data:"passivo"},
              { render: function(data, type, row){
                return row["attivo"]-row["passivo"];}
              }
            ]
        });
      return;
  };