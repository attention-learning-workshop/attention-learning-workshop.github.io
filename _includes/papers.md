### CogSci and Neuroscience
{% for paper in site.data.cogsci %}
{{ paper.author }} ({{ paper.year }}). {{ paper.title }}. *{{ paper.venue }}*. [Link]({{ paper.link }})
{% endfor %}