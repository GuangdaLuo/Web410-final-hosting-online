$(document).ready(function() {
	console.log("search");

	$('#search_btn').click(function() {
		$keyword = $('#search').val()
		console.log("keyword = " + $keyword);
		$(location).attr('href', 'http://localhost/interested_activity.html' + '?keyword=' + $keyword)
	})

});


// function get_activities(keyword) {
// 	console.log("go to see intersted activities");
// 	$(location).attr('href', 'http://localhost/interested_activity.html' + '?keyword=' + keyword)
// 	//window.location.replace("http://stackoverflow.com");
// }