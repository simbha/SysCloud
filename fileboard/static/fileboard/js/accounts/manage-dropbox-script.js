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

$(function() {
	
	$("#delete").click(function() {
		$.post("/fileboard/accounts/dropbox/delete", {id: $(".account-list table input:checked").prop("id")}, function(resp) {
			if(resp) {
				var accountName = $(".account-list table input:checked").parent("td").next().children("label").text();
				var account = $(".account-list table input:checked").parent("td").parent("tr");
				account.remove();
				$(".manage-accounts .status").css("color","green");
				$(".manage-accounts .status").html("The dropbox account " + accountName + " has been deleted");
				var accountListLength = $(".account-list table tr").length;
				if(accountListLength == 1) {
					$(".account-list table").remove();
					$(".account-list").append("<p>No accounts have been configured for Dropbox</p>");
					$(".account-list").append("<span>To configure a new account, go back to the account palette and click on Add New Account for Dropbox</span>");
					$(".manage-accounts input[type='button']").hide();
					sizeEle();
				}
			}
		});
	});
	
	$("#disallow").click(function() {
		$.post("/fileboard/removeAccess/dropbox",
		{id: $(".account-list table input:checked").prop("id")},
		function(resp) {
			if(resp) {
				$("#disallow").prop("disabled", true);
				var access = $(".account-list table input:checked").parent("td").next().next().children("label");
				access.prop("class","False");
				access.text("False");
				var account = $(".account-list table input:checked").parent("td").next().children("label").text();
				$(".manage-accounts .status").css("color","green");
				$(".manage-accounts .status").html("The access token for " + account + " has been destroyed");
			}
		});
	});
	
	$(".account-list table input[type='radio']").click(function() {
		$("#delete").prop("disabled", false);
		var access = $(this).parent("td").next().next().children("label").text();
		if(access == "True") {
			$("#disallow").prop("disabled", false);
		}
	});
});