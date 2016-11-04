---
layout: post
permalink: /sql-reference.html
title: My SQL cheat sheet
tags: SQL cheat-sheet
author: Frédéric Bardolle
---

# Manipulation

Create a table:
{% highlight SQL%}
CREATE TABLE ponies (id INTEGER, name TEXT, kind TEXT);
{% endhighlight %}

Add a row:
{% highlight SQL%}
INSERT INTO ponies (id, name, kind) VALUES (1, 'Pinkie Pie', 'Earth');
{% endhighlight %}

Select a column:
{% highlight SQL%}
SELECT name FROM ponies;
{% endhighlight %}

Select every column:
{% highlight SQL%}
SELECT * FROM ponies;
{% endhighlight %}

Update:
{% highlight SQL%}
UPDATE ponies 
SET name = "Applejack" 
WHERE id = 1; 
{% endhighlight %}

Alter:
{% highlight SQL%}
ALTER TABLE ponies ADD COLUMN color TEXT; 
{% endhighlight %}

Delete:
{% highlight SQL%}
DELETE FROM ponies WHERE color IS NULL;
{% endhighlight %}


# Queries

Query two columns:
{% highlight SQL%}
SELECT name, imdb_rating FROM movies;
{% endhighlight %}

Return unique values:
{% highlight SQL%}
SELECT DISTINCT genre FROM movies;
{% endhighlight %}

Filter with condition:
{% highlight SQL%}
SELECT * FROM movies WHERE imdb_rating > 8;
{% endhighlight %}

Search for a specific pattern:
{% highlight SQL%}
SELECT * FROM movies
WHERE name LIKE 'Se_en';
{% endhighlight %}

Wildcards:

* `_`: one character
* `%`: zero or more characters

Between:
{% highlight SQL%}
SELECT * FROM movies
WHERE name BETWEEN 'A' AND 'J';
{% endhighlight %}

{% highlight SQL%}
SELECT * FROM movies
WHERE year BETWEEN 1990 AND 2000;
{% endhighlight %}

And:
{% highlight SQL%}
SELECT * FROM movies
WHERE year BETWEEN 1990 AND 2000
AND genre = 'comedy';
{% endhighlight %}

Or:
{% highlight SQL%}
SELECT * FROM movies
WHERE genre = 'comedy'
OR year < 1980;
{% endhighlight %}

Order by:
{% highlight SQL%}
SELECT * FROM movies
ORDER BY imdb_rating DESC;
{% endhighlight %}

Limit the number of rows returned:
{% highlight SQL%}
SELECT * FROM movies
ORDER BY imdb_rating ASC
LIMIT 3;
{% endhighlight %}

# Aggregate Functions

Count:
{% highlight SQL%}
SELECT COUNT(*) FROM fake_apps;
{% endhighlight %}

Group by:
{% highlight SQL%}
SELECT price, COUNT(*) FROM fake_apps
GROUP BY price;
{% endhighlight %}

Sum:
{% highlight SQL%}
SELECT SUM(downloads) FROM fake_apps;
{% endhighlight %}

Max:
{% highlight SQL%}
SELECT MAX(downloads) FROM fake_apps;
{% endhighlight %}

Min:
{% highlight SQL%}
SELECT MIN(downloads) FROM fake_apps;
{% endhighlight %}

Average:
{% highlight SQL%}
SELECT AVG(downloads) FROM fake_apps;
{% endhighlight %}

Round:
{% highlight SQL%}
SELECT price, ROUND(AVG(downloads), 2) FROM fake_apps
GROUP BY price;d
{% endhighlight %}


# Multiple Tables

Primary key:
{% highlight SQL%}
CREATE TABLE artists(id INTEGER PRIMARY KEY, name TEXT)
{% endhighlight %}

Data from two tables (cross join) (NB: this query sucks):
{% highlight SQL%}
SELECT albums.name, albums.year, artists.name FROM albums, artists;
{% endhighlight %}

Rigth way to do that (inner join):
{% highlight SQL%}
SELECT
  *
FROM
  albums
JOIN artists ON
  albums.artist_id = artists.id;
{% endhighlight %}

If we want to include albums where we don't have the artist (left outer join):
{% highlight SQL%}
SELECT
  *
FROM
  albums
LEFT JOIN artists ON
  albums.artist_id = artists.id;
{% endhighlight %}

Using alias for column or table name:
{% highlight SQL%}
SELECT
  albums.name AS 'Album',
  albums.year,
  artists.name AS 'Artist'
FROM
  albums
JOIN artists ON
  albums.artist_id = artists.id
WHERE
  albums.year > 1980;
{% endhighlight %}
