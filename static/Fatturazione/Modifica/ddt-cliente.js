var UserTable=$("#tablef3");
var TempUserTable=null;
var x=0;
var sum=0;
var ar=[];
var choice="";
var ret="";
var x=0;
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#tt").hide();
    $("#tbf2").hide();
    $("#tbf3").hide();
    $("#pgm").hide();
    $("#btsel").hide();
    $("#chc").hide();
    $("#tott").hide();
    
     //var table = $('#tablef3').DataTable();
        //var value = $('.dataTables_filter input').val();
        //if (value.length==0) 
            //v=0;


//$("div.dataTables_filter input").keyup( function (e) {
    //if (e.keyCode == 13) {
        //oTable.fnFilter( this.value );
    //}
//} );


    $('#tablef3').on( 'search.dt', function () {
        var value = $('.dataTables_filter input').val();
        if(value.length==0 && x==0)
            GetDT(0);
        if (value.length!=0)
            OrderDT();
    });    

    $("#clientes").click(function(){
        ar.length=0;
        $("#tott").hide();
        $("#tt").hide();
        $("#btsel").hide();
        $("#btddt").hide();
        $("#tbf1").hide();
        $("#tbf2").hide();
        $("#pgm").show();
        GetTable($("#clientes option:selected").val());
    });
    
    $("#bttt").click(function(){
        ar.length=0;
        $("#tt").hide();
        $("#btsel").hide();
        $("#btddt").hide();
        $("#tbf1").hide();
        $("#tbf2").hide();
        GetDT(0);        
    });
   $("#pagam").click(function(){
        $("#btsel").show();
    });
    
    $("#chc").click(function(){
        choice=$("#chc :checked").val();
        $("#btsel").show();
        $("#btddt").show();
    });
    
   $("#btsel").click(function(){
        if($("#pagam").val()==0)
            $("#chc").show();
        else
            $("#btddt").show();
        $("#tt").show();
        $("#tot").attr("readonly",false);
        GetDdt();
    });

   $("#btddt").click(function(){
        SendDdt()
        $("#chc").hide();
        $("#pgm").hide();
        $("#tbddt").hide();
        $("#tbsel").hide();
    });
});




function GetTable(cl){
    $.post(
        "ddt",
        {cliente:cl,action:"tbl"},
        function(res){
           $("#tbf3").hide();
            var sum=0;
            if(res.length==0)
                return;
            var label="";
            for (i=0;i<res.length;i++){
               sum=sum+parseFloat(res[i].valore);
               label=label + '<tr>';
               if(cl!=0)
                   label=label + '<td><input type="checkbox" class="chc" value='+res[i].ddt+'></td>';
                else
                    label=label + '<td></td>';
               label=label + '<td>' + res[i].ddt + '</td>';
               label=label + '<td>' + res[i].cliente__azienda + '</td>';
               label=label + '<td>' + res[i].valore+ '</td>';
               label=label + '<td>' +res[i].data + '</td>';
               label=label + '</tr>';
               before=res[i].ddt;
           }
           $("#tb6").html(label);
           $("#totale").val(sum.toFixed(2));
           if(cl==0)
             $("#tott").show();
           $("#tbf1").show();

    });
   return
};

function GetDT(cl){
    $.post(
        "ddt",
        {cliente:cl,action:"tbl"},
        function(ress){
            ret=ress;
            var sum=0;
            if(ress.length==0)
                return;

        if (TempUserTable!=null)
          TempUserTable.destroy();
          TempUserTable=UserTable.DataTable({
    //        "searching": false,
            "ordering":true,
            data:eval(ress),
            columns:[
              {data:"ddt"},
              {data:"cliente__azienda"},
              {data:"valore"},
              {data:"data"}
              //{ render: function(data, type,row){
              //return row["valore"];}
              //}
            ]
        });
        var table = $('#tablef3').DataTable();
        t=table.column( 2 ).data().sum();
        $("#totale").val(t.toFixed(2));
        $("#pgm").hide();
        $("#tbf3").show();
        $("#tott").show()
//      return;
  });
  x=1;
  };

function OrderDT(){
    var t=0;
    $("#tb63 tr").each(function(){
         t=t+parseFloat($(this).find("td:eq(2)").text());
    });
    $("#totale").val(t.toFixed(2));
    $("#tott").show()
    x=0;
    return;


};
 
function GetDdt(){
    var t=0;
    var xx=0;
    sum=0;
    $("#tbf1 :checked").each(function(index){
        xx=index+1;
        ar[index]=$(this).val();
    });
    if(xx>0){
        $("#tb6 tr").each(function(){
             r=$(this).find("td:eq(1)").text();
             for (i=0;i<ar.length;i++){
                 if(r==ar[i]){
                     sum+=parseFloat($(this).find("td:eq(3)").text());
                     t=1
                     break;
                 }
                 continue;
             }
            if(t==0)
                 $(this).remove();
             t=0;
         });
    } 
    else {
        $("#tb6 tr").each(function(){
            ar.push($(this).find("td:eq(1)").text());
            sum+=parseFloat($(this).find("td:eq(3)").text());
         });
    }
    $("#tot").val(sum.toFixed(2));
    if($("#pagam").val()!=0)
        $("#tot").attr("readonly",true);
 };


function SendDdt(){
    var t=parseFloat($("#tot").val()).toFixed(2);
    var pg=$("#pagam").val();
    var sf=parseFloat(sum.toFixed(2));
    if(pg>0)
        t=0;
    else if(t>sf|| t<0){
        alert ("valore inammissibile")
        return 1;
    }
    else if(t<sf)
        pg=1
    $.post(
        "ddt",
        {ddt:JSON.stringify(ar),action:"ddt",cln:$("#clientes option:selected").val(),pgm:pg,tot:t,chc:choice},
        function(res){

        });
};
