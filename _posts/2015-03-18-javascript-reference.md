---
layout: post
permalink: /javascript-reference.html
title: My Javascript cheat sheet
tags: Javascript cheat-sheet
author: Frédéric Bardolle
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

## General syntax
Single line comment:
{% highlight javascript %}
// this is a comment
{% endhighlight %}

Multi-line comment:
{% highlight javascript %}
/*
Is this the real life?
Is this just fantasy?
Caught in a landslide,
No escape from reality.
*/
{% endhighlight %}

Some comparison operators:
{% highlight javascript %}
a === 3;	//equal value and equal type
b <= 8;     //less than or equal to
{% endhighlight %}

Logical Operators:
{% highlight javascript %}
x < 10 && y > 1;    //and
x === 5 || y === 5; //or
!(x === y);         //not
{% endhighlight %}


<iframe width="560" height="315" src="http://www.youtube.com/embed/EKoxLxzWNOk" frameborder="0" allowfullscreen></iframe>
