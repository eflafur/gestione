$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#bla").focus();

     $("#bolla").keypress(function(){
        $("#cldt2").show();
    });
    
    $("#qnt").keypress(function(){
        $("#idLKP").show();
    });
    
     $("#codice").click(function(){
        var bl=$("#bolla").val();
        $("#bolla").attr("disabled",true);
        var qt=$("#qnt").val();
        $("#idLKP").hide();
        if(bl==""){
            alert("inserire bolla")
             $("#bolla").focus();
        }
        else if (qt==""){
            alert("inserire quanatita")
             $("#qnt").focus();
        }
        else 
            Read();   
            $("#qnt").val("");
            $("#idLKP").hide();
    });
    
     $("#btn2").click(function(){
        $("#bolla").val("");
        $("#qnt").val("");
        $("#bolla").attr("disabled",false);
        $("#cldt2").hide();
        $("#idLKP").hide();
        $("#codice option:eq(1)").selected();
     });
});

function Read(){
    $.post(
        "entrata",
        {a2:$("#qnt").val(),a1:$("#codice").val(),a3:$("#bolla").val()},
    
    function (result){
        //var arr= new Array();
        //if(result[1]==2){
            //var data=result[0]
            //arr=result[0].split('-');
            //lll=arr[0]
            //alert("duplcazione bolla per l'utente: " + arr[0])
        //}
    });
        return;
};



//$(document).ready(function(){
    //$.ajaxSetup({cache:false});
    //$("#codice").focus();
    //$("#codice").click(function(){
        //$("#cldt2").show();
        //$("#qnt").focus();
    //});
    //$("#qnt").keypress(function(){
        //$("#idLKP1").show();
    //});
    //$("#bolla").click(function(){
        //a=$("#qnt").val()
        //if(a==""){
            //alert("Inserire la Quantita'")
            //$("#idLKP1").hide();
            //$("#qnt").focus();
        //}
    //});

    //$("#bolla").keypress(function(){
        //$("#btn1").show();
    //});
    
    //$("#btn1").click(function(){
        //a=$("#qnt").val()
        //b=$("#bolla").val()
        //if(a==""){
            //alert("Inserire la Quantita'")
            //$("#idLKP1").hide();
            //$("#qnt").focus();
            //$("#btn1").hide();
        //}
       //else if(b==""){
            //alert("Inserire dati di Bolla'")
            //$("#btn1").hide();
            //$("#bolla").focus();
        //}
        //else if (b!=""){
            //Read();
                //$("#qnt").val("");
                //$("#bolla").val("");
                //$("#cldt2").hide();
                //$("#idLKP1").hide();
                //$("#btn1").hide();
                //$("#codice option:first").attr("selected", true);
        //}
        //return;
    //});
//});

//function Read(){
    //$.post(
        //"entrata",
        //{a2:$("#qnt").val(),a1:$("#codice").val(),a3:$("#bolla").val()},
    
    //function (result){
        //var arr= new Array();
        //if(result[1]==2){
            //var data=result[0]
            //arr=result[0].split('-');
            //lll=arr[0]
            //alert("duplcazione bolla per l'utente: " + arr[0])
        //}
    //});
        //return;
//};