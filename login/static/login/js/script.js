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

$(document).ready(function() {
	$(".login").css("left","15%");
	$(".loginform").on("submit",function(event) {
		event.preventDefault();
		$("#invalid").html("");
		var email = $("#email").val();
		var password = $("#password").val();
		$.post("/login/authorise/",{email: email,password: password},function(resp) {
			$(".login").css("left","150%");
		}).fail(function(){
			$("#invalid").html("The email ID or password you entered is incorrect.");
		});
	});
});

