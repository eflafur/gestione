
$(document).ready(function(){
  $.ajaxSetup({cache:false});

  $("#lgt").click(function(){
    Exit();
    });
  });
  
  function Exit(){
    $.post(
      "logout",
      //function(result){
        //if (TempUserTable!=null)
          //TempUserTable.destroy();
          //TempUserTable=UserTable.DataTable({
            //"ordering":false,
            //data:eval(result),
            //columns:[
              //{data:"produttore__azienda"}
            //]
          //});
      );
      return;
  };