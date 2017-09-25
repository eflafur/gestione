var option=""
var optionValues=[];
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#tx1").hide();
    $("#slc1").click(function(){
    //$('input[name="ss2"]').val("");
    //$('#ss2 option').text("");

    //var h=$('#ss2 option').text();
    //for (i = 0; i < h.length; i++) {
        //optionValues[i]=h[i];
        //h[i]=""
    //}
//    $('#result').html(optionValues);
//    $('#ss2 option').val("");
    var a=$("#slc1 option:selected").val();
    $("#tx1").show();
    Put(a);
    });
});

function Put(item) {
    $.post(
            "articolo",
            //{ csrfmiddlewaretoken: "{{ csrf_token }}"},
            { var: item,s1:"insert"},
            function (result) {
             option="";
            for (var i=0;i<result.length;i++){
                   option += '<option value="'+ result[i].articolo+ '">' + result[i].articolo+ '</option>';
            }
                $('#ss2').html(option);
            });
    return;
};
