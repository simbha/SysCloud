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
		$("#allow-gdrive .status").html("");
		var regex = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$|^([\w-\.]+@([\w-]+\.)+[\w-]{2}(\.)[\w-]{2})?$/;
		var input = $(this).val();
		if(input != "" && regex.test(input)) {
			$.post("/fileboard/accounts/exists", {account: $(".acc-email").val(), storageType: "google-drive"}, function(resp) {
				if(resp == "False")
					$(".access .acc-button").prop("disabled",false);
				else {
					$(".access .acc-button").prop("disabled",true);
					$("#allow-gdrive .status").css("color","red");
					$("#allow-gdrive .status").html("An account with this e-mail address already exists");
				}
			});
		} else {
			$(".access .acc-button").prop("disabled",true);
		}
	});
	
	$("#code").keyup(function() {
		var input = $(this).val();
		if(input != ""){
			$(".access #gDriveCredentials").prop("disabled",false);
		} else {
			$(".access #gDriveCredentials").prop("disabled",true);
		}
	});
});

$(function() {
	$(".acc-button").click(function(){
		$.post("/fileboard/getURL/google-drive", {account: $(".acc-email").val()}, function(resp) {
			var url = resp;
			popUp(url);
		});
	});
	
	$("#gDriveCredentials").click(function() {
		var code = $("#code").val();
		if(code == "") {
			$("#allow-gdrive .status").css("color","red");
			$("#allow-gdrive .status").html("Please enter a valid verification code");
		} else {
			$.post("/fileboard/getAccess/google-drive", {account: $(".acc-email").val(), code: $("#code").val()}, function(resp) {
				if(resp == "True") {
					$("#allow-gdrive .status").css("color","green");
					$("#allow-gdrive .status").html("Your Google Drive account has been successfully set up!");
					if($("#goto-fileboard").prop("disabled")) {
						$("#goto-fileboard").prop("disabled",false);
					}
				} else if(resp == "False") {
					$("#allow-gdrive .status").css("color","red");
					$("#allow-gdrive .status").html("Please allow access to Syscloud and try again");
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