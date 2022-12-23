---
layout: splash
title: Members

---

# Members

**Faculty**

<ul>
{% for x in site.data.faculty.members %}
  <li>
    <a href="{{ x.website }}">{{ x.name }}</a>
  </li>
{% endfor %}
</ul>

**PhD Students**

<ul>
{% for x in site.data.phds.members %}
  <li>
    <a href="{{ x.website }}">{{ x.name }}</a>
  </li>
{% endfor %}
</ul>

**Masters Students**

<ul>
{% for x in site.data.masters.members %}
  <li>
    <a href="{{ x.website }}">{{ x.name }}</a>
  </li>
{% endfor %}
</ul>

**Undergraduate Students**

<ul>
{% for x in site.data.undergrads.members %}
  <li>
    <a href="{{ x.website }}">{{ x.name }}</a>
  </li>
{% endfor %}
</ul>

**Alumni**

<ul>
{% for x in site.data.alumni.members %}
  <li>
    <a href="{{ x.website }}">{{ x.name }}</a>: {{ x.where }}
  </li>
{% endfor %}
</ul>

**Affiliated**

<ul>
{% for x in site.data.affiliated.members %}
  <li>
    <a href="{{ x.website }}">{{ x.name }}</a>
  </li>
</ul>
