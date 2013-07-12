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
		$("#allow-dropbox .status").html("");
		var regex = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$|^([\w-\.]+@([\w-]+\.)+[\w-]{2}(\.)[\w-]{2})?$/;
		var input = $(this).val();
		if(input != "" && regex.test(input)) {
			$.post("/fileboard/accounts/exists", {account: $(".acc-email").val(), storageType: "dropbox"}, function(resp) {
				if(resp == "False")
					$(".access .acc-button").prop("disabled",false);
				else {
					$(".access .acc-button").prop("disabled",true);
					$("#allow-dropbox .status").css("color","red");
					$("#allow-dropbox .status").html("An account with this e-mail address already exists");
				}
			});
		} else {
			$(".access .acc-button").prop("disabled",true);
		}
	});
	
	$("#code").keyup(function() {
		var input = $(this).val();
		if(input != ""){
			$(".access #dropboxAccessToken").prop("disabled",false);
		} else {
			$(".access #dropboxAccessToken").prop("disabled",true);
		}
	});
});

$(function() {
	$(".acc-button").click(function(){
		$.post("/fileboard/getURL/dropbox", {account: $(".acc-email").val()}, function(resp) {
			var url = resp;
			popUp(url);
		});
	});
	
	$("#dropboxAccessToken").click(function() {
		var code = $("#code").val();
		if(code == "") {
			$("#allow-dropbox .status").css("color","red");
			$("#allow-dropbox .status").html("Please enter a valid authorization code");
		} else {
			$.post("/fileboard/getAccess/dropbox", {account: $(".acc-email").val(), code: $("#code").val()}, function(resp) {
				if(resp == "True") {
					$("#allow-dropbox .status").css("color","green");
					$("#allow-dropbox .status").html("Your Dropbox account has been successfully set up!");
				} else if(resp == "False") {
					$("#allow-dropbox .status").css("color","red");
					$("#allow-dropbox .status").html("Please allow access to Syscloud and try again");
				}
			});
		}
	});
});

function popUp(url) {
	var windowFeatures = "resizable=yes,scrollbars=yes,status=yes,left=100,top=100,height=400,width=600";
	dropboxWindow = window.open(url,'Allow access to your Dropbox',windowFeatures);
	if (window.focus) {
		dropboxWindow.focus()
	}
	return false;
}