$(document).ready(function(){

	$(".shared-task").hide();
	$("#task-response").fadeOut(5000);

    $("#dashboard-task").click(function(){
    	$(".dashboard-task").show();
        $(".shared-task").hide();
    });

    $("#shared-task").click(function(){
        $(".dashboard-task").hide();
        $(".shared-task").show();
    });
});
