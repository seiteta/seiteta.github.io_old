---
layout: post
permalink: /python-reference.html
title: My Python cheat sheet
tags: Python cheat-sheet
---

# List
Create a list:
{% highlight python %}
favmathband = ["TTNG","toe","Clever Girl",'Radiohead']
{% endhighlight %}

Delete an item:
{% highlight python %}
favmathband.remove('Radiohead')
{% endhighlight %}

# Dictionaries
Pairs of key and value. **Warning**: dictionaries are unordered.
Create a dictionnary:
{% highlight python %}
ponies = { 'Twilight Sparkle' : 'Unicorn pony',
'Applejack' : 'Earth pony',
'Pinkie Pie' : 'Earth pony',
'Fluttershy' : 'Pegasus pony',
'Rainbow Dash' : 'Pegasus pony',
'Rarity' : 'Unknown'}
{% endhighlight %}

Change an item:
{% highlight python %}
ponies['Rarity'] = 'Unicorn pony'
{% endhighlight %}

Delete an item:
{% highlight python %}
del ponies['Rarity']
{% endhighlight %}

Values can be list, int, string...
{% highlight python %}
backpack = {
    'money' : 30,
    'pocket' : ['glasses','beany', 'charger','fan']
}
{% endhighlight %}

Access a value in a list in a dictionary:
{% highlight python %}
backpack["pocket"][0]
# return glasses \o-o/
{% endhighlight %}


#Loops
##for loop
**Warning**: don't forget the `:`
{% highlight python %}
felid = ["tiger","linx","snow leopard","cat"]
for name in felid:
    print name
{% endhighlight %}

