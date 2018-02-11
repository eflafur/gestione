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
        "contims",
        {ms:cod},
        function(ret){
            Write(ret,cod);            
        });
        return
};

function Write(res,cod){
    var label="";
    var subtot=0;
    var cliente="";
    for (i=0;i<res.length;i++){
        subtot+=res[i].sum__dare
        if(res[i].cliente__azienda!=cliente && cliente!=""){
            label=label + '<tr>';
            label=label + '<td>' + res[i].sum__dare+ '</td>';
            label=label + '<td>' + res[i].sum__avere+ '</td>';
            label=label + '<td>' +res[i].cliente__azienda+ '</td>';
            label=label + '</tr>';
        
        }
        else{
            label=label + '<tr>';
            label=label + '<td>' + res[i].sum__dare+ '</td>';
            label=label + '<td>' + res[i].sum__avere+ '</td>';
            label=label + '<td>' +res[i].cliente__azienda+ '</td>';
            label=label + '</tr>';
        }
        cliente=res[i].cliente__azienda
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
              {data:"cliente__azienda"},
              {data:"dare"},
              {data:"avere"},
              { render: function(data, type, row){
                return row["dare"]-row["avere"];}
              }
            ]
        });
      return;
  };