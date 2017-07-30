$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $('select').first().focus();
    $("#azienda").click(function(){
      var a=$("#azienda option:selected").text();
      Put(a);
    });
    $("#reg").click(function(){
      var r=$("#reg option:selected").text();
      if(r!="")
          PutCitta(r);
    });
 $("#aziendadel").click(function(){
      var r=$("#aziendadel option:selected").text();
      DelFornitore(r);
    });
});

function Put(item) {
    $.post(
            "modana",
            { var: item,a1:"insert"},
            function (result) {
            var option=" ";
            var option1=" ";
            var option2=" ";
            var option3=" ";
            for (var i=0;i<result[0].prova.length;i++){
                    option += '<option value="'+ result[0].prova[i].regione+ '">' + result [0].prova[i].regione+ '</option>';
                }
            for (var i=0;i<result[0].ct.length;i++){
                option1 += '<option value="'+ result[0].ct[i].sito__citta+ '">' + result [0].ct[i].sito__citta+ '</option>';
            }
                $('#ct').html(option1);
                $('#ct').val(result[0].citta);
                $('#reg').html(option);
                $('#reg').val(result[0].regione);
                $('#tel').val(result[0].tel);
                $('#email').val(result[0].email);
                $('#trpag').val(result[0].trpag);
                $('#indirizzo').val(result[0].indirizzo);
                $('#pi').val(result[0].pi);
            });
    return;
};

function PutCitta(item) {
    $.post(
            "modana",
            { var: item,a1:"regione"},
            function (result) {
            var option=" ";
            for (var i=0;i<result[0].ct.length;i++){
                option += '<option value="'+ result[0].ct[i].sito__citta+ '">' + result [0].ct[i].sito__citta+ '</option>';
            }
                $('#ct').html(option);
                $('#ct select').val(result[0].citta);
            });
    return;
};

function DelFornitore(item) {
    $.post(
            "delcliente",
            { var: item,a1:"insert"},
            function (result) {
                $('#ct').val(result[0].citta);
                $('#reg').val(result[0].regione);
                $('#tel').val(result[0].tel);
                $('#email').val(result[0].email);
                $('#trpag').val(result[0].trpag);
                $('#indirizzo').val(result[0].indirizzo);
                $('#pi').val(result[0].pi);
            });
    return;
};