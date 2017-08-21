
var UserTable=$("#mytable");
var TempUserTable=null;

var option=""
var optionValues=[];
$(document).ready(function(){
    $.ajaxSetup({cache:false});

    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01",//autoSize:true,appendText: "(yyyy-mm-dd)",// 
        onSelect: function (date) {
            GetTable(date);
                $("#tbf1").show();
        }
    });
    
    $("#tablef").on('click','a',function(){
        a=$(this).text();
        window.location.replace("fattura?nome="+a+"&azione=sps");
    });
    
});

//evidenzia tutte le righe della sospesa *1
//function GetTable(date){
    //$.post(
        //"sospesa",
        //{data:date,azione:"tabella"},
        //function(res){
            //var label="";
            //var sum=0
            //var before=" "
            //var prd=0;
            //for (i=0;i<res.length;i++){
                //if(res[i].fatturas!=before){
                    //if(i!=0)
                        //label=label + '<td>' + sum + '</td>';
                    //prd=parseFloat(res[i].prezzo)*parseFloat(res[i].q)
                    //sum=prd;                
                    //label=label + '<td><a href="#">' + res[i].fatturas + '</a></td>';
                    //label=label + '<td>' + res[i].cliente__azienda + '</td>';
                    //label=label + '<td>' + res[i].data + '</td>';

                //}
                //else{
                    //prd=parseFloat(res[i].prezzo)*parseFloat(res[i].q)
                    //sum=sum+prd;
                //}
                //before=res[i].fatturas;
            //}
            //$("#tb6").html(label);  
            //$("#idLKP").show();
        //});
        //return
//};
function GetTable(date){
    $.post(
        "sospesa",
        {data:date,cliente:" "},
        function(res){
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                label=label + '<td><a href="#">' + res[i].fatturas + '</a></td>';
                label=label + '<td>' + res[i].cliente__azienda + '</td>';
                label=label + '<td>' + res[i].valore+ '</td>';
                label=label + '<td>' +res[i].data + '</td>';
                label=label + '</tr>';
            }
            $("#tb6").html(label);  
            $("#idLKP").show();
        });
        return
};



