var UserTable=$("#mytable");
var TempUserTable=null;

$(document).ready(function(){
  $.ajaxSetup({cache:false});
  $('select').focus();
  $("#btn").click(function(){
      $("#tb").show();
      $('select').focus();
    });
    $("#azienda").click(function(){
      console.log('doc ready');
      $("#tb").show().hide(10);
    });
  });
  
