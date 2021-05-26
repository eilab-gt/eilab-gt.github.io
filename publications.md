---
layout: splash
title: Publications
classes: wide
---

<script type="text/javascript"> 
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
</script>

<style type="text/css">
  a:link, a:visited, a:hover, a:active {text-decoration: none;}
  .arxiv {
  	font-size: small;
  	background-color: red;
  	color: white;
  	border: 1px solid red;
  	text-decoration: none;
  	text-decoration-color: white;
  	border-radius: 1px;
  }
  .pdf {
  	font-size: small;
  	background-color: blue;
  	color: white;
  	border: 1px solid blue;
  	text-decoration: none;
  	text-decoration-color: black;
  	border-radius: 1px;
  }
  .journal {
  	font-size: small;
  	background-color: green;
  	color: white;
  	border: 1px solid green;
  	text-decoration: none;
  	text-decoration-color: white;
  	border-radius: 1px;
  }
  .conference {
  	font-size: small;
  	background-color: orange;
  	color: white;
  	border: 1px solid orange;
  	text-decoration: none;
  	text-decoration-color: white;
  	border-radius: 1px;
  }
  .workshop {
  	font-size: small;
  	background-color: purple;
  	color: white;
  	border: 1px solid purple;
  	text-decoration: none;
  	text-decoration-color: white;
  	border-radius: 1px;
  }
  .bibbutton {
  	font-size: small;
  	background-color: black;
  	color: white;
  	border: 1px solid black;
  	text-decoration: none;
  	text-decoration-color: white;
  	border-radius: 1px;
  }
  .bibtex {
  	white-space: pre-wrap;
  	font-size: small;
  	font-family: Courier;
  	background: #eeeeee;
  	border: 1px dotted black;
  	width: 75%;
  }
  .year {
  	font-size: xx-large;
  	font-weight: bold;
  	width: 100%;
  	border: 1px solid gray;
  	border-top-style: solid;
  	border-bottom-style: none;
  	border-left-style: none;
  	border-right-style: none;
  }
</style>

# Publications

{% assign years = "2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999" | split: ',' %}
{% for y in years %}
<div class="year">{{ y }}</div>
<p>
{% for x in site.data.pubs.entries %}
  {% if x.year == y %}
	  <p>
	  	{% for a in x.author %}
	  		{% if forloop.last == true and forloop.first == false %}and{% endif%} {{ a.first }} {{ a.middle }} {{ a.last }}{% if forloop.last == false and forloop.length > 2 %},{% endif %}
	  	{% endfor %}<br>
	    <b>{{ x.title }}</b><br>
	    <em>{{ x.journal }}{{ x.booktitle }} 
	    {{ x.volume }} 
	    ({{ x.year }})</em>.<br>
	    {% if x.url %}
	    	<a href="{{x.url}}">{% if x.url contains "arxiv" %}<span class="arxiv">arXiv</span>{% else %}<span class="pdf">PDF</span>{% endif %}</a>
	    {% endif %}
	    {% if x.journal and x.volume %}<span class="journal">Journal</span>{% endif %}
	    {% if x.booktitle %}{% if x.booktitle contains "Workshop" %}<span class="workshop">Workshop</span>{% else%}<span class="conference">Conference</span>{% endif %}{% endif %}
	    {% if x.bibtex %}
	    <a onclick="toggleBibtex({{ x.id }});"><span class="bibbutton">bibtex</span></a><br>
	    <div class="bibtex" id="{{ x.id }}" style="display: none;">{{ x.bibtex }}</div>
	    {% endif %}
	  </p>
  {% endif %}
{% endfor %}
</p>
{% endfor %}

