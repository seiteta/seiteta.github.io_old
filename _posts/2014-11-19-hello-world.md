---
layout: post
permalink: /hello.html
title: Hello world
---

Hello world, this is my first post using Jekyll! やった!!

This is some Python:
{% highlight python %}
from kartograph import Kartograph

def myfilter(record):
    return record['name'] == "France"

cfg = {
  "proj": {
    "id": "mercator",
    "lon0": "auto"
    },
    "layers": {
        "mylayer": {
            "src": "subunits.shp",
            "filter": myfilter
        }
    }
}
    
K = Kartograph()
K.generate(cfg, outfile='mymap.svg')
{% endhighlight %}

And here is an image:
[My first image](/downloads/branching.png)

Images displayed this way appear on GitHub but not on the Jekyll:
<img src ="/downloads/branching.png" align="center" title="Branching on GH" class="img"</img>

This way works better:
![branching](/downloads/branching.png "Branching on GH")



[branching](/downloads/branching.png "Branching on GH")
