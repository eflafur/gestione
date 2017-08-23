var UserTable=$("#mytable");
var TempUserTable=null;

$(document).ready(function(){
  $.ajaxSetup({cache:false});
   $('select').first().focus();
  $("#catls").text("");
  
  $("#azienda").click(function(){
     $('select').first().focus();
    var a=$("#azienda option:selected").text();
    GetGenere(a)
      $("#caddgen").show();
      $("#caddart").hide();
      $("#caddcat").hide();
      $("#btn1").hide();
    });

  $("#gen").click(function(){
    var b=$("#gen option:selected").text();
    GetSettore(b);
    $("#caddart").show();
    $("#caddcat").hide();
    $("#btn1").hide();

  });

 $("#art").click(function(){
    var a=$("#art option:selected").text();
    GetSpec(a);
    $("#caddcat").show();
    $("#btn1").show();
  });
  });
  
  function GetGenere(name){
  $.post(
    "addart",
     {azienda:name,a2:"genere"},
    function (result){
      var option= " ";
      for (var i=0;i<result.length;i++){
        option += '<option value="'+ result[i]["nome"]+ '">' + result[i]["nome"]+ '</option>';
        }
        $('#gen').html(option);
        //for (i = 0; i < result[1].length; i++) {
            //label = label + '<tr>';
            //label = label + '<td>' + result[i]["nome"] + '</td>';
            //label = label + '</tr>';
          //}
          //$("#tb1").html(label);
         });
         return;
};

 function GetSettore(art){
  $.post(
    "addart",
     {genere:art,a2:"settore"},
    function (result){
      var label = " ";
      var option= " ";
      for (var i=0;i<result.length;i++){
        option += '<option value="'+ result[i]["articolo"]+ '">' + result[i]["articolo"]+ '</option>';
        }
        $('#art').html(option);
        //for (i = 0; i < result[1].length; i++) {
            //label = label + '<tr>';
            //label = label + '<td>' + result[i]["articolo"] + '</td>';
            //label = label + '</tr>';
          //}
          //$("#tb1").html(label);
        });
         return;
};

function GetSpec(art){
  $.post(
    "addart",
     {articolo:art,a2:"spec"},
    function (result){
      var label1 = " ";
      for (var i=0;i<result.length;i++){
        label1 += '<option value="'+ result[i].nome+ '">' + result[i].nome+ '</option>';
        }
        $('#catls').html(label1);
         });
         return;
};

  
  function GetList(name){
  $.post(
    "addart",
     {data:name,insert:"prdc"},
    function (result){
      var label = " ";
      var option= " ";
      for (var i=0;i<result[0].length;i++){
        option += '<option value="'+ result[0][i]+ '">' + result[0][i]+ '</option>';
        }
        $('#art').html(option);
        //for (i = 0; i < result[1].length; i++) {
            //label = label + '<tr>';
            //label = label + '<td>' + result[1][i] + '</td>';
            //label = label + '</tr>';
          //}
          //$("#tb1").html(label);
         });
         return;
};

  function Add(azd,art){
  $.post(
    "addart",
     {azienda:azd,articolo:art,insert:"add"},
  function (result){
    var label = " ";
    var option= " ";
     for (var i=0;i<result[0].length;i++){
                    option += '<option value="'+ result[0][i]+ '">' + result[0][i]+ '</option>';
                }
            $('#gen').html(option);
        //for (i = 0; i < result[1].length; i++) {
                    //label = label + '<tr>';
                    //label = label + '<td>' + result[1][i] + '</td>';
                    //label = label + '</tr>';
                //}
                //$("#tb1").html(label);
        });
    return;
};