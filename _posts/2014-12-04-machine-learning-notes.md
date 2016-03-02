---
layout: post
permalink: /ml-notes.html
title: Machine learning notes
author: Frédéric Bardolle
---

My notes from the [ML Coursera class](https://www.coursera.org/course/ml), taught by Andrew Ng. See also this [wiki](https://share.coursera.org/wiki/index.php/ML:Main).

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

## III. Linear Algebra Review (Week 1)

![<3 matrices](https://media.giphy.com/media/ohdY5OaQmUmVW/giphy.gif)

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

One last thing:  using the normal equation does not require any feature scaling.

## V. Octave Tutorial (Week 2)

### Vectorization

One can implement the equation $$h_{\theta}(x) = \sum_{j=0}^{n} \theta_j x_j$$ with this code:

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

The vectorized implementation should be preferred because it is more concise and runs much faster.

## VI. Logistic Regression (Week 3)

### Classification

Logistic regression is used for classification problem. In this chapter, we study binary classification problem. The output $$y$$ is either 0 or 1, where 0 is the "negative class" and 1 is the "positive class". Hence, $$h_\theta (x)$$ should always be between 0 and 1 for binary classification.

### Hypothesis representation

The hypothesis function for logistic regression is called the sigmoid function or the logistic function:

$$ h_\theta (x) = \dfrac{1}{1+e^{-\theta^T x}}$$

$$h_\theta$$ give us the probability that our output is 1:

$$h_\theta(x) = P(y=1 | x ; \theta)$$

that reads "the probability that $$y=1$$, given $$x$$, parametrized by $$\theta$$

### Decision boundary

To get our binary classification we can translate the output of the hypothesis function as follows:

$$
\begin{align*}
& h_\theta(x) \geq 0.5 \rightarrow y = 1 \\
& h_\theta(x) < 0.5 \rightarrow y = 0 \\
\end{align*}
$$

$$h_\theta(x) = 0.5 $$ define a line: the decision boundary. For example, if $$\theta = \begin{bmatrix} -3 \\ 1 \\ 1 \end{bmatrix}$$, then $$h_\theta(x) = g(\theta_0 + \theta_1 x_1 + \theta_2 x_2) = g(-3 +  x_1 +  x_2)$$ and the boudary line is $$ x_1 +  x_2 = 3$$.

$$y = 1$$ in the region define by  $$ x_1 +  x_2 \geq 3$$ and $$y = 0$$ in the region define by  $$ x_1 +  x_2 < 3$$

By adding polynomial terms to the hypothesis function, it is possible to have more complex decision boundaries, like conics and complicated shapes.

### Cost function

The cost function used in linear regression can't be used in logistic regression because it become non-convex, with many local minima. It can be written as:

$$J(\theta) =  \dfrac{1}{m} \sum_{i=1}^{m} \left ( \text{cost}(h_\theta (x^{(i)}), y^{(i)}\right )$$

with

$$
\text{cost}(h_\theta(x),y) = 
\begin{cases}
−\log(h_\theta(x)) & \text{if } y = 1 \\
−\log(1−h_\theta(x)) & \text{if } y = 0 \\
\end{cases}
$$

This way, when $$y = 1$$, if $$ h_\theta(x) = 1$$, then $$\text{cost}(h_\theta(x),y) = 0$$, and when $$ h_\theta(x) \rightarrow 0$$, then $$ \text{cost}(h_\theta(x),y) \rightarrow \infty$$. This cost function comes from maximum-likelihood estimation (whereas the cost function for linear regression comes from least squares estimation).

### Simplified Cost Function and Gradient Descent

Since $$y$$ is always equal to either $$0$$ or $$1$$, the cost function can be expressed as: 

$$J(\theta) = - \frac{1}{m} \sum_{i=1}^m \left [y^{(i)}\log \left (h_\theta (x^{(i)}) \right) + (1 - y^{(i)})\log \left (1 - h_\theta(x^{(i)}) \right ) \right ]$$

The gradient descent looks exactly the same, except for the hypothesis function. Repeat until convergence:

$$\theta_j := \theta_j - \alpha \dfrac{1}{m} \sum_{i=1}^{m} \left (h_\theta (x^{(i)}) - y^{(i)} \right)\cdot  x_j^{(i)}$$

and simultaneously update all $$\theta_j$$.

### Advanced Optimization
Instead of gradient descent, it is possible to minimize the cost function with other algorithms like conjugate gradient, BFGS or L-BFGS. Some of their advantages is that $$\alpha$$ is automatically updated and they converge faster.

These algorithms already exist in librairies, but to use them, we need to write a function that return the cost function and the partial derivatives:

{% highlight matlab %}
function [jVal, gradient] = costFunction(theta)
  jval = []; %code to compute J(theta)
  gradient = []; % code to compute partial derivative of J(theta)
end
{% endhighlight %}

and then call it with a solver like [`fminunc`](http://fr.mathworks.com/help/optim/ug/fminunc.html):

{% highlight matlab %}
options = optimset('GradObj', 'on', 'MaxIter', 100);
initialTheta = zeros(2,1);

[optTheta, functionVal, exitFlag] = fminunc(@costFunction, initialTheta, options); %the @ is for Octave, not sure about MATLAB
{% endhighlight %}

### Multiclass Classification: One-vs-all
If the problem is multiclass instead of binary, we can use the one-vs-all (or one-vs-rest) approach. The idea is to train a single classifier for each class $$i$$:

$$h_\theta^{(i)}(x) = P(y = i | x ; \theta)$$

To make new prediction for a new sample $$x$$: $$\text{prediction}=\max_i( h_\theta ^{(i)}(x) $$.

## VII. Regularization (Week 3)

### The Problem of Overfitting
A model that is too simple can lead to underfitting (or high bias). Conversely, a model that is too complex can lead to overfitting (or high variance), meaning that the learned hypothesis fits the train set very well but fail to generalize to new examples.

There are two main options to address the issue of overfitting:

1. Reduce the number of features.
2. Regularization.

### Cost Function
The idea behind regularization is having small values for the parameters $$\theta_j$$ to have a simpler hypothesis. Basically, it is a way to use less features as possible.

$$J(\theta_0, \theta_1) = \dfrac{1}{2m} \left[ \sum_{i=1}^{m} \left(h_\theta (x^{(i)}) - y^{(i)}\right)^2 + \lambda\ \sum_{j=1}^n \theta_j^2 \right]$$

$$\lambda$$ is called the regularization parameter.

### Regularized Linear Regression
For gradient descent:

$$
\begin{align*}
& \theta_0 := \theta_0 - \alpha\ \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_0^{(i)} \\
& \theta_j := \theta_j - \alpha\ \left[ \left( \frac{1}{m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)} \right) + \frac{\lambda}{m}\theta_j \right] & \text{for } j \in \lbrace 1,2...n\rbrace \\
\end{align*}
$$

For normal equation:

$$
\begin{align*}
& \theta = \left( X^TX + \lambda \cdot L \right)^{-1} X^Ty \\
& \text{where } L = 
\begin{bmatrix}
 0 & & & \\
 & 1 & & \\
 & & \ddots & \\
 & & & 1 \\
\end{bmatrix}
\end{align*}
$$

A quick note about non-invertibility: supposed the $$m \le n$$ (i.e. there are more features than examples), the matrix $$X^TX$$ is non-invertible (or singular), but the matrix $$X^TX + \lambda \cdot L$$ is invertible. Thank you regularization!

### Regularized Logistic Regression

For logistic regression, the cost function becomes:
$$ J(\theta) = - \frac{1}{m} \sum_{i=1}^m \left [y^{(i)}\log \left (h_\theta (x^{(i)}) \right) + (1 - y^{(i)})\log \left (1 - h_\theta(x^{(i)}) \right ) \right ] + \frac{\lambda}{2m}\sum_{j=1}^n \theta_j^2 $$

and the gradient descent algorithm looks like the one for linear regression, exept $$h_\theta$$ is a different function.

## VIII. Neural Networks: Representation (Week 4)

### Non-linear Hypotheses

The problem with methods like logistic regression is that if we want to build a non-linear hypothesis function, we need approximatly $$\dfrac{n^2}{2}$$ parameters for $$n$$ features to include all the quadratic term. But an image of only 50x50 pixels have 2500 features if it is grayscale, and 7500 if it is colored. That means 3 millions features for the grayscale version and 28 millions features for the colored ones.

### Neurons and the Brain

![Pinky and the Brain](https://media.giphy.com/media/JGWTrgUc1WMDe/giphy.gif)

Some "rewiring" experiences prove that the brain have what is call "neuroplasticity", which basically means that every piece of the brain can learn to perform any task.

### Model Representation I

$$\theta$$ parameters are sometimes called "weights" in the neural networks model. The first layer is called the "input layer", the last is called "output layer" and the layers in-between are called "hidden layers".

* $$a_i^{j}$$ is the activation of the unit $$i$$ in the layer $$j$$.
* Parameters are represented in $$\Theta^{j}$$, a matrix of weights controlling the mapping from a layer $$j$$ to a layer $$j+1$$.
* If network has $$s_j$$ units in layer $$j$$ and $$s_{j+1}$$ units in layer $$j+1$$, then $$\Theta^{j}$$ will be of dimension $$s_{j+1}×(s_{j}+1)$$.

### Model Representation II

Considering only the last hidden unit and the output unit, we are doing exactly the same thing as we did in logistic regression, excepted that the neural network, rather than using the original features, is using new features, computed by the hidden unit. More details on the vector implementation can be founded [here](https://share.coursera.org/wiki/index.php/ML:Neural_Networks:_Representation#Model_Representation_II).

### Examples and Intuitions I

It is easy to build AND and OR function using simple single-layer neural network:

AND: If $$\Theta^{1}$$ = \begin{bmatrix} -30 & 20 & 20 \end{bmatrix}$$, then $$h_\Theta(x) = g(-30 + 20x_1 + 20x_2)$$. The thruth table is:
| $$x_1$$ | $$x_2$$ | h_\Theta(x)          |
|:-------:|---------|----------------------|
| 0       | 0       | $$g(-30) \approx 0$$ |
| 0       | 1       | $$g(-10) \approx 0$$ |
| 1       | 0       | $$g(-10) \approx 0$$ |
| 1       | 1       | $$g(10) \approx 1$$  |

