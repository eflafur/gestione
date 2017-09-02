$(document).ready(function(){
    $.ajaxSetup({cache:false});
    
    $("#ggraph").click(function(){
        GetGraph();
    });
});


function GetGraph(){
    $.post(
    "ioio",
    function(res){
        var ls=[];
        var data=[];
        var c;
        data=JSON.parse(res);
        $('#tree1').tree({
            data: data,
            closedIcon: '+',
        });
    });
};