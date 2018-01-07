var UserTable=$("#tablef2");
var TempUserTable=null;

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#dtft").hide();
    $("#tbf1").hide();
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01", 
        onSelect: function (date) {
            dt1=date;
            GetBT(date,$("#bcodice option:selected").val());
         }
    });
    
    $("#bcodice").click(function(){
        $("#dt2").val(" ");
        $("#tbf1").hide();
        $("#dtft").show();
    });
});

function GetBT(data,cod){
    $.post(
        "fattmese",
        {},
        function(ret){
            Write(ret,cod);            
        });
        return
};

function Write(res,cod){
    var label="";
    var tot=0;
    var imp=0;
    var subtot=0,tot=0,subsaldo=0,totsaldo=0;
    var cliente="";
    var cliente1="";
    var dt=[];
    for (i=1;i<res.length;i++){
        if(cod==1)
            cliente1=res[i].nome
        else{
            dt= res[i].dtreg.split("-");
            cliente1=dt[2];
        }
        if(cliente1!=cliente && cliente!=""){
            label=label + '<tr style="color:Green">'
            label=label + '<td>' +"SubTotale"+'</td>';
            label=label + '<td></td><td>' + subtot.toFixed(2)+ '</td><td></td>';
            label=label + '<td></td><td>' + subsaldo+ '</td>';
            label=label + '</tr>';
            tot+=subtot
            totsaldo+=subsaldo
            subtot=0
            subsaldo=0
        }
        subtot+=parseFloat(res[i].tot)
        subsaldo+=parseFloat(res[i].saldo)
        label=label + '<tr>';
        label=label + '<td>' + res[i].dtreg+ '</td>';
        label=label + '<td>' + res[i].nome+ '</td>';
        label=label + '<td>' + res[i].tot+ '</td>';
        label=label + '<td>' +res[i].imp+ '</td>';
        label=label + '<td>' + res[i].erario+ '</td>';
        label=label + '<td>' +res[i].saldo+ '</td>';
        label=label + '</tr>';
        if(cod==1)
            cliente=res[i].nome
        else
            cliente=dt[2];
    }
    tot+=subtot;
    totsaldo+=subsaldo
    label=label + '<tr style="color:Green">'
    label=label + '<td>' +"SubTotale"+'</td>';
    label=label + '<td></td><td>' + subtot+ '</td><td></td>';
    label=label + '<td></td><td>' + subsaldo+ '</td>';
    label=label + '</tr>';
    label+='<tr style="background-color:Blue"><td>' +"Totale"+'</td><td></td><td>' + tot.toFixed(2)+ '</td><td></td><td></td><td>' + subsaldo+ '</td></tr>';
    $("#tbf1").show();
    $("#tb6").html(label);  
    return
};


 function WriteDt(result,cod){
     $("#tbf1").show();
        if (TempUserTable!=null)
          TempUserTable.destroy();
          TempUserTable=UserTable.DataTable({
            "ordering":true,
            data:eval(result),
            columns:[
              {data:"cliente__azienda"},
              {data:"attivo"},
              {data:"passivo"},
              { render: function(data, type, row){
                return row["attivo"]-row["passivo"];}
              }
            ]
        });
      return;
  };