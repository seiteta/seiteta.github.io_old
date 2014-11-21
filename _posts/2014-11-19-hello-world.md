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
My code here
{% raw %}{% highlight endhighlight %}{% endraw %}
{% endhighlight %}


#Image
Here is a link to my first image:
[My first image](/downloads/branching.png)


Images displayed this way appear on GitHub but not on the Jekyll:
<img src ="/downloads/branching.png" align="center" title="Branching on GH" class="img"</img>
{% highlight markdown %}
<img src ="/downloads/branching.png" align="center" title="Branching on GH" class="img"</img>
{% endhighlight %}

This way works better:
![branching](/downloads/branching.png "Branching on GH")
{% highlight markdown %}
{% raw %}![branching](/downloads/branching.png "Branching on GH"){% endraw %}
{% endhighlight %}
