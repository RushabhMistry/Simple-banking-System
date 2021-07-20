$().ready(function() {
    var drBalance = 0;
    var today = new Date();
    var date = today.getDate() + '/' + (today.getMonth()+1) + '/'+ today.getFullYear();
    document.getElementById("currentDate").value = date;
    $("body").on("change", "#crName", function(){
        //console.log("ID=",$(this).val());
        $("#crId").val($(this).val());
    });
    $(".td-btn").on("click", function() {
        $("#txnContainer").show();
        $("#crId").val("");
        var drName = $(this).text();
        var drId = $($(this).parent().children()[0]).text();
        drBalance = Number($($(this).parent().children()[3]).text());
        $("#drName").val(drName);
        $("#drId").val(drId);
        var tbody = $(this).parent().parent();
        console.log("tbody=",tbody)
        $("#crName").empty();
        $("#crName").append("<option value='0' disabled selected>Select name...</option>");
        $(tbody).children().each(function(id, tr){
            console.log("tr=",tr);
            var crid = $($(tr).children()[0]).text();
            var cname = $($(tr).children()[1]).text();
            if(cname!=drName) {
                $("#crName").append("<option value='"+crid+"'>"+cname+"</option>");
            }
        });
        $("body").css({
            "overflow-y": "hidden"
        });
    });
    $("body").on("click", "#submit", function(){
        var amt = Number($("#amount").val());
        if(amt<=drBalance){
            alert("Transaction successful.");
            document.getElementById("myForm").submit();
            // console.log("submitting...");
            
        }else{
            alert("Your amount must not be greater than available balance.");
        }
        // $.ajax({
        //     type : "POST", 
        //     url: "{% url 'ajax_posting' %}",
        //     data: {
        //         amt: Number($("#amount").val()),
        //         bal: Number($("#drBalance").val()),
        //         csrfmiddlewaretoken: '{{ csrf_token }}',
        //         dataType: "json",
     
        //     },
            
        //     success: function(data){
        //        $('#output').html(data.msg);
        //     },
     
        //     failure: function() {
                
        //     }
        // });
    });
    $("#cancel").on("click", function() {
        $("#txnContainer").hide();
        $("body").css({
            "overflow-y": "auto"
        });
    })
});
