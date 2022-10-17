{% for paper in site.data.papers %}
{{ paper.author }} ({{ paper.year }}). {{ paper.title }}. *{{ paper.venue }}*. <{{ paper.link }}>
{% endfor %}