
$(document).ready(function(){
    $.ajaxSetup({cache:false});

    $("#clientes").click(function(){
        $("#tbf1").hide();
        var cl=$("#clientes").val()
        GetTable(cl);
        $("#tbf1").show();
    });
    
    
    $("#tablef").on('click','a',function(){
        a=$(this).text();
        window.location.replace("fattura?nome="+a+"&azione=sps");
    });
    
});

function GetTable(cl){
    $.post(
        "lksps",
        {cliente:cl},
        function(res){
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                label=label + '<td><a href="#">' + res[i].fatturas + '</a></td>';
                label=label + '<td>' + res[i].cliente__azienda + '</td>';
                label=label + '<td>' + res[i].valore+ '</td>';
                label=label + '<td>' +res[i].data + '</td>';
                label=label + '</tr>';
                before=res[i].fatturas;
            }
            $("#tb6").html(label);  
            $("#idLKP").show();
        });
        return
};




