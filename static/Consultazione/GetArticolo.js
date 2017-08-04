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
  
function GetList(name){
  $.post(
    "ricercaA",
    {data:name},
    function (result){
    if(result.length==0){
      label="";
      label = '<tr>';
      label = label + '<th>' + " " + '</th>';
      label = label + '<td>' + " " + '</td>';
      label = label + '<td>' + " "+ '</td>';
      label = label + '</tr>';
      $("#tb1").html(label);
      return
    }
    var count=0
    label="";
    label = '<tr>';
    label = label + '<th>' + result[0].produttore__azienda + '</th>';
    label = label + '<td>' + result[0].produttore__margine + '</td>';
    label = label + '<td>' + result[0].settore__articolo+ '</td>';

    for (i = 1; i < result.length; i++) {
      count=i
      if(result[i].produttore__azienda!=result[i-1].produttore__azienda){
      //  label = label + '<td>' + result[i-1].produttore__margine + '</td>';
        label = label + '</tr>';
        label = label + '<tr>';
        label = label + '<th>' + result[i].produttore__azienda + '</th>';
        label = label + '<td>' + result[i].produttore__margine + '</td>';
        label = label + '<td>' + result[i].settore__articolo + '</td>';
      }
      else if (result[i].settore__articolo!=result[i-1].settore__articolo){
        label = label + '<td>' + result[i].settore__articolo + '</td>';
      }
    }
   // label = label + '<td>' + result[count].produttore__margine + '</td>';
    label = label + '</tr>';
    $("#tb1").html(label);
            });
    return;
};

//function GetList(name){
  //$.post(
    //"ricercaA",
    //{data:name},
    //function (result){
    //var label = " ";
        //for (i = 0; i < result.length; i++) {
                    //label = label + '<tr>';
                    //label = label + '<td>' + result[i].produttore__azienda + '</td>';
                    //label = label + '</tr>';
                //}
                //$("#tb1").html(label);
            //});
    //return;
//};
  
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
  
 