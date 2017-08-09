$(document).ready(function(){
    $.ajaxSetup({cache:false});
        $('input').first().focus();
        $("#acq").val("2000-01-01");
        $("#trpag").val("0");
        $("#fatturato").val("0");

    $("#reg").click(function(){
        a=$("#dl").val();
        if (a==""){
            alert("inserire CLiente")
            $("#dl").focus();
            return 
        }
      var a=$("#reg option:selected").text();
     Put(a);
    });
});

function Put(item) {
    $.post(
            "ca",
            //{ csrfmiddlewaretoken: "{{ csrf_token }}"},
            { vary: item,a1:"insert"},
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
                {data: "ruolo"},
                {data: "tipo" },
                {data  : "qualifica" }
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