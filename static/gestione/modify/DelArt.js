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
    
  $("#delart").click(function(){
    var a=$("#azienda option:selected").text();
    var b=$("#delart option:selected").text();
    Del(a,b);
    });
    
  });
  
  function GetList(name){
  $.post(
    "delart",
     {data:name,insert:"dlrt"},
    function (result){
    var label = " ";
    var option= " ";
     for (var i=0;i<result[0].length;i++){
                    option += '<option value="'+ result[0][i] + '">' + result[0][i]+ '</option>';
                }
            $('#delart').html(option);
        for (i = 0; i < result[1].length; i++) {
                    label = label + '<tr>';
                    label = label + '<td>' + result[1][i] + '</td>';
                    label = label + '</tr>';
                }
                $("#tb1").html(label);
        });
    return;
};

  function Del(azd,art){
  $.post(
    "delart",
     {azienda:azd,articolo:art,insert:"del"},
  function (result){
    var label = " ";
    var option= " ";
     for (var i=0;i<result[0].length;i++){
                    option += '<option value="'+ result[0][i]+ '">' + result[0][i]+ '</option>';
                }
            $('#delart').html(option);
        for (i = 0; i < result[1].length; i++) {
                    label = label + '<tr>';
                    label = label + '<td>' + result[1][i] + '</td>';
                    label = label + '</tr>';
                }
                $("#tb1").html(label);
            
           
        });
    return;
};