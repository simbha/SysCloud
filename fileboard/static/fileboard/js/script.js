$(document).ready(function() {
	$("body").hide();
	$("body").fadeIn();
	var boardHeight = $(".board").height();
	var tdHeight = (0.8 * boardHeight) / 2;
	var tdCount = $(".board .files td").length;
	var tdPerRow = Math.ceil(tdCount / 2);
	tdWidth = 100 / tdPerRow;
	$(".board .files td").css("height",tdHeight);
	$(".board .files td").css("width",tdWidth);
	$(".board .files td div").css("height",tdHeight);
	var filesHeight = $(".board .files").height();
	$(".board .files").css("margin-top", (boardHeight - filesHeight) / 2);
	$(".board .files td div img").css("height", tdHeight / 2);
	$(".board .files td div label").css("font-size", 0.1 * tdHeight);
});

$(window).resize(function(e) {
	var boardHeight = $(".board").height();
	var tdHeight = (0.8 * boardHeight) / 2;
	var tdCount = $(".board .files td").length;
	var tdPerRow = Math.ceil(tdCount / 2);
	tdWidth = 100 / tdPerRow;
	$(".board .files td").css("height",tdHeight);
	$(".board .files td").css("width",tdWidth);
	$(".board .files td div").css("height",tdHeight);
	var filesHeight = $(".board .files").height();
	$(".board .files").css("margin-top", (boardHeight - filesHeight) / 2);
	$(".board .files td div img").css("height", tdHeight / 2);
	$(".board .files td div label").css("font-size", 0.1 * tdHeight);
});