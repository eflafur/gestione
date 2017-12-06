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
        "rfrn",
        {codcn:cod,datacn:data,azione:"cod"},
        function(ret){
            WriteDt(ret,cod);            
        });
        return
};

function Write(res,cod){
    var label="";
    for (i=0;i<res.length;i++){
        label=label + '<tr>';
        label=label + '<td>' + res[i].prot+ '</td>';
        label=label + '<td>' + res[i].dtreg+ '</td>';
        label=label + '<td>' + res[i].doc+ '</td>';
        label=label + '<td>' + res[i].desc+ '</td>';
        label=label + '<td>' + res[i].conto+ '</td>';
        label=label + '<td>' + res[i].dare+ '</td>';
        label=label + '<td>' +res[i].avere+ '</td>';
        label=label + '</tr>';
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
              {data:"prot"},
              {data:"dtreg"},
              {data:"doc"},
              {data:"desc"},
              {data:"conto"},
              {data:"dare"},
              {data:"avere"}
            ]
        });
      return;
  };