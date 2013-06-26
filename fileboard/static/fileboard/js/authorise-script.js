$(document).ready(function() {
	$("#goto-fileboard").prop("disabled",true);
	$(".iframe").colorbox({
		iframe:true, 
		width:"80%", 
		height:"80%",
		onClosed: function() {
			$.post("fileboard/getAccess/dropbox", function(resp) {
				$("#goto-fileboard").prop("disabled",false);
			});
		}
	});
});

$("#goto-fileboard").click(function() {         
	window.location.replace("/fileboard/" + email + "/" + sessionKey);
});