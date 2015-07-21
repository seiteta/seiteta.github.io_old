---
layout: post
permalink: /python-reference.html
title: My Python cheat sheet
tags: Python cheat-sheet
author: Frédéric Bardolle
---
## String
* Iterate over a string:
{% highlight python %}
word = "hello"
for char in word:
    print char
{% endhighlight %}

* Split a sentence:
{% highlight python %}
sentence = "As you wish"
words = sentence.split(" ") #the result is a list containing the words
{% endhighlight %}

* Join a list of words to create a sentence:
{% highlight python %}
sentence2 = " ".join(words) #Continuing the above example
{% endhighlight %}

## List
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

* List comprehension: a concise way to create lists. For example, to build the list of even numbers from 0 to 50:
{% highlight python %}
evens_to_50 = [i for i in range(51) if i % 2 == 0]
{% endhighlight %}

instead of:
{% highlight python %}
evens_to_50 = []
for i in range(51):
    if i % 2 == 0:
        evens_to_50.append(i)
{% endhighlight %}

List comprehension can contain more than one for loop (example taken from [here](http://intermediatepythonista.com/python-comprehensions)):
{% highlight python %}
combinations = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
{% endhighlight %}

* List slicing `[start:end:stride]`:
{% highlight python %}
my_list = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print my_list[2:9:2]
# Return [9, 25, 49, 81]
{% endhighlight %}

Default value are `[0:len(my_list):1]`.

A nice way to reverse the element of a list:
{% highlight python %}
my_list = range(1, 11)
backwards = my_list[::-1]
{% endhighlight %}

## Dictionaries
Pairs of key and value. **Warning**: dictionaries are unordered.

* Create a dictionnary:
{% highlight python %}
ponies = { 'Twilight Sparkle' : 'Unicorn pony',
'Applejack' : 'Earth pony',
'Pinkie Pie' : 'Earth pony',
'Fluttershy' : 'Pegasus pony',
'Rainbow Dash' : 'Pegasus pony',
'Rarity' : 'Unknown'}
{% endhighlight %}

* Change an item:
{% highlight python %}
ponies['Rarity'] = 'Unicorn pony'
{% endhighlight %}

* Delete an item:
{% highlight python %}
del ponies['Rarity']
{% endhighlight %}

* Values can be list, int, string...
{% highlight python %}
backpack = {
    'money' : 30,
    'pocket' : ['glasses','beany', 'charger','fan']
}
{% endhighlight %}

* Access a value in a list in a dictionary:
{% highlight python %}
backpack["pocket"][0]
# return glasses \o-o/
{% endhighlight %}

* Keys and values:
{% highlight python %}
backpack.items()  #return an array of tuples, each containing a key/value pair
backpack.values() #return an array of the dictionary's values
backpack.keys()   #return an array of the dictionary's keys
{% endhighlight %}

* Iterate over a dicitonary (again in no specific order):
{% highlight python %}
for key in ponies:
    print key, ponies[key]
{% endhighlight %}

## Loops

### for loop
With a list: (**warning**: don't forget the `:`)
{% highlight python %}
felid = ["tiger","linx","snow leopard","cat"]
for name in felid:
    print name
{% endhighlight %}

If you need to know how far into the list you are:
{% highlight python %}
choices = ['veggie pizza', 'seitan curry', 'chocolate']
print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item
{% endhighlight %}

Iterate over multiple lists (**warning**: it stop at the shortest list):
{% highlight python %}
for a, b in zip(list_a, list_b):
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
            #first time I thought "wow, Python is beautiful"
    return total
{% endhighlight %}

Repeat `n` times (from `0` to `n-1`):
{% highlight python %}
n=3
for x in range(0, n):
    print "We're on time %d" % (x)
{% endhighlight %}

## Comparison operators
* Equal is `==`:
{% highlight python %}
a == b
{% endhighlight %}

* Not equal is `!=`:
{% highlight python %}
a != b
{% endhighlight %}

## Random
* Random integer
{% highlight python %}
from random import randint
coin = randint(0, 1)
dice = randint(1, 6)
{% endhighlight %}

## Anonymous function
* Lambda syntax:
{% highlight python %}
lambda x: x % 3 == 0
{% endhighlight %}
is equivalent to:
{% highlight python %}
def by_three(x):
    return x % 3 == 0
{% endhighlight %}

## Matrix (np.array)
* See this [page](http://sebastianraschka.com/Articles/2014_matrix_cheatsheet_table.html) giving MATLAB/Python equivalents. Or this [one](http://wiki.scipy.org/NumPy_for_Matlab_Users#head-13d7391dd7e2c57d293809cff080260b46d8e664).

## Regular expression
* See this [page](https://developers.google.com/edu/python/regular-expressions) from Google's Python Class.

## Class
* Basic class syntax
{% highlight python %}
class Robot(object):
    def __init__(self, name):
        self.name = name
{% endhighlight %}

 * More advanced syntax with a method (`description`) and a member variable(`is_alcoholic`)
{% highlight python %}
class Robot(object):
    is_alcoholic = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        print "My name is %s and I was build %s years ago." % (self.name, self.age)
{% endhighlight %}

* Create new instances of the class
{% highlight python %}
bending_unit = Robot("Bender", 2)
astomech_droid = Robot("R2D2", 32)
{% endhighlight %}

* Access to the attributes. Note that only the variable in Bender changed, not in R2D2.
{% highlight python %}
print bending_unit.is_alcoholic #True
astomech_droid.is_alcoholic = False
print astomech_droid.is_alcoholic #False
{% endhighlight %}

* Call a method
{% highlight python %}
bending_unit.description()
astomech_droid.description()
{% endhighlight %}
