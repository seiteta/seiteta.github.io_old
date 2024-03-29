---
layout: post
permalink: /ml-notes.html
title: 🏫 MOOC Machine Learning – notes
author: Frédéric Bardolle
---

My notes from the [Machine Learning class](https://www.coursera.org/course/ml), taught by Andrew Ng from Stanford on Coursera. See also this [wiki](https://share.coursera.org/wiki/index.php/ML:Main).

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

$$\theta_1 := \theta_1 - \alpha \dfrac{1}{m} \sum_{i=1}^{m} \left (h_\theta (x^{(i)}) - y^{(i)} \right)\cdot x^{(i)}$$

and simultaneously update $$\theta_0$$ and $$\theta_1$$.

## III. Linear Algebra Review (Week 1)

 
![matrices luv](https://media.giphy.com/media/ohdY5OaQmUmVW/giphy.gif)

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

$$h_\theta (x) = \begin{bmatrix} \theta_0 &\theta_1 & ... & \theta_n \end{bmatrix} + \begin{bmatrix} x_0 \\ x_1 \\ \vdots \\ x_n\end{bmatrix} = \theta^T x$$

$$\theta = \begin{bmatrix} \theta_0 \\ \theta_1 \\ \vdots \\ \theta_n \end{bmatrix}$$ is a parameter vector.

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

One last thing: using the normal equation does not require any feature scaling.

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

### Model Representation I & II

$$\theta$$ parameters are sometimes called "weights" in the neural networks model. The first layer is called the "input layer", the last is called "output layer" and the layers in-between are called "hidden layers".

* $$a_i^{j}$$ is the activation of the unit $$i$$ in the layer $$j$$.
* Parameters are represented in $$\Theta^{j}$$, a matrix of weights controlling the mapping from a layer $$j$$ to a layer $$j+1$$.
* If network has $$s_j$$ units in layer $$j$$ and $$s_{j+1}$$ units in layer $$j+1$$, then $$\Theta^{j}$$ will be of dimension $$s_{j+1}×(s_{j}+1)$$.

Considering only the last hidden unit and the output unit, we are doing exactly the same thing as we did in logistic regression, excepted that the neural network, rather than using the original features, is using new features, computed by the hidden unit. More details on the vector implementation can be founded [here](https://share.coursera.org/wiki/index.php/ML:Neural_Networks:_Representation#Model_Representation_II).

* To compute the activations in the layer $$j$$, first we compute $$z^{(j)} = \Theta^{(j-1)}a^{(j-1)}$$
* And then we apply the sigmoid function: $$a^{(j)} = g(z^{(j)})$$

### Examples and Intuitions I & II

It is easy to build AND and OR function using simple single-layer neural network:

* AND: If $$\Theta^{1} = \begin{bmatrix} -30 & 20 & 20 \end{bmatrix}$$, then $$h_\Theta(x) = g(-30 + 20x_1 + 20x_2)$$:

| $$x_1$$ | $$x_2$$ |    $$h_\Theta(x)$$   |
|:-------:|:-------:|:--------------------:|
|  $$0$$  |  $$0$$  | $$g(-30) \approx 0$$ |
|  $$0$$  |  $$1$$  | $$g(-10) \approx 0$$ |
|  $$1$$  |  $$0$$  | $$g(-10) \approx 0$$ |
|  $$1$$  |  $$1$$  |  $$g(10) \approx 1$$ |
|         |         |                      |

* OR: If $$\Theta^{1} = \begin{bmatrix} -10 & 20 & 20 \end{bmatrix}$$, then $$h_\Theta(x) = g(-10 + 20x_1 + 20x_2)$$:

| $$x_1$$ | $$x_2$$ |    $$h_\Theta(x)$$   |
|:-------:|:-------:|:--------------------:|
|  $$0$$  |  $$0$$  | $$g(-10) \approx 0$$ |
|  $$0$$  |  $$1$$  |  $$g(10) \approx 1$$ |
|  $$1$$  |  $$0$$  |  $$g(10) \approx 1$$ |
|  $$1$$  |  $$1$$  |  $$g(30) \approx 1$$ |
|         |         |                      |

It is possible to build more complicated function (XNOR for example) by adding an hidden layer.

### Multiclass Classification

To do multiclass classification, we [one-hot](https://en.wikipedia.org/wiki/One-hot) encode the resulting classes.


## IX. Neural Networks: Learning (Week 5)

### Cost Function

The neural network cost function is a generalization of the one we used for logistic regression. With $$L$$ the number of layers, $$s_l$$ the number of units (not counting bias unit) in layer $$l$$ and $$K$$ the number of output units/classes:

$$J(\Theta) = - \frac{1}{m} \left[ \sum_{i=1}^m \sum_{k=1}^K y^{(i)}_k \log ((h_\Theta (x^{(i)}))_k) + (1 - y^{(i)}_k)\log (1 - (h_\Theta(x^{(i)}))_k)\right] + \frac{\lambda}{2m}\sum_{l=1}^{L-1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_{l+1}} ( \Theta_{j,i}^{(l)})^2$$

### Backpropagation Algorithm

Since we try to minimize $$J(\Theta)$$, we will need to compute $$J(\Theta)$$ and $$\dfrac{\partial}{\partial \Theta_{i,j}^{(l)}}J(\Theta)$$.

For each example in the training set, we have to do a forward propagation to compute the activation values, then do a backward propagation to compute the $$\delta_j^{(l)}$$ ("error" of node $$j$$ in layer $$l$$) which are added in an "accumulator": $$\Delta^{(l)}_{i,j} := \Delta^{(l)}_{i,j} + a_j^{(l)} \delta_i^{(l+1)}$$.

More details in the [wiki](https://share.coursera.org/wiki/index.php/ML:Neural_Networks:_Learning#Backpropagation_Algorithm).

### Backpropagation Intuition

Computation of an activation weight (forward propagation): first, compute $$ z_1^{(3)} =  \Theta^{(2)}_{10} * 1 + \Theta^{(2)}_{11} * a_1^{(2)} + \Theta^{(2)}_{12} * a_2^{(2)}$$ and then $$a_1^{(3)} = g(z_1^{(3)})$$.

Computation of $$\delta$$ "errors" are very similar (backward propagation): for example $$\delta_2^{(2)} = \Theta^{(2)}_{12} * \delta_1^{(3)} + \Theta^{(2)}_{22} * \delta_2^{(3)} $$

### Implementation Note: Unrolling Parameters

Optimization algorithms expect vectors for theta and gradient. However, in neural networks, theta and gradient are matrices. In order to use optimizing functions such as `fminunc()`, we will want to "unroll" all the elements and put them into one long vector:

{% highlight matlab %}
thetaVector = [ Theta1(:); Theta2(:); Theta3(:); ]
deltaVector = [ D1(:); D2(:); D3(:) ]
{% endhighlight %}

If the dimensions of Theta1 is 10x11, Theta2 is 10x11 and Theta3 is 1x11, then we can get back our original matrices from the "unrolled" versions as follows:

{% highlight matlab %}
Theta1 = reshape(thetaVector(1:110),10,11)
Theta2 = reshape(thetaVector(111:220),10,11)
Theta3 = reshape(thetaVector(221:231),1,11)
{% endhighlight %}

### Gradient Checking

Backpropagation is tricky to implement. To ensure that everything works fine, we can compute a numerical estimation of the gradient and compare it to the gradient calculated with backpropagation. The derivative of the cost function is :

$$\dfrac{\partial}{\partial\Theta}J(\Theta) \approx \dfrac{J(\Theta + \epsilon) - J(\Theta - \epsilon)}{2\epsilon}$$

And for $$\Theta_j$$:

$$\dfrac{\partial}{\partial\Theta_j}J(\Theta) \approx \dfrac{J(\Theta_1, \dots, \Theta_j + \epsilon, \dots, \Theta_n) - J(\Theta_1, \dots, \Theta_j - \epsilon, \dots, \Theta_n)}{2\epsilon}$$

Which can be implemented as:

{% highlight matlab %}
epsilon = 1e-4; % value recommended in the course
for i = 1:n,
  thetaPlus = theta;
  thetaPlus(i) += epsilon;
  thetaMinus = theta;
  thetaMinus(i) -= epsilon;
  gradApprox(i) = (J(thetaPlus) - J(thetaMinus))/(2*epsilon)
end;
{% endhighlight %}

Note: gradient checking is only use in debugging. It should be turned off when we train the model because it is a very slow algorithm.

### Random Initialization

If we initialize all the parameters at $$0$$, every activation weigths (in their respective layer) wil be the same. Each parameter is initialize to a random value between $$[−\epsilon,\epsilon]$$, for example:

{% highlight matlab %}
Theta1 = rand(10,11) * (2 * INIT_EPSILON) - INIT_EPSILON;
{% endhighlight %}

NB: the $$\epsilon$$ used here has nothing to do with gradient checking.


## X. Advice for Applying Machine Learning (Week 6)

### Deciding What to Try Next

If the machine learning model sucks, here is what we can try:

* Getting more training examples
* Trying smaller sets of features
* Trying additional features
* Trying polynomial features
* Increasing or decreasing $$\lambda$$

But we shouldn't pick one of these methods randomly.

### Evaluating a Hypothesis

We train the model on a subset of the original dataset (train set), and we test it on another subset (test set). A typical split: 70% train set and 30% test set. The procedure can be written:

1. Learn $$\Theta$$ and minimize $$J_{train}(\Theta)$$ using the training set
2. Compute the test set error $$J_{train}(\Theta)$$

### Model Selection and Train/Validation/Test Sets

Even better, we can use three subsets: a train set, a cross-validation set and a test set (typical spit: 60/20/20). We train the model with the train set, and select which is the best one with the cross-validation set. Then, we can estimate the generalization error using the test set.

### Diagnosing Bias vs. Variance

In a nutshell, high bias = underfitting ; high variance = overfitting.

![bias-vs-variance](/downloads/bias-vs-variance.png "Bias vs variance")

### Regularization and Bias/Variance

To choose the "just right" value for $$\lambda$$ (not too low, not too large), we try different values, and evaluate the cost function on the cross-validation set (/!\ without the regularization term).

![lambda-vs-hypothesis](/downloads/lambda-vs-hypothesis.png "Lambda vs hypothesis")

### Learning Curves

If a learning algorithm is suffering from high bias, getting more training data will not (by itself) help much.

![learning-curves](/downloads/learning-curves.png "Learning curves")

On the other hand, if a learning algorithm is suffering from high variance, getting more training data is likely to help.

![learning-curves2](/downloads/learning-curves2.png "Learning curves 2")

### Deciding What to Do Next (Revisited)

Fixes high variance:

* Getting more training examples
* Trying smaller sets of features
* Increasing $$\lambda$$

Fixes high bias:

* Adding features
* Adding polynomial features
* Decreasing $$\lambda$$

About neural networks: small neural networks are prone to underfitting but computationally cheaper. Large neural networks are prone to overfitting and computationally more expensive (use regularization to adress overfitting).

## XI. Machine Learning System Design (Week 6)

### Prioritizing What to Work On
What to do when we face a new problem? Collects more data? Develop sophisticated features? Develop sophisticated algorithm?

### Error Analysis
The recommended approach is :

* Start with a simple algorithm, implement it quickly, and test it early
* Plot learning curves to decide if more data, more features, etc. will help
* Error analysis: manually examine the errors on examples in the cross validation set and try to spot a trend

To test new ideas, it is also important to get error results as a single numerical value, in order to assess the algorithm's performance.

### Error Metrics for Skewed Classes

If classes are skewed, only having the error result is not enough. To solve this problem, we use the confusion matrix:

|           |   |    Confusion   |     matrix     |
|:---------:|:-:|:--------------:|:--------------:|
|           |   |     Actual     |      class     |
|           |   |        1       |        0       |
| Predicted | 1 |  True positive | False positive |
|   class   | 0 | False negative |  True negative |
|           |   |                |                |

Then, we calculate new metrics (example with cancer prediction):

* Precision: of all patients we predicted where $$y=1$$, what fraction actually has cancer? $$\text{precision} = \dfrac{TP}{TP+FP}$$
* Recall: Of all the patients that actually have cancer, what fraction did we correctly detect as having cancer? $$\text{recall} = \dfrac{TP}{TP+FN}$$

### Trading Off Precision and Recall

We might want a confident prediction (i.e. predict cancer if very confident): high precision but low recall. But if we want safe prediction (i.e. avoid false negative): high recall but low precision.

To have a single number out of these metrics, we can use the F-score:

$$\text{F-score} = 2\dfrac{PR}{P + R}$$

Side note: we want to train precision and recall on the cross validation set so as not to bias our test set.

### Data for Machine Learning

When to use do you need more data? 

A useful test is: given input $$x$$, would a human expert be able to confidently predict $$y$$? For example, you can't predict the housing price from only size.

The best models have low bias (many useful features or many parameters) and low variance (lots of data).

## XII. Support Vector Machines (Week 7)

### Optimization Objective

The Support Vector Machine (SVM) is another type of supervised machine learning algorithm. Its cost function is:

$$J(\theta) = C\sum_{i=1}^m y^{(i)} \ \text{cost}_1(\theta^Tx^{(i)}) + (1 - y^{(i)}) \ \text{cost}_0(\theta^Tx^{(i)}) + \dfrac{1}{2}\sum_{j=1}^n \Theta^2_j$$

with $$z = \theta^Tx$$, $$\text{cost}_0(z) = \max(0, k(1+z))$$ and \text{cost}_1(z) = \max(0, k(1-z)).

It can be seen as a modification of the logistic regression algorithm, with $$C = \dfrac{1}{\lambda}$$ and [hinge loss](https://en.wikipedia.org/wiki/Hinge_loss) functions instead of $$log$$ functions. The output of SVM is either $$0$$ or $$1$$, not probability like logistic regression.

### Large Margin Intuition

In SVMs, the decision boundary is as far away as possible from both the positive and the negative examples. The distance of the decision boundary to the nearest example is called the margin. Since SVMs maximize this margin, it is often called a Large Margin Classifier (when $$C$$ is large). If we have outlier examples that we don't want to affect the decision boundary, then we can reduce $$C$$. Increasing and decreasing $$C$$ is similar to respectively decreasing and increasing $$\lambda$$, and can simplify our decision boundary.

### Mathematics Behind Large Margin Classification

![inner product luv](https://media.giphy.com/media/ohdY5OaQmUmVW/giphy.gif)

### Kernels I

Kernels allow us to make complex, non-linear classifiers using SVMs. The idea is to measure the proximity of our training examples $$x_j$$ with several landmarks $$l^{(i)}_{j}$$. The most common kernel is the Gaussian kernel:

$$f_i = \exp(-\dfrac{||x - l^{(i)}||^2}{2\sigma^2})$$

$$\sigma^2$$ is a parameter of the Gaussian kernel that can be modified to increase or decrease the drop-off. 

### Kernels II

Practically, $$m$$ landmarks are put in the exact same locations as all the $$m$$ training examples. We can generate a feature vector containing all the similarities $$f^{(i)}$$. To get the parameters $$\Theta$$ we can use the SVM minimization algorithm but with $$f^{(i)}$$ substituted in for $$x^{(i)}$$:

$$\min_{\Theta} C \sum_{i=1}^m y^{(i)}\text{cost}_1(\Theta^Tf^{(i)}) + (1 - y^{(i)})\text{cost}_0(\theta^Tf^{(i)}) + \dfrac{1}{2}\sum_{j=1}^n \Theta^2_j$$

* Large C: high variance, low bias
* Small C: low variance, high bias
* Large $$\sigma^2$$: low variance, high bias
* Small $$\sigma^2$$: high variance, low bias

### Using An SVM

Good SVM libraries exist, use them! Reminder: $$n$$ is the number of features, $$m$$ is the number of data.

* If $$n$$ is large (10,000) and $$m$$ is small (10 – 1,000), then use logistic regression, or SVM without a kernel (aka linear kernel)
* If $$n$$ is small (10 – 1,000) and $$m$$ is intermediate (10 – 10,000), then use SVM with a Gaussian kernel
* If $$n$$ is small (10 – 1,000) and $$m$$ is large (50,000+), then create features, and use logistic regression or SVM without a kernel.

A neural network is likely to work well for any of these situations, but may be slower to train.

## XIII. Clustering (Week 8)

### Unsupervised Learning: Introduction

Unsupervised learning deals with unlabeled data ($$x^{(i)}$$ without corresponding $$y^{(i)}$$).

### K-Means Algorithm

The K-Means Algorithm is a widely used algorithm for automatically grouping data into coherent subsets. For $$K=2$$, steps are:

1. Randomly initialize two points in the dataset called the cluster centroids.
2. Cluster assignment: assign all examples into one of two groups based on which cluster centroid the example is closest to.
3. Move centroid: compute the averages for all the points inside each of the two cluster centroid groups, then move the cluster centroid points to those averages.
4. Re-run (2) and (3) until we have found our clusters.

In pseudo-code:

{% highlight text %}
Randomly initialize K cluster centroids mu(1), mu(2), ..., mu(K)
Repeat:
   for i = 1 to m:
      c(i) := index (from 1 to K) of cluster centroid closest to x(i)
   for k = 1 to K:
      mu(k) := average (mean) of points assigned to cluster k
{% endhighlight %}

The first for-loop is the "cluster assignment" step:

$$c^{(i)} = argmin_k\ ||x^{(i)} - \mu_k||^2$$

The second for-loop is the "move centroid":

$$\mu_k = \dfrac{1}{n}[x^{(k_1)} + x^{(k_2)} + \dots + x^{(k_n)}]$$

### Optimization Objective

The cost function to be minimized is:

$$J(c^{(i)},\dots,c^{(m)},\mu_1,\dots,\mu_K) = \dfrac{1}{m}\sum_{i=1}^m ||x^{(i)} - \mu_{c^{(i)}}||^2$$

This cost function always decreases.

### Random Initialization

Usually, the initialization is done by setting the cluster centroids equal to $$K$$ unique training examples. Since K-Means can get stuck in local optima, we should run the algorithm on many different random initializations.

### Choosing the Number of Clusters

One way to choose $$K$$ is the elbow method: plot the cost $$J$$ and the number of clusters $$K$$. The cost function should reduce as we increase the number of clusters, and then flatten out. Choose $$K$$ at the point where the cost function starts to flatten out. However, fairly often, the curve is very gradual, so there's no clear elbow.

Another way to choose $$K$$ is to observe how well K-Means performs on a downstream purpose. In other words, we choose $$K$$ that proves to be most useful for some goal we are trying to achieve from using these clusters.

## XIV. Dimensionality Reduction (Week 8)

### Motivation I: Data Compression

We may want to reduce the dimension of our features if we have a lot of redundant data. Dimensionality reduction reduces the number of features but not than the number of examples.

### Motivation II: Visualization

Since it is not easy to visualize data that is more than three dimensions, we can reduce the dimensions of our data to 3 or less in order to plot it.

### Principal Component Analysis Problem Formulation

The goal of PCA is to reduce the projection error, i.e. the average of all the distances of every feature to the projection line (or plane).

PCA is not linear regression: 

* In linear regression, we are minimizing the squared error from every point to our predictor line and these are vertical distances.
* In PCA, we are minimizing the shortest orthogonal distances to our data points.

### Principal Component Analysis Algorithm

* Mean normalization and feature scaling (last one optional)
* Compute the covariance matrix $$\Sigma = \dfrac{1}{m}\sum^m_{i=1}(x^{(i)})(x^{(i)})^T$$:

{% highlight matlab %}
Sigma = (1/m) * X' * X;
{% endhighlight %}

* Compute the eigenvectors of the covariance matrix $$\Sigma$$:

{% highlight matlab %}
[U,S,V] = svd(Sigma);
{% endhighlight %}

* Take the first $$k$$ columns of the $$U$$ matrix and compute $$z$$:

{% highlight matlab %}
Ureduce = U(:,1:k);
Z = X * Ureduce;   
{% endhighlight %}

### Reconstruction from Compressed Representation

To reconstructe our data from their compressed representation, we can use the following equation: $$x_{approx}^{(1)} = U_{reduce} \cdot z^{(1)}$$

### Choosing the Number of Principal Components

To choose $$k$$ (the number of principal components), we can look at the retained variance (here 99% of the variance is retained.):

$$\dfrac{\dfrac{1}{m}\sum^m_{i=1}||x^{(i)} - x_{approx}^{(i)}||^2}{\dfrac{1}{m}\sum^m_{i=1}||x^{(i)}||^2} \leq 0.01$$

The numerator is the average squared projection error and the denominator is the total variation in the data. Instead of calculating this formula for every $$k$$, we can use the $$S$$ matrix computed when we call the `svd` function and compute $$\dfrac{\sum_{i=1}^kS_{ii}}{\sum_{i=1}^nS_{ii}} \geq 0.99$$.

### Advice for Applying PCA

Two main applications:

* Compressions (to reduce data space or speed up the algorithm)
* Visualization of data (with $$k = 2$$ or $$k = 3$$)

Two warnings:

* PCA reduction should be used on the training set and not on the cross-validation or test sets.
* PCA reduction should not be used prevrent overfitting (regularization is most effective and doesn't lost so much information).


## XV. Anomaly Detection (Week 9)

### Problem Motivation

We are given a dataset and we want to know whether a new example is anomalous. We define a model $$p(x)$$ that tells us the probability the example is not anomalous and a threshold $$\epsilon$$ as a dividing line so we can say which examples are anomalous and which are not.

Anomalous examples are the $$x$$ for which $$p(x)<\epsilon$$. If our anomaly detector is flagging too many anomalous examples, then we need to decrease our threshold $$\epsilon$$

### Gaussian Distribution

The probability distribution function of the Gaussian distribution is:

$$p(x;\mu,\sigma^2) = \dfrac{1}{\sigma\sqrt{(2\pi)}}e^{-\dfrac{1}{2}\left(\dfrac{x - \mu}{\sigma}\right)^2}$$

If a dataset follows a Gaussian distribution, we can estimate $$\mu$$ and $$\sigma^2$$ with $$\mu = \dfrac{1}{m}\displaystyle \sum_{i=1}^m x^{(i)}$$ and $$\sigma^2 = \dfrac{1}{m}\displaystyle \sum_{i=1}^m\left(x^{(i)} - \mu\right)^2$$.

### Algorithm

1. Choose features $$xi$$ that you think might be indicative of anomalous examples.
2. For $$j=1$$ to $$n$$, calculate $$\mu_j = \dfrac{1}{m}\displaystyle \sum_{i=1}^m x_j^{(i)}$$ and $$\sigma^2_j = \dfrac{1}{m}\displaystyle \sum_{i=1}^m\left(x_j^{(i)} - \mu_j\right)^2$$
3. Given a new example x, compute p(x): $$p(x) = \displaystyle \prod^n_{j=1} p(x_j;\mu_j,\sigma_j^2) = \prod\limits^n_{j=1} \dfrac{1}{\sigma_j\sqrt{(2\pi)}}e^{-\dfrac{1}{2}\left(\dfrac{x_j - \mu_j}{\sigma_j}\right)^2}$$
4. Anomaly if $$p(x) < \epsilon$$

### Developing and Evaluating an Anomaly Detection System

1. Fit model $$p(x)$$ on training set $$\lbrace x^{(1)},\dots,x^{(m)} \rbrace$$
2. On a cross validation/test example $$x$$, predict: $$y=1$$ if $$p(x)<\epsilon$$ (anomaly) or $$y=0$$ if $$p(x)≥\epsilon$$ (normal)

Non-anomalous (negative i.e. $$y=0$$) examples are split 60/20/20 between the training, CV and test sets. Anomalous (positive i.e. $$y=1$$) examples are split 50/50 between the CV and test sets.

Several evaluation metrics can be used: TP, FP, FN, TN, precision, recall or F-score. Accuracy can't be used because classes are highly skewed.

### Anomaly Detection vs. Supervised Learning

We should use anomaly detection when :

 * we have a very small number of positive examples and a large number of negative (y=0) examples.
 * we have many different "types" of anomalies and future anomalies may look nothing like any of the anomalous examples we've seen so far.

We should use supervised learning when:

* we have a large number of both positive and negative examples.
* we have enough positive examples for the algorithm to get a sense of what new positives examples look like and future positive examples are likely similar to the ones in the training set.

### Choosing What Features to Use

If some features are not distributed as gaussian distribution, we can apply some transform, like $$\log(x + c_1)$$ or $$x^{c_2}$$.

If the algorithm performs poorly, we should find features with large $$p(x)$$ for normal examples and small $$p(x)$$ for anomalous examples, by figuring out new features that will better distinguish the data.

### Multivariate Gaussian Distribution

If features are correlated, gaussian distributions don't work very well because their contours are always rounds. Instead, we can use multivariate gaussian distributions (an extension of gaussian distributions) because their contours can be ellpsises. Their equation is:

$$p(x;\mu,\Sigma) = \dfrac{1}{(2\pi)^{n/2} |\Sigma|^{1/2}} exp(-1/2(x-\mu)^T\Sigma^{-1}(x-\mu))$$

The covariance matrix $$\Sigma$$ changes the shape, $$\mu$$ changes the center.

### Anomaly Detection using the Multivariate Gaussian Distribution

We can fit the model $$p(x)$$ by calculating the parameters $$\mu$$ and $$\Sigma$$:

$$\mu = \dfrac{1}{m}\displaystyle \sum_{i=1}^m x^{(i)}$$

$$\Sigma = \dfrac{1}{m}\sum^m_{i=1}(x^{(i)}-\mu)(x^{(i)}-\mu)^T$$

Then, we can flag an anomaly if $$p(x) < \epsilon$$.

Gaussian distribution models are a special case of multivariate gaussian distribution model. In gaussian distribution models, the covariance matrix is a diagonal matrix, so there is no matrix to inverse. Hence, these models are computationally cheaper and we don't need to have $$m \gg n$$ (more training example than features). The problem is they don't automatically capture correlations between features, so we have to build our own features.


## XVI. Recommender Systems (Week 9)

### Problem Formulation

Recommendation is a very popular application of machine learning. For example we can recommend movies to customer, with the following definitions:

* $$n_u$$= number of users
* $$n_m$$= number of movies
* $$r(i,j)=1$$ if user $$j$$ has rated movie $$i$$
* $$y(i,j)=$$ rating given by user $$j$$ to movie $$i$$ (defined only if $$r(i,j)=1$$)

### Content Based Recommendations

We can introduce some features $$x^{i}$$ describing the movie $$i$$. Then, we can try to find a parameter $$\theta^{(j)}$$ for each user $$j$$. This is in fact a linear regression problem. For the user $$j$$, we are looking for:

$$min_{\theta^{(j)}} = \dfrac{1}{2}\displaystyle \sum_{i:r(i,j)=1} ((\theta^{(j)})^T(x^{(i)}) - y^{(i,j)})^2 + \dfrac{\lambda}{2} \sum_{k=1}^n(\theta_k^{(j)})^2$$

For all the users, it is:

$$min_{\theta^{(1)},\dots,\theta^{(n_u)}} = \dfrac{1}{2}\displaystyle \sum_{j=1}^{n_u} \sum_{i:r(i,j)=1} ((\theta^{(j)})^T(x^{(i)}) - y^{(i,j)})^2 + \dfrac{\lambda}{2} \sum_{j=1}^{n_u} \sum_{k=1}^n(\theta_k^{(j)})^2$$

We can solve these equation with our traditional gradient descent method.

### Collaborative Filtering

If we suppose we know the parameters $$\theta^{(j)}$$, we can do a linear regression to find the features $$x^{i}$$:

$$min_{x^{(1)},\dots,x^{(n_m)}} \dfrac{1}{2} \displaystyle \sum_{i=1}^{n_m} \sum_{j:r(i,j)=1} ((\theta^{(j)})^T x^{(i)} - y^{(i,j)})^2 + \dfrac{\lambda}{2}\sum_{i=1}^{n_m} \sum_{k=1}^{n} (x_k^{(i)})^2$$

In fact, we can randomly guess the values for $$\theta$$ to guess the features $$x$$, then $$\theta$$, then $$x$$ and so on, and we will actually converge to a good set of features.

### Collaborative Filtering Algorithm

Instead, we can simultaneously minimize features and parameters:

$$J(x,\theta) = \dfrac{1}{2} \displaystyle \sum_{(i,j):r(i,j)=1}((\theta^{(j)})^Tx^{(i)} - y^{(i,j)})^2 + \dfrac{\lambda}{2}\sum_{i=1}^{n_m} \sum_{k=1}^{n} (x_k^{(i)})^2 + \dfrac{\lambda}{2}\sum_{j=1}^{n_u} \sum_{k=1}^{n} (\theta_k^{(j)})^2$$

The algorithm is:

1. Initilize $$x^{(i)},...,x^{(n_m)},\theta^{(1)},...,\theta^{(n_u)}$$ to small random values (to break symmetry).
2. Minimize $$J(x^{(i)},...,x^{(n_m)},\theta^{(1)},...,\theta^{(n_u)})$$ with gradient descent. $$x_k^{(i)} := x_k^{(i)} - \alpha\left (\displaystyle \sum_{j:r(i,j)=1}{((\theta^{(j)})^T x^{(i)} - y^{(i,j)}) \theta_k^{(j)}} + \lambda x_k^{(i)} \right)$$ and $$\theta_k^{(j)} := \theta_k^{(j)} - \alpha\left (\displaystyle \sum_{i:r(i,j)=1}{((\theta^{(j)})^T x^{(i)} - y^{(i,j)}) x_k^{(i)}} + \lambda \theta_k^{(j)} \right)$$
3. For a user with parameters $$\theta$$ and a movie with learned features $$x$$, predict a star rating of $$\theta^{T}x$$.

### Vectorization: Low Rank Matrix Factorization

Given matrices $$X$$ (each row containing features of a particular movie) and $$\Theta$$ (each row containing the weights for those features for a given user), the full matrix $$Y$$ of all predicted ratings of all movies by all users is $$Y = X\Theta^T$$.

Predicting how similar two movies $$i$$ and $$j$$ are can be done using the distance between their respective feature vectors $$x$$: $$\left \| x^{(i)} - x^{(j)} \right \|$$. A small distance between two movies means that these two movies are similar.

### Implementation Detail: Mean Normalization

If we use the algorithm as if, new users will have all their predicted movie ranks equal to 0. To change that, for each movie, we can substract its mean rating to its rating: $$\mu_i = \frac{\sum_{j:r(i,j)=1}{Y_{i,j}}}{\sum_{j}{r(i,j)}}$$.

Prediction are now equal to $$(\theta^{(j)})^T x^{(i)} + \mu_i$$ and new users will have their predicted movie ranks equal to each movie mean rating.

## XVII. Large Scale Machine Learning (Week 10)

### Learning with Large Datasets

If our algorithm has high variance when $$m$$ (the number of example) is small, it can benefit from a larger dataset. But doing gradient descent with $$m = 100,000,000$$ would be too slow and we need to use other approaches.

### Stochastic Gradient Descent

In stochastic gradient descent, the cost function is calculated for just one training example at the time (instead of every example for the classic batch gradient descent):

* Step 1, the dataset is randomly shuffled
* Step 2, for $$i = 1\dots m$$, $$\Theta_j := \Theta_j - \alpha (h_{\Theta}(x^{(i)}) - y^{(i)}) \cdot x^{(i)}_j$$

This way, we can make progress in gradient descent without having to scan all $$m$$ training examples first.

The algorithm will be unlikely to converge at the global minimum and will instead wander around it randomly, but usually yields a result that is close enough.

Stochastic gradient descent will usually take 1-10 passes through the data set to get near the global minimum.

### Mini-Batch Gradient Descent

Instead of using all $$m$$ examples as in batch gradient descent, or only 1 example as in stochastic gradient descent, we can use some in-between number of examples $$b$$ (usually between 2 and 100). For example, with $$b = 10$$ and $$m = 1000$$, the algorithm repeats:

* For $$i = 1,11,21,31,\dots,991$$, $$\theta_j := \theta_j - \alpha \dfrac{1}{10} \displaystyle \sum_{k=i}^{i+9} (h_\theta(x^{(k)}) - y^{(k)})x_j^{(k)}$$

Mini-batch gradient descent is usually faster than stochastic gradient descent because it can be vectorized.

### Stochastic Gradient Descent Convergence

In order to choose the learning rate $$\alpha$$ and study the convergence of the algorithm, we can plot the average cost of the hypothesis applied to every 1000 or so training examples. These costs can be computed during the gradient descent iterations.

To converge toward the global minimum we can slowly decrease $$\alpha$$ over time: $$\alpha = \dfrac{C^1}{\text{iteration} + C^2}$$ ($$C^1$$ and $$C^2$$ are constant).

### Online Learning

If a website has a continuous stream of users, we collect some user actions for the features in $$x$$ to predict some behavior $$y$$ and we can run an endless loop that update $$\theta$$ for each individual $$(x,y)$$ pair as we collect them. This way, the model can adapt to new pools of users.

### Map Reduce and Data Parallelism

We can divide up batch gradient descent and dispatch the cost function for a subset of the data to many different machines to train our algorithm in parallel. First, the training set is split into $$z$$ subsets (one for each machine). Then MapReduce 'map' the computation to the $$z$$ machines, and 'reduce' them by calculating:

$$\Theta_j := \Theta_j - \alpha \dfrac{1}{z}(temp_j^{(1)} + temp_j^{(2)} + \cdots + temp_j^{(z)})$$

Linear regression, logistic regression are easily parallelizable. For neural networks, we can compute forward propagation and back propagation on subsets of data on many machines.

## XVII. Photo OCR (Week 11)

### Problem Description and Pipeline

A machine learning pipeline is a system with many components, several of which may use a machine learning.

In this example, the photo OCR pipeline is Photo OCR Pipeline: Image –> Text detection –> Character segmentation –> Character recognition

### Sliding Windows

First, we collect positive and negative examples of a fixed dimension to build a training set for a supervised learning algorithm. The algorithm takes an input image patch and classifies it as either containing a text or not.

Then, we start by taking a rectangular patch of the image and run this image patch through our classifier, as the patch slides through the entire photo. The amount by which we shift the patch each time is a parameter called step-size or stride.

### Getting Lots of Data and Artificial Data

To get a high performance machine learning system we can take a low bias learning algorithm and train it on a massive training set. Artificial data synthesis is an easy way to provide such training set. Date can be created from scratch or can be modified version of a small labeled training set.

When creating artifical data, introduced distortions should represent the type of distortions in the test set. Adding purely random noise usually does not help.

Before getting more data, we should make sure that we have a low bias classifier (by plotting learning curves), for example a neural network with lots of features or hiddent units.

### Ceiling Analysis

Ceiling analysis is used to evaluate each module of the pipeline in terms of potential performance improvement of the entire system. It can help us to decide on which module we should spend our time on. To estimate the performance improvement of each module, we can build manually perfect outputs for each module and see how it affects the overall performance of the system.

## Conclusion

This MOOC was amazing. Thank you very much Andrew Ng!
