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

//begin a fileboard session for a user
function beginSession() {
	setTimeout(function() {
		$.post("/fileboard/permissions", function(resp) {
			var permitted = resp;
			if(permitted == 'True') { //if access has been allowed to one or more cloud accounts
				window.location.replace("/fileboard");
			} else {
				window.location.replace("/fileboard/accounts");
			}
		});		
	}, 3000);
}

$(document).ready(function() {
	$("#loading").hide();
	$(".login").css("left","15%");
	$(".loginform").on("submit",function(event) {
		event.preventDefault();
		$("#invalid").html("");
		var email = $("#email").val();
		var password = $("#password").val();
		//authenticate the user for fileboard access
		$.post("/login/authorise",{email: email,password: password},function(resp) {
			$(".login").css("left","150%");
			$("#loading").show();
			//start a session for the logged in user
			if(resp == 'True')
				beginSession();
		}).fail(function(){
			$("#invalid").html("The email ID or password you entered is incorrect.");
		});
	});
});

