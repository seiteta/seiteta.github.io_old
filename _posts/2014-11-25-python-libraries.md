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

* [Pie chart](http://matplotlib.org/api/pyplot_api.html?highlight=pie#matplotlib.pyplot.pie)
{% highlight python %}
import matplotlib.pyplot as plt
 
activities_list = [1, 5, 7, 0.2]
label_list = ["eat", "sleep", "destroy everything", "purr"]

plt.axis("equal") #changes limits of x or y axis so that equal increments of x and y have the same length.
plt.pie(
activities_list,
labels=label_list,
autopct="%1.1f%%" #labels the wedges with their numeric value
)
plot.title("My cat activities")
plt.show() #displays the figure
{% endhighlight %}
   
