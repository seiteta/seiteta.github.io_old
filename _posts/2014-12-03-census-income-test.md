---
layout: post
permalink: /income-test.html
title: Dataiku test
author: Frédéric Bardolle
---
The dataset used in this project come from the US Census Bureau and contain 42 anonymised information about approx. 300,000 persons. The goal was to predict whether or not these people earns more than 50k$ per year.

The objective of this test are:

1. Describe the different variables
2. Create a categorization model.

The Python code is in this [repo](https://github.com/seiteta/dataiku_test).

The libraries I used:

* `matplotlib` and `prettyplotlib` to create beautiful graphic
* `pandas` to import the csv file
* `sklearn` to build the model
* and also `scipy`, `numpy`, `pydot` and `os`

## Explanatory variables 
I've decided to consider variables as explantory when the frequency difference between classes is superior to a threshold (here it's 10%).

* Discrete variables :

Class|Values
:---:|:---:
class of worker|Not in universe, Private
detailed household and family stat|Child <18 never marr not in subfamily, Householder
detailed household summary in household|Child under 18 never married, Householder
education|Bachelors degree(BA AB BS), Children, Masters degree(MA MS MEng MEd MSW MBA)
family members under 18|Both parents present, Not in universe
full or part time employment stat|Children or Armed Forces, Full-time schedules, Not in labor force
industry code|0
major industry code|Not in universe or children
major occupation code|Executive admin and managerial, Not in universe, Professional specialty
marital status|Married-civilian spouse present, Never married
occupation code|0, 2
sex|Female, Male
tax filer status|Joint both under 65, Nonfiler
veterans benefits|0, 2
 | 

* Continuous variables :

|Variables|
|:---:|
|age|
|wage per hour|
|capital gains|
|capital losses|
|divdends from stocks|
|num persons worked for employer|
|weeks worked in year|
| |


## Vizualisation 

Some histograms and bar charts

![age](/downloads/age.png "Age histogram")

![weeks worked in year](/downloads/weeks worked in year.png "Number of weeks worked histogram")

![class of worker](/downloads/class of worker.png "Class of worker by classes bar chart")

![major industry code](/downloads/major industry code.png "Major industry code by classes bar chart")

![sex](/downloads/sex.png "Sex by classes bar chart")

![tax filer status](/downloads/tax filer status.png "Tax filer status by classes chart")


## Modelization

* Decision tree, minimun samples leaf = 5000

![income-tree](/downloads/income-tree.png "Decision tree, minimun samples leaf = 5000")

* Optimization of the classifier hyperparameters

![optimization](/downloads/optimization.png "Optimization of the classifier hyperparameters")
