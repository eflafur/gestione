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
        "rettifica",
        { res: item,a1:"js"},
        function (result) {

        $("#kg").val(result[0].q);
        $("#cdc").val(result[0].idcod__cod);
        $("#dt3").val(result[0].data);
    });
    return;
};
