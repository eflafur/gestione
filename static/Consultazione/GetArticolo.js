var UserTable=$("#mytable");
var TempUserTable=null;

$(document).ready(function(){
  $.ajaxSetup({cache:false});

  $("#articolo").click(function(){
    var a=$("#articolo option:selected").text();
    GetList(a);
      $("#idLKP").show();
    });
  $("#bt0").click(function(){
    GetData();
    });

  });
  
  function Get(name){
    $.post(
      "ricercaA",
      {data:name},
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
  
  function GetList(name){
  $.post(
    "ricercaA",
     {data:name},
    function (result){
    var label = " ";
        for (i = 0; i < result.length; i++) {
                    label = label + '<tr>';
                    label = label + '<td>' + result[i].produttore__azienda + '</td>';
                    label = label + '</tr>';
                }
                $("#tb1").html(label);
            });
    return;
};