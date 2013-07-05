function sizeEle() {
	var noOfRows = $("table tr").length;
	var noOfCols = $("table tr:first-child td").length;
	var tdWidth = (1/noOfCols) * $(document).width();
	$("table tr td").width(tdWidth);
	var divHeight = (1/noOfRows) * window.innerHeight;
	$("table tr td div").height(divHeight);
	var imgWidth = 0.25 * (1/noOfCols) * $(document).width();
	$("table tr td div img").width(imgWidth);
	$("table tr td div img").css("margin-left", tdWidth / 2);
	$("table tr td div img").css("margin-top", 0.2 * divHeight);
	$("table tr td div input").css("margin-left", 0.1 * tdWidth);
	$("table tr td div input").css("font-size", 0.04 * divHeight);
}

$(document).ready(function() {
	//resize all the elements on the page
	sizeEle();
});

$(window).resize(function(e) {
	sizeEle();
});

function hideAll() {
	hideBox();
	hideDropbox();
	hideGDrive();
	hideAmazon();
}

function hideDropbox() {
	$("#dropbox").animate({
		right: "-=500",
		top: "-=500"
	}, 1500);
}

function hideBox() {
	$("#box").animate({
		left: "-=500",
		top: "-=500"
	}, 1500);
}

function hideGDrive() {
	$("#google-drive").animate({
		left: "-=500",
		bottom: "-=500"
	}, 1500);
}

function hideAmazon() {
	$("#amazons3").animate({
		right: "-=500",
		bottom: "-=500"
	}, 1500);
}

$(function() {
	$(".palette input").click(function() {
		hideAll();
		
		var id = $(this).parent("div").prop("id");
		var action = $(this).prop("class");
		setTimeout(function() {
			window.location.replace("/fileboard/accounts/" + id + "/" + action);	
		}, 1500);
	});
});