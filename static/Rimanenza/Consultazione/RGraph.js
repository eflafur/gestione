var node=" ";
var dd=0;
flag=$("#fl").text();

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#fl").hide();
    $("#go").click(function(){
        SetNode($("#peso").val());
    });
    if(flag=='m'){
        $("#ggraph").hide();
        GetGraph(flag);
    }
    else if(flag=='t'){
        $("#ggrapht").hide();
        GetGraph(flag);
    }
        
    $("#ggraph").click(function(){
        GetGraph('m');
        $("#ggraph").hide();
        $("#ggrapht").show();
    });
    $("#ggrapht").click(function(){
        GetGraph('t');
        $("#ggrapht").hide();
        $("#ggraph").show();
    });
});

function GetGraph(fl){
    if(dd!=0){
        $('#tree1').tree('destroy');
        window.location.replace("lkrgraph?opr="+fl)
    }
    dd=1;
    $.post(
        "lkrgraph",
        {act:"tree",flag:fl},
        function(res){
            var ls=[];
            var data=[];
            var c;
            data=JSON.parse(res);
            $('#tree1').tree({
                data: data,    
                autoOpen:true,
                closedIcon: '+',
                selectable: false
            });
        });
};


$('#tree1').bind(
    'tree.click',
    function(event) {
        node=" "
        mul=[];
        var nd = event.node;
        node = $('#tree1').tree('getNodeById', nd.id);
//        alert (node.name)
        mul=node.name.split(":")
        if (mul.length>=2){
            $("#peso").val(" ");
            $("#ps").show();
            $("#go").show();
            $("#peso").focus();
        }
        else{
            $("#peso").val(" ");
            $("#ps").hide();
            $("#go").hide();
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
 
 
 //$('#tree1').tree({
 //rtl: true
    ////onLoading:function (is_loading, node, $el){
        ////var a="ciao"
    ////}    
//});