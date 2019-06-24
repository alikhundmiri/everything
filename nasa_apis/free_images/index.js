const api_request = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY";

/* API REQUESTS*/
fetch(api_request)
.then(resp => resp.json())
.then(function(data){
	/* FETCH THE JSON DATA*/
	let image_title = data.title;
	let image_url = data.url;
	let image_explain = data.explanation;

	/* CHANGE THE TITLE, BACKGROUND IMAGE, AND EXPLANATION*/
	document.getElementById("imageTitle").innerHTML = image_title;
	document.body.style.backgroundImage = "url('" + image_url + "')";
	document.getElementById("imageExplanation").innerHTML = image_explain;
	/* EXIT*/
})