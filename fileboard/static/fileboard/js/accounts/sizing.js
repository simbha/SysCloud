function sizeEle() {
	var imgWidth = 0.15 * $(document).width();
	$("img").width(imgWidth);
	$("label").css("font-size", 0.03 * window.innerHeight);
	$("p").css("font-size", 0.03 * window.innerHeight);
	$("input").css("font-size", 0.02 * window.innerHeight);
	$("span").css("font-size", 0.02 * window.innerHeight);
}

$(document).ready(function() {
	$("body").hide();
	sizeEle();
	if($(".manage-accounts table tr").length == 1) {
		$(".manage-accounts input[type='button']").hide();
	}
	$("body").fadeIn();
});

$(window).resize(function() {
	sizeEle();
});