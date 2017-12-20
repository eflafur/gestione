var res=[];
var dt1;
$(document).ready(function(){
    $.ajaxSetup({cache:false});
    $("#dtft").hide();
    $("#s1").hide();
    $("#s2").hide();
    $("#s3").hide();
    $("#dt2").datepicker({dateFormat:"yy-mm-dd",defaultDate:"2017-01-01", 
        onSelect: function (date) {
            dt1=date;
            GetBT(date,$("#bcodice option:selected").val());
         }
    });
    
    $("#bcodice").click(function(){
        $("#dt2").val(" ");
        $("#s1").hide();
        $("#s2").hide();
        $("#dtft").show();
    });
});

function Write(res,cod){
    if(cod==1){
        $("#s1").show();
        $("#rc").val(res[0]);
        $("#cst").val(res[1]);
        
        $("#clna").val(res[2]);
        $("#clnd").val(res[3]);
        $("#frna").val(res[4]);
        $("#frnd").val(res[5]);
        
        
        $("#slce").val((res[0]-res[1]).toFixed(2));
        $("#slsp").val((res[3]-res[2]).toFixed(2));
        $("#slsp1").val((res[4]-res[5]).toFixed(2));
    }
    else if(cod==2){
        $("#s2").show();
        $("#csa").val(res[0])
        $("#csd").val(res[1]);
        $("#bca").val(res[2]);
        $("#bcd").val(res[3]);
        $("#era").val(res[4]);
        $("#erd").val(res[5]);
        $("#slcs").val((res[1]-res[0]).toFixed(2));
        $("#slbn").val((res[3]-res[2]).toFixed(2));
        $("#sler").val((res[5]-res[4]).toFixed(2));
    }
};

function GetBT(data,cod){
    res.length=0;
    $.post(
        "rtot",
        {codcn:cod,datacn:data,azione:"cod"},
        function(ret){
            Write(ret,cod);            
        });
        return
};
