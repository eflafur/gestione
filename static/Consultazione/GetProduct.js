var UserTable=$("#mytable");
var TempUserTable=null;

$(document).ready(function(){
  $.ajaxSetup({cache:false});

  $("#azienda").click(function(){
    var a=$("#azienda option:selected").text();
    
    GetList(a);
      $("#idLKP").show();
      $("#idLKP1").show();
    });
  $("#bt0").click(function(){
    GetData();
    });

  });
  
  function Get(name){
    $.post(
      "ricercaP",
      {data:name},
      function(result){
        if (TempUserTable!=null)
          TempUserTable.destroy();
          TempUserTable=UserTable.DataTable({
            "ordering":false,
            data:eval(result),
            columns:[
              {data:"settore__articolo"}
              //{data:"tel"}
            ]
          });
      });
      return;
  };
  
  function GetList(name){
  $.post(
    "ricercaP",
     {data:name},
    function (result){
    var label = " ";
        for (i = 0; i < result.length; i++) {
                    label = label + '<tr>';
                    label = label + '<td>' + result[i].settore__articolo + '</td>';
                    //label = label + '<td>' + result[i].tel + '</td>';
                    label = label + '</tr>';
                }
                $("#tb1").html(label);
                $("#pr").html(result[0].tel);  //val(result[0].tel);
            });
    return;
};