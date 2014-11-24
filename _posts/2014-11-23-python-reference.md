---
layout: post
permalink: /python-reference.html
title: My Python cheat sheet
tags: Python cheat-sheet
---

# List
* Create a list:
    {% highlight python %}
    favmathband = ["TTNG","toe","Clever Girl","Radiohead"]
    {% endhighlight %}

* Add an item:
    {% highlight python %}
    favmathband.append("Tangled Hair")
    {% endhighlight %}

* Delete an item:
{% highlight python %}
favmathband.remove("Radiohead")
{% endhighlight %}
or (**Warning**: first index is 0)
{% highlight python %}
favmathband.pop(3)
{% endhighlight %}
or
{% highlight python %}
del(favmathband[3])
{% endhighlight %}

* Range list:
{% highlight python %}
range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
{% endhighlight %}

* Two methods to iterate over a list (the second one make it possible to modify the list):
{% highlight python %}
for item in list:
    print item
{% endhighlight %}
{% highlight python %}
for i in range(len(list)):
    print list[i]
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
With a list:
{% highlight python %}
felid = ["tiger","linx","snow leopard","cat"]
for name in felid:
    print name
{% endhighlight %}

With a dictionary:
{% highlight python %}
for key in dictionary:
    print dictionary[key]
    #print values associated with keys, in no particular order
{% endhighlight %}

Codecademy Supermarket example:
{% highlight python %}
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for fruit in food:
        if stock[fruit] <> 0:
            total += prices[fruit]
            stock[fruit] += -1
            #first time I think "Python is beautiful"
    return total
{% endhighlight %}

# Comparison operators
Equal is `==`:
{% highlight python %}
a == b
{% endhighlight %}

Not equal is `!=`:
{% highlight python %}
a != b
{% endhighlight %}
