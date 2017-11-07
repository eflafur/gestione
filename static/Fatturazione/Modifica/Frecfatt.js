
//var UserTable=$("#mytable");
//var TempUserTable=null;

var fatt=""
$(document).ready(function(){
    $.ajaxSetup({cache:false});

    $("#cln").click(function(){
        $("#tbf").hide();
        GetTable();
    });
    
    $("#tablef").on('click','a',function(){
        fatt=$(this).text();
        cl=$('#cln').val();
// funzione di reso tabellare
        GetFatt(fatt,cl);
//        window.location.replace("reso?nome="+a+"&cln="+cl);
    });
    
    $("#btrs").on('click',function(){
        LoopTable();
    });
});

function GetTable(){
    $.post(
        "recfatt",
        {cl:$("#cln").val(),action:"ga"},
        function(res){
            var label="";
            for (i=0;i<res.length;i++){
                label=label + '<tr>';
                label=label + '<td><a href="#">' + res[i].fattura + '</a></td>';
                label=label + '<td>' + res[i].cliente__azienda + '</td>';
                label=label + '<td>' + res[i].valore+ '</td>';
                label=label + '<td>' +res[i].data + '</td>';
                label=label + '</tr>';
            }
            $("#tbf1").show();
            $("#tb6").html(label);
            $("#idLKP").show();
        });
        return
};

// funzione di reso tabellare
function GetFatt(fatt,cl){
    $.post(
        "recfatt",
        {ft:fatt,cln:cl,action:"gf"},
        function(res){
            var label="";
            var sumf=0;
            for (i=0;i<res.length;i++){
                imp=res[i].prezzo*res[i].q*(parseFloat(res[i].idcod__genere__iva)+1)
                sumf=sumf+imp;
                label = label + '<tr>';
                label = label + '<td style="display: none">' + res[i].idcod__id+ '</td>';
                label = label + '<td>' + res[i].idcod__cod+ '</td>';
                label = label + '<td>' + res[i].q+ '</td>';
                label = label + '<td>'+ res[i].cassa+ '</td>';
                label = label + '<td>' + res[i].idcod__genere__iva+ '</td>';
                label = label + '<td>' + res[i].prezzo+ '</td>';
                label = label + '<td>' + imp+ '</td>';
                label = label + '<td>' + res[i].lotto+ '</td>';
                label = label + '<td><input type="text"  size="8"></td>';
                label = label + '</tr>';
            }
            label=label + '<tr><td>TOT</td><td></td><td></td><td></td><td></td><td>'+sumf.toFixed(2)+ '</td></tr>';
            $("#tbf1").hide();
            $("#tbf").show();
            $("#tbfb").html(label);
//            $("#tbfb tr:last").find("td:last").css("color","blue");
            return;
    });
};

function LoopTable(){
    var ls=[];
    $("#tbfb tr").each(function(){
        rs=$(this).find("input").val();
        if(rs!=null && rs!=" " ){
            var dc={};
            rsid=$(this).find("td:eq(0)").text();
            dc["id"]=rsid
            dc["rs"]=rs
            ls.push(dc);
        }
    });
    ret=JSON.stringify(ls);
    $.post(
        "recfatt",
        {rsls:ret,ft:fatt,action:"rs",cln:$("#cln").val()},
        function(res){
          
        });
};