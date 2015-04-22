### Schedule

**9:15 am**: [Pair Problem](pair.md)

**9:45 am**: More Model Selection and Regularization

**10:45 am**: Brief overview of `statsmodels` vs. `sklearn` for linear regression.

**12:00 pm**: Lunch!

**1:30 pm**: Best projects ever!

**5:00 pm**: Rest for the weary.


### Further Reading

[Regularized Linear Regression with scikit learn](http://www.datarobot.com/blog/regularized-linear-regression-with-scikit-learn/): This goes over some of the theory we discussed, and shows using regularization on an actual scikit learn example. It uses Lasso instead of Ridge. The only difference between Lasso and Ridge regularization is this: Ridge adds sum of beta squares to the cost, Lasso adds sum of beta absolute values. Other than that functional form, the idea is pretty much the same. The interface of using LinearRegression() or Ridge(alpha) or Lasso(alpha) is also exactly the same.

[Maximum likelihood and regularization](http://ttic.uchicago.edu/~gregory/courses/wis-ml2012/lectures/lect2ho.pdf): These lecture notes from Greg Shakhnarovich go into a bit more detail on model selection, (regularization is in the end) and uses more formal linear algebra notation while presenting the same ideas. It is also useful if you would like to read more on maximum likelihood (the other method of fitting, it is not least squares, but a probability based, Bayesian way of fitting).

[Ten minute video lecture on learning curves](https://www.youtube.com/watch?v=g4XluwGYPaA): Remember: "High bias" is underfitting, "high variance" is overfitting. Andrew Ng builds intuition in how to use learning curves to understand your model.

[Ten minute video lecture on regularization](https://www.youtube.com/watch?v=fx-TqOzjDbM): Another ten minute lecture by Andrew Ng on how the cost function manipulation works in regularization. It helps build intuition.
