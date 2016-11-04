---
layout: post
permalink: /sql-reference.html
title: My SQL cheat sheet
tags: SQL cheat-sheet
author: Frédéric Bardolle
---

# Manipulation

## Create

Create a table:
{% highlight SQL%}
CREATE TABLE ponies (id INTEGER, name TEXT, kind TEXT);
{% endhighlight %}

Add a row:
{% highlight SQL%}
INSERT INTO ponies (id, name, kind) VALUES (1, 'Pinkie Pie', 'Earth');
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


# Queries

Query two columns
SELECT name, imdb_rating FROM movies;

Return unique values
SELECT DISTINCT genre FROM movies;

Filter with condition
SELECT * FROM movies WHERE imdb_rating > 8;

Search for a specific pattern
SELECT * FROM movies
WHERE name LIKE 'Se_en';

Wildcards:

* `_`: one character
* `%`: zero or more characters

Between:

SELECT * FROM movies
WHERE name BETWEEN 'A' AND 'J';

SELECT * FROM movies
WHERE year BETWEEN 1990 AND 2000;

And:
SELECT * FROM movies
WHERE year BETWEEN 1990 AND 2000
AND genre = 'comedy';

Or:
SELECT * FROM movies
WHERE genre = 'comedy'
OR year < 1980;

Order by:
SELECT * FROM movies
ORDER BY imdb_rating DESC;

Limit the number of rows returned:
SELECT * FROM movies
ORDER BY imdb_rating ASC
LIMIT 3;

# Aggregate Functions

Count
SELECT COUNT(*) FROM fake_apps;


# Multiple Tables
