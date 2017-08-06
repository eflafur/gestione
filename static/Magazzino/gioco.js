$(document).ready(function(){
    $.ajaxSetup({cache:false});
       $("#reg").click(function(){
      var a=$("#reg option:selected").text();
     Put(a);
    });
    
          //  $('a[href]').hide();
            //$("div").css("font-size","10px");
            //$("#menu1 li:last-child").css("font-size","30px");
             //$("#menu1 li:nth-child(3)").css("font-size","30px");
             //$("ul#menu1 li:nth-last-child(3)").css("font-size","30px");
            //$("div:has(p)").css("font-size","40px");
            //$("p:contains('bello sopra')").css("font-size","40px");
            // $('p:not(.c1)').css("font-size","30px");   //funziona per tutti
            // $("#dv1").find('p').hide();
             // $("#reg").children().hide();
              //per ID e Class
             $(".li1").next().css("background-color", "blue");
            //$("#li1").next().css("background-color", "blue");
    //ritorna tutti gli elementi dello stesso livello ad esclusione dell'elemento corrente
          //  $(".li1").siblings().css("background-color", "blue");
    //funzione each
             //$(".li1").siblings().each(function(index){
                //Write(index);
             //});
              $("#menu2 li").each(function(index){
                Write(index);
             });
            });
          
function Write(index){
   label="ciccio della bruma lariolacci";
    if($(this).is('.ull')){
        $("#pp").val(label);
    }
    else { 
        $("#pp").val(index);
    }
};

function Read(){
    $.post(
        "entrata",
        {a2:$("#qnt").val(),a1:$("#codice").val(),a3:$("#bolla").val()},
    
    function (result){
        if(result==2){
            alert("duplcazione bolla")
        }
    });
        return;
};


function Put(item) {
    $.post(
            "produttore",
            //{ csrfmiddlewaretoken: "{{ csrf_token }}"},
            { vary: item,a2:"insert"},
            function (result) {
            var option=" ";
            for (var i=0;i<result.length;i++){
                    option += '<option value="'+ result[i].citta + '">' + result[i].citta  + '</option>';
                }
                $('#ct').html(option);
            });
    return;
};
