var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function sizeEle() {
	var imgWidth = 0.15 * $(document).width();
	$("img").width(imgWidth);
	$("label").css("font-size", 0.03 * window.innerHeight);
	$("input").css("font-size", 0.02 * window.innerHeight);
	$("span").css("font-size", 0.02 * window.innerHeight);
}

$(document).ready(function() {
	$("body").hide();
	sizeEle();
	$("body").fadeIn();
	$(".acc-email").focus();
});

$(window).resize(function() {
	sizeEle();
});

$(function() {
	$(".acc-email").keyup(function() {
		$("#allow-skydrive .status").html("");
		var regex = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$|^([\w-\.]+@([\w-]+\.)+[\w-]{2}(\.)[\w-]{2})?$/;
		var input = $(this).val();
		if(input != "" && regex.test(input)) {
			$.post("/fileboard/accounts/exists", {account: $(".acc-email").val(), storageType: "skydrive"}, function(resp) {
				if(resp == "False")
					$(".access .acc-button").prop("disabled",false);
				else {
					$(".access .acc-button").prop("disabled",true);
					$("#allow-skydrive .status").css("color","red");
					$("#allow-skydrive .status").html("An account with this e-mail address already exists");
				}
			});
		} else {
			$(".access .acc-button").prop("disabled",true);
		}
	});
	
	$("#code").keyup(function() {
		var input = $(this).val();
		if(input != ""){
			$(".access #skydriveAccessToken").prop("disabled",false);
		} else {
			$(".access #skydriveAccessToken").prop("disabled",true);
		}
	});
});

$(function() {
	$(".acc-button").click(function(){
		$.post("/fileboard/getURL/skydrive", {account: $(".acc-email").val()}, function(resp) {
			var url = resp;
			popUp(url);
		});
	});
	
	$("#skydriveAccessToken").click(function() {
		var code = $("#code").val();
		if(code == "") {
			$("#allow-skydrive .status").css("color","red");
			$("#allow-skydrive .status").html("Please enter a valid authorization code");
		} else {
			$.post("/fileboard/getAccess/skydrive", {account: $(".acc-email").val(), code: $("#code").val()}, function(resp) {
				if(resp == "True") {
					$("#allow-skydrive .status").css("color","green");
					$("#allow-skydrive .status").html("Your SkyDrive account has been successfully set up!");
				} else if(resp == "False") {
					$("#allow-skydrive .status").css("color","red");
					$("#allow-skydrive .status").html("Please allow access to Syscloud and try again");
				}
			});
		}
	});
});

function popUp(url) {
	var windowFeatures = "resizable=yes,scrollbars=yes,status=yes,left=100,top=100,height=400,width=600";
	dropboxWindow = window.open(url,'Allow access to your SkyDrive',windowFeatures);
	if (window.focus) {
		dropboxWindow.focus()
	}
	return false;
}