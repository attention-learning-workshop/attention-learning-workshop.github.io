## CogSci and Neuroscience
{% for paper in site.data.papers %}
{{ paper.author }} ({{ paper.year }}). {{ paper.title }}. *{{ paper.venue }}*. [Link]({{ paper.link }})
{% endfor %}