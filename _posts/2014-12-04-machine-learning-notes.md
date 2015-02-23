---
layout: post
permalink: /ml-notes.html
title: Machine learning notes
---

My notes from the [ML Coursera class](https://www.coursera.org/course/ml), taught by Andrew Ng.

## I. Introduction (Week 1)

### Supervised learning

Supervised learning means that the algorithm know the "correct" outputs.

Regression problem: when the outputs have continuous values. Example: Housing price vs Housing size.

Classification problem: whent the output have discrete values. Example: Tumor size vs benign or malignant.

### Unsupervised learning

In unsupervised learning, the algorithm has no idea what is a "correct output". Its challenge is then to try to find a structure in the data.

Clustering: data are grouped inside separated clusters. Example: Google News related articles.
Cocktail party algorithm. Example: Separation of two sounds played together.

## II. Linear Regression with One Variable (Week 1)

### Linear Regression Model

Definitons: a function $$h$$ (for hypothesis) maps from input variables $$x$$ to output variables $$y$$. Couple $$(x, y)$$ are training example (from the training set).

Here, $$h$$ is a linear function: 

$$ h_\theta (x) = \theta_0 + \theta_1 x $$

$$\theta_0$$ and $$\theta_1$$ are the parameters. To find the best model is to find the parameters that minimize the sum of the squared difference between $$h_\theta (x^{(i)})$$ and $$y^{(i)}$$. The cost function $$J$$ is then the squared error function:

$$J(\theta_0, \theta_1) = \dfrac{1}{2m} \sum_{i=1}^{m} \left(h_\theta (x^{(i)}) - y^{(i)}\right)^2$$

where $$m$$ is the size of the training set. 

### Gradient descent algorithm

For a two parameters model, repeat until convergence:

$$\theta_j := \theta_j - \alpha \dfrac{\partial}{\partial \theta_j}J(\theta_0, \theta_1) $$

and simultaneously update for $$j=0$$ and $$j=1$$.

$$J$$ is the cost function, $$\alpha$$ is the learning rate that control the speed of the descent and $$\dfrac{\partial}{\partial \theta_j}J(\theta_0, \theta_1) $$ is the derivative term that give the direction of the slope.

One problem is that if the initial values give a cost function located in local minimum, the parameters won't move since the derivative term is equal to zero.

One advantage is that we don't have to change $$\alpha$$ to slow things down as we approach the minimum because the derivative is getting smaller and smaller, and so are the steps.

### Gradient Descent for Linear Regression

For a linear regression model, repeat until convergence:

$$\theta_0 := \theta_0 - \alpha \dfrac{1}{m} \sum_{i=1}^{m} \left (h_\theta (x^{(i)}) - y^{(i)} \right )$$

$$\theta_1 := \theta_1 - \alpha \dfrac{1}{m} \sum_{i=1}^{m} \left (h_\theta (x^{(i)}) - y^{(i)} \right)\cdot  x^{(i)}$$

and simultaneously update $$\theta_0$$ and $$\theta_1$$.

## IV. Linear Regression with Multiple Variables (Week 2)

### Multivariate linear regression:

Size ($$x_1$$)|Number of bedroom ($$x_2$$)|Age of home ($$x_3$$)|Price ($$y$$)
:---:|:---:|:---:|:---:
2104|5|45|460 000
1646|3|40|232 000
852|2|36|178 000
|||

* $$x_j^{(i)}$$ is the value of feature $$j$$ in the $$i$$<sup>th</sup> training example.
* $$m$$ is the number of training examples
* $$n=\|x^{(i)}\|$$ is the number of features.

The hypothesis function become:

$$h_\theta (x) = \begin{bmatrix} \theta_0  &\theta_1  & ... & \theta_n \end{bmatrix} + \begin{bmatrix}  x_0  \\ x_1  \\ ...  \\ x_n\end{bmatrix} = \theta^T x$$

$$\theta = \begin{bmatrix} \theta_0  \\ \theta_1  \\ ... \\ \theta_n \end{bmatrix}$$ is a parameter vector.

### Feature scaling and mean normalization
Make sure the feature are on a similar scale in order to avoid hemstitching phenomenon due to the narrow valley of the cost function. In practice, it means to get every value of the different features between -1 and 1 approximately.

And substract the mean (mean normalization).

$$x_j := \dfrac{x_j - \mu_j}{s_j}$$

With $$\mu_j$$ the mean of the feature $$j$$ and $$s_j$$ its standard deviation.

### Learning rate
Choose the learning rate: plot cost function vs number of iteration. The cost function $$J(\theta)$$ should decrease every iteration. If it's not, choose a smaller $$\alpha$$. But be careful because if $$\alpha$$ is too small, the algorithm will take foreeeeeeeever to converge.

It is also possible to use a convergence test: for example, you can declare convergence if the cost function decrease by less than $$10^{-3}$$ in one iteration.

### Polynomial regression
A model represented as a polynomial equation, for example:

$$ h_\theta (x) = \theta_0 + \theta_1 (size) + \theta_2 (size) ^2$$

can be transformed into a multivariate linear model by changing the features $$(size) = x_1$$ and $$ (size)^2 = x_2$$:

$$ h_\theta (x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 $$

In that case, it's even more important to take care of the *feature scaling* because the scale difference is squared.

### Normal equation

Another of finding the minimum of the cost function is to use the normal equation. Basically, you have to find the parameter vector $$\theta$$ for which the partial derivatives of $$J(\theta)$$ equal to zero. Under some assumptions, a solution to this problem is (see proof [here](http://en.wikipedia.org/wiki/Linear_least_squares_%28mathematics%29#The_general_problem)):

$$ \theta=(X^TX)^{-1}X^Ty $$

Note that if $$ X^TX $$ is non-invertible (it can happen when their are too many features or when they are linearly dependant), the pseudoinverse of the matrix can be used. The MATLAB function is [`pinv`](http://mathworks.com/help/matlab/ref/pinv.html), instead of [`inv`](http://mathworks.com/help/matlab/ref/inv.html).

Compared to the descent algorithm, there is no need to choose $$\alpha$$ nor the number of iteration, which is good. But the inversion of the matrix can make the algorithme slow when the number of features $$n$$ become big (for our computer $$n>=10^6$$) because it has a complexity in $$O(n^3)$$.

## V. Octave Tutorial (Week 2)

### Vectorization

One can implement this equation $$h_{\theta}(x) = \sum_{j=0}^{n} \theta_j x_j$$ with this code:

{% highlight matlab %}
prediction = 0.0;
for j = 1:n+1,
  prediction += theta(j) * x(j);
end;
{% endhighlight %}

But since it's equivalent to $$h_{\theta}(x) = \theta^T x$$, it can be implemented in a vectorized way:

{% highlight matlab %}
prediction = theta' * x;
{% endhighlight %}

## VI. Logistic Regression (Week 3)

## Classification

Logistic regression is used for classification problem. In this chapter, we study binary classification problem. The output $$y$$ is either 0 or 1, where 0 is the "negative class" and 1 is the "positive class".

##Hypothesis representation

We use the sigmoid function:
$$ h_\theta (x) = \dfrac{1}{1+e{-\theta^T x}}$$
