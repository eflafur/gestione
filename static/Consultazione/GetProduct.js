var UserTable=$("#mytable");
var TempUserTable=null;

$(document).ready(function(){
  $.ajaxSetup({cache:false});
  $('select').focus();
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
  
  //function GetList(name){
  //$.post(
    //"ricercaP",
    //{data:name},
    //function (result){
 
    //label="";
    //label = '<tr>';
    //label = label + '<th>' + result[0].genere__nome + '</th>';


    //label1="";
    //label1 = '<tr>';
    //label1 = label1 + '<td>' + result[0].settore__articolo + '</td>';

    //for (i = 1; i < result.length; i++) {
      //if(result[i].genere__nome!=result[i-1].genere__nome){
      //label1 = label1 + '</tr>';
        //label1 = label1 + '<tr>';
        //label = label + '<th>' + result[i].genere__nome + '</th>';
        //label1 = label1 + '<td>' + result[i].settore__articolo + '</td>';
      //}
      //else if (result[i].settore__articolo!=result[i-1].settore__articolo){
        //label1 = label1 + '<td>' + result[i].settore__articolo + '</td>';
      //}
    //}
    //label = label + '</tr>';
    //$("#head").html(label);
    //label1 = label1 + '</tr>';
    //$("#tb1").html(label1);
            //});
    //return;
//};

  
  function GetList(name){
  $.post(
    "ricercaP",
    {data:name},
    function (result){
 
    label="";
    label = '<tr>';
    label = label + '<th>' + result[0].genere__nome + '</th>';
    label = label + '<td>' + result[0].settore__articolo+ '</td>';
    for (i = 1; i < result.length; i++) {
      if(result[i].genere__nome!=result[i-1].genere__nome){
      label = label + '</tr>';
        label = label + '<tr>';
        label = label + '<th>' + result[i].genere__nome + '</th>';
        label = label + '<td>' + result[i].settore__articolo + '</td>';
      }
      else if (result[i].settore__articolo!=result[i-1].settore__articolo){
        label = label + '<td>' + result[i].settore__articolo + '</td>';
      }
    }
    $('#pr').val(result[0].produttore__margine);
    label = label + '</tr>';
    $("#tt").html(label);
            });
    return;
};