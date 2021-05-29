function toggleBibtex(obj) { 
	console.log(obj.id);
	var id = obj.id;
	element = document.getElementById(obj.id)
	console.log(element);
	if (element.style.display == "none") {
		element.style.display="block";
	}
	else {
		element.style.display="none";
	} 
}
