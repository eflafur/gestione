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
        $("#tree1 ul:last-child").each(function(){
            $(this).find("li:last-child").each(function(){        
                $(this).css("font-size","20px");
            });
        });
        //$("#tree1 li:last-child").each(function(){
                //$(this).css("font-size","30px");
            //});   
    });
};

