//3920656735
var option=""
var optionValues=[];
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#slc1").click(function(){
        $("#dt2").val("");
         $("#idLKP").hide();
        $("#cldt2").show();
        
//per la selezione dell'articolo***
    //var a=$("#slc1 option:selected").val();
    //Put(a);
//Fine

//    $('input[name="s2"]').val("");
//    $('#s3 option').text("");

    //var h=$('#s3 option').text();
    //for (i = 0; i < h.length; i++) {
        //optionValues[i]=h[i];
        //h[i]=""
        //}

//    $('#result').html(optionValues);
 //   $('#s2 option').val("");

    //var a=$( "#s3 option:selected" ).text();
    //alert(a)
    });

//per la selezione dell-articolo***
   //$("#slc2").click(function(){
 
       //// GetTable(a,b)
        //$("#dt2").val("");
        //$("#cldt2").show();
        //});
//Fine
    
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01",//autoSize:true,appendText: "(yyyy-mm-dd)",// 
        onSelect: function (date) {
            a=$("#slc1 option:selected").val();
          //  b=$("#slc2 option:selected").val();
            GetTable(a,date);
            //LightTd();
        }
    });
});

function LightTd(){
    var $a=$("#tb4 tr:last-child");
    var $b= $a.find("td:last");  //.css("font-size","30px");
    $b.css("font-size","30px");
};

function GetTable(pr,date){
    $.post(
        "lkprodotto",
        {prd:pr,data:date,s1:"table"},
        function(res){
            var arr=new Array();
            var label="";
            var sum=0
            for (i=0;i<res.length;i++){
                arr=""
                arr=(res[i].idcod__cod).split("-");
                sum=sum+parseFloat(res[i].q);
                label=label + '<tr>';
                label=label + '<td>' + arr[0] + '</td>';
                label=label + '<td>' + arr[2] + '</td>';
                label=label + '<td>' + res[i].q + '</td>';
                label=label + '<td>' + res[i].cassa + '</td>';
                label=label + '<td>' +res[i].bolla + '</td>';
                 label=label + '<td>' +res[i].data+ '</td>';
                label=label + '</tr>';
            }
            label=label + '<tr><td>TOT</td><td></td><td>'+sum+ '</td></tr>';
            $("#tb4").html(label);  
            $("#idLKP").show();
            var $a=$("#tb4 tr:last-child");
            var $b= $a.find("td:last");  //.css("font-size","30px");
            $b.css("color", "blue");
        });
        return
};


//per la selezione dell-articolo***
//function Put(item) {
    //$.post(
            //"lkprodotto",
            ////{ csrfmiddlewaretoken: "{{ csrf_token }}"},
            //{ var: item,s1:"insert"},
            //function (result) {
            ////var result= [1, 2, 3, 4, 5];
             //option="";
            //for (var i=0;i<result.length;i++){
                   //option += '<option value="'+ result[i].articolo+ '">' + result[i].articolo+ '</option>';
                 //}
                //$('#slc2').html(option);
            //});
    //return;
//};
