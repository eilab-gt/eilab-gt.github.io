---
layout: single
title: Publications
classes: wide
---

{% assign years = "2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999" | split: ',' %}
{% for y in years %}
<p><b>{{ y }}</b></p>
<ul>
{% for x in site.data.pubs.bibs %}
  {% if x.YEAR == y %}
	  <li>
	  	{% for a in x.AUTHOR %}
	  		{% if forloop.last == true and forloop.first == false %}and{% endif%} {{ a.name }}{% if forloop.last == false %},{% endif %}
	  	{% endfor %}<br>
	    <b>{{ x.TITLE }}</b><br>
	    <em>{{ x.JOURNAL }}{{ x.BOOKTITLE }} 
	    {{ x.VOLUME }} 
	    ({{ x.YEAR }})</em>.
	    {% if x.URL %}<br>
	    	<a href="{{x.URL}}">{% if x.URL contains "arxiv" %}ARXIV{% else %}PDF{% endif %}</a>
	    {% endif %}
	  </li>
  {% endif %}
{% endfor %}
</ul>
{% endfor %}

