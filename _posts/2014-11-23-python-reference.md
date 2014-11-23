---
layout: post
permalink: /python-reference.html
title: My Python cheat sheet
tags: Python cheat-sheet
---

# List
{% highlight python %}
awesome-band = ["TTNG","toe","Clever Girl"]
{% endhighlight %}

# Dictionaries
Pairs of key and value.
{% highlight python %}
ponies = { 'Twilight Sparkle' : 'Unicorn pony',
'Applejack' : 'Earth pony',
'Fluttershy' : 'Pegasus pony',
'Pinkie Pie' : 'Earth pony',
'Rarity' : 'Unknown',
'Rainbow Dash' : 'Pegasus pony',}
{% endhighlight %}

Change an item:
{% highlight python %}
ponies['Rarity'] = 'Unicorn pony'
{% endhighlight %}

Delete an item:
{% highlight python %}
del ponies['Rarity']
{% endhighlight %}
