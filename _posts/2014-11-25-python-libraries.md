---
layout: post
permalink: /python-libraries.html
title: My Python libraries cheat sheet
tags: Python library cheat-sheet
---

# [pandas](http://pandas.pydata.org/)
*pandas* is a data analysis library. For example, it provides tools to read and write CSV files.

# [matplotlib](http://matplotlib.org)
*matplotlib* is a 2D plotting library.

* Color

  There are several ways to define colors:

Color model| Code 
--- | ---
RVB|`(0.2, 0.2, 0.6)`
RVBA (i.e. RVB + opacity)|`(0.2, 0.2, 0.6, 0.5)`
Hex|`'#FF9E4A'`
Name|`'gold'`
Abbreviation (for basic colors, like yellow or cyan)|`'y'`
Grayscale|`'0.15'`


* [Pie chart](http://matplotlib.org/api/pyplot_api.html?highlight=pie#matplotlib.pyplot.pie)
{% highlight python %}
import matplotlib.pyplot as plt
import numpy as np

### DATA 
#activities = [2, 5, 8, 1]          # default list
activities = np.array([2, 5, 8, 1]) # NumPy array
labels = ["eat", "sleep", "destroy everything", "purr"]
colors = ['#729ECE', '#FF9E4A', '#67BF5C', '#ED665D']

### CONFIG
plt.axis("equal") #changes limits of x or y axis so that equal increments of x and y have the same length.
plt.title("My cat activities", color = '0.15')

plt.rcParams['patch.linewidth'] = 0.5       #reduces edges
plt.rcParams['patch.edgecolor'] = '0.15'    #changes edges color to dark grey
plt.rcParams['font.size'] = 15
plt.rcParams['text.color'] = '0.15'
plt.rcParams['axes.labelcolor'] = '0.15'

### PLOT
plt.pie(
activities,
labels = labels,
colors = colors,
startangle = 160,   #rotates the pie
autopct = "%1.1f%%" #labels the wedges with their numeric value
)

### DISPLAY
plt.show() #displays the figure
{% endhighlight %}

Results:
![cat](/downloads/cat-activities.png "My cat activities")

# [numpy](http://www.numpy.org/)
*numpy* is a scientific computing library, allowing user to uses matrices.

{% highlight python %}
import numpy.random as npr
A = npr.rand(3, 3) #create a 3x3 random matrix
{% endhighlight %}
