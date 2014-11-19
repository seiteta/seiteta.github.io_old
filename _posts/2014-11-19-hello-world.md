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