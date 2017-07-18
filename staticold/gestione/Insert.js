

$(document).ready(function(){
    $.ajaxSetup({cache:false});
    
    $("#reg").click(function(){
      var a=$("#reg option:selected").text();
    //var a=$("#a5").html();
     Put(a);
    });
});


function BonusLevel(data1) {
    $.post(
    "GetOfferta",
    { date: data1 },
    function (result) {

        if (AdvisorUserTable != null)
            AdvisorUserTable.destroy();
            AdvisorUserTable = UserTable.DataTable({
            "ordering": false,
            data: eval(result),
            columns: [
                //{data: "azienda__offerta__ruolo"},
                //{data: "azienda__offerta__level__qualifica"},
                {data: "ruolo"},
                {data: "tipo" },
                {data  : "qualifica" }
                //{data  : "azienda__azienda" },
                //{data : "azienda__general__settore"},
                //{data : "level__qualifica"}
            ]
        });
    });
    return;
};

function Put(item) {
    $.post(
            "produttore",
            //{ csrfmiddlewaretoken: "{{ csrf_token }}"},
            { var: item,a2:"insert"},
            function (result) {
            //var result= [1, 2, 3, 4, 5];
            var option=" ";
            for (var i=0;i<result.length;i++){
                    option += '<option value="'+ result[i].citta + '">' + result[i].citta  + '</option>';
                }
                $('#ct').html(option);
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