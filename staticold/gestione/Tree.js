
var label = " ";
label = label + '<tr>';

$(document).ready(function(){
  $.ajaxSetup({cache:false});

  $("#bt1").click(function(){
    CreateTree();
  });
});

function CreateTree(){
    $.post(
    "tree",
    function (result) {
        Design(result)
    $("#tb1").html(label);
    
    
        //$('#tree1').tree({
            //data: res
        //});
    });
    };
    
    function Design(result){
        label = label + '<td>' + result.name + '</td>';
        for (i = 0; i < result.children.length; i++) {
            Design(result.children[i])
        }
        return
    };
    


  