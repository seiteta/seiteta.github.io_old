---
layout: post
permalink: /javascript-reference.html
title: My Javascript cheat sheet
tags: Javascript cheat-sheet
---
## Function
* Create a function:
{% highlight javascript %}
var timesTwo = function(number) {
    return number * 2;
};
{% endhighlight %}

General syntax:
{% highlight javascript %}
// Create a function:
var functionName = function(input1, input2) {
    //do something here;
};

// Call a function:
functionName(value1,value2);
{% endhighlight %}

## If/else
General syntax:
{% highlight javascript %}
if (condition1) {
    return "some string";
}
else {
    return "another string";
}
{% endhighlight %}

## Random
Random number between 0 and 1:
{% highlight javascript %}
Math.random()
{% endhighlight %}
