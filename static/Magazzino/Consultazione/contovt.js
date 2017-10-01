var UserTable=$("#mytable");
var TempUserTable=null;

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#tbfcv1").hide();
    $("#btncvt").click(function(){
        GetBolla('p');
    });
    $("#btncvc").click(function(){
        $("#tbfcv1").hide();
        GetBolla('c');
    });
    $("#btnf").click(function(){
        $("#tbfcv1").hide();
        GetBolla('f');
    });

});


function GetBolla(x) {
   $.post(
      "cvt",
      {item:x},
      function(res){
        var label="";
        var k=0;
        var before="";
        $("#tbfcv1").show();
        for (i=0;i<res.length;i++){
            label=label + '<tr>';
            if( res[i].bolla!=before){
                label=label + '<td>'+res[i].bolla+'</td>';
            }
            else
                label=label + '<td></td>';
            label=label + '<td>' + res[i].idcod__cod+ '</td>';
            label=label + '<td>' + res[i].q+ '</td>';
            label=label + '<td>' + res[i].cassa + '</td>';
            label=label + '<td>' + res[i].cassaexit + '</td>';
            label=label + '<td>' + res[i].data+ '</td>';
            label=label + '</tr>';
            before=res[i].bolla;
        }
        $("#tbcv6").html(label);
        $("#tbcv6 tr:first").find("td:first").css("color","blue");
    });
        return
};

 //function GetBollaDt(){
    //$.post(
      //"cvt",
      //function(result){
        //if (TempUserTable!=null)
          //TempUserTable.destroy();
          //TempUserTable=UserTable.DataTable({
            //"ordering":false,
            //data:eval(result),
            //columns:[
              //{data:"bolla"},
              //{data:"idcod__cod"},
              //{data:"q"},
              //{data:"cassa"},
              //{data:"cassaexit"},
              //{data:"data"}
            //]
          //});
      //});
      //return;
  //};