

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#azienda").click(function(){
      var a=$("#azienda option:selected").text();
      Put(a);
    });
    $("#ct").click(function(){
      var r=$("#ct option:selected").text();
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
            "mp",
            { var: item,a2:"insert"},
            function (result) {
            var option=" ";
            var option1=" ";
            var option2=" ";
            var option3=" ";

            for (var i=0;i<result[0].prova.length;i++){
                    option += '<option value="'+ result[0].prova[i].regione+ '">' + result [0].prova[i].regione+ '</option>';
                }
            for (var i=0;i<result[0].ct.length;i++){
                option2 += '<option value="'+ result[0].ct[i].sito__citta+ '">' + result [0].ct[i].sito__citta+ '</option>';
            }
             for (var i=0;i<result.length;i++){
                option3 += '<option value="'+ result[i].settore__articolo+ '">' + result [i].settore__articolo+ '</option>';
            }
                $('#lsart').html(option3);
                $('#lsart').val(result[0].citta);
                $('#slc').val(result[0].settore__articolo);
                $('#cct').html(option2);
                $('#cct').val(result[0].citta);
                $('#ct').html(option);
                $('#ct').val(result[0].regione);
                $('#tel').val(result[0].tel);
                $('#email').val(result[0].email);
                $('#acq').val(result[0].acquisizione);
                $('#cap').val(result[0].capacita);
                $('#contatto').val(result[0].contatto);
                $('#trpag').val(result[0].trpag);
                $('#margine').val(result[0].margine);
                $('#fatturato').val(result[0].fatturato);
                $('#pi').val(result[0].pi);

            });
    return;
};

function PutCitta(item) {
    $.post(
            "mp",
            { var: item,a2:"regione"},
            function (result) {

         
            var option=" ";

            for (var i=0;i<result[0].ct.length;i++){
                option += '<option value="'+ result[0].ct[i].sito__citta+ '">' + result [0].ct[i].sito__citta+ '</option>';
            }
                $('#cct').html(option);
                $('#cct select').val(result[0].citta);
            });
    return;
};

function DelFornitore(item) {
    $.post(
            "fe",
            { var: item,a2:"insert"},
            function (result) {
            
                $('#citta').val(result[0].citta);
                $('#ct').val(result[0].regione);
                $('#slc').val(result[0].settore__articolo);
                $('#tel').val(result[0].tel);
                $('#email').val(result[0].email);
                $('#acq').val(result[0].acquisizione);
                $('#cap').val(result[0].capacita);
                $('#contatto').val(result[0].contatto);
                $('#trpag').val(result[0].trpag);
                $('#margine').val(result[0].margine);
                $('#fatturato').val(result[0].fatturato);
            });
    return;
};