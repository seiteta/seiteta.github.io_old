---
layout: post
permalink: /sql-reference.html
title: My SQL cheat sheet
tags: SQL cheat-sheet
author: Frédéric Bardolle
---

## Create

Create a table:
{% highlight SQL%}
CREATE TABLE ponies (id INTEGER, name TEXT, type TEXT);
{% endhighlight %}

Add a row:
{% highlight SQL%}
INSERT INTO ponies (id, name, type) VALUES (1, 'Pinkie Pie', 'Earth');
{% endhighlight %}


## Select

Select a column:
{% highlight SQL%}
SELECT name FROM ponies;
{% endhighlight %}

Select every column:
{% highlight SQL%}
SELECT * FROM ponies;
{% endhighlight %}


## Update

{% highlight SQL%}
UPDATE ponies 
SET name = "Applejack" 
WHERE id = 1; 
{% endhighlight %}


## Alter

{% highlight SQL%}
ALTER TABLE ponies ADD COLUMN color TEXT; 
{% endhighlight %}


## Delete

{% highlight SQL%}
DELETE FROM ponies WHERE color IS NULL;
{% endhighlight %}
