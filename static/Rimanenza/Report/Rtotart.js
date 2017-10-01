//var UserTable=$("#mytable1");
//var TempUserTable=null;
var dt1="";
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#pf").hide();
    $("#btt").hide();
    $("#tbtart").hide();
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01", 
        onSelect: function (date) {
            dt1=date;
            $("#btt").show(); 
            $("#pf").hide();
         }
    });

    $("#btsps").click(function(){
            GetTotArt(0);
    });
    $("#btems").click(function(){
            GetTotArt(1);
    });
});

function GetBT(ctr){
    $.post(
        "rtotart",
        {data:dt1,tipo:ctr,azione:"tart"},
        function(ret){
            $("#pf").show();
            $("#btot").val(ret);  
        });
        return
};

function GetTotArt(ctr){
    $.post(
        "rtotart",
        {data:dt1,tipo:ctr,azione:"tart"},
        function(res){
            before="";
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                if(before!=res[i].frn)
                    label=label + '<td>' +res[i].frn+ '</td>';
                else
                    label=label + '<td></td>';
//                label=label + '<td><a href="#">' + res[i].ddt + '</a></td>';
                label=label + '<td>' + res[i].cod + '</td>';
                label=label + '<td>' +res[i].diff+ '</td>';
                label=label + '<td>' +res[i].diffcasse+ '</td>';
                label=label + '</tr>';
                before=res[i].frn;
            }
            $("#tbtart").show();
            $("#tbtart1").html(label);  
        });
        return
};






//function GetTotArt(date){
    //$.post(
        //"rtotart",
        //{data:date,azione:"tart"},
        //function(result){
          //if (TempUserTable!=null)
            //TempUserTable.destroy();
            //TempUserTable=UserTable.DataTable({
              //"ordering":false,
              //data:eval(result),
              //columns:[
                //{data:"cod"},
////                {data:"idcod__produttore__azienda"},
                //{data:"diff"},
              //]
            //});
        //});
        //return;
  //};
  
  
  
  
  