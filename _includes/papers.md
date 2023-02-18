### CogSci and Neuroscience
{% for paper in site.data.cogsci %}
{{ paper.author }} ({{ paper.year }}). {{ paper.title }}. *{{ paper.venue }}*. [Link]({{ paper.link }})
{% endfor %}
<br />

### Machine Learning, Deep Learning and Reinforcement Learning
{% for paper in site.data.ml %}
{{ paper.author }} ({{ paper.year }}). {{ paper.title }}. *{{ paper.venue }}*. [Link]({{ paper.link }})
{% endfor %}
<br />

### HCI, HRI and Robotics
{% for paper in site.data.hci %}
{{ paper.author }} ({{ paper.year }}). {{ paper.title }}. *{{ paper.venue }}*. [Link]({{ paper.link }})
{% endfor %}
<br />