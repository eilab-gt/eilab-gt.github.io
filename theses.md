---
layout: splash
title: Theses
classes: wide

---

# Theses

{% for thesis in site.data.theses reversed %}

**{{ thesis.name }}. [{{ thesis.title }}]({{thesis.url}}). Ph.D. Dissertation, {{ thesis.institute }}, {{ thesis.year }}.**

{{ thesis.abstract}}

{% endfor %}




