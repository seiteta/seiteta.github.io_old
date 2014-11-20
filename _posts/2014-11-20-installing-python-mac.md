---
layout: post
permalink: /installing-python-mac.html
title: Installing Python on a Mac OS X for novice
---

I have lost a few hours trying to make Python work correctly on Mac OS X so I'm writting this post in case you're also in trouble.

#The problem
Python is already installed in Mac OS X but, as I understand it, it's better to install another version of it so you can control everything and choose your version.


So I tried to install Python following the instructions from the [official documentation](https://docs.python.org/2/using/mac.html) but I wasn't able to load modules through the IDE. In fact, the modules were install from the terminal and only work with the built-in version of Python. 


After some screams and tears, followed by a hot cup of tea, I've finally found a [method](http://docs.python-guide.org/en/latest/starting/install/osx/) that made everything work like a charm.


#The solution: [Homebrew](http://brew.sh/)

Homebrew is a package manager (like Synaptic if you are familiar with Ubuntu) that will took care of everything. Basically, you install it with one line:
{% highlight bash %}
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
{% endhighlight %}
and you just follow its instructions. For example, it told to run `brew doctor` to clean up my previous attempt. You will also need to change the PATH, but again Homebrew will told you how to do.


Then, when you are ready to brew, run
{% highlight bash %}
$ brew install python
{% endhighlight %}
and voilà, Python is installed on you computer!
