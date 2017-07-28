var UserTable=$("#mytable");
var TempUserTable=null;

$(document).ready(function(){
  $.ajaxSetup({cache:false});
  $("#azienda").click(function(){
    var a=$("#azienda option:selected").text();
    
    GetList(a);
      $("#caddart").show();
      $("#caddart1").show();
      $("#idLKP1").show();
    });

    
  $("#slc").click(function(){
    var a=$("#azienda option:selected").text();
    var b=$("#slc option:selected").text();
    Add(a,b);
    });
    
  });
  
  function GetList(name){
  $.post(
    "addart",
     {data:name,insert:"prdc"},
    function (result){
      var label = " ";
      var option= " ";
      for (var i=0;i<result[0].length;i++){
        option += '<option value="'+ result[0][i]+ '">' + result[0][i]+ '</option>';
        }
        $('#slc').html(option);
        for (i = 0; i < result[1].length; i++) {
            label = label + '<tr>';
            label = label + '<td>' + result[1][i] + '</td>';
            label = label + '</tr>';
          }
          $("#tb1").html(label);
         });

         return;
};

  function Add(azd,art){
  $.post(
    "addart",
     {azienda:azd,articolo:art,insert:"add"},
  function (result){
    var label = " ";
    var option= " ";
     for (var i=0;i<result[0].length;i++){
                    option += '<option value="'+ result[0][i]+ '">' + result[0][i]+ '</option>';
                }
            $('#slc').html(option);
        for (i = 0; i < result[1].length; i++) {
                    label = label + '<tr>';
                    label = label + '<td>' + result[1][i] + '</td>';
                    label = label + '</tr>';
                }
                $("#tb1").html(label);
            
           
        });
    return;
};