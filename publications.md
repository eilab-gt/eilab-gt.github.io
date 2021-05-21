---
layout: single
title: Publications
classes: wide
---

<style type="text/css">
  .arxiv {
  	font-size: small;
  	background-color: red;
  	color: white;
  	border: 1px solid black;
  	text-decoration: none;
  	text-decoration-color: white;
  }
  .pdf {
  	font-size: small;
  	background-color: blue;
  	color: white;
  	border: 1px solid black;
  	text-decoration: none;
  	text-decoration-color: black;
  }
  .journal {
  	font-size: small;
  	background-color: green;
  	color: white;
  	border: 1px solid black;
  	text-decoration: none;
  	text-decoration-color: white;
  }
  .conference {
  	font-size: small;
  	background-color: orange;
  	color: white;
  	border: 1px solid black;
  	text-decoration: none;
  	text-decoration-color: white;
  }
  .workshop {
  	font-size: small;
  	background-color: purple;
  	color: white;
  	border: 1px solid black;
  	text-decoration: none;
  	text-decoration-color: white;
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

{% assign years = "2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999" | split: ',' %}
{% for y in years %}
<div class="year">{{ y }}</div>
<p>
{% for x in site.data.pubs.bibs %}
  {% if x.YEAR == y %}
	  <p>
	  	{% for a in x.AUTHOR %}
	  		{% if forloop.last == true and forloop.first == false %}and{% endif%} {{ a.name | replace:'~',' ' }}{% if forloop.last == false and forloop.length > 2 %},{% endif %}
	  	{% endfor %}<br>
	    <b>{{ x.TITLE }}</b><br>
	    <em>{{ x.JOURNAL }}{{ x.BOOKTITLE }} 
	    {{ x.VOLUME }} 
	    ({{ x.YEAR }})</em>.<br>
	    {% if x.URL %}
	    	<a href="{{x.URL}}">{% if x.URL contains "arxiv" %}<span class="arxiv">arXiv</span>{% else %}<span class="pdf">PDF</span>{% endif %}</a>
	    {% endif %}
	    {% if x.JOURNAL and x.VOLUME %}<span class="journal">Journal</span>{% endif %}
	    {% if x.BOOKTITLE %}{% if x.BOOKTITLE contains "Workshop" %}<span class="workshop">Workshop</span>{% else%}<span class="conference">Conference</span>{% endif %}{% endif %}
	  </p>
  {% endif %}
{% endfor %}
</p>
{% endfor %}

