$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#bolla").click(function(){
        var a=$("#bolla option:selected").text();
        $("#cldt2").show();
        $("#idLKP1").show();
        $("#idLKP2").show();
        $("#btn1").show();
        Put(a);
    });
});

function Put(item) {
    $.post(
        "elimina",
        { a1: item,a2:"js"},
        function (result) {
        //$("#tbf1").show();
            //Write(result)
    });
    return;
};

function Write(res) {
    var label="";
    for (i=0;i<res.length;i++){
        label=label + '<tr>';
        label=label + '<td>' +res[i].idcod__cod+ '</td>';
        label=label + '<td>' + res[i].q+ '</td>';
        label=label + '<td>' + res[i].cassa+ '</td>';
        label=label + '<td>' + res[i].data+ '</td>';
        label=label + '</tr>';
    }
    $("#tb6").html(label);
    return
};