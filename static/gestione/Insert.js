$(document).ready(function(){
    $.ajaxSetup({cache:false});
        $("#sl").hide();
        $('input').first().focus();
        $("#acq").val("2000-01-01");
        $("#trpag").val("0");
        $("#margine").val("0");
        $("#fatturato").val("0");
        $("#dl").focusout(function(){
        var str = $("#dl").val().replace(/\s+/g, '');
            $("#sl option").each(function(){
                if(str==$(this).val()){
                    alert("Nominativo già presente");
                    $("#dl").val(" ")
                }
            });
        });
    $("#reg").click(function(){
      var a=$("#reg option:selected").text();
     Put(a);
    });
});

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