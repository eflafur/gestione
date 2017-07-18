var UserTable=$("#tb");
var TempUserTable=null;

$(document).ready(function(){
  $.ajaxSetup({cache:false});

  $("#bt1").click(function(){
    GetTempData();
    });
  $("#bt0").click(function(){
    GetData();
    });
  });
  
  function GetTempData(){
    $.post(
      "manage",
      //{data:data1},
      function(result){
        if (TempUserTable!=null)
          TempUserTable.destroy();
          TempUserTable=UserTable.DataTable({
            "ordering":false,
            data:eval(result),
            columns:[
              {data:"settore"},
              {data:"area"},
              {data:"offerte"}
            ]
          });
      });
      return;
  };
  
  function GetData(){
  $.post(
    "manage",
    function (result){
    var label = " ";
        for (i = 0; i < result.length; i++) {
                    label = label + '<tr>';
                    label = label + '<td>' + result[i].settore + '</td>';
                    label = label + '<td>' + result[i].area+ '</td>';
                    label = label + '<td>' + result[i].offerte+ '</td>';
                    label = label + '</tr>';
                }
                $("#prova").html(label);
            });
            //});
    return;
};