### CogSci and Neuroscience
<br />
{% for paper in site.data.cogsci %}
{{ paper.author }} ({{ paper.year }}). {{ paper.title }}. *{{ paper.venue }}*. [Link]({{ paper.link }})
{% endfor %}


### Machine Learning, Deep Learning and Reinforcement Learning
<br />
{% for paper in site.data.ml %}
{{ paper.author }} ({{ paper.year }}). {{ paper.title }}. *{{ paper.venue }}*. [Link]({{ paper.link }})
{% endfor %}


### HCI, HRI and Robotics
<br />
{% for paper in site.data.hci %}
{{ paper.author }} ({{ paper.year }}). {{ paper.title }}. *{{ paper.venue }}*. [Link]({{ paper.link }})
{% endfor %}