var node=" ";
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#go").hide();
    $("#ggraph").click(function(){
        GetGraph();
    });
    $("#go").click(function(){
        var q=$("#peso").val();
        SetNode(q);
    });
});

function GetGraph(){
    $.post(
        "lkrgraph",
        {act:"tree"},
        function(res){
            var ls=[];
            var data=[];
            var c;
            data=JSON.parse(res);
            $('#tree1').tree({
                data: data,    
                autoOpen:2,
                closedIcon: '+',
                selectable: false
            });
        });
};


$('#tree1').bind(
    'tree.click',
    function(event) {
        mul=[];
        var nd = event.node;
        node = $('#tree1').tree('getNodeById', nd.id);
        alert (node.name)
        mul=node.name.split(":")
        if (mul.length==2){
            $("#peso").val(" ");
            $("#ps").show();
            $("#go").show();
            $("#ggraph").hide();
            $("#peso").focus();
        }
        else{
            $("#peso").val(" ");
            $("#ps").hide();
            $("#go").hide();
            $("#ggraph").hide();
        }
});

function SetNode(q){
    var arr= new Array();
    arr=node.name.split(':');
    $.post(
        "lkrgraph",
        {node:node.id,peso:q,act:"set"},
        function(res){
        
        });
    updateNode(arr[0],q)
        $("#ps").hide();
        $("#go").hide();
};
 
 function updateNode(cod,p){
    var name=cod+"  :  "+p;
    $('#tree1').tree('updateNode', node, name);
    return
 };