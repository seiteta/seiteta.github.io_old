---
layout: post
permalink: /ml-notes.html
title: Machine learning notes
---

Some notes from the [ML Coursera class](https://www.coursera.org/course/ml), taught by Andrew Ng.

## I. Introduction (Week 1)

### Supervised learning

Supervised learning means that the algorithm know "correct" outputs.

Regression problem: when the outputs have continuous values. Example: Housing price vs Housing size.

Classification problem: whent the output have discrete values. Example: Tumor size vs benign or malignant.

### Unsupervised learning

In unsupervised learning, the algorithm has no idea what is a "correct output". Its challenge is then to try to find a structure in the data.

Clustering: data are grouped inside separated clusters. Example: Google News related articles.
Cocktail party algorithm. Example: Separation of two sounds played together.

## II. Linear Regression with One Variable (Week 1)
Definitons: a function *h* (for hypothesis) maps from input variables *x*'s to output variables *y*'s.
*h* is a linear function: `h_\theta (x) = \theta_0 + \theta_1 x`. `\theta_0` and `\theta_1` are the parameters.

Training set: 
