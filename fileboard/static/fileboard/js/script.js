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

function resize() {
	var headerHeight = $(".header").height();
	$(".header .user").css("font-size", 0.1 * headerHeight);
	$(".header .list").css("font-size", 0.2 * headerHeight);
	$(".header .list img").height(0.2 * headerHeight);
	var boardHeight = $(".board").height();
	$(".board .files").height(0.9 * boardHeight);
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
	$(".board .files td div img[alt='skydrive']").css("height", tdHeight / 3);
	$(".board .files td div img[alt='amazons3']").css("height", tdHeight / 3);
	$(".board .files td div label").css("font-size", 0.1 * tdHeight);
	if($(".board .files tr").length <= 2) {
		$(".board .files").css("overflow-y","hidden");
	} else {
		$(".board .files").css("overflow-y","scroll");
	}
}

function loadTemplate(context, link) {
	$.post("/fileboard/files", context, function(template) {
		$(".board").html(template);
		if(link)
			$(".list").append(" <span>></span> <a>" + link + "</a>");
		resize();
	});	
}

$(document).ready(function() {
	$("body").hide();
	$("body").fadeIn();
	loadTemplate();
});

$(window).resize(function(e) {
	resize();
});

$(function() {
	$(".board").on("click", $(".files td div"), function(e) {
		link = $(e.target).children("label").text();
		account_type = $(e.target).prop("id");
		len = $(".list a").length;
		if(len > 2) {
			account = $(".list a:eq(2)").text();
			context = {account_type: account_type, account: account, folder_name: link};
		} else {
			context = {account_type: account_type, account: link};
		}
		
		loadTemplate(context, link);
	});
	
	$(".header .list").on("click", $("a"), function(e) {
		if($(e.target).index() == $(".header .list").children("a").length + $(".header .list").children("span").length) {
			e.preventDefault();
		} else {
			var index = $(e.target).index();
			if(index == 1) {
				loadTemplate();
			}
			else if(index == 3) {
				account_type = ($(e.target).text()).toLowerCase();
				context = {account_type: account_type};
				loadTemplate(context);
			} else if(index == 5) {
				account_type = ($(".header .list a:eq(1)").text()).toLowerCase();
				account = $(e.target).text();
				context = {account_type: account_type, account: account};
				loadTemplate(context);
			} else if(index > 5){
				account_type = ($(".header .list a:eq(1)").text()).toLowerCase();
				account = ($(".header .list a:eq(2)").text()).toLowerCase();
				folder_name = $(e.target).text();
				context = {account_type: account_type, account: account, folder_name: folder_name};
				loadTemplate(context);
			}
			$(e.target).nextAll().remove();
		}
	});
});

