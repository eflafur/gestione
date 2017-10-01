
var regione;
$(document).ready(function(){
    $.ajaxSetup({cache:false});
        regione=$("#reg option:selected").text();


        //$("#reg").click(function(){
            //opt=$("#reg option:selected").text();
            //Put(opt);
        //});


    //var num="380.24";    
    //var iNum = parseFloat(num);
    //var g=iNum;
    //var lnk="<a href='lkrgraph'> prova </a>"
    
    //$("#btl").click(function(){
            //citta=$("#ct option:selected").text();
////            alert (citta);
            //$("#reg option:selected").html(regione);
            //var aa=$(lnk);
            //$("#mio").text(aa);
        //});
        
          //  $('a[href]').hide();
            //$("div").css("font-size","10px");
 
 
             //$("#menu1 li:nth-child(3)").css("font-size","30px");
             //$("ul#menu1 li:nth-last-child(3)").css("font-size","30px");
            //$("div:has(p)").css("font-size","40px");
            //$("p:contains('bello sopra')").css("font-size","40px");
            // $('p:not(.c1)').css("font-size","30px");   //funziona per tutti
            // $("#dv1").find('p').hide();
             // $("#reg").children().hide();
              //per ID e Class
            // $(".li1").next().css("background-color", "blue");
            //$("#li1").next().css("background-color", "blue");
    //ritorna tutti gli elementi dello stesso livello ad esclusione dell'elemento corrente
          //  $(".li1").siblings().css("background-color", "blue");
    //funzione each
             //$(".li1").siblings().each(function(index){
                //Write(index);
             //});
 
                
                $('#idLKP11 tr').each(function() {
                    var customerId = $(this).find("td:first").html(); 
                    $("pp").val(customerId);
                    alert (customerId);
                });
                
                //LightTd();
                //LightLi();
                
                //$("#tb4 a").click(function(){
                    //o=$(this).text();   
                    //alert (o );
                //});
                
              
                  
                //$("#ulfb a").click(function(){
                //$('#tbfb').on('click','a',function(){
                    //o=$(this).text();
                    //alert (o );
                //});
                
                //$("#btl").click(function(){
                    //Test("ciao");
                //});
                
                  //$("#btadd").click(function(){
                    //Fill("ciao");
                    //res=$("#tbfb tr:first-child").next();
                    //res1=res.find("td").first();
                    //res1.css("background-color", "black");
                //});
                
                
                //var lnk="<a href='lkrgraph'>" + itemsc["idcod__specifica__nome"]+ "</a>"
                
                
                
                
            //var es=$("#menu2 ul");
                //$(es).each(function(){
                    //var g=$(this).children().find("li:last");
                    //g.css("color","yesllow");
            //});
            
            //$("#indice").children().css("color", "blue");
            
            //var es=$("#menu2 ul>li");"input"
           //var d=$(es).find("li:first-child").find("li").first();
           //// var  dd=$(es).children().find("li").first().next();//.find("li:eq(1)");//.children();//.find("li:first-child");
            //es.css("color","yellow");
            //$(d).each(function(index){
////                    $(this).text("pipo");
  ////                  alert($(this).text())
            //});
            
            //$("#btl").on(click,"td",function(){
                //$("#ct option").each(function(){
                        //var a=$(this).text();
                        //alert (a)
                //});
            //});


            //var a=$("#menu2").children();
                //$(a).each(function(){
                        //$(this).css("color","yellow");
            //}); 
 
        // $("#menu2 li").each(function(index){
              //alert(index);
         // });
         //$("#tbf1").show();
         //GetBolla();

    });
            

function GetBolla(){
    var label="";
            for (i=0;i<10;i++){
                label=label + '<tr>';
                label=label + '<td> io'+i+ '</td>';
                label=label + '<td> tu'+i+ '</td>';
                label=label + '<td> egli'+i+ '</td>';
                label=label + '<td> noi'+i+ '</td>';
                label=label + '<td> voi'+i+ '</td>';
                label=label + '<td> essi'+i+ '</td>';
                label=label + '</tr>';
            }
            $("#tb7").html(label);  
        return
};            
            

          
function Write(index){
   label="ciccio della bruma lariolacci";
    if($(this).is('.ull')){
        $("#pp").val(label);
    }
    else { 
        $("#pp").val(index);
    }
};            
            
            
function Test(el){
    var obj = jQuery.parseJSON( '[{ "name": "John","cod":"23" },{ "name": "pat","cod":"32" }]' );
   var a=obj[1].cod;
   var b=JSON.stringify(obj);
   
};            


function Fillul(res){
  var label="";
  label=label +'<ul>';
    for (i = 0; i < 3; i++) {
        label = label + '<li> aa'+i+' <a href="#"  >'+i+'</a> </li>';
    }
    label = label + '</ul>';
    $("#ulfb").html(label);  
    return;
};                        
            
            
        
function Fill(res){
  var label="";
    for (i = 0; i < 3; i++) {
        label = label + '<tr>';
        label = label + '<td> aa'+i+' </td>';
        label = label + '<td> bb'+i+' </td>';
        label = label + '<td> <a href="#" value="ded" ><p>'+i+'</p></a></td>';
        label = label + '</tr>';
    }
    $("#tbfb").html(label);  
    return;
};            
            

function LightTd(){
    var a=$("#mytable tr:nth-child(1)");
    var b=a.next('tr');
    var c= b.find("td:last");
    c.css("font-size","30px");
};          
function LightLi(){
    //var a=$("#menu2").children();
    //var b= a.find("li:not(.li1)");
    //b.css("font-size","30px");
    
    //var a=$("#menu2").children();
    //var b= a.find("ul:last-child");
    //var c=a.find("li:last-child");
    //var d=c.parent();
    //d.css("font-size","30px");
    
    var a=$("#menu2").children();
    var b= a.find("li:not(.li1)");
    var c=b.first();
    c.css("font-size","30px");
    
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
