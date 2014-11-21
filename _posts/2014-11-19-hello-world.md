---
layout: post
permalink: /hello.html
title: Hello world
---

Hello world, this is my first post using Jekyll! やった!!

#Code
This is some Python:
{% highlight python %}
from kartograph import Kartograph
K = Kartograph()
K.generate(cfg, outfile='mymap.svg')
{% endhighlight %}


Code syntax is:
{% highlight text %}
{% raw %}{% highlight markdown %}{% endraw %}
{% raw %}{% highlight endhighlight %}{% endraw %}
{% endhighlight %}


#Image
Here is a link to my first image:
[My first image](/downloads/branching.png)
