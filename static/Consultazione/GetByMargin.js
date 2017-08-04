var UserTable=$("#mytable");
var TempUserTable=null;

$(document).ready(function(){
  $.ajaxSetup({cache:false});

  $("#bt2").click(function(){
    var a=$("#margine").val();
    if(a==""){
      return
    }
    GetList(a);
      $("#idLKP").show();
    });
  });
  
  function Get(name){
    $.post(
      "ricercaM",
      {data:name},
      function(result){
        if (TempUserTable!=null)
          TempUserTable.destroy();
          TempUserTable=UserTable.DataTable({
            "ordering":false,
            data:eval(result),
            columns:[
              {data:"azienda"},
              {data:"margine"},
              {data:"regione"},
              {data:"citta"}
            ]
          });
      });
      return;
  };
  
  function GetList(name){
  $.post(
    "ricercaM",
     {data:name},
    function (result){
    var label = " ";
        for (i = 0; i < result.length; i++) {
                    label = label + '<tr>';
                    label = label + '<td>' + result[i].azienda+ '</td>';
                    label = label + '<td>' + result[i].margine+ '</td>';
                    label = label + '<td>' + result[i].regione+ '</td>';
                    label = label + '<td>' + result[i].citta+ '</td>';
                    label = label + '</tr>';
                }
                $("#tb1").html(label);
            });
    return;
};

f