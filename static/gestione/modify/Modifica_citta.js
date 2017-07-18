

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    
    $("#ct").click(function(){
      var a=$("#ct option:selected").text();
     Put(a);
    });
});

function Put(item) {
    $.post(
            "mp",
            { var: item,a2:"regione"},
            function (result) {

            //var result= [1, 2, 3, 4, 5];
            var option=" ";
 
            for (var i=0;i<result[0].ct.length;i++){
                option += '<option value="'+ result[0].ct[i].sito__citta+ '">' + result [0].ct[i].sito__citta+ '</option>';
            }
                $('#ct').html(option);
                $('#ct').val(result[0].sito__citta);
            });
    return;
};

function BonusData(item) {
    $.post(
            "produttore",
            //{ csrfmiddlewaretoken: "{{ csrf_token }}"},
            { var: item,var1:"insert"},
            function (result) {
                var label = " ";
                for (i = 0; i < result.length; i++) {
                    label = label + '<tr>';
                    label = label + '<td>' + result[i].ruolo + '</td>';
                    label = label + '<td>' + result[i].tipo + '</td>';
                    label = label + '<td>' + result[i].qualifica + '</td>';
                    label = label + '</tr>';
                }
                $("#tb1").html(label);
            });
            //});
    return;
};